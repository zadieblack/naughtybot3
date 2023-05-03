#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from random import *
from util import *
import re 

BodyPartHistoryQ = HistoryQ(10)

TagExclDict = {"black": ["white"],
               "white": ["black"],
               "large": ["small"],
               "small": ["large"],
               "older": ["young"],
               "young": ["older"]}

class PartDescSet:
    def __init__(self, ParentPart, iNumAdjs = 3, ExtraAdjList = None, NotList = [], bStdNouns = True, bDescNouns = True, bSillyNouns = True):
        self._ParentPart = ParentPart
        self._NotList = NotList
        self._bStdNouns = bStdNouns
        self._bDescNouns = bDescNouns
        self._bSillyNouns = bSillyNouns
        self._Noun = ""
        self._Color = ""
        self._AdjList = []

        if ExtraAdjList is None:
            ExtraAdjList = []

        self.SetSelf(iNumAdjs = iNumAdjs, ExtraAdjList = ExtraAdjList)

    def SetSelf(self, iNumAdjs = 3, ExtraAdjList = None):
        ParentPart = self._ParentPart

        if ExtraAdjList is None:
            ExtraAdjList = []

        if isinstance(ParentPart, BodyParts):
            self._Noun = ParentPart.GetNoun(NotList = self._NotList + self._AdjList, bStdNouns = self._bStdNouns, bDescNouns = self._bDescNouns, bSillyNouns = self._bSillyNouns)

            for i in range(iNumAdjs):
                sAdj = ParentPart.GetAdj(NotList = self._NotList + self._AdjList)
                self.AddAdj(sAdj)

            for adj in ExtraAdjList:
                self.AddAdj(adj)

            if len(ParentPart._ColorList.GetWordList()) > 0:
                self._Color = ParentPart.GetColor(NotList = self._NotList + self._AdjList + [self._Noun])

    def SetNotList(self, NotList):
        self._NotList = NotList
        self.SetSelf()

    def SetStdNouns(self, bStdNouns):
        self._bStdNouns = bStdNouns
        self.SetSelf()

    def SetDescNouns(self, bDescNouns):
        self._bDescNouns = bDescNouns
        self.SetSelf()

    def SetSillyNouns(self, bSillyNouns):
        self._bSillyNouns = bSillyNouns
        self.SetSelf()

    def AddAdj(self, adj):
        if adj != "":
            self._AdjList.append(adj)

    def RemoveAdj(self, adj):
        if adj in self._AdjList:
            self._AdjList.remove(adj)

    def RemoveAdjByNum(self, inum):
        if inum >= 0 and inum < len(self._AdjList):
            self._AdjList.pop(inum)

    def SetAdj(self, inum, adj):
        if inum >= 0 and inum < len(self._AdjList):
            self._AdjList[inum] = adj

    def SetNoun(self, noun):
        self._Noun = noun

    def SetColor(self, color):
        self._Color = color

    def Adj(self, inum):
        sAdj = ""
        if inum >= 0 and inum < len(self._AdjList):
            sAdj = self._AdjList[inum]
        
        return sAdj

    def Noun(self):
        return self._Noun

    def Color(self):
        return self._Color

    def bStdNouns(self):
        return self._bStdNouns

    def bDescNouns(self):
        return self._bStdNouns

    def bSillyNouns(self):
        return self._bStdNouns

    def GetFullDesc(self, bColor = True):
        sFullDesc = ""
        DescWordList = []

        if self.Noun() != "":
            DescWordList.insert(0, self.Noun())
        if self.Color() != "" and bColor:
            DescWordList.insert(0, self.Color())
        DescWordList = self._AdjList + DescWordList

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

        if self.Noun() != "":
            DescWordList.insert(0, self.Noun())
        if self.Color() != "":
            DescWordList.insert(0, self.Color())
        DescWordList = self._AdjList + DescWordList

        return DescWordList
        
