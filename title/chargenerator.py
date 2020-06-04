#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import TempType 
from title.chartemplates import *
from util import *
from title.util import TempType
from title.util import MaleCharType 
          
class FemaleChar(Character):
    def __init__(self, ReqList = [], ExclList = [],
                        TempType = TempType.Flowery,
                        Type = GirlType.Neutral, 
                        NotList = None, 
                        bAddTheArticle = False, 
                        bAddAnArticle = False,
                        sPosArticle = "My", 
                        bSplitArticle = False,
                        bAddEndNoun = True,
                        bAllowAttitude = True, 
                        bAllowPhysChar = True, 
                        bAllowSkinHairColor = True, 
                        bAllowGenMod = True, 
                        bAllowClothing = True, 
                        bAllowAge = True, 
                        bAllowPregState = True, 
                        bAllowMaritalStatus = True,     
                        bAllowNation = True, 
                        bAllowProf = True, 
                        bAllowSpecies = True, 
                        bAllowSexuality = True, 
                        bAllowTrope = True, 
                        bAllowRelate = False, 
                        bAllowTitle = True,
                        SelectTemplateID = 0,
                        MaxChars = 9999):
        super().__init__()
        if NotList is None:
            NotList = []
          
        self.Gender = Gender.Female 
        self.GirlType = Type
          
        # add any CharBits that we are going to exclude to the exclusion list
          
        if not bAllowAttitude:
            ExclList.append(AttitudeFemale())
            ExclList.append(AttitudeBadFemale())
            ExclList.append(AttitudeGoodFemale())
        if not bAllowPhysChar:
            ExclList.append(PhysCharFemale())
        if not bAllowSkinHairColor:
            ExclList.append(SkinHairColorFemale())
        if not bAllowGenMod:
            ExclList.append(GenModFemale())
        if not bAllowClothing:
            ExclList.append(ClothingFemale())
        if not bAllowPregState:
            ExclList.append(PregState())
        if not bAllowMaritalStatus:
            ExclList.append(MaritalStatusFemale())
        if not bAllowNation:
            ExclList.append(NationFemale())
        if not bAllowProf:
            ExclList.append(ProfFemale())
            ExclList.append(ProfBadFemale())
            ExclList.append(ProfGoodFemale())
        if not bAllowSpecies:
            ExclList.append(SpeciesFemale())
        if not bAllowSexuality:
            ExclList.append(SexualityFemale())
        if not bAllowRelate:
            ExclList.append(RelateFemale())     
        if not bAllowTitle:
            ExclList.append(TitlesFemale())

        TemplateList = []
        for subclass in FemCharTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        for subclass in FemTropeTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)       

        for subclass in FemSpeciesTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        SelectionList = self.BuildSelectionList(bAllowTrope = bAllowTrope, bAllowSpecies = bAllowSpecies)
          
        self.SetCharDesc(TemplateList = TemplateList, 
                         SelectionList = SelectionList,
                         ReqList = ReqList,
                         ExclList = ExclList, 
                         TempType = TempType,
                         NotList = NotList, 
                         bAddEndNoun = bAddEndNoun,
                         bAddTheArticle = bAddTheArticle,
                         bAddAnArticle = bAddAnArticle,
                         sPosArticle = sPosArticle,
                         bSplitArticle = bSplitArticle,
                         SelectTemplateID = SelectTemplateID,
                         MaxChars = MaxChars)
          
    def BuildSelectionList(self, bAllowTrope, bAllowSpecies):
        SelectionList = []

        iStdCount = 0
          
        for subclass in FemCharTemplate.__subclasses__():
            template = subclass()
            if (self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType) \
                and not template.RequestOnly:
                i = 0
                while i < template.Priority * 5:
                    SelectionList.append(template)
                    i = i + 1
                    iStdCount = iStdCount + 1
                
        if bAllowTrope:
            for subclass in FemTropeTemplate.__subclasses__():
                template = subclass()
                if (self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType) \
                    and not template.RequestOnly:
                    i = 0
                    while i < template.Priority * 2:
                        SelectionList.append(template)
                        i = i + 1
     
        if bAllowSpecies:
            for subclass in FemSpeciesTemplate.__subclasses__():
                template = subclass()
                if () \
                    and not template.RequestOnly:
                    i = 0
                    while i < template.Priority:
                        SelectionList.append(template)
                        i = i + 1
          
        if len(SelectionList) == 0:
            print("=*= WARNING =*= FemaleChar() template list is empty")
        else:
            print("Template List length is " + str(len(SelectionList)) + "\nTEMPLATE LIST")
            #print("NAME:\t\t\tID\tGIRL TYPE:\tTEMPLATE TYPE:")
            #sTable = ""
            #for item in SelectionList:
            #    sObjName = str(item).split(" ")[0][21:]
            #    sTable += sObjName 
            #    iNumSpaces = 25 - len(sObjName)
            #    i = 0
            #    while i < iNumSpaces:
            #        sTable += " "
            #        i = i + 1

            #    sTable += str(item.ID) + "\t"
            #    if item.GirlType == GirlType.Good:
            #        sTable += "good"
            #    elif item.GirlType == GirlType.Bad:
            #        sTable += "bad"
            #    else: 
            #        sTable += "neutral"
            #    sTable += "\t\t"
            #    if isinstance(item,FemTropeTemplate):
            #        sTable += "Female Trope"
            #    elif isinstance(item,FemSpeciesTemplate):
            #        sTable += "Female Species"
            #    elif isinstance(item,FemNiceGirlTemplate1):
            #        sTable += "Nice Girl"
            #    elif isinstance(item,FemLesbianTemplate1):
            #        sTable += "Lesbian"
            #    else:
            #        sTable += "Female Template"
            #    sTable += "\n"

            #print(sTable)

            #print("There are " + str(iStdCount) + " standard fem templates out of " + str(len(SelectionList)) + " (" + str(round(100 * (iStdCount / len(SelectionList)),2)) + "%)")

        return SelectionList

