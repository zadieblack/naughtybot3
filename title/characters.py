#!/usr/bin/env python
# -*- coding: utf-8 -*-
# People module

from random import *
from util import *

import title.util as titutil
import title.misc as titmisc
import misc as misc

FemCBitHistoryQ = HistoryQ(10)
MaleCBitHistoryQ = HistoryQ(10)

class TempType(Enum):
	Short = 1
	Medium = 2
	Flowery = 3


class CharBit():
	def __init__(self, charlist, gen = Gender.Neuter):
		self.Gender = gen 
		
		if isinstance(charlist,str):			#initialize with a string
			self._CharList = WordList([charlist])
			#print("CharBit().__init__(): Initialized with a string")
		elif isinstance(charlist,list):			#initialize with a list
			self._CharList = WordList(charlist)
			#print("CharBit().__init__(): Initialized with a List")
		elif isinstance(charlist,WordList):		#initialize with a WordList
			self._CharList = charlist
			#print("CharBit().__init__(): Initialized with a WordList")
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
		
class CharTemplate():
	def __init__(self, id = 0, gen = Gender.Neuter, temptype = TempType.Flowery):
		self._CharBitList = []
		self.Gender = gen 
		self.TempType = temptype 
		self.ID = id
		
	def GetDesc(self):
		sDesc = ""
		#print("GetDesc() description for template " + str(self.ID) + ". _CharBitList is [" + str(self._CharBitList) + "]")
		for item in self._CharBitList:
			print("Getting CharBit() " + str(item))
			if sDesc != "":
				sDesc += " " 
			if isinstance(item, CharBit):
				#print("CharTemplate().GetDesc(): item = " + str(item))
				sDesc += item.Get()
			# else:
				# print("CharTemplate().GetDesc(): item class not CharBit. item is " + str(item))
			
		return sDesc
		
	def HasCharBit(self, charbit):
		bHasCharBit = False 
		charbit = charbit() 
		
		for item in self._CharBitList:
			if item.__class__ == charbit.__class__:
				bHasCharBit = True 
			
		return bHasCharBit
		
class Character():
	def __init__(self, gen = Gender.Neuter):
		self.Gender = gen
		
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

class AttitudeGoodFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.AttitudeGoodFemale(),girltype = GirlType.Good)
		
class AttitudeBadFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.AttitudeBadFemale(),girltype = GirlType.Bad)
		
class MaritalStatusFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.MaritalStatusFemale())
		
class NationFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.NationFemale())
		
class PhysCharFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.PhysCharFemale())
		
class ProfGoodFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.ProfGoodFemale(),girltype = GirlType.Good)
		
class ProfBadFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.ProfBadFemale(),girltype = GirlType.Bad)
		
class MaritalStatusFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.MaritalStatusFemale())
		
class NationFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.NationFemale())
		
class SkinHairColorFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.SkinHairColorFemale())
		
class SpeciesFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.SpeciesFemale())
		
class RelateFemale(FemCharBit):
	def __init__(self):
		super().__init__(titmisc.RelateFemale())
		
class TropeFemale(FemCharBit):
	pass
		
class TropeSmallTownGirl(TropeFemale):
	def __init__(self):
		super().__init__("Small-Town Girl",girltype = GirlType.Good)
		
class TropeAmishMaiden(TropeFemale):
	def __init__(self):
		super().__init__("Amish Maiden",girltype = GirlType.Good)
		
class TropeCatholicSchoolGirl(TropeFemale):
	def __init__(self):
		super().__init__("Catholic Schoolgirl")
		
class TropeSoccerMom(TropeFemale):
	def __init__(self):
		super().__init__("Small-Town Girl",girltype = GirlType.Good)

class TropePregnantStripper(TropeFemale):
	def __init__(self):
		super().__init__("Pregnant Stripper",girltype = GirlType.Bad)

class TropeSorityGirl(TropeFemale):
	def __init__(self):
		super().__init__("Sorority Girl",girltype = GirlType.Bad)

class TropeSexKitten(TropeFemale):
	def __init__(self):
		super().__init__("Sex Kitten",girltype = GirlType.Bad)	

class FemCharTemplate(CharTemplate):
	def __init__(self, charbits = [], id = 0, temptype = TempType.Flowery, girltype = GirlType.Neutral):
		super().__init__(id = id, temptype = temptype, gen = Gender.Female)
		
		self.GirlType = girltype 
		for item in charbits:
			self._CharBitList.append(item()) 
			
		self.GirlType = girltype
		
class FemTemplate1(FemCharTemplate):
	def __init__(self):
		super().__init__([AttitudeGoodFemale,
						PhysCharFemale,
						ProfGoodFemale
						], id = 1, temptype = TempType.Flowery,girltype = GirlType.Good)

class FemTemplate2(FemCharTemplate):
	def __init__(self):
		super().__init__([AttitudeBadFemale,
						PhysCharFemale,
						ProfBadFemale
						], id = 2, temptype = TempType.Flowery,girltype = GirlType.Bad)
						
class FemTemplate3(FemCharTemplate):
	def __init__(self):
		super().__init__([PhysCharFemale,
						SkinHairColorFemale,
						ProfGoodFemale
						], id = 3, temptype = TempType.Flowery,girltype = GirlType.Good)
									

									
class FemTemplate4(FemCharTemplate):
	def __init__(self):
		super().__init__([AttitudeGoodFemale,
						 PhysCharFemale,
						 SkinHairColorFemale,
						 TropeAmishMaiden
						], id = 4, temptype = TempType.Flowery,girltype = GirlType.Good)

class FemTemplate5(FemCharTemplate):
	def __init__(self):
		super().__init__([AttitudeBadFemale,
						 PhysCharFemale,
						 TropePregnantStripper
						], id = 5, temptype = TempType.Flowery,girltype = GirlType.Good)		

class FemTemplate6(FemCharTemplate):
	def __init__(self):
		super().__init__([AttitudeBadFemale,
						 NationFemale,
						 TropePregnantStripper
						], id = 6, temptype = TempType.Flowery,girltype = GirlType.Good)							
								
		
class FemaleChar(Character):
	def __init__(self, Type = GirlType.Neutral, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowClothing = True, bAllowAge = True, 
		bAllowPregState = True, bAllowMaritalStatus = True,	bAllowNation = True, bAllowProf = True, bAllowSpecies = True, 
		bAllowSexuality = True, bAllowTrope = True, bAllowRelate = False, bAllowTitle = True):
		super().__init__()
		print("Initializing FemaleChar()")
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		print("Getting templates")
		TemplateList = []
		for subclass in FemCharTemplate.__subclasses__():
			template = subclass()
			if template.Gender == Gender.Female or template.Gender == Gender.Neutral:
				if Type == GirlType.Neutral or template.GirlType == Type:
					TemplateList.append([template.ID, template])
			# if template.HasCharBit(charbit = PhysCharFemale):
				# print("FemaleChar().__init__(): Template " + str(template) + " contains PhysCharFemale charbit!")
				
		#pick a template at random from the list 
		print(str(len(TemplateList)) + " templates found")
		SelCharTemplate = TemplateList[randint(0,len(TemplateList) - 1)][1]
		print("Selected random template: " + str(SelCharTemplate))
			
		bIsRelate = False

		self.Desc = SelCharTemplate.GetDesc()
	