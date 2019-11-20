#!/usr/bin/env python
# -*- coding: utf-8 -*-
# People module

from random import *
from title.util import *
from util import *

import title.misc

FemCBitHistoryQ = HistoryQ(10)
MaleCBitHistoryQ = HistoryQ(10)

class CharBit():
	def __init__(self):
		self.val = ""
		self.part = ""
		self.IsRelate = False 

class Character():
	def __init__(self):
		self.Gender = Gender.Neuter
		
class AgeFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if CoinFlip():
			self.val = title.misc.AgeFemaleNoun().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			self.part = "noun"
		else:
			self.val = title.misc.AgeFemaleAdj().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			self.part = "adj"
		return self.val
		
class AttitudeFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = title.misc.AttitudeGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = title.misc.AttitudeBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = title.misc.AttitudeFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class ClothingFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.ClothingFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class GenModFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.GenModFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class MaritalStatusFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.MaritalStatusFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class NationFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.NationFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class PhysCharFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.PhysCharFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class PregState(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.PregState().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class ProfFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = title.misc.ProfGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = title.misc.ProfBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = title.misc.ProfFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			
		self.part = "noun"
		return self.val
		
class RelateFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.RelateFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		
		self.part = "noun"
		self.IsRelate = True
		return self.val

class SexualityFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.SexualityFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class SkinHairColorFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.SkinHairColorFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class SpeciesFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.SpeciesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class TitleFemale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.TitlesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class TropeFemale(CharBit):
	def __init__(self, Type = GirlType.Neutral):
		super().__init__()
		
		self.Type = Type
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		if self.Type == GirlType.Good:
			self.val = title.misc.TropesGoodFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		elif self.Type == GirlType.Bad:
			self.val = title.misc.TropesBadFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		else:
			self.val = title.misc.TropesFemale().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)	
			
		self.part = "noun"
		
		return self.val
		
class LesFemaleAdj(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.LesFemaleAdj().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class LesFemaleNoun(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.LesFemaleNoun().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class ProfLesbian(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.ProfLesbian().GetWord(NotList = NotList, SomeHistoryQ = FemCBitHistoryQ)
			
		self.part = "noun"
		return self.val
		
class FemaleChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, Type = GirlType.Neutral, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowClothing = True, bAllowAge = True, 
		bAllowPregState = True, bAllowMaritalStatus = True,	bAllowNation = True, bAllowProf = True, bAllowSpecies = True, 
		bAllowSexuality = True, bAllowTrope = True, bAllowRelate = False, bAllowTitle = True):
		super().__init__()
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		
		CharBitList = []
		
		if bAllowAttitude:
			CharBitList.append(AttitudeFemale(Type = Type))
			CharBitList.append(AttitudeFemale(Type = Type))
		if bAllowPhysChar:
			CharBitList.append(PhysCharFemale())
			CharBitList.append(PhysCharFemale())
		if bAllowSkinHairColor:
			CharBitList.append(SkinHairColorFemale())
		if Type != GirlType.Good and bAllowGenMod:
			CharBitList.append(GenModFemale())
		if bAllowClothing:
			CharBitList.append(ClothingFemale())
		if bAllowPregState:
			CharBitList.append(PregState())
		if bAllowMaritalStatus:
			CharBitList.append(MaritalStatusFemale())
		if bAllowNation:
			CharBitList.append(NationFemale())
		if bAllowAge:
			CharBitList.append(AgeFemale())
		if bAllowSexuality:
			CharBitList.append(SexualityFemale())
		if bAllowProf: 
			#CharBitList.append(ProfFemale(Type = Type))
			CharBitList.append(ProfFemale(Type = Type))
			CharBitList.append(ProfFemale(Type = Type))
		if bAllowSpecies:
			CharBitList.append(SpeciesFemale())
		if bAllowTrope:
			#CharBitList.append(TropeFemale(Type = Type))
			CharBitList.append(TropeFemale(Type = Type))
			CharBitList.append(TropeFemale(Type = Type))
		if bAllowRelate:
			CharBitList.append(RelateFemale())
		if bAllowTitle:
			CharBitList.append(TitleFemale())
			
		BitGetList = []
		bFoundNoun = False 
		bIsRelate = False
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		iNumCBits = round((irand1 + irand2) / 2) 
			
		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits)):
			sBit = CharBitList[x].Get(NotList = NotList)
			if CharBitList[x].part == "noun":
				bFoundNoun = True 
			if CharBitList[x].IsRelate:
				bIsRelate = True
			NotList.append(sBit)
			BitGetList.append(sBit)
			
		if bAddEndNoun:
			if not bFoundNoun:
				NounList = []
					
				if bAllowProf:
					NounList.append(ProfFemale(Type = Type))
					NounList.append(ProfFemale(Type = Type))
					NounList.append(ProfFemale(Type = Type))
				if bAllowSpecies:
					NounList.append(SpeciesFemale())
				if bAllowTrope:
					NounList.append(TropeFemale(Type = Type))
				if bAllowRelate:
					NounList.append(RelateFemale())
				if bAllowTitle:
					NounList.append(TitleFemale())
					
				BitGetList.append(NounList[randint(0,len(NounList) - 1)].Get(NotList = NotList))
		
		sDesc = ""
		for x in range(0, len(BitGetList)):
			if x > 0:
				sDesc += " "
			sDesc += BitGetList[x]
			
		if bAddArticle:				
			if bIsRelate:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc
				
		self.Desc = sDesc
			
class LesbianChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, Type = GirlType.Neutral, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowClothing = True, bAllowAge = True, 
		bAllowPregState = True, bAllowMaritalStatus = True,	bAllowNation = True, bAllowProf = True, bAllowSpecies = True, 
		bAllowTrope = True, bAllowRelate = False, bAllowTitle = True):
		super().__init__()
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Female 
		
		self.GirlType = Type
		
		CharBitList = []
		
		if bAllowAttitude:
			CharBitList.append(AttitudeFemale(Type = Type))
			CharBitList.append(AttitudeMale())
		if bAllowPhysChar:
			CharBitList.append(PhysCharFemale())
		if bAllowSkinHairColor:
			CharBitList.append(SkinHairColorFemale())
		CharBitList.append(LesFemaleAdj())
		if bAllowClothing:
			CharBitList.append(ClothingFemale())
		if bAllowPregState:
			CharBitList.append(PregState())
		if bAllowMaritalStatus:
			CharBitList.append(MaritalStatusFemale())
		if bAllowNation:
			CharBitList.append(NationFemale())
		if bAllowAge:
			CharBitList.append(AgeFemale())
		if bAllowProf:
			CharBitList.append(ProfLesbian())
		if bAllowSpecies:
			CharBitList.append(SpeciesFemale())
		if bAllowTrope:
			CharBitList.append(TropeFemale(Type = Type))
		if bAllowRelate:
			CharBitList.append(RelateFemale())
		CharBitList.append(LesFemaleNoun())
		if bAllowTitle:
			CharBitList.append(TitleFemale())
		
		BitGetList = []
		bFoundNoun = False 
		bIsRelate = False
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		iNumCBits = round((irand1 + irand2) / 2) 
			
		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits)):
			sBit = CharBitList[x].Get(NotList = NotList)
			if CharBitList[x].part == "noun":
				bFoundNoun = True 
			if CharBitList[x].IsRelate:
				bIsRelate = True
			NotList.append(sBit)
			BitGetList.append(sBit)
			
		if bAddEndNoun:
			if not bFoundNoun:
				BitGetList.append(LesFemaleNoun().Get(NotList = NotList))
		
		sDesc = ""
		for x in range(0, len(BitGetList)):
			if x > 0:
				sDesc += " "
			sDesc += BitGetList[x]
			
		if bAddArticle:				
			if bIsRelate:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc
				
		self.Desc = sDesc
			
class AgeMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.AgeMaleAdj().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "adj"
		
		return self.val
		
class AttitudeMale(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.AttitudeMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class GenModMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.GenModMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class MaritalStatusMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.MaritalStatusMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class NationMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.NationMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		
		self.part = "adj"
		return self.val
		
class PhysCharMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.PhysCharMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class DickCharMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.DickCharMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "adj"
		return self.val

		
class ProfMale(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.ProfMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)

		self.part = "noun"
		return self.val
		
class RelateMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.RelateMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		
		self.part = "noun"
		self.IsRelate = True
		return self.val
		
class SkinHairColorMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.SkinHairColorMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "adj"
		return self.val
		
class SpeciesMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.SpeciesMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class TitleMale(CharBit):
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.TitlesMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
		self.part = "noun"
		return self.val
		
class TropeMale(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.TropesMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
			
		self.part = "noun"
		
		return self.val
		
class GangMale(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.GangsMale().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
			
		self.part = "noun"
		
		return self.val
		
class GayMaleAdj(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.GayMaleAdj().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
			
		self.part = "adj"
		
		return self.val

class GayMaleNoun(CharBit):
	def __init__(self):
		super().__init__()
		
	def Get(self, NotList = None):
		if NotList is None:
			NotList = []
		
		self.val = title.misc.GayMaleNoun().GetWord(NotList = NotList, SomeHistoryQ = MaleCBitHistoryQ)
			
		self.part = "noun"
		
		return self.val
		
class MaleChar():
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, NotList = None, bAllowGang = True, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True,
		bAllowAttitude = True, bAllowPhysChar = True, bAllowDickChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowAge = True, bAllowMaritalStatus = True,
		bAllowNation = True, bAllowProf = True, bAllowSpecies = True, bAllowTrope = True, bAllowRelate = False,
		bAllowTitle = True):
		if NotList is None:
			NotList = []
		
		self.Char = None 
		
		iRand = randint(1, 5)
		if iRand == 5 and bAllowGang == True:
			self.Char = MaleGangChar(iNumMinCBits = iNumMinCBits, iNumMaxCBits = iNumMaxCBits, NotList = NotList, bAddArticle = bAddArticle, sPosArticle = sPosArticle, bAddEndNoun = bAddEndNoun,
				bAllowAttitude = bAllowAttitude, bAllowSkinHairColor = bAllowSkinHairColor,
				bAllowGenMod = bAllowGenMod, bAllowAge = bAllowAge, bAllowDickChar = bAllowDickChar,
				bAllowNation = bAllowNation, bAllowProf = bAllowProf, bAllowSpecies = bAllowSpecies, bAllowTrope = bAllowTrope)
		else:
			self.Char = MaleRegChar(iNumMinCBits = iNumMinCBits, iNumMaxCBits = iNumMaxCBits, NotList = NotList, bAddArticle = bAddArticle, sPosArticle = sPosArticle, bAddEndNoun = bAddEndNoun,
				bAllowAttitude = bAllowAttitude, bAllowPhysChar = bAllowPhysChar, bAllowDickChar = bAllowDickChar, bAllowSkinHairColor = bAllowSkinHairColor,
				bAllowGenMod = bAllowGenMod, bAllowAge = bAllowAge, bAllowMaritalStatus = bAllowMaritalStatus, 
				bAllowNation = bAllowNation, bAllowProf = bAllowProf, bAllowSpecies = bAllowSpecies, bAllowTrope = bAllowTrope,
				bAllowRelate = bAllowRelate, bAllowTitle = bAllowTitle)
			
		self.Desc = self.Char.Desc
		
class MaleRegChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True, 
		bAllowAttitude = True, bAllowPhysChar = True, bAllowDickChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowAge = True, bAllowMaritalStatus = True,
		bAllowNation = True, bAllowProf = True, bAllowSpecies = True, bAllowTrope = True, bAllowRelate = False,
		bAllowTitle = True):
		super().__init__()
		sDesc = ""
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Male 
		
		CharBitList = []
		
		if bAllowAttitude:
			CharBitList.append(AttitudeMale())
			CharBitList.append(AttitudeMale())
		if bAllowPhysChar:
			CharBitList.append(PhysCharMale())
			CharBitList.append(PhysCharMale())
		if bAllowDickChar:
			CharBitList.append(DickCharMale())
		if bAllowSkinHairColor:
			CharBitList.append(SkinHairColorMale())
		if bAllowGenMod:
			CharBitList.append(GenModMale())
		if bAllowAge:
			CharBitList.append(AgeMale())
		if bAllowMaritalStatus:
			CharBitList.append(MaritalStatusMale())
		if bAllowNation:
			CharBitList.append(NationMale())
		if bAllowProf:
			CharBitList.append(ProfMale())
			CharBitList.append(ProfMale())
		if bAllowSpecies:
			CharBitList.append(SpeciesMale())
		if bAllowTrope:
			CharBitList.append(TropeMale())
		if bAllowRelate:
			CharBitList.append(RelateMale())
		if bAllowTitle:
			CharBitList.append(TitleMale())
			
		BitGetList = []
		bFoundNoun = False 
		bIsRelate = False 
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		iNumCBits = round((irand1 + irand2) / 2) 

		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits)):
			sBit = CharBitList[x].Get(NotList = NotList)
			if CharBitList[x].part == "noun":
				bFoundNoun = True 
			if CharBitList[x].IsRelate:
				bIsRelate = True
			NotList.append(sBit)
			BitGetList.append(sBit)
			
		if bAddEndNoun:
			if not bFoundNoun:
				if bAddEndNoun:
					NounList = []
					
					if bAllowProf:
						NounList.append([ProfMale(), False])
						NounList.append([ProfMale(), False])
						NounList.append([ProfMale(), False])
					if bAllowSpecies:
						NounList.append([SpeciesMale(), False])
					if bAllowTrope:
						NounList.append([TropeMale(), False])
					if bAllowRelate:
						NounList.append([RelateMale(), True])
					if bAllowTitle:
						NounList.append([TitleMale(), False])
						
					Noun = NounList[randint(0,len(NounList) - 1)]
					if Noun[1]:
						bIsRelate = True
						
					BitGetList.append(Noun[0].Get(NotList = NotList))
		
		sDesc = ""
		for x in range(0, len(BitGetList)):
			if x > 0:
				sDesc += " "
			sDesc += BitGetList[x]
			
		if bAddArticle:				
			if bIsRelate:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc
			
		self.Desc = sDesc
			
class MaleGangChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True, 
		bAllowAttitude = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowAge = True, bAllowDickChar = True,
		bAllowNation = True, bAllowProf = True, bAllowSpecies = True, bAllowTrope = True):
		super().__init__()
		
		sDesc = ""
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Male 
		
		CharBitList = []
		
		if bAllowAttitude:
			CharBitList.append(AttitudeMale())
			CharBitList.append(AttitudeMale())
		if bAllowSkinHairColor:
			CharBitList.append(SkinHairColorMale())
		if bAllowGenMod:
			CharBitList.append(GenModMale())
		if bAllowAge:
			CharBitList.append(AgeMale())
		if bAllowDickChar:
			CharBitList.append(DickCharMale())
		if bAllowNation:
			CharBitList.append(NationMale())
		if bAllowProf:
			CharBitList.append(ProfMale())
			CharBitList.append(ProfMale())
		if bAllowTrope:
			CharBitList.append(TropeMale())
		if bAllowSpecies:
			CharBitList.append(SpeciesMale())
			
		BitGetList = []
		bFoundNoun = False 
		bIsRelate = False 
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		iNumCBits = round((irand1 + irand2) / 2) 
			
		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits - 1)):
			sBit = CharBitList[x].Get(NotList = NotList)

			NotList.append(sBit)
			BitGetList.append(sBit)
			if CharBitList[x].IsRelate:
				bIsRelate = True
		
		for x in range(0, len(BitGetList)):
			if x > 0:
				sDesc += " "
			sDesc += BitGetList[x]
		
		if bAddEndNoun:
			if sDesc != "":
				sDesc += " "
			sDesc += GangMale().Get(NotList = NotList)
		
		if bAddArticle:				
			if bIsRelate:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc
		
		self.Desc = sDesc
		