class LesbianChar(Character):
     def __init__(self, ReqList = [], ExclList = [],
                            TempType = TempType.Flowery,
                            Type = GirlType.Neutral, 
                            NotList = None, 
                            bAddTheArticle = False, 
                            bAddAnArticle = False,
                            sPosArticle = "My", 
                            bSplitArticle = False,
                            bAddEndNoun = True,
                            bAllowAttitude = True, 
                            bAllowPhysChar = True, 
                            bAllowSkinHairColor = True, 
                            bAllowGenMod = True, 
                            bAllowClothing = True, 
                            bAllowAge = True, 
                            bAllowPregState = True, 
                            bAllowMaritalStatus = True,     
                            bAllowNation = True, 
                            bAllowProf = True, 
                            bAllowSpecies = True, 
                            bAllowSexuality = True, 
                            bAllowTrope = True, 
                            bAllowRelate = False, 
                            bAllowTitle = True,
                            SelectTemplateID = 0,
                            MaxChars = 9999):
          super().__init__()

          if NotList is None:
               NotList = []
          
          self.Gender = Gender.Female 
          self.GirlType = Type
          
          # add any CharBits that we are going to exclude to the exclusion list
          
          if not bAllowAttitude:
               ExclList.append(AttitudeFemale())
               ExclList.append(AttitudeBadFemale())
               ExclList.append(AttitudeGoodFemale())
          if not bAllowPhysChar:
               ExclList.append(PhysCharFemale())
          if not bAllowSkinHairColor:
               ExclList.append(SkinHairColorFemale())
          if not bAllowGenMod:
               ExclList.append(GenModFemale())
          if not bAllowClothing:
               ExclList.append(ClothingFemale())
          if not bAllowPregState:
               ExclList.append(PregState())
          if not bAllowMaritalStatus:
               ExclList.append(MaritalStatusFemale())
          if not bAllowNation:
               ExclList.append(NationFemale())
          if not bAllowProf:
               ExclList.append(ProfFemale())
               ExclList.append(ProfBadFemale())
               ExclList.append(ProfGoodFemale())
          if not bAllowSpecies:
               ExclList.append(SpeciesFemale())
          if not bAllowSexuality:
               ExclList.append(SexualityFemale())
          if not bAllowRelate:
               ExclList.append(RelateFemale())     
          if not bAllowTitle:
               ExclList.append(TitlesFemale())
               
          TemplateList = []
          for subclass in FemLesbianTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

          SelectionList = self.BuildTemplateList()
          
          self.SetCharDesc(TemplateList = TemplateList, 
                           SelectionList = SelectionList,
                           ReqList = ReqList,
                           ExclList = ExclList, 
                           TempType = TempType,
                           NotList = NotList, 
                           bAddEndNoun = bAddEndNoun,
                           bAddTheArticle = bAddTheArticle,
                           bAddAnArticle = bAddAnArticle,
                           sPosArticle = sPosArticle,
                           bSplitArticle = bSplitArticle,
                           SelectTemplateID = SelectTemplateID,
                           MaxChars = MaxChars)
          
     def BuildTemplateList(self):
          SelectionList = []
          
          for subclass in FemLesbianTemplate.__subclasses__():
            template = subclass()
            i = 0
            while i < template.Priority * 5:
                SelectionList.append(template)
                i = i + 1

          if len(SelectionList) == 0:
              print("=*= WARNING =*= LesbianChar() template list is empty")
          
          return SelectionList
          