class BodyParts:
     def __init__(self):
          self._StdNounList = WordList([])
          self._DescNounList = WordList([])
          self._SillyNounList = WordList([])
          self._AdjList = WordList([])
          self._ColorList = WordList([])
          self._DefaultNoun = ""
          self._DefaultAdj = "naked"
          
          self.NounHistoryQ = HistoryQ(3)
          self.AdjHistoryQ = HistoryQ(3)

          self.PartDescSet = PartDescSet(self)
        
     def StdNounList(self, NewNounList = None):
          if NewNounList == None:
               SetStdNounList = []
          else:
               SetStdNounList = NewNounList 
               
          self._StdNounList = WordList(SetStdNounList)

          self.PartDescSet.SetSelf()

     def DescNounList(self, NewNounList = None):
          if NewNounList == None:
               SetDescNounList = []
          else:
               SetDescNounList = NewNounList 
               
          self._DescNounList = WordList(SetDescNounList)

          self.PartDescSet.SetSelf()

     def SillyNounList(self, NewNounList = None):
          if NewNounList == None:
               SetSillyNounList = []
          else:
               SetSillyNounList = NewNounList 
               
          self._SillyNounList = WordList(SetSillyNounList)

          self.PartDescSet.SetSelf()

     def NounList(self, NewNounList = None):
          self.StdNounList(NewNounList)

          self.PartDescSet.SetSelf()
          
     def AdjList(self, NewAdjList = None):
          if NewAdjList == None:
               SetAdjList = []
          else:
               SetAdjList = NewAdjList
               
          self._AdjList = WordList(SetAdjList)

          self.PartDescSet.SetSelf()
          
     def ColorList(self, NewColorList = None):
          if NewColorList == None:
               SetColorList = []
          else:
               SetColorList = NewColorList
               
          self._ColorList = WordList(SetColorList)

          self.PartDescSet.SetSelf()
          
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
     
     def GetNoun(self, sNot = "", NotList = None, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
        sNoun = "" 
        LocalNounList = []
         
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)
          
        if bStdNouns:
            LocalNounList += self._StdNounList.GetWordList()
        if bSillyNouns:
            LocalNounList += self._SillyNounList.GetWordList()
        if bDescNouns:
            LocalNounList += self._DescNounList.GetWordList()
        if len(LocalNounList) == 0:
            LocalNounList += self._StdNounList.GetWordList()
  
        return WordList(LocalNounList).GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
     
     def GetAdj(self, sNot = "", NotList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)
                    
          return self._AdjList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
          
     def GetColor(self, sNot = "", NotList = None):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)
                    
          return self._ColorList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
          
     def GetNounList(self):
          return self.GetStdNounList()

     def GetStdNounList(self):
          return self._StdNounList.List 

     def GetDescNounList(self):
          return self._DescNounList.List 

     def GetSillyNounList(self):
          return self._SillyNounList.List 
          
     def GetAdjList(self):
          return self._AdjList.List
          
     def GetColorList(self):
          return self._ColorList.List
          
     def HasColors(self):
          bHasColors = False 
          
          if len(self._ColorList.List) > 0:
               bHasColors = True
               
          return bHasColors

     #noun only ("hair")
     def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          DescSet = None 
         
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
              ExtraAdjList = []

          DescSet = PartDescSet(self, ExtraAdjList = ExtraAdjList, iNumAdjs = 0, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)

          return DescSet.GetFullDesc(bColor = False)
     
     #adjective noun ("red hair")
     def MediumDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          DescSet = None
          
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)
          
          DescSet = PartDescSet(self, ExtraAdjList = ExtraAdjList, iNumAdjs = 1, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
          
          return DescSet.GetFullDesc(bColor = CoinFlip())
     
     #adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
     def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          DescSet = None
          
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
              ExtraAdjList = []
          
          iNumAdjs = choice([1,1,1,2,2,2,2,3])

          DescSet = PartDescSet(self, ExtraAdjList = ExtraAdjList, iNumAdjs = iNumAdjs, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)

          return DescSet.GetFullDesc(bColor = CoinFlip())
     
     def RandomDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
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
                         sRandomDesc = self.ShortDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
                    else:
                         sRandomDesc = self.GetDefaultNoun(NotList = NotList)
               else:
                    sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
          elif iRand in range(3,6):
          #medium desc 
               sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
          else:
          #flowery desc if allowed
               if bAllowLongDesc:
                    sRandomDesc = self.FloweryDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
               else:
                    sRandomDesc = self.MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
               
          return sRandomDesc

# This class attempts to create 'smart sets' of descriptive words. It will pick a number 
# of adjectives (usually 3) and a noun for a given body part. It will try to avoid
# picking the same words twice. In the case of adjs, it will even try to pick a diff
# type of adj each time. 

# This class can also "describe" the words it has picked, putting them in a row with
# proper spaces and commas. This functionality is used by MediumDescription() and
# FloweryDescription().
class PartDescSet_new:
    def __init__(self, ParentPart, iNumAdjs = 3, ExtraAdjList = None, bVaryAdjTags = True, NotList = [], bStdNouns = True, bDescNouns = True, bSillyNouns = True):
        self._ParentPart = ParentPart
        self._NotList = NotList
        self._Noun = ""
        self._Color = ""
        self._iNumAdjs = iNumAdjs
        self._AdjList = []
        self._bVaryAdjTags = bVaryAdjTags

        self._ReqTagList = []
        self._ExclTagList = []
        self._NounReqTagList = []
        self._NounExclTagList = []
        self._AdjReqTagList = []
        self._AdjExclTagList = []
        self._Adj1ReqTagList = []
        self._Adj1ExclTagList = []
        self._Adj2ReqTagList = []
        self._Adj2ExclTagList = []
        self._Adj3ReqTagList = []
        self._Adj3ExclTagList = []

        if ExtraAdjList is None:
            self._ExtraAdjList = []
        else:
            self._ExtraAdjList = ExtraAdjList

        #self.SetStdNouns(bStdNouns)
        #self.SetDescNouns(bDescNouns)
        #self.SetSillyNouns(bDescNouns)

        self.SetSelf()

    def SetSelf(self):
        ParentPart = self._ParentPart

        if isinstance(ParentPart, BodyParts_New):
            # Don't bother if bodypart adj lists or noun lists are empty
            if ParentPart.NounListLen() > 0 and ParentPart.AdjListLen() > 0:
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

                Adj1ReqTagList = [] 
                if len(self._Adj1ReqTagList) > 0:
                    Adj1ReqTagList = self._Adj1ReqTagList
                elif len(self._AdjReqTagList) > 0:
                    Adj1ReqTagList = self._AdjReqTagList
                else:
                    Adj1ReqTagList = self._ReqTagList

                Adj1ExclTagList = []
                if len(self._Adj1ExclTagList) > 0:
                    Adj1ExclTagList = self._Adj1ExclTagList
                elif len(self._AdjExclTagList) > 0:
                    Adj1ExclTagList = self._AdjExclTagList
                else:
                    Adj1ExclTagList = self._ExclTagList

                Adj2ReqTagList = []
                if len(self._Adj2ReqTagList) > 0:
                    Adj2ReqTagList = self._Adj2ReqTagList
                elif len(self._AdjReqTagList) > 0:
                    Adj2ReqTagList = self._AdjReqTagList
                else:
                    Adj2ReqTagList = self._ReqTagList

                Adj2ExclTagList = []
                if len(self._Adj2ExclTagList) > 0:
                    Adj2ExclTagList = self._Adj2ExclTagList
                elif len(self._AdjExclTagList) > 0:
                    Adj2ExclTagList = self._AdjExclTagList
                else:
                    Adj2ExclTagList = self._ExclTagList

                Adj3ReqTagList = []
                if len(self._Adj3ReqTagList) > 0:
                    Adj3ReqTagList = self._Adj3ReqTagList
                elif len(self._AdjReqTagList) > 0:
                    Adj3ReqTagList = self._AdjReqTagList
                else:
                    Adj3ReqTagList = self._ReqTagList

                Adj3ExclTagList = []
                if len(self._Adj3ExclTagList) > 0:
                    Adj3ExclTagList = self._Adj3ExclTagList
                elif len(self._AdjExclTagList) > 0:
                    Adj3ExclTagList = self._AdjExclTagList
                else:
                    Adj3ExclTagList = self._ExclTagList

                self._Noun = ParentPart.GetNoun(NotList = self._NotList + self._AdjList, ReqTagList = NounReqTagList, ExclTagList = NounExclTagList)
                print("  ---")
                global TagExclDict
                UsedTagList = []
                if self._bVaryAdjTags and len(AdjReqTagList) == 0:
                    for tag in ParentPart.GetUnitTags(self._Noun):
                        if tag in TagExclDict:
                            UsedTagList.append(tag)
                    print("  Added any excluding noun tags for \"" + self._Noun + "\" to UsedTagList " + str(UsedTagList))

                self.ClearAdjList()
                for i in range(self._iNumAdjs):
                    LocalReqTagList = []
                    LocalExclTagList = []
                    if i == 0:
                        LocalReqTagList = Adj1ReqTagList.copy()
                        LocalExclTagList = Adj1ExclTagList.copy()
                    elif i == 1:
                        LocalReqTagList = Adj2ReqTagList.copy()
                        LocalExclTagList = Adj2ExclTagList.copy()
                    elif i == 2:
                        LocalReqTagList = Adj3ReqTagList.copy()
                        LocalExclTagList = Adj3ExclTagList.copy()
                    else:
                        LocalReqTagList = AdjReqTagList.copy()
                        LocalExclTagList = AdjExclTagList.copy()

                    sAdj = ParentPart.GetAdj(NotList = self._NotList + self._AdjList, ReqTagList = LocalReqTagList, ExclTagList = LocalExclTagList + UsedTagList)
                    for tag in ParentPart.GetUnitTags(sAdj):
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
                
                    print("  Picked adj \"" + sAdj + "\" " + str(ParentPart.GetUnitTags(sAdj)) + "\n    excl tags " + str(LocalExclTagList) + "\n    used tags " + str(UsedTagList))
                    self.AddAdj(sAdj)
                    #print("  Adj list " + str(self._AdjList))

                for adj in self._ExtraAdjList:
                    self.AddAdj(adj)

                #if len(ParentPart._ColorList.GetWordList()) > 0:
                #    self._Color = ParentPart.GetColor(NotList = self._NotList + self._AdjList + [self._Noun])

    def SetNotList(self, NotList):
        self._NotList = NotList
        self.SetSelf()

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
        self.SetSelf()

    def ExclTagList(self, TagList):
        self._ExclTagList = TagList
        self.SetSelf()

    def NounReqTagList(self, TagList):
        self._NounReqTagList = TagList
        self.SetSelf()

    def NounExclTagList(self, TagList):
        self._NounExclTagList = TagList
        self.SetSelf()

    def AdjReqTagList(self, TagList):
        self._AdjReqTagList = TagList
        self.SetSelf()

    def AdjExclTagList(self, TagList):
        self._AdjExclTagList = TagList
        self.SetSelf()

    def Adj1ReqTagList(self, TagList):
        self._Adj1ReqTagList = TagList
        self.SetSelf()

    def Adj1ExclTagList(self, TagList):
        self._Adj1ExclTagList = TagList
        self.SetSelf()

    def Adj2ReqTagList(self, TagList):
        self._Adj2ReqTagList = TagList
        self.SetSelf()

    def Adj2ExclTagList(self, TagList):
        self._Adj2ExclTagList = TagList
        self.SetSelf()

    def Adj3ReqTagList(self, TagList):
        self._Adj3ReqTagList = TagList
        self.SetSelf()

    def Adj3ExclTagList(self, TagList):
        self._Adj3ExclTagList = TagList
        self.SetSelf()

    def GetAdj(self, inum):
        sAdj = ""
        if inum >= 0 and inum < len(self._AdjList):
            sAdj = self._AdjList[inum]
        
        return sAdj

    def GetNoun(self):
        return self._Noun

    def GetColor(self):
        return self._Color

    def GetFullDesc(self, bColor = True):
        sFullDesc = ""
        DescWordList = []

        if self.GetNoun() != "":
            DescWordList.insert(0, self.GetNoun())
        #if self.Color() != "" and bColor:
        #    DescWordList.insert(0, self.Color())
        DescWordList = self._AdjList + DescWordList

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

        if self.Noun() != "":
            DescWordList.insert(0, self.Noun())
        #if self.Color() != "":
        #    DescWordList.insert(0, self.Color())
        DescWordList = self._AdjList + DescWordList

        return DescWordList

    def SetStdNouns(self, bStdNouns):
        if bStdNouns:
            self.ReqNounTagList(["std"])
        else:
            self.ExclNounTagList(["std"])
        self.SetSelf()

    def SetDescNouns(self, bDescNouns):
        if bDescNouns:
            self.ReqNounTagList(["desc"])
        else:
            self.ExclNounTagList(["desc"])
        self.SetSelf()

    def SetSillyNouns(self, bSillyNouns):
        if bSillyNouns:
            self.ReqNounTagList(["silly"])
        else:
            self.ExclNounTagList(["silly"])
        self.SetSelf()

class BodyParts_New:
    def __init__(self):
        self._AllUnitLists = {"adj": {"master": []}, "noun": {"master": [], "std": []}}
        self._UnitTags = dict()
        self._DefaultNoun = ""
        self._DefaultAdj = "naked"
          
        self.NounHistoryQ = HistoryQ(3)
        self.AdjHistoryQ = HistoryQ(3)

        # No point in initializing the PartDescSet if this bodypart doesn't have its word lists
        self.PartDescSet = None

    # This must be run every time this object's unit lists are updated
    def InitPartDescSet(self):
        if self.PartDescSet is None:          
            self.PartDescSet = PartDescSet(self)
        else:
            self.PartDescSet.SetSelf()

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

    def GetNounList(self, sListName):
        return self.GetUnitList(sListName, "noun") 

    def GetAdjList(self, sListName):
        return self.GetUnitList(sListName, "adj") 

    def AddUnitToList(self, sUnit, sListName, sType, iPriority = None):
        UnitList = self.GetUnitList(sListName, sType)
        ListDict = self._AllUnitLists[sType.lower()]

        if UnitList is None:
            #create
            ListDict[sListName] = []

        if iPriority is None:
            iPriority = 1

        if not self.IsUnitInList(sUnit, sListName, sType):
            for i in range(iPriority):
                if not sListName.lower() in ListDict:
                    ListDict[sListName.lower()] = []
                ListDict[sListName.lower()].append(sUnit)

            self.AddUnitTag(sUnit, sListName)

        self.InitPartDescSet()

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

    def UnitList(self, NewUnitList, sType):
        #print("Entered UnitList()")
        for item in NewUnitList:
            sUnit = ""
            iPriority = 1
            TagList = []

            #print(" item = \"" + item + "\"")

            # clean string
            item = item.strip()

            # locate priority
            #print(" Looking for priority")
            matchPriority = re.search(r"(?<=[x])([\d]+)", item)
            if matchPriority:
                iPriority = int(matchPriority.group())
                #print("  Priority found! iPriority = " + str(iPriority))
            #else:
                #print("  No priority found! iPriority = " + str(iPriority))

            ItemSections = item.split(":")

            # locate Unit 
            #print(" Looking for Unit")
            #print("  Looking for colon[:]")
            if len(ItemSections) > 1:
                #print("   Colon[:] found. ItemSections[0] = \"" + ItemSections[0] + "\"")
                matchUnit = re.search(r"([x][\d]+)", ItemSections[0])
                #print("   Looking for priority end point")
                if matchUnit:
                    sUnit = ItemSections[0][0:matchUnit.span()[0]]
                    #print("    Priority end point found. sUnit = \"" + sUnit + "\"")
                else:
                    sUnit =  ItemSections[0]
                    #print("    No priority endpoint found. Using ItemSections[0] as Unit. sUnit = \"" + sUnit + "\"")
                sUnit = sUnit.strip()
            else:
                sUnit = ItemSections[0].strip()
                #print("   No colon[:] found. sUnit = \"" + sUnit + "\"")

            # locate tag list 
            #print(" Looking for tag list")
            matchTags = re.search(r"(?<=[:])([\w\s,]*)", item)
            if matchTags:
                TagList = "".join(matchTags.group().split(" ")).split(",")
                #print("  Tag list found. TagList = " + str(TagList) + "")
            #else:
                #print("  Tag list not found.")

            self.AddUnitToList(sUnit, "master", sType, iPriority)
            #print(" Added \"" + sUnit + "\" to master list.")
            for tag in TagList:
                if tag.strip() != "":
                    self.AddUnitToList(sUnit, tag, sType, iPriority)
                #print(" Added \"" + sUnit + "\" to " + tag + " list.")
               
        self.InitPartDescSet()

    def NounList(self, NewNounList):
        self.UnitList(NewNounList, "noun")

    def AdjList(self, NewAdjList):
        self.UnitList(NewAdjList, "adj")

    def UnitListLen(self, sType):
        ListLen = 0 
        ListDict = self._AllUnitLists[sType.lower()]

        ListLen = len(ListDict["master"])

        return ListLen

    def NounListLen(self):
        return self.UnitListLen("noun")

    def AdjListLen(self):
        return self.UnitListLen("adj")

    #def ColorList(self, NewColorList = None):
    #    if NewColorList == None:
    #        SetColorList = []
    #    else:
    #        SetColorList = NewColorList
               
    #    self._ColorList = WordList(SetColorList)

    #    self.PartDescSet.SetSelf()
          
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
        #print("  Entered GetUnit()")
         
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if ExclTagList is None:
            ExclTagList = []

        ExclUnitList = []
        for unitlist in ExclTagList:
            #print("    Getting word units for " + unitlist)
            for unit in self.GetUnitList(unitlist, sType):
                ExclUnitList.append(unit)

        if ReqTagList == None or len(ReqTagList) == 0:
            #print("  ReqTagList is empty. Using master list.")
            for Unit in self.GetUnitList("master", sType):
                if not Unit in ExclUnitList:
                    LocalUnitList.append(Unit)
        else:
            for taglistname in ReqTagList:
                #print("  Adding taglist " + taglistname)
                for Unit in self.GetUnitList(taglistname, sType):
                    if not Unit in ExclUnitList:
                        LocalUnitList.append(Unit)

        #print("  LocalUnitList = " + str(LocalUnitList) + "\n")

        return WordList(LocalUnitList).GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)

    def GetNoun(self, sNot = "", NotList = None, ReqTagList = None, ExclTagList = None):
        return self.GetUnit("noun", sNot = sNot, NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)

    def GetAdj(self, sNot = "", NotList = None, ReqTagList = None, ExclTagList = None):
        return self.GetUnit("adj", sNot = sNot, NotList = NotList, ReqTagList = ReqTagList, ExclTagList = ExclTagList)

    #def GetColor(self, sNot = "", NotList = None):
    #    if NotList == None:
    #        NotList = []
          
    #    if sNot != "":
    #        NotList.append(sNot)
                    
    #    return self._ColorList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
          
    #def GetColorList(self):
    #    return self._ColorList.List
          
    def HasColors(self):
        return False

    #noun only ("hair")
    def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        DescSet = None 
         
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if NounReqTagList == None:
            NounReqTagList = []

        if NounExclTagList == None:
            NounExclTagList = []

        if AdjReqTagList == None:
            AdjReqTagList = []

        if AdjExclTagList == None:
            AdjExclTagList = []

        if ExtraAdjList is None:
            ExtraAdjList = []

        DescSet = PartDescSet_new(self, ExtraAdjList = ExtraAdjList, iNumAdjs = 0, NotList = NotList)
        DescSet.NounReqTagList(NounReqTagList)
        DescSet.NounExclTagList(NounExclTagList)
        DescSet.AdjReqTagList(AdjReqTagList)
        DescSet.AdjExclTagList(AdjExclTagList)

        return DescSet.GetFullDesc(bColor = False)
     
    #adjective noun ("red hair")
    def MediumDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        DescSet = None
          
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if NounReqTagList == None:
            NounReqTagList = []

        if NounExclTagList == None:
            NounExclTagList = []

        if AdjReqTagList == None:
            AdjReqTagList = []

        if AdjExclTagList == None:
            AdjExclTagList = []
          
        DescSet = PartDescSet_new(self, ExtraAdjList = ExtraAdjList, iNumAdjs = 1, NotList = NotList)
        DescSet.NounReqTagList(NounReqTagList)
        DescSet.NounExclTagList(NounExclTagList)
        DescSet.AdjReqTagList(AdjReqTagList)
        DescSet.AdjExclTagList(AdjExclTagList)
          
        return DescSet.GetFullDesc(bColor = CoinFlip())
     
    #adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
    def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        DescSet = None
          
        if NotList == None:
            NotList = []
          
        if sNot != "":
            NotList.append(sNot)

        if NounReqTagList == None:
            NounReqTagList = []

        if NounExclTagList == None:
            NounExclTagList = []

        if AdjReqTagList == None:
            AdjReqTagList = []

        if AdjExclTagList == None:
            AdjExclTagList = []

        if ExtraAdjList is None:
            ExtraAdjList = []
          
        iNumAdjs = choice([1,1,1,2,2,2,2,3])

        DescSet = PartDescSet_new(self, ExtraAdjList = ExtraAdjList, iNumAdjs = iNumAdjs, NotList = NotList)
        DescSet.NounReqTagList(NounReqTagList)
        DescSet.NounExclTagList(NounExclTagList)
        DescSet.AdjReqTagList(AdjReqTagList)
        DescSet.AdjExclTagList(AdjExclTagList)

        return DescSet.GetFullDesc(bColor = CoinFlip())
     
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
          
          self.NounList(['face',
               'face',
               'face',
               'features'])
          
          self.AdjList(['adorable',
               'angelic',
               'beaming',
               'beautiful',
               'cute',
               'delicate',
               'elegant',
               'excited',
               'gentle',
               'gorgeous',
               'flushed',
               'freckled',
               'heart-shaped',
               'innocent',
               'lovely',
               'oval',
               'pale',
               'pretty',
               'radiant',
               'rosy',
               'round',
               # 'sculpted',
               'smiling',
               'startled',
               # 'surprised',
               'sweet',
               'warm',
               'wide-eyed'])
               
          self.DefaultNoun('face')
          
class BackFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['back','back','back','back',
               'spine'])
          
          self.AdjList(['arched','arched',
               'arching',
               'bare',
               'carved',
               'concave',
               'curved','curved',
               'delicate',
               'feminine',
               'flexible',
               'gently curved',
               'graceful','graceful',
               'lissome',
               'lithe','lithe',
               'long',
               'naked',
               'sculpted',
               'sexy',
               'sleek',
               'slender','slender',
               'slim','slim',
               'smooth',
               'tapered','tapered','tapered',
               'tapering','tapering',
               'well-defined',
               'willowy','willowy'])
               
          self.DefaultNoun('back')
          
class Skin(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['skin','skin','skin','skin',
               'flesh'])
               
          self.ColorList(['almond-colored',
                              'brown',
                              'bronzed',
                              'chocolate',
                              'chocolate-colored',
                              'coffee-colored',
                              'creamy',
                              'dark',
                              'fresh pink',
                              'honeyed',
                              'pale',
                              'pink',
                              'porcelain',
                              'rosy',
                              'sun-browned',
                              'sun-kissed'])
                              
          self.AdjList([
               'bare',
               'delicate',
               'exposed',
               'freckled',
               'gentle',
               'gleaming',
               'glistening',
               'glowing',
               'gossamer',
               'luscious',
               'naked',
               'perfect',
               'silken',
               'soft',
               'smooth',
               'supple',
               'sweet',
               'tender',
               'un-blemished',
               'un-sullied',
               'warm',
               'yielding',
               'youthful'])
          
          self.DefaultNoun('skin')
          self.IsPlural = False
          
