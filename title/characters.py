#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Characters module

from random import *
from util import *
from title.util import TempType
import re

import title.util as titutil
import title.misc as titmisc
import misc as misc

MAX_CHARACTER_CHARBITS = 4
MAX_VARIANT_TRIES = 200

FemCBitHistoryQ = HistoryQ(10)
MaleCBitHistoryQ = HistoryQ(10)




class CharBit():
     def __init__(self, charlist, gen = Gender.Neuter):
          self.Gender = gen 
          
          if isinstance(charlist,str):               #initialize with a string
               self._CharList = WordList([charlist])
          elif isinstance(charlist,list):               #initialize with a list
               self._CharList = WordList(charlist)
          elif isinstance(charlist,WordList):          #initialize with a WordList
               self._CharList = charlist
          else:                                             #shrug
               self._CharList = WordList([])

          self._IsNoun = False 
          
     def IsNoun(self):
          return self._IsNoun
          
     def SetNoun(self):
          self._IsNoun = True 
          
     def HasCharBit(self, target):
          bHasCharBit = False 
          
          if isinstance(target, list):
               for item in target:
                    if self.__class__ == item:
                         bHasCharBit = True 
          else:
               if self.__class__ == target:
                    bHasCharBit = True 
               
          return bHasCharBit
          
     def Get(self, NotList = None):
          sResult = ""
          if NotList is None:
               NotList = []
               
          if isinstance(self._CharList, WordList):
               if self._CharList.Length() > 1:
                    sResult = self._CharList.GetWord(NotList = NotList)
               else:
                    if self._CharList.GetWordList()[0] not in NotList:
                         sResult = self._CharList.GetWordList()[0]

          return sResult

class CTEntry():
     def __init__(self, charbits, orderno):
          if isinstance(charbits, list):
               self.CharBits = WordList()
               for item in charbits:
                    if isinstance(item, CharBit):
                         self.CharBits.AddWord(item)
                    else:
                         self.CharBits.AddWord(item())
          elif isinstance(charbits, CharBit):
               self.CharBits = WordList([charbits])
          else:
               self.CharBits = WordList([])

          if isinstance(orderno, (int)):
               self.OrderNo = orderno 
          else:
               self.OrderNo = 0
               
     def PickOne(self, NotList = None):
          if NotList is None:
               NotList = []
               
          return self.CharBits.GetWord(NotList = NotList)
          
     def HasCharBit(self, charbit):
          bHasCharBit = False 
          
          if self.CharBits is not None and isinstance(self.CharBits, WordList):
               for item in self.CharBits.GetWordList():
                    if charbit.__class__ == item.__class__:
                         bHasCharBit = True
                         break
                         
          return bHasCharBit
     