class MaleChar(Character):
     def __init__(self, ReqList = [], ExclList = [],
                            MaleCharType = MaleCharType.Straight,
                            TempType = TempType.Flowery,
                            NotList = None, 
                            bAddTheArticle = False, 
                            bAddAnArticle = False,
                            sPosArticle = "My", 
                            bSplitArticle = False,
                            bAddEndNoun = True,
                            bAllowGang = False,
                            bAllowAttitude = True, 
                            bAllowPhysChar = True, 
                            bAllowDickChar = True, 
                            bAllowSkinHairColor = True, 
                            bAllowGenMod = True, 
                            bAllowTypeMod = True,
                            bAllowClothing = True,
                            bAllowAge = True, 
                            bAllowMaritalStatus = True,
                            bAllowNation = True, 
                            bAllowProf = True, 
                            bAllowSpecies = True, 
                            bAllowTrope = True, 
                            bAllowRelate = False,
                            bAllowTitle = True,
                            SelectTemplateID = 0,
                            MaxChars = 9999):
          super().__init__()
               
          bShowGangChar = self.ShowGangChar(bAllowGang)
          
          if (MaleCharType == MaleCharType.Straight and bShowGangChar and bAddAnArticle) or MaleCharType == MaleCharType.GangSingular:
          # show singular gang character 
               Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType.GangSingular, 
                                                   ReqList = ReqList,
                                                   ExclList = ExclList, 
                                                   NotList = NotList, bAddTheArticle = bAddTheArticle,
                                                   bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, bSplitArticle = bSplitArticle,
                                                   bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
                                                   bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
                                                   bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
                                                   bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
                                                   bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID,
                                                   MaxChars = MaxChars) 
          elif (MaleCharType == MaleCharType.Straight and bShowGangChar and bAddTheArticle) or MaleCharType == MaleCharType.GangAny:
          # show any gang character 
               Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType.GangAny,
                                                   ReqList = ReqList,
                                                   ExclList = ExclList, 
                                                   NotList = NotList, bAddTheArticle = bAddTheArticle, bSplitArticle = bSplitArticle,
                                                   bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, 
                                                   bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
                                                   bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
                                                   bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
                                                   bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
                                                   bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID,
                                                   MaxChars = MaxChars) 
          elif MaleCharType == MaleCharType.GangSingular or MaleCharType == MaleCharType.GangPlural:
          # show gang character depending on parameter passed in
               Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType, 
                                                   ReqList = ReqList,
                                                   ExclList = ExclList,
                                                   NotList = NotList, bAddTheArticle = bAddTheArticle,
                                                   bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, bSplitArticle = bSplitArticle,
                                                   bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
                                                   bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
                                                   bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
                                                   bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
                                                   bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID,
                                                   MaxChars = MaxChars) 
          else:
          # show a normal straight character
               Char = StraightMaleChar(TempType = TempType, NotList = NotList, bAddTheArticle = bAddTheArticle,
                                                   ReqList = ReqList,
                                                   ExclList = ExclList,
                                                   bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, bSplitArticle = bSplitArticle,
                                                   bAddEndNoun = bAddEndNoun, bAllowAttitude = bAllowAttitude, 
                                                   bAllowPhysChar = bAllowPhysChar, bAllowDickChar = bAllowDickChar, 
                                                   bAllowSkinHairColor = bAllowSkinHairColor, bAllowGenMod = bAllowGenMod,
                                                   bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
                                                   bAllowAge = bAllowAge, bAllowMaritalStatus = bAllowMaritalStatus,
                                                   bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
                                                   bAllowSpecies = bAllowSpecies, bAllowTrope = bAllowTrope, 
                                                   bAllowRelate = bAllowRelate,bAllowTitle = bAllowTitle,
                                                   SelectTemplateID = SelectTemplateID,
                                                   MaxChars = MaxChars) 
     
          
          self.Desc = Char.Desc

     def ShowGangChar(self, bAllowGangChar):
          bShowGangChar = False 
          
          if bAllowGangChar:
               if randint(1,4) == 1:
                    bShowGangChar = True
          
          return bShowGangChar
               