class Mouth(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['mouth',
                               'mouth',
                               'mouth',
                               'mouth',
                               'mouth-hole'])
               
          self.AdjList(['eager',
               'greedy',
               'hungry',
               'insatiable',
               'insolent',
               'lewd',
               'open',
               'wanting',
               'willing'])
          
          self.DefaultNoun("mouth")
          self.DefaultAdj("insatiable")
          self.IsPlural = False
          
class Lips(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['lips'])
               
          self.AdjList(['collagen-injected',
               'full',
               'inviting',
               'insolent',
               'luscious',
               'pouting',
               'sensual',
               'sweet'])
               
          self.ColorList(['candy-colored',
                              'dark',
                              'red','red',
                              'rose-colored',
                              'rouge',
                              'painted black'
                           ])
          
          self.DefaultNoun("lips")
          self.DefaultAdj("full")
          
class Eyes(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['eyes'])
               
          self.AdjList(['alluring',
               'beautiful',
               'bewitching',
               'bright',
               'captivating',
               'clear',
               'dazzling',
               'earnest',
               'electric',
               'electrifying',
               'enchanting',
               'kind',
               'large',
               'mischievous',
               'soulful',
               'sparkling',
               'sweet',
               'wide'])
               
          self.ColorList(['blue','blue',
                           'brown',
                           'gray',
                           'green',
                           'hazel',
                           'pale'])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("bewitching")
          
class Hips(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['hips'])
               
          self.AdjList(['curvy',
               'curvaceous',
               'bare',
               'fertile',
               'rounded',
               'sensual',
               'shapely',
               'slinky',
               'sultry',
               'tantalizing',
               'voluptuous',
               'wanton',
               'wide',
               'womanly'])
          
          self.DefaultNoun("hips")
          
class Hair(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['hair',
               'hair',
               'hair',
               'locks'])
               
          self.AdjList(['curly',
               'braided',
               'glossy',
               'long',
               'luxuriant',
               'pixie cut',
               'silken',
               'short',
               'straight',
               'vibrant',
               'wavy'])
               
          self.ColorList(['black','black',
                              'blonde','blonde',
                              'blue-dyed',
                              'brunette',
                              'dark',
                              'dyed green',
                              'flaming-red',
                              'golden',
                              'kinky black-girl',
                              'platinum blonde',
                              'punk blue',
                              'sandy',
                              'red'])
                              
          
          self.DefaultNoun("hair")
          self.DefaultAdj("flowing")
          
class Legs(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['legs'])
               
          self.AdjList(['athletic',
               'coltish',
               'elegant',
               'graceful',
               'lithe',
               'limber',
               'lissome',
               'lithesome',
               'long','long',
               'long, sexy',
               'toned',
               'sexy',
               'shapely',
               'shaved',
               'smooth',
               'smooth-shaven'])
          
          self.DefaultNoun("legs")
          
class Thighs(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['thighs'])
               
          self.AdjList(['bare',
               'bronzed',
               'chubby',
               'comely',
               'delectable',
               'full',
               'girlish',
               'heavy',
               'inviting',
               'luscious',
               'nubile',
               'pale',
               'powerful',
               'porcelain',
               'ripe',
               'rounded',
               'sensual',
               'sexy',
               'shapely',
               'silken',
               'smooth',
               'soft',
               'tanned',
               'tender',
               'thick','thick',
               'un-sullied',
               'wide',
               'womanly',
               'youthful'])
          
          self.DefaultNoun("thighs")
          
class Nipples(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['nipples',
               'nipples',
               'nipples',
               'nips',
               'teats',
               ])
               
          self.AdjList(['blossoming',
               'budding',
               'dainty',
               'enormous',
               'erect',
               'exposed',
               'inch-long',
               'long',
               'luscious',
               'petite',
               'pert',
               'pokey',
               'puffy',
               'ripe',
               'sensitive',
               'shameless',
               'stiff',
               'succulent',
               'suckable',
               'swollen',
               'tasty',
               'tender',
               'tiny',
               'wide'])
               
          self.ColorList(['chocolate',
                              'dark',
                              'pink',
                              'rosebud',
                              'rose-colored'
                              ])
          
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")

