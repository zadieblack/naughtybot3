#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

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
              }

class ParsedUnit:
    def __init__(self, sUnit = "", iPriority = 1, TagList = []):
        self.sUnit = sUnit
        self.iPriority = iPriority
        self.TagList = TagList

# ============================
# *** Bodyparts base class ***
# ============================


class BodyParts:
    def __init__(self, iNumAdjs = 5, ExtraAdjList = None, bVaryAdjTags = True, NotList = None):
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

    def Reset(self, iNumAdjs = None):
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

            if isinstance(self, Breasts):
                stuff = "foo"

            self._Noun = self.GetNewNoun(NotList = self._NotList, ReqTagList = NounReqTagList, ExclTagList = NounExclTagList)
            #print("  ---")
            global TagExclDict
            UsedTagList = []
            if self._bVaryAdjTags and len(AdjReqTagList) == 0:
                for tag in self.GetUnitTags(self._Noun):
                    if tag in TagExclDict:
                        UsedTagList.append(tag)
                #print("  Added any excluding noun tags for \"" + self._Noun + "\" to UsedTagList " + str(UsedTagList))

            self.ClearAdjList()

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

            #if bTestBreasts and self._iNumAdjs > 3:
            #    print("  ---")
            for i in range(self._iNumAdjs):
                LocalReqTagList = AdjReqTagList.copy()
                LocalExclTagList = AdjExclTagList.copy()

                if isinstance(self, Breasts):
                    stuff = "foo"
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
                #if isinstance(self, Breasts):
                #    print("  Picked adj \"" + sAdj + "\" " + str(self.GetUnitTags(sAdj)) + "\n    excl tags " + str(LocalExclTagList) + "\n    used tags " + str(UsedTagList))
                #print("  Adj list " + str(self._AdjList))

            # Sort 
            #print("    Unsorted adj list is " + str(self._AdjList))
            ExtraAdjBucket = ParsedExtraAdjList
            AgeAdjBucket = []
            ColorAdjBucket = []
            OtherAdjBucket = []
            SuperAdjBucket = []
            for adj in self._AdjList:
                if "young" in self.GetUnitTags(adj) or "older" in self.GetUnitTags(adj):
                    #print("      \"" + adj + "\" is an age adj.")
                    AgeAdjBucket.append(adj)
                elif "color" in self.GetUnitTags(adj):
                    #print("      \"" + adj + "\" is a color adj.")
                    ColorAdjBucket.append(adj)
                elif "super" in self.GetUnitTags(adj):
                    #print("      \"" + adj + "\" is a superlative adj.")
                    SuperAdjBucket.append(adj)
                else:
                    #print("      \"" + adj + "\" is a normal adj.")
                    OtherAdjBucket.append(adj)
            AgeAdjBucket.sort(key = str.lower)
            ColorAdjBucket.sort(key = str.lower)
            SuperAdjBucket.sort(key = str.lower)
            OtherAdjBucket.sort(key = str.lower)
            #self.ClearAdjList()
            self._AdjList = SuperAdjBucket + OtherAdjBucket + ColorAdjBucket + AgeAdjBucket + ExtraAdjBucket
            #print("    Sorted adj list is " + str(self._AdjList))

            #print("  Final Adj List is " + str(self._AdjList))
            DictAdjTags = dict()
            for adj in self._AdjList:
                DictAdjTags[adj] = self.GetUnitTags(adj)
                #print("  Tags for \"" + adj + "\" are " + str(DictAdjTags[adj]))
            #if len(self._ColorList.GetWordList()) > 0:
            #    self._Color = self.GetColor(NotList = self._NotList + self._AdjList + [self._Noun])


    def NotList(self, NotList):
        self._NotList = NotList
        self.Reset()

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
        self.Reset()

    def ExclTagList(self, TagList):
        self._ExclTagList = TagList
        self.Reset()

    def NounReqTagList(self, TagList):
        self._NounReqTagList = TagList
        self.Reset()

    def NounExclTagList(self, TagList):
        self._NounExclTagList = TagList
        self.Reset()

    def AdjReqTagList(self, TagList):
        self._AdjReqTagList = TagList
        self.Reset()

    def AdjExclTagList(self, TagList):
        self._AdjExclTagList = TagList
        self.Reset()

    def GetAdj(self, inum):
        sAdj = ""
        if inum >= 0 and inum < len(self._AdjList):
            sAdj = self._AdjList[inum]
        
        return sAdj

    def GetNoun(self):
        return self._Noun

    def GetColor(self):
        return self._Color

    def GetFullDesc(self, iNumAdjs, bColor = True):
        sFullDesc = ""
        DescWordList = []
        
        if len(self._AdjList) < iNumAdjs:
            iNumAdjs = len(self._AdjList)
        for i in range(len(self._AdjList) - iNumAdjs, len(self._AdjList)):
            if i < len(self._AdjList):
                DescWordList.append(self._AdjList[i])
            else:
                break

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
        self._UnitTags[sUnit.lower()] = TagList 

    def AddUnitTag(self, sUnit, sTag):
        # If a unit does not have a tag list, add an entry
        if not sUnit in self._UnitTags:
             self._UnitTags[sUnit.lower()] = []
 
        # No duplicates
        if not sTag in self._UnitTags[sUnit.lower()]:
            self._UnitTags[sUnit.lower()].append(sTag)

    def GetUnitTags(self, sUnit):
        UnitTags = [] 

        if sUnit in self._UnitTags:
            UnitTags = self._UnitTags[sUnit.lower()]

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

        if isinstance(self, Breasts):
            pass

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

            if isinstance(self, Breasts):
                stuff = "foo"

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
               
        self.Reset()

    def NotList(self, NewNotList):
        self._NotList = NewNotList 
        self.Reset()

    def NounList(self, NewNounList):
        self.UnitList(NewNounList, "noun")

    def AdjList(self, NewAdjList):
        self.UnitList(NewAdjList, "adj")

    def ExtraAdjList(self, ExtraAdjList):
        self._ExtraAdjList = ExtraAdjList
        self.Reset()

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
     
    def GetUnit(self, sType, sNot = "", NotList = None, ReqTagList = None, ExclTagList = None):
        sUnit = "" 
        LocalUnitList = []
        #print("      Entered GetUnit()")
         
        if NotList is None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ReqTagList is None:
            ReqTagList = []

        if ExclTagList is None:
            ExclTagList == []

        if ExclTagList is None:
            ExclTagList = []
        #else:
        #    print("      ExclTagList is + " + str(ExclTagList))

        ExclUnitList = []
        for tag in ExclTagList:
            #print("    Getting word units for " + unitlist)
            for unit in self.GetUnitList(tag, sType):
                ExclUnitList.append(unit)
        #print("      ExclUnitList is + " + str(ExclUnitList))

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

        sNewAdj = self.GetUnit("adj", NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)
        for tag in self.GetUnitTags(sNewAdj):
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
    def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []

            if sNot != "":
                NotList.append(sNot)
                self.NotList(NotList)
        else:
            if sNot != "":
                NotList.append(sNot)

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

        return self.GetFullDesc(iNumAdjs = 0, bColor = False)
     
    #adjective noun ("red hair")
    def MediumDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []

            if sNot != "":
                NotList.append(sNot)
                self.NotList(NotList)
        else:
            if sNot != "":
                NotList.append(sNot)

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
          
        return self.GetFullDesc(iNumAdjs = 1, bColor = CoinFlip())
     
    #adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
    def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []

            if sNot != "":
                NotList.append(sNot)
                self.NotList(NotList)
        else:
            if sNot != "":
                NotList.append(sNot)

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

        return self.GetFullDesc(iNumAdjs = iNumAdjs, bColor = CoinFlip())
     
    def RandomDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        sRandomDesc = ""
          
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExtraAdjList is None:
            ExtraAdjList = []
          
        iRand = randint(0, 12)
        if iRand in range(0, 3):
        #short desc if allowed 
            if bAllowShortDesc:
                #use noun from the list or default noun
                if CoinFlip():
                        sRandomDesc = self.ShortDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
                else:
                        sRandomDesc = self.GetDefaultNoun(NotList = NotList)
            else:
                sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
        elif iRand in range(3,6):
        #medium desc 
            sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
        else:
        #flowery desc if allowed
            if bAllowLongDesc:
                sRandomDesc = self.FloweryDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
            else:
                sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
               
        return sRandomDesc

class Face(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['face x3: default,std,sing',
                         'features: poetic,plur'
                        ])
          
          self.AdjList(['adorable: super,cute,young,attractive',
                        'angelic: super,cute,attractive',
                        'beaming: emotion,happy',
                        'beautiful: super,attractive',
                        'cute: super,cute,attractive',
                        'delicate: cute',
                        'dark: color',
                        'elegant: older,attractive',
                        'excited: emotion,happy',
                        'expressive: emotion',
                        'gentle: attitude',
                        'gorgeous: super,attractive',
                        'flushed: arousal',
                        'freckled: color,whitepers',
                        'heart-shaped: shape',
                        'innocent: attitude,cute,young,virginal',
                        'lovely: super,attractive',
                        'oval: shape',
                        'pale: color,whitepers',
                        'pretty: attractive',
                        'radiant: ',
                        'rosy: color,young',
                        'round: shape',
                        'smiling: emotion,happy',
                        'startled: emotion',
                        'sweet: attitude,cute,attractive',
                        'warm: attitude,feel',
                        'wide-eyed: cute,attractive'])
               
          self.DefaultNoun('face')
          
class BackFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['back x4:default,std,sing',
                         'spine:std,clinical,sing'])
          
          self.AdjList(['arched x2: shape',
                         'arching: action',
                         'bare: nude',
                         'carved: shape',
                         'concave: shape',
                         'curved x2: shape',
                         'delicate: super,attractive',
                         'feminine: attractive',
                         'flexible: flexible,attractive',
                         'gently curved: shape, attractive',
                         'graceful x2: fit',
                         'lissome: attractive,slender',
                         'lithe x2: athletic,young,flexible,slender',
                         'long: size,length,long',
                         'naked: nude',
                         'sculpted: attractive',
                         'sexy: attractive',
                         'sleek: slender',
                         'slender x2: slender,shape',
                         'slim x2: slender',
                         'smooth: feel',
                         'tapered x3: shape,slender',
                         'tapering x2: shape,slender',
                         'well-defined: shape',
                         'willowy x2: slender,flexible'
                        ])
               
          self.DefaultNoun('back')
          self.DefaultAdj('curved')
          
