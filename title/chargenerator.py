#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import TempType 
from title.chartemplates import *
from util import *
from title.util import TempType
from title.util import MaleCharType 
		
class FemaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
					   Type = GirlType.Neutral, 
					   NotList = None, 
					   bAddTheArticle = False, 
					   bAddAnArticle = False,
					   sPosArticle = "My", 
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
					   SelectTemplateID = 0):
		super().__init__()
		
		#print("CharGenerator.FemaleChar() started")
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		self.GirlType = Type
		
		# add any CharBits that we are going to exclude to the exclusion list
		ExclusionList = []
		
		if not bAllowAttitude:
			ExclusionList.append(AttitudeFemale())
			ExclusionList.append(AttitudeBadFemale())
			ExclusionList.append(AttitudeGoodFemale())
		if not bAllowPhysChar:
			ExclusionList.append(PhysCharFemale())
		if not bAllowSkinHairColor:
			ExclusionList.append(SkinHairColorFemale())
		if not bAllowGenMod:
			ExclusionList.append(GenModFemale())
		if not bAllowClothing:
			ExclusionList.append(ClothingFemale())
		if not bAllowPregState:
			ExclusionList.append(PregState())
		if not bAllowMaritalStatus:
			ExclusionList.append(MaritalStatusFemale())
		if not bAllowNation:
			ExclusionList.append(NationFemale())
		if not bAllowProf:
			ExclusionList.append(ProfFemale())
			ExclusionList.append(ProfBadFemale())
			ExclusionList.append(ProfGoodFemale())
		if not bAllowSpecies:
			ExclusionList.append(SpeciesFemale())
		if not bAllowSexuality:
			ExclusionList.append(SexualityFemale())
		if not bAllowRelate:
			ExclusionList.append(RelateFemale())	
		if not bAllowTitle:
			ExclusionList.append(TitlesFemale())
			
		#print("ExclusionList is " + str(ExclusionList) + "\n")
		
		#print("CharGenerator.FemaleChar() Getting templates")
		TemplateList = self.BuildTemplateList(bAllowTrope = bAllowTrope, bAllowSpecies = bAllowSpecies)
		
		self.SetCharDesc(TemplateList, ExclusionList, 
						 TempType = TempType,
						 NotList = NotList, 
						 bAddEndNoun = bAddEndNoun,
						 bAddTheArticle = bAddTheArticle,
						 bAddAnArticle = bAddAnArticle,
						 sPosArticle = sPosArticle,
						 SelectTemplateID = SelectTemplateID)
		
	def BuildTemplateList(self, bAllowTrope, bAllowSpecies):
		TemplateList = []
		
		for subclass in FemCharTemplate.__subclasses__():
			template = subclass()
			if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
				i = 0
				while i < template.Priority:
					TemplateList.append(template)
					i = i + 1
	
		if bAllowTrope:
			for subclass in FemTropeTemplate.__subclasses__():
				template = subclass()
				if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
					i = 0
					while i < template.Priority:
						TemplateList.append(template)
						i = i + 1
	
		if bAllowSpecies:
			for subclass in FemSpeciesTemplate.__subclasses__():
				template = subclass()
				if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
					i = 0
					while i < template.Priority:
						TemplateList.append(template)
						i = i + 1
		
		return TemplateList
		
class MaleChar(Character):
	def __init__(self, MaleCharType = MaleCharType.Straight,
					   TempType = TempType.Flowery,
					   NotList = None, 
					   bAddTheArticle = False, 
					   bAddAnArticle = False,
					   sPosArticle = "My", 
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
					   SelectTemplateID = 0):
		super().__init__()
			
		bShowGangChar = self.ShowGangChar(bAllowGang)
		
		if (MaleCharType == MaleCharType.Straight and bShowGangChar and bAddAnArticle) or MaleCharType == MaleCharType.GangSingular:
		# show singular gang character 
			Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType.GangSingular, 
										 NotList = NotList, bAddTheArticle = bAddTheArticle,
										 bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, 
										 bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
										 bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
										 bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
										 bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
										 bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID) 
		elif (MaleCharType == MaleCharType.Straight and bShowGangChar and bAddTheArticle) or MaleCharType == MaleCharType.GangAny:
		# show any gang character 
			Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType.GangAny, 
										 NotList = NotList, bAddTheArticle = bAddTheArticle,
										 bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, 
										 bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
										 bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
										 bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
										 bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
										 bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID) 
		elif MaleCharType == MaleCharType.GangSingular or MaleCharType == MaleCharType.GangPlural:
		# show gang character depending on parameter passed in
			Char = GangMaleChar(TempType = TempType, MaleCharType = MaleCharType, 
										 NotList = NotList, bAddTheArticle = bAddTheArticle,
										 bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, 
										 bAddEndNoun = bAddEndNoun, bAllowPhysChar = bAllowPhysChar, 
										 bAllowDickChar = bAllowDickChar, bAllowGenMod = bAllowGenMod,
										 bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
										 bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
										 bAllowSpecies = bAllowSpecies, SelectTemplateID = SelectTemplateID) 
		else:
		# show a normal straight character
			Char = StraightMaleChar(TempType = TempType, NotList = NotList, bAddTheArticle = bAddTheArticle,
										 bAddAnArticle = bAddAnArticle, sPosArticle = sPosArticle, 
										 bAddEndNoun = bAddEndNoun, bAllowAttitude = bAllowAttitude, 
										 bAllowPhysChar = bAllowPhysChar, bAllowDickChar = bAllowDickChar, 
										 bAllowSkinHairColor = bAllowSkinHairColor, bAllowGenMod = bAllowGenMod,
										 bAllowTypeMod = bAllowTypeMod,bAllowClothing = bAllowClothing,
										 bAllowAge = bAllowAge, bAllowMaritalStatus = bAllowMaritalStatus,
										 bAllowNation = bAllowNation, bAllowProf = bAllowProf, 
										 bAllowSpecies = bAllowSpecies, bAllowTrope = bAllowTrope, 
										 bAllowRelate = bAllowRelate,bAllowTitle = bAllowTitle,
										 SelectTemplateID = SelectTemplateID) 
	
		
		self.Desc = Char.Desc

	def ShowGangChar(self, bAllowGangChar):
		bShowGangChar = False 
		
		if bAllowGangChar:
			if randint(1,4) == 1:
				bShowGangChar = True
		
		return bShowGangChar
			
class StraightMaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
					   NotList = None, 
					   bAddTheArticle = False, 
					   bAddAnArticle = False,
					   sPosArticle = "My", 
					   bAddEndNoun = True,
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
					   SelectTemplateID = 0):
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
		
		TemplateList = self.BuildTemplateList(bAllowTrope = bAllowTrope, bAllowSpecies = bAllowSpecies)
		
		self.SetCharDesc(TemplateList, ExclusionList, 
						 TempType = TempType,
						 NotList = NotList, 
						 bAddEndNoun = bAddEndNoun,
						 bAddTheArticle = bAddTheArticle,
						 bAddAnArticle = bAddAnArticle,
						 sPosArticle = sPosArticle,
						 SelectTemplateID = SelectTemplateID)

	def BuildTemplateList(self, bAllowTrope, bAllowSpecies):
		TemplateList = []
		
		for subclass in MaleCharTemplate.__subclasses__():
			template = subclass()
			i = 0
			while i < template.Priority:
				TemplateList.append(template)
				i = i + 1
		
		if bAllowTrope:
			for subclass in MaleTropeTemplate.__subclasses__():
				template = subclass()
				i = 0
				while i < template.Priority:
					TemplateList.append(template)
					i = i + 1
			
		if bAllowSpecies:
			for subclass in MaleSpeciesTemplate.__subclasses__():
				template = subclass()
				i = 0
				while i < template.Priority:
					TemplateList.append(template)
					i = i + 1
			
		return TemplateList

class GangMaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
					   MaleCharType = MaleCharType.GangAny,
					   NotList = None, 
					   bAddTheArticle = False, 
					   bAddAnArticle = False,
					   sPosArticle = "My", 
					   bAddEndNoun = True,  
					   bAllowPhysChar = True, 
					   bAllowDickChar = True, 
					   bAllowGenMod = True, 
					   bAllowTypeMod = True,
					   bAllowClothing = True,
					   bAllowNation = True, 
					   bAllowProf = True, 
					   bAllowSpecies = True,
					   SelectTemplateID = 0):
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
		
		TemplateList = self.BuildTemplateList(MaleCharType)
		self.SetCharDesc(TemplateList, ExclusionList, 
						 TempType = TempType,
						 NotList = NotList, 
						 bAddEndNoun = bAddEndNoun,
						 bAddTheArticle = bAddTheArticle,
						 bAddAnArticle = bAddAnArticle,
						 sPosArticle = sPosArticle,
						 SelectTemplateID = SelectTemplateID)

	def BuildTemplateList(self, malechartype):
		TemplateList = []
		
		if malechartype == MaleCharType.GangSingular or malechartype == MaleCharType.GangAny:
			TemplateList.append(MaleGangSingularTemplate())
		if malechartype == MaleCharType.GangPlural or malechartype == MaleCharType.GangAny:
			TemplateList.append(MaleGangPluralTemplate())
		if malechartype == MaleCharType.GangAny:
			TemplateList.append(MaleGangAnyTemplate())
				
		return TemplateList