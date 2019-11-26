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

MAX_CHARACTER_CHARBITS = 5

FemCBitHistoryQ = HistoryQ(10)
MaleCBitHistoryQ = HistoryQ(10)




class CharBit():
	def __init__(self, charlist, gen = Gender.Neuter):
		#print("CharBit started")
		self.Gender = gen 
		
		if isinstance(charlist,str):			#initialize with a string
			self._CharList = WordList([charlist])
			#print("CharBit().__init__(): Initialized with a string, \"" + charlist + "\"")
		elif isinstance(charlist,list):			#initialize with a list
			self._CharList = WordList(charlist)
			#print("CharBit().__init__(): Initialized with a List, " + str(charlist))
		elif isinstance(charlist,WordList):		#initialize with a WordList
			self._CharList = charlist
			#print("CharBit().__init__(): Initialized with a WordList, " + str(charlist.GetWordList()))
		else:									#shrug
			self._CharList = WordList([])
			#print("CharBit().__init__(): Initialized with other")
		#print("CharBit()__init__(): _CharList = " + str(self._CharList) + ".")
		self._IsNoun = False 
		
	def IsNoun(self):
		return self._IsNoun
		
	def SetNoun(self):
		self._IsNoun = True 
		
	def HasCharBit(self, exclusionlist):
		bHasCharBit = False 
		#print("CharBit.HasCharBit() started. excludedcarbits: " + str(excludedcharbits))
		if isinstance(exclusionlist, list):
			for item in exclusionlist:
				#print("CharBit: checking self \"" + str(self.__class__) + "\" against \"" + str(item.__class__) + "\"")
				if self.__class__ == item.__class__:
					#print("==<< CharBit Excluded charbit match found! >>==")
					bHasCharBit = True 
					
		return bHasCharBit
		
	def Get(self, NotList = None):
		sResult = ""
		if NotList is None:
			NotList = []
			
		if isinstance(self._CharList, WordList):
			sResult = self._CharList.GetWord(NotList = NotList)
		# else:
			# print("CharBit().Get(): WARNING: _CharList is not a WordList. Type is " + str(self_.CharList))
		
		# print("CharBit().Get(): " + sResult + ".")
		return sResult

class CTEntry():
	def __init__(self, charbits, orderno):
		#print("CTEntry started, order no = " + str(orderno) + ", charbits = " + str(charbits))
		if isinstance(charbits, list):
			self.CharBits = WordList()
			for item in charbits:
				self.CharBits.AddWord(item())
			
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
				#print("CTEntry: Checking excluded item " + str(charbit.__class__) + " against charbit " + str(item.__class__) + ".\n")
				if charbit.__class__ == item.__class__:
					bHasCharBit = True
					#print("==<< CTEntry: Excluded adjective match found! >>==")
					break
					
		return bHasCharBit
	
#MAX_CHARACTER_CHARBITS = 5
class CharTemplate():
	def entry_key(self,entry):
		return entry.OrderNo
		
	def __init__(self, noun, 
					   id = 0, 
					   adjlist = [], 
					   gen = Gender.Neuter, 
					   priority = 1, 
					   bpersonal = False,
					   NotList = None):
		#print("CharTemplate started")
		if NotList is None:
			NotList = []
			
		self.Gender = gen 
		self.ID = id
		self.Priority = priority
		self.NotList = NotList
		
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
		#print("CharTemplate.GetShortVariant() started")
		variant = []
		variant.append(self.Noun)
		return variant
			
	def GetMediumVariant(self):
		#print("CharTemplate.GetMediumVariant() started")
		variant = []
		if isinstance(self._AdjList, list):
			if len(self._AdjList) > 1:
				variant.append(self.Noun)
				variant.append(choice(self._AdjList).PickOne(NotList = self.NotList))
				
			else:
				variant.append(GetShortVariant())
				
		variant.reverse()
		
		return variant
			
	def GetFloweryVariant(self):
		#print("CharTemplate.GetFloweryVariant() started")
		variant = []
		if isinstance(self._AdjList, list):
			if len(self._AdjList) > 2:
				iMaxCharbits = MAX_CHARACTER_CHARBITS - 1			#get the max allowed charbits in one description string
				if len(self._AdjList) < MAX_CHARACTER_CHARBITS:
					iMaxCharbits = len(self._AdjList) - 1
				#print("CharTemplate.GetFloweryVariant() iMaxCharbits = " + str(iMaxCharbits))
				
				iTotal = randint(2,iMaxCharbits)					#pick a number >= the max but > short or medium variants 
				#print("CharTemplate.GetFloweryVariant() iTotal = " + str(iTotal))

																	#get a random selection from the adjectives list,sort
				selections = sorted(sample(self._AdjList, k = iTotal), key = self.entry_key, reverse = True)
				
				for item in selections:								#append to variant, selecting one option at random if there are 
					variant.append(item.PickOne(NotList = self.NotList))	#  multiple options for the same order #
				variant.append(self.Noun)							#get the noun
			else:
				variant = GetMediumVariant()
		
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
		
class ProfBadFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.ProfBadFemale(),girltype = GirlType.Bad)
		
class ProfFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.ProfFemale())
		
class MaritalStatusFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.MaritalStatusFemale())
		
class NationFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.NationFemale())
		
class RelateFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.RelateFemale())
		
class SexualityFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.SexualityFemale(),girltype = GirlType.Bad)

class SexualityNounFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.SexualityNounFemale(),girltype = GirlType.Bad)
		
class SkinHairColorFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.SkinHairColorFemale())
		
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

class RelateMale(MaleCharBit):
	def __init__(self):
		super().__init__(titmisc.RelateMale())

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
		
class TropeBitMale(MaleCharBit):
	pass
		
class Character():
	def __init__(self):
		
		self.Gender = Gender.Neuter
		
	def BuildTemplateList(self):
		pass
	
	def GetVariantFromTemplate(self, Template, TempType):
		variant = None 
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
			for item in exclusionlist:
				for varitem in variant:
					if varitem.HasCharBit(exclusionlist):
						bIsVariantExcluded = True
						break 
				if bIsVariantExcluded:
					break
			
		return bIsVariantExcluded
		
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
			
	def SetCharDesc(self, TemplateList, 
						  ExclusionList, 
						  TempType = TempType.Flowery,
						  GirlType = GirlType.Neutral,
						  NotList = None, 
						  bAddEndNoun = True, 
						  bAddAnArticle = False, 
						  bAddTheArticle = False, 
						  sPosArticle = "My",
					SelectTemplateID = 0):	
		SelCharTemplate = None 
		variant = None
		
		if SelectTemplateID > 0:
			ExclusionList = []
			
			if isinstance(TemplateList, list):
				for item in TemplateList:
					SelCharTemplate = item
					if item.ID == SelectTemplateID:
						break
						
				variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
		else:
			SelCharTemplate = choice(TemplateList)
			
			variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
			#print("Selected first template is + " + str(SelCharTemplate))
			iTryCounter = 1
			#while self.IsTemplateExcluded(SelCharTemplate, ExclusionList):
			while self.IsVariantExcluded(variant, ExclusionList):
				SelCharTemplate = choice(TemplateList)
				
				iTryCounter = iTryCounter + 1
				
				variant = self.GetVariantFromTemplate(SelCharTemplate, TempType)
				#print("==<<COLLISION!! Template had an excluded type! New selected template is + " + str(SelCharTemplate) + ">>==")

			print("Template " + str(SelCharTemplate) + " selected, it took " + str(iTryCounter) + " tries.\n")
			
		NotList = NotList + SelCharTemplate.NotList 

		sDesc = self.DescribeTemplateVariant(variant, bAddEndNoun = bAddEndNoun, NotList = NotList)

		if bAddTheArticle:
			if SelCharTemplate.IsPersonal:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc 
		elif bAddAnArticle:
			if SelCharTemplate.IsPersonal:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = AddArticles(sDesc, bMakeUpper = True)
		
		self.Desc = sDesc

		