class StraightMaleChar(Character):
    def __init__(self, ReqList = [], ExclList = [],
                        TempType = TempType.Flowery,
                        NotList = None, 
                        bAddTheArticle = False, 
                        bAddAnArticle = False,
                        sPosArticle = "My", 
                        bAddEndNoun = True,
                        bSplitArticle = False,
                        bAllowAttitude = True, 
                        bAllowPhysChar = True, 
                        bAllowDickChar = True, 
                        bAllowSkinHairColor = True, 
                        bAllowGenMod = True, 
                        bAllowTypeMod = True,
                        bAllowClothing = True,
                        bAllowAge = True, 
                        bAllowMaritalStatus = True,
                        bAllowNation = True, 
                        bAllowProf = True, 
                        bAllowSpecies = True, 
                        bAllowTrope = True, 
                        bAllowRelate = False,
                        bAllowTitle = True,
                        SelectTemplateID = 0,
                        MaxChars = 9999):
        super().__init__()
        #print("CharGenerator.MaleChar() started")
        if NotList is None:
            NotList = []
          
        self.Gender = Gender.Male 
          
        ExclusionList = []
        if not bAllowGenMod:
            ExclusionList.append(GenModMale())
        if not bAllowTypeMod:
            ExclusionList.append(TypeModMale())
        if not bAllowAttitude:
            ExclusionList.append(AttitudeMale())
        if not bAllowPhysChar:
            ExclusionList.append(PhysCharMale())
        if not bAllowDickChar:
            ExclusionList.append(DickCharMale())
        if not bAllowSkinHairColor:
            ExclusionList.append(SkinHairColorMale())
        if not bAllowClothing:
            ExclusionList.append(ClothesMale())
        if not bAllowMaritalStatus:
            ExclusionList.append(MaritalStatusMale())
        if not bAllowNation:
            ExclusionList.append(NationMale())
            ExclusionList.append(NationNounMale())
        if not bAllowAge:
            ExclusionList.append(AgeAdjMale())
        if not bAllowProf:
            ExclusionList.append(ProfBlueCollarMale())
            ExclusionList.append(ProfWhiteCollarMale())
            ExclusionList.append(ProfFantasyMale())
            ExclusionList.append(ProfAthleteMale())
            ExclusionList.append(ProfRockstarMale())
            ExclusionList.append(ProfNormalMale())
            ExclusionList.append(ProfAspirationalMale())
            ExclusionList.append(ProfMale())
        if not bAllowSpecies:
            ExclusionList.append(SpeciesMale())
        if not bAllowRelate:
            ExclusionList.append(RelateMale())     
        if not bAllowTitle:
            ExclusionList.append(TitlesMale())
          
        TemplateList = []
        for subclass in MaleCharTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        for subclass in MaleTropeTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        for subclass in MaleSpeciesTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        SelectionList = self.BuildTemplateList(bAllowTrope = bAllowTrope, bAllowSpecies = bAllowSpecies)
          
        self.SetCharDesc(TemplateList = TemplateList,  
                         SelectionList = SelectionList,
                         ReqList = ReqList,
                         ExclList = ExclList,  
                         TempType = TempType,
                         NotList = NotList, 
                         bAddEndNoun = bAddEndNoun,
                         bAddTheArticle = bAddTheArticle,
                         bAddAnArticle = bAddAnArticle,
                         sPosArticle = sPosArticle,
                         bSplitArticle = bSplitArticle,
                         SelectTemplateID = SelectTemplateID,
                         MaxChars = MaxChars)

    def BuildTemplateList(self, bAllowTrope, bAllowSpecies):
        SelectionList = []
          
        for subclass in MaleCharTemplate.__subclasses__():
            template = subclass()
            if not template.RequestOnly:
                i = 0
                while i < template.Priority:
                    SelectionList.append(template)
                    i = i + 1
          
        if bAllowTrope:
            for subclass in MaleTropeTemplate.__subclasses__():
                template = subclass()
                if not template.RequestOnly:
                    i = 0
                    while i < template.Priority:
                        SelectionList.append(template)
                        i = i + 1
               
        if bAllowSpecies:
            for subclass in MaleSpeciesTemplate.__subclasses__():
                template = subclass()
                if not template.RequestOnly:
                    i = 0
                    while i < template.Priority:
                        SelectionList.append(template)
                        i = i + 1

        if len(SelectionList) == 0:
            print("=*= WARNING =*= StraightMaleChar() template list is empty")
              
        return SelectionList