#MAX_CHARACTER_CHARBITS = 5
class CharTemplate():
    def entry_key(self,entry):
        return entry.OrderNo
          
    def __init__(self, noun = None, 
                id = 0, 
                adjlist = [], 
                gen = Gender.Neuter, 
                priority = 1, 
                bpersonal = False,
                NotList = None):

        if noun is None:
            noun = CharBit("")
        if NotList is None:
            NotList = []
               
        self.Gender = gen 
        self.ID = id
        self.Priority = priority
        self.NotList = NotList
        self.RequestOnly = False
          
        noun.SetNoun()
        self.Noun = noun
          
        #adjlist.sort(key = self.entry_key)
        self._AdjList = []
        i = 0
        while i < len(adjlist):
            adjlist[i].priority = i
            self._AdjList.append(adjlist[i])
            i = i + 1
          
        #self._AdjList = adjlist 
          
        if bpersonal:
            self.IsPersonal = True
        else:
            self.IsPersonal = False 
     
    def GetShortVariant(self):
        variant = []
        variant.append(self.Noun)
        return variant
               
    def GetMediumVariant(self):
        variant = []
        if isinstance(self._AdjList, list):
            if len(self._AdjList) > 1:
                variant.append(self.Noun)
                variant.append(choice(self._AdjList).PickOne(NotList = self.NotList))
                    
            else:
                variant.append(self.GetShortVariant())
                    
        variant.reverse()
          
        return variant
               
    def GetFloweryVariant(self):
        variant = []
        if isinstance(self._AdjList, list):
            if len(self._AdjList) > 2:
                iMaxCharbits = MAX_CHARACTER_CHARBITS - 1               #get the max allowed charbits in one description string
                if len(self._AdjList) < MAX_CHARACTER_CHARBITS:
                        iMaxCharbits = len(self._AdjList) - 1
                #print("CharTemplate.GetFloweryVariant() iMaxCharbits = " + str(iMaxCharbits))
                    
                iTotal = randint(2,iMaxCharbits)                         #pick a number >= the max but > short or medium variants 
                #print("CharTemplate.GetFloweryVariant() iTotal = " + str(iTotal))

                                                                                    #get a random selection from the adjectives list,sort
                selections = sorted(sample(self._AdjList, k = iTotal), key = self.entry_key, reverse = True)
                    
                for item in selections:                                        #append to variant, selecting one option at random if there are 
                        variant.append(item.PickOne(NotList = self.NotList))     #  multiple options for the same order #
                variant.append(self.Noun)                                   #get the noun
            else:
                variant = self.GetMediumVariant()
          
        return variant
               
    def GetDesc(self, temptype = TempType.Flowery):
        sDesc = ""
        variant = None

        if temptype == TempType.Short:
            variant = self.GetShortVariant()
        elif temptype == TempType.Medium:
            variant = self.GetMediumVariant()
        else:
            variant = self.GetFloweryVariant()
          
        sNoun = variant[len(variant) - 1].Get(NotList = self.NotList)
        self.NotList.append(re.findall(r"[\w']+", sNoun))
        for charbit in variant[:-1]:
            #print("CharTemplate.GetDesc() charbit is " + str(charbit))
            if sDesc != "":
                sDesc += " "
            sAdj = charbit.Get(NotList = self.NotList)
            for s in re.findall(r"[\w']+",sAdj):
                self.NotList.append(s)
            sDesc += sAdj
        if sDesc != "":
            sDesc += " " 
        sDesc += sNoun 
               
        #print("Final NotList is " + str(self.NotList))
        return sDesc
          
    def HasCharBit(self, charbits):
        bHasCharBit = False 
          
        if isinstance(charbits, CharBit):
            charbits = [charbit()]

        if isinstance(charbits, list):
            for checkitem in charbits:
                checknoun = None
                if isinstance(self.Noun, CTEntry):
                        checknoun = self.Noun.CharBit 
                else:
                        checknoun = self.Noun 
                #print("CharTemplate: Checking excluded class \"" + str(checkitem.__class__) + "\" against template Noun, \"" + str(checknoun.__class__) + "\"\n")
                if checkitem.__class__ == checknoun.__class__:
                        bHasCharBit = True 
                        #print("==<< CharTemplate: Excluded noun match found! >>==\n")
                        break 
                for myitem in self._AdjList:
                        #print("CharTemplate: Checking excluded class \"" + str(checkitem.__class__) + "\" against adj, \"" + str(myitem.__class__) + "\"")
                        if myitem.HasCharBit(checkitem):
                            bHasCharBit = True 
                            #print("==<< CharTemplate: Excluded adjective match found! >>==\n")
                            break
        #print("CharTemplate returning " + str(bHasCharBit))
        return bHasCharBit

class FemCharTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1,  
                            bpersonal = False,
                            girltype = GirlType.Neutral,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, gen = Gender.Female, priority = priority, bpersonal = bpersonal, NotList = NotList)

          self.GirlType = girltype
          
class FemTropeTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            girltype = GirlType.Neutral,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)
          
          self.GirlType = girltype

class FemSpeciesTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            girltype = GirlType.Neutral,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)
          
          self.GirlType = girltype

class FemLesbianTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            girltype = GirlType.Neutral,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)
          
          self.GirlType = girltype

class MaleCharTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, gen = Gender.Male, priority = priority, bpersonal = bpersonal, NotList = NotList)

class MaleTropeTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)

class MaleSpeciesTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)

class MaleGangTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)

class MaleGayTemplate(CharTemplate):
     def __init__(self, noun, 
                            id = 0, 
                            adjlist = [], 
                            priority = 1, 
                            bpersonal = False,
                            NotList = None):
          if NotList is None:
               NotList = []
               
          super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, bpersonal = bpersonal, NotList = NotList)

