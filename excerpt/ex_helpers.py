#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Excerpt Helpers module

from dataclasses import dataclass, field
from collections import namedtuple
from random import *
from util import *
import re 

MAXSECTIONBUCKETTRIES = 100
BodyPartHistoryQ = HistoryQ(10)

TagExclDict = {"bigdick": ["smalldick"],
               "bigtits": ["smalltits"],
               "cauc": ["poc"],
               "college": ["teen","twenties","thirties","middleaged"],
               "female": ["male"],
               "hairy": ["shaved","trimmed"],
               "large": ["small"],
               "loose": ["tight"],
               "male": ["female"],
               "middleaged": ["teen","college","twenties","thirties"],
               "older": ["teen","college","twenties",],
               "poc": ["cauc"],
               "plussize": ["slender"],
               "shaved": ["hairy","trimmed"],
               "short": ["tall"],
               "slender": ["plussize"],
               "slutty": ["virginal"],
               "small": ["large"],
               "smalldick": ["bigdick"],
               "smalltits": ["bigtits"],
               "tall": ["short"],
               "teen": ["college","twenties","thirties","middleaged"],
               "thick": ["thin"],
               "thin": ["thick"],
               "thirties": ["teen","college","twenties","middleaged"],
               "tight": ["loose"],
               "twenties": ["teen","college","thirties","middleaged"],
               "trimmed": ["hairy","shaved"],
               "virginal": ["slutty"],
               "young": ["thirties","middleaged","older"],
              }