class Skin(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['skin x4: default,std,sing',
                         'flesh: sing'
                        ])
                              
          self.AdjList(['almond-colored: asian,color',
                        'bare: nude',
                        'brown: color,poc',
                        'chocolate: color,taste,poc,',
                        'chocolate-colored: color,poc,',
                        'coffee-colored: color,poc',
                        'creamy: texture,color,taste,whitepers',
                        'dark: color,poc',
                        'delicate: texture,cute',
                        'exposed: nude',
                        'freckled: texture,whitepers',
                        'fresh pink: color,whitepers',
                        'gentle: feel,texture',
                        'gleaming: texture,shiny',
                        'glistening: wet,texture,shiny',
                        'glowing: texture',
                        'gossamer: feel,texture',
                        'honeyed: color, taste,texture',
                        'luscious: taste,super',
                        'naked: nude',
                        'pale: color,whitepers',
                        'perfect: super',
                        'pink: color,whitepers,young',
                        'porcelain: color,texture,whitepers',
                        'rosy: color,texture,whitepers,young',
                        'silken: feel,texture',
                        'soft: feel,texture',
                        'smooth: feel,texture',
                        'sun-browned: color',
                        'sun-kissed: color',
                        'supple: feel,young,texture',
                        'sweet: super,taste',
                        'tender: feel,cute',
                        'un-blemished: young,virginal,texture',
                        'un-sullied: young,virginal',
                        'warm: feel',
                        'yielding: feel',
                        'youthful: young',
                       ])
          
          self.DefaultNoun('skin')
          self.IsPlural = False
          
class Mouth(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['mouth x4: default,std,sing',
                         'mouth-hole: silly,crude,sing'])
               
          self.AdjList(['eager: attitude',
                        'filthy: attitude,horny,rude',
                        'greedy: horny',
                        'hot: feel',
                        'hungry: horny',
                        'insatiable: horny',
                        'insolent: attitude,rude',
                        'lewd: horny',
                        'open: open',
                        'pretty: attractive',
                        'soft: feel',
                        'sweet: super,attractive',
                        'thirsty: horny',
                        'wanting: horny',
                        'warm: feel',
                        'wet: wet',
                        'willing: attitude,horny'])
          
          self.DefaultNoun("open")
          self.DefaultAdj("insatiable")
          self.IsPlural = False
          
class Lips(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['lips: default,std,plur'])
               
          self.AdjList(['candy-colored: lipstick,color,',
                        'collagen-injected: fake,feel',
                        'curved: shape',
                        'dark: color',
                        'full: thick,desc',
                        'glossy: shiny,texture',
                        'inviting: attitude',
                        'insolent: attitude',
                        'luscious: super,thick,taste',
                        'moist: feel,taste',
                        'painted: lipstick',
                        'pouting: emotion',
                        'pouty: emotion,shape',
                        'red x2: color',
                        'rose-colored: color',
                        'rosy: color',
                        'rouge: color',
                        'sensual: attitude',
                        'shiny: shiny',
                        'smiling: emotion',
                        'soft: feel,texture',
                        'sweet: young,taste'
                        'tender: feel',
                        'warm: feel',
                       ])
          
          self.DefaultNoun("lips")
          self.DefaultAdj("full")
          
class Eyes(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['eyes: std,default,plur'])
               
          self.AdjList(['alluring: attractive',
                        'beautiful: attractive',
                        'bewitching: attractive',
                        'bright: attractive,young,whitepers',
                        'blue x4: color,whitepers',
                        'brown x3: color',
                        'captivating: attractive',
                        'clear: attractive,desc',
                        'dazzling: attractive,shiny',
                        'earnest: emotion',
                        'electric: attractive',
                        'electrifying: attractive',
                        'enchanting: attractive',
                        'exotic: attractive',
                        'gray x2: color,whitepers',
                        'green x3: color,whitepers',
                        'hazel x2: color,whitepers',
                        'kind: emotion',
                        'large: size,large,desc',
                        'mischievous: emotion',
                        'pale: color,whitepers',
                        'piercing: ',
                        #'slanted: asian',
                        'soulful: attractive',
                        'sparkling: attractive,shiny',
                        'sweet: attractive',
                        'wide: size,large'])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("bewitching")
          
class Hips(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['hips: std,default,plur'])
               
          self.AdjList(['curvy: width,wide,shape,desc',
                        'curvaceous: wide,width',
                        'bare: nude',
                        'fertile: width,wide,horny',
                        'girlish: shape,width,narrow,young',
                        'narrow: shape,width,narrow',
                        'rounded: shape',
                        'sensual: attractive',
                        'shapely: shape,attractive',
                        'slender: shape,size,small',
                        'slinky: attitude',
                        'sultry: attitude,attractive',
                        'tantalizing: horny,attractive,',
                        'voluptuous: size,wide,width',
                        'wanton: horny',
                        'wide: size,wide',
                        'womanly: feminine,wide'])
          
          self.DefaultNoun("hips")
          
class Hair(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['braids: style,plur',
                         'hair x4: std,default,sing',
                         'fro: poc,sing'
                         'locks x2: plur',
                         'pig-tails: style,young,plur',
                         ])
               
          self.AdjList(['auburn: color,whitepers',
                        'black x2:color',
                        'blonde x4: color,whitepers',
                        'brunette x3: color,whitepers',
                        'curly: shape,style',
                        'braided: style',
                        'dark x2: color',
                        'dyed-blue: color,fake',
                        'dyed-green: color,fake',
                        'dyed-pink: color,fake',
                        'dyed-purple: color,fake',
                        'fashionable: style',
                        'flaming-red: color,whitepers',
                        'flowing: poetic'
                        'glossy: feel',
                        'golden: color,whitepers',
                        'kinky black-girl: color,poc',
                        'long: length',
                        'luxuriant: feel',
                        'pixie cut: style',
                        'platinum blonde x2: color,whitepers',
                        'punk blue: color,fake,style',
                        'red: color,whitepers',
                        'sandy: color,whitepers',
                        'silken: feel',
                        'short: length',
                        'straight: shape,style',
                        'vibrant: poetic',
                        'wavy: shape,style'])
          
          self.DefaultNoun("hair")
          self.DefaultAdj("flowing")
          
class Legs(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['legs: std,default,plur'])
               
          self.AdjList(['athletic: fit',
                        'bare: nude',
                        'chiseled: fit,attractive',
                        'chubby: curvy',
                        'coltish x2: slender, young',
                        'comely: attractive',
                        'elegant: poetic',
                        'feminine: attractive',
                        'fetching: attractive',
                        'fit: fit',
                        'flexible: flexible',
                        'girlish: young,slender',
                        'graceful: fit',
                        'lithe: flexible',
                        'limber: flexible',
                        'lissome: flexible,fit,slender',
                        'lithesome: flexible,fit,slender',
                        'long x3: length,long',
                        'long, sexy: length,long,attractive',
                        'lovely: attractive,super',
                        'naked: nude',
                        'satiny: feel,shiny',
                        'sinuous: attractive,flexible',
                        'smooth: feel,hairless',
                        'supple: feel,soft,young',
                        'tall: length,long',
                        'tan: color',
                        'tanned: color',
                        'toned: fit',
                        'sexy: attractive',
                        'shapely: fit',
                        'shaved: hairless',
                        'short: length,short',
                        'slender: slender',
                        'smooth: hairless',
                        'smooth-shaven: hairless',
                        'supple: soft,young,feel',
                        'svelte: slender,flexible',
                        'willowy: slender',
                        'womanly: curvy,attractive',
                        'yielding: soft,feel,horny',
                       ])
          
          self.DefaultNoun("legs")
          
class Thighs(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['thighs: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'bronzed: color,tan',
                        'chubby: curvy,chubby',
                        'comely: attractive, poetic',
                        'delectable: super,taste',
                        'full: curvy,chubby,large',
                        'girlish: slender,young',
                        'heavy: chubby,large',
                        'inviting: horny',
                        'luscious: super',
                        'nubile: young',
                        'pale: color,whitepers',
                        'plump: curvy,chubby'
                        'powerful: fit,strong',
                        'porcelain: color,whitepers',
                        'ripe: attractive',
                        'rounded: shape',
                        'sensual: attractive',
                        'sexy: attractive',
                        'shapely: shape,attractive',
                        'silken: feel',
                        'smooth: feel,hairless',
                        'soft: feel',
                        'tanned: color,tan',
                        'tender: feel',
                        'thick x2: large,chubby',
                        'un-sullied: young, virginal',
                        'wide: chubby,large',
                        'womanly: curvy',
                        'youthful: young'])
          
          self.DefaultNoun("thighs")
          
class Nipples(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['nipples x4: std,default,plur',
                         'nips: silly,plur',
                         'teats: silly,plur',
               ])
               
          self.AdjList(['aching: horny',
                        'bare: nude',
                        'bared: nude',
                        'black: color, poc',
                        'blossoming: young',
                        'brown: color,',
                        'budding: cute',
                        'chocolate: color',
                        'dainty: size,small,cute',
                        'dark: color,',
                        'dusky: color',
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'exquisite: attractive,super',
                        'hard: arousal,',
                        'inch-long: size,large,',
                        'long,: size,large',
                        'luscious: super',
                        'petite: size,small,cute,',
                        'pert: arousal,cute',
                        'pierced: style',
                        'pink: color,whitepers',
                        'plump: size,large,feel',
                        'pokey: arousal',
                        'prominent: poetic',
                        'puffy: feel,',
                        'ripe: attractive',
                        'rose-colored: color,whitepers',
                        'rosebud: color,whitepers',
                        'sensitive: feel',
                        'shameless: horny',
                        'shy: cute',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'succulent: attractive,taste',
                        'suckable: horny,attractive',
                        'swollen: arousal,size,large,',
                        'tasty: taste,horny,attractive',
                        'tempting: attractive,horny',
                        'tender: feel',
                        'thick: size,large,arousal,',
                        'tiny: size,small,',
                        'wide: size,large'])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")

