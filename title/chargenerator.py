#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import TempType 
from title.chartemplates import *
from util import *
from title.util import TempType
		
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
		
		if SelectTemplateID > 0:
			ExclusionList = []
			
			if isinstance(self.TemplateList, list):
				for item in self.TemplateList:
					SelCharTemplate = item
					if item.ID == SelectTemplateID:
						break
		else:
			SelCharTemplate = choice(TemplateList)
			
			#print("Selected first template is + " + str(SelCharTemplate))
			iTryCounter = 1
			while self.IsTemplateExcluded(SelCharTemplate, ExclusionList):
				SelCharTemplate = choice(TemplateList)
				iTryCounter = iTryCounter + 1
				#print("==<<COLLISION!! Template had an excluded type! New selected template is + " + str(SelCharTemplate) + ">>==")

			print("Template selected, it took " + str(iTryCounter) + " tries.\n")
		
		variant = None 
		if TempType == TempType.Short:
			variant = SelCharTemplate.GetShortVariant()
		elif TempType == TempType.Medium:
			variant = SelCharTemplate.GetMediumVariant()
		else:
			variant = SelCharTemplate.GetFloweryVariant()

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
		
	def BuildTemplateList(self, bAllowTrope, bAllowSpecies):
		TemplateList = []
		
		for subclass in FemCharTemplate.__subclasses__():
			template = subclass()
			if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
				TemplateList.append(template)
	
		if bAllowTrope:
			for subclass in FemTropeTemplate.__subclasses__():
				template = subclass()
				if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
					TemplateList.append(template)
	
		if bAllowSpecies:
			for subclass in FemSpeciesTemplate.__subclasses__():
				template = subclass()
				if self.GirlType == GirlType.Neutral or template.GirlType == self.GirlType:
					TemplateList.append(template)
		
		return TemplateList


class MaleChar(Character):
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
			ExclusionList.append(ClothingMale())
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
		
		if SelectTemplateID > 0:
			ExclusionList = []
			
			if isinstance(self.TemplateList, list):
				for item in self.TemplateList:
					SelCharTemplate = item
					if item.ID == SelectTemplateID:
						break
		else:
			SelCharTemplate = choice(TemplateList)
			
			#print("Selected first template is + " + str(SelCharTemplate))
			iTryCounter = 1
			while self.IsTemplateExcluded(SelCharTemplate, ExclusionList):
				SelCharTemplate = choice(TemplateList)
				iTryCounter = iTryCounter + 1
				#print("==<<COLLISION!! Template had an excluded type! New selected template is + " + str(SelCharTemplate) + ">>==")

			print("Template selected, it took " + str(iTryCounter) + " tries.\n")
		
		variant = None 
		if TempType == TempType.Short:
			variant = SelCharTemplate.GetShortVariant()
		elif TempType == TempType.Medium:
			variant = SelCharTemplate.GetMediumVariant()
		else:
			variant = SelCharTemplate.GetFloweryVariant()

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

	def BuildTemplateList(self, bAllowTrope, bAllowSpecies):
		TemplateList = []
		
		for subclass in MaleCharTemplate.__subclasses__():
			TemplateList.append(subclass())
		
		if bAllowTrope:
			for subclass in MaleTropeTemplate.__subclasses__():
				TemplateList.append(subclass())
			
		if bAllowSpecies:
			for subclass in MaleSpeciesTemplate.__subclasses__():
				TemplateList.append(subclass())
			
		return TemplateList