class Breasts_new(BodyParts_New):
     def __init__(self):
          super().__init__()
          
          self.NounList(['boobies: silly,slang,cute,plur',
                         'boobs x2: std,slang,plur',
                         'bosoms x2: std,poetic,plur',
                         'breasticles x2: silly,crude,slang,plur',
                         'breasts x3: std,clinical,default,plur',
                         'buds x2: poetic,cute,plur,desc,small,young',
                         'bust: std,sing',
                         'chest: std,sing',
                         'coconuts: poetic,silly,slang,cute,plur',
                         'dumplings: poetic,silly,cute,plur',
                         'gazongas: silly,crude,slang,plur',
                         'globes x2: poetic,silly,crude,desc,plur',
                         'jugs: silly,crude,slang,plur',
                         'knockers: silly,crude,slang,plur',
                         'orbs x2: poetic,silly,desc,plur',
                         'mammaries: silly,clinical,plur',
                         'melons: large,silly,poetic,crude,desc,plur',
                         'milk-balloons: large,silly,crude,desc,plur',
                         'mounds x2: poetic,desc,plur',
                         'tatas: silly,crude,slang,cute,plur',
                         'teats: std,clinical,desc,plur',
                         'tiddies: silly,crude,slang,cute,plur',
                         'titties: silly,crude,slang,cute,plur',
                         'tits : std,crude,slang,plur',
                        ])
               
          # todo: A cup, B cup, etc should be inserted as 'extra adjs' so they show up
          #       right before the noun
          self.AdjList(['A cup: size,small',
                        'B cup: size,small',
                        'black: color,black',
                        'big: size,large',
                        'bite-sized: size,small',
                        'bouncy: large,movement',
                        'bountiful: large,poetic',
                        'bronzed: color',
                        'brown: color,black',
                        'budding: small,poetic,young',
                        'buxom: large',
                        'chocolate: color,black,taste',
                        'chubby: large,size,shape',
                        'creamy: color,white,poetic,taste,horny',
                        'dark: color,black',
                        'D cup: size,large',
                        'DDD: size,large,size',
                        'delicious: super,poetic,taste,horny',
                        'double-D: size,large,size',
                        'fair: color,white',
                        'fake: fake,large,size,feel,shape',
                        'fat x3: large,size,feel,shape',
                        'fuckable: large,horny',
                        'full: large,poetic',
                        'fulsome: large,poetic',
                        'generous: size,large,poetic',
                        'gentle: poetic,feel',
                        'girlish: small,young',
                        'glorious: super',
                        'gorgeous: super',
                        'heaving: movement,poetic',
                        'heavy: large,feel',
                        'impressive: super,large',
                        'jiggling: movement',
                        'juicy: large,super,feel,taste,horny',
                        'luscious: large,super',
                        'lush: large,super',
                        'luxuriant: large,super',
                        'magnificent: large,super',
                        'nubile: pos,young,poetic',
                        'oiled-up: color,feel',
                        'pale: color,white,young',
                        'pendulous: large,shape,older',
                        'perky: shape,young',
                        'pert: shape,poetic,',
                        'petite: size,small,',
                        'plentiful: large,poetic,super',
                        'plump: large,feel,shape,',
                        'proud: large,super,poetic,',
                        'quivering: movement,poetic,',
                        'ripe: poetic,feel,shape,young',
                        'round: shape,fake',
                        'sensual: poetic',
                        'shapely: shape,poetic',
                        'smooth: feel,young',
                        'soft: feel',
                        'statuesque: shape,large,poetic',
                        'stunning: super',
                        'succulent: super,taste,poetic',
                        'suckable: taste,horny',
                        'sumptuous: large,super,poetic',
                        'supple: feel,poetic,young',
                        'surgically-enhanced: large,shape,fake',
                        'swaying: large,movement',
                        'sweet: super',
                        'swollen: size,large,shape',
                        'tender: feel,poetic',
                        'voluptuous: size,large,poetic'])
          
          self.DefaultNoun("breasts")
          
