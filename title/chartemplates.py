#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import *
from util import *

# Adj:		AgeAdjFemale, AttitudeGoodFemale, AttitudeBadFemale, AttitudeFemale,
# 			ClothingFemale, GenModFemale, MaritalStatusFemale, NationFemale, PhysCharFemale
#			PregState, SexualityFemale, SkinHairColorFemale
# Nouns: 	AgeNounFemale, ProfGoodFemale, ProfBadFemale, ProfFemale, RelateFemale,TitlesFemale
# Tropes:	TropeAmishMaiden, TropeCatholicSchoolGirl, TropePregnantStripper, TropeSexKitten
#			TropeSoccerMom, TropeSorityGirl	

# Good Female Profession
class FemTemplate1(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfGoodFemale,
							 id = 1, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],6),
										  CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)
		
# Bad Female Profession		
class FemTemplate2(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale,
							 id = 2, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],9),
										  CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)
					
# Good (Pregnant) Female Profession					
class FemTemplate3(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfGoodFemale,
							 id = 3, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([NationFemale, SkinHairColorFemale],3),
										  CTEntry([PregState],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)
				
# Bad (Pregnant) Female Profession				
class FemTemplate4(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale,
							 id = 4, 
							 adjlist = 	[ CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)
						
# Good Female Royalty						
class FemTemplate5(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = TitlesFemale,
							 id = 5, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],6),
										  CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)

# Bad Female Royalty
class FemTemplate6(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = TitlesFemale,
							 id = 7, 
							 adjlist = 	[ CTEntry([AgeAdjFemale],9),
										  CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)

# Good Female Relation					
class FemTemplate8(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = RelateFemale,
							 id = 8, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale, SkinHairColorFemale],2),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good)

# Bad Female Relation 
class FemTemplate9(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun =  RelateFemale,
							 id = 9, 
							 adjlist = 	[ CTEntry([GenModFemale],7),
										  CTEntry([AttitudeBadFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad)

# Female Good Profession + Bad Profession 			
class FemTemplate10(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = ProfBadFemale,
							 id = 10, 
							 adjlist = 	[ CTEntry([GenModFemale],8),
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],3),  
										  CTEntry([SpeciesFemale],2),
										  CTEntry([ProfGoodFemale],1),
										], 
							girltype = GirlType.Bad)

# Good Female of a Certain Age
class FemTemplate11(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale,
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)
			
# Bad Female of a Certain Age 			
class FemTemplate9(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale,
							 id = 9, 
							 adjlist = 	[ CTEntry([GenModFemale],6),
										  CTEntry([AttitudeBadFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([ClothingFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([SexualityFemale],1),  
										], 
							girltype = GirlType.Bad)


# === Good Trope templates ===

# Good Female of a Certain Age
class FemTemplate11(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale,
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)

class FemTemplate12(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = CharBit("Young Lady"),
							 id = 12, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)

# === Bad Trope templates ===

class FemBadTropeTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Sex Kitten"),
							 id = 1, 
							 adjlist = 	[CTEntry([GenModFemale],7),
										  CTEntry([AttitudeBadFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad,
							NotList = ['Christian','Mormon'])		
						
	

			