class FemCharBit(CharBit):
     def __init__(self, charlist, girltype = GirlType.Neutral):
          super().__init__(charlist,gen = Gender.Female)
               
          self.GirlType = girltype
          
class MaleCharBit(CharBit):
     def __init__(self, charlist):
          super().__init__(charlist,gen = Gender.Male)


class AgeNounFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AgeFemaleNoun())
          
class AgeAdjFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AgeFemaleAdj())

class AttitudeGoodFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AttitudeGoodFemale(),girltype = GirlType.Good)
               
class AttitudeBadFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AttitudeBadFemale(),girltype = GirlType.Bad)
          
class AttitudeFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AttitudeFemale())
          
class ClothingFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ClothingFemale(),girltype = GirlType.Bad)
          
class GenModFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.GenModFemale(),girltype = GirlType.Bad)
          
class MaritalStatusFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.MaritalStatusFemale())
          
class PhysCharFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.PhysCharFemale())
          
class PregState(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.PregState())
          
class ProfGoodFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfGoodFemale(),girltype = GirlType.Good)
          
class ProfNeutralFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfNeutralFemale(),girltype = GirlType.Bad)
          
class ProfBadFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfBadFemale(),girltype = GirlType.Bad)
          
class ProfVeryBadFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfVeryBadFemale(),girltype = GirlType.Bad)
          
class ProfFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfFemale())
          
class MaritalStatusFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.MaritalStatusFemale())
          
class NationFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.NationFemale())

class RaceFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.RaceFemale())
          
class RelateFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.RelateFemale())
          
class SexualityFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SexualityFemale(),girltype = GirlType.Bad)

class SexualityNounFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SexualityNounFemale(),girltype = GirlType.Bad)

class SkinColorPOCFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorPOCFemale())
          
class SkinColorWhiteFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorWhiteFemale())          
          
class SkinColorFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorFemale())
          
class HairColorWhiteFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.HairColorWhiteFemale())
          
class HairColorPOCFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.HairColorPOCFemale())
          
class HairColorFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.HairColorFemale())
          
class SkinHairColorFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinHairColorFemale())

class GirlFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.GirlFemale())
          
class SpeciesFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.SpeciesFemale())
          
class TitlesFemale(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.TitlesFemale())
          
class TropeBitFemale(FemCharBit):
     def __init__(self, trope, girltype = GirlType.Neutral):
          super().__init__(trope,girltype = girltype)
     
class TropeBitBadFemale(TropeBitFemale):
     def __init__(self, trope):
          super().__init__(trope, girltype = GirlType.Bad)
     
class TropeBitGoodFemale(TropeBitFemale):
     def __init__(self, trope):
          super().__init__(trope, girltype = GirlType.Good)

class LesFemaleAdj(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.LesFemaleAdj())
          
class FirstAdjsNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.FirstAdjsNiceGirl())

class AttitudesNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.AttitudesNiceGirl())

class DiminuitiveNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.DiminuitiveNiceGirl())

class PhysCharAdjsNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.PhysCharAdjsNiceGirl())

class NationHairColorNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.NationHairColorNiceGirl())
          
class NounsNiceGirl(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.NounsNiceGirl())
          
class LesFemaleNoun(FemCharBit):
     def __init__(self):
          super().__init__(titmisc.LesFemaleNoun())

class AgeAdjMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.AgeMaleAdj())

class AttitudeMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.AttitudeMale())
          
class ClothesMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ClothesMale())     

class GenModMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GenModMale())

class MaritalStatusMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.MaritalStatusMale())

class NationMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.NationMale())

class NationNounMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.NationNounMale())
          
class PhysCharMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.PhysCharMale())

class DickCharMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.DickCharMale())

class ProfBlueCollarMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfBlueCollarMale())
 
class ProfEducatorMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfEducatorMale())

class ProfWhiteCollarMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfWhiteCollarMale())
          
class ProfFantasyMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfFantasyMale())
          
class ProfAthleteMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfAthleteMale())
          
class ProfRockstarMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfRockstarMale())
          
class ProfNormalMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfNormalMale())
          
class ProfAspirationalMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfAspirationalMale())
          
class ProfMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.ProfMale())

class RaceMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.RaceMale())
          
class RelateMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.RelateMale())

class HairColorMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.HairColorMale())
          
class SkinColorPOCMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorPOCMale())
          
class SkinColorWhiteMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorWhiteMale())
          
class SkinColorMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinColorMale())

class SkinHairColorMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SkinHairColorMale())

class SpeciesMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SpeciesMale())

class TitlesMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.TitlesMale())          

class TropesWealthyMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.TropesWealthyMale())          

class GangsMaleSingular(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GangsMaleSingular())          

class GangsMalePlural(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GangsMalePlural())          

class GangsMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GangsMale())          
          
class TypeModMale(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.TypeModMale())          

class GayMaleNoun(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GayMaleNoun())          
          
class GayMaleAdj(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.GayMaleAdj())          

class SpaceManColorAdjs(MaleCharBit):
     def __init__(self):
          super().__init__(titmisc.SpaceManColorAdjs())  
          
class TropeBitMale(MaleCharBit):
     pass          

          
class Character():
    def __init__(self):
          
        self.Desc = ""
        self.Gender = Gender.Neuter
        self.TemplateList = []
          
    def GetWordList(self):
     
        return re.findall(r"[\w']+", self.Desc)
          
    def BuildTemplateList(self):
        pass
     
    def GetVariantFromTemplate(self, Template, TempType = None):
        variant = None 

        if TempType is None:
            TemptType = TempType.Short

        if not Template is None:
            if TempType == TempType.Short:
                variant = Template.GetShortVariant()
            elif TempType == TempType.Medium:
                variant = Template.GetMediumVariant()
            else:
                variant = Template.GetFloweryVariant()
               
        return variant 
          
    def IsVariantExcluded(self, variant, exclusionlist):
        bIsVariantExcluded = False 
          
        if isinstance(variant, list) and isinstance(exclusionlist, list):
            if len(exclusionlist) > 0:
                # for item in exclusionlist:
                for varitem in variant:
                        if varitem.HasCharBit(exclusionlist):
                            bIsVariantExcluded = True
                            #print(" - - Found a match for variant item " + str(variant) + " on the excluded list")
                            break 
                        # if bIsVariantExcluded:
                            # break
        #print(" - - - IsVariantExcluded() returning " + str(bIsVariantExcluded))
        return bIsVariantExcluded
          
    def DoesVariantMeetReqs(self, variant, reqlist):
        bDoesVariantMeetReqs = False 
        ReqFoundList = []
          
        if isinstance(variant, list) and isinstance(reqlist, list):
            if len(reqlist) > 0:
                for item in reqlist:
                        for varitem in variant:
                            if varitem.HasCharBit(item):
                                ReqFoundList.append(item)
                                #print(" - - Found a match between required item " + str(item) + " and variant item " + str(varitem))
                                break 
                #print(" - - - DoesVariantMeetReqs() ReqFoundList length = " + str(len(ReqFoundList)) + ", reqlist length = " + str(len(reqlist)))
                if len(ReqFoundList) == len(reqlist):
                        bDoesVariantMeetReqs = True
                              
            else:
                bDoesVariantMeetReqs = True
        #print(" - - - DoesVariantMeetReqs() returning " + str(bDoesVariantMeetReqs))     
        return bDoesVariantMeetReqs
          
    def DescribeTemplateVariant(self, variant, bAddEndNoun, NotList = None):
        sDesc = ""
          
        if NotList is None:
            NotList = []
               
        if isinstance(variant, list):
               
            sNounDesc = ""
            Noun = variant[len(variant) - 1] 
            if bAddEndNoun and isinstance(Noun, CharBit):
                sNounDesc = Noun.Get(NotList = NotList)

                NotList = NotList + (re.findall(r"[\w']+", sNounDesc))

            if len(variant) > 1:     
                for charbit in variant[:-1]:
                        if sDesc != "":
                            sDesc += " "
                        sAdjDesc = charbit.Get(NotList = NotList)
                        for s in re.findall(r"[\w']+",sAdjDesc):
                            NotList.append(s)
                        sDesc += sAdjDesc
            if sDesc != "" and sNounDesc != "":
                sDesc += " " 
            sDesc += sNounDesc 
               
            return sDesc
               
    def SetCharDesc(self, 
                    TemplateList, 
                    SelectionList,
                    ReqList = [],
                    ExclList = [], 
                    TempType = TempType.Flowery,
                    GirlType = GirlType.Neutral,
                    NotList = None, 
                    bAddEndNoun = True, 
                    bAddAnArticle = False, 
                    bAddTheArticle = False, 
                    sPosArticle = "My",
                    bSplitArticle = False,
                    SelectTemplateID = 0,
                    MaxChars = 9999):     
        SelCharTemplate = None 
        variant = None
        iTryCounter = 1
        sDesc = ""

        #print("SetCharDesc()")
          
        if SelectTemplateID > 0:
            # Note: if a specific template ID is requested the exclusion and required lists will be ignored
            #print(" - Getting a template for SelectTemplateID = " + str(SelectTemplateID))
            if isinstance(TemplateList, list):
                for item in TemplateList:
                    SelCharTemplate = item
                    if item.ID == SelectTemplateID:
                        break
                              
                if SelCharTemplate is None and not len(TemplateList) == 0:
                    SelCharTemplate = TemplateList[0]
                #print("  -- Was given SelectTemplateID = " + str(SelectTemplateID) + ", got template #" + str(SelCharTemplate.ID) + " [" + str(SelCharTemplate) + "]")
          
                variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
                    
                while (not self.DoesVariantMeetReqs(variant, ReqList) \
                    or self.IsVariantExcluded(variant, ExclList)) and iTryCounter < MAX_VARIANT_TRIES:
                        iTryCounter = iTryCounter + 1
                         
                        variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
                    
        else:
            #print(" - Getting a template at random.")
            #print(" - ExclList is " + str(ExclList))
            for item in SelectionList:
                for excl in ExclList:    
                    if type(item.Noun) == excl:
                        SelectionList.remove(item)
                        #print("  -- item.Noun [" + str(item.Noun) + "] is the type of excluded charbit [" + str(excl) + "]. Removing")
                        break
                    else:
                        pass
                        #print("  -- item.Noun [" + str(item.Noun) + "] is NOT the type of excluded charbit [" + str(excl) + "]. Doing nothing.")
            
            if len(TemplateList) > 0:
                SelCharTemplate = choice(SelectionList) 

                variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
                sDesc = self.DescribeTemplateVariant(variant, bAddEndNoun = bAddEndNoun, NotList = NotList)

                while ((not self.DoesVariantMeetReqs(variant, ReqList) \
                        or self.IsVariantExcluded(variant, ExclList)) \
                        and iTryCounter < MAX_VARIANT_TRIES) \
                        or len(sDesc) > MaxChars:
                    SelCharTemplate = choice(SelectionList)
                    
                    iTryCounter = iTryCounter + 1
                    
                    variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
                    sDesc = self.DescribeTemplateVariant(variant, bAddEndNoun = bAddEndNoun, NotList = NotList)

            else:
                SelCharTemplate = CharTemplate()
                variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
                sDesc = self.DescribeTemplateVariant(variant, bAddEndNoun = bAddEndNoun, NotList = NotList)
            
            # print("\nRandomly selected character template #" + str(SelCharTemplate.ID) + " [" + str(SelCharTemplate) + "]")
            # print(" - It took " + str(iTryCounter) + " tries.\n")
        NotList = NotList + SelCharTemplate.NotList 

        sDesc = self.DescribeTemplateVariant(variant, bAddEndNoun = bAddEndNoun, NotList = NotList)

        sArticleSplitter = " "
        if bSplitArticle:
            sArticleSplitter = "\n"

        if bAddTheArticle:
            if SelCharTemplate.IsPersonal:
                sDesc = sPosArticle + sArticleSplitter + sDesc
            else:
                sDesc = "The"+ sArticleSplitter + sDesc 
        elif bAddAnArticle:
            if SelCharTemplate.IsPersonal:
                sDesc = sPosArticle + sArticleSplitter + sDesc
            else:
                sDesc = AddArticles(sDesc, bMakeUpper = True, bSplitArticle = bSplitArticle)
          
        self.Desc = sDesc




