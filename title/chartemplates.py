#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Character templates module

from title.characters import *
from util import *

# Good Female Profession
class FemTemplate1(FemCharTemplate):
	def __init__(self):
		super().__init__(	noun = ProfGoodFemale(),
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
		super().__init__(	 noun = ProfBadFemale(),
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
		super().__init__(	noun = ProfGoodFemale(),
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
		super().__init__(	 noun = ProfBadFemale(),
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
		super().__init__(	noun = TitlesFemale(),
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
		super().__init__(	 noun = TitlesFemale(),
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
		super().__init__(	noun = RelateFemale(),
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
		super().__init__(	noun =  RelateFemale(),
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
		super().__init__(	 noun = ProfBadFemale(),
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
		super().__init__(	 noun = AgeNounFemale(),
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)
			
# Bad Female of a Certain Age 			
class FemTemplate9(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale(),
							 id = 9, 
							 adjlist = 	[ CTEntry([GenModFemale],6),
										  CTEntry([AttitudeBadFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([ClothingFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([SexualityFemale],1),  
										], 
							girltype = GirlType.Bad)

# Good Female of a Certain Age
class FemTemplate11(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = AgeNounFemale(),
							 id = 11, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),
										], 
							girltype = GirlType.Good)
							
# Bad Female of a Fantasy Species 			
class FemTemplate12(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = SpeciesFemale(),
							 id = 12, 
							 adjlist = 	[ CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([SexualityFemale],2),
										  CTEntry([ProfBadFemale,ProfGoodFemale],1)
										], 
							girltype = GirlType.Bad)

# Good Female of a Fantasy Species
class FemTemplate13(FemCharTemplate):
	def __init__(self):
		super().__init__(	 noun = SpeciesFemale(),
							 id = 13, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([SkinHairColorFemale],4),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["succubus"])
							
# === Good Trope templates ===

class FemGoodTropeTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Amish Maiden"),
							 id = 100, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([SkinHairColorFemale,PregState],2),
										  CTEntry([PregState],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["amish","maiden"])
							
class FemGoodTropeTemplate2(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("BBW"),
							 id = 101, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([ProfGoodFemale],1),  
										  CTEntry([SpeciesFemale],0),
										], 
							girltype = GirlType.Good,
							NotList = ["athletic","bikini","flat-chested","leggy","little","slender","sporty","tight"])
							
class FemGoodTropeTemplate3(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Beauty"),
							 id = 102, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["beauty"])
							
class FemGoodTropeTemplate4(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Beauty Queen"),
							 id = 103, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],3),
										  CTEntry([PhysCharFemale],2),
										  CTEntry([NationFemale,SkinHairColorFemale],1),   
										], 
							girltype = GirlType.Good,
							NotList = ["beauty","queen"])

class FemGoodTropeTemplate5(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Bride"),
							 id = 104, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),   
										], 
							girltype = GirlType.Good)
							
class FemGoodTropeTemplate6(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Catholic School-girl"),
							 id = 105, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["Catholic","school"])
							
class FemGoodTropeTemplate7(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Chaste Nun"),
							 id = 106, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([NationFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["chaste","sexy","bikini","mormon"])
							
class FemGoodTropeTemplate8(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Cheer-Squad Captain"),
							 id = 107, 
							 adjlist = 	[CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["cheer"])
							
class FemGoodTropeTemplate9(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Damsel-in-Distress"),
							 id = 108, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Good,
							NotList = ["damsel"])
							
class FemGoodTropeTemplate10(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Farmer's Daughter"),
							 id = 109, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["farmer","daughter"])
							
class FemGoodTropeTemplate11(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Hippy Chick"),
							 id = 110, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale,PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good)
							
class FemGoodTropeTemplate12(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("HuCow"),
							 id = 111, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([MaritalStatusFemale,AgeAdjFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["athletic","flat-chested","slender","sporty","tight"])
							
class FemGoodTropeTemplate13(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Kitten"),
							 id = 112, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1),  
										], 
							girltype = GirlType.Good,
							NotList = ["mom"])
							
class FemGoodTropeTemplate14(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Pastor's Wife"),
							 id = 113, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["tanned"])
							
class FemGoodTropeTemplate15(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Pixie"),
							 id = 114, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2), 
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["marm","mommy","Amish","Mormon","Christian"])
							
class FemGoodTropeTemplate16(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Princess"),
							 id = 115, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([NationFemale],2), 
										  CTEntry([SpeciesFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["mom"])

class FemGoodTropeTemplate17(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Prom Queen"),
							 id = 116, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([SkinHairColorFemale],2)
										], 
							girltype = GirlType.Good,
							NotList = ["queen","shy","kind","gentle","bashful","lactating","nursing"])
							
class FemGoodTropeTemplate18(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("School-girl"),
							 id = 117, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([NationFemale,SkinHairColorFemale,PregState],2),
										  CTEntry([SpeciesFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["school"])
							
class FemGoodTropeTemplate19(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Single Mom"),
							 id = 118, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([NationFemale,SkinHairColorFemale],3),
										  CTEntry([PregState],2),
										  CTEntry([ProfGoodFemale],1), 
										], 
							girltype = GirlType.Good,
							NotList = ["single","mom","asian","japanese","amish","russian","columbian","bronzed","tanned","czech","brazillian","swedish"])
							
class FemGoodTropeTemplate20(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Slave Girl"),
							 id = 119, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([PregState],3),
										  CTEntry([NationFemale,SkinHairColorFemale],2),
										  CTEntry([ProfBadFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["black","ebony","dark-skinned","town","American","porn","fashion","queen","housewife","nurse","country"])
							
class FemGoodTropeTemplate21(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Small-town Girl"),
							 id = 120, 
							 adjlist = 	[ CTEntry([AttitudeGoodFemale],5),
										  CTEntry([MaritalStatusFemale],4),
										  CTEntry([PhysCharFemale],3),
										  CTEntry([SkinHairColorFemale,PregState],2),
										  CTEntry([ProfGoodFemale],1)
										], 
							girltype = GirlType.Good,
							NotList = ["schoolgirl"])
							
class FemGoodTropeTemplate22(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Snow Bunny"),
							 id = 121, 
							 adjlist = 	[CTEntry([AttitudeGoodFemale],5),
										  CTEntry([PhysCharFemale],4),
										  CTEntry([SkinHairColorFemale,],3),
										  CTEntry([NationFemale,],2),
										], 
							girltype = GirlType.Good,
							NotList = ["mom","town","straight-laced","amish","mormon","christian","modest","shy","demure","conservative","virtuous","uptight","bashful","sheltered"])
							
# Adj:		AgeAdjFemale, AttitudeGoodFemale, AttitudeBadFemale, AttitudeFemale,
# 			ClothingFemale, GenModFemale, MaritalStatusFemale, NationFemale, PhysCharFemale
#			PregState, SexualityFemale, SkinHairColorFemale, SpeciesFemale
# Nouns: 	AgeNounFemale, SpeciesFemale, ProfGoodFemale, ProfBadFemale, ProfFemale, RelateFemale,TitlesFemale


# === Bad Trope templates ===

class FemBadTropeTemplate1(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Porn Star"),
							 id = 200, 
							 adjlist = 	[ 
										  CTEntry([AttitudeBadFemale],7),
										  CTEntry([PhysCharFemale],6),
										  CTEntry([ClothingFemale],5),
										  CTEntry([NationFemale,SkinHairColorFemale],4),
										  CTEntry([AgeAdjFemale],3),
										  CTEntry([SexualityFemale],2),  
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad	)
							
class FemBadTropeTemplate2(FemTropeTemplate):
	def __init__(self):
		super().__init__(	 noun = TropeBitBadFemale("Sex Kitten"),
							 id = 201, 
							 adjlist = 	[CTEntry([GenModFemale],7),
										  CTEntry([AttitudeBadFemale],6),
										  CTEntry([PhysCharFemale],5),
										  CTEntry([ClothingFemale],4),
										  CTEntry([SkinHairColorFemale],3),
										  CTEntry([SpeciesFemale],1),
										], 
							girltype = GirlType.Bad,
							NotList = ['Christian','Mormon'])	
							
	
						
	

			