@dataclass 
class NPParams:
    iNumAdjs: int = 4
    bVaryAdjTags: bool = True
    bEnableSpecials: bool = False

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
                       #iNumAdjs = 4, 
                       #bVaryAdjTags = True, 
                       #ExtraAdjList = None, 
                       #bEnableSpecials = False,
                       NotList = None,
                       TLParams = None
                ):
        self._AllUnitLists = {"adj": {"master": []}, "noun": {"master": [], "std": []}}
        self._UnitTags = dict()
        self._DefaultNoun = ""
        self._DefaultAdj = "naked"
          
        self.NounHistoryQ = HistoryQ(3)
        self.AdjHistoryQ = HistoryQ(3)

        if Params is None:
            Params = NPParams()

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
        self._AdjList = []
        self._NotList = NotList
        self._Noun = ""
        self._Color = ""

        self._ExclTagList = []
        self._ReqTagList = []
        self._NounExclTagList = []
        self._NounReqTagList = []
        self._AdjExclTagList = []
        self._AdjReqTagList = []

        self._PermExclTagList = TLParams.excl
        self._PermReqTagList = TLParams.req
        self._PermNounExclTagList = TLParams.noun_excl
        self._PermNounReqTagList = TLParams.noun_req
        self._PermAdjExclTagList = TLParams.adj_excl
        self._PermAdjReqTagList = TLParams.adj_req
        
        self._ExtraAdjList = TLParams.adj_extra

        # self.Reset()

    # *** PDS methods ***
    # -------------------

    def Reset(self, sCalledBy, iNumAdjs = None):
        #print("<< Reset called by " + self.__class__.__name__ + "." + sCalledBy + "() >>")
        if iNumAdjs is None:
            iNumAdjs = self._iNumAdjs

        self.ClearAdjList()
        self._Noun = ""

        NounTagList = []
        if self.NounListLen() > 0 and self.AdjListLen() > 0:
            NounReqTagList = []
            if len(self._NounReqTagList) > 0:
                NounReqTagList = self._NounReqTagList + self._PermNounReqTagList + self._PermReqTagList
            else:
                NounReqTagList = self._ReqTagList + self._PermNounReqTagList + self._PermReqTagList

            NounExclTagList = []
            if len(self._NounExclTagList) > 0:
                NounExclTagList = self._NounExclTagList + self._PermNounExclTagList + self._PermExclTagList
            else:
                NounExclTagList = self._ExclTagList + self._PermNounExclTagList + self._PermExclTagList

            AdjReqTagList = []
            if len(self._AdjReqTagList) > 0:
                AdjReqTagList = self._AdjReqTagList + self._PermAdjReqTagList + self._PermReqTagList
            else:
                AdjReqTagList = self._ReqTagList + self._PermAdjReqTagList + self._PermReqTagList

            AdjExclTagList = []
            if len(self._AdjExclTagList) > 0:
                AdjExclTagList = self._AdjExclTagList + self._PermAdjExclTagList + self._PermExclTagList
            else:
                AdjExclTagList = self._ExclTagList + self._PermAdjExclTagList + self._PermExclTagList

            self._Noun = self.GetNewNoun(NotList = self._NotList, ReqTagList = NounReqTagList, ExclTagList = NounExclTagList)
            #print("  ---")
            global TagExclDict
            UsedTagList = []

            # ! Confused about what's supposed to be happening below
            # ------------------------------------------------------
            # if self._bVaryAdjTags and len(AdjReqTagList) == 0:
            for tag in self.GetUnitTags(self._Noun):
                if not tag in NounTagList:
                    NounTagList.append(tag)
                        #UsedTagList.append(tag)
                #print("  Added any excluding noun tags for \"" + self._Noun + "\" to UsedTagList " + str(UsedTagList))
            # ------------------------------------------------------
            for nountag in NounTagList:
                if nountag in TagExclDict:
                    for tag in TagExclDict[nountag]:
                        if not tag in UsedTagList:
                            UsedTagList.append(tag)
            #self.ClearAdjList()

            # Parse extra adjs list, add any tags to the parent
            # and to the used tag list
            ParsedExtraAdjList = []
            if not self._ExtraAdjList is None:
                for adj in self._ExtraAdjList:
                    Unit = self.ParseUnit(adj)
                    if Unit.sUnit != "":
                        ParsedExtraAdjList.append(Unit.sUnit)
                        #self.AddAdj(Unit.sUnit)
                        for tag in Unit.TagList:
                            #def AddUnitTag(self, sUnit, sTag):
                            self.AddUnitTag(Unit.sUnit,tag)
                            if not tag in UsedTagList:
                                UsedTagList.append(tag)

            for i in range(self._iNumAdjs):
                LocalReqTagList = AdjReqTagList.copy()
                LocalExclTagList = AdjExclTagList.copy()

                sAdj = self.GetNewAdj(NotList = self._NotList + [self._Noun] + self._AdjList, ReqTagList = LocalReqTagList, ExclTagList = LocalExclTagList + UsedTagList)
                if sAdj == "":
                    print("=*= WARNING =*= bodyparts.Reset() unable to get more adjectives.\n")
                    break

                for tag in self.GetUnitTags(sAdj):
                    # Try and pick adjs from different tags if required tags are not set
                    if self._bVaryAdjTags and len(LocalReqTagList) == 0:
                        if not tag == "master" and not tag in UsedTagList:
                            UsedTagList.append(tag)

                    # Avoid choosing adjectives with mutally exclusive tags
                    if tag in TagExclDict:
                        for excltag in TagExclDict[tag]:
                            if not excltag in LocalExclTagList:
                                LocalExclTagList.append(excltag)
                                #print("    Detected tag \"" + tag + "\", excluding tags " + str(TagExclDict[tag]))
                
                self.AddAdj(sAdj)

            # Sort 
            #print("    Unsorted adj list is " + str(self._AdjList))
            ExtraAdjBucket = ParsedExtraAdjList
            SpecialAdjBucket = []
            AgeAdjBucket = []
            ColorAdjBucket = []
            OtherAdjBucket = []
            SuperAdjBucket = []
            for adj in self._AdjList:
                adjtags = self.GetUnitTags(adj)
                if "special" in adjtags:
                    SpecialAdjBucket.append(adj)
                #elif "young" in self.GetUnitTags(adj) or "older" in self.GetUnitTags(adj):
                elif "age" in adjtags:
                    #print("      \"" + adj + "\" is an age adj.")
                    AgeAdjBucket.append(adj)
                elif "color" in adjtags:
                    #print("      \"" + adj + "\" is a color adj.")
                    ColorAdjBucket.append(adj)
                elif "super" in adjtags:
                    #print("      \"" + adj + "\" is a superlative adj.")
                    SuperAdjBucket.append(adj)
                else:
                    #print("      \"" + adj + "\" is a normal adj.")
                    OtherAdjBucket.append(adj)
            AgeAdjBucket.sort(key = str.lower)
            ColorAdjBucket.sort(key = str.lower)
            SuperAdjBucket.sort(key = str.lower)
            OtherAdjBucket.sort(key = str.lower)
            SpecialAdjBucket.sort(key = str.lower)

            self._AdjList = SuperAdjBucket + OtherAdjBucket + ColorAdjBucket + AgeAdjBucket + SpecialAdjBucket + ExtraAdjBucket

            #DictAdjTags = dict()
            #for adj in self._AdjList:
            #    DictAdjTags[adj] = self.GetUnitTags(adj)

    def GetAdj(self, inum, adj):
        if inum >= 0 and inum < len(self._AdjList):
            self._AdjList[inum] = adj

    def AddAdj(self, adj):
        if adj != "":
            self._AdjList.append(adj)

    def RemoveAdj(self, adj):
        if adj in self._AdjList:
            self._AdjList.remove(adj)

    def RemoveAdjByNum(self, inum):
        if inum >= 0 and inum < len(self._AdjList):
            self._AdjList.pop(inum)

    def ClearAdjList(self):
        self._AdjList = []

    def Noun(self, noun):
        self._Noun = noun

    def Color(self, color):
        self._Color = color

    def ReqTagList(self, TagList):
        self._ReqTagList = TagList
        self.Reset("ReqTagList")

    def ExclTagList(self, TagList):
        self._ExclTagList = TagList
        self.Reset("ExclTagList")

    def NounReqTagList(self, TagList):
        self._NounReqTagList = TagList
        self.Reset("NounReqTagList")

    def NounExclTagList(self, TagList):
        self._NounExclTagList = TagList
        self.Reset("NounExclTagList")

    def AdjReqTagList(self, TagList):
        self._AdjReqTagList = TagList
        self.Reset("AdjReqTagList")

    def AdjExclTagList(self, TagList):
        self._AdjExclTagList = TagList
        self.Reset("AdjExclTagList")

    def GetRandomAdj(self):
        return choice(self._AdjList)

    def GetAdj(self, inum):
        sAdj = ""
        if inum >= 0 and inum < len(self._AdjList):
            sAdj = self._AdjList[inum]
        
        return sAdj

    def GetNoun(self):
        return self._Noun

    def IsPlural(self):
        bIsPlural = False

        NounTags = self.GetUnitTags(self.GetNoun())
        if 'plur' in NounTags:
            bIsPlural = True

        return bIsPlural

    def IsSing(self):
        bIsSing = False

        NounTags = self.GetUnitTags(self.GetNoun())
        if 'sing' in NounTags:
            bIsSing = True

        return bIsSing

    def GetColor(self):
        return self._Color

    def GetFullDesc(self, iNumAdjs, bColor = True):
        sFullDesc = ""
        DescWordList = self._AdjList.copy()

        if iNumAdjs < len(DescWordList):
            for i in range(len(DescWordList) - iNumAdjs):
                DescWordList.remove(choice(DescWordList))

        if self.GetNoun() != "":
            DescWordList.append(self.GetNoun())

        if len(DescWordList) < 3:
            sFullDesc = " ".join(DescWordList)
        elif len(DescWordList) == 3:
            sFullDesc = ", ".join(DescWordList[:1]) + ", " + " ".join(DescWordList[1:])
        elif len(DescWordList) == 4:
            sFullDesc = ", ".join(DescWordList[:-2]) + ", " + " ".join(DescWordList[-2:])
        else:
            sFullDesc = ", ".join(DescWordList[:-3]) + ", " + " ".join(DescWordList[-3:])
        
        return sFullDesc

    def GetDescWordList(self):
        DescWordList = []

        sNoun = self.GetNoun()

        if sNoun != "":
            DescWordList.insert(0, sNoun)
        #if self.Color() != "":
        #    DescWordList.insert(0, self.Color())
        DescWordList = self._AdjList + DescWordList

        return DescWordList

    # *** Bodyparts methods ***
    # -------------------------

    def SetUnitTags(self, sUnit, TagList):
        self._UnitTags[sUnit] = TagList 

    def AddUnitTag(self, sUnit, sTag):
        # If a unit does not have a tag list, add an entry
        if not sUnit in self._UnitTags:
             self._UnitTags[sUnit] = []
 
        # No duplicates
        if not sTag in self._UnitTags[sUnit]:
            self._UnitTags[sUnit].append(sTag)

    def GetUnitTags(self, sUnit):
        UnitTags = [] 

        if sUnit in self._UnitTags:
            UnitTags = self._UnitTags[sUnit]

        return UnitTags

    def GetUnitList(self, sListName, sType):
        UnitList = []
        ListDict = self._AllUnitLists[sType.lower()]

        if sListName.lower() in ListDict:
            UnitList = ListDict[sListName.lower()]

        return UnitList 

    def GetNounList(self, sListName = None):
        if sListName is None:
            sListName = "master"
        return self.GetUnitList(sListName, "noun") 

    def GetAdjList(self, sListName = None):
        if sListName is None:
            sListName = "master"
        return self.GetUnitList(sListName, "adj") 

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

    def AddNounToList(self, sNoun, sListName, iPriority = None):
        self.AddUnitToList(sNoun,sListName,"noun", iPriority = iPriority)

    def AddAdjToList(self, sNoun, sListName, iPriority = None):
        self.AddUnitToList(sNoun,sListName,"adj", iPriority = iPriority)

    def IsUnitInList(self, sUnit, sListName, sType):
        bIsUnitInList = False 

        UnitList = self.GetUnitList(sListName, sType)
        if not UnitList is None:
            if sUnit.lower() in UnitList:
                bIsUnitInList = True

        return bIsUnitInList

    def IsNounInList(self, sNoun, sListName):
        return self.IsUnitInList(sNoun, sListName, "noun")

    def IsAdjInList(self, sNoun, sListName):
        return self.IsUnitInList(sNoun, sListName, "adj")

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

    def UnitList(self, NewUnitList, sType):
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
               
        self.Reset("UnitList_" + sType)

    def NotList(self, NotList):
        self._NotList = NotList
        self.Reset("NotList")

    def NounList(self, NewNounList):
        self.UnitList(NewNounList, "noun")

    def AdjList(self, NewAdjList):
        self.UnitList(NewAdjList, "adj")

    def ExtraAdjList(self, ExtraAdjList):
        self._ExtraAdjList = ExtraAdjList
        self.Reset("ExtraAdjList")

    def UnitListLen(self, sType):
        ListLen = 0 
        ListDict = self._AllUnitLists[sType.lower()]

        ListLen = len(ListDict["master"])

        return ListLen

    def NounListLen(self):
        return self.UnitListLen("noun")

    def AdjListLen(self):
        return self.UnitListLen("adj")
          
    def DefaultNoun(self, NewNoun = None):
        if NewNoun == None:
            NewNoun = ""
               
        self._DefaultNoun = NewNoun 
     
    def DefaultAdj(self, NewAdj = None):
        if NewAdj == None:
            NewAdj = ""
               
        self._DefaultAdj = NewAdj 
          
    def GetDefaultNoun(self, NotList = None):
        sDefaultNoun = ""
          
        if NotList == None:
            NotList = []

        if self._DefaultNoun not in NotList:
            sDefaultNoun = self._DefaultNoun
               
        return sDefaultNoun
          
    def GetDefaultAdj(self, NotList = None):
        sDefaultAdj = ""
          
        if NotList == None:
            NotList = []

        if self._DefaultAdj not in NotList:
            sDefaultAdj = self._DefaultAdj
               
        return sDefaultAdj
     
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

        if ReqTagList == None or len(ReqTagList) == 0:
            #print("  ReqTagList is empty. Using master list.")
            for unit in self.GetUnitList("master", sType):
                if not unit in ExclUnitList:
                    LocalUnitList.append(unit)
        else:
            for taglistname in ReqTagList:
                #print("  Adding taglist " + taglistname)
                for unit in self.GetUnitList(taglistname, sType):
                    if not unit in ExclUnitList:
                        LocalUnitList.append(unit)

        #print("  LocalUnitList = " + str(LocalUnitList) + "\n")

        if len(LocalUnitList) == 0:
            if ReqTagList == None or len(ReqTagList) == 0:
                LocalUnitList += self.GetUnitList("master", sType)
        else:
            for taglistname in ReqTagList:
                LocalUnitList += self.GetUnitList(taglistname, sType)

        if len(LocalUnitList) > 0:
            # First, try with the not list, the excluded tag list, and the required tag list

            sUnit = WordList(LocalUnitList).GetWord(NotList = NotList + ExclUnitList)

            if sUnit == "":
                # Second, try with the not list and the required tag list
                print("  GetUnit() could not retrieve word. Trying without excluded tag list.")
                sUnit = WordList(LocalUnitList).GetWord(NotList = NotList)

                if sUnit == "":
                    # Third, try with just the not list
                    print("   GetUnit() could not retrieve word. Trying without the required tag list.")
                    sUnit = WordList(self.GetUnitList("master", sType)).GetWord(NotList = NotList)

                    if sUnit == "":
                        # Fourth, try without any constraints
                        print("   GetUnit() could not retrieve word. Trying without the not list.")
                        sUnit == WordList(self.GetUnitList("master", sType)).GetWord()
            #print("  GetUnit() new word is \"" + sUnit + "\"")

        return sUnit

    def GetNewAdj(self, NotList = None, ReqTagList = None, ExclTagList = None):
        sNewAdj = ""
        
        if NotList is None:
            NotList = []
        if ReqTagList is None:
            ReqTagList = []
        if ExclTagList is None:
            ExclTagList = []

        UsedTagList = []
        for adj in self._AdjList:
            UsedTagList += self.GetUnitTags(adj)

        sNewAdj = self.GetUnit("adj", NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList + UsedTagList)
        
        for tag in self.GetUnitTags(sNewAdj): 
            if not tag.lower() == "master":
                self.AddUnitTag(sNewAdj, tag)

        return sNewAdj

    def GetNewNoun(self, NotList = None, ReqTagList = None, ExclTagList = None):
        sNewNoun = ""

        if NotList is None:
            NotList = []
        if ReqTagList is None:
            ReqTagList = []
        if ExclTagList is None:
            ExclTagList = []

        sNewNoun = self.GetUnit("noun", NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)
        for tag in self.GetUnitTags(sNewNoun):
            self.AddUnitTag(sNewNoun, tag)

        return sNewNoun

    def UpdateTagLists(self, TLParams = None):
        if TLParams is None:
            TLParams = TagLists()

        if len(TLParams.req) > 0:
            self.ReqTagList(TLParams.req)

        if len(TLParams.excl) > 0:
            self.ExclTagList(TLParams.excl)

        if len(TLParams.noun_req) > 0:
            self.NounReqTagList(TLParams.noun_req)

        if len(TLParams.noun_excl) > 0:
            self.NounExclTagList(TLParams.noun_excl)

        if len(TLParams.adj_req) > 0:
            self.AdjReqTagList(TLParams.adj_req)

        if len(TLParams.adj_excl) > 0:
            self.AdjExclTagList(TLParams.adj_excl)

        if len(TLParams.adj_extra) > 0:
            self.AdjReqTagList(TLParams.adj_extra)

        return True

    #noun only ("hair")
    def ShortDescription(self, NotList = None, TLParams = None): #, ExtraAdjList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        self.UpdateTagLists(TLParams)

        return self.GetFullDesc(iNumAdjs = 0)
     
    #adjective noun ("red hair")
    def MediumDescription(self, NotList = None, TLParams = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        self.UpdateTagLists(TLParams)
          
        return self.GetFullDesc(iNumAdjs = 1)
     
    #adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
    def FloweryDescription(self, NotList = None, TLParams = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        self.UpdateTagLists(TLParams)
          
        iNumAdjs = choice([1,1,1,2,2,2,2,3])

        return self.GetFullDesc(iNumAdjs = iNumAdjs)
     
    def RandomDescription(self, bAllowShortDesc = True, bAllowLongDesc = True, NotList = None, TLParams = None):
        sRandomDesc = ""
          
        iRand = randint(0, 12)
        if iRand in range(0, 3):
        #short desc if allowed 
            if bAllowShortDesc:
                #use noun from the list or default noun
                if CoinFlip():
                        sRandomDesc = self.ShortDescription(NotList = NotList, TLParams = TLParams)
                else:
                        sRandomDesc = self.GetDefaultNoun(NotList = NotList)
            else:
                sRandomDesc = self.MediumDescription(NotList = NotList, TLParams = TLParams)
        elif iRand in range(3,6):
        #medium desc 
            sRandomDesc = self.MediumDescription(NotList = NotList, TLParams = TLParams)
        else:
        #flowery desc if allowed
            if bAllowLongDesc:
                sRandomDesc = self.FloweryDescription(NotList = NotList, TLParams = TLParams)
            else:
                sRandomDesc = self.MediumDescription(NotList = NotList, TLParams = TLParams)
               
        return sRandomDesc

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