class GayChar(Character):
	def __init__(self, iNumMinCBits = 1, iNumMaxCBits = 3, NotList = None, bAddArticle = False, sPosArticle = "My", bAddEndNoun = True, 
		bAllowAttitude = True, bAllowPhysChar = True, bAllowSkinHairColor = True, bAllowGenMod = True, bAllowAge = True, bAllowMaritalStatus = True,
		bAllowNation = True, bAllowProf = True, bAllowSpecies = True, bAllowTrope = True, bAllowRelate = True,
		bAllowTitle = True):
		super().__init__()
		sDesc = ""
		
		if NotList is None:
			NotList = []
		
		self.Gender = Gender.Male 
		
		CharBitList = []
		
		if bAllowAttitude:
			CharBitList.append(AttitudeMale())
		if bAllowPhysChar:
			CharBitList.append(PhysCharMale())
		if bAllowSkinHairColor:
			CharBitList.append(SkinHairColorMale())
		if bAllowGenMod:
			CharBitList.append(GenModMale())
		CharBitList.append(GayMaleAdj())
		if bAllowAge:
			CharBitList.append(AgeMale())
		if bAllowMaritalStatus:
			CharBitList.append(MaritalStatusMale())
		if bAllowNation:
			CharBitList.append(NationMale())
		if bAllowProf:
			CharBitList.append(ProfMale())
			CharBitList.append(ProfMale())
		if bAllowSpecies:
			CharBitList.append(SpeciesMale())
		if bAllowTrope:
			CharBitList.append(TropeMale())
		if bAllowRelate:
			CharBitList.append(RelateMale())
		CharBitList.append(GayMaleNoun())
		if bAllowTitle:
			CharBitList.append(TitleMale())
		
		BitGetList = []
		bFoundNoun = False 
		bIsRelate = True
		iNumCBits = 1
		
		irand1 = randint(iNumMinCBits, iNumMaxCBits)
		irand2 = randint(iNumMinCBits, iNumMaxCBits)
		
		iNumCBits = round((irand1 + irand2) / 2) 

		for x in sorted(sample(range(0, len(CharBitList)), iNumCBits)):
			sBit = CharBitList[x].Get(NotList = NotList)
			if CharBitList[x].part == "noun":
				bFoundNoun = True 
			if CharBitList[x].IsRelate:
				bIsRelate = True
			NotList.append(sBit)
			BitGetList.append(sBit)
		
		if bAddEndNoun:		
			if not bFoundNoun:
				BitGetList.append(GayMaleNoun().Get(NotList = NotList))
		
		sDesc = ""
		for x in range(0, len(BitGetList)):
			if x > 0:
				sDesc += " "
			sDesc += BitGetList[x]
			
		if bAddArticle:
			Relations = ["dad","brother","husband","boyfriend", "father", "fiancé", "boss", "lover"]
			bFoundIn = False
			for x in range(0, len(Relations)):
				if Relations[x] in sDesc.lower():
					bFoundIn = True
					break 
					
			if bFoundIn:
				sDesc = sPosArticle + " " + sDesc
			else:
				sDesc = "The " + sDesc
			
		self.Desc = sDesc

class Person(WordList):
	def GetPerson(self, NotList = None):
		if NotList is None:
			NotList = []
			
		sPerson = ""
		
		sPerson = self.GetWord(NotList)
		
		return sPerson
		
class MaleSO(Person):
	def __init__(self):
		super().__init__(['boyfriend','boyfriend',
			'fiancé',
			'hubby',
			'husband'])
			