class GangMaleChar(Character):
    def __init__(self, ReqList = [], ExclList = [],
                        TempType = TempType.Flowery,
                        MaleCharType = MaleCharType.GangAny,
                        NotList = None, 
                        bAddTheArticle = False, 
                        bAddAnArticle = False,
                        sPosArticle = "My", 
                        bAddEndNoun = True,  
                        bSplitArticle = False,
                        bAllowPhysChar = True, 
                        bAllowDickChar = True, 
                        bAllowGenMod = True, 
                        bAllowTypeMod = True,
                        bAllowClothing = True,
                        bAllowNation = True, 
                        bAllowProf = True, 
                        bAllowSpecies = True,
                        SelectTemplateID = 0,
                        MaxChars = 9999):
        super().__init__()

        if NotList is None:
            NotList = []
          
        self.Gender = Gender.Male 
          
        ExclusionList = []
        if not bAllowGenMod:
            ExclusionList.append(GenModMale())
        if not bAllowTypeMod:
            ExclusionList.append(TypeModMale())
        if not bAllowPhysChar:
            ExclusionList.append(PhysCharMale())
        if not bAllowDickChar:
            ExclusionList.append(DickCharMale())
        if not bAllowClothing:
            ExclusionList.append(ClothesMale())
        if not bAllowNation:
            ExclusionList.append(NationMale())
        if not bAllowProf:
            ExclusionList.append(ProfBlueCollarMale())
            ExclusionList.append(ProfWhiteCollarMale())
            ExclusionList.append(ProfFantasyMale())
            ExclusionList.append(ProfAthleteMale())
            ExclusionList.append(ProfRockstarMale())
            ExclusionList.append(ProfNormalMale())
            ExclusionList.append(ProfAspirationalMale())
            ExclusionList.append(ProfMale())
        if not bAllowSpecies:
            ExclusionList.append(SpeciesMale())
          
        
        TemplateList = []
        for subclass in MaleGangSingularTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)
        for subclass in MaleGangPluralTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)
        for subclass in MaleGangAnyTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        SelectionList = self.BuildTemplateList(MaleCharType)
        self.SetCharDesc(TemplateList = TemplateList,  
                         SelectionList = SelectionList,
                         ReqList = ReqList,
                         ExclList = ExclList, 
                         TempType = TempType,
                         NotList = NotList, 
                         bAddEndNoun = bAddEndNoun,
                         bAddTheArticle = bAddTheArticle,
                         bAddAnArticle = bAddAnArticle,
                         sPosArticle = sPosArticle,
                         bSplitArticle = bSplitArticle,
                         SelectTemplateID = SelectTemplateID,
                         MaxChars = MaxChars)

    def BuildTemplateList(self, malechartype):
        SelectionList = []
          
        if malechartype == MaleCharType.GangSingular or malechartype == MaleCharType.GangAny:
            #SelectionList.append(MaleGangSingularTemplate())
            for subclass in MaleGangSingularTemplate.__subclasses__():
                template = subclass()
                SelectionList.append(template)
        if malechartype == MaleCharType.GangPlural or malechartype == MaleCharType.GangAny:
            #SelectionList.append(MaleGangPluralTemplate())
            for subclass in MaleGangPluralTemplate.__subclasses__():
                template = subclass()
                SelectionList.append(template)
        if malechartype == MaleCharType.GangAny:
            #SelectionList.append(MaleGangAnyTemplate())
            for subclass in MaleGangAnyTemplate.__subclasses__():
                template = subclass()
                SelectionList.append(template)

        if len(SelectionList) == 0:
            print("=*= WARNING =*= GangMaleChar() template list is empty")
              
        return SelectionList
          
