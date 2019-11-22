#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Characters module

from random import *
from util import *

import title.util as titutil
import title.misc as titmisc
import misc as misc

MAX_CHARACTER_CHARBITS = 5

FemCBitHistoryQ = HistoryQ(10)
MaleCBitHistoryQ = HistoryQ(10)

class TempType(Enum):
	Short = 1
	Medium = 2
	Flowery = 3


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
			
	def PickOne(self):
		return self.CharBits.GetWord()
	
#MAX_CHARACTER_CHARBITS = 5
class CharTemplate():
	def entry_key(self,entry):
		return entry.OrderNo
		
	def __init__(self, noun, 
					   id = 0, 
					   adjlist = [], 
					   gen = Gender.Neuter, 
					   priority = 1, 
					   NotList = None):
		#print("CharTemplate started")
		if NotList is None:
			NotList = []
			
		self.Gender = gen 
		self.ID = id
		self.Priority = priority
		self.NotList = NotList
		
		self.Noun = noun
		
		adjlist.sort(key = self.entry_key)
		
		self._AdjList = adjlist 
	
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
				variant.append(choice(self._AdjList).PickOne())
				
			else:
				variant.append(GetShortVariant())
				
		variant.reverse()
		
		return variant
			
	def GetFloweryVariant(self):
		#print("CharTemplate.GetFloweryVariant() started")
		variant = []
		if isinstance(self._AdjList, list):
			if len(self._AdjList) > 2:
				#variant.append(self.Noun)							#get the noun
				#print("CharTemplate.GetFloweryVariant() noun is \"" + str(variant[0]) +"\"")
				iMaxCharbits = MAX_CHARACTER_CHARBITS - 1			#get the max allowed charbits in one description string
				if len(self._AdjList) < MAX_CHARACTER_CHARBITS:
					iMaxCharbits = len(self._AdjList) - 1
				#print("CharTemplate.GetFloweryVariant() iMaxCharbits = " + str(iMaxCharbits))
				
				iTotal = randint(2,iMaxCharbits)					#pick a number >= the max but > short or medium variants 
				#print("CharTemplate.GetFloweryVariant() iTotal = " + str(iTotal))

																	#get a random selection from the adjectives list,sort
				selections = sorted(sample(self._AdjList, k = iTotal), key = self.entry_key, reverse = True)
				
				for item in selections:								#append to variant, selecting one option at random if there are 
					variant.append(item.PickOne())					#  multiple options for the same order #
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
		
		for charbit in variant:
			#print("CharTemplate.GetDesc() charbit is " + str(charbit))
			if sDesc != "":
				sDesc += " "
			sDesc += charbit.Get()
			
		return sDesc
		
	def HasCharBit(self, charbit):
		bHasCharBit = False 
		charbit = charbit() 
		
		for item in self._CharBitList:
			if item.__class__ == charbit.__class__:
				bHasCharBit = True 
			
		return bHasCharBit
		
class FemCharTemplate(CharTemplate):
	def __init__(self, noun, 
					   id = 0, 
					   adjlist = [], 
					   priority = 1, 
					   girltype = GirlType.Neutral,
					   NotList = None):
		if NotList is None:
			NotList = []
			
		super().__init__(noun = noun, id = id,  adjlist = adjlist, gen = Gender.Female, priority = priority, NotList = NotList)

		self.GirlType = girltype
		
class FemTropeTemplate(CharTemplate):
	def __init__(self, noun, 
					   id = 0, 
					   adjlist = [], 
					   priority = 1, 
					   girltype = GirlType.Neutral,
					   NotList = None):
		if NotList is None:
			NotList = []
			
		super().__init__(noun = noun, id = id,  adjlist = adjlist, priority = priority, NotList = NotList)
		
		self.GirlType = girltype

				
class FemCharBit(CharBit):
	def __init__(self, charlist, girltype = GirlType.Neutral):
		super().__init__(charlist,gen = Gender.Female)
			
		self.GirlType = girltype

class AgeNounFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.AgeFemaleNoun())
		
class AgeAdjFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.AgeFemaleAdj())
		
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
		super().__init__(titmisc.AttitudeGoodFemale())
		
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
	
class Character():
	pass
	
		
								
		