class FemaleSO(Person):
	def __init__(self):
		super().__init__(['bride',
			'girlfriend','girlfriend',
			'fiancé',
			'wife'])
		
class FemaleFWB(Person):
	def __init__(self):
		super().__init__(['aunt',
		'babysitter',
		'barista',
		'boss',
		'boss\'s wife',
		'CEO',
		'co-ed student',
		'hot cousin',
		'cute roommate',
		'dad\'s girlfriend',
		'daughter',
		'daughter\'s best friend',
		'daughter-in-law',
		'dominatrix',
		'eighth-grade teacher',
		'English teacher',
		'ex',
		'fashion model',
		'flight attendant',
		'French maid',
		'girlfriend',
		'girlfriend\'s mom',
		'girlfriend\'s sister',
		'guidance counselor',
		'hot best friend',
		'intern',
		'land lady',
		'librarian',
		'English lit student',
		'maid',
		'math teacher',
		'marriage counselor',
		'masseuse',
		'math tutor',
		'mom\'s best friend',
		'mother-in-law',
		'next-door neighbor',
		'niece',
		'nurse',
		'parole officer',
		'pastor\'s wife',
		'personal trainer',
		'roommate\'s girlfriend',
		'secretary',
		'sister',
		'sister-in-law',
		'sister\'s hot friend',
		'soccer mom',
		'son\'s principal',
		'step-daughter',
		'step-mom',
		'step-sister',
		'Sunday School teacher',
		'teacher',
		'twin sister',
		'wedding planner',
		'wife',
		'wife\'s Avon Lady',
		'wife\'s pregnancy surrogate'])
		
class MaleFWB(Person):
	def __init__(self):
		super().__init__(['attorney',
			'attractive male masseuse',
			'baby daddy',
			'bank teller',
			'barista',
			'best friend\'s fiancé',
			'billionaire fiancé',
			'bodyguard',
			'boss',
			'boy toy',
			'boyfriend',
			'brother',
			'brother-in-law',
			'celebrity crush',
			'co-worker',
			'contractor',
			'dad\'s best friend',
			'daddy',
			'daddy dom',
			'daughter\'s boyfriend',
			'dentist',
			'dom',
			'driver',
			'drug dealer',
			'ex-boyfriend',
			'father',
			'father-in-law',
			'fiancé',
			'friend-with-benefits',
			'geography teacher',
			'girlfriend',
			'guidance counselor',
			'gynecologist',
			'hubby',
			'husband',
			'landlord',
			'life coach',
			'lifeguard',
			'lord',
			'mailman',
			'manager',
			'master',
			'minister',
			'one true love',
			'pastor',
			'pediatrician',
			'personal trainer',
			'photographer',
			'pizza delivery boy',
			'pool boy',
			'priest',
			'prince',
			'proctologist',
			'professor',
			'psychiatrist',
			'roommate',
			'shift supervisor',
			'sister\'s boyfriend',
			'son-in-law',
			'step-son',
			'tennis coach',
			'twin brother',
			'uber driver',
			'vice-principal',
			'volleyball coach',
			'yoga teacher'])
			