class Breasts(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.Nipples = []

          self.StdNounList(['boobs',
                            'bosoms','bosoms',
                            'breasts','breasts','breasts',
                            'buds','buds',
                            'bust',
                            'tits',
                           ])

          self.DescNounList(['globes','globes',
                             'orbs','orbs',
                             'mounds','mounds',
                           ])

          self.SillyNounList(['boobies',
                              'breasticles',
                              'coconuts',
                              'dumplings',
                              'gazongas',
                              'jugs',
                              'knockers',
                              'mammaries',
                              'melons',
                              'teats',
                              'tatas','tiddies','titties'
                             ])
               
          self.AdjList(['bouncy',
               'bountiful',
               'budding',
               'buxom',
               'delicious',
               'double-D',
               'full',
               'fulsome',
               'generous',
               'gentle',
               'girlish',
               'glorious',
               'gorgeous',
               'heaving',
               'heavy',
               'impressive',
               'jiggling',
               'juicy',
               'luscious',
               'lush',
               'luxuriant',
               'magnificent',
               'nubile',
               'pale',
               'pendulous',
               'perky',
               'pert',
               'petite',
               'plump',
               'proud',
               'quivering',
               'ripe',
               'round',
               'sensual',
               'shapely',
               'smooth',
               'soft',
               'statuesque',
               'stunning',
               'succulent',
               'sumptuous',
               'supple',
               'surgically-enhanced',
               'swaying',
               'sweet',
               'swollen',
               'tender',
               'voluptuous'])
          
          self.DefaultNoun("breasts")
          self.Nipples = Nipples() 
          
class Clitoris(BodyParts):
     def __init__(self):
          super().__init__()

          self.StdNounList(['clit','clit','clit',
                            'clitoris','clitoris',
                           ])

          self.DescNounList(['nub',
                             'pearl'
                            ])

          self.SillyNounList(['love-button',
                              'love-nub',
                              'magic button',
                             ])
               
          self.AdjList(['delicate',
               'engorged',
               'engorged',
               'erect',
               'exposed',
               'fevered',
               'pink',
               'pulsating',
               'pulsing',
               'secret',
               'sensitive',
               'shy little',
               'swollen',
               'tender',
               'throbbing',
               'tingling'])
          
          self.DefaultNoun("clit")
          self.IsPlural = False

class VaginaInner(BodyParts):

     def __init__(self):
          super().__init__()

          self.StdNounList([
                            'vagina',
                            'vaginal canal',
                            'vestibule',
                            'womanhood'
                           ])

          self.DescNounList(['cherry',
                             'cleft',
                             'chamber',
                             'chasm',
                             'furrow',
                             'gash',
                             'hole',
                             'passage',
                             'slit',
                             'tunnel',
                            ])

          self.SillyNounList(['cock-sock',
                              'cunt-hole',
                              'fuck-tunnel',
                              'fuckhole',
                              'honey hole',
                              'honeypot',
                              'keyhole',
                              'love-channel',
                              'love-tunnel',
                             ])
                    
          self.AdjList(['cherry',
                    'cherry red',
                    'deep',
                    'deep',
                    'dripping',
                    'glazed',
                    'gushing',
                    'hungry',
                    'juicy',
                    'lewd',
                    'lustful',
                    'pink',
                    'pink',
                    'pink',
                    'secret',
                    'silken',
                    'slick',
                    'slick',
                    'snug',
                    'sopping',
                    'spread',
                    'succulent',
                    'sweet',
                    'tender',
                    'tight',
                    'velvet',
                    'velvet',
                    'wanton',
                    'well-used'])
               
          self.DefaultNoun("vaginal canal")
          self.IsPlural = False
     
class VaginaOuterLabia(BodyParts):

     def __init__(self):
          super().__init__()
          
          self.StdNounList(['labia',
                            'lips',
                            'mons pubis',
                            'outer labia',
                            'outer pussy lips',
                            'pussy lips',
                            'vulva'])

          self.DescNounList(['mound',
                             'nether lips',
                            ])

          self.AdjList(['bare',
                                   'dewy',
                                   'downy',
                                   'down-thatched',
                                   'dripping',
                                   'fat',
                                   'fat',
                                   'fleshy',
                                   'flushed',
                                   'fur-lined',
                                   'girlish',
                                   'gleaming wet',
                                   'glistening',
                                   'hairless',
                                   'honeyed',
                                   'juicy',
                                   'lickable',
                                   'luscious',
                                   'lush',
                                   'moist',
                                   'naked',
                                   'peach-fuzzed',
                                   'pink',
                                   'plump',
                                   'puffy',
                                   'shameless',
                                   'shaved',
                                   'shaven',
                                   'silken',
                                   'slick',
                                   'smooth',
                                   'succulent',
                                   'suckable',
                                   'supple',
                                   'sweet',
                                   'swollen',
                                   'tender',
                                   'trim',
                                   'wet'])
                                   
               
          self.DefaultNoun("mons pubis")

class VaginaInnerLabia(BodyParts):

     def __init__(self):
          super().__init__()

          self.StdNounList(['inner labia',
                            'labia',
                            'pussy lips',
                           ])

          self.DescNounList(['butterfly wings',
                                'flaps',
                                'flower petals',
                                'folds',
                                'fringe',
                                'lips',
                                'petals',
                               ])

          self.SillyNounList(['beef-curtains',
                              'cunt-lips',
                              'cunt-flaps',
                              'meat curtains',
                              'meat-flaps',
                              'nether-lips',
                              'piss-flaps',
                              'pussy-flaps',
                              'sex flaps',
                              'sex-lips',
                              'wizard sleeve'
                            ])

          self.AdjList(['beefy',
                        'chewy',
                        'dangling','dangling',
                        'delicate',
                        'dewy','dewy',
                        'drooping',
                        'fleshy',
                        'gossamer',
                        'lengthy',
                        'lickable',
                        'long',
                        'lush',
                        'meaty','meaty',
                        'moist',
                        'ruffled',
                        'secret',
                        'shameless',
                        'silken',
                        'shy',
                        'succulent',
                        'suckable',
                        'trim',
                        'well-used'])
                                   
          self.ColorList(['dark',
                              'drooping',
                              'droopy',
                              'little',
                              'lengthy',
                              'long',
                              'meaty',
                              'pink',
                              'purple',
                              'tender',
                              'velvet'])
                              
          self.DefaultNoun("inner labia")
               
class Vagina(BodyParts):
     InnerVag = []
     InnerLabia = []
     OuterLabia = []
     Clitoris = []
     
     def __init__(self):
          super().__init__()
          
          self.StdNounList(['cooch','coochie',
                            'cunny',
                            'cunt','cunt',
                            'muff','muffin',
                            'pussy','pussy','pussy',
                            'quim',
                            'sex',
                            'snatch',
                            'twat','twat',
                            'vagina','vagina',
                            'womanhood'
                            ])

          self.DescNounList(['flower',
                             'peach',
                            ])

          self.SillyNounList(['cherry pie',
                              'cock-garage',
                              'cock-sock',
                              'cunt-hole',
                              'fuckhole',
                              'fur-burger',
                              'honey-hole',
                              'honeypot',
                              'love-muffin',
                              'pie',
                             ])
                            
          self.AdjList(['bare',
                         'cherry',
                         'clenched',
                         'delightful',
                         'dewy',
                         'down-thatched',
                         'dripping',
                         'exposed',
                         'fuckable',
                         'fur-lined',
                         'girlish',
                         'gleaming wet',
                         'glistening',
                         'gushing',
                         'hairless',
                         'honeyed',
                         'horny',
                         'hungry',
                         'juicy',
                         'leaky',
                         'lewd',
                         'lickable',
                         'luscious',
                         'lush',
                         'lustful',
                         'moist',
                         'naked',
                         'needful',
                         'peach-fuzzed',
                         'puffy',
                         'shameless',
                         'silken',
                         'slick',
                         'slutty',
                         'smooth',
                         'sopping',
                         'succulent',
                         'suckable',
                         'supple',
                         'sweet',
                         'swollen',
                         'tender',
                         'tight',
                         'trim',
                         'unsullied',
                         'velvet',
                         'wanton',
                         'well-used',
                         'willing'])
          
          self.DefaultNoun("vagina")
          self.IsPlural = False
          self.InnerVag = VaginaInner()
          self.OuterLabia = VaginaOuterLabia()
          self.InnerLabia = VaginaInnerLabia()
          self.Clitoris = Clitoris()


class AnusFemale(BodyParts):
     def __init__(self):
          super().__init__()

          self.StdNounList(['anus','anus','anus','anus',
                            'asshole','asshole','asshole','asshole',
                            'bowels',
                            'butthole','butthole','butt hole',
                            'rectum','rectum',
                            'sphincter','sphincter',
                            ])

          self.DescNounList(['back orifice',
                             'back passage',
                             'backdoor',
                             'brown hole',
                             'brown star',
                             'heinie hole',
                             'knot',
                             'rear orifice',
                             'rectal cavity',
                             'rosebud',
                            ])

          self.SillyNounList(['arse-cunt',
                              'back-pussy',
                              'bunghole',
                              'chocolate starfish',
                              'corn hole',
                              'dirt-pipe',
                              'dirt-box',
                              'fart blaster',
                              'fart-box',
                              'fart-hole',
                              'poop-chute',
                              'poop-trap',
                              'pooper',
                              'shit-hole',
                              'shitter',
                              'starfish','starfish',
                             ])
       
          self.AdjList(['brown',
               'clenched',
               'forbidden',
               'fuckable',
               'gaping',
               'knotted',
               'lewd',
               'little','little','little','little',
               'loose',
               'nasty',
               'naughty',
               'pert',
               'puckered',
               'rusty',
               'shy',
               'smooth',
               'snug','snug',
               'taboo',
               'tender',
               'tight','tight','tight','tight',
               'wanton',
               'well-used',
               'willing',
               'winking'])
          
          self.DefaultNoun("anus")
          self.IsPlural = False
          
class ButtocksFemale(BodyParts):
     def __init__(self):
          super().__init__()
     
          self.NounList(['buns',
               'butt-cheeks',
               'buttocks',
               'cheeks'])
               
          self.AdjList(['ample',
               'chubby',
               'curvaceous',
               'curvy',
               'cute',
               'fat',
               'honeyed',
               'jiggling',
               'juicy',
               'luscious',
               'muscular',
               'plump',
               'rotund',
               'round',
               'rounded',
               'shapely','shapely','shapely',
               'smooth',
               'squeezable','squeezable',
               'succulent',
               'supple',
               'sweet',
               'tender',
               'thick','thick','thick',
               'tight',
               'trim',
               'voluptuous',
               'well-rounded'])
               
          self.ColorList(['bronzed',
                              'black',
                              'brown',
                              'coffee-colored',
                              'creamy',
                              'dark',
                              'pale',
                              'pink',
                              'rosy',
                              'sun-kissed',
                              'tanned'
                            ])
          
          self.DefaultNoun("buttocks")
          
class AssFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksFemale()
          
          self.NounList(['ass',
               'backside',
               'behind',
               'booty',
               'bottom',
               'bum',
               'butt',
               'gluteous maximus',
               'heinie',
               'rump',
               'tush',
               'tushy'])
               
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
               
          self.ColorList(['bronzed',
                              'black',
                              'brown',
                              'coffee-colored',
                              'creamy',
                              'dark',
                              'pale',
                              'pink',
                              'rosy',
                              'sun-kissed',
                              'tanned'
                            ])
          
          self.DefaultNoun("ass")
          
class BodyFemale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['anatomy',
               'body',
               'body',
               'body',
               'body',
               'curves',
               'figure',
               'form',
               'physique'])
               
          self.AdjList(['beautiful',
               'busty',
               'buxom',
               'curvaceous',
               'curvy',
               'feminine',
               'gorgeous',
               'leggy',
               'little',
               'lush',
               'luxuriant',
               'model-esque',
               'nubile',
               'pale',
               'ravishing',
               'ripe',
               'sensual',
               'sexy',
               'shameless',
               'shapely',
               'slender',
               'statuesque',
               'stunning',
               'sultry',
               'sweet',
               'teenage',
               'tight',
               'voluptuous',
               'womanly',
               'young',
               'youthful'])
               
          self.ColorList(['black',
                              'brown',
                              'coffee-colored',
                              'mocha',
                              'pale',
                              'pink',
                              'tanned'
                            ])
          
          self.DefaultNoun("body")
          self.DefaultAdj("nubile")
          self.IsPlural = False
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
          
     def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
          sPartDesc = ""
          
          if sPossessive is None:
               sPossessive = ""
          
          PartNotList = []
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
               sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          else:
               sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          
          if bAddArticles:
               sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bExplicit = False, bAllowLongDesc = True, sPossessive = None):
          sBodyDesc = ""
          
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
          
          self.StdNounList(['head','head','head',
               'tip','tip','tip'])

          self.DescNounList(['helmet',
                             'mushroom','mushroom','mushroom',
                            ])

          self.SillyNounList(['cock-head',
                              'dick-tip',
                              'knob','knob',
                             ])
               
          self.AdjList(['broad',
                        'bulging',
                        'dripping',
                        'engorged',
                        'fat',
                        'glistening',
                        'pulsating',
                        'purple',
                        'smooth',
                        'swollen',
                        'thick',
                        'throbbing',
                        'tumescent'])
               
          self.ColorList(['black',
               'brown',
               'purple',
               'red'])
          
          self.DefaultNoun("head")
          self.IsPlural = False
          