class Breasts(BodyParts):
    def __init__(self):
        super().__init__()
          
        self.NounList(['boobies: silly,slang,cute,plur',
                        'boobs x4: std,slang,plur',
                        'bosoms x2: std,plur',
                        'breast implants: std,fake,plur',
                        'breasticles x2: silly,crude,slang,plur',
                        'breasts x4: std,clinical,default,plur',
                        'buds x2: cute,desc,small,young,plur',
                        'bust: std,sing',
                        'chest: std,sing',
                        'coconuts: silly,slang,cute,plur',
                        'dumplings: silly,cute,plur',
                        'gazongas: silly,crude,slang,plur',
                        'globes x2: silly,crude,desc,plur',
                        'implants: std,fake,plur',
                        'jugs: silly,crude,slang,plur',
                        'knockers: silly,crude,slang,plur',
                        'orbs x2: silly,desc,plur',
                        'mammaries: silly,clinical,plur',
                        'melons: large,silly,crude,desc,plur',
                        'milk-balloons: large,silly,crude,desc,milk,plur',
                        'mommy milkers: silly,crude,milk,plur',
                        'mounds x2: desc,plur',
                        'tatas: silly,crude,slang,cute,plur',
                        'teats: std,clinical,desc,plur',
                        'tiddies: silly,crude,slang,cute,plur',
                        'titties x2: silly,crude,slang,cute,plur',
                        'tits x3: std,crude,slang,plur',
                        'udders: crude,slang,large,plur',
                    ])
               
        self.AdjList(['black: color,poc',
                    'big: size,large',
                    'bite-sized: size,small',
                    'bouncy: movement',
                    'bountiful: large',
                    'bronzed: color',
                    'brown: color,poc',
                    'budding: small,young',
                    'buxom: large',
                    'chocolate: color,poc,taste',
                    'chubby: large,plussize',
                    'creamy: color,whitepers,taste',
                    'dark: color,poc',
                    'delicious: super,taste',
                    'enchanting: super,attractive',
                    'fair: color,whitepers',
                    'fake: fake,large',
                    'fat x3: large,size,feel,plussize,shape',
                    'fuckable: large,horny',
                    'full: large',
                    'fulsome: large',
                    'generous: super,large',
                    'gentle: feel',
                    'girlish: small,young',
                    'glistening: wet',
                    'glorious: super',
                    'gorgeous: super',
                    'heaving: movement',
                    'heavy: large,feel',
                    'impressive: super,large',
                    'jiggling: movement',
                    'juicy: large,super,feel,taste,horny',
                    'luscious: taste,super',
                    'lush: super',
                    'luxuriant: large,super',
                    'magnificent: large,super',
                    'maternal: older',
                    'nubile: pos,young',
                    'oiled-up: wet',
                    'pale: color,whitepers,young',
                    'pendulous: large,shape,older',
                    'perky: shape,young',
                    'pert: shape,',
                    'petite: size,small,',
                    'plentiful: large,super',
                    'plump: large,feel,shape,',
                    'proud: large,super,',
                    'quivering: movement,',
                    'ripe: feel,shape,young',
                    'rosy: color,whitepers,young',
                    'round: shape',
                    'sensual: poetic',
                    'shapely: shape',
                    'smooth: feel,young',
                    'soft: feel',
                    'statuesque: shape,large,older',
                    'stunning: super',
                    'succulent: super,taste',
                    'suckable: taste,horny',
                    'sumptuous: large,super',
                    'supple: feel,young',
                    'surgically-enhanced: large,shape,fake',
                    'swaying: large,movement',
                    'sweet: super',
                    'swollen: size,large,shape',
                    'tender: feel',
                    'titanic: large',
                    'voluptuous: size,large'])
          
        self.DefaultNoun("breasts")

        self.Nipples = Nipples()

    def CupBuilder(self, NotList = None):
        if NotList == None:
            NotList = []

        CupList = ["A-cup: small,cupsize",
                   "B-cup: small,cupsize",
                   "D-cup: large,cupsize",
                   "double-D cup: large,cupsize",
                   "triple-D cup: large,cupsize",
                  ]

        return WordList(CupList).GetWord(NotList = NotList)

    def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExtraAdjList is None:
            ExtraAdjList = []

        if bCupSize is None:
            bCupSize = CoinFlip()

        if bCupSize and len(ExtraAdjList) == 0:
            ExtraAdjList.append(self.CupBuilder(NotList = NotList))
            #print("  Selected cup size is " + ExtraAdjList[0])

        return super().ShortDescription(sNot = "", ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
          
    def MediumDescription(self, ExtraAdjList = None, sNot = "",  NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExtraAdjList is None:
            ExtraAdjList = []

        if bCupSize is None:
            bCupSize = CoinFlip()

        if bCupSize and len(ExtraAdjList) == 0:
            ExtraAdjList.append(self.CupBuilder(NotList = NotList))
            #print("  Selected cup size is " + ExtraAdjList[0])
               
        return super().MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
    def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExtraAdjList is None:
            ExtraAdjList = []

        if bCupSize is None:
            bCupSize = CoinFlip()

        if bCupSize and len(ExtraAdjList) == 0:
            ExtraAdjList.append(self.CupBuilder(NotList = NotList))
            #print("  Selected cup size is " + ExtraAdjList[0])
          
        return super().FloweryDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
    def RandomDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExtraAdjList is None:
            ExtraAdjList = []

        if bCupSize is None:
            bCupSize = CoinFlip()

        if bCupSize:
            ExtraAdjList.append(self.CupBuilder(NotList = NotList))
            print("  Selected cup size is " + ExtraAdjList[0])
          
        return super().RandomDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
     
          
class Clitoris(BodyParts):
     def __init__(self):
          super().__init__()

          self.NounList(['bean: desc,silly,slang,sing',
                         'clit x3: std,slang,sing',
                         'clitoris x2: std,default,sing',
                         'love-button: silly,sing',
                         'love-nub: silly,sing',
                         'magic button: silly,sing',
                         'nub: desc,sing',
                         'pearl: desc,sing',
                        ])
               
          self.AdjList(['delicate: small,cute',
                        'engorged x2: arousal,large',
                        'erect: arousal',
                        'exposed: nude',
                        'fevered: horny',
                        'hooded: style',
                        'little: size',
                        'pierced: style',
                        'pink x4: color',
                        'pulsating: horny',
                        'pulsing: horny',
                        'secret: cute',
                        'sensitive: feel',
                        'shy: cute',
                        'swollen: size,large,arousal',
                        'tender: feel,cute',
                        'throbbing: horny',
                        'tingling: feel'])
          
          self.DefaultNoun("clit")
          self.IsPlural = False

class VaginaInner(BodyParts):

     def __init__(self):
          super().__init__()

          self.NounList(['baby-maker: silly,crude,sing',
                         'cherry: crude,desc,slang,sing',
                         'cleft: desc,sing',
                         'chamber: sing',
                         'chasm: sing',
                         'cock-hole: crude,slang,sing',
                         'cock-sock: crude,silly,sing',
                         'fuck-tunnel: crude,slang,horny,sing',
                         'fuckhole: crude,slang,horny,sing',
                         'furrow: desc,sing',
                         'gash: desc,crude,slang,sing',
                         'hole: desc,crude,std,sing',
                         'honey-hole: silly,slang,sing',
                         'keyhole: silly,desc,sing',
                         'lewdness: silly,sing',
                         'love-channel: silly,sing',
                         'love-tunnel: silly,slang,sing',
                         'opening: desc,sing',
                         'passage: desc,sing',
                         'slit: desc,crude,sing',
                         'tunnel: desc,sing',
                         'vagina: std,default,sing',
                         'vaginal canal: std,clinical,sing',
                         'vestibule: sing',
                         'womanhood: sing',
                         'womb: sing',
                        ])
                    
          self.AdjList(['cherry: color',
                        'cherry-red: color',
                        'deep x2: size',
                        'dripping: wet',
                        'fleshy: feel,desc',
                        'gaping: open',
                        'glazed: wet',
                        'gooey: wet',
                        'gushing: wet',
                        'hungry: horny,slutty',
                        'juicy: wet,feel,taste,slutty',
                        'lewd: horny',
                        'little x3: tight,size,small',
                        'lustful: horny',
                        'needful: horny,slutty',
                        'pink x3: color',
                        'secret: taboo,cute,virginal',
                        'silken: feel',
                        'slick x2: wet,feel',
                        'sloppy: wet',
                        'snug: tight',
                        'sopping x2: wet',
                        'spread: open,slutty',
                        'succulent: super,taste',
                        'sweet: cute,taste',
                        'tender: feel,virginal',
                        'tight x3: tight',
                        'velvet x2: feel',
                        'wanton: horny',
                        'warm: feel',
                        'well-used: horny,slutty',
                        'virgin: young,virginal',
                       ])
               
          self.DefaultNoun("vaginal canal")
          self.IsPlural = False
     
class VaginaOuterLabia(BodyParts):

     def __init__(self):
          super().__init__()
          
          self.NounList(['labia: std,default,plur',
                         'lips: std,desc,plur',
                         'mons pubis: std,clinical,sing',
                         'mound: desc,sing',
                         'nether lips: desc,plur',
                         'outer labia: std,clinical,plur',
                         'outer pussy lips: std,desc,slang,crude,plur',
                         'pussy lips: std,desc,slang,crude,plur',
                         'vulva: std,clinical,sing'
                        ])

          self.AdjList(['bare: nude',
                        'dewy: wet',
                        'downy: hairy,feel,young',
                        'down-thatched: hairy,feel',
                        'dripping: wet',
                        'fat x2: size,large,shape',
                        'fleshy: feel',
                        'flushed: arousal,color',
                        'fur-lined: hairy',
                        'girlish: young',
                        'gleaming wet: wet',
                        'glistening: wet',
                        'hairless: hairless',
                        'honeyed: wet,taste',
                        'juicy: wet,taste,attractive',
                        'lickable: horny',
                        'luscious: taste,attractive',
                        'lush: attractive,superlative',
                        'moist: wet',
                        'naked: nude',
                        'peach-fuzzed: hairy,young',
                        'pink: color,hairless',
                        'plump x3: size,large,shape',
                        'puffy: arousal,shape',
                        'shameless: horny',
                        'shaved: hairless',
                        'shaven: hairless',
                        'silken: feel',
                        'slick: wet,feel',
                        'smooth: feel,hairless',
                        'succulent: taste,super',
                        'suckable: horny',
                        'supple: feel',
                        'sweet: super,cute',
                        'swollen: arousal,shape',
                        'tender: feel',
                        'trim: hairy',
                        'wet: wet'])
               
          self.DefaultNoun("mons pubis")

class VaginaInnerLabia(BodyParts):

     def __init__(self):
          super().__init__()

          self.NounList(['beef-curtains: silly,crude,plur',
                         'butterfly wings:  desc, cute, plur',
                         'cunt-lips: crude,plur',
                         'flaps: desc,crude,plur',
                         'flower petals: desc,cute,plur',
                         'folds: desc,plur',
                         'fringe: desc,plur',
                         'inner labia: std,default,clinical,plur',
                         'labia: std,default,clinical,plur',
                         'lips: desc,plur',
                         'meat-curtains: crude, silly, plur',
                         'meat-flaps: crude, silly, plur',
                         'nether-lips:  plur',
                         'petals: desc,cute,plur',
                         'piss-flaps: crude,plur',
                         'pussy flaps: desc,crude,plur',
                         'pussy lips: std,default,slang,plur',
                         'sex-flaps: silly,crude,plur',
                         'sex-lips: silly,plur',
                         'wizard sleeve: silly,crude,sing',
                        ])

          self.AdjList(['beefy: meaty',
                        'chewy: taste,meaty',
                        'dangling x2: hanging,shape',
                        'dark: color',
                        'delicate: small,attractive,cute',
                        'dewy x2: wet,cute',
                        'drooping: hanging,shape',
                        'fleshy: meaty',
                        'gossamer: attractive,cute',
                        'lengthy: size,long',
                        'lickable: horny',
                        'little: size,small',
                        'long: long',
                        'lush: attractive,cute',
                        'meaty x2: meaty',
                        'moist: wet',
                        'pink: color',
                        'purplish: color',
                        'ruffled: shape',
                        'secret: taboo,virginal',
                        'shameless: horny',
                        'silken: feel,attractive,cute',
                        'shy: virginal,cute',
                        'succulent: taste,super',
                        'suckable: horny',
                        'tasty: taste,horny',
                        'tender: feel,cute',
                        'trim: size, small',
                        'well-used: slutty',
                        'velvet: attractive, feel'])
                              
          self.DefaultNoun("inner labia")
               
class Vagina(BodyParts):
     InnerVag = []
     InnerLabia = []
     OuterLabia = []
     Clitoris = []
     
     def __init__(self):
          super().__init__()
          
          self.NounList(['cherry pie: silly,cute,slang,young,sing',
                         'cock-garage: silly,crude,slang,sing',
                         'cock-sock: silly,crude,slang,sing',
                         'cooch: std,slang,sing',
                         'coochie: std,slang,sing',
                         'cunny: std,slang,cute,sing',
                         'cunt x3: std,slang,crude,sing',
                         'cunt-hole: crude,slang,sing',
                         'flower: desc,sing',
                         'fuckhole: crude,slang,sing',
                         'fur-burger: hairy,crude,silly,slang,sing',
                         'honey-hole: silly,slang,cute,sing',
                         'honeypot: silly,slang,cute,sing',
                         'love-muffin: silly, slang, cute, sing',
                         'muff: hairy,std,slang,sing',
                         'muffin: hairy,std,slang,sing',
                         'peach: desc,cute,sing',
                         'pie: silly,slang,cute,sing',
                         'pussy x4: std,slang,crude,sing',
                         'quim: std,crude,sing',
                         'sex: std,sing',
                         'snatch: std,slang,sing',
                         'twat x2: std,slang,crude,sing',
                         'vagina x4: std,clinical,sing',
                         'womanhood: std,sing',
                        ])
                            
          self.AdjList(['bare: nude',
                         'cherry: young,virginal',
                         'clenched: tight',
                         'delightful: super',
                         'dewy: wet',
                         'down-thatched: hairy,young',
                         'dripping: wet',
                         'exposed: bare,horny',
                         'fuckable: horny',
                         'fur-lined: hairy',
                         'girlish: young',
                         'gleaming wet: wet',
                         'glistening: wet',
                         'gushing: wet',
                         'hairless: hairless',
                         'honeyed: taste',
                         'horny: horny,arousal',
                         'hungry: horny',
                         'juicy: taste,super,slutty',
                         'leaky: wet,slutty',
                         'lewd: horny',
                         'lickable: taste,horny',
                         'luscious: super,taste',
                         'lush: super',
                         'lustful: horny',
                         'moist: wet',
                         'naked: nude',
                         'needful: horny,slutty',
                         'peach-fuzzed: hairy,young',
                         'puffy: shape,arousal',
                         'shameless: horny,slutty',
                         'silken: feel',
                         'slick: wet,feel',
                         'slutty: slutty,horny',
                         'smooth: feel,hairless',
                         'sopping: wet',
                         'succulent: super,taste',
                         'suckable: horny,taste',
                         'supple: feel,hairless,young',
                         'sweet: super',
                         'swollen: arousal,shape,feel',
                         'tender: feel,cute',
                         'tight x4: tight',
                         'trim: hairy,cute',
                         'unsullied: virginal',
                         'velvet: feel',
                         'wanton: horny',
                         'well-used: slutty',
                         'willing: horny'])

          # todo: Add "is wet" parameter
          
          self.DefaultNoun("vagina")
          self.IsPlural = False
          self.InnerVag = VaginaInner()
          self.OuterLabia = VaginaOuterLabia()
          self.InnerLabia = VaginaInnerLabia()
          self.Clitoris = Clitoris()

class AnusFemale(BodyParts):
     def __init__(self):
          super().__init__()

          self.NounList(['anus x4: std,default,clinical,sphincter,sing',
                         'arse-cunt: crude,orifice,sing',
                         'ass: std,orifice,sing',
                         'asshole x4: std,slang,crude,sphincter,sing',
                         'back orifice: desc,clinical,orifice,sing',
                         'back passage: desc,orifice,sing',
                         'back-pussy: silly,crude,slang,orifice,sing',
                         'backdoor: desc,slang,orifice,sing',
                         'bowels: std,plur',
                         'brown hole: desc,slang,crude,sphincter,sing',
                         'bunghole: silly,crude,slang,sphincter,sing',
                         'chocolate starfish: silly,crude,slang,sphincter,sing',
                         'corn hole: silly,crude,slang,sphincter,sing',
                         'dirt-pipe: crude,slang,orifice,sing',
                         'dirt-box: crude,slang,orifice,sing',
                         'fart-blaster: silly,crude,slang,orifice,sing',
                         'fart-box: silly,crude,slang,orifice,sing',
                         'fart-hole: silly,crude,slang,sphincter,sing',
                         'heinie hole: desc,slang,cute,sphincter,sing',
                         'knot: desc,sphincter, sing',
                         'poop-chute: crude,slang,desc,orifice,sing',
                         'poop-trap: crude,slang,sing,sphincter',
                         'rear orifice: desc, clinical, orifice,sing',
                         'rectal cavity: desc, clinical, orifice,sing',
                         'rectum: std,clinical,orifice,sing',
                         'ring: desc,sphincter,sing',
                         'rosebud: desc,slang,cute,crude,sing',
                         'shit-hole: crude,slang,desc,orifice,sing',
                         'shitter: crude,slang,orifice,sing',
                         'sphincter x2: std,clinical,sphincter,sing',
                         'starfish x2: silly,cute,slang,sphincter,sing',
                        ])
       
          self.AdjList(['brown: color',
                        'clenched: small,tight,action',
                        'flexing: action',
                        'forbidden: taboo',
                        'fuckable: horny',
                        'gaping: large,gape',
                        'knotted: small,tight,desc',
                        'lewd: horny',
                        'little x4: small,cute,',
                        'loose: gape',
                        'nasty: taboo',
                        'naughty: horny',
                        'pert: cute,young',
                        'puckered: action',
                        'rusty: desc,color',
                        'shy: horny,taboo',
                        'smooth: feel,desc',
                        'snug x2: small,tight,cute,'
                        'taboo: taboo',
                        'tender: feel,desc,cute',
                        'tight x4: small,tight',
                        'wanton: horny',
                        'well-used: gape,old',
                        'willing: horny',
                        'winking: small,tight,action',
                       ])
          
          self.DefaultNoun("anus")
          
class ButtocksFemale(BodyParts):
     def __init__(self):
          super().__init__()
     
          self.NounList(['buns: std,plur',
                          'butt-cheeks: std,plur',
                          'buttocks: std,clinical,plur',
                          'cheeks:std,plur',
                         ])
               
          self.AdjList(['ample: large,curvy',
                        'big: size,large',
                        'black: color,poc',
                        'bronzed: color',
                        'brown: color,poc',
                        'bubble-butt: shape',
                        'bubble-shaped: shape',
                        'chubby: shape,plussize,curvy',
                        'coffee-colored: color,poc',
                        'creamy: color,whitepers',
                        'curvaceous: shape,curvy',
                        'curvy: curvy,shape',
                        'cute: cute',
                        'dark: color,poc',
                        'fat: large,plussize',
                        'honeyed: taste',
                        'jiggling: movement',
                        'juicy: wet,taste,horny',
                        'lickable: taste,horny',
                        'luscious: super,large',
                        'muscular: strong',
                        'pale: color,whitepers',
                        'petite: size,small',
                        'pink: color,whitepers',
                        'plump: large,plussize,curvy',
                        'rosy: color,whitepers',
                        'rotund: large,plussize',
                        'round: shape',
                        'rounded: shape',
                        'shapely x3: shape,attractive',
                        'smooth: hairless,feel,texture',
                        'squeezable x2: horny',
                        'succulent: super,attractive,horny',
                        'sun-browned: color',
                        'sun-kissed: color',
                        'supple: feel,texture,young',
                        'sweet: attractive',
                        'tender: feel',
                        'tanned: color',
                        'thick x3: size,large,shape,curvy',
                        'tight: size,small',
                        'trim: size,small',
                        'voluptuous: shape,curvy,attractive',
                        'well-rounded: shape',
                        'well-tanned: color',
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksFemale()
          
          self.NounList(['ass: std,default,sing',
               'backside: std,sing',
               'behind: std,sing',
               'booty: std,cute,slang,sing',
               'bottom: std,desc,sing',
               'bum: std,cute,slang,sing',
               'butt: std,slang,sing',
               'gluteous maximus: std,clinical,sing',
               'heinie: std,cute,slang,sing',
               'rump: desc,sing',
               'tush: cute,slang,sing',
               'tushy: cute,slang,sing'])
               
          self.AdjList(['ample',
               'bountiful',
               'broad',
               'bubble-shaped',
               'chubby',
               'curvaceous',
               'curvy',
               'cute little',
               'fat',
               'fuckable',
               'generous',
               'glistening',
               'huge',
               'honeyed',
               'jiggling',
               'juicy',
               'lush',
               'luscious',
               'muscular',
               'nubile',
               'pert',
               'plump',
               'ripe',
               'rotund',
               'round',
               'rounded',
               'shameless',
               'shapely',
               'succulent',
               'supple',
               'sweet',
               'tender',
               'thick','thick',
               'tight',
               'trim',
               'voluptuous',
               'womanly',
               'well-rounded'])
               
          #self.ColorList(['bronzed',
          #                    'black',
          #                    'brown',
          #                    'coffee-colored',
          #                    'creamy',
          #                    'dark',
          #                    'pale',
          #                    'pink',
          #                    'rosy',
          #                    'sun-kissed',
          #                    'tanned'
          #                  ])
          
          self.DefaultNoun("ass")
          
class BodyFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['anatomy: std,sing',
                         'body x4: std,default,sing',
                         'curves: plur',
                         'figure: std,sing',
                         'form: std,sing',
                         'physique: std,sing'])
               
          self.AdjList(['beautiful: attractive,super',
                        'black: color,poc',
                        'bronzed: color',
                        'brown: color,poc',
                        'busty: bigtits',
                        'buxom: bigtits',
                        'coffee-colored: color,poc',
                        'curvaceous: shape,curvy,bigtits,attractive',
                        'curvy: shape,curvy',
                        'feminine: curvy',
                        'gorgeous: super,attractive',
                        'leggy: longlegs',
                        'little: size,small',
                        'lush: super',
                        'luxuriant: super',
                        'mocha: color,poc',
                        'model-esque: attractive',
                        'nubile: young,virginal',
                        'pale: color,whitepers',
                        'pink: color,whitepers,young',
                        'plus-size: size,large,plussize',
                        'ravishing: super,attractive,horny',
                        'ripe: attractive',
                        'sensual: attractive,super',
                        'sexy: attractive,super',
                        'shameless: horny',
                        'shapely: attractive,bigtits',
                        'slender: slender',
                        'statuesque: bigtits,older',
                        'stunning: super,attractive',
                        'sultry: attractive',
                        'sun-bronzed: color',
                        'sun-kissed: color',
                        'sweet: super,attractive,taste',
                        'tanned: color',
                        'teenage: young',
                        'tight: slender,size,small',
                        'voluptuous: bigtits,curvy',
                        'womanly: curvy',
                        'young: young',
                        'youthful: young',
                       ])
          
          self.DefaultNoun("body")
          self.DefaultAdj("nubile")

          self.Hair = Hair()
          self.Face = Face()
          self.Eyes = Eyes()
          self.Lips = Lips()
          self.Mouth = Mouth()
          self.Hips = Hips()
          self.Back = BackFemale()
          self.Legs = Legs()
          self.Skin = Skin()
          self.Thighs = Thighs()
          self.Breasts = Breasts()
          self.Vagina = Vagina()
          self.Ass = AssFemale()
          
     
     def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
          sPartDesc = ""
          
          if sPossessive is None:
               sPossessive = ""
          
          PartNotList = ['naked','nude','bare','exposed']
          bAddArticles = True
          
          if isinstance(part, Skin):
               PartNotList += ['warm','tender']
               bAddArticles = False 
          elif isinstance(part, Hair): 
               bAddArticles = False 
          elif isinstance(part, Eyes):
               bAddArticles = False 
          elif isinstance(part, Mouth):
               bAddArticles = True 
               PartNotList += ['open','mouth-hole','lewd','insatiable','willing']
          elif isinstance(part, Lips):
               bAddArticles = False 
          elif isinstance(part, Hips):
               bAddArticles = False 
          elif isinstance(part, Legs):
               bAddArticles = False 
          elif isinstance(part, Breasts):
               PartNotList += ['boobies','boobs','buds','coconuts','dumplings','gazongas',
                                        'globes','jugs','knockers','mammaries','melons','teats','titties',
                                        'delicious','gentle','girlish','jiggling','lus','nubile',
                                        'pendulous','pert','quivering','ripe','sensual','surgic',
                                        'sweet','swollen','tender']
               bAddArticles = False 
               
          #print(" - PartNotList is [" + str(PartNotList) + "]\n")
          if not sPossessive == "":
               bAddArticles = False 
               sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          else:
               sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
               if bAddArticles:
                    sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
          sBodyDesc = ""
          
          if sPossessive is None:
               sPossessive = ""
          
          if iNum < 3:
               iNum = 3
          if iNum > 5:
               iNum = 5
               
          hair = self.Hair
          face = self.Face 
          eyes = self.Eyes 
          if CoinFlip():
               mouth = self.Lips 
          else:
               mouth = self.Mouth 
          hips = self.Hips 
          back = self.Back
          legs = self.Legs 
          skin = self.Skin
          boobs = self.Breasts 
          body = self
          
          PartPriorities = [[hair,1],
                                [eyes,1],
                                [face,2],
                                [mouth,3],
                                [legs,4],
                                [hips,4],
                                [back,5],
                                [skin,6],
                                [body,6],
                                [boobs,7]]
          
          PartGroups = []
          
          if iNum == 3:
               for part1 in PartPriorities: #skin 6
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] == part1[1] and not part2[0] == part1[0]:
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        PartGroups.append([part1[0],part2[0],part3[0]])
                         
          elif iNum == 4:
               for part1 in PartPriorities:
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                             if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                  PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
     
          else:
               for part1 in PartPriorities:
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                             if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                  for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
                                                       if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
                                                            PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
          
          SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
          
          iLoops = 0
          while iLoops < iNum:
               sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc
          
     def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None, NotList = None):
          sPartDesc = ""

          if NotList is None:
              NotList = []
          
          if sPossessive is None:
               sPossessive = ""
          
          bAddArticles = True
          
          if isinstance(part, Hips):
               bAddArticles = False 
          elif isinstance(part, Skin):
               bAddArticles = False 
          elif isinstance(part, Legs):
               bAddArticles = False 
          elif isinstance(part, Thighs):
               bAddArticles = False 
          elif isinstance(part, Breasts):
               bAddArticles = False 
          
          if not sPossessive == "":
               bAddArticles = False 
               sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = NotList)
          else:
               sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = NotList)
          
          if bAddArticles:
               sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bExplicit = False, bAllowLongDesc = True, sPossessive = None, NotList = None):
          sBodyDesc = ""

          if NotList is None:
              NotList = []
          
          if sPossessive is None:
               sPossessive = ""
               sPossessive = ""
          
          if iNum < 3:
               iNum = 3
          if iNum > 5:
               iNum = 5
               
          hair = self.Hair
          face = self.Face 
          eyes = self.Eyes 
          if CoinFlip():
               mouth = self.Lips 
          else:
               mouth = self.Mouth 
          hips = self.Hips 
          back = self.Back
          legs = self.Legs 
          skin = self.Skin
          thighs = self.Thighs 
          nipples = self.Breasts.Nipples
          boobs = self.Breasts 
          pussy = self.Vagina 
          innerlabia = self.Vagina.InnerLabia
          outerlabia = self.Vagina.OuterLabia
          cunthole = self.Vagina.InnerVag 
          ass = self.Ass 
          asshole = self.Ass.Anus 
          body = self
          
          PartPriorities = [[legs,1],
                                [hips,1],
                                [thighs,2],
                                [back,3],
                                [skin,4],
                                [body,4]]
          
          if bBoobs:
               PartPriorities.append([boobs,5])
               PartPriorities.append([nipples,6])
          if bAss:
               PartPriorities.append([ass,7])
          if bPussy:
               PartPriorities.append([pussy,7])
          if bExplicit:
               PartPriorities.append([innerlabia,8])
               PartPriorities.append([outerlabia,8])
               PartPriorities.append([cunthole,8])
               PartPriorities.append([asshole,9])
          
          PartGroups = []
          
          if iNum == 3:
               for part1 in PartPriorities: #skin 6
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] == part1[1] and not part2[0] == part1[0]:
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        PartGroups.append([part1[0],part2[0],part3[0]])
                         
          elif iNum == 4:
               for part1 in PartPriorities:
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                             if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                  PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
     
          else:
               for part1 in PartPriorities:
                    for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                         if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                              for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                   if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                        for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                             if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                  for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
                                                       if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
                                                            PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
          
          SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
          
          iLoops = 0
          while iLoops < iNum:
               sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               NotList += re.split(r',|\w|', sBodyDesc)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc

     def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
          Parts = []
          AllParts = []
          
          if bIncludeInners:
               AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc = bAllowShortDesc))
          else:
               AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               
          for x in sorted(sample(range(0, len(AllParts)), iNum)):
               Parts.append(AllParts[x])
               
          return Parts
                    
     def GetHoles(self, bIncludeMouth = True):
          Holes = []
          
          if bIncludeMouth:
               Holes = [3]
          
               Holes[0] = self.Mouth.RandomDescription()
               Holes[1] = self.Vagina.RandomDescription()
               Holes[2] = self.Ass.Anus.RandomDescription()
          else:
               Holes = [2]
               
               Holes[0] = self.Vagina.RandomDescription()
               Holes[1] = self.Ass.Anus.RandomDescription()
          
          return Holes
          
     def GetRandomHole(self, bIncludeMouth = True, bAllowShortDesc = True, bAllowLongDesc = True):
          sHole = ""
          Holes = []
          if bIncludeMouth:          
               Holes.append(self.Mouth.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
          else:
               Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
          
          iRand = randint(0, len(Holes) - 1)
          sHole = Holes[iRand]
          
          return sHole
          
class PenisHead(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['cock-head: silly,slang,sing',
                         'dick-tip: silly,crude,slang,sing',
                         'head x3: std,default,sing',
                         'helmet: desc,sing',
                         'knob x2: crude,silly,desc,slang,sing',
                         'mushroom: desc,sing',
                         'tip x3: std, default,sing',
                        ])
               
          self.AdjList(['broad',
                        'brown',
                        'bulging',
                        'dripping',
                        'engorged',
                        'fat',
                        'glistening',
                        'pulsating',
                        'purple',
                        'red',
                        'smooth',
                        'swollen',
                        'thick',
                        'throbbing',
                        'tumescent'])
          
          self.DefaultNoun("head")
          self.IsPlural = False
          
class Testicles(BodyParts):
     def __init__(self):
          super().__init__()

          self.NounList(['balls x3: std,default,plur', 
                         'ballsack x2: silly,crude,slang,plur',
                         'bollocks: silly,crude,plur',
                         'gonads: std, clinical, plur',
                         'nuts: silly,slang,plur',
                         'nutsack: silly,slang,crude,sing',
                         'sack: desc,sing',
                         'scrotum x2: std,clinical,sing',
                         'silk purse: desc,sing',
                         'testicles x2',
                        ])
               
          self.AdjList(['dangling',
                        'downy',
                        'down-covered',
                        'fleshy',
                        'hairy',
                        'heavy',
                        'hefty',
                        'pendulous',
                        'round',
                        'satin',
                        'silken',
                        'soft',
                        'smooth',
                        'swaying',
                        'swinging',
                        'tender',
                        'wrinkled'])
          
          self.DefaultNoun("testicles")

class Penis(BodyParts):
     def BuildAPenis(self, NotList = []):
          sPenis = ""
          
          iRandFront = 0
          iRandBack = 0
          
          iRandFront = randint(0,len(self.PenisFrontPart) - 1)
          iRandBack = randint(0,len(self.PenisBackPart) - 1)
          sFrontPart = self.PenisFrontPart[iRandFront]
          sBackPart = self.PenisBackPart[iRandBack]
          
          while FoundIn(sFrontPart, sBackPart) or FoundIn(sFrontPart, NotList) or FoundIn(sBackPart, NotList):
               iRandFront = randint(0,len(self.PenisFrontPart) - 1)
               iRandBack = randint(0,len(self.PenisBackPart) - 1)
               sFrontPart = self.PenisFrontPart[iRandFront]
               sBackPart = self.PenisBackPart[iRandBack]
               
          sPenis = sFrontPart + "-" + sBackPart
          
          while sPenis in self.GetNounList("silly"):
               iRandFront = randint(0,len(self.PenisFrontPart) - 1)
               iRandBack = randint(0,len(self.PenisBackPart) - 1)
               sFrontPart = self.PenisFrontPart[iRandFront]
               sBackPart = self.PenisBackPart[iRandBack]
               
               while FoundIn(sFrontPart, sBackPart) or FoundIn(sFrontPart, NotList) or FoundIn(sBackPart, NotList):
                    iRandFront = randint(0,len(self.PenisFrontPart) - 1)
                    iRandBack = randint(0,len(self.PenisBackPart) - 1)
                    sFrontPart = self.PenisFrontPart[iRandFront]
                    sBackPart = self.PenisBackPart[iRandBack]
                    
               sPenis = sFrontPart + "-" + sBackPart
               
          return sPenis
          
     def __init__(self, bAllowBAP = True):
          super().__init__()

          self.NounList(['boner: silly,crude,hard,sing',
                         'choad: crude,slang,small,sing',
                         'cock x3: std,default,slang,crude,sing',
                         'cock-meat: crude,sing',
                         'cocksicle: silly,crude,slang,sing',
                         'dick x3: std,slang,sing',
                         'erection x2: std,clinical,hard,sing',
                         'girth: desc,sing',
                         'goo-gun: silly,crude,semen,sing',
                         'hard-on: std,slang,hard,sing',
                         'hardness: desc,hard,sing',
                         'hot-rod: silly,crude,slang,sing',
                         'joystick: silly,slang,sing',
                         'lady-dagger: silly,slang,sing',
                         'love-gun: silly,slang,sing',
                         'meat: crude,slang,sing',
                         'member: std,clinical,sing',
                         'monster: silly,hard,sing',
                         'organ: std,clinical,sing,',
                         'pecker: std,slang,small',
                         'penis x4: std,clinical,sing',
                         'phallus: std,sing',
                         'pole: desc,hard,sing',
                         'popsicle: silly,slang,sing',
                         'prick: std,slang,crude,sing',
                         'ramrod: crude,desc,sing',
                         'rod: desc,sing',
                         'sausage: desc,silly,slang,crude,sing',
                         'schlong: silly,slang,sing',
                         'serpent: desc,sing',
                         'shaft: desc,sing',
                         'snake: desc,sing',
                         'stalk: desc,sing',
                         'stem: desc,sing',
                         'thing: std,silly,sing',
                         'tool: std, slang,sing',
                         'wood: crude,slang,sing'
                        ])

          self.AdjList(['bald: hairless',
                        'black: color,poc',
                        'beautiful: super',
                        'beefy: large,taste',
                        'bent: shape',
                        'big x4: size,large',
                        'broad x2: size,wide',
                        'bulging x2: hard,large,shape'
                        'burning: feel,warm',
                        'carefully man-scaped: style',
                        'circumcized: cut',
                        'crooked: shape',
                        'curved: shape',
                        'delicious: taste,horny,super',
                        'dripping: wet',
                        'engorged x2: hard',
                        'enormous: size,large',
                        'enormously erect: size,large,hard',
                        'erect x2: hard',
                        'fat x4: size,large',
                        'fevered: feel,warm',
                        'feverish: feel,warm',
                        'firm x3: hard,feel',
                        'fully engorged: hard',
                        'fully erect: hard',
                        'girthy x2: size,wide',
                        'glistening: wet,shiny',
                        'god-like: super',
                        'gorgeous: super,attractive',
                        'greasy x4: feel,wet',
                        'hairy: hairy',
                        'hairless: hairless',
                        'hard x3: hard',
                        'hardened: hard',
                        'heavy: large,feel',
                        'hefty: large',
                        'hooked: shape',
                        'hot x2: feel,attractive,super',
                        'huge: size,large',
                        'hugely erect: size,large,hard',
                        'impressive: super',
                        'legendary: super',
                        'lengthy: length,long',
                        'long: length,long',
                        'lovingly man-scaped: style',
                        'lustful x2: horny',
                        'magnificient: super',
                        'massive: size,large',
                        'massively erect: size,large,hard',
                        'meaty x3: feel,taste',
                        'monstrous: super,large',
                        'mouth-watering: horny',
                        'oily: wet,shiny',
                        'pierced: style',
                        'pink: color,whitepers',
                        'powerful: horny,super',
                        'pretty: attractive',
                        'proud: poetic',
                        'pulsating: feel,throb',
                        'purple: color',
                        'raging: hard',
                        'rampant: hard',
                        'red: color',
                        'ribbed: feel,shape',
                        'rigid: hard',
                        'rock-hard: hard',
                        'serpentine: shape',
                        'silken: feel',
                        'smooth x3: hairless,feel',
                        'stiff x2: hard',
                        'strong x3: super,horny',
                        'swollen x2: hard,large',
                        'tall: length,long',
                        'tasty x3: taste,horny',
                        'thick x3: size,wide',
                        'throbbing x2: feel,throb',
                        'towering: length,long,size,large',
                        'tumescent: hard',
                        'turgid x2:hard',
                        'uncircumcized: style, cut',
                        'uncut: style, cut',
                        'veiny x4: texture',
                        'virile: attractive',
                        'warm: feel,warm',
                        'wrinkled: texture,older'
                        'well-oiled: shiny,wet',
                        'youthful: young',
                       ])
               
          self.PenisFrontPart = ['beef',
                                 'daddy',
                                 'flesh',
                                 'fuck',
                                 'love',
                                 'man',
                                 'meat',
                                 'rape',
                                 'splooge',
                                ]
               
          self.PenisBackPart = ['bayonette',
                               'bone',
                               'burrito',
                               'hammer',
                               'lance',
                               'meat',
                               'missile',
                               'monster',
                               'pipe',
                               'pistol',
                               'pole',
                               'popsicle',
                               'python',
                               'rocket',
                               'rod',
                               'rifle',
                               'sausage',
                               'serpent',
                               'shaft',
                               'snake',
                               'stack',
                               'stalk',
                               'stick',
                               'sword',
                               'tool',
                               'torpedo',
                               'tube',
                               'weapon',
                               'worm']
          
          self.DefaultNoun("cock")
          self.IsPlural = False
          self.Head = PenisHead()
          self.Testicles = Testicles()
          
          if bAllowBAP:
               for i in range(0, int(self.NounListLen() * (2/3))):
                    sBAP = self.BuildAPenis()
                    self.AddNounToList(sBAP,"silly")
                    self.AddNounToList(sBAP,"crude")
     
     def GetRandomPenisPart(self, sNot = None, NotList = None, bAllowShortDesc = False):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)
               
          iRand = randint(1,3)
          
          if iRand == 1:
               return self.Head.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
          elif iRand == 2: 
               return self.Testicles.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
          else:
               return self.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
               
     def GenerateLength(self):
          sLength = ""
          
          sLength = str(randint(6, 13))
          if CoinFlip():
               sLength += " 1/2"
          sLength += "-inch"
          
          return sLength
               
     def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().ShortDescription(sNot = "", ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
          
     def MediumDescription(self, ExtraAdjList = None, sNot = "",  NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
               
          return super().MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
     def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().FloweryDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
     def RandomDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().RandomDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
     
class Semen(BodyParts):
     def __init__(self):
          super().__init__()

          self.NounList(['baby batter: silly,slang,sing',
                         'baby gravy: silly,crude,slang,sing',
                         'cock-milk: crude,slang,sing',
                         'cock-snot: crude,silly,slang,sing',
                         'cream: desc,sing',
                         'cum x4: std,slang,sing',
                         'daddy-sauce: silly,crude,slang,sing',
                         'gravy: desc,crude,sing',
                         'jizm: crude,slang,sing',
                         'jizz x2: crude,slang,sing',
                         'load x2: slang,sing',
                         'lotion: desc,sing',
                         'love juice: silly,slang,sing',
                         'man-custard: desc,silly,slang,sing',
                         'man-o-naise: silly,sing',
                         'man-milk: desc,silly,sing',
                         'man-seed: desc,sing',
                         'nut-butter: silly,slang,sing',
                         'penis pudding: silly,crude,slang,sing',
                         'sauce: desc,sing',
                         'seed x2: std,sing',
                         'semen x3: std,clinical,default,sing',
                         'sperm x2: std,clinical,plur',
                         'splooge: std,slang,sing',
                         'spunk: std,slang,sing',
                         'throat yogurt: silly,crude,slang,sing',
                         'trouser gravy: silly,crude,slang,sing',
                         'weiner sauce: silly,crude,slang,sing',
                        ])
               
          self.AdjList(['creamy x3: taste,color',
                        'delicious: taste,super',
                        'glossy: shiny',
                        'gooey x3: sticky',
                        'hot x3: feel,warm',
                        'nasty: gross,horny',
                        'nourishing: taste,horny',
                        'oozing: sticky',
                        'ropy: shape',
                        'salty x2: taste',
                        'silken: feel',
                        'silky: feel',
                        'sloppy x2: sticky,gross',
                        'sticky x4: sticky',
                        'tasty: taste,horny',
                        'thick x4: thick',
                        'warm x3: feel,warm',
                        'white-hot x2: warm',
                        'yummy: taste,horny',
                        'cream-colored: color',
                        'milky: color',
                        'pearly: color,shiny',
                        'pearlescent: color,shiny'])
          
          self.DefaultNoun("semen")
          self.DefaultAdj("gooey")
          
class ButtocksMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['buns: std,cute,desc,plur',
                         'butt cheeks: std,slang,plur',
                         'buttocks: std,default,clinical,plur',
                         'glutes: std,strong,plur',
                         ])
               
          self.AdjList(['beefy: large',
                        'broad: size,wide',
                        'bronzed: color',
                        'chiseled: shape',
                        'compact: size,small,shape',
                        'hairy: hairy',
                        'lean: shape',
                        'manly: attractive',
                        'masculine: attractive',
                        'muscular: strong',
                        'rock-hard: feel,strong',
                        'sexy: attractive',
                        'smooth: hairless',
                        'strapping: strong',
                        'swole: size,large,shape',
                        'taut: strong',
                        'tan: color',
                        'tight x2: size,small,shape',
                        'trim: size,narrow,shape',
                        'virile: attractive',
                        'well-defined: shape'
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksMale()
          
          self.NounList(['ass x3: std,slang,default,sing',
                         'backside: std,sing',
                         'behind: std,sing',
                         'bottom: std,sing',
                         'bum: std,cute,sing',
                         'buns: desc,cute,plur',
                         'butt x3: std,sing',
                         'gluteous maximus: std,clinical,sing',
                         'rump: std,sing',
                         'tush: silly,slang,sing',
                        ])
               
          self.AdjList(['beefy: large',
                        'broad: size,wide',
                        'bronzed: color',
                        'chiseled: shape',
                        'compact: size,small',
                        'hairy: hairy',
                        'lean: size,small',
                        'manly: attractive',
                        'masculine: attractive',
                        'muscular: strong',
                        'naked: nude',
                        'powerful: strong,super',
                        'rippling: shape',
                        'rock-hard: feel',
                        'smooth: hairless',
                        'strapping:  strong',
                        'supple: feel',
                        'taut: shape,strong',
                        'tight: shape,small',
                        'trim: shape,small',
                        'virile: attractive',
                        'well-defined: shape',
                       ])
          
          self.DefaultNoun("buttocks")
          
class SkinMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['skin x4: default,std,sing',
                         'flesh x2: std,sing',
                         'hide: std,sing',
                        ])
               
          self.AdjList(['bare: nude',
                        'bronzed: color',
                        'brown: color,poc',
                        'coffee-colored: color,poc',
                        'dark: color,poc',
                        'ebony: color,poc',
                        'exposed: bare',
                        'freckled: color,whitepers',
                        'glistening: shiny,wet,texture',
                        'hairy: hairy',
                        'leathery: feel,texture,older',
                        'naked: nude',
                        'pale: color,whitepers',
                        'rough: texture',
                        'rugged: texture',
                        'smooth: texture',
                        'sun-browned: color',
                        'supple: feel,young,texture',
                        'tanned: color',
                        'tough: texture',
                        'warm: feel',
                        'weathered: texture,older',
                        'youthful: young'])
          
          self.DefaultNoun("skin")
          self.DefaultAdj("rugged")
          
class ShouldersMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['shoulders'])
               
          self.AdjList(['bare: nude',
                        'brawny: strong,large',
                        'broad: size,wide',
                        'bronzed: color',
                        'brown: color,poc',
                        'coffee-colored: color,poc',
                        'dark: color,poc',
                        'ebony: color,poc',
                        'freckled: color,whitepers',
                        'mighty: strong',
                        'muscular: shape,strong',
                        'naked: nude',
                        'powerful: super',
                        'rugged: shape',
                        'square: shape,wide',
                        'strong: strong',
                        'sturdy: strong',
                        'sun-browned: color',
                        'tanned: color',
                        'well-built: shape',
                        'wide: size,wide'])

          self.DefaultNoun("shoulders")
          self.DefaultAdj("broad")
          
class MusclesMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['muscles: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: large,strong',
                        'broad: size,large,wide',
                        'bronzed: color',
                        'bulging: shape',
                        'burly: strong',
                        'chiseled: shape',
                        'dark: color',
                        'hard: feel',
                        'hulking: size,large',
                        'impressive: super',
                        'lean: size,small',
                        'magnificent: super',
                        'massive: size,large',
                        'mighty: strong',
                        'powerful: strong',
                        'robust: strong',
                        'rugged: shape',
                        'sinewy: poetic',
                        'strapping x2: poetic',
                        'strong: strong',
                        'sturdy: strong',
                        'supple: feel,young',
                        'tanned: color',
                        'taut: shape',
                        'toned: shape',
                        'tight: feel',
                        'well-built: size,large',
                        'well-defined: shape',
                        'whip-cord: shape',
                        'wood-carved: shape'])
          
          self.DefaultNoun("muscles")
          self.DefaultAdj("strapping")

class NipplesMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['nipples: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'bared: nude',
                        'black: color, poc',
                        'bold: hard',
                        'broad: size,large',
                        'brown: color,',
                        'chocolate: color',
                        'dark: color,',
                        'dusky: color',
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'firm: arousal',
                        'handsome: super,attractive',
                        'hard: arousal,',
                        'perfect: super,attractive',
                        'pert: arousal,cute',
                        'pierced: style',
                        'pink: color,whitepers',
                        'prominent: poetic',
                        'reddish: color',
                        'small: size,small',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'sun-kissed: color',
                        'tanned: color',
                        'thick: size,large,arousal,',
                        'tiny: size,small,',
                        'turgid: arousal',
                        'wide: size,large'])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")
          
class ChestMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['chest x4: std,default,sing',
                         'pectorals: std,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: muscular',
                        'broad: size,large,wide',
                        'bronzed: color',
                        'brown: color,poc',
                        'burly: muscular,size,large,shape',
                        'coffee-colored: color,poc',
                        'compact: size,small',
                        'dark: color,poc',
                        'dark-thatched: hairy',
                        'ebony: color,poc',
                        'expansive: size,large,wide',
                        'hairy: hairy',
                        'lusty: horny',
                        'mighty: strong',
                        'muscular: muscular',
                        'naked: nude',
                        'oiled: wet,shiny',
                        'powerful: strong',
                        'rippling: super,shape',
                        'ripped: muscular',
                        'rugged: attractive',
                        'strapping: muscular,strong',
                        'strong: strong',
                        'sturdy: size,large',
                        'sun-browned: color',
                        'tanned: color',
                        'toned: muscular',
                        'wide: size,wide',
                        'uncovered: nude',
                        'virile: attractive',
                        'well-built: muscular',
                        'well-defined: muscular,shape',
                        'well-oiled: wet,shiny'])

          self.Nipples = NipplesMale()
          self.DefaultNoun("chest")
          self.DefaultAdj("broad")
          
class ArmsMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['arms x4: std,default,plur',
                         'limbs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong',
                        'bronzed: color',
                        'burly: shape,strong',
                        'long: size,length,long',
                        'mighty: strong',
                        'muscular: shape',
                        'naked: bare',
                        'powerful: super',
                        'protective: friendly',
                        'rippling: shape',
                        'ripped: strong,shape',
                        'short: size,short',
                        'sinewy: shape',
                        'strapping: strong',
                        'strong: strong',
                        'sturdy: size,large,wide',
                        'thick: size,wide',
                        'toned: shape',
                        'trunk-like: size,wide',
                        'well-built: shape',
                        'wiry: shape'])
          
          self.DefaultNoun("arms")
          self.DefaultAdj("muscular")
          
class EyesMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['eyes'])
               
          self.AdjList(['alluring: attractive',
                        'beautiful: super',
                        'blue: color,whitepers',
                        'bright: shiny',
                        'brown: color',
                        'brooding: emotion',
                        'captivating: attractive',
                        'clear: ',
                        'dark: color',
                        'dazzling: shiny',
                        'deep: ',
                        'earnest: emotion',
                        'electric: attractive',
                        'electrifying: attractive',
                        'gray: color, whitepers',
                        'green: color, whitepers',
                        'hazel: color, whitepers',
                        'icy-blue: color, whitepers',
                        'kind: emotion',
                        'large: size,large',
                        'mischievous: emotion',
                        'narrow: size,narrow',
                        'penetrating: emotion',
                        'small: size,small',
                        'soulful: emotion',
                        'sparkling: shiny',
                        'steely: emotion',
                        'steely-blue: color, whitepers',
                        'stern: emotion',
                        'sweet: young,attractive',
                        'youthful: young',
                        'wide: size,wide,large',
                       ])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("penetrating")