class GayMaleChar(Character):
    def __init__(self, ReqList = [], ExclList = [],
                        TempType = TempType.Flowery,
                        NotList = None, 
                        bAddTheArticle = False, 
                        bAddAnArticle = False,
                        sPosArticle = "My", 
                        bAddEndNoun = True,  
                        bSplitArticle = False,
                        bAllowPhysChar = True, 
                        bAllowDickChar = True, 
                        bAllowGenMod = True, 
                        bAllowTypeMod = True,
                        bAllowClothing = True,
                        bAllowNation = True, 
                        bAllowProf = True, 
                        bAllowTitle = False,
                        bAllowSpecies = True,
                        SelectTemplateID = 0,
                        MaxChars = 9999):
        super().__init__()

        if NotList is None:
            NotList = []
          
        self.Gender = Gender.Male 
          
        ExclusionList = []
        if not bAllowGenMod:
            ExclusionList.append(GenModMale())
        if not bAllowTypeMod:
            ExclusionList.append(TypeModMale())
        if not bAllowPhysChar:
            ExclusionList.append(PhysCharMale())
        if not bAllowDickChar:
            ExclusionList.append(DickCharMale())
        if not bAllowClothing:
            ExclusionList.append(ClothesMale())
        if not bAllowNation:
            ExclusionList.append(NationMale())
        if not bAllowProf:
            ExclusionList.append(ProfBlueCollarMale())
            ExclusionList.append(ProfWhiteCollarMale())
            ExclusionList.append(ProfFantasyMale())
            ExclusionList.append(ProfAthleteMale())
            ExclusionList.append(ProfRockstarMale())
            ExclusionList.append(ProfNormalMale())
            ExclusionList.append(ProfAspirationalMale())
            ExclusionList.append(ProfMale())
        if not bAllowSpecies:
            ExclusionList.append(TitlesMale())
        if not bAllowSpecies:
            ExclusionList.append(SpeciesMale())
          
        TemplateList = []
        for subclass in MaleGayTemplate.__subclasses__():
            template = subclass()
            TemplateList.append(template)

        SelectionList = self.BuildTemplateList(MaleCharType)
        self.SetCharDesc(TemplateList = TemplateList,  
                         SelectionList = SelectionList,
                         ReqList = ReqList,
                         ExclList = ExclList, 
                         TempType = TempType,
                         NotList = NotList, 
                         bAddEndNoun = bAddEndNoun,
                         bAddTheArticle = bAddTheArticle,
                         bAddAnArticle = bAddAnArticle,
                         sPosArticle = sPosArticle,
                         bSplitArticle = bSplitArticle,
                         SelectTemplateID = SelectTemplateID,
                         MaxChars = MaxChars)

    def BuildTemplateList(self, malechartype):
        SelectionList = []
          
        for subclass in MaleGayTemplate.__subclasses__():
            template = subclass()
            i = 0
            while i < template.Priority * 5:
                SelectionList.append(template)
                i = i + 1

        if len(SelectionList) == 0:
            print("=*= WARNING =*= GayMaleChar() template list is empty")
                    
        return SelectionList