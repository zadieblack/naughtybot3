#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Excerpt Helpers module

from random import *
from util import *
import re 

BodyPartHistoryQ = HistoryQ(10)

TagExclDict = {"poc": ["whitepers"],
               "whitepers": ["poc"],
               "large": ["small"],
               "small": ["large"],
               "older": ["young"],
               "young": ["older"],
               "hairless": ["hairy"],
               "hairy": ["hairless"],
               "tall": ["short"],
               "short": ["tall"],
               "slender": ["plussize"],
               "plussize": ["slender"],
               "thick": ["thin"],
               "thin": ["thick"],
              }

class ParsedUnit:
    def __init__(self, sUnit = "", iPriority = 1, TagList = []):
        self.sUnit = sUnit
        self.iPriority = iPriority
        self.TagList = TagList

# =============================
# *** NounPhrase base class ***
# =============================

# This complex class is designed to create noun phrases. For our
# purposes, a noun phrase is a noun that can be proceeded by any
# number of adjectives.

# NounPhrase objects will have lists of nouns and adjectives. 
# The NounPhrase object picks a noun and some adjs at random,
# although the choice may be constrained by other parameters.
# It then strings them together in a way that hopefully makes
# grammatical sense.

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
    def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = True, NotList = None, bEnableSpecials = False):
        self._AllUnitLists = {"adj": {"master": []}, "noun": {"master": [], "std": []}}
        self._UnitTags = dict()
        self._DefaultNoun = ""
        self._DefaultAdj = "naked"
          
        self.NounHistoryQ = HistoryQ(3)
        self.AdjHistoryQ = HistoryQ(3)

        # PDS code
        if NotList is None:
            NotList = []

        self._NotList = NotList
        self._Noun = ""
        self._Color = ""
        self._EnableSpecials = bEnableSpecials
        self._iNumAdjs = iNumAdjs
        self._AdjList = []
        self._bVaryAdjTags = bVaryAdjTags

        # Nouns and Adjs have their own specific required and excluded
        # tag lists which they will use if available. Otherwise, they
        # fall back on the general required and excluded tag lists.
        self._ReqTagList = []
        self._ExclTagList = []
        self._NounReqTagList = []
        self._NounExclTagList = []
        self._AdjReqTagList = []
        self._AdjExclTagList = []

        if ExtraAdjList is None:
            self._ExtraAdjList = []
        else:
            self._ExtraAdjList = ExtraAdjList

        # self.Reset()

    # *** PDS methods ***
    # -------------------

    def Reset(self, sCalledBy, iNumAdjs = None):
        #print("<< Reset called by " + self.__class__.__name__ + "." + sCalledBy + "() >>")
        if iNumAdjs is None:
            iNumAdjs = self._iNumAdjs

        self.ClearAdjList()
        self._Noun = ""

        if self.NounListLen() > 0 and self.AdjListLen() > 0:
            NounReqTagList = []
            if len(self._NounReqTagList) > 0:
                NounReqTagList = self._NounReqTagList
            else:
                NounReqTagList = self._ReqTagList

            NounExclTagList = []
            if len(self._NounExclTagList) > 0:
                NounExclTagList = self._NounExclTagList
            else:
                NounExclTagList = self._ExclTagList

            AdjReqTagList = []
            if len(self._AdjReqTagList) > 0:
                AdjReqTagList = self._AdjReqTagList
            elif len(self._AdjReqTagList) > 0:
                AdjReqTagList = self._AdjReqTagList
            else:
                AdjReqTagList = self._ReqTagList

            AdjExclTagList = []
            if len(self._AdjExclTagList) > 0:
                AdjExclTagList = self._AdjExclTagList
            elif len(self._AdjExclTagList) > 0:
                AdjExclTagList = self._AdjExclTagList
            else:
                AdjExclTagList = self._ExclTagList

            self._Noun = self.GetNewNoun(NotList = self._NotList, ReqTagList = NounReqTagList, ExclTagList = NounExclTagList)
            #print("  ---")
            global TagExclDict
            UsedTagList = []
            if self._bVaryAdjTags and len(AdjReqTagList) == 0:
                for tag in self.GetUnitTags(self._Noun):
                    if tag in TagExclDict:
                        UsedTagList.append(tag)
                #print("  Added any excluding noun tags for \"" + self._Noun + "\" to UsedTagList " + str(UsedTagList))

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
                        if not tag == "master":
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

    #noun only ("hair")
    def ShortDescription(self, ExtraAdjList = None, NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if NounReqTagList == None:
            NounReqTagList = []
        else:
            self.NounReqTagList(NounReqTagList)

        if NounExclTagList == None:
            NounExclTagList = []
        else:
            self.NounExclTagList(NounExclTagList)

        if AdjReqTagList == None:
            AdjReqTagList = []
        else:
            self.AdjReqTagList(AdjReqTagList)

        if AdjExclTagList == None:
            AdjExclTagList = []
        else:
            self.AdjExclTagList(AdjExclTagList)

        if ExtraAdjList is None:
            ExtraAdjList = []
        else:
            self.ExtraAdjList(ExtraAdjList)

        return self.GetFullDesc(iNumAdjs = 0)
     
    #adjective noun ("red hair")
    def MediumDescription(self, ExtraAdjList = None, NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if NounReqTagList == None:
            NounReqTagList = []
        else:
            self.NounReqTagList(NounReqTagList)

        if NounExclTagList == None:
            NounExclTagList = []
        else:
            self.NounExclTagList(NounExclTagList)

        if AdjReqTagList == None:
            AdjReqTagList = []
        else:
            self.AdjReqTagList(AdjReqTagList)

        if AdjExclTagList == None:
            AdjExclTagList = []
        else:
            self.AdjExclTagList(AdjExclTagList)

        if ExtraAdjList is None:
            ExtraAdjList = []
        else:
            self.ExtraAdjList(ExtraAdjList)
          
        return self.GetFullDesc(iNumAdjs = 1)
     
    #adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
    def FloweryDescription(self, ExtraAdjList = None, NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
        else:
            self.NotList(NotList)

        if NounReqTagList == None:
            NounReqTagList = []
        else:
            self.NounReqTagList(NounReqTagList)

        if NounExclTagList == None:
            NounExclTagList = []
        else:
            self.NounExclTagList(NounExclTagList)

        if AdjReqTagList == None:
            AdjReqTagList = []
        else:
            self.AdjReqTagList(AdjReqTagList)

        if AdjExclTagList == None:
            AdjExclTagList = []
        else:
            self.AdjExclTagList(AdjExclTagList)

        if ExtraAdjList is None:
            ExtraAdjList = []
        else:
            self.ExtraAdjList(ExtraAdjList)
          
        iNumAdjs = choice([1,1,1,2,2,2,2,3])

        return self.GetFullDesc(iNumAdjs = iNumAdjs)
     
    def RandomDescription(self, ExtraAdjList = None, NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
                              # ExtraAdjList = None, NotList = None,                                                NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None
        sRandomDesc = ""
          
        iRand = randint(0, 12)
        if iRand in range(0, 3):
        #short desc if allowed 
            if bAllowShortDesc:
                #use noun from the list or default noun
                if CoinFlip():
                        sRandomDesc = self.ShortDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
                else:
                        sRandomDesc = self.GetDefaultNoun(NotList = NotList)
            else:
                sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
        elif iRand in range(3,6):
        #medium desc 
            sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
        else:
        #flowery desc if allowed
            if bAllowLongDesc:
                sRandomDesc = self.FloweryDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
            else:
                sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
               
        return sRandomDesc