class FacialHair(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['beard x3: beard,std,default,sing',
                         'fuzz: stubble,std,sing',
                         'goatee: goatee,std,sing',
                         'moustache: moustache,std,sing',
                         'stubble: stubble,std,sing',
                        ])
               
          self.AdjList(['black x2: color',
                        'blonde x2: color,whitepers',
                        'bristling: style',
                        'brown: color',
                        'bushy: shape',
                        'coifed: style',
                        'curly: shape',
                        'dark: color',
                        'full: size,large',
                        'glossy: shiny',
                        'gray: color, older',
                        'long: size,large',
                        'luxuriant: super',
                        'magnificent: super',
                        'manly: attractive',
                        'messy: style',
                        'red: color, whitepers',
                        'sandy: color,whitepers',
                        'silken: feel',
                        'short: size,small,style',
                        'thick: size,large',
                        'trimmed: style',
                        'unkempt: style',
                        'untamed: style',
                        'well-trimmed: style',
                        'wild: style',
                        'wiry: style'])
          
          self.DefaultNoun("beard")
          self.DefaultAdj("glossy")
          
class HairMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['afro: std,poc,sing',
                         'bouffant: std,sing',
                         'coif: std,sing',
                         'dreads: std,plur',
                         'fro: std,poc,sing',
                         'hair x4: std,default,sing',
                         'locks x3: std,plur'
                        ])
               
          self.AdjList(['black x2: color',
                        'blonde x2: color,whitepers',
                        'brunette: color',
                        'coifed: style',
                        'curly: shape',
                        'dark: color',
                        'dyed-green: color,fake',
                        'flaming-red: color,whitepers',
                        'glossy: shiny',
                        'golden: color,young,whitepers',
                        'graying: color,older',
                        'long: size,length,long',
                        'luxuriant: super',
                        'messy: style',
                        'platinum blonde: color',
                        'punk blue: color,fake',
                        'red: color,whitepers',
                        'sandy: color,whitepers',
                        'silken: feel',
                        'shaggy: style',
                        'short: size,length,short,small',
                        'spiky: style',
                        'untamed: style',
                        'vibrant: super',
                        'wavy: shape',
                        'wild: style'])
          
          self.DefaultNoun("hair")
          self.DefaultAdj("glossy")
          
class LegsMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['legs x3: std,default,plur',
                         'calves: std,plur',
                         'limbs: std,plur',
                         'thighs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong,large,shape',
                        'bronzed: color',
                        'burly: strong,large,shape',
                        'long: length,long',
                        'mighty: strong',
                        'muscular: strong,shape',
                        'naked: bare',
                        'powerful: super',
                        'rangy: length,long,width,narrow',
                        'rippling: shape',
                        'sinewy: shape',
                        'short: length,short',
                        'slender: width,narrow',
                        'slim: width,narrow',
                        'strapping: strong',
                        'strong: strong',
                        'sturdy: width,wide',
                        'thick: width,wide',
                        'toned: shape',
                        'trunk-like: shape,width,wide',
                        'well-built: shape',
                        'wiry: width,narrow'
                       ])
          
          self.DefaultNoun("legs")
          self.DefaultAdj("sinewy")
          
class JawMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['jaw'])
               
          self.AdjList(['angular: shape',
                        'bearded: beard,hairy',
                        'chiseled: shape',
                        'commanding: attitude',
                        'decisive: attitude',
                        'dominant: attitude',
                        'forceful: attitude',
                        'handsome: attractive',
                        'powerful: attitude',
                        'rugged: shape',
                        'scruffy: stubble,hairy',
                        'sharp: shape',
                        'smooth-shaven: hairless',
                        'square: shape',
                        'striking: attractive',
                        'stubbled: stubble,hairy',
                        'unshaven: stubble,hairy',
                       ])
          
          self.DefaultNoun("jaw")
          self.DefaultAdj("chiseled")
          
class BodyMale(BodyParts):     
    def __init__(self):
        super().__init__()
          
        self.NounList(['body x4: std,default,sing',
                       'build: std,sing',
                       'bulk: std,large,heavy,sing',
                       'form: std,sing',
                       'physique x2: std,sing',
                      ])
               
        self.AdjList(['beefy: large',
                      'brawny: strong,shape',
                      'broad: size,wide',
                      'bronzed: color',
                      'burly: strong,shape,size,wide',
                      'commanding: attitude',
                      'compact: size,small',
                      'dad-bod: plussize',
                      'dark-thatched: hairy',
                      'godlike: super',
                      'handsome: attractive',
                      'hardened: strong',
                      'hearty: size,large',
                      'hung: bigdick',
                      'husky: size,large,plussize',
                      'lanky: width,narrow',
                      'lean: width,narrow',
                      'limber: flexible',
                      'manly: manly',
                      'masculine: manly',
                      'massive: size,large',
                      'muscular: shape',
                      'powerful: strong',
                      'rugged: shape',
                      'sexy: attractive',
                      'short: length,short',
                      'sinewy: shape',
                      'smooth: hairless',
                      'strapping: strong',
                      'striking: attractive',
                      'strong: strong',
                      'sturdy: size,large',
                      'supple: flexible,young',
                      'tall: height,tall',
                      'taut: shape',
                      'thin: width,narrow',
                      'tight: shape,strong',
                      'toned: shape,strong',
                      'towering: size,large,height,tall',
                      'trim: width,narrow',
                      'virile x2: manly',
                      'well-built: shape',
                      'well-hung: bigdick',
                      'wiry: width,narrow',
                      'youthful: young',
                     ])
          
        self.DefaultNoun("body")
        self.IsPlural = False
        self.FacialHair = FacialHair()
        self.Hair = HairMale()
        self.Eyes = EyesMale()
        self.Jaw = JawMale()
        self.Legs = LegsMale()
        self.Skin = SkinMale()
        self.Shoulders = ShouldersMale()
        self.Muscles = MusclesMale()
        self.Chest = ChestMale()
        self.Arms = ArmsMale()
        self.Ass = AssMale()
        self.Penis = Penis()
          
    # woman random body parts used by gen 8 (one instance), 18,21,31,38,60,72
    # man random body parts used by gen 19, 20, 22,38
     
    def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
        sPartDesc = ""
          
        if sPossessive is None:
            sPossessive = ""
          
        PartNotList = ['naked','nude','bare','exposed']
        bAddArticles = True
          
        if isinstance(part, SkinMale):
            PartNotList += ['warm','tender']
            bAddArticles = False 
        elif isinstance(part, HairMale): 
            bAddArticles = False
        elif isinstance(part, FacialHair): 
            bAddArticles = True 
        elif isinstance(part, EyesMale):
            bAddArticles = False 
        elif isinstance(part, ShouldersMale):
            bAddArticles = False 
        elif isinstance(part, ChestMale):
            bAddArticles = True 
        elif isinstance(part, LegsMale):
            bAddArticles = False 
        elif isinstance(part, AssMale):
            bAddArticles = True 
        elif isinstance(part, PenisHead):
            bAddArticles = True 
        elif isinstance(part, Testicles):
            bAddArticles = True 
        elif isinstance(part, Head):
            bAddArticles = True 
        elif isinstance(part, JawMale):
            bAddArticles = True 
        elif isinstance(part, MusclesMale):
            bAddArticles = False 
        elif isinstance(part, ArmsMale):
            PartNotList += ['boobies']
            bAddArticles = False 
               
        if not sPossessive == "":
            bAddArticles = False 
            sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
        sBodyDesc = ""
          
        if sPossessive is None:
            sPossessive = ""
          
        if iNum < 3:
            iNum = 3
        if iNum > 5:
            iNum = 5
               
        hair = self.Hair
        beard = self.FacialHair
        jaw = self.Jaw 
        eyes = self.Eyes 
        chest = self.Chest
        legs = self.Legs 
        skin = self.Skin
        shoulders = self.Shoulders
        arms = self.Arms
          
        PartPriorities = [[hair,1],
                            [eyes,1],
                            [beard,2]
                            [jaw,2]
                            [chest,3],
                            [shoulders,4],
                            [legs,4],
                            [body,5],
                            [skin,6]]
                                
          
        PartGroups = []
          
        if iNum == 3:
            for part1 in PartPriorities: 
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                        if part2[1] == part1[1] and not part2[0] == part1[0]:
                            for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                    PartGroups.append([part1[0],part2[0],part3[0]])
                         
        elif iNum == 4:
            for part1 in PartPriorities:
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                        if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                            for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                    for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                            if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
     
        else:
            for part1 in PartPriorities:
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                        if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                            for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                                if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                    for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                            if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                                for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
                                                    if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
                                                        PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
          
        SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
          
        iLoops = 0
        while iLoops < iNum:
            sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1
               
        return sBodyDesc
          
    def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
        sPartDesc = ""
          
        if sPossessive is None:
            sPossessive = ""
          
        PartNotList = []
        bAddArticles = True
          
        if isinstance(part, SkinMale):
            PartNotList += ['warm','tender']
            bAddArticles = False 
        elif isinstance(part, HairMale): 
            bAddArticles = False
        elif isinstance(part, FacialHair): 
            bAddArticles = True 
        elif isinstance(part, EyesMale):
            bAddArticles = False 
        elif isinstance(part, ShouldersMale):
            bAddArticles = False 
        elif isinstance(part, ChestMale):
            bAddArticles = True 
        elif isinstance(part, LegsMale):
            bAddArticles = False 
        elif isinstance(part, AssMale):
            bAddArticles = True 
        elif isinstance(part, PenisHead):
            bAddArticles = True 
        elif isinstance(part, Testicles):
            bAddArticles = True 
        elif isinstance(part, PenisHead):
            bAddArticles = True 
        elif isinstance(part, JawMale):
            bAddArticles = True 
        elif isinstance(part, ArmsMale):
            bAddArticles = False 
        elif isinstance(part, MusclesMale):
            bAddArticles = False 
               
        if not sPossessive == "":
            sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bPenis = True, bAss = True, bExplicit = False, bAllowLongDesc = True, sPossessive = None):
        sBodyDesc = ""
          
        if sPossessive is None:
            sPossessive = ""
            sPossessive = ""
          
        if iNum < 3:
            iNum = 3
        if iNum > 5:
            iNum = 5
               
        hair = self.Hair
        beard = self.FacialHair
        jaw = self.Jaw 
        eyes = self.Eyes 
        chest = self.Chest
        muscles = self.Muscles
        legs = self.Legs 
        skin = self.Skin
        shoulders = self.Shoulders
        arms = self.Arms
        penis = self.Penis
        balls = self.Penis.Testicles
        head = self.Penis.Head 
        ass = self.Ass 
        asshole = self.Ass.Anus 
        body = self
          
        PartPriorities = [[chest,1],
                            [shoulders,2],
                            [muscles,3],
                            [legs,4],
                            [skin,5],
                            [body,6]]
          
        if bAss:
            PartPriorities.append([ass,4])
        if bPenis:
            PartPriorities.append([penis,8])
          
        if bExplicit:
            PartPriorities.append([balls,9])
            PartPriorities.append([head,10])
            #PartPriorities.append([asshole,11])
          
        PartGroups = []
          
        if iNum == 3:
            for part1 in PartPriorities: #skin 6
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                    if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                        for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                            if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                PartGroups.append([part1[0],part2[0],part3[0]])
                         
        elif iNum == 4:
            for part1 in PartPriorities:
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                    if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                        for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                            if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                    if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                        PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
     
        else:
            for part1 in PartPriorities:
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                    if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
                        for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
                            if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
                                for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
                                    if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
                                        for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
                                            if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
                                                PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
        
        SelectedParts = None
        
        if len(PartGroups) > 1:
            SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
        elif len(PartGroups) == 1:
            SelectedParts = PartGroups[0]

        iLoops = 0
        while iLoops < iNum:
            sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1

        return sBodyDesc
          
 
    def GetRandomIntimateParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
        Parts = []
        AllParts = []
          
        if bIncludeInners:
            AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
        else:
            AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               
        for x in sorted(sample(range(0, len(AllParts)), iNum)):
            Parts.append(AllParts[x])
               
        return Parts