class JobBlueCollar(Person):
	def __init__(self):
		super().__init__(['aluminum can recycler',
		'bag boy',
		'baggage handler',
		'ball boy',
		'bellhop',
		'bus driver',
		'Starbucks barista',
		'beat cop',
		'blogger',
		'bus driver',
		'call center worker',
		'cat box scooper',
		'cattle wrangler',
		'civil servant',
		'club bouncer',
		'Comcast technician',
		'dish washer at Applebee\'s',
		'dog walker',
		'dog groomer',
		'farm hand',
		'farmer',
		'food court worker',
		'freshman in college',
		'fry cook',
		'garbage man',
		'gas station attendant',
		'golf caddy',
		'gym coach',
		'home theater installer',
		'hot dog vendor',
		'high school history teacher',
		'intern',
		'janitor',
		'junk scavenger',
		'lawn maintenance man',
		'living statue',
		'Lyft driver',
		'manager at Arby\'s',
		'masseur',
		'male nurse',
		'mall santa',
		'mechanic',
		'meter maid',
		'office assistant',
		'page boy',
		'paige',
		'painter',
		'peasant',
		'pest control technician',
		'pet store clerk',
		'Pizza Hut delivery guy',
		'plumber',
		'pool boy',
		'porn set fluffer',
		'postal clerk',
		'private in the army',
		'public restroom attendant',
		'rent-a-cop',
		'roadie',
		'roadkill disposal worker',
		'sea man',
		'self-published author',
		'serf',
		'server at Applebee\'s',
		'shift supervisor',
		'short-order cook',
		'stable boy',
		'stand-up comedian',
		'Whole Foods stock boy',
		'taxidermist',
		'third-grade teacher',
		'ticket stub collector',
		'tow-truck driver',
		'tour guide',
		'truck driver',
		'used car salesman',
		'waiter',
		'Wal-Mart greeter',
		'wedding DJ',
		'writer of erotic romances'])
		
class JobWhiteCollar(Person):
	def __init__(self):
		super().__init__(['accountant',
						'actuary',
						'airline pilot',
						'Apple Store genius',
						'architect',
						'astronaut',
						'bank teller',
						'bass guitarist',
						'bee keeper',
						'cakery owner',
						'chiropractor',
						'city councilman',
						'civil engineer',
						'classical violinist',
						'crossword puzzle writer',
						'database developer',
						'dental hygienist'
						'dentist',
						'dive instructor',
						'executive producer',
						'first-chair flautist',
						'funeral director',
						'gynecologist',
						'homicide detective',
						'fashion photographer',
						'flight attendant',
						'house flipper',
						'insurance adjuster',
						'investment banker',
						'IT professional',
						'jet fighter pilot',
						'life coach',
						'middle manager',
						'motivational speaker',
						'network administrator',
						'neurosurgeon',
						'opthamologist',
						'orthodonist',
						'pharmacist',
						'PhD candidate',
						'physician\'s assistant',
						'photographer',
						'plastic surgeon',
						'podiatrist',
						'high school principal',
						'proctologist',
						'project manager',
						'public radio host',
						'published author',
						'radiologist',
						'rancher',
						'realtor',
						'regional manager',
						'romance novelist',
						'sex therapist',
						'sex toy designer',
						'stay-at-home dad',
						'surgeon',
						'tax attorney',
						'tenured professor',
						'therapist',
						'train conductor',
						'urologist',
						'veterinarian',
						'web designer',
						'Wendy\'s franchise owner',
						'yoga teacher',
						'YouTube personality'])
		
class JobWealthyMale(Person):
	def __init__(self):
		super().__init__(['archduke',
		'baron',
		'Bitcoin billionaire',
		'billionaire',
		'celebrity chef',
		'CEO',
		'count',
		'duke',
		'earl',
		'emperor',
		'film mogul',
		'general',
		'king',
		'knight',
		'marquess',
		'marquis',
		'movie star',
		'Nobel Prize winner',
		'Dalai Lama',
		'pope',
		'president',
		'prime minister',
		'prince',
		'pro football quarterback',
		'rock star',
		'senator',
		'shah',
		'sheikh',
		'sheriff',
		'sultan',
		'surgeon general',
		'titan of industry',
		'viscount'])

class JobWealthyFemale(Person): 
	def __init__(self):
		super().__init__(['actress',
		'archduchess',
		'baroness',
		'CEO',
		'contessa',
		'countess',
		'duchess',
		'heiress',
		'empress',
		'fasion designer',
		'first lady',
		'high-born lady',
		'marchioness',
		'mother superior',
		'Nobel Prize winner',
		'porn star',
		'president',
		'princess',
		'prime minister',
		'queen',
		'queen mother',
		'pop star',
		'senator',
		'social media influencer',
		'supermodel',
		'surgeon general',
		'viscountess',
		'wealthy MILF'])