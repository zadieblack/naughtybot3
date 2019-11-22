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
				TemplateList.append([template.ID, template])
			# if template.HasCharBit(charbit = PhysCharFemale):
				# print("FemaleChar().__init__(): Template " + str(template) + " contains PhysCharFemale charbit!")
		
		# if bAllowTrope:
			# for subclass in FemTropeTemplate.__subclasses__():
				# template = subclass()
				# TemplateList.append([template.ID, template])
		
		SelCharTemplate	= None		
		#pick a template at random from the list 
		if SelectTemplateID > 0:
			for template in TemplateList:
				if template[0] == SelectTemplateID:
					SelCharTemplate = template[1]
		else:
			SelCharTemplate = choice(TemplateList)[1]
		#SelCharTemplate = TemplateList[6][1] # testing sex kitten trope
		print("CharGenerator.FemaleChar() selected random template: " + str(SelCharTemplate.ID))
			
		bIsRelate = False

		self.Desc = SelCharTemplate.GetDesc(temptype = TempType)
	