class Testicles(BodyParts):
     def __init__(self):
          super().__init__()

          self.StdNounList(['balls','balls','balls',     
                            'gonads',
                            'scrotum','scrotum',
                            'testicles','testicles',
                           ])

          self.DescNounList(['sack',
                             'silk purse',
                            ])

          self.SillyNounList(['ballsack','ballsacks',
                              'bollocks',
                              'nuts','nutsack',
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
          
          while sPenis in self.GetNounList():
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

          self.StdNounList(['cock','cock','cock',
                            'dick','dick','dick',
                            'erection','erection',
                            'hard-on',
                            'member',
                            'organ',
                            'penis','penis','penis','penis',
                            'phallus',
                            'prick',
                            'thing',
                            'tool',
                           ])

          self.DescNounList(['girth',
                             'hardness',
                             'pole',
                             'rod',
                             'sausage',
                             'serpent',
                             'shaft',
                             'snake',
                             'stalk',
                             'stem',
                            ])

          self.SillyNounList(['boner',
                              'cock meat',
                              'cocksicle',
                              'goo-gun',
                              'hot-rod',
                              'joystick',
                              'lady-dagger',
                              'love-gun',
                              'meat',
                              'monster',
                              'popsicle',
                              'ramrod',
                              'schlong',
                              'wood',
                             ])
               
          self.AdjList(['bald',
               'black',
               'beautiful',
               'beefy',
               'bent',
               'big','big','big','big',
               'broad','broad',
               'bulging','bulging',
               'burning',
               'carefully man-scaped',
               'circumcized',
               'crooked',
               'curved',
               'delicious',
               'dripping',
               'engorged','engorged',
               'enormous',
               'enormously erect',
               'erect',
               'erect',
               'fat','fat','fat','fat',
               'fevered','feverish',
               'firm','firm','firm',
               'fully engorged',
               'fully erect',
               'girthy','girthy',
               'glistening',
               'god-like',
               'gorgeous',
               'greasy','greasy','greasy','greasy',
               'hairy',
               'hairless',
               'hard','hard','hard',
               'hardened',
               'heavy',
               'hefty',
               'hooked',
               'hot','hot',
               'huge',
               'hugely erect',
               'impressive',
               'legendary',
               'lengthy',
               'long',
               'lovingly man-scaped',
               'lustful','lustful',
               'magnificient',
               'massive',
               'massively erect',
               'meaty','meaty','meaty',
               'monstrous',
               'mouth-watering',
               'oily',
               'pierced',
               'pink',
               'powerful',
               'pretty',
               'proud',
               'pulsating',
               'purple',
               'raging',
               'rampant',
               'red',
               'ribbed',
               'rigid',
               'rock-hard',
               'serpentine',
               'silken',
               'smooth','smooth','smooth',
               'stiff','stiff',
               'strong','strong','strong',
               'swollen','swollen',
               'tall',
               'tasty','tasty','tasty',
               'thick','thick','thick',
               'throbbing','throbbing',
               'towering',
               'tumescent',
               'turgid','turgid',
               'uncircumcized',
               'uncut',
               'veiny','veiny','veiny','veiny',
               'virile',
               'warm',
               'wrinkled','wrinkled',
               'well-oiled',
               'youthful',
              ])
               
          self.PenisFrontPart = ['beef',
               'flesh',
               'fuck',
               'love',
               'man',
               'meat']
               
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
               'tube',
               'weapon',
               'worm']
          
          self.DefaultNoun("cock")
          self.IsPlural = False
          self.Head = PenisHead()
          self.Testicles = Testicles()
          
          if bAllowBAP:
               iLen = len(self.GetStdNounList()) + len(self.GetDescNounList()) + len(self.GetSillyNounList())
               for i in range(0, int(iLen * (2/3))):
                    self.GetSillyNounList().append(self.BuildAPenis())
     
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
               
     def ShortDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAddLen = False, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().ShortDescription(sNot = "", ExtraAdjList = ExtraAdjList, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns)
          
     def MediumDescription(self, ExtraAdjList = None, sNot = "",  NotList = None, bAddLen = False, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
               
          return super().MediumDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns) 
          
     def FloweryDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAddLen = False, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().FloweryDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns) 
          
     def RandomDescription(self, ExtraAdjList = None, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False, bStdNouns = True, bDescNouns = True, bSillyNouns = True):
          if NotList == None:
               NotList = []
          
          if sNot != "":
               NotList.append(sNot)

          if ExtraAdjList is None:
               ExtraAdjList = []

          if bAddLen:
               ExtraAdjList.append(self.GenerateLength())
          
          return super().RandomDescription(ExtraAdjList = ExtraAdjList, sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc, bStdNouns = bStdNouns, bDescNouns = bDescNouns, bSillyNouns = bSillyNouns) 
     
class Semen(BodyParts):
     def __init__(self):
          super().__init__()

          self.StdNounList(['cum','cum','cum','cum',
                            'seed','seed',
                            'semen','semen','semen',
                            'sperm','sperm',
                            'splooge',
                            'spunk',
                           ])

          self.DescNounList(['cream',
                             'gravy',
                             'lotion',
                             'man-milk',
                             'man-seed',
                             'sauce',
                            ])

          self.SillyNounList(['baby batter',
                                 'baby gravy',
                                 'cock milk',
                                 'cock-snot',
                                 'daddy sauce',
                                 'dick juice',
                                 'jizm','jizz','jizz',
                                 'load',
                                 'love juice',
                                 'man-custard',
                                 'man-jam',
                                 'man-o-naise',
                                 'nut-butter',
                                 'penis pudding',
                                 'throat yogurt',
                                 'trouser gravy',
                                 'weiner sauce',
                                ])
               
          self.AdjList(['creamy','creamy','creamy',
               'delicious',
               'glossy',
               'gooey','gooey','gooey',
               'hot','hot','hot',
               'nasty',
               'nourishing',
               'oozing',
               'ropy',
               'salty','salty',
               'silken',
               'silky',
               'sloppy','sloppy',
               'sticky','sticky','sticky','sticky',
               'tasty',
               'thick','thick','thick','thick',
               'warm','warm','warm',
               'white-hot','white-hot',
               'yummy',
               'cream-colored',
               'milky',
               'pearly',
               'pearlescent'])
          
          self.DefaultNoun("semen")
          self.DefaultAdj("gooey")
          
class ButtocksMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['buns',
               'butt cheeks',
               'buttocks',
               'glutes'])
               
          self.AdjList(['beefy',
               'broad',
               'bronzed',
               'chiseled',
               'compact',
               'hairy',
               'lean',
               'manly',
               'masculine',
               'muscular',
               'rock-hard',
               'sexy',
               'smooth',
               'strapping',
               'swole',
               'taut',
               'tan',
               'tight','tight',
               'trim',
               'virile',
               'well-defined'])
          
          self.DefaultNoun("buttocks")
          
class AssMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksMale()
          
          self.NounList(['ass',
               'backside',
               'behind',
               'bottom',
               'bum',
               'buns',
               'butt',
               'gluteous maximus',
               'rump',
               'tush'])
               
          self.AdjList(['beefy',
               'broad',
               'bronzed',
               'chiseled',
               'compact',
               'hairy',
               'lean',
               'manly',
               'masculine',
               'muscular',
               'naked',
               'powerful',
               'rippling',
               'rock-hard',
               'smooth',
               'strapping',
               'supple',
               'taut',
               'tight',
               'trim',
               'virile',
               'well-defined'])
          
          self.DefaultNoun("buttocks")
          
class SkinMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['skin',
               'skin',
               'skin',
               'flesh',
               'hide'])
               
          self.AdjList(['bare',
               'exposed',
               'glistening',
               'hairy',
               'leathery',
               'naked',
               'rough',
               'rugged',
               'smooth',
               'supple',
               'tough',
               'warm',
               'youthful'])
               
          self.ColorList(['bronzed',
                              'brown',
                              'coffee-colored',
                              'dark',
                              'ebony',
                              'freckled',
                              'light-colored',
                              'pale',
                              'sun-browned',
                              'tanned'
                            ])
          
          self.DefaultNoun("skin")
          self.DefaultAdj("rugged")
          
class ShouldersMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['shoulders'])
               
          self.AdjList(['bare',
               'brawny',
               'broad',
               'freckled',
               'mighty',
               'muscular',
               'naked',
               'powerful',
               'rugged',
               'strong',
               'sturdy',
               'well-built',
               'wide'])
               
          self.ColorList(['bronzed',
                              'brown',
                              'coffee-colored',
                              'dark',
                              'ebony',
                              'sun-browned',
                              'tanned'
                            ])
          
          self.DefaultNoun("shoulders")
          self.DefaultAdj("broad")
          
class MusclesMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['muscles'])
               
          self.AdjList(['bare',
               'brawny',
               'broad',
               'bulging',
               'burly',
               'chiseled',
               'hard',
               'hulking',
               'impressive',
               'lean',
               'magnificent',
               'massive',
               'mighty',
               'powerful',
               'robust',
               'rugged',
               'sinewy',
               'strapping','strapping',
               'strong',
               'sturdy',
               'supple',
               'taut',
               'toned',
               'tight',
               'well-built',
               'well-defined',
               'whip-cord',
               'wood-carved'])
               
          self.ColorList(['bronzed',
                              'dark',
                              'tanned'
                            ])
          
          self.DefaultNoun("shoulders")
          self.DefaultAdj("broad")
          
class ChestMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['chest',
               'chest',
               'chest',
               'chest',
               'pectorals'])
               
          self.AdjList(['bare',
               'brawny',
               'broad',
               'burly',
               'compact',
               'dark-thatched',
               'expansive',
               'hairy',
               'lusty',
               'mighty',
               'muscular',
               'naked',
               'powerful',
               'rippling',
               'ripped',
               'rugged',
               'strapping',
               'strong',
               'sturdy',
               'toned',
               'wide',
               'uncovered',
               'virile',
               'well-built',
               'well-defined',
               'well-oiled'])
               
          self.ColorList(['bronzed',
                              'brown',
                              'coffee-colored',
                              'dark',
                              'ebony',
                              'sun-browned',
                              'tanned'
                            ])
          
          self.DefaultNoun("chest")
          self.DefaultAdj = "broad"
          
class ArmsMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['arms',
               'arms',
               'arms',
               'arms',
               'limbs'])
               
          self.AdjList(['athletic',
               'bare',
               'brawny',
               'bronzed',
               'burly',
               'long',
               'mighty',
               'muscular',
               'naked',
               'powerful',
               'protective',
               'rippling',
               'ripped',
               'sinewy',
               'strapping',
               'strong',
               'sturdy',
               'thick',
               'toned',
               'trunk-like',
               'well-built',
               'wiry'])
          
          self.DefaultNoun("arms")
          self.DefaultAdj("muscular")
          
class EyesMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['eyes'])
               
          self.AdjList(['alluring',
               'beautiful',
               'bright',
               'brooding',
               'captivating',
               'clear',
               'dazzling',
               'deep',
               'earnest',
               'electric',
               'electrifying',
               'kind',
               'mischievous',
               'penetrating',
               'soulful',
               'sparkling',
               'steely',
               'stern',
               'sweet',
               'youthful',
               'wide'])
               
          self.ColorList(['blue',
                              'brown',
                              'dark',
                              'gray',
                              'green',
                              'hazel',
                              'icy-blue',
                              'steely-blue'
                            ])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("penetrating")

class FacialHair(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['beard','beard','beard',
               'fuzz',
               'goatee',
               'moustache',
               'stubble',
               'fro'])
               
          self.AdjList(['bristling',
               'bushy',
               'curly',
               'full',
               'glossy',
               'long',
               'luxuriant',
               'magnificent',
               'manly',
               'messy',
               'silken',
               'short',
               'thick',
               'trimmed',
               'unkempt',
               'untamed',
               'well-trimmed',
               'wild',
               'wiry'])
               
          self.ColorList(['black','black',
                              'blonde','blonde',
                              'brown',
                              'coifed',
                              'dark',
                              'graying',
                              'sandy',
                              'red'])
                              
          
          self.DefaultNoun("hair")
          self.DefaultAdj("glossy")
          
class HairMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['afro',
               'bouffant',
               'coif',
               'dreads',
               'fro',
               'hair','hair','hair',
               'locks'])
               
          self.AdjList(['curly',
               'glossy',
               'long',
               'luxuriant',
               'measy',
               'silken',
               'shaggy',
               'short',
               'spiky',
               'untamed',
               'vibrant',
               'wavy',
               'wild'])
               
          self.ColorList(['black','black',
                              'blonde','blonde',
                              'brunette',
                              'coifed',
                              'dark',
                              'dyed green',
                              'flaming-red',
                              'golden',
                              'graying',
                              'platinum blonde',
                              'punk blue',
                              'sandy',
                              'red'])
                              
          
          self.DefaultNoun("hair")
          self.DefaultAdj("glossy")
          
class LegsMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['legs',
               'legs',
               'legs',
               'calves',
               'limbs',
               'thighs'])
               
          self.AdjList(['athletic',
               'bare',
               'brawny',
               'bronzed',
               'burly',
               'long',
               'mighty',
               'muscular',
               'naked',
               'powerful',
               'rangy',
               'rippling',
               'sinewy',
               'strapping',
               'strong',
               'sturdy',
               'thick',
               'toned',
               'trunk-like',
               'well-built',
               'wiry'])
          
          self.DefaultNoun("legs")
          self.DefaultAdj("sinewy")
          
class JawMale(BodyParts):
     def __init__(self):
          super().__init__()
          
          self.NounList(['jaw'])
               
          self.AdjList(['bearded',
               'chiseled',
               'commanding',
               'decisive',
               'dominant',
               'forceful',
               'handsome',
               'powerful',
               'rugged',
               'scruffy',
               'sharp',
               'striking'])
          
          self.DefaultNoun("jaw")
          self.DefaultAdj("chiseled")
          
class BodyMale(BodyParts):     
    def __init__(self):
        super().__init__()
          
        self.NounList(['body','body','body','body',
            'form',
            'physique',
            'bulk',
            'build',
            'physique'])
               
        self.AdjList(['beefy',
            'brawny',
            'broad',
            'bronzed',
            'burly',
            'commanding',
            'compact',
            'dark-thatched',
            'handsome',
            'hardened',
            'hearty',
            'hung',
            'husky',
            'lanky',
            'lean',
            'limber',
            'manly',
            'masculine',
            'massive',
            'muscular',
            'powerful',
            'rugged',
            'sinewy',
            'smooth',
            'strapping',
            'striking',
            'strong',
            'sturdy',
            'supple',
            'tall',
            'taut',
            'tight',
            'toned',
            'towering',
            'trim',
            'virile','virile',
            'well-built',
            'well-hung',
            'wiry',
            'youthful'])
          
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