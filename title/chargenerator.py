#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import TempType 
from title.chartemplates import *
from util import *

class FemaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
		Type = GirlType.Neutral, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowClothing = True, bAllowAge = True, 
		bAllowPregState = True, bAllowMaritalStatus = True,	bAllowNation = True, bAllowProf = True, bAllowSpecies = True, 
		bAllowSexuality = True, bAllowTrope = True, bAllowRelate = False, bAllowTitle = True,
		SelectTemplateID = 0):
		super().__init__()
		#print("CharGenerator.FemaleChar() started")
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		#print("CharGenerator.FemaleChar() Getting templates")
		TemplateList = []
		for subclass in FemCharTemplate.__subclasses__():
			template = subclass()
			if Type == GirlType.Neutral or template.GirlType == Type:
				TemplateList.append(template)
			# if template.HasCharBit(charbit = PhysCharFemale):
				# print("FemaleChar().__init__(): Template " + str(template) + " contains PhysCharFemale charbit!")
		
		if bAllowTrope:
			for subclass in FemTropeTemplate.__subclasses__():
				template = subclass()
				
				TemplateList.append(template)
		
		SelCharTemplate	= None		
		#pick a template at random from the list 
		print("SelectTemplateID = " + str(SelectTemplateID))
		if SelectTemplateID > 0:
			for template in TemplateList:
				SelCharTemplate = template
				if template.ID == SelectTemplateID:
					break
					
		else:
			SelCharTemplate = choice(TemplateList)

		print("CharGenerator.FemaleChar() selected random template # " + str(SelCharTemplate.ID) + ", " + str(SelCharTemplate))
			
		bIsRelate = False

		self.Desc = SelCharTemplate.GetDesc(temptype = TempType)
		
		
class FemaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
		Type = GirlType.Neutral, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowClothing = True, bAllowAge = True, 
		bAllowPregState = True, bAllowMaritalStatus = True,	bAllowNation = True, bAllowProf = True, bAllowSpecies = True, 
		bAllowSexuality = True, bAllowTrope = True, bAllowRelate = False, bAllowTitle = True,
		SelectTemplateID = 0):
		super().__init__()
		#print("CharGenerator.FemaleChar() started")
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		#print("CharGenerator.FemaleChar() Getting templates")
		TemplateList = []
		for subclass in FemCharTemplate.__subclasses__():
			template = subclass()
			if Type == GirlType.Neutral or template.GirlType == Type:
				TemplateList.append(template)
			# if template.HasCharBit(charbit = PhysCharFemale):
				# print("FemaleChar().__init__(): Template " + str(template) + " contains PhysCharFemale charbit!")
		
		if bAllowTrope:
			for subclass in FemTropeTemplate.__subclasses__():
				template = subclass()
				
				TemplateList.append(template)
		
		SelCharTemplate	= None		
		#pick a template at random from the list 
		print("SelectTemplateID = " + str(SelectTemplateID))
		if SelectTemplateID > 0:
			for template in TemplateList:
				SelCharTemplate = template
				if template.ID == SelectTemplateID:
					break
					
		else:
			SelCharTemplate = choice(TemplateList)

		print("CharGenerator.FemaleChar() selected random template # " + str(SelCharTemplate.ID) + ", " + str(SelCharTemplate))
			
		bIsRelate = False

		if bAddArticle:
			if SelCharTemplate.IsPersonal:
				self.Desc = sPosArticle + " " + SelCharTemplate.GetDesc(temptype = TempType)
			else:
				self.Desc = AddArticles(SelCharTemplate.GetDesc(temptype = TempType), bMakeUpper = True)
		else:
			self.Desc = SelCharTemplate.GetDesc(temptype = TempType)
		
		

class MaleChar(Character):
	def __init__(self, TempType = TempType.Flowery,
		NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowDickChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowAge = True, bAllowMaritalStatus = True,
		bAllowNation = True, bAllowProf = True, bAllowSpecies = True, bAllowTrope = True, bAllowRelate = False,
		bAllowTitle = True,
		SelectTemplateID = 0):
		super().__init__()
		#print("CharGenerator.FemaleChar() started")
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Male 
		
		#print("CharGenerator.MaleChar() Getting templates")
		TemplateList = []
		for subclass in MaleCharTemplate.__subclasses__():
			template = subclass()
			TemplateList.append(template)
			# if template.HasCharBit(charbit = PhysCharMale):
				# print("MaleChar().__init__(): Template " + str(template) + " contains PhysCharFemale charbit!")
		
		if bAllowTrope:
			for subclass in MaleTropeTemplate.__subclasses__():
				template = subclass()
				
				TemplateList.append(template)
		
		SelCharTemplate	= None		
		#pick a template at random from the list 
		print("SelectTemplateID = " + str(SelectTemplateID))
		if SelectTemplateID > 0:
			for template in TemplateList:
				SelCharTemplate = template
				if template.ID == SelectTemplateID:
					break
					
		else:
			SelCharTemplate = choice(TemplateList)

		print("CharGenerator.MaleChar() selected random template # " + str(SelCharTemplate.ID) + ", " + str(SelCharTemplate))
			
		bIsRelate = False

		if bAddArticle:
			if SelCharTemplate.IsPersonal:
				self.Desc = sPosArticle + " " + SelCharTemplate.GetDesc(temptype = TempType)
			else:
				self.Desc = AddArticles(SelCharTemplate.GetDesc(temptype = TempType), bMakeUpper = True)
		else:
			self.Desc = SelCharTemplate.GetDesc(temptype = TempType)
	