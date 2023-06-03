#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Excerpt Helpers module

# When more than one adjective comes before a noun, the 
# adjectives are normally in a particular order. 
# Adjectives which describe opinions or attitudes (e.g. 
# amazing) usually come first, before more neutral, 
# factual ones (e.g. red):

#   She was wearing an amazing red coat.

#   Not: … red amazing coat

# If we don’t want to emphasise any one of the 
# adjectives, the most usual sequence of adjectives is:

# ord | relating to   | examples 
# -----------------------------------------------------
# 1     opinion         unusual, lovely, beautiful
# 2     size            big, small, tall
# 3     phys. quality   thin, rough, untidy
# 4     shape           round, square, rectangular
# 5     age             young, old, youthful
# 6     color           blue, red, pink
# 7     origin          Dutch, Japanese, Turkish
# 8     material        metal, wood, plastic
# 9     type            general-purpose, four-sided, U-shaped
# 10    purpose         cleaning, hammering, cooking


from dataclasses import dataclass, field
from collections import namedtuple
from random import *
from util import *
import re 
import excerpt.bodyparts

MAXSECTIONBUCKETTRIES = 100
BodyPartHistoryQ = HistoryQ(10)

TagExclDict = {"adult": ["teen"],
               "asian": ["cauc","redhead","latin","poc"],
               "bigdick": ["smalldick"],
               "bigtits": ["smalltits"],
               "blonde": ["brunette","darkhair","grayhair","redhead"],
               "brunette": ["blonde","darkhair","grayhair","redhead"],
               "cauc": ["poc","asian","latin","redhead"],
               "college": ["teen","twenties","thirties","middleaged","milf","older"],
               "curvy": ["slender"],
               "darkhair": ["blonde","brunette","grayhair","redhead"],
               "female": ["male"],
               "redhead": ["asian","cauc","latin","poc"],
               "grayhair": ["blonde","brunette","darkhair","redhead"],
               "hairy": ["shaved","trimmed"],
               "latin": ["asian","cauc","redhead","poc"],
               "large": ["small"],
               "loose": ["tight"],
               "male": ["female"],
               "middleaged": ["teen","college","twenties","thirties"],
               "milf": ["teen","college","twenties","young"],
               "narrow": ["wide"],
               "nation": ["race"],
               "older": ["teen","college","twenties","young"],
               "poc": ["cauc","asian","latin","redhead"],
               "plussize": ["slender"],
               "race": ["nation"],
               "redhead": ["blonde","brunette","darkhair","grayhair"],
               "shaved": ["hairy","trimmed"],
               "short": ["tall"],
               "slender": ["curvy","plussize"],
               "slutty": ["virginal"],
               "small": ["large"],
               "smalldick": ["bigdick"],
               "smalltits": ["bigtits"],
               "tall": ["short"],
               "teen": ["adult","college","twenties","thirties","middleaged","milf"],
               "thick": ["thin"],
               "thin": ["thick"],
               "thirties": ["teen","college","twenties","middleaged"],
               "tight": ["loose"],
               "twenties": ["teen","college","middleaged","older","thirties",],
               "trimmed": ["hairy","shaved"],
               "virginal": ["slutty"],
               "wide": ["narrow"],
               "young": ["thirties","middleaged","older","milf"],
              }

AdjMods = WordList(["extremely",
                    "incredibly",
                    "really",
                    "very",])

@dataclass 
class NPParams:
    iNumAdjs: int = 4
    bVaryAdjTags: bool = True
    bEnableSpecials: bool = False
    sColor: str = ""
    AdjList: list = field(default_factory=list)
    ColorList: list = field(default_factory=list)
    NounList: list = field(default_factory=list)

@dataclass 
class TagLists:
    excl: list = field(default_factory=list)
    req: list = field(default_factory=list)
    adj_excl: list = field(default_factory=list)
    adj_req: list = field(default_factory=list)
    adj_extra: list = field(default_factory=list)
    noun_excl: list = field(default_factory=list)
    noun_req: list = field(default_factory=list)

@dataclass
class ParsedUnit:
    sUnit: str = ""
    iPriority: int = 1
    TagList: list = field(default_factory=list)

# =============================
# *** NounPhrase base class ***
# =============================

# This complex class is designed to create noun phrases. For our
# purposes, a noun phrase is a noun that can be proceeded by any
# number of adjectives.

# NounPhrase objects will have lists of nouns and adjectives. 
# The NounPhrase object picks a noun and some adjs at random 
# from those lists, although the choice may be constrained by 
# other parameters. It then strings them together in a way 
# that hopefully makes grammatical sense.

# Words in the word list can have tags which divide them into 
# categories. Ideally in a noun phrase we want different 
# categories for each word. We also don't want to pick words
# whose categories contradict each other. For instance, "big,
# small dog" is a noun phrase we should avoid. "Small, tiny
# dog" is also not great. "Big, friendly brown dog" is a good
# example of a noun phrase.

# A NounPhrase object selects a bunch of adjectives and a
# a noun. It can then use them to form a string that is a
# descriptive phrase, with adjectives separated by commas
# if needed. 

class NounPhrase:
    def __init__(self, Params = None,
                       NotList = None,
                       TLParams = None
                ):
        self._AllUnitLists = {"adj":    {"master": []}, 
                              "color":  {"master": []},
                              "noun":   {"master": [], 
                                         "std": []}
                             }
        self._UnitTags = dict()
        self._DefaultNoun = ""
        self._DefaultAdj = "naked"
          
        self.AdjHistoryQ = HistoryQ(12)
        self.ColorHistoryQ = HistoryQ(12)
        self.NounHistoryQ = HistoryQ(12)
        
        bDoReset = False

        if Params is None:
            Params = NPParams()

        if len(Params.AdjList) > 0:
            self.AdjList(NewAdjList = Params.AdjList, bReset = False)
            bDoReset = True
        if len(Params.ColorList) > 0:
            self.ColorList(NewColorList = Params.ColorList, bReset = False)
            bDoReset = True
        if len(Params.NounList) > 0:
            self.NounList(NewNounList = Params.NounList, bReset = False)
            bDoReset = True


        # Nouns and Adjs have their own specific required and excluded
        # tag lists which they will use if available. Otherwise, they
        # fall back on the general required and excluded tag lists.
        if TLParams is None or not isinstance(TLParams, TagLists):
            #print("WARNING - NounPhrase.init(): TagLists not found, creating new instance")
            TLParams = TagLists()

        if NotList is None:
            NotList = []

        self._iNumAdjs = Params.iNumAdjs
        self._bVaryAdjTags = Params.bVaryAdjTags
        self._EnableSpecials = Params.bEnableSpecials
        self._Color = Params.sColor
        self._AdjList = []
        self._NotList = NotList
        self._Noun = ""
 
        self._AdjExtraTagList = []
        self._AdjExclTagList = []
        self._AdjReqTagList = []
        self._ExclTagList = []
        self._NounExclTagList = []
        self._NounReqTagList = []
        self._ReqTagList = []

        self._PermExclTagList = TLParams.excl
        self._PermReqTagList = TLParams.req
        self._PermNounExclTagList = TLParams.noun_excl
        self._PermNounReqTagList = TLParams.noun_req
        self._PermAdjExclTagList = TLParams.adj_excl
        self._PermAdjReqTagList = TLParams.adj_req

        self._ExtraAdjList = TLParams.adj_extra

        if bDoReset:
            self.Reset("__init()__")

        return

    # *** Reset method ***
    # --------------------

    # Re-select noun and all adjectives
    def Reset(self, sCalledBy, iNumAdjs = None):
        #print("<< Reset called by " + self.__class__.__name__ + "." + sCalledBy + "() >>")
        if iNumAdjs is None:
            iNumAdjs = self._iNumAdjs

        self.ClearAdjList()
        self._Noun = ""

        NounTagList = []
        UsedTagList = []
        if self.NounListLen() > 0:
            # Sets are unique, so we can convert each list 
            # to a set, OR them together, and convert back
            # to a list that is now free of duplicates.
            AdjExclTagList = list(set(self._AdjExclTagList) | set(self._ExclTagList) | set(self._PermAdjExclTagList) | set(self._PermExclTagList))
            
            AdjReqTagList = list(set(self._AdjReqTagList) | set(self._ReqTagList) | set(self._PermAdjReqTagList) | set(self._PermReqTagList))

            NounExclTagList = list(set(self._ExclTagList) | set(self._NounExclTagList) | set(self._PermExclTagList) | set(self._PermNounExclTagList))
            
            NounReqTagList = list(set(self._ReqTagList) | set(self._NounReqTagList) | set(self._PermReqTagList) | set(self._PermNounReqTagList))

            self._Noun = self.GetNewNoun(NotList = self._NotList, ReqTagList = NounReqTagList, ExclTagList = NounExclTagList)
            #print("  ---")
            if self.AdjListLen() > 0:
                for tag in self.GetUnitTags(self._Noun):
                    if not tag in NounTagList:
                        if not tag.lower() == "master":
                            NounTagList.append(tag)

                for nountag in NounTagList:
                    if nountag in TagExclDict:
                        for tag in TagExclDict[nountag]:
                            if not tag in UsedTagList:
                                UsedTagList.append(tag)
       
                LocalReqTagList = AdjReqTagList.copy()
                LocalExclTagList = AdjExclTagList.copy()

                # Parse extra adjs list, add any tags to the parent
                # and to the used tag list
                ParsedExtraAdjList = []
                if not self._ExtraAdjList is None:
                    for adj in self._ExtraAdjList:
                        Unit = self.ParseUnit(adj)
                        sUnit = Unit.sUnit.strip()
                        if sUnit != "":
                            ParsedExtraAdjList.append(sUnit)
                            #self.AddAdj(Unit.sUnit)
                            for tag in Unit.TagList:
                                self.AddUnitTag(sUnit,tag)
                                if not tag in UsedTagList:
                                    UsedTagList.append(tag)
                            if set(UsedTagList).intersection(LocalReqTagList):
                                for newtag in UsedTagList:
                                    if newtag in LocalReqTagList:
                                        LocalReqTagList.remove(newtag)

                # Get color
                if self.GetColor() == "":
                    if self.ColorListLen() > 0:
                        self.Color(self.GetNewColor(NotList = self._NotList + [self._Noun] + self._AdjList, ReqTagList = ["color"], ExclTagList = AdjExclTagList))

                iColorAdjNum = 0
                if not self.GetColor():
                    self.AddAdj(self.GetColor())
                    iColorAdjNum += 1

                for i in range(self._iNumAdjs - iColorAdjNum):
                    sAdj = self.GetNewAdj(NotList = list(set(self._NotList) | set([self._Noun]) | set(self._AdjList)), 
                                          ReqTagList = LocalReqTagList, 
                                          ExclTagList = list(set(LocalExclTagList) | set(UsedTagList)),
                                          bVaryAdjTags = True)
                    if sAdj == "":
                        print("=*= WARNING =*= bodyparts.Reset() unable to get more adjectives.\n")
                        break

                    #if isinstance(self, excerpt.bodyparts.Breasts):
                    #    print("Reset() adj(" + str(i) + ") = " + str(sAdj))

                    NewAdjTags = self.GetUnitTags(sAdj)
                    for tag in NewAdjTags:
                        # Try and pick adjs from different tags if required tags are not set
                        if self._bVaryAdjTags:
                            if not tag == "master" and not tag in UsedTagList:
                                UsedTagList.append(tag)

                        # Avoid choosing adjectives with mutally exclusive tags
                        if tag in TagExclDict:
                            for excltag in TagExclDict[tag]:
                                if not excltag in LocalExclTagList:
                                    LocalExclTagList.append(excltag)
                                    #print("    Detected tag \"" + tag + "\", excluding tags " + str(TagExclDict[tag]))

                    self.AddAdj(sAdj)

                    # If we have required tags, once an adj with one
                    # of the required tags has been used we can stop
                    # worrying about selecting more adjs from that 
                    # tag. 
                    if set(NewAdjTags).intersection(LocalReqTagList):
                        for newtag in NewAdjTags:
                            if newtag in LocalReqTagList:
                                LocalReqTagList.remove(newtag)

                #print("Reset() : Selected _AdjList is " + str(self._AdjList))
                ExtraAdjBucket = ParsedExtraAdjList
                SpecialAdjBucket = []
                AgeAdjBucket = []
                RaceAdjBucket = []
                #HairColorAdjBucket = []
                #EyeColorAdjBucket = []
                HairEyeAdjBucket = []
                ColorAdjBucket = []
                OtherAdjBucket = []
                SuperAdjBucket = []

                if self.GetColor():
                    ColorAdjBucket.append(self.GetColor())

                for adj in self._AdjList:
                    adjtags = self.GetUnitTags(adj)
                    if "special" in adjtags:
                        SpecialAdjBucket.append(adj)
                    elif "race" in adjtags:
                        RaceAdjBucket.append(adj)
                    elif "age" in adjtags:
                        #print("      \"" + adj + "\" is an age adj.")
                        AgeAdjBucket.append(adj)
                    #elif "haircolor" in adjtags:
                    #    HairColorAdjBucket.append(adj)
                    elif "color" in adjtags:
                    #    #print("      \"" + adj + "\" is a color adj.")
                        ColorAdjBucket.append(adj)
                    elif "haircolor" in adjtags or "eyecolor" in adjtags:
                        HairEyeAdjBucket.append(adj)
                    #elif "eyecolor" in adjtags:
                    #    EyeColorAdjBucket.append(adj)
                    elif "super" in adjtags:
                        #print("      \"" + adj + "\" is a superlative adj.")
                        SuperAdjBucket.append(adj)
                    else:
                        #print("      \"" + adj + "\" is a normal adj.")
                        OtherAdjBucket.append(adj)
                AgeAdjBucket.sort(key = str.lower)
                ColorAdjBucket.sort(key = str.lower)
                OtherAdjBucket.sort(key = str.lower)
                SpecialAdjBucket.sort(key = str.lower)
                SuperAdjBucket.sort(key = str.lower)

                self._AdjList = SuperAdjBucket + OtherAdjBucket + HairEyeAdjBucket + ColorAdjBucket + AgeAdjBucket + RaceAdjBucket + SpecialAdjBucket + ExtraAdjBucket

            return

    # *** Alphabetized standard methods ***
    # -------------------------------------

    # Add an adjective to _AdjList
    def AddAdj(self, adj):
        if adj != "":
            self._AdjList.append(adj)
        return

    # Add an adjective to a tag list
    def AddAdjToList(self, sNoun, sListName, iPriority = None):
        self.AddUnitToList(sNoun,sListName,"adj", iPriority = iPriority)
        return

    # Add a noun to a tag list
    def AddNounToList(self, sNoun, sListName, iPriority = None):
        self.AddUnitToList(sNoun,sListName,"noun", iPriority = iPriority)
        return

    # SET the AdjList
    def AdjList(self, NewAdjList, bReset = True):
        self.UnitList(NewAdjList, "adj", bReset)
        return

    # Get the length of the AdjList
    def AdjListLen(self):
        return self.UnitListLen("adj")

    # Add a tag for a specified unit
    def AddUnitTag(self, sUnit, sTag):
        # If a unit does not have a tag list, add an entry
        if not sUnit in self._UnitTags:
             self._UnitTags[sUnit] = []
 
        # No duplicates
        if not sTag in self._UnitTags[sUnit]:
            self._UnitTags[sUnit].append(sTag)

        return

    # Add a unit to a list. Create list if that list doesn't exist.
    def AddUnitToList(self, sUnit, sListName, sType, iPriority = None):
        UnitList = self.GetUnitList(sListName, sType)
        ListDict = self._AllUnitLists[sType.lower()]

        if UnitList is None:
            #create
            self._AllUnitLists[sType.lower()][ListDict]
            #ListDict[sListName] = []

        if iPriority is None:
            iPriority = 1

        if not self.IsUnitInList(sUnit, sListName, sType):
            for i in range(iPriority):
                if not sListName.lower() in ListDict:
                    ListDict[sListName.lower()] = []
                ListDict[sListName.lower()].append(sUnit)

            self.AddUnitTag(sUnit, sListName)

        return

    # Clear the _AdjList
    def ClearAdjList(self):
        self._AdjList = []
        return 

    # SET the color
    def Color(self, color):
        self._Color = color
        return 

    # SET the ColorList
    def ColorList(self, NewColorList, bReset = True):
        self.UnitList(NewColorList, "color", bReset)
        return 

    # Get the length of the ColorList
    def ColorListLen(self):
        return self.UnitListLen("color")
     
    # SET the default adj
    def DefaultAdj(self, NewAdj = None):
        if NewAdj == None:
            NewAdj = ""
               
        self._DefaultAdj = NewAdj 

        return

    # SET the default noun
    def DefaultNoun(self, NewNoun = None):
        if NewNoun == None:
            NewNoun = ""
               
        self._DefaultNoun = NewNoun 

        return

    # Get a randomly-selected adj from the _AdjList
    def GetRandomAdj(self):
        return choice(self._AdjList)

    # Get a specified adj from the _AdjList
    def GetAdj(self, inum):
        sAdj = ""
        if inum >= 0 and inum < len(self._AdjList):
            sAdj = self._AdjList[inum]
        
        return sAdj

    # Get two adjectives for use in sentences like
    # "the noun was adj1 and adj2." The adjectives
    # will be selected from the second or third 
    # order adj in the adj list, plus one later adj.
    def GetAdjPair(self):
        AdjPair = ["",""]

        DescWordList = self.GetDescWordList()
        iWord1 = 0
        iWord2 = 0

        # The first words in the word list, the noun & 
        # first order adj, cannot be used as part of this
        # pair. If there are 4 or more words, this pair 
        # will be 3 & 4. If there are only 3, this pair 
        # will be 3 and a blank.
        if len(DescWordList) > 3:
            if len(DescWordList) == 4:
                iWord1 = -3 
            else:
                iWord1 = choice([-3,-4])
            iWord2 = -1 * randint(-1 * (iWord1 - 1), len(DescWordList))
            
            # Gerunds only really sound good in Word1.
            # So if we have one in Word2, let's pick a
            # different word.
            iCounter = 0
            while iWord2 >= -1 * len(DescWordList) and iCounter < 20:
                if len(DescWordList[iWord2]) > 3 and DescWordList[iWord2][-3:].lower() == "ing":
                    pass
                elif len(DescWordList[iWord2]) > 4 and DescWordList[iWord2][-4:].lower() == "able":
                    pass
                else: 
                    break
                iWord2 = -1 * randint(-1 * (iWord1 - 1), len(DescWordList))
                iCounter += 1

        elif len(DescWordList) == 3:
            iWord1 = -3
        
        if not iWord2 == 0:
            AdjPair[0] = DescWordList[iWord2]
        if not iWord1 == 0:
            AdjPair[1] = DescWordList[iWord1]

        return AdjPair

        # The adjs are returned in reversed order
        return [iWord2, iWord1]

    # Get the AdjList
    def GetAdjList(self, sListName = None):
        if sListName is None:
            sListName = "master"
        return self.GetUnitList(sListName, "adj") 

    # Get the color
    def GetColor(self):
        sColor = ""

        if not self._Color is None and isinstance(self._Color, str):
            sColor = self._Color.strip()

        return sColor

    # Get the ColorList
    def GetColorList(self):
        return self.GetUnitList("master", "color") 

    # Get the default adj
    def GetDefaultAdj(self, NotList = None):
        sDefaultAdj = ""
          
        if NotList == None:
            NotList = []

        if self._DefaultAdj not in NotList:
            sDefaultAdj = self._DefaultAdj
               
        return sDefaultAdj

    # Get the default noun
    def GetDefaultNoun(self, NotList = None):
        sDefaultNoun = ""
          
        if NotList == None:
            NotList = []

        if self._DefaultNoun not in NotList:
            sDefaultNoun = self._DefaultNoun
               
        return sDefaultNoun

    # Get all selected adjs and nouns as a list
    def GetDescWordList(self):
        DescWordList = []

        sNoun = self.GetNoun()

        if sNoun != "":
            DescWordList.insert(0, sNoun)
        DescWordList = self._AdjList + DescWordList

        return DescWordList

    # Dumb workaround for when the param = the class name
    # but you need to ref the class not the param
    def GetEmptyTagLists(self):
        return TagLists()

    # Get a new adjective that is not in the current _AdjList but
    # does not conflict with it
    def GetNewAdj(self, NotList = None, 
                  ReqTagList = None, ExclTagList = None, AdjExclTagList = None, AdjReqTagList = None, NounExclTagList = None, NounReqTagList = None,
                  bVaryAdjTags = False):
        sNewAdj = ""
        
        if NotList is None:
            NotList = []

        if AdjExclTagList is None:
            AdjExclTagList = []
        if AdjReqTagList is None:
            AdjReqTagList = []
        if ExclTagList is None:
            ExclTagList = []
        if NounExclTagList is None:
            NounExclTagList = []
        if NounReqTagList is None:
            NounReqTagList = []
        if ReqTagList is None:
            ReqTagList = []

        UsedTagList = []
        if bVaryAdjTags:
            for adj in self._AdjList:
                UsedTagList += self.GetUnitTags(adj)

        sNewAdj = self.GetUnit("adj", 
                               NotList = NotList, ReqTagList = ReqTagList, ExclTagList = list(set(ExclTagList) | set(AdjExclTagList) | set(UsedTagList)))
        
        #for tag in self.GetUnitTags(sNewAdj): 
        #    if not tag.lower() == "master":
        #        self.AddUnitTag(sNewAdj, tag)

        return sNewAdj

    # Get a new color. Does NOT check to see if there is a 
    # currently selected color
    def GetNewColor(self, NotList = None, ReqTagList = None, ExclTagList = None):
        sNewColor = ""
        
        if NotList is None:
            NotList = []

        sNewColor = self.GetUnit("color", NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)
        for tag in self.GetUnitTags(sNewColor): 
            if not tag.lower() == "master":
                self.AddUnitTag(sNewColor, tag)

        return sNewColor

    # Get a new noun that is not the current noun but does not
    # conflict with it.
    def GetNewNoun(self, NotList = None, ReqTagList = None, ExclTagList = None):
        sNewNoun = ""

        if NotList is None:
            NotList = []
        if ReqTagList is None:
            ReqTagList = []
        if ExclTagList is None:
            ExclTagList = []

        if self.NounListLen() > 1 and not self._Noun == "":
            sNewNoun = self.GetUnit("noun", NotList = NotList + [self._Noun], ReqTagList = ReqTagList, ExclTagList = ExclTagList)
        else:
            sNewNoun = self.GetUnit("noun", NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)
        
        for tag in self.GetUnitTags(sNewNoun):
            self.AddUnitTag(sNewNoun, tag)

        return sNewNoun

    # Get the current selected noun
    def GetNoun(self):
        return self._Noun

    # Get the NounList
    def GetNounList(self, sListName = None):
        if sListName is None:
            sListName = "master"
        return self.GetUnitList(sListName, "noun") 

    # Get a unit of any type: adj, noun, or color
    def GetUnit(self, sType, NotList = None, ReqTagList = None, ExclTagList = None):
        sUnit = "" 
        LocalUnitList = []
        #print("      Entered GetUnit()")
         
        if NotList is None:
            NotList = []

        if ReqTagList is None:
            ReqTagList = []

        if ExclTagList is None:
            ExclTagList = []

        HistoryQ = None
        if sType.lower() == "adj":
            HistoryQ = self.AdjHistoryQ 
        elif sType.lower() == "color":
            HistoryQ = self.ColorHistoryQ
        elif sType.lower() == "noun":
            HistoryQ = self.NounHistoryQ

        ExclUnitList = []
        for tag in ExclTagList:
            #print("    Getting word units for " + unitlist)
            if tag.lower() != "master":
                for unit in self.GetUnitList(tag, sType):
                    ExclUnitList.append(unit)
        #print("      ExclUnitList is + " + str(ExclUnitList))

        if not self._EnableSpecials:
            for unit in self.GetUnitList("special", sType):
                ExclUnitList.append(unit)

        # If the req tag list is empty, build the valid unit 
        # selection list from the master list
        if ReqTagList == None or len(ReqTagList) == 0:
            #print("  ReqTagList is empty. Using master list.")
            for unit in self.GetUnitList("master", sType):
                if not unit in ExclUnitList:
                    LocalUnitList.append(unit)
        else:
        # Otherwise, build the valid unit selection list from
        # words with tags in the req list
            for taglistname in ReqTagList:
                #print("  Adding taglist " + taglistname)
                for unit in self.GetUnitList(taglistname, sType):
                    if not unit in ExclUnitList:
                        LocalUnitList.append(unit)

        #print("  LocalUnitList = " + str(LocalUnitList) + "\n")

        if len(LocalUnitList) > 0:
            # First, try with the not list, the excluded 
            # tag list, and the required tag list
            sUnit = WordList(LocalUnitList).GetWord(NotList = list(set(NotList) | set(ExclUnitList)), SomeHistoryQ = HistoryQ)

            if sUnit == "":
                # Second, try with the not list and the required tag list
                print("  GetUnit() could not retrieve word. Trying without excluded tag list.")
                sUnit = WordList(LocalUnitList).GetWord(NotList = NotList, SomeHistoryQ = HistoryQ)

                if sUnit == "":
                    # Third, try with just the not list
                    print("   GetUnit() could not retrieve word. Trying without the required tag list.")
                    sUnit = WordList(self.GetUnitList("master", sType)).GetWord(NotList = NotList, SomeHistoryQ = HistoryQ)

                    #if sUnit == "":
                    #    # Fourth, try without any constraints
                    #    print("   GetUnit() could not retrieve word. Trying without the not list.")
                    #    sUnit == WordList(self.GetUnitList("master", sType)).GetWord()
            #print("  GetUnit() new word is \"" + sUnit + "\"")
        
        return sUnit

    # Get the tags for a specified unit
    def GetUnitTags(self, sUnit):
        UnitTags = [] 

        if sUnit in self._UnitTags:
            UnitTags = self._UnitTags[sUnit]

        return UnitTags

    # Get a list of a specified type (noun, adj, or color)
    def GetUnitList(self, sListName, sType):
        UnitList = []
        ListDict = self._AllUnitLists[sType.lower()]

        if sListName.lower() in ListDict:
            UnitList = ListDict[sListName.lower()]

        return UnitList 

    def GetWasWere(self):
        sVerb = "was"
        if self.IsPlural():
            sVerb = "were"

        return sVerb

    # Return true if specified adj in specified list
    def IsAdjInList(self, sAdj, sListName):
        return self.IsUnitInList(sAdj, sListName, "adj")

    # Return true if specified noun in specified list
    def IsNounInList(self, sNoun, sListName):
        return self.IsUnitInList(sNoun, sListName, "noun")

    # Return true if current noun is plural
    def IsPlural(self):
        bIsPlural = False

        NounTags = self.GetUnitTags(self.GetNoun())
        if 'plur' in NounTags:
            bIsPlural = True

        return bIsPlural

    # Return true if current noun is singular
    def IsSing(self):
        bIsSing = False

        NounTags = self.GetUnitTags(self.GetNoun())
        if 'sing' in NounTags:
            bIsSing = True

        return bIsSing

    # Return true if specified unit word in specified list
    def IsUnitInList(self, sUnit, sListName, sType):
        bIsUnitInList = False 

        UnitList = self.GetUnitList(sListName, sType)
        if not UnitList is None:
            if sUnit.lower() in UnitList:
                bIsUnitInList = True

        return bIsUnitInList

    # SET the currently selected noun
    def Noun(self, noun):
        self._Noun = noun

        return True

    # SET the NounList
    def NounList(self, NewNounList, bReset = True):
        self.UnitList(NewNounList, "noun", bReset)
        #self.Reset("NotList")
        return True

    # Gets the length of the NounList
    def NounListLen(self):
        return self.UnitListLen("noun")

    # Parse a string and extract tags and priority, if any
    def ParseUnit(self, sParse):
        sUnit = ""
        iPriority = 1
        TagList = []

        # clean string
        sUnit = sParse.strip()

        # locate priority
        matchPriority = re.search(r"(?<=[x])([\d]+)", sUnit)
        if matchPriority:
            iPriority = int(matchPriority.group())

        # locate Unit 
        ItemSections = sUnit.split(":")
        sUnitWord = ""
        matchUnit = re.search(r"([x][\d]+)", ItemSections[0])
        if matchUnit:
            sUnitWord = ItemSections[0][0:matchUnit.span()[0]]
        else:
            sUnitWord =  ItemSections[0]
        sUnitWord = sUnitWord.strip()

        # locate tag list 
        matchTags = re.search(r"(?<=[:])([\w\s,]*)", sUnit)
        if matchTags:
            TagList = "".join(matchTags.group().split(" ")).split(",")

        return ParsedUnit(sUnitWord, iPriority, TagList)

    # Generates a descriptive phrase in the format:
    #  "adj noun was adj2 and adj1"
    def PhraseWasAnd(self, NotList = None, TagLists = None):
        sPhrase = ""

        if not NotList is None:
            self.NotList(NotList)

        if not TagLists is None:
            self.UpdateTagLists(TLParams = TagLists)

        DescWordList = self.GetDescWordList()

        if len(DescWordList) > 0:
            # Add the noun 
            sPhrase = DescWordList[-1]

        if len(DescWordList) > 1:
            # Add the 1st order adj
            sPhrase = DescWordList[-2] + " " + sPhrase

        if len(DescWordList) > 2:
            # Add "was" or "were" depending on noun
            # plurality
            sPhrase += " " + self.GetWasWere()

            # Add the adj pair. If there are not enough
            # adjs for a complete pair, only [1] will
            # be used.
            AdjPair = self.GetAdjPair()
            if AdjPair[0] != "":
                sPhrase += " " + AdjPair[0] + " and"
            if AdjPair[1] != "":
                sPhrase += " " + AdjPair[1]

        return sPhrase

    # Remove an adjective from the currently selected adjs (_AdjList)
    # by value
    def RemoveAdj(self, adj):
        bSuccess = False
        if adj in self._AdjList:
            self._AdjList.remove(adj)
            bSuccess = True

        return bSuccess

    # Remove an adj from the currently selected adjs (_AdjList)
    # by index
    def RemoveAdjByNum(self, inum):
        bSuccess = False
        if inum >= 0 and inum < len(self._AdjList):
            self._AdjList.pop(inum)
            bSuccess = True

        return bSuccess

    # Set the tags for a specified unit word
    def SetUnitTags(self, sUnit, TagList):
        self._UnitTags[sUnit] = TagList 

        return True

    # SET a specified unit list (NounList, AdjList, or ColorList)
    def UnitList(self, NewUnitList, sType, bReset = True):
        #print("Entered UnitList()")
        for item in NewUnitList:
            sUnit = ""
            iPriority = 1
            TagList = []

            Unit = self.ParseUnit(item)
            sUnit = Unit.sUnit
            iPriority = Unit.iPriority
            TagList = Unit.TagList

            self.AddUnitToList(sUnit, "master", sType, iPriority)
            #print(" Added \"" + sUnit + "\" to master list.")
            for tag in TagList:
                if tag.strip() != "":
                    self.AddUnitToList(sUnit, tag, sType, iPriority)
                #print(" Added \"" + sUnit + "\" to " + tag + " list.")
               
        if bReset:
            self.Reset("UnitList_" + sType)

        return True

    # Get the length of a specified list (AdjList, NounList, ColorList)
    def UnitListLen(self, sType):
        ListLen = 0 
        ListDict = self._AllUnitLists[sType.lower()]

        ListLen = len(ListDict["master"])

        return ListLen

    # Update any and all tag lists
    def UpdateTagLists(self, TLParams = None):
        if TLParams is None:
            TLParams = TagLists()

        if not TLParams.adj_extra is None and len(TLParams.adj_extra) > 0:
            self.ExtraAdjList(TLParams.adj_extra)

        if not TLParams.adj_excl is None and len(TLParams.adj_excl) > 0:
            self.AdjExclTagList(TLParams.adj_excl)

        if not TLParams.adj_req is None and len(TLParams.adj_req) > 0:
            self.AdjReqTagList(TLParams.adj_req)

        if not TLParams.req is None and len(TLParams.req) > 0:
            self.ReqTagList(TLParams.req)

        if not TLParams.excl is None and len(TLParams.excl) > 0:
            self.ExclTagList(TLParams.excl)

        if not TLParams.noun_excl is None and len(TLParams.noun_excl) > 0:
            self.NounExclTagList(TLParams.noun_excl)

        if not TLParams.noun_req is None and len(TLParams.noun_req) > 0:
            self.NounReqTagList(TLParams.noun_req)

        return 

    # Update any and all tag lists
    def _UpdateTagListsNoReset(self, TLParams = None):
        if TLParams is None:
            TLParams = TagLists()

        if not TLParams.adj_extra is None and len(TLParams.adj_extra) > 0:
            self._ExtraAdjList = TLParams.adj_extra

        if not TLParams.adj_excl is None and len(TLParams.adj_excl) > 0:
            self._AdjExclTagList = TLParams.adj_excl

        if not TLParams.adj_req is None and len(TLParams.adj_req) > 0:
            self._AdjReqTagList = TLParams.adj_req

        if not TLParams.req is None and len(TLParams.req) > 0:
            self._ReqTagList = TLParams.req

        if not TLParams.excl is None and len(TLParams.excl) > 0:
            self._ExclTagList = TLParams.excl

        if not TLParams.noun_excl is None and len(TLParams.noun_excl) > 0:
            self._NounExclTagList = TLParams.noun_excl

        if not TLParams.noun_req is None and len(TLParams.noun_req) > 0:
            self._NounReqTagList = TLParams.noun_req

        return 


    # *** Set the tag lists ***
    # -------------------------

    # SET the excluded tag list (general)
    def ExclTagList(self, TagList):
        self._ExclTagList = TagList
        self.Reset("ExclTagList")
        return True

    # SET the extra adj list
    def ExtraAdjList(self, ExtraAdjList):
        self._ExtraAdjList = ExtraAdjList
        self.Reset("ExtraAdjList")
        return True

    # SET the excluded adj tag list
    def AdjExclTagList(self, TagList):
        self._AdjExclTagList = TagList
        self.Reset("AdjExclTagList")
        return True

    # SET the required adj tag list
    def AdjReqTagList(self, TagList):
        self._AdjReqTagList = TagList
        self.Reset("AdjReqTagList")
        return True

    # SET the excluded noun tag list
    def NounExclTagList(self, TagList):
        self._NounExclTagList = TagList
        self.Reset("NounExclTagList")
        return True

    # SET the required noun tag list
    def NounReqTagList(self, TagList):
        self._NounReqTagList = TagList
        self.Reset("NounReqTagList")
        return True

    # SET the NotList
    def NotList(self, NotList):
        self._NotList = NotList
        self.Reset("NotList")
        return True

    # SET the required tag list (general)
    def ReqTagList(self, TagList):
        self._ReqTagList = TagList
        self.Reset("ReqTagList")
        return True


    # *** Description Methods ***
    # ---------------------------

    # Get selected adjectives and nouns as a comma-separated string
    def GetFullDesc(self, iNumAdjs, bCommas = True):
        sFullDesc = ""
        DescWordList = self._AdjList.copy()

        #print("GetFullDesc(" + str(iNumAdjs) + ") Unfiltered _AdjList = " + str(DescWordList))
        if iNumAdjs < len(DescWordList):
            for i in range(len(DescWordList) - iNumAdjs):
                DescWordList.remove(choice(DescWordList))

        if self.GetNoun() != "":
            DescWordList.append(self.GetNoun())

        if bCommas:
            #print("   DescWordList (filtered) = " + str(DescWordList))
            if len(DescWordList) == 1:
                sFullDesc = DescWordList[0]
            elif len(DescWordList) == 2:
                sFullDesc = DescWordList[0] + " " + DescWordList[1]
            elif len(DescWordList) == 3:
                sFullDesc = ", ".join(DescWordList[:1]) + ", " + " ".join(DescWordList[1:])
            elif len(DescWordList) == 4:
                sFullDesc = ", ".join(DescWordList[:-2]) + ", " + " ".join(DescWordList[-2:])
            else:
                sFullDesc = ", ".join(DescWordList[:-3]) + ", " + " ".join(DescWordList[-3:])
        else:
            sFullDesc = " ".join(DescWordList)

        return sFullDesc

    # Gets a string description of the noun only ("hair")
    def ShortDesc(self, NotList = None, TagLists = None, bSilly = False): #, ExtraAdjList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if not bSilly:
            if TagLists is None:
                TagLists = self.GetEmptyTagLists()
            TagLists.noun_excl.append("silly")

        self.UpdateTagLists(TagLists)

        return self.GetFullDesc(iNumAdjs = 0)
     
    # Gets a string description of one adjective plus the noun ("red hair")
    def MediumDesc(self, NotList = None, TagLists = None, bSilly = False):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if not bSilly:
            if TagLists is None:
                TagLists = self.GetEmptyTagLists()
            TagLists.noun_excl.append("silly")

        self.UpdateTagLists(TagLists)
          
        return self.GetFullDesc(iNumAdjs = 1)
     
    # Gets a string description of 1-3 adjs plus the noun ("long, wavy, red hair")
    def FloweryDesc(self, NotList = None, TagLists = None, bSilly = False):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if not bSilly:
            if TagLists is None:
                TagLists = self.GetEmptyTagLists()
            TagLists.noun_excl.append("silly")

        self.UpdateTagLists(TagLists)
          
        iNumAdjs = choice([1,1,1,2,2,2,2,3])

        return self.GetFullDesc(iNumAdjs = iNumAdjs)
     
    # Chooses either ShortDesc, MediumDesc, or FloweryDesc at random
    def RandomDesc(self, bShortDesc = True, bLongDesc = True, NotList = None, TagLists = None, bSilly = False):
        sRandomDesc = ""
          
        iRand = randint(0, 12)
        if iRand in range(0, 3):
        #short desc if allowed 
            if bShortDesc:
                #use noun from the list or default noun
                if FoundIn(self.GetDefaultNoun(), NotList) or CoinFlip():
                    sRandomDesc = self.ShortDesc(NotList = NotList, TagLists = TagLists, bSilly = bSilly)
                else:
                    sRandomDesc = self.GetDefaultNoun(NotList = NotList)
            else:
                sRandomDesc = self.MediumDesc(NotList = NotList, TagLists = TagLists, bSilly = bSilly)
        elif iRand in range(3,6):
        #medium desc 
            sRandomDesc = self.MediumDesc(NotList = NotList, TagLists = TagLists, bSilly = bSilly)
        else:
        #flowery desc if allowed
            if bLongDesc:
                sRandomDesc = self.FloweryDesc(NotList = NotList, TagLists = TagLists, bSilly = bSilly)
            else:
                sRandomDesc = self.MediumDesc(NotList = NotList, TagLists = TagLists, bSilly = bSilly)
               
        return sRandomDesc

# =============================
# *** SectionSelector class ***
# =============================

# This class allows you to put a bunch of strings into it
# and then get back one at random. Each time you get 
# a string it is removed, so strings will never be
# repeated. Strings can have priorities.

class SectionSelector():
    #class Section():
    #    def init(self, Txt, Priority = GenPriority.Normal):
    #        self.Txt = Txt
    #        self.Priority = Priority

    def __init__(self):
        self.Reset()

    def Reset(self):
        self.SuperHighBucket = []
        self.HighBucket = []
        self.AboveAverageBucket = []
        self.NormalBucket = []
        self.LowBucket = []
        self.LowestBucket = []

        self.iNumSections = 0
        #self.UsedSectionsQ = []

    def AddSection(self, Txt, Priority = GenPriority.Normal):
        Bucket = None

        self.iNumSections += 1

        if Priority == GenPriority.SuperHigh:
            Bucket = self.SuperHighBucket
        elif Priority == GenPriority.High:
            Bucket = self.HighBucket
        elif Priority == GenPriority.AboveAverage:
            Bucket = self.AboveAverageBucket
        elif Priority == GenPriority.Low:
            Bucket = self.LowBucket
        elif Priority == GenPriority.Lowest:
            Bucket = self.LowestBucket
        else:
            Bucket = self.NormalBucket
        
        Bucket.append((self.iNumSections, Txt))
        
        return self.iNumSections

    def GetSection(self):
        SectionTxt = ""
        Section = None

        Bucket = []
        iCount = 0
        while len(Bucket) == 0 and iCount < MAXSECTIONBUCKETTRIES:
            iChance = randint(1, 55) # 1 + 2 + 4 + 8 + 16 + 24 = 56
            
            if iChance == 1:
                Bucket = self.LowestBucket
            elif iChance >= 2 and iChance < 4:      # 2x lowest
                Bucket = self.LowBucket 
            elif iChance >= 4 and iChance < 8:      # 2x low
                Bucket = self.NormalBucket 
            elif iChance >= 8 and iChance < 16:      # 2x normal
                Bucket = self.AboveAverageBucket
            elif iChance >= 16 and iChance < 32:     # 2x above average
                Bucket = self.HighBucket
            elif iChance >= 32 and iChance < 56:     # 1.5x high
                Bucket = self.SuperHighBucket
            else:
                Bucket = self.NormalBucket
                print("=*= WARNING =*= Default bucket (normal) selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.\n")

            iCount = iCount + 1

        if iCount >= MAXSECTIONBUCKETTRIES:
            print("=*= WARNING =*= Maximum attempts to choose a bucket exceeded for " + self.GeneratorClassName + " GetBucket(). Bucket " + str(Bucket) + " accepted by default.\n")

        if len(Bucket) > 0:
            iCount = 0
            Section = choice(Bucket)
            Bucket.remove(Section)
            SectionTxt = Section[1]
        else:
            SectionTxt = ""

        return SectionTxt