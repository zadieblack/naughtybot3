#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *

import excerpt.util as exutil
import util as shutil
import excerpt.locations as locations

from util import CoinFlip
from util import WordList
from excerpt.util import AddArticles

from excerpt.locations import LocationSelector

import excerpt.bodyparts as bodyparts
import excerpt.verbs as verbs
import excerpt.misc as misc
import excerpt.scenes as scenes
#import excerpt.names as names
import names 

from excerpt.scenes import SceneSelector

import excerpt.bodyparts as bodyparts
import excerpt.verbs as verbs
import misc as sharedmisc
import excerpt.misc as misc
import excerpt.scenes as scenes

import excerpt.people as people
import excerpt.texttoimg as texttoimg
import title.people as titpeople

PromoHistoryQ = exutil.HistoryQ(2)
	
class Generator():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = exutil.GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def GenerateTweet(self):
		self.MaleBodyParts = bodyparts.BodyMale()
		self.FemBodyParts = bodyparts.BodyFemale()
		self.Semen = bodyparts.Semen()
		
		self.Event = misc.Events()
		self.Exclamation = misc.Exclamations()
		self.TermsOfEndearment = misc.TermsOfEndearment()
		self.Punchline = misc.Punchline()
		self.AfterSexPunchline = misc.PunchlineAfterSex()
		self.WomanAdjs = misc.WomanAdjs()
	
		self.FemaleName = names.NamesFemale()
		self.MaleName = names.NamesMale()
		self.BadGirlNoun = misc.BadGirlNouns()
		self.BadGirlAdj = misc.BadGirlAdjs()
		
		self.VDrip = verbs.VerbDrip()
		self.VEjac = verbs.VerbEjaculate()
		self.VForeplay = verbs.VerbForeplay()
		self.VMakeLove = verbs.VerbMakeLove()
		self.VMoan = verbs.VerbMoan()
		self.VSex = verbs.VerbSex()
		self.VSexWith = verbs.VerbSexWith()
		self.VThrust = verbs.VerbThrust()
		self.VOralMale = verbs.VerbOralMale()
		self.VSexActByMale = verbs.VerbSexActsByMale()
		self.VSexActByFemale = verbs.VerbSexActsByFemale()
		
		self.MaleSO = people.MaleSO()
		self.FemaleSO = people.FemaleSO()
		self.MFWB = people.MaleFWB()
		self.FFWB = people.FemaleFWB()
		
		self.WealthyMan = people.JobWealthyMale()
		self.WealthyWoman = people.JobWealthyFemale()
		self.WhiteCollar = people.JobWhiteCollar()
		self.BlueCollar = people.JobBlueCollar()
	
		return ""
		
def GetTweet(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
	gen = None
	GenType = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	# print("GetTweet() Generator Type is " + str(GenType))
	
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if gen == None:
			gen = Generator()
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
		
	return gen
	
class Generator1(Generator):
	# The baron desecrated Jacinda's well-used muffin with his thick pole.	
	ID = 1
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.VForeplay.Present()
		sTweet = "The " + self.WealthyMan.GetPerson() + " " + self.VThrust.Past() + " " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n'" + sVerb.capitalize() + " my " + self.FemBodyParts.Breasts.RandomDescription() + "!' she " + self.VMoan.Past() + ". '" + sVerb.capitalize() + " them and fill me with your " + self.Semen.FloweryDescription() + "!'"
		
		return sTweet
		
class Generator2(Generator):
	# Spreading open her supple buttocks with his rough hands, he desecrated her well-used anus with his erect boner. 'Fuck me,
	# Jordan!' she screamed. 'Pound me like your wife!'	
		
	ID = 2
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Penis = self.MaleBodyParts.Penis
		Ass = self.FemBodyParts.Ass
		
		sHole1 = self.FemBodyParts.Ass.Anus.RandomDescription()
		sHole2 = self.FemBodyParts.Ass.Anus.RandomDescription()
		while sHole2 in sHole1:
			sHole2 = self.FemBodyParts.Ass.Anus.RandomDescription()
			
		sVerb1 = self.VThrust.Past()
		sVerb2 = ""
		
		sTweet = "Spreading open " + sHerName + "'s " + Ass.RandomDescription() + " "
		sTweet += "with his " + WordList(['rough','strong','calloused','gentle-but-firm']).GetWord() + " hands, "
		sTweet += "he " + sVerb1 + " her " + sHole1 + " with his " + Penis.RandomDescription() + ".\n\n"
		sTweet += "'Fuck me, " + sHisName + "!\' she " + self.VMoan.Past() + ". "
		
		if CoinFlip():
			sVerb = WordList(['Fuck','Do','Pound','Stuff','Ravish','Hammer','Impale','Ream','Plough']).GetWord()
			
			sTweet += "'" + sVerb + " me like I'm your " + self.FFWB.GetPerson() + "!'"
		else:
			sVerb = WordList(['Fuck','Do','Pound','Stuff','Ravish','Hammer','Impale',
							  'Ream','Jack-hammer','Plough','Pump Into','Desecrate',
							  'Defile','Stretch','Probe','Fill']).GetWord()
			sHole = WordList(['anus','ass','asshole','back-door','bowels','bunghole','butthole','corn-hole',
							  'dirt-pipe','fart-blaster','heinie-hole','poop-chute','poop-trap','rectum']).GetWord()
							  
			sTweet += "'" + sVerb + " my " + sHole + " like I'm your " + self.FFWB.GetPerson() + "!'"
		
		return sTweet

class Generator3(Generator):
	# 'Please, no!' she said, squirming as he bayonetted her pink cooch. 'Not while my yoga teacher is watching!'
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Watchers = WordList(['my boss','the mailman','the minister','the pizza delivery boy','the pool boy',
							 'the principal','the rest of the class','my step-son',
							 'my yoga class','the other librarians','the neighbors','the tourists',
							 'my in-laws','my coworkers','the chess club','the cheer squad',
							 'my students','the other moms','the lifeguard','the babysitter',
							 'your step-mom','your friends','your girlfriend','the dog','the cat',
							 'the Jeffersons','the Smiths','the Joneses',
							 'those construction workers','the other nurses','the servants',
							 'the other shoppers','the truck drivers','the janitor','the tour bus',
							 'my sorority sisters','my classmates','the ranch hands','the TV crew',
							 'the youth group','those frat boys','the roadies','mom and dad',
							 'those golfers','the marching band','the dean','the bridesmaids',
							 'the groomsmen','the other flight attendants','the rest of the dojo',
							 'the parade','the ladies from church','my sunday school class',
							 'the nuns','the hockey team','the football team','the judge'])
							 
		Moans = WordList(['cried out','gasped','moaned','panted','whimpered','whispered'])
							 
		Verbs = WordList(['bored into','desecrated','drilled','eagerly filled','fucked','hammered',
						  'penetrated','pistoned into','ploughed','pounded','pumped into',
						  'rammed relentlessly into','ravished','reamed','stuffed',
						  'thrust deep into','licked','sucked on','tongued','fingered','ate out',
						  'rubbed','lubed up','dildoed','massaged','oiled up',
						  'inserted a finger into','inserted two fingers into',
						  'inserted three fingers into','inserted his fist into',
						  'rubbed his ' + self.MaleBodyParts.Penis.RandomDescription(bAllowLongDesc = False) + ' against',
						  'eased his ' + self.MaleBodyParts.Penis.Head.RandomDescription(bAllowLongDesc = False) + ' into'])
			
		sTweet = "'Please!' " + self.FemaleName.FirstName() + " " + Moans.GetWord() + ", squirming with pleasure "
		sTweet += "as " + self.MaleName.FirstName() + " " + Verbs.GetWord() + " "
		if CoinFlip():
			sTweet += "her " + self.FemBodyParts.Vagina.RandomDescription(bAllowLongDesc = False) + ". "
		else:
			if CoinFlip():
				sTweet += "her " + self.FemBodyParts.Ass.RandomDescription(bAllowLongDesc = False) + ". "
			else:
				sTweet += "her " + self.FemBodyParts.Ass.Anus.RandomDescription(bAllowLongDesc = False) + ". "
		sTweet += "'Not here where " + Watchers.GetWord() + " can see us!'"
		
		return sTweet

class Generator4(Generator):
	# 'You may cum inside my womanhood if you like', she instructed him, 'But only my photographer is allowed to bayonette my sphincter.'	
	ID = 4
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'You may cum inside my " + self.FemBodyParts.Vagina.ShortDescription() + " if you like', " + self.FemaleName.FirstName() + " instructed him, 'But only my " + self.MFWB.GetPerson() + " is allowed to " + self.VThrust.Present() + " my " + self.FemBodyParts.Ass.Anus.RandomDescription() + "'."
		
		return sTweet
		
class Generator5(Generator):
	# 'Oh, Leon,' she moaned, 'I'm so thirsty for your glossy spunk!' 'But Ophelia,' he said, 'You're my mother-in-law!'
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'Oh, " + self.MaleName.FirstName() + ",' she " + self.VMoan.Past() + " in his " + self.MaleBodyParts.Arms.MediumDescription() + ", 'I'm so thirsty for your " + self.Semen.RandomDescription() + "!'\n\n'But " + self.FemaleName.FirstName() + ",' he said, 'You're my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
class Generator6(Generator):
	# 'You don't have to hide the truth from me, Honey,' he said, 'Tom is a successful opthamologist and I'm just a lowly roadie!' 
	# 'That's true,' she said, 'But YOU have a 8 1/2 inch fuck-pole!'	
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		PenisAdjs = WordList(['beautiful','beefy','enormous','fat','hairy','hard','magnificient',
							  'massive','meaty','rock-hard','smooth','tasty','thick','juicy',
							  'yummy','stiff','tasty'])
		PenisNouns = WordList(['boner','cock','cock','cock meat','cocksicle','dick','goo-gun',
							   'hard-on','hot-rod','joystick','love-gun','penis','pole',
							   'popsicle','prick','ramrod','schlong','tool'])
		PenisSizes = WordList(['seven-inch','eight-inch','nine-inch','ten-inch','eleven-inch',
							  'foot-long','13-inch','14-inch'])
		
		sRivalName = self.MaleName.FirstName()
		sTweet = "'You don't have to hide the truth from me, " + self.FemaleName.FirstName() + ",' he said, "
		sTweet += "'" + sRivalName + " is a successful " + self.WhiteCollar.GetPerson() + " "
		sTweet += "and I'm just a lowly " + self.BlueCollar.GetPerson() + "!'\n\n"
		sTweet += "'I don't care about " + sRivalName + ",' she said, 'He doesn't have what I want. "
		sTweet += "Now hurry up and " + WordList(['stuff','fill','do','plough','ravish','pound','fuck']).GetWord() + " me with that "
		
		if CoinFlip():
			sTweet += PenisAdjs.GetWord() + " " + PenisSizes.GetWord() + " " + PenisNouns.GetWord() + " of yours!'"
		else:
			sTweet += PenisAdjs.GetWord() + " " + PenisSizes.GetWord() + " " + self.MaleBodyParts.Penis.BuildAPenis() + " of yours!'"
		
		return sTweet
		
class Generator7(Generator):
	# Charity bit her lip as Tristan fondled her heaving bosoms. 'Oh god,' she said, 'What would my pastor say 
	# if he saw that I was letting my pool boy pump into my crack?'	
	
	ID = 7
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(['bang','do','drill','fuck','gape','hammer','impale','nail','plough','pound','ravish','ream','stuff','violate'])
		Location = locations.LocationSelector().Location()
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on "
			sTweet += Location.LyingOn + ", her " + self.FemBodyParts.Breasts.RandomDescription() + " " 
			sTweet += WordList(["heaving", "quivering", "trembling", "shuddering", "rising and falling"]).GetWord() + " "
			sTweet += "as " + self.FemaleName.FirstName() + " lubed up a " 
			sTweet += str(randint(8,16)) + " 1/2\" " + WordList(["black", "pink", "steel", "vibrating"]).GetWord() + " strap-on. "
			sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' she said, "
			sTweet += "'What would Father " + self.MaleName.FirstName() + " say if he knew that "
			sTweet += "my lesbian lover was about to " 
		else:
			sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on " + Location.LyingOn + ", "
			sTweet += "her " + self.FemBodyParts.Breasts.RandomDescription() + " " 
			sTweet += WordList(["heaving", "quivering", "trembling", "shuddering", "rising and falling"]).GetWord() + " "
			sTweet += "as " + self.MaleName.FirstName() + " lubed up her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ". "
			sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' she said, "
			sTweet += "'What would Father " + self.MaleName.FirstName() + " say if he knew that "
			sTweet += "my " + self.MFWB.GetPerson() + " was about to " 
		
		if CoinFlip():
		#ass 
			sTweet += Verbs.GetWord(NotList = ['hammer','impale','nail']) + " my ass " + Location.NamePrep + "?'"
		else:
		#asshole 
			sTweet += Verbs.GetWord(NotList = ['bang','do']) + " my " + self.FemBodyParts.Ass.Anus.ShortDescription() + " " + Location.NamePrep + "?'"
		
		return sTweet

class Generator8(Generator):
	#Bianca bit her lip as he caressed her youthful thighs. 'Ferdinand!' she said, 'My orthodontist is in the next room!' 
	#'Should we invite him?' he asked innocently, inserting a finger into her love channel.	
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(InOut = exutil.LocInOutType.Indoors)
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		sHisName2 = self.MaleName.FirstName()
		while sHisName == sHisName2:
			sHerName2 = self.MaleName.FirstName()
		sHerName2 = self.FemaleName.FirstName()
		while sHerName == sHerName2:
			sHerName2 = self.FemaleName.FirstName()
		sInsertedObject = WordList(["a finger", "two fingers", "three fingers", "a nine-inch steel dildo", 
									"a large eggplant","a ketchup bottle", "a wine bottle", 
									"an enormous black vibrator", "a huge black dildo", "a second dildo",
									"four fingers", "her wadded up dirty panties", "a thumb", "a toe",
									"a strap-on"]).GetWord()
									
		FondleParts = WordList([self.FemBodyParts.Vagina.RandomDescription(),
								self.FemBodyParts.Thighs.RandomDescription(),
								self.FemBodyParts.Ass.RandomDescription(),
								self.FemBodyParts.Vagina.InnerLabia.RandomDescription(),
								self.FemBodyParts.Vagina.OuterLabia.RandomDescription(),
								self.FemBodyParts.Ass.Anus.RandomDescription(),
								self.FemBodyParts.Breasts.RandomDescription(),
								self.FemBodyParts.Breasts.Nipples.RandomDescription(),
								self.FemBodyParts.Hips.RandomDescription(),
								self.FemBodyParts.Skin.RandomDescription()])
								
		
		if CoinFlip():
			sTweet = self.FemaleName.FirstName() + " bit her lip as "
			sTweet += "he " + self.VForeplay.Past() + " "
			sTweet += "her " + FondleParts.GetWord() + " " + Location.NamePrep + ". "
			sTweet += "'" + sHisName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson()
			if CoinFlip():
				sTweet += ", " + self.MaleName.FirstName() + ","
			sTweet += " is right outside!'\n\n'Do you think he'd like to join us?' " + sHisName + " asked innocently, "
			sTweet += "inserting " + sInsertedObject + " into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
		else:
			sTweet = sHerName2 + " bit her lip as " + sHerName + " " + self.VForeplay.Past() + " her " + FondleParts.GetWord() + " " + Location.NamePrep + ". "
			sTweet += "'" + sHerName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson() 
			if CoinFlip():
				sTweet += ", " + self.MaleName.FirstName() + ","
			sTweet += " is right outside!'\n\n'Do you think he'd like to join us?' " + sHerName + " asked innocently, "
			sTweet += "inserting " + sInsertedObject + " into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
		
		return sTweet
		
class Generator9(Generator):
	# 'What?' she said. 'Hasn't a girl ever let you fuck her oiled-up coconuts with your meat pole before?''Only my dad's girlfriend,' he replied.
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'What?' she asked. 'Hasn't a girl ever let you fuck her " + WordList(["big", "massive", "ample", "bountiful", "double-D", "jiggling", "pendulous", "swollen", "plump", "heavy", "hefty", "enormous", "fat"]).GetWord() + ", " + WordList(["oiled-up", "lubed-up", "greased-up", "baby oil-covered", "lotion-soaked"]).GetWord() + " " + self.FemBodyParts.Breasts.ShortDescription() + " with your "
		if CoinFlip():
			sTweet += self.MaleBodyParts.Penis.RandomDescription(bAddLen = True) 
		else:
			sTweet += self.MaleBodyParts.Penis.RandomDescription()
		sTweet += " before?'\n\n'Only my " + self.FFWB.GetPerson() + ",' " + self.MaleName.FirstName() + " replied."
		
		return sTweet
		
class Generator10(Generator):
	# 'Oh lord, what a day it has been,' said the dutchess. Ripping open her blouse, she exposed 
	# her massive double-D mammaries. 'Come, my little fry cook, I need you to nibble on my 
	# buns and then to cover my hard nipples in your salty man jam.'
	ID = 10
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = "'" + self.Exclamation.GetWord(bExMk = False).capitalize() + ", "
		sTweet += "what a day it has been,' said the " + misc.WomanAdjs().GetWord() + " " 
		sTweet += self.WealthyWoman.GetPerson() + ". "
		
		if CoinFlip():
			sTweet += "Ripping open her blouse, she exposed her " + self.FemBodyParts.Breasts.RandomDescription() + " " 
			sTweet += "to him. 'Come, my little " + self.BlueCollar.GetPerson() + ". I need you to " 
			sTweet += self.VForeplay.Present() + " my " + self.FemBodyParts.GetRandomIntimateParts(1, True, True)[0] 
			sTweet += " and cover my " + self.FemBodyParts.GetRandomIntimateParts(1, False, True)[0] + " "
			sTweet += "in your " + self.Semen.RandomDescription() + ".'"
		else:
			sTweet += "Ripping open her blouse, she exposed her " + self.FemBodyParts.Breasts.RandomDescription() + " "
			sTweet += "to " + self.FemaleName.FirstName() + ". 'Come, my " + self.FFWB.GetPerson() + ". I need you to " 
			sTweet += self.VForeplay.Present() + " my " + self.FemBodyParts.GetRandomIntimateParts(1, True, True)[0] + " "
			sTweet += "and then " + WordList(["finger-bang", "fist", "eat out", "lick"]).GetWord() + " "
			sTweet += "my " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ".'"
		
		return sTweet
		
class Generator11(Generator):
	# 'Oh God, Julia,' he said, 'You are so beautiful. I love your supple skin, your sumptuous hips, 
	# your perfect thighs, and the way you look with my ballsack in your mouth.'
	ID = 11
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Parts = self.FemBodyParts
		
		sTweet = "\"" + WordList(["Oh fuck", "Oh god", "Goddam", "Holy fuck", "Oh baby", "Oh god", "Oh fuck","Holy shit"]).GetWord() + ", "
		sTweet += self.FemaleName.FirstName() + ",\" he " + WordList(["moaned","gasped","exclaimed","whispered","cried"]).GetWord() + ", \"You are so " + WordList(['beautiful','sexy','perfect','fucking sexy','hot and sexy','fucking perfect']).GetWord() + ". I love your "
			
		sHair = "your " + Parts.Hair.GetAdj() + " hair, "
		sEyes = "your " + Parts.Eyes.GetAdj() + " eyes, "
		sMouth = "" 
		if CoinFlip():
		#mouth 
			sMouth += "your " + Parts.Mouth.GetAdj() + " mouth, "
		else:
		#lips 
			sMouth += "your " + Parts.Lips.GetAdj() + " lips, "
		sSkin = "your " + Parts.Skin.GetAdj() + " skin, "
		sLegs = "your " + Parts.Legs.GetAdj() + " legs, "
		sThighs = "your " + Parts.Thighs.GetAdj() + " thighs, "
		sAss = "your " + Parts.Ass.MediumDescription() + ", "
		sBody = "your " + Parts.GetAdj() + " body, "
		sTits = "your " + Parts.Breasts.GetAdj() + " breasts, "
			
		PartsDescs = []
		PartsDescs.append(sHair + sEyes + sBody + sTits)
		PartsDescs.append(sHair + sEyes + sSkin + sTits)
		PartsDescs.append(sHair + sEyes + sLegs + sTits)
		PartsDescs.append(sHair + sMouth + sBody + sTits)
		PartsDescs.append(sHair + sMouth + sSkin + sTits)
		PartsDescs.append(sHair + sMouth + sLegs + sTits)
		PartsDescs.append(sHair + sLegs + sThighs + sTits)
		PartsDescs.append(sEyes + sMouth + sBody + sTits)
		PartsDescs.append(sEyes + sMouth + sSkin + sTits)
		PartsDescs.append(sEyes + sMouth + sLegs + sTits)
		PartsDescs.append(sEyes + sSkin + sBody + sTits)
		PartsDescs.append(sEyes + sSkin + sLegs + sTits)
		
		PartsDescs.append(sHair + sEyes + sBody + sAss)
		PartsDescs.append(sHair + sEyes + sSkin + sAss)
		PartsDescs.append(sHair + sEyes + sLegs + sAss)
		PartsDescs.append(sHair + sMouth + sBody + sAss)
		PartsDescs.append(sHair + sMouth + sSkin + sAss)
		PartsDescs.append(sHair + sMouth + sLegs + sAss)
		PartsDescs.append(sHair + sLegs + sThighs + sAss)
		PartsDescs.append(sEyes + sMouth + sBody + sAss)
		PartsDescs.append(sEyes + sMouth + sSkin + sAss)
		PartsDescs.append(sEyes + sMouth + sLegs + sAss)
		PartsDescs.append(sEyes + sSkin + sBody + sAss)
		PartsDescs.append(sEyes + sSkin + sLegs + sAss)
	
		sTweet += PartsDescs[randint(0, len(PartsDescs) - 1)] + "and "
		
		sTweet += "the way you look " 
		
		Endings = []
		Endings.append("with my " + self.MaleBodyParts.Penis.GetRandomPenisPart() + " in your " + self.FemBodyParts.Mouth.RandomDescription(bAllowShortDesc = True))
		Endings.append("with my " + self.Semen.MediumDescription() + " on your " + WordList(["angelic", "innocent", "pretty","sweet","cute","adorable"]).GetWord() + " little face")
		Endings.append("with my " + self.Semen.MediumDescription() + " dripping from your chin")
		Endings.append("with my " + self.Semen.MediumDescription() + " on your " + self.FemBodyParts.Breasts.RandomDescription() + "")
		Endings.append("with my " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + " slapping against your chin")
		Endings.append("with your " + WordList(['red','cherry','full','slutty']).GetWord () + " lips around my " + self.MaleBodyParts.Penis.RandomDescription(bAllowShortDesc = True) + "")
		Endings.append("at me when I'm " + WordList(['balls-deep in','buried to the hilt inside','deep inside','stuffing','pounding']).GetWord() + " " + WordList(["your sister","your twin-sister","your step-sister","your best friend","the babysitter","your step-mom","my secretary","the yoga instructor","that stripper Wendy","some college slut I picked up at the club"]).GetWord())
		Endings.append("with my " + self.MaleBodyParts.Penis.Testicles.MediumDescription() + " stuffed in your mouth")
		Endings.append("when I spank your ass with a riding crop")
		Endings.append("with your " + WordList(['sphincter','anus','asshole','bunghole']).GetWord() + " raw and gaping after I've fucked your ass")
		Endings.append("with my " + self.Semen.MediumDescription() + " " + self.VDrip.Gerund() + " out of your freshly-fucked " + WordList(['sphincter','anus','asshole','bunghole','dirt pipe','pooper']).GetWord())
		Endings.append("with a ball-gag in your mouth")
		Endings.append("with your black eyeliner running as you deep throat me")
		
		sTweet += Endings[randint(0,len(Endings)) - 1] + ".\""
		
		return sTweet
		
class Generator12(Generator):
	# Ginger's robe fell to the floor, and his heart skipped a beat. She had a shapely form with ripe boobs, 
	# wide hips, and a well-used hole. "I can't believe you're my sister," he said.	
	ID = 12
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Parts = self.FemBodyParts
		
		sTweet = sHerName + "'s robe fell to the floor, and his heart skipped a beat. "
		sTweet += "She had "
		
		sSkin = Parts.Skin.GetAdj() + " skin, "
		sLegs = Parts.Legs.GetAdj() + " legs, "
		sThighs =  Parts.Thighs.GetAdj() + " thighs, "
		sAss = "a " + Parts.GetAdj() + " " + WordList(['ass','ass','booty','bottom','behind','butt','tush']).GetWord() + ", "
		sBody = "a " + Parts.GetAdj() + " body, "
		sTits = Parts.Breasts.GetAdj() + " breasts, "
		sVag = "and a " + Parts.Vagina.RandomDescription(bAllowShortDesc = False)
		
		PartsDescs = []
		PartsDescs.append(sSkin + sLegs + sTits + sThighs + sVag)
		PartsDescs.append(sBody + sLegs + sTits + sThighs + sVag)
		PartsDescs.append(sSkin + sLegs + sTits + sThighs + sVag)
		PartsDescs.append(sSkin + sLegs + sAss + sThighs + sVag)
		PartsDescs.append(sBody + sLegs + sThighs + sAss + sVag)
		PartsDescs.append(sSkin + sLegs + sTits + sAss + sVag)
		PartsDescs.append(sLegs + sThighs + sTits + sAss + sVag)
		PartsDescs.append(sBody + sLegs + sTits + sAss + sVag)
		PartsDescs.append(sSkin + sBody + sTits + sAss + sVag)
		
		sTweet += PartsDescs[randint(0, len(PartsDescs) - 1)] + ".\n\n\""
		
		sTweet += self.Exclamation.GetWord(bHappy = True).capitalize() + " "
		
		sMoan = WordList(['gasped','moaned','exclaimed']).GetWord()
		Endings = []
		Endings.append("I can't believe you're really my " + self.FFWB.GetPerson() + "!\"")
		Endings.append("I can't believe I get to " + WordList(["do","fuck","bang","have sex with"]).GetWord() + " my " + self.FFWB.GetPerson() + "!\"")
		Endings.append("I've always fantasized about " + WordList(["doing","fucking","banging","having sex with"]).GetWord() + " my " + self.FFWB.GetPerson() + "!\"")
		
		sTweet += Endings[randint(0,len(Endings)) - 1] + " " + sHisName + " " + sMoan + "."
		
		
		return sTweet
		
class Generator13(Generator):	
	# 'Oh thank God Christina,' he gasped. 'You saved me. How can I ever repay you?' Christina bent over and pulled down her panties,
	# revealing her pert bum. 'You can start by licking my starfish,' she said.
	ID = 13
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iRand = randint(1,3)
		sGirlfriendName = self.FemaleName.FirstName()
		if CoinFlip():
			sTweet = "'Oh thank God,' he said to the " + self.FemBodyParts.Eyes.GetAdj() + "-eyed woman with the " + self.FemBodyParts.Hair.RandomDescription(bAllowShortDesc = False) + ". 'You saved me. How can I ever repay you?'\n\n"
			sTweet += "'My name is " + sGirlfriendName + ",' she said. Then she "
		else:
			sTweet = "'Oh thank God " + sGirlfriendName + ",' " + self.FemaleName.FirstName() + " said to her " + self.FemBodyParts.Eyes.GetAdj() + "-eyed " + self.FFWB.GetPerson() + " with the " + self.FemBodyParts.Hair.RandomDescription(bAllowShortDesc = False) + ". 'You saved me. How can I ever repay you?'\n\n" + sGirlfriendName + " "
			
		if iRand == 1:
			sTweet +=  "bent over and pulled down her panties, revealing her " + self.FemBodyParts.Ass.RandomDescription() + ".\n\n"
			sTweet += "'You can start by licking my " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' she said."
		elif iRand == 2:
			sTweet += "bent over and pulled down her panties, revealing her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ".\n\n"
			sTweet += "'You can start by eating out my filthy little " + self.FemBodyParts.Vagina.ShortDescription() + ",' she said."
		else:
			sTweet += "bent over and pulled down her panties, revealing her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ".\n\n"
			sTweet += "'You can start by fisting my " + self.FemBodyParts.Vagina.InnerVag.ShortDescription() + ",' she said."
		
		return sTweet
	
class Generator14(Generator):
	# 'Oh Julian,' she said, 'I've never been with a duke before.'
	# 'Fear not, my love,' he said, as he began to gently fuck her bunghole."
	ID = 14
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName1 = self.MaleName.FirstName()
		sHisName2 = self.MaleName.FirstName()
		sHerName1 = self.FemaleName.FirstName()
		sHerName2 = self.FemaleName.FirstName()
		
		iRand = randint(1,3)
		
		if iRand == 1:
			sTweet = "'Oh " + sHisName1 + ",' she said, 'I've never been with " + AddArticles(self.WealthyMan.GetPerson()) + " before.'\n\n"
			sTweet += "'Fear not, my " + self.TermsOfEndearment.GetWord() + ", I would never hurt you,' he said as he began to " + self.VMakeLove.Present() + " her " + self.FemBodyParts.GetRandomHole() + " with his " +self.MaleBodyParts.Penis.RandomDescription(bAddLen = True) + "."
		elif iRand == 2:
			sTweet = "'Oh " + sHerName1 + ",' she said, 'I've never been with " + AddArticles(self.WealthyWoman.GetPerson()) + " before.'\n\n"
			sTweet += "'Fear not, my " + self.TermsOfEndearment.GetWord() + ", I would never hurt you,' " + sHerName1 + " said as she " + self.VMakeLove.Past() + " " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.GetRandomHole() + " with " + str(randint(2,5)) + " fingers."
		else:
			sTweet = "'Oh " + sHisName1 + ",' " + sHisName2 + " said, 'I've never been with " + AddArticles(self.WealthyMan.GetPerson()) + " before.'\n\n"
			sTweet += "'Fear not, my sweet boy, I would never hurt you,' " + sHisName1 + " said as he began to " + self.VMakeLove.Present() + " " + sHisName2 + "'s " + self.FemBodyParts.Ass.Anus.ShortDescription() + " with his " + self.MaleBodyParts.Penis.RandomDescription(bAddLen = True) + "."
		
		return sTweet
		
class Generator15(Generator):
	# 'Vance, my love, where are you?' called Anjelica from the next room. Vance looked down at Veronica. Her dazzling blue eyes 
	# were locked on his as she wrapped her hungry mouth around his massive meat pole. "I'll just be a minute dear," Vance replied.
	ID = 15
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iRand = randint(1,3)
				
		sBoyfriendName = self.MaleName.FirstName()
		sTweet = "'" + sBoyfriendName + ", my love, where are you?' called " + self.FemaleName.FirstName() + " from the next room.\n\n"
		sTweet += sBoyfriendName + " looked down at " + self.FemaleName.FirstName() + ". "
		if iRand == 1:
			sTweet += "Her head was cupped in his hands as she bobbed up and down on his " + self.MaleBodyParts.Penis.FloweryDescription() + ".\n\n"
		elif iRand == 2:
			iRandCockLen = randint(6,10)
			sTweet += "Tears trailed from her " + self.FemBodyParts.Eyes.RandomDescription() + " as she took his " + self.MaleBodyParts.Penis.FloweryDescription(bAddLen = True) + " deep into her throat.\n\n"
		elif iRand == 3:
			iRandCockLen = randint(6,10)
			sTweet += "Her " + self.FemBodyParts.Lips.GetAdj() + " lips were wrapped around his " + self.MaleBodyParts.Penis.Head.RandomDescription(bAllowShortDesc = True) + " and she was gently massaging his " + self.MaleBodyParts.Penis.Testicles.ShortDescription() + ".\n\n"
		else:
			sTweet += "Her " + self.FemBodyParts.Eyes.RandomDescription() + " were locked on his as she wrapped her " + self.FemBodyParts.Mouth.RandomDescription() + " around his " + self.MaleBodyParts.Penis.FloweryDescription() + ".\n\n"
		sTweet += "'I'll just be a minute dear,' " + sBoyfriendName + " replied."
		
		return sTweet
		
class Generator16(Generator):
	# Devon squeezed and sucked on Sabrina's luscious double-D mammaries as he fingered her clit and jackhammered her willing cunt 
	# hole. 'My god,' whispered Grant, stroking his meat sword, 'I can't believe I'm watching my wife fuck an opthamologist!'"
		
	ID = 16
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.MaleName.FirstName() + " squeezed and sucked on " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.Breasts.RandomDescription() + " as he fingered her " + self.FemBodyParts.Vagina.Clitoris.RandomDescription() + " and " + self.VThrust.Past() + " her " + self.FemBodyParts.GetRandomHole() + ".\n\n"
		sTweet += "'" + self.Exclamation.GetWord(bHappy = True).capitalize() + "' " + self.VMoan.Past() + " " + self.MaleName.FirstName() + ", stroking his " + self.MaleBodyParts.Penis.RandomDescription() + " as he looked on, 'I can't believe I'm watching my " + self.FemaleSO.GetWord() + " " + self.VSexWith.Present() + " " + AddArticles(self.WhiteCollar.GetPerson()) + "!'"
		
		return sTweet
		
class Generator17(Generator):
	# Charity's eyes were wide as she cupped his dangling nutsack. 'Does every opthamologist have one like this?' she asked. 
	# 'No darling,' said Brad. 'Not every opthamologist has a 9 1/2 inch meat sword. Now play with my testicles while you rub the swollen head.'
	ID = 17
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sWhiteCollarJob = self.WhiteCollar.GetPerson()
		sTweet = self.FemaleName.FirstName() + " stared with innocent " + self.FemBodyParts.Eyes.MediumDescription() + " at his " + self.MaleBodyParts.Penis.MediumDescription() + ". 'Does every " + sWhiteCollarJob + " have a... thing like this?' she asked.\n\n"
		sTweet += "'No darling,' said " + self.MaleName.FirstName() + " chuckling. 'Not every " + sWhiteCollarJob + " has a " + self.MaleBodyParts.Penis.ShortDescription(bAddLen = True) + ". Now massage my " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + " while you suck on my " + self.MaleBodyParts.Penis.Head.ShortDescription() + ".'"
		
		return sTweet
		
class Generator18(Generator):
	# "'Jacinda, my dear, I wrote you a poem,' he said. 'What is it about?' asked Jacinda. 'It's about you, my love: your golden 
	# hair, your generous tits, your smooth legs, your dangling labia.' 'Oh Brad!' she sighed."
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "'" + sGirlfriendName + ", my dear, I wrote you a poem,' he said.\n\n"
		sTweet += "'What about?' she asked.\n\n"
		sTweet += "'It's about you, my love,' he said. 'It's about "
		sTweet += self.FemBodyParts.DescRandomClothedBodyParts(iNum = 5, sDivideChar = ';', bAllowLongDesc = True, sPossessive = "your") + ". "
		sTweet += "And, of course, your " 
		
		iRand = randint(1,5)
		if iRand == 1:
			#Ass
			sTweet += self.FemBodyParts.Ass.FloweryDescription(NotList = ['backside','cheeks','rear','bottom','behind'])
		elif iRand == 2:
			#Asshole
			sTweet += self.FemBodyParts.Ass.Anus.FloweryDescription(NotList = ['back','butt','behind'])
		elif iRand == 3:
			#Vag
			sTweet += self.FemBodyParts.Vagina.FloweryDescription(NotList = ['vag','virgin','mound'])
		elif iRand == 4:
			#Inner labia
			sTweet += self.FemBodyParts.Vagina.InnerLabia.FloweryDescription(NotList = ['virgin','petals'])
		else:
			#Outer labia
			sTweet += self.FemBodyParts.Vagina.OuterLabia.FloweryDescription(NotList = ['virgin','mons pubis','petals','mound','vulva'])
		
		sTweet += ".'\n\n"
		if CoinFlip():
			sTweet += "'Oh " + self.MaleName.FirstName() + "!' she sighed."
		else:
			sTweet += "'Ravish me, " + self.MaleName.FirstName() + "!' she exclaimed."
		
		return sTweet
		
class Generator19(Generator):
	#Unaware Roxanne was watching him, Nicolas pulled his tshirt and jeans off, revealing his broad 
	#shoulders, powerful chest, and sinewy thighs. But what made Roxanne's mouth water was the massive, 
	#throbbing tool between his legs.	
	ID = 19
	Priority = 50
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "Unaware " + sGirlfriendName + " was watching him, " 
		sTweet += self.MaleName.FirstName() + " pulled his tshirt and jeans off. "
		sTweet += "Her eyes widened at the sight of "
		sTweet += self.MaleBodyParts.DescRandomNakedParts(iNum = 5, sDivideChar = ";", bPenis = False, sPossessive = "his")
		sTweet += ". But what made her mouth water was "
		sTweet += "the " + self.MaleBodyParts.Penis.FloweryDescription() + " between his legs."
		
		return sTweet
		
class Generator20(Generator):
	#Xavier approached the bed, completely naked. A thrill ran through Constance at the sight of his broad  
	#shoulders, powerful chest, sinewy thighs, muscular buttocks and swollen man meat. She could hardly 
	#believe that in a few minutes this man would be stuffing her virgin pussy.
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = self.MaleName.FirstName() + " approached the bed completely naked. "
		sTweet += "A " + WordList(['thrill','shiver','tingle']).GetWord() + " "
		sTweet += "ran through " + self.FemaleName.FirstName() + " at the sight of "
		if CoinFlip():
			sTweet += "his " + self.MaleBodyParts.Eyes.RandomDescription(bAllowShortDesc = False) + ", "
		else:
			sTweet += "his " + self.MaleBodyParts.Jaw.RandomDescription(bAllowShortDesc = False) + ", "
		sTweet += self.MaleBodyParts.DescRandomNakedParts(iNum = 4, sDivideChar = ";",bAss = True, bPenis = True, sPossessive = "his")
		sTweet += ".\n\n"
		sTweet += "She could hardly believe that in a few minutes this man would be "
		iRand = randint(1,8)
		if iRand in [1,3]:
			#ass 
			sTweet += self.VThrust.Gerund() + " her virgin " + self.FemBodyParts.Ass.Anus.ShortDescription()
		elif iRand in [4]:
			#mouth
			sTweet += self.VThrust.Gerund() + " her "
			sTweet += self.FemBodyParts.Mouth.RandomDescription()
		elif iRand in [5]:
			#other 
			sTweet += "deep inside her, filling her with his " + self.Semen.RandomDescription()
		else:
			#cunt
			sTweet += self.VThrust.Gerund() + " her virgin " + self.FemBodyParts.Vagina.ShortDescription()
			
		
		sTweet += "!"
		
		return sTweet
		
# class Generator21(Generator):
	# #Candy stroked Lorenzo's turgid meat vigorously. Suddenly his engorged head swelled and spurted gobs of white hot semen on her lips, on her breasts, on her thighs, on her pussy. 'Oh God', she said, 'it's all over my nice Easter Sunday outfit!'
	# ID = 21
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# sTweet = self.FemaleName.FirstName() + " stroked " + self.MaleName.FirstName() + "'s " + self.MaleBodyParts.Penis.RandomDescription() + " vigorously. Suddenly its " + self.MaleBodyParts.Penis.Head.RandomDescription() + " swelled and he " + self.VEjac.Past() + ", sending gobs of " + self.Semen.RandomDescription() + " all over her "
		
		# Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
		# for part in Parts:
			# if not part == Parts[len(Parts) - 1]:
				# sTweet += part + "; "
			# else:
				# sTweet += "and her " + part + ".\n\n"
		# sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' she said. 'You've ruined my nice " + self.Event.GetWord(bRemoveMy = True) + " dress!'"
		
		# return sTweet
		
class Generator22(Generator):
	# John's robe fell to the floor, and Ginger's heart skipped a beat. He had a compact athletic physic with wide shoulders, brawny arms, tight buns, and a 
	# lengthy penis. "I can't believe you're my brother-in-law," she said.	
	ID = 22
	Priority = 2 #2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ['prince','girlfriend']

		sTweet = self.MaleName.FirstName() + "'s robe fell to the floor, and " + self.FemaleName.FirstName() + "'s heart skipped a beat. He had "
		
		sTweet += self.MaleBodyParts.DescRandomNakedParts(iNum = 5, sDivideChar = ";", bPenis = True, bAss = True)
		sTweet += ".\n\n\"" + self.Exclamation.GetWord(bHappy = True).capitalize() + " "
		sTweet += "I'm a lucky " + WordList(['girl','woman']).GetWord() + "!\" "
		sTweet += "she thought to herself. "
		sTweet += "\"My " + self.MFWB.GetPerson() + " "
		sTweet += "is " + WordList(["a sex god","such a snacck","a total dreamboat","such a DILF",
									"such a hunk","fucking sexy","a total hearthrob",
									"a hunk of beefcake"]).GetWord() + "!\""
		
		return sTweet
		
class Generator23(Generator):
	# 'My mother thinks an opthamolgist and a librarian can never find love together,' said Raoul as Esmerelda lay exhausted in his strong arms.\r\n
	# 'You're no opthamologist,' she replied, panting. 'You're the mayor of Ream My Ass City!'
	ID = 23
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sWhiteCollar = self.WhiteCollar.GetPerson()
		sTweet = "'My " + self.FFWB.GetPerson() + " thinks " + AddArticles(sWhiteCollar) + " and his " + self.FFWB.GetPerson() + " can never find love together,' said " + self.MaleName.FirstName() + " as " + self.FemaleName.FirstName() + " lay exhausted in his " + self.MaleBodyParts.Arms.MediumDescription() + ".\n\n"
		sTweet += "'You're no " + sWhiteCollar + ",' she replied, panting. 'You're the mayor of " + WordList(["do", "fill", "fuck", "hammer", "hump", "jizz", "nail", "plough", "pound", "ravage", "ream", "slam", "stuff"]).GetWord().capitalize() + " My " + self.FemBodyParts.GetRandomHole(bAllowShortDesc = True, bAllowLongDesc = False, bIncludeMouth = False).title() + " City!'"
		
		return sTweet
		
class Generator24(Generator):
	#Whispering and giggling, they locked themselves in the dressing room. In moments, the man had Angelica 
	#bent over the bench in the dressing room, and the two were banging passionately. He was soon exploding 
	#deep within her trim entrance as an intense orgasm wracked her body. Warm beads of cream hung from 
	#Angelica's lustful cunt and onto the rubber mat. She scooped some up with her fingers and tasted it. 
	#Angelica got down on her knees and began to lick the silken cock-snot from his thick erection. Angelica 
	#wiggled into her panties.
	#'Hell, yes! I can't believe I'm not a virgin anymore,' she said.
	ID = 24
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		
		sTweet = Location.BeginDesc + " "
		
		bMale = CoinFlip()
		if bMale:
			sHisName = self.MaleName.FirstName()
			sHerName = "the woman"	
		else:
			sHisName = "the man"
			sHerName = self.FemaleName.FirstName()
		
		CreamPieScene = scenes.SceneCreamPie("", sHerName, Location = Location)
		SceneSelect = SceneSelector()

		if CoinFlip():
			if bMale:
				sTweet += sHisName + " took the " + self.WomanAdjs.GetWord() + " woman in his " + self.MaleBodyParts.Arms.MediumDescription() + ". "
			else: 
				sTweet += sHerName + " sighed as " + sHisName + " began to squeeze her " + self.FemBodyParts.Breasts.MediumDescription() + " and kiss the nape of her neck. "
			Scene1 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
			
			sTweet += "First " + Scene1.SceneShortDesc3P + ", then "
			
			Scene2 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
			while Scene2.__class__ == Scene1.__class__:
				Scene2 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location) 
			sTweet += Scene2.SceneShortDesc3P + ", and finally "
			
			Scene3 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location) 
			while Scene3.__class__ == Scene1.__class__ or Scene3.__class__ == Scene2.__class__:
				Scene3 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location) 
			sTweet += Scene3.SceneShortDesc3P + ". "
			
			SceneClimax = SceneSelect.GetScene(Tags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
			
			sTweet += SceneClimax.Scene() + "\n\n"
		else: 
			SceneForeplay = None
			ScenePosition = None 
			SceneClimax = None 
			
			if bMale:
				SceneForeplay = SceneSelect.GetScene(Tags = {exutil.TAG_FOREPLAY, exutil.TAG_DONE_TO_HER}, sHisName = sHisName, sHerName = sHerName, Location = Location)
			else:
				SceneForeplay = SceneSelect.GetScene(Tags = {exutil.TAG_FOREPLAY, exutil.TAG_DONE_TO_HIM}, sHisName = sHisName, sHerName = sHerName, Location = Location)
			
			if CoinFlip():
				sTweet += SceneForeplay.Scene() + "\n\n"
				
				ScenePosition = SceneSelect.GetScene(Tags = {exutil.TAG_POSITION}, sHisName = sHisName, sHerName = sHerName, Location = Location)
				
				SceneClimax = SceneSelect.GetScene(Tags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
				
				sTweet += "Then, " + ScenePosition.SceneShortDesc3P + ". At last he could stand it no longer, so " + SceneClimax.SceneShortDesc3P + ".\n\n"
			else:
				if bMale:
					sTweet += sHisName + " took the " + self.WomanAdjs.GetWord() + " woman in his " + self.MaleBodyParts.Arms.MediumDescription() + ". "
				else: 
					sTweet += sHerName + " carressed the man's " + self.MaleBodyParts.MediumDescription() + ". "
					
				sTweet += "First, " + SceneForeplay.SceneShortDesc3P + " until at last she was ready. "
				
				ScenePosition = SceneSelect.GetScene(Tags = {exutil.TAG_POSITION}, sHisName = sHisName, sHerName = sHerName, Location = Location)
				
				sTweet += ScenePosition.Scene() + " "
				
				SceneClimax = SceneSelect.GetScene(Tags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
				
				sTweet += "At last he could stand it no longer, so " + SceneClimax.SceneShortDesc3P + ".\n\n"
		
		if bMale:
			sTweet += sHisName + " " + Location.PutOnMaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.AfterSexPunchline.GetPunchline(exutil.Gender.Male)
		else: 
			sTweet += sHerName + " " + Location.PutOnFemaleClothing(bBottomOnly = True) + "."
			sTweet += " " + self.AfterSexPunchline.GetPunchline(exutil.Gender.Female)
		
		return sTweet
		
class Generator25(Generator):
	#Juliette knelt on the boss's desk and Tristan began to lick her hairless outer labia. Despite the the danger of being caught it felt amazing. Tristan eased his hairless penis into her velvet vagina. 
	#'But Tristan,' she said, 'Someone will catch us!!' 
	#'Don't worry baby,' he said, pounding into her. 
	#The door opened and a tall man walked in. 'Fuck, its my boss!' she said. 
	#'Lord! I'm gonna cum!' said Tristan. 
	#'Wait, not yet!' she cried. 
	#'Too late!' said Tristan. 'I'm ejaculating!' And then, as her boss watched, open-mouthed, he grabbed her by the hips and filled her succulent womb with silken milky man-custard.
	ID = 25
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		iRand = randint(1,3)
		
		sTweet = sHerName + " knelt " + Location.KneelingOn + " and " + sHisName + " began to lick her "
		
		if iRand == 1:
			sTweet += self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + ". "
		elif iRand == 2:
			sTweet += self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + ". "
		else:
			sTweet += self.FemBodyParts.Ass.Anus.RandomDescription() + ". "
			
		sTweet += sHisName + " eased his " + self.MaleBodyParts.Penis.RandomDescription() + " into her " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + ".\n\n"
		sTweet += "'But " + sHisName + ",' she said, '" + Location.HurryReason + "!'\n\n"
		
		if CoinFlip():
			sTweet += "'Don't worry baby,' he said, " + self.VThrust.Gerund() + " into her.\n\n"
			sTweet += Location.Caught + "\n\n"
			if CoinFlip():
				sTweet += "'" + self.Exclamation.GetWord().capitalize() + " I'm gonna cum!' said " + sHisName + ".\n\n"
				sTweet += "'Wait, not yet!' she cried.\n\n"
				sTweet += "'Too late!' said " + sHisName + ". 'I'm " + self.VEjac.Gerund() + "!' And then, as " + Location.Consequence + ", he grabbed her by the hips and filled her " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " with " + self.Semen.RandomDescription() + "."
			else:
				sTweet += sHisName + " smiled at the " + Location.AuthorityFigure + ". 'It's okay if you want to watch us,' he said."
		else:
			sTweet += "'But you want us to get caught, don't you, baby?' he purred. 'You want me to " + self.VThrust.Present() + " your little " + self.FemBodyParts.Vagina.GetAdj(sNot ="little") + " " + self.FemBodyParts.Vagina.GetNoun() + " in front of " + Location.AuthorityFigure + ". You want me to fill your " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " with my " + self.Semen.RandomDescription() + " as they watch you get fucked.\n\n"
			sTweet += "'Ooh, fuck yes!' she " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator26(Generator):
	#Naked in a public location and caught.
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		iRand = randint(1,3)
		iRandLength = randint (7,12)
		
		sTweet = sHisName + " and " + sHerName + " could barely keep their hands off each other as they tore off their clothes. " + sHisName + " grabbed her and squeezed her bare " + self.FemBodyParts.Ass.RandomDescription() + " as he explored her " + self.FemBodyParts.Mouth.RandomDescription() + " with his tongue.\n\n"
		sTweet += sHerName + " got on her knees and began to " + self.VForeplay.Present() + " his " + str(iRandLength) + "\" " + self.MaleBodyParts.Penis.ShortDescription() + " and " + self.VForeplay.Present() + " his " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + ".\n\n"
		sTweet += "Suddenly, " + sHerName + " froze. " + Location.Caught + "\n\n"
		sTweet += Location.Excuse + "\n\n"
		sTweet += "'" + self.Exclamation.GetWord(bSad = True).capitalize() + "' " + sHerName + " exclaimed. 'I knew it was a bad idea to do this " + Location.NamePrep + "!'"
		
		return sTweet
		
class Generator27(Generator):
	# 'You're such a slut, Veronica,' he said. 'I *am* a slut,' she said. 'I'm one for *you*, James. 
	# I'm a slut for your hard cock in my mouth.' 'You're also a slut because you let me fuck your 
	# backdoor in the bathroom at Starbucks,' he said.
	ID = 27
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sBadGirlName = self.BadGirlNoun.GetWord() 
		Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "'You're such " + AddArticles(sBadGirlName).lower() + ", " + sHerName + ",' he said.\n\n"
		sTweet += "'I *am* " + AddArticles(sBadGirlName).lower() + ",' she said. 'I'm one for *you*, " + sHisName + ". I'm " + AddArticles(sBadGirlName) + " for your " + self.MaleBodyParts.Penis.RandomDescription(bAddLen = True) + " in my " + self.FemBodyParts.Mouth.RandomDescription(bAllowLongDesc = False) + ".'\n\n"
		sTweet += "'You're also " + AddArticles(sBadGirlName).lower() + " because you let me " + self.VThrust.Present() + " your " + self.FemBodyParts.Ass.Anus.ShortDescription() + " " + Location.NamePrep + ",' he said."
		
		return sTweet
		
class Generator28(Generator):
	#Doing it in a location. Surprise! They're being watched by her husband.
	ID = 28
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = Location.BeginDesc + " "
		if not Location.FemaleBottomClothing == "": 
			sTweet += sHisName + " ripped " + sHerName + "'s " + Location.FemaleBottomClothing + " off. "
		sTweet += "She sat down " + Location.SittingOn + " and spread her legs. " + sHisName + " began to "
		if CoinFlip():
			sTweet += self.VForeplay.Present() + " her " + self.FemBodyParts.Vagina.OuterLabia.RandomDescription() + " vigorously.\n\n" 
		else: 
			sTweet += self.VForeplay.Present() + " her " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " tenderly.\n\n"
		sTweet += "'I'm ready!' she " + self.VMoan.Past() + ". 'I want that " + self.MaleBodyParts.Penis.RandomDescription() + " in me right now!'\n\n"
		sTweet += "He inserted his " + self.MaleBodyParts.Penis.ShortDescription() + " into her " + self.FemBodyParts.Vagina.InnerVag.MediumDescription() + " and began to " + self.VThrust.Present() + " it roughly.\n\n"
		sTweet += "'Harder, baby, I want you to " + self.VEjac.Present() + " inside,' she " + self.VMoan.Past() + ". Then she looked over at her " + self.MaleSO.GetWord() + ", " + self.MaleName.FirstName() + "."
		
		iRand = randint(1,4)
		if iRand == 1:
			sTweet += " 'You like this, baby?' she asked him."
		elif iRand == 2:
			sTweet += " 'Do you want him to do my ass, baby?' she asked him."
		elif iRand == 3: 
			sTweet += " 'This is how a real man does it', she " + self.VMoan.Past() + "."
		else:
			sTweet += " 'I think he's bigger than you, baby,' she said to him."
		
		return sTweet
		
class Generator29(Generator):
	#Martin walked in to see Sabrina lying on the bed. Her nose was in a book and her short nightgown was hiked up over her pert bottom. Her hand was down her panties and Martin could see that she was frigging her starfish urgently.
	#'What are you reading?' Martin asked.
	#'Sex Slave to the Vampire Pirates,' Sabrina moaned.
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = sHisName + " found " + sHerName + " lying on her bed in her nightgown with her nose in a book and one hand down her lacy panties. She was frigging her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + " with urgent fingers.\n\n"
		sTweet += "'What are you reading?' he asked.\n\n"
		sTweet += "'" + misc.BookTitleBuilder().GetTitle() + ",' " + sHerName + " " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator30(Generator):
	#'C'mere baby,' she said. 'I want you to suck on my inch-long nipples. I want to feel your fevered package against my bottom and then I want you to fill my silk womb with your semen.' 'Ooooh, yes,' sighed Julian. 'But my priest says it's wrong to do this with my teacher.'
	ID = 30
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'C'mere baby,' she said. 'I want you to suck on my "
		if CoinFlip():
			sTweet += self.FemBodyParts.Breasts.ShortDescription() + ". "
		else:
			sTweet += self.FemBodyParts.Breasts.Nipples.RandomDescription() + ". "
		if CoinFlip():
			sTweet += "I want to feel your " + self.MaleBodyParts.Penis.RandomDescription() + " against my " + self.FemBodyParts.Ass.ShortDescription() + " "
		else:
			sTweet += "I want you to spread my legs wide and " + self.VForeplay.Present() + " my " + self.FemBodyParts.Vagina.Clitoris.RandomDescription() + " "
		if CoinFlip():
			sTweet += "and then I want you to " + self.VMakeLove.Present() + " my " + self.FemBodyParts.Vagina.RandomDescription() + ".'\n\n"
		else:
			sTweet += "and then I want you to fill my " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " with your " + self.Semen.RandomDescription() + ".'\n\n"
		
		sTweet += "'Ooooh, yes,' " + self.VMoan.Past() + " " + self.MaleName.FirstName() + ". 'But my priest says it's wrong to do this with my " + self.FFWB.GetPerson() + ".'"
		
		return sTweet
		
class Generator31(Generator):
	# Trevor walked in and froze. His step-sister lay on the bed totally nude. His wide eyes took in her heavy tits, wide hips, sticky folds, and puckered sphincter. The naked guy next to her was idly diddling her peach. He looked up at Trevor. 'You want in?' he asked.
	ID = 31
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sFFWB = self.FFWB.GetPerson()
		
		sTweet = sHisName + " walked in and froze. His " + sFFWB + " lay on the bed totally nude. His wide eyes took in "
		sTweet += self.FemBodyParts.DescRandomNakedParts(bPussy = True, bAss = True, bAllowLongDesc = True, sPossessive = "her") + ".\n\n"
		sTweet += "The naked guy next to her was idly " + self.VForeplay.Gerund() + " her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". "
		"He looked up at " + sHisName + ".\n\n"
		sTweet += "\"" + WordList(["Oh hey, bruh","Wassup, bruh","Oh, hey dude","Wassup, my dude"]).GetWord() + ",\" "
		sTweet += "he said. \"You want in?\""
		
		return sTweet
		
class Generator32(Generator):
	#I've got a present for you, she said. What's that? he asked her. She [bent over and pulled her panties aside, 
	#revealing her little starfish.] [lifted up her short skirt revealing that she wasn't wearing any panties. He 
	#could clearly see her smooth pussy lips and her inner folds.] [pulled her titties out of her blouse. They 
	#were large and gleaming with oil.]
	ID = 32
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iRand = randint(1,3)
		
		sTweet = "'I've got a present for you,' she said.\n\n"
		sTweet += "'What's that?' he asked.\n\n"
		if iRand == 1:
			sTweet += "She bent over and hiked her skirt up, showing him her " + self.FemBodyParts.Ass.RandomDescription() + ". Then she pulled her panties aside, revealing her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ".\n\n"
		elif iRand == 2:
			sTweet += "She lifted up her short skirt and he saw that she wasn't wearing panties. Her " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " peaked out shyly from her " + self.FemBodyParts.Vagina.OuterLabia.MediumDescription() + "."
			if CoinFlip():
				sTweet += " Her " + self.FemBodyParts.Vagina.ShortDescription() + " was shaved smooth and bare"
			else:
				sTweet += " Her bush had been carefully trimmed to " + WordList(["a thin landing strip", "a fuzzy little 'v'", "an arrow pointing directly at her pink cleft"]).GetWord()
				if CoinFlip(): 
					sTweet += " and dyed a startling shade of " + WordList(["mauve", "purple", "red", "turquoise", "blue", "green"]).GetWord()
			sTweet += ".\n\n"
		else:
			sTweet += "She pulled her " + self.FemBodyParts.Breasts.RandomDescription() + " out of her low-cut blouse. They were large and " + self.FemBodyParts.Breasts.GetAdj() + " and gleaming with oil. She rolled her " + self.FemBodyParts.Breasts.Nipples.RandomDescription() + " between her fingers.\n\n"
		sTweet += "'Happy " + self.Event.GetWord() + ", baby,' she said."
		
		return sTweet
		
class Generator33(Generator):
	# 'I own you now,' he said to Cherry. "Your pretty mouth belongs to me. So do your lickable tits, 
	# and the dripping folds of your cunt. Even your tight little asshole is mine now.' and I even own..." 
	# He leaned forward, and whispered in her ear, "Your tight little starfish."
	# "Ooh, yes {sir/master/daddy}," she said. "Make me your fuck toy! But wait," she added. 
	# "Am I still your babysitter?"
	ID = 33
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		LastNames = WordList(['Beaver','Bell','Bottoms','Brown','Butts','Chang','Church','Clark',
							  'Cox','Cummings','Davis','Devlyn','Goodbody','Gray','Green','Hancock',
							  'Hill','Jefferson','Johnson','Jones','King','Lee','Long','Lopez',
							  'Moore','Moorecox','Muncher','Peach','Pearl','Peckwood','Peters',
							  'Philmore','Popper','Robinson','Rogers','Ross','Sanderson',
							  'Smith','St. Claire','Taylor','Wang','White','Williams','Wilson',
							  'Woody','Black'])
		Jobs = WordList(['babysitter','barista','English teacher','guidance counselor','maid',
						  'marriage counselor','math tutor','parole officer','secretary',
						  'Sunday School teacher','teacher','psychiatrist','teacher\'s aid',
						  'office manager','research assistant','real estate agent',
						  'coach','wife\'s pregnancy surrogate',
						  'student','pupil','house maid','nanny','nurse','yoga instructor',
						  'therapist''personal assistant'])
						  
		Others = WordList(['mom','dad','my husband','your wife','your girlfriend','your fiancé',
						   'my boyfriend','my fiancé','your brother-in-law','your other employees',
						   'the rest of the class','the other nurses'])
						   
		MouthPhrases = WordList(['dirty little mouth','insatiable mouth','filthy little mouth',
								 'insolent mouth','whore mouth','full lips','cherry lips',
								 'sweet lips','innocent mouth','dick-sucking lips',
								 'cock-sucking lips','cock-hungry mouth','soft lips'])
		sMouthPhrase = MouthPhrases.GetWord()
		sMouthOwnVerb = ""
		if "lips" in sMouthPhrase:
			sMouthOwnVerb = "belong"
		else:
			sMouthOwnVerb = "belongs"
		
		VagNames = WordList(['cunt','flower','love-muffin','pussy','quim','sex','snatch','twat','vagina','womanhood'])
		SubAdjs = WordList(['little','little','dirty','nasty','dirty','filthy','little black','little blonde',
							'little Asian','little redheaded','little white','shameless','little brown'])
		SubNouns = WordList(["cum slut","fuck toy","cum rag","whore","sex slave","slave girl","fuck bunny","slut","cock-slut"])
		
		sTweet = "\"I own you now,\" he said to " + sHerName + ". "
		sTweet += "\"Your " + sMouthPhrase + " " + sMouthOwnVerb + " to me now. "
		sTweet += "So do your " + self.FemBodyParts.Breasts.GetAdj() + " " + WordList(["tits","boobs","titties","breasts","melons"]).GetWord() + " "
		sTweet += "and the " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " of your " + VagNames.GetWord() + ". "
		sTweet += "Even your " + self.FemBodyParts.Ass.RandomDescription() + " is mine now to do with as I please.\"\n\n"
		
		if CoinFlip():
			sTweet += "\"Ooh, yes " + WordList(['master','daddy','sir']).GetWord() + "!\" said " + sHerName + ". "
			sTweet += "\"Make me your " + SubAdjs.GetWord() + " " + SubNouns.GetWord() + "! "
			
			if CoinFlip():
				sTweet += "But hang on,\" she added. \"Am I still going to be your " + Jobs.GetWord() + "?\""
			else:
				sTweet += "But hang on,\" she added. \"What do we tell " + Others.GetWord() + "?\""
		else:
			sLastName = LastNames.GetWord()
			
			sTweet += "\"Ooh, yes Mr. " + sLastName + "!\" she said. "
			sTweet += "\"Make me your " + SubAdjs.GetWord() + " " + SubNouns.GetWord() + "! "
			sTweet += "But hang on,\" she added. \"What about Mrs. " + sLastName + "?\""
		
		return sTweet
		
class Generator34(Generator):
	#'It was just a silly bet,' he said.\n\n
	#'No, fair is fair,' she said, pulling down her panties. 'I said that you could use my cocksock any way you want, right here in the woods, and I never go back on a bet.' 
	ID = 34
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		iRand = randint(1,4)
		
		sTweet = "'It was just a silly bet,' " + self.MaleName.FirstName () + " said to his " + misc.WomanAdjs().GetWord() + " " + self.FFWB.GetPerson() + ". 'Don't worry about it.'\n\n"
		sTweet += "'No, fair is fair,' " + self.FemaleName.FirstName() + " said, pulling down her " + Location.FemaleBottomClothing + ". "
		if iRand == 1:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Vagina.RandomDescription() + " any way you want, "
		elif iRand == 2:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Vagina.InnerVag.RandomDescription() + " any way you want, "
		elif iRand == 3:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Ass.RandomDescription() + " any way you want, "
		else:
			sTweet += "'I said that you could use my " + self.FemBodyParts.Ass.Anus.RandomDescription() + " any way you want, "
		sTweet += "right here " + Location.NamePrep + ", and I never go back on a bet.' "
		
		return sTweet
		
class Generator35(Generator):
	#'Oh baby,' she said. 'I love you so much. I just want to be with you and make you happy. Tell me what I can do,' she said, giving him a peck on the lips.
	#'I want {to fuck your big titties / to put my finger in your butthole / to put my balls in your mouth / you to eat out my starfish },' he said.
	ID = 35
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Private)
		
		iRand = randint(1,7)
		sHisName = self.MaleName.FirstName()
		
		sTweet = "'Oh " + sHisName + ",' " + self.FemaleName.FirstName() + " said to him. They were sitting together " + Location.NamePrep + ". 'I love you so much. I just want to be with you and make you happy. Just tell me how,' she said, giving him a peck on the lips.\n\n"
		if iRand == 1:
			sTweet += "'I want to rub my " + self.MaleBodyParts.Penis.ShortDescription() + " on your " + self.FemBodyParts.Breasts.RandomDescription(bAllowLongDesc = False) + "', he said."
		elif iRand == 2:
			sTweet += "'I want to put my finger in your " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' he said."
		elif iRand == 3:
			sTweet += "'I want to put my " + self.MaleBodyParts.Penis.Testicles.ShortDescription() + " in your mouth,' he said."
		elif iRand == 4:
			sTweet += "'I want to fist your " + self.FemBodyParts.Vagina.MediumDescription() + ",' he said."
		elif iRand == 5:
			sActs = WordList(["throat fuck","finger bang","tea bag","titty-fuck","bang","have sex with","butt-fuck",
							  "ass-fuck","impregnate","fist","creampie"]).GetWord()
			sTweet += "'I want to " + sActs + " your " + WordList(['sister','twin sister','best friend','maid of honor','cousin','BFF']).GetWord() + ",' he said."
		elif iRand == 6:
			sFilthyAct = WordList(["my friends to gang-bang you","to have a gang-bang","to have a threesome with your sister",
							  "to fuck your mom","to taste your asshole","you to fuck my friends",
							  "to teabag you","to take your anal virginity","to pop your anal cherry",
							  "to post naked pics of you on Facebook","you to blow my best friend",
							  "to give you a Dirty Sanchez","to pee in your mouth","butt fuck you",
							  "cum on your face","to fuck you in a church","to see you take double anal",
							  "you to give my dad a blowjob","to titty-fuck you","to whore you out",
							  "you to do porn with black men","you to wear a ball gag",
							  "to watch you have sex with a girl","to do you in front of your brother",
							  "you to wear a gimp suit during sex","you to suck on my hairy balls",
							  "you to get your clit pierced","to fist your poop-chute"]).GetWord()
			sTweet += "'I want " + sFilthyAct + ",' he said."
		else:
			sTweet += "'I want you to lick my " + self.FemBodyParts.Ass.Anus.ShortDescription() + ",' he said."
		
		return sTweet
		
class Generator36(Generator):
	#Their masked host guided them into the banquet hall. On the dining table a beautiful woman lay spread-eagled, completely naked, in the center. Her succulent bronzed skin was dripping with honey, her lissome form was covered with fruits and berries, her navel was brimming with liquor, her full, perfect breasts were topped with whipped cream, and her pussy was stuffed with a single ripe strawberry. 'Gentlemen,' said the marquis, 'Let's eat!'\n\n'Holy fuck,' thought Leon, 'That's my step-daughter!'
	ID = 36
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		print("Generator36 active")
		
		sTweet = "Their masked host ushered them into the banquet hall. In the center of the dining table a beautiful woman lay spread-eagled, completely naked. "
		
		Feast = []
		Feast.append("her succulent " + self.FemBodyParts.Skin.GetAdj(sNot = "succulent") + " " + self.FemBodyParts.Skin.GetNoun() + " was dripping with syrup") 
		Feast.append("she held a ripe cherry between her " + self.FemBodyParts.Lips.GetAdj(sNot = "cherry") + " lips")
		Feast.append("her " + self.FemBodyParts.GetAdj(sNot = "womanly") + " " + self.FemBodyParts.GetNoun() + " was covered with fruits and berries")
		Feast.append("her navel was a goblet brimming with liquor") 
		Feast.append("her full, " + self.FemBodyParts.Breasts.GetAdj(sNot = "full") + " " + self.FemBodyParts.Breasts.GetNoun() + " were topped with whip cream")
		Feast.append("the inside of her " + self.FemBodyParts.Thighs.ShortDescription() + " were glazed with chocolate")
		Feast.append("her " + self.FemBodyParts.Vagina.OuterLabia.GetNoun() + " gleamed with sticky honey")
			
		sFeast = ""
		if len(Feast) > 0:
			for x in sorted(sample(range(0, len(Feast)), 3)): 
				sFeast += Feast[x] + ", "
			sFeast += "and a "
			sFeast = sFeast.capitalize()
		else: 
			sFeast = "A "
				
		sTweet += sFeast + "single, ripe strawberry was stuffed in her " + self.FemBodyParts.Vagina.MediumDescription() + ". "
		sTweet += "'Gentlemen,' said the " + self.WealthyMan.GetPerson() + ", 'Let's feast!'\n\n"
		sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' thought " + self.MaleName.FirstName() + ", 'That's my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
# class Generator37(Generator):
	# ID = 37
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Penis = self.MaleBodyParts.Penis 
		
		# sManEyes = ""
		# sManPenis = ""
		# sManTip = ""
		# sManBalls = ""
		# sManSize = str(randint(7,12))
		# sWealthyMan = self.WealthyMan.GetPerson()
		# sManAdjs = WordList(["tall", "muscular", "bearded"])
		
		# if CoinFlip():
			# #wealthy man is a BBC
			# sWealthyMan = "black " + sWealthyMan
			# sManEyes = "dark, smoldering eyes"
			# sManPenis = "black, " + Penis.GetAdj(sNot="black") + " " + Penis.ShortDescription()
			# sManTip = "dark, " + Penis.Head.GetAdj(sNot="dark") + " " + Penis.Head.ShortDescription()
			# sManBalls = "ebony " + Penis.Testicles.ShortDescription()
		# else:
			# sManEyes = self.MaleBodyParts.Eyes.RandomDescription()
			# sManPenis = Penis.RandomDescription()
			# sManTip = Penis.Head.RandomDescription()
			# sManBalls = Penis.Testicles.ShortDescription()
			
		# if CoinFlip():
			# sManSize += " & 1/2\""
		# else:
			# sManSize += "\""
		
		# sHisName = self.MaleName.FirstName()
		# sHerName = self.FemaleName.FirstName()
		
		# sTweet = "'I'm afraid, Miss " + sHerName + ",' said the " + sWealthyMan + ", 'that I'm going to have to tell your " + self.MaleSO.GetPerson() + " about your little... indiscretion.'\n\n"
		# sTweet += "'Please don't tell him,' she said, looking up at him " + WordList(["pitifully", "hopefully", "wretchedly", "wistfully", "dejectedly", "breathlessly"]).GetWord() + ". He had " + sManEyes + " and his " + WordList(['brawny','broad','mighty','muscular','powerful','rugged','strong','sturdy','well-built','wide']).GetWord() + " shoulders filled out his sharply-tailored " + WordList(["tuxedo", "three-piece suit", "black suit", "button-down silk shirt", "sport coat", "gray suit"]).GetWord() + " nicely. 'I'll do anything.'\n\n"
		# if CoinFlip():
			# sTweet += "'You must be punished, Miss " + sHerName + ",' he said. 'Will you do as I say?' She nodded.\n\n"
			# sTweet += "'Then bend over and lift your skirt.' " + sHerName + " flushed, but she knew she had no choice. She bent lifted the hem, exposing her bare " + self.FemBodyParts.Ass.MediumDescription(sNot = "bare") + " and her " + self.FemBodyParts.Vagina.RandomDescription() + ". 'No panties?' said the " + sWealthyMan + ", 'My, my, you *are* a " + self.BadGirlNoun.GetWord() + ".' He unbuckled his belt and pulled it off. She tensed as he approached. He put one hand on her " + self.FemBodyParts.Ass.RandomDescription() + " and raised the belt in his fist.\n\n"
			# sTweet += "'I'd tell you this will only sting a little,' he said, 'But " + WordList(["we both know that it is going to hurt", "that would be a lie", "I would never lie to a beautiful woman", "this will definitely leave a mark", "if it didn't hurt, it wouldn't be a punishment"]).GetWord() + ".'"
		# else:
			# sTweet += "'Anything?' he asked, arching an eyebrow. She nodded mutely. 'On your knees, then,' he said. "
			# if CoinFlip():
				# sTweet += "He slowly unbuckled his belt. Then he "
			# else:
				# sTweet += "He "
			# sTweet += "unzipped his trousers. "	+ sHerName + "'s eyes widened as his " + sManSize + " " + sManPenis + " unfurled. His " + sManBalls + " was " + Penis.Testicles.GetAdj() + " and " + Penis.Testicles.GetAdj() + ", and his " + sManTip + " was inches from her face.\n\n"
			# sTweet += WordList(["'You can start by sucking my " + Penis.ShortDescription() + ",' he said.", "'You can start by deep-throating this,' he said.", "'Now suck on my " + Penis.Testicles.MediumDescription() + ",' he said.", "'You will do what I say,' he said, 'and right now I say suck my " + Penis.ShortDescription() + ".'"]).GetWord()
			
		
		# return sTweet
		
class Generator38(Generator):
	# Brad entered the bedroom. Marsha was lying on the bed wearing nothing but red high heels. His gaze lingered on her pert breasts, rounded hips, and lush tush. 
	# 'This is a great birthday present babe, he said.
	# 'This isn't your present,' said Marsha.
	# A tall black woman stepped thru the bathroom door. Her sumptuous breasts were full and heavy and her pussy was shaved bare.
	# 'THIS is your birthday present,' Marsha said.
	ID = 38
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ThirdAdj = WordList(['blonde', 'redheaded', 'brunette', 'Asian', 'black'])
		
		sGiverName = ""
		sBirthdayName = ""
		
		if CoinFlip():
			sGiverName = self.FemaleName.FirstName()
			sBirthdayName = self.MaleName.FirstName()
		
			sTweet = sBirthdayName + " entered the bedroom. " + sGiverName + " was lying on the bed wearing nothing but " + WordList(["a leather corset", "a jeweled butt-plug", "a red garter around her thigh", "crotchless panties", "red high heels"]).GetWord() + ". His gaze lingered on her "
			
			sTweet += self.FemBodyParts.DescRandomNakedParts(iNum = 4, bAllowLongDesc = True, bPussy = True, bAss = True, sPossessive = "her")
			sTweet += ". 'This is a great birthday present, babe,' he said.\n\n"
			sTweet += "'This isn't your present,' said " + sGiverName + "."
			
		else:
			sGiverName = self.MaleName.FirstName()
			sBirthdayName = self.FemaleName.FirstName()
		
			sTweet = sBirthdayName + " entered the bedroom. " + sGiverName + " was wearing nothing but " + WordList(["a cowboy hat", "a leather jacket", "a cock ring", "a bowtie", "a pair of cowboy boots", "a leather body harness"]).GetWord() + " and his " + self.MaleBodyParts.RandomDescription() + " gleamed with oil. Her gazed lingered on his "
			
			Parts = self.MaleBodyParts.DescRandomNakedParts(iNum = 3, bAss = True, bPenis = True, sDivideChar = ";")
			for part in Parts:
				if not part == Parts[len(Parts) - 1]:
					sTweet += part + "; "
				else:
					sTweet += "and " + part
			sTweet += ". 'This is a great birthday present, babe,' she said.\n\n"
			sTweet += "'This isn't your present,' said " + sGiverName + "."
			
		if CoinFlip():
			sTweet += " A tall " + ThirdAdj.GetWord() + " woman stepped thru the bathroom door. She opened her robe to reveal her naked body. Her sumptuous " + self.FemBodyParts.Breasts.GetNoun(sNot = "sumptuous") + " were full and heavy and her " + self.FemBodyParts.Vagina.GetNoun() + " was shaved bare.\n\n"
		else:
			sTweet += " A tall " + ThirdAdj.GetWord() + " man stepped thru the bathroom door. He opened his robe to reveal his naked body. His strapping chest was " + self.MaleBodyParts.Chest.GetAdj(sNot = "strapping") + " and his " + self.MaleBodyParts.Penis.ShortDescription(bAddLen = True) + " was " + self.MaleBodyParts.Penis.GetAdj() + " and " + self.MaleBodyParts.Penis.GetAdj() + ".\n\n"
			
		sTweet += "'THIS is your birthday present,' " + sGiverName + " said."
		
		return sTweet
		
class Generator39(Generator):
	#Naked in a public location and watched.
	ID = 39
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public, InOut = exutil.LocInOutType.Indoors)
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		iRand = randint(1,3)
		iRandLength = randint (7,12)
		
		sTweet += sHerName + " " + Location.RemoveFemaleClothing() + ". " + sHisName + " bent her over " + Location.BentOver + ". His " + self.MaleBodyParts.Penis.ShortDescription() + " was " + self.MaleBodyParts.Penis.GetAdj(sNot = "erect") + " and fully erect. "
		if CoinFlip():
			sTweet += "He spread her " + self.FemBodyParts.Ass.MediumDescription() + " open and carefully eased into her " + self.FemBodyParts.Ass.Anus.RandomDescription(bAllowShortDesc = False) + ". "
		else:
			sTweet += "He spread her legs and then eased all " + str(randint(5,13)) + " inches of his " + self.MaleBodyParts.Penis.MediumDescription() + " inside her " + self.FemBodyParts.Vagina.InnerVag.MediumDescription() + " and then began to " + self.VThrust.Present() + " into her. "
		sTweet += "'But " + sHisName + ",' she " + self.VMoan.Past() + ", '" + Location.HurryReason + "!'\n\n"
		sTweet += "'Don't worry, baby,' he said. 'No one will see us " + Location.NamePrep + ".'\n\n"
		
		if CoinFlip():
			if CoinFlip():
				sTweet += self.MaleName.FirstName() + " watched from his hiding place. His jeans were unzipped and he was stroking his " + self.MaleBodyParts.Penis.MediumDescription() + " feverishly."
			else:
				sTweet += self.MaleName.FirstName() + " watched through the camera. He was stroking his " + self.MaleBodyParts.Penis.MediumDescription() + " feverishly."
		else:
			if CoinFlip():
				sTweet += self.FemaleName.FirstName() + " watched from her hiding place. Her hands were down her panties and she was frigging her " + self.FemBodyParts.Vagina.ShortDescription() + " furiously."
			else:
				sTweet += self.FemaleName.FirstName() + " watched through the camera. She was frigging her " + self.FemBodyParts.Vagina.ShortDescription() + " furiously."
			
		return sTweet
		
class Generator40(Generator):
	ID = 40
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		AdvExcited = WordList(["breathlessly", "huskily", "with a moan", "ardently", "lustfully", "with a sigh"])
		VerbFill = WordList(["fill", "stuff", "ravish", "pound", "fuck", "deflower", "enter"])
		sVagAdj1 = self.FemBodyParts.Vagina.GetAdj(sNot = "moist")
		
		sSceneStart = ""
		if CoinFlip():
			sSceneStart = Location.BeginDesc + " "
		else:
			sSceneStart = Location.NamePrep.capitalize() + ","
		
		sMaleJob = ""
		if CoinFlip():
			sMaleJob = self.WealthyMan.GetPerson()
		else:
			sMaleJob = self.WhiteCollar.GetPerson()
			
		sExposed = ""
		if CoinFlip():
			sExposed = self.FemBodyParts.Vagina.ShortDescription()
		else:
			sExposed = self.FemBodyParts.Vagina.OuterLabia.ShortDescription()
		
		sTweet = sSceneStart + " "
		if not Location.FemaleBottomClothing == "": 
			sTweet += sHisName + " slipped " + sHerName + "'s " + Location.FemaleBottomClothing + " down over her " + self.FemBodyParts.Hips.RandomDescription(bAllowShortDesc = True) + ". "
		else:
			sTweet += sHerName + " was already naked and wet for " + sHisName + ". "
		sTweet += "She sat down " + Location.SittingOn + " and spread her legs, exposing her moist, " + self.FemBodyParts.Vagina.GetAdj(sNot = "moist") + " " + sExposed + ".\n\n"
		sTweet += "'" + sHisName + "' she said " + AdvExcited.GetWord() + ". 'I want you in me right now. I want you to " + VerbFill.GetWord() + " me with your big, " + self.MaleBodyParts.Penis.GetAdj(sNot = "big") + " " + sMaleJob + "'s " + self.MaleBodyParts.Penis.ShortDescription(bAddLen = True) + "!'"
		
		return sTweet
		
class Generator41(Generator):
	#Adam walked into the bedroom and froze. His wife and another man were rolling on the bed and their 
	#clothes were strewn about the room.\n\n{sex act}\n\n{'My god, Marsha', he said angrily. 'You and 
	#the MaleFWB??' / 'Oh Marsha,' he sighed, 'This is revenge for when I titty-fucked my 
	#FemaleFWB, isn't it?' / }
	ID = 41
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		sThisScene = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		iRand = randint(1,3)
		
		if CoinFlip():
			sThisScene = SceneSelector().GetScene(Location = Location, sHisName = "the man", sHerName = sHerName).Scene()
			
			sTweet = sHisName + " walked into the bedroom and froze. His " + self.FemaleSO.GetPerson() + " " + sHerName + " and another man were rolling around on the bed naked. "
			sTweet += sThisScene + "\n\n"
			
			if iRand == 1:
				sTweet += "'My god, " + sHerName + "', " + sHisName + " shouted angrily. 'You and your " + self.MFWB.GetPerson() + "??'"
			elif iRand == 2:
				sTweet += "'" + sHerName + " you " + self.BadGirlAdj.GetWord() + " " + self.BadGirlNoun.GetWord() + "!', " + sHisName + " said. 'I can't believe you two started without me!'"
			else:
				sTweet += "'Oh " + sHerName + ",' " + sHisName + " sighed, 'This is revenge for when I " + self.VSexActByMale.Past() + " my " + self.FFWB.GetPerson() + ", isn't it?'"
		else:
			sThisScene = SceneSelector().GetScene(Location = Location, sHisName = sHisName, sHerName = "the woman").Scene()
			
			sTweet = sHerName + " walked into the bedroom and froze. Her " + self.MaleSO.GetPerson() + " " + sHisName + " and another woman were rolling around on the bed naked. "
			sTweet += sThisScene + "\n\n"
			
			if iRand == 1:
				sTweet += "'My god, " + sHisName + "', she shouted angrily. 'You and your " + self.FFWB.GetPerson() + "??'"
			elif iRand == 2:
				sTweet += "'" + sHisName + ", you fucking slut!', she said. 'I can't believe you two started without me!'"
			else:
				sTweet += "'Oh " + sHisName + ",' she sighed, 'This is revenge for when I " + self.VSexActByFemale.Past() + " my " + self.MFWB.GetPerson() + ", isn't it?'"

		return sTweet
		
class Generator42(Generator):
	ID = 42
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location()
		
		if CoinFlip():
			sTweet = "'Oh " + sHerName + "', he sighed as he held her in his " + self.MaleBodyParts.Arms.GetAdj() + " " + self.MaleBodyParts.Arms.GetNoun() + " " + Location.NamePrep + ", 'I never want this moment to end. I want to stare into your " + self.FemBodyParts.Eyes.MediumDescription() + " and "
			
			iRand = randint(1,3)
			if iRand == 1:
				sTweet += "kiss your " + self.FemBodyParts.Breasts.MediumDescription() 
			elif iRand == 2:
				sTweet += "kiss your " + self.FemBodyParts.Lips.MediumDescription()
			else:
				sTweet += "kiss you all over your " + self.FemBodyParts.Skin.MediumDescription()
			
			sTweet += " forever. I want to " + self.VSexActByMale.Present(NotList = ['jerk off']) + " you all night long.'"
		
		else:
			sTweet = "'Oh " + sHisName + "', she sighed as he held her in his " + self.MaleBodyParts.Arms.GetAdj() + " " + self.MaleBodyParts.Arms.GetNoun() + " " + Location.NamePrep + ", 'I never want this moment to end. I want to stare into your " + self.MaleBodyParts.Eyes.MediumDescription() + " and "
			
			if CoinFlip():
				sTweet += "kiss your " + self.MaleBodyParts.Jaw.MediumDescription() 
			else:
				sTweet += "put my head against your " + self.MaleBodyParts.Chest.MediumDescription()
			
			sTweet += " forever. I want to " + self.VSexActByFemale.Present() + " you all night long.'"
		
		return sTweet
		
class Generator43(Generator):
	ID = 43
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		sSkankDesc = self.BadGirlAdj.GetWord() + " " + self.BadGirlNoun.GetWord()
		
		sTweet = "'Tell me the truth, " + sHisName + ",' she said. 'Tell me you're not seeing that " + sSkankDesc + " " + sHerName + " again.'\n\n"
		sTweet += "'I promise, my dear,' he said."
		
		iRand = randint(1,6)
		if iRand == 1:
			sTweet += "\n\n'Good,' she said. 'I want to be the only " + self.FFWB.GetPerson() + " that you are " + self.VSexWith.Gerund() + ".'"
		elif iRand == 2:
			sHole = ""
			if CoinFlip():
				sHole = self.FemBodyParts.Vagina.ShortDescription()
			else:
				sHole = self.FemBodyParts.Ass.Anus.ShortDescription()
			sTweet += " 'Besides, her " + sHole + " smells like " + WordList(["fish", "garlic", "pickles", "vinegar", "sour milk", "spinach"]).GetWord() + ".'"
		elif iRand == 3:
			sHole = self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowLongDesc = False, bAllowShortDesc = True)
			sTweet += " 'Your " + sHole + " is the only " + sHole + " for me.'"
		elif iRand == 4:
			sTweet += "\n\n'Good,' she said. 'Anyway, I'll bet she doesn't let you " + self.VSexActByMale.Present() + " her like I do.'"
		elif iRand == 5:
			sTweet += " 'Do you think I'd buy a solid gold butt plug for anyone else's " + self.FemBodyParts.Ass.Anus.MediumDescription() + " but yours?'"
		else:
			sTweet += " 'She means nothing to me. She's only my " + self.FemaleSO.GetPerson() + ".'"
			
		return sTweet
		
class Generator44(Generator):
	ID = 44
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Vagina = self.FemBodyParts.Vagina
		Breasts = self.FemBodyParts.Breasts
		Ass = self.FemBodyParts.Ass 
		
		DressAdj = WordList(["little", "slinky", "skimpy", "scanty", "revealing", "elegant", "short", "sparkly"]).GetWord()
		DressColor = WordList(["black", "red", "blue", "white", "sheer"]).GetWord()
		
		sTweet = "'You like my outfit?' " + self.FemaleName.FirstName() + " asked.\n\n"
		sTweet += "'It's stunning, babe,' " + self.MaleName.FirstName() + " said.\n\n"
		
		if CoinFlip() and CoinFlip():
		#do breasts
			if CoinFlip():
				sTweet += "He slid one strap of her " + DressAdj + " " + DressColor + " dress off her shoulder. Then he boldly pulled out one of her " + Breasts.RandomDescription() + ". He squeezed it " + WordList(["gently", "tenderly", "delicately", "softly", "lovingly"]).GetWord() 
			else:
				sTweet += "He grabbed the top of her strapless " + DressColor + " gown and tugged it down, revealing her " + Breasts.RandomDescription() + ". He cupped them with his hands and squeezed them " + WordList(["gently", "tenderly", "delicately", "softly", "lovingly"]).GetWord() 
			sTweet += ". Then he began to " + WordList(["suck", "lick", "kiss"]).GetWord() + " her " + Breasts.Nipples.RandomDescription() + "."
				
		else:
		#do ass
			if CoinFlip():
				sTweet += "She grinned wickedly and spun around. "
			else:
				sTweet += "'Right answer', she said, turning around. "
			sTweet += "She lifted up the hem of her " + DressAdj + " " + DressColor + " dress, showing him her " + Ass.RandomDescription() + " and " 
			if CoinFlip():
				sTweet += Vagina.RandomDescription()
			else:
				sTweet += Vagina.OuterLabia.RandomDescription()
			sTweet += ".\n\n"
			
			sTweet += WordList(["'Now remember,' she said, 'Just the tip.'", 
								"'Put your finger in my " + Ass.Anus.ShortDescription() + ",' she said.",
								"'Do you want to do me in my " + Vagina.ShortDescription() + " or my " + Ass.Anus.ShortDescription() + "?' she asked.",
								"'Pick a hole, daddy,' she said.", 
								"'My " + Vagina.ShortDescription() + " is yours, daddy,' she said.",
								"'My " + Ass.Anus.ShortDescription() + " is yours, daddy,' she said.",
								"'Remember, no butt stuff', she said.", 
								"'Take me hard, daddy,' she said.",
								"'I want you to pop my anal cherry, baby,' she said.",
								"'Come here and eat my ass,' she said.",
								"'Use me like a whore,' she whispered.",
								"'Spank me hard, I've been very naughty, daddy!' she said.",
								"'I like it rough, daddy,' she purred.",
								"'Lube me up, daddy,' she purred.",
								"'Cum fill me with your " + self.Semen.RandomDescription() + ",' she moaned.",
								"'Come lube up my " + Ass.Anus.ShortDescription() + ",' she said.",
								"'All my holes are yours, daddy,' she purred.",
								"'Now I want you to stuff me with that big " + self.MaleBodyParts.Penis.ShortDescription() + ",' she said.", 
								"'The trick is not to wear anything underneath,' she said.", 
								"'I need you to bang me like a screen door, baby,' she said.",
								"'I even shaved my " + Vagina.ShortDescription() + " for you, daddy,' she said."
							  ]).GetWord()
			
		
		return sTweet
		
class Generator45(Generator):
	ID = 45
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		BadWeatherAdjs = WordList(["bleak", "chilly", "cold", "damp", "dark", "freezing", "frosty", "raining", "snowing", "stormy", "tempestuous", "wet", "wild", "windswept", "windy", "wintry"])
		sBWAdj1 = BadWeatherAdjs.GetWord()
		sBWAdj2 = BadWeatherAdjs.GetWord(NotList = [sBWAdj1])
		
		sTweet = "It was " + sBWAdj1 + " and " + sBWAdj2 + " " + WordList(["in the forest", "in the old manor house", "on the moor", "in the ruins of the castle", "on the shore of the frozen lake", "along the rocky beach", "atop the cliff", "among the craggy hills", "beneath the stars", "in the heart of the mountains"]).GetWord() + ".\n\n'We had best huddle together for warmth, " + sHerName + ",' said " + sHisName + ". She curled up against him and he wrapped his " + self.MaleBodyParts.Arms.GetAdj() + " arms around her.\n\n'Oh! What is that?' " + sHerName + " exclaimed."

		if CoinFlip():
			sTweet += " 'It feels long and hard!'"
			
		sTweet += "\n\n'That's my " + self.MaleBodyParts.Penis.BuildAPenis() + ", " + misc.TermsOfEndearment().GetWord() + ",' he said.\n\n'We had better keep it warm,' " + sHerName + " said. "
		
		if CoinFlip():
			if CoinFlip():
				sTweet += "'Why don't you snuggle it against my " + self.FemBodyParts.Ass.GetNoun() + ",' she suggested."
			else:
				sTweet += "'I'll use my mouth,' she said. Then she scooted down and began to " + self.VOralMale.Present() + " his " + self.MaleBodyParts.Penis.RandomDescription(bAllowShortDesc = True) + "."
		else:
				sTweet += "'Why don't you put it in here?' she asked. Then " + sHisName + " felt her hands guiding his " + self.MaleBodyParts.Penis.MediumDescription() + " into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
			
		return sTweet

class Generator46(Generator):
	#Martin walked in to see Sabrina lying on the bed. Her nose was in a book and her short nightgown was hiked up over her pert bottom. Her hand was down her panties and Martin could see that she was frigging her starfish urgently.
	#'What are you reading?' Martin asked.
	#'Sex Slave to the Vampire Pirates,' Sabrina moaned.
	ID = 46
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = sHisName + " found " + sHerName + " lying on her bed in her nightgown with her nose in a book and one hand down her lacy panties. She was frigging her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + " with urgent fingers.\n\n"
		sTweet += "'What are you reading?' he asked.\n\n"
		sTweet += "'" + misc.BookTitleBuilder().GetTitle() + ",' " + sHerName + " " + self.VMoan.Past() + "."
		
		return sTweet
		
class Generator47(Generator):
	#Sable could feel the swollen head of Geoffrey's cock against the tight ring of her anus. 'Oh, go slowly Geoffrey!'
	#
	#'I am, my love,' he replied. Gently but firmly, he eased his turgid 8 1/2" cock into her entrance.
	#
	#'Oh!' Sable gasped. 'Wow! Don't stop Geoffrey, please.'
	#
	#Geoffrey took his time and used lots of lube until at last he was balls deep inside her tush. 'Oh god, baby, you're so 
	#tight!' he gasped as he began to piston into her.
	#
	#'I've let dozens of men fuck my pussy, babe,' said Sable, 'But you're the only man who will ever plough my sphincter.'
	ID = 47
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = None
		Penis = self.MaleBodyParts.Penis 
		Ass = self.FemBodyParts.Ass
		Anus = Ass.Anus 
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = sHerName + " felt the " + Penis.Head.RandomDescription(bAllowShortDesc = True) + " of " + sHisName + "'s " + Penis.ShortDescription() + " against the tight ring of her " + Anus.ShortDescription(sNot = "anus") + ". 'Oh, go slowly!' she " + self.VMoan.Past() + ".\n\n"
		sTweet += WordList(["Gently", "Tenderly", "Carefully", "Lovingly", "Patiently"]).GetWord() + " but " + WordList(["firmly", "forcefully", "powerfully", "unwaveringly", "decisively"]).GetWord() + ", applying lots of lube, " + sHisName + " eased his " + Penis.RandomDescription(bAddLen = True) + " into her " + Anus.RandomDescription(bAllowLongDesc = False) + ". "
		sTweet += " At last he was " + WordList(["balls-deep", "buried to the hilt", 
												 "up to his " + Penis.Testicles.RandomDescription(bAllowShortDesc = True)]).GetWord() + " "
		sTweet += "inside her " + Ass.RandomDescription(bAllowShortDesc = True, NotList = ['behind','buns','buttocks','cheeks']) + ". "
		sTweet += "'" + self.Exclamation.GetWord(bHappy = True, bExMk = False).capitalize() + ", " 
		sTweet += self.TermsOfEndearment.GetWord() + ", you're so tight!' "
		sTweet += "he " + self.VMoan.Past(NotList = ['purr','sigh','wail']) + ".\n\n"
		
		iRand = randint(1,6)
		
		if iRand == 1:
			Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
			sTweet += "'" + self.Exclamation.GetWord(bHappy = True, bExMk = False).capitalize() + ", " 
			sTweet += sHisName + ",' she " + self.VMoan.Past() + ". "
			sTweet += "'Make me an anal-" + self.BadGirlNoun.GetWord(NotList = ['wanton']) + " right here " + Location.NamePrep + "!'"
		elif iRand == 2:
			Location = locations.LocationSelector().Location(InOut = exutil.LocInOutType.Outdoors)
			sTweet += "'" + self.Exclamation.GetWord(bHappy = True).capitalize() + "' "
			sTweet += "she " + self.VMoan.Past() + ". 'I love the feeling of " 
			sTweet += WordList(["doing anal", "getting butt-fucked", "getting ass-fucked", "having my asshole pounded", 
								"anal penetration"]).GetWord() + " " 
			sTweet += Location.NamePrep + "!'"
		elif iRand == 3:
			sFuck1 = WordList(['fucked','creamed','stuffed','pounded','banged']).GetWord()
			sFuck2 = WordList(['fuck','cream','stuff','pound','nail','ravish','do','ream',
							   'violate','fist','bang','impale','gape']).GetWord(NotList = [sFuck1])
			sTweet += "'" + WordList(['Dozens of','At least twenty','More than two dozen','More than three dozen',
									  'Over fifty','At least sixty-nine','Over a hundred',
									  'Over two hundred','Dozens and dozens of']).GetWord() + " "
			sTweet += "men have " + sFuck1 + " "
			sTweet += "my " + self.FemBodyParts.Vagina.ShortDescription() + ", " 
			sTweet += self.TermsOfEndearment.GetWord() + ",' she said. "
			sTweet += "'But you're the only one I'll ever let " + sFuck2 + " my " + Anus.ShortDescription() + "!'"
		elif iRand == 4:
			sTweet += sHerName + " " + WordList(["squeezed","clenched","contracted","constricted"]).GetWord() + " "
			sTweet += "her " + WordList(["sphincter", "bowels", "anus", "rectum", "asshole"]).GetWord() + " "
			sTweet += "tightly around his " + Penis.ShortDescription() + ". " 
			sTweet += sHisName + " " + WordList(['gasped','moaned']).GetWord() + " aloud. "
			sTweet += "'That means \"I love you\" " + self.TermsOfEndearment.GetWord() + ",' she said to him."
		elif iRand == 5:
			sTweet += "'Whoops! " + self.Exclamation.GetWord(bHappy = False, bExMk = True).capitalize() + "' " 
			sTweet += sHerName + " said. 'Hand me that toilet paper, baby.'"
		else:
			sTweet += "'Hurry up and " + self.VEjac.Present() + ", " + self.TermsOfEndearment.GetWord() + ",' she said. "
			sTweet += "'" + self.MaleName.FirstName() + "'s turn is next.'"
		
		return sTweet
		
class Generator48(Generator):
	ID = 48
	Priority = 1
	Type = exutil.GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		TitleBuilder = misc.BookTitleBuilder()
		BookSeller = misc.BookSellers()
		Hashtag = misc.Hashtags()
		SexyAdj = misc.SexyAdjs()
		FavWord = WordList()
		
		Titles = []
		
		Titles.append("\"" + TitleBuilder.GetTitle() + "\"\n\nComing soon on " + BookSeller.GetWord() + "!")
		Titles.append("\"" + TitleBuilder.GetTitle() + "\"\n\nAvailable soon at " + BookSeller.GetWord() + "!")
		Titles.append("\"" + TitleBuilder.GetTitle() + "\"\n by F.L. Bott\n\nOut soon on " + BookSeller.GetWord() + "!")
		
		sTweet = Titles[randint(0,len(Titles) - 1)]
		
		return sTweet
		
class Generator49(Generator):
	#'Now remember,' Veronica said, 'when you meet my parents, you can't tell them that you're a dishwasher at Applebee's 
	#and that we met when you titty-fucked me behind a club. You're a successful chiropractor and your name is Reginald.'
	ID = 49
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)

		Scene = scenes.SceneSelector().GetScene("", "", Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, Location = Location)
		sShortScene = Scene.SceneShortDesc1PHer
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sBlueCollarJob = self.BlueCollar.GetPerson()
		sWhiteCollar = self.WhiteCollar.GetPerson()
		
		sTweet = "'Now remember', " + sHerName + " said, 'When you meet my parents, you can't tell them that you're " + AddArticles(sBlueCollarJob) + " and that we met when " + sShortScene + " " + Location.NamePrep + ". You are a successful " + sWhiteCollar + " and your name is " + sHisName + ".'"
		
		return sTweet

class Generator50(Generator):
	# 'Did you miss me, Francesca?' asked Veronica. She was wearing a blue tank-top and daisy dukes that rode high, showing off her tanned thighs and her bubble butt. Her pert nipples poking through the thin fabric of her top. Pablo could see that she was bra-less. He swallowed the lump in his throat. 
	# 'Go away, Francesca,' he said. 'I'm a successful veterinarian now. I'm married to a beautiful opthamalogist. We have (2-14) children!' Pablo said. 
	# 'That's too bad,' she said. 'Then I guess you have no interest in *this*.' She pulled the crotch of her tight shorts aside. Her pussy lips were tanned and hairless, and a metal piercing gleamed in her clit.
	# 'Oh, fuck!' moaned Pablo.
	ID = 50
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		DressAdj = WordList(["little", "slinky", "skimpy", "scanty", "revealing", "sparkly", "sheer", "clingy"]).GetWord()
		DressColor = WordList(["black", "red", "blue", "white", "sheer"]).GetWord()
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sWhiteCollarHim = self.WhiteCollar.GetPerson()
		sWhiteCollarHer = self.WhiteCollar.GetPerson()
		sExclaim = self.Exclamation.GetWord()
		
		Ass = self.FemBodyParts.Ass
		Breasts = self.FemBodyParts.Breasts
		Vag = self.FemBodyParts.Vagina
		Hips = self.FemBodyParts.Hips
		
		Teases = []
		sText1 = "She was wearing a " + DressColor + " tank-top. Her daisy dukes rode high, showing off her tanned thighs and her " + Ass.RandomDescription() + ". Her " + Breasts.Nipples.MediumDescription() + " poked through the thin fabric of her top. Pablo could see that she was bra-less. "
		sText2 = "She pulled the crotch of her tight shorts aside. Her " + Vag.OuterLabia.RandomDescription(bAllowShortDesc = True) + " were tanned and hairless, and a metal piercing gleamed in her clit"
		
		#---------
		sText1 = "She had poured herself into a " + DressAdj + " " + DressColor + " dress that hugged her " + Hips.MediumDescription() + " and left little to the imagination. "
		sText2 = "She pulled down the zipper on the back of the little " + DressAdj + " dress, and it slipped from her shoulders and pooled about her feet. She was naked except for her high heels. Her " + Breasts.ShortDescription() + " were tanned and " + Breasts.GetAdj(sNot = "tanned") + " and her " + Vag.ShortDescription() + " was shaved bare."
		Teases.append([sText1, sText2])
		#---------
		
		#---------
		sText1 = "She was wearing a " + WordList(["skimpy", "tiny", "little", "sexy", "revealing", "sparkly", "itty-bitty"]).GetWord() + " " + DressColor + " bikini top that barely contained her " + Breasts.RandomDescription() + " and a pair of very short shorts. "
		sText2 = "She wiggled her shorts down over her " + Hips.RandomDescription(bAllowLongDesc = False) + " and let them fall to the ground. The narrow " + DressColor + " g-string she had on underneath plunged between her " + WordList(["hairless", "shaved", "smoothly shaven", "naked", "bare"]).GetWord() + " " + Vag.OuterLabia.RandomDescription() + "."
		Teases.append([sText1, sText2])
		#---------
		
		#---------
		sText1 = "She had poured herself into a " + DressColor + " dress with a plunging neckline that showed off her " + Breasts.RandomDescription() + " nicely. "
		sText2 = "She unzipped her dress and let it slide off her shoulders. Underneath she was wearing lacey, " + DressAdj + " lingerie. Her " + Breasts.Nipples.RandomDescription() + " were clearly visible through the thin bra and her " + Vag.RandomDescription() + " peeked from her crotchless panties."
		Teases.append([sText1, sText2])
		#---------
		
		#---------
		sText1 = "She was wearing a " + DressColor + " spandex sports bra and a very tight pair of little running shorts. He could not help but admire her " + self.FemBodyParts.RandomDescription() + " and her "
		if CoinFlip():
			sText1 += Ass.RandomDescription() + ". "
		else:
			sText1 += Breasts.RandomDescription() + ". The sports bra could not conceal the fact that she had pierced her nipples. "
		sText2 = "She peeled the shorts down off her " + Hips.RandomDescription(bAllowShortDesc = True) + ". She was not wearing any panties. She had shaved her bush into " + WordList(["a narrow landing strip", "a heart", "an arrow pointing downward", "a narrow 'V'"]).GetWord() + " and her " + Vag.RandomDescription(sNot = 'glistening') + " glistened with moisture."
		Teases.append([sText1, sText2])
		#---------
		
		#---------
		BodyParts = WordList([Breasts.RandomDescription(), Hips.RandomDescription(), self.FemBodyParts.Legs.RandomDescription(), Ass.RandomDescription(), Vag.RandomDescription(), Vag.OuterLabia.RandomDescription(), Vag.InnerLabia.RandomDescription()])
		sText1 = "A " + DressAdj + " " + DressColor + " dress hugged her " + self.FemBodyParts.RandomDescription() + " and she was wearing sheer stockings and red high-heels. "
		sText2 = "She shrugged the " + DressColor + " dress from her bare shoulders and let it fall to the floor. " + sHisName + " realized that what he had taken to be pantyhose was in fact a sheer bodystocking. His hungry eyes took in her "
		i = 0
		for x in sorted(sample(range(0, len(BodyParts.List)), 3)): 
			if i == 2:
				sText2 += "and "
			sText2 += BodyParts.List[x]
			if i < 2:
				sText2 += ", "
			i += 1
		sText2 += "."
		Teases.append([sText1, sText2])
		#---------
		
		iRand = randint(0, len(Teases) - 1)
		
		sTweet = "'Did you miss me, " + sHisName + "?' asked " + sHerName + ". "
		sTweet += Teases[iRand][0]
		sTweet += "He swallowed the lump in his throat.\n\n"
		sTweet += "'" + WordList(["Go away", "Leave me alone", "Get out of here", "I'm not interested"]).GetWord() + ", " + sHerName + ",' he said. 'I'm a successful " + sWhiteCollarHim + " now. I'm married to a beautiful " + sWhiteCollarHer + ". We have " + str(randint(2,14)) + " children!'\n\n"
		sTweet += "'That's too bad,' she said. 'I suppose that means you have no interest in *this.*'\n\n"
		sTweet += Teases[iRand][1]
		sTweet += "\n\n'" + sExclaim.capitalize() + "' " + self.VMoan.Past() + " " + sHisName + "."
		
		
		return sTweet
		
class Generator51(Generator):
	ID = 51
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		SceneFuck = None
		SceneOrgasm = None
		
		sTweet += Location.BeginDesc + " " 
		
		iRand = randint(1,4)
		if iRand == 1:
		#blowjob 
			SceneFuck = scenes.SceneBlowjob(sHisName = sHisName, sHerName = sHerName, Location = Location)
			SceneOrgasm = scenes.SceneFacial(sHisName = sHisName, sHerName = sHerName, Location = Location)
		elif iRand == 2:
		#cowgirl
			SceneFuck = scenes.SceneCowgirl(sHisName = sHisName, sHerName = sHerName, Location = Location)
			SceneOrgasm = scenes.SceneCreamPie(sHisName = sHisName, sHerName = sHerName, Location = Location)
		
		elif iRand == 3:
		#doggy 
			SceneFuck = scenes.SceneDoggy(sHisName = sHisName, sHerName = sHerName, Location = Location)
			SceneOrgasm = scenes.SceneCreamPie(sHisName = sHisName, sHerName = sHerName, Location = Location)
		else:
		#missionary
			SceneFuck = scenes.SceneMissionary(sHisName = sHisName, sHerName = sHerName, Location = Location)
			SceneOrgasm = scenes.SceneFacial(sHisName = sHisName, sHerName = sHerName, Location = Location)
		
		sTweet = SceneFuck.Scene() + " " + SceneOrgasm.Scene() + "\n\n"
		sTweet += self.AfterSexPunchline.GetPunchline(exutil.Gender.Male)

		return sTweet
		
class Generator52(Generator):
	ID = 52
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Actions = []
		
		Interruptors = WordList(["mom", "mother", "dad", "daddy", "aunt", "grandma", "grandpa", "husband", "boyfriend", "fiancé", "brother", "step-brother", "sister", "step-sister", "brother-in-law", "baby-sitter"])
		
		Colors = WordList(["pink", "lavender", "mauve", "crimson", "sky-blue", "foam-green", "rose-colored", "maroon", "peach-colored", "teal", "periwinkle-colored", "violet"])
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = sHisName + " and " + sHerName + " tumbled onto the " + WordList(["thick", "frilly", "downy", "florid"]).GetWord() + " " + Colors.GetWord() + " bedspread together"
		if CoinFlip():
			sTweet += ", scattering " + Colors.GetWord() + " pillows everywhere"
		sTweet += ". "
		
		sInterruptText = "Suddenly, there was a pounding on the bedroom door. 'What are you two doing in there?' demanded " + WordList(["a muffled", "an angry", "a suspicious", "a loud"]).GetWord() + " voice.\n\n'" + self.Exclamation.GetWord(bSad = True).capitalize() + " It's my " + Interruptors.GetWord() + "!' she said to him. "
		
		sText = ""
		
		# Done-to-her
		sText = ""
		Scene1 = None 
		Scene1 = SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_PEN, exutil.TAG_CLIMAX},)
		#print("\n))) Generator sHisName = " + sHisName + " and sHerName = " + sHerName + ", but for Scene 1 HisName = " + Scene1.HisName + ", HerName = " + Scene1.HerName + " (((")
		if exutil.TAG_ABOVE_BELT in Scene1.Tags:
			sText += "She giggled and playfully struggled with him as he tried to " + WordList(["unbutton her blouse", "pull her top down", "pull her shirt up", "pull the straps of her dress down"]).GetWord() + ". "
		elif exutil.TAG_BELOW_BELT in Scene1.Tags:
			sText += "She giggled and playfully fought him as he tried to " + WordList(["unzip her bluejeans", "pull her skirt down", "pull her panties off", "slide her shorts down"]).GetWord() + ". "
		else:
			sText += "He began urgently undressing her. "

		if not Scene1 is None:
			sText += Scene1.Scene() + "\n\n"
			sText += sInterruptText
			sText += "'It's okay!' she called, '" + sHisName + " was only " + Scene1.VerbGerund + " me!'"
			
			for _ in range(3):
				Actions.append(sText)
		#==================
		
		# Both equally
		sText = ""
		Scene2 = None
		Scene2 = SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, NotTags = {exutil.TAG_PEN, exutil.TAG_DONE_TO_HER, exutil.TAG_DONE_TO_HIM, exutil.TAG_CLIMAX})
		#print("\n))) Generator sHisName = " + sHisName + " and sHerName = " + sHerName + ", but for Scene 2 HisName = " + Scene2.HisName + ", HerName = " + Scene2.HerName + " (((")
		sText += "They were giggling and hushing each other as they " + WordList(["tore each other's clothes off", "stripped down to their underwear"]).GetWord() + ". "

		if not Scene2 is None:
			sText += Scene2.Scene() + "\n\n"
			sText += sInterruptText
			sText += "'It's okay!' she " + WordList(["called", "called out", "shouted", "yelled", "shouted out"]).GetWord() + ", 'We were only " + Scene2.VerbGerund + "!'"
			
			for _ in range(3):
				Actions.append(sText)
		#==================
		
		# Done-to-him
		sText = ""
		Scene3 = None
		Scene3 = SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, Tags = {exutil.TAG_DONE_TO_HIM}, NotTags = {exutil.TAG_PEN, exutil.TAG_CLIMAX})
		#print("\n))) Generator sHisName = " + sHisName + " and sHerName = " + sHerName + ", but for Scene 3 HisName = " + Scene3.HisName + ", HerName = " + Scene3.HerName + " (((")
		if exutil.TAG_ABOVE_BELT in Scene3.Tags:
			sText += "He laughed as she tried to " + WordList(["wrestle his t-shirt off of him", "unbutton his shirt",]).GetWord() + ". "
		elif exutil.TAG_BELOW_BELT in Scene3.Tags:
			sText += "He laughed as she tried to " + WordList(["unzip his bluejeans", "unbutton his trousers", "unbuckle his belt", "pull his shorts down", "slide his boxers down", "slide his briefs down"]).GetWord() + ". "
		else:
			sText += "She began tearing his clothes off. "
		
		if not Scene3 is None:
			sText += Scene3.Scene() + "\n\n"
			sText += sInterruptText
			sText += "'It's okay!' she called, 'I was only " + Scene3.VerbGerund + " " + sHisName + "!'"
			
			for _ in range(1):
				Actions.append(sText)
		#==================
		
		if len(Actions) > 0:
			sTweet += Actions[randint(0, len(Actions) - 1)]

		return sTweet
		
#generator for testing scenes 
class Generator53(Generator):
	ID = 53
	Priority = 2
	Type = exutil.GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		# sHisName = self.MaleName.FirstName()
		# sHerName = self.FemaleName.FirstName()
		
		# Location = locations.LocationSelector().Location()
		# MyScene = scenes.SceneRimjobHim(sHisName = sHisName, sHerName = sHerName, Location = Location)
		
		# sTweet = Location.BeginDesc + " "
		
		# sTweet += MyScene.Scene()
		#sTweet += "\n\n" + TitFuckScene.ShortScene()
		
		#sTweet += "AddArticles('excited, beautiful face'): " + AddArticles('excited, beautiful face') + "\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(3,sDivideChar = ';') + ". [3/any]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(4,sDivideChar = ';') + ". [4/any]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(5,sDivideChar = ';') + ". [5/any]\n"
		# sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(3,sDivideChar = ',',bAllowLongDesc = False) + ". [3/short]\n"
		# sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(4,sDivideChar = ',',bAllowLongDesc = False) + ". [4/short]\n"
		# sTweet += "She had " + self.FemBodyParts.DescRandomClothedBodyParts(5,sDivideChar = ',',bAllowLongDesc = False) + ". [5/short]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(3,sDivideChar = ';') + ". [3/any]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(4,sDivideChar = ';') + ". [4/any]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(5,sDivideChar = ';') + ". [5/any]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(3,sDivideChar = ',',bAllowLongDesc = False) + ". [3/short]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(4,sDivideChar = ',',bAllowLongDesc = False) + ". [4/short]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(5,sDivideChar = ',',bAllowLongDesc = False) + ". [5/short]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(4,sDivideChar = ',',bAss = True) + ". [4/bAss=True]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(5,sDivideChar = ',',bPussy = True) + ". [5/bPussy=True]\n"
		sTweet += "She had " + self.FemBodyParts.DescRandomNakedParts(5,sDivideChar = ',',bPussy = True,bAss = True) + ". [5/bAss&bPussy=True]\n"
		
		return sTweet
		
# 'Gosh, Eduardo,' Tonya panted. 'I need you right now. I want you to pull my panties off, bend me over, 
# spank my trim backside, and then fill me with your big fucking love-meat. Bang my cherry, velvet, 
# glazed entrance until you squirt inside it. I need you to fill me with your delicious, tasty, glossy 
# cream, right here, right now, at the gym!'
class Generator54(Generator):
	ID = 54
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "'" + self.Exclamation.GetWord(bExMk = False).capitalize() + ", " + sHisName + ",' " + sHerName + " " + self.VMoan.Past() + ". "
		if CoinFlip():
			sTweet += "'I need you right now. I want you to pull my " + Location.FemaleBottomClothing + " off, spread my " + self.FemBodyParts.Legs.MediumDescription() + " and " + WordList(["fill me", "stuff me", "impale me", "enter me"]).GetWord() + " with your big " + self.MaleBodyParts.Penis.RandomDescription() + ". "
		else:
			sTweet += "'I need you right now. I want you to pull my " + Location.FemaleBottomClothing + " off, bend me over, spank my " + self.FemBodyParts.Ass.MediumDescription() + ", and then " + WordList(["fill me", "stuff me", "impale me", "enter me"]).GetWord() + " with your big " + self.MaleBodyParts.Penis.RandomDescription() + ". "
		
		sTweet += self.VThrust.Present().capitalize() + " my " + self.FemBodyParts.Vagina.RandomDescription() + " until you " + self.VEjac.Present() + " inside it. I need you to fill me with your " + self.Semen.RandomDescription(bAllowShortDesc = True) + ", right here, right now, " + Location.NamePrep + "!'"
		return sTweet

class Generator55(Generator):
	# 'No,' thought Nora, 'I can never forgive Brad for sleeping with my twin sister. I have to cut him out of my life 
	# once and for all. No more will I stare at his picture. No more will I think about his lengthy, virile beef snake. 
	ID = 55
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		VDrip = verbs.VerbDrip()
		
		Fantasies = WordList(["rugged jaw", "broad chest", "brawny shoulders", "full lips", "silken blonde hair", 
							  "chiseled abs", "tanned skin", "tall, handsome build", "soulful blue eyes"])
		sFantasy1 = Fantasies.GetWord()
		sFantasy2 = Fantasies.GetWord(NotList = [sFantasy1])
		
		sTweet = "'No,' thought " + sHerName + ", 'I can never forgive " + sHisName + " for "
		sTweet += WordList(["fucking my twin sister", 
							"having anal sex with my step-mom", 
							"rimming my best friend", 
							"drilling the entire cheerleading squad",
							"suggesting we have a threesome with my sister",
							"spooning naked with my sister", 
							"stepping on my cat", 
							"refusing to go down on me", 
							"drop-kicking my Pomeranian",
							"playing Fantasy Football on our anniversary", 
							"finger-banging his secretary", 
							"what happened during the threesome", 
							"what happened during the orgy",
							"fingering his step-daughter's butt-hole",
							"showing up drunk to the Bat Mitzvah", 
							"asking me to get implants", 
							"giving me a wet willy", 
							"mistaking my twin sister for me in the shower",
							"getting that full-body tattoo", 
							"giving me that awful tattoo", 
							"telling my ex I was into water sports",
							"giving the pool boy a blowjob", 
							"getting an erection during church",
							"calling my mother a fat whore", 
							"titty-fucking my best friend",
							"sexting my sister", 
							"showing everyone those pictures", 
							"letting my labradoodle escape", 
							"refusing to marry me",
							"suggesting I get breast implants", 
							"ruining my favorite dress with semen stains", 
							"puking in my mom's spaghetti",
							"shaving his chest hair", 
							"shaving his pubes",
							"putting it in the wrong hole",
							"wearing my lingerie", 
							"farting in my face during sex", 
							"using my favorite panties as a cum rag",
							"showering with the neighbor",
							"investing our savings in Bitcoin", 
							"what he did in the sauna with Raoul", 
							"forgetting our three-month anniversary",
							"refusing to eat my ass", 
							"getting cum in my eye at church",
							"not being able to find my clitoris", 
							"what he wrote in my yearbook", 
							"staring at my mom's tits", 
							"using my vibrator without telling me",
							"giving me chlamydia", 
							"calling me 'Karen' in bed", 
							"buying me a Nickleback album for my birthday",
							"shaving my maltipoo", 
							"dying my pubes purple", 
							"unfollowing me on Facebook",
							"sharing my mom's nude selfies online",
							"giving the Uber driver a blowjob",
							"eating out that bikini model", 
							"calling them my 'piss-flaps'", 
							"calling them my 'meat balloons'",
							"calling my mother 'a raging thunder-cunt'", 
							"putting it in my pooper"]).GetWord() + ". "
		sTweet += WordList(["I have to cut him out of my life once and for all.", 
							"This time we are really through.",
							"This time he has gone too far. We are finished.",
							"I never want to see him again, ever.",
							"I have to let him go, once and for all."]).GetWord() + " "
		sTweet += "No more will I stare at his picture. I must forget about his "
		sTweet += sFantasy1 + ", " + sFantasy2 + ", "
		
		if CoinFlip():
			#penis
			sTweet += "and his " + self.MaleBodyParts.Penis.FloweryDescription(bAddLen = True)
			if CoinFlip():
				sTweet += " and the way " + self.Semen.RandomDescription() + " " + VDrip.Past() + " from its " + self.MaleBodyParts.Penis.Head.FloweryDescription() 
		elif CoinFlip():
			#testicles
			sTweet += "and his " + self.MaleBodyParts.Penis.FloweryDescription(bAddLen = True) + " and his "
			sTweet += self.MaleBodyParts.Penis.Testicles.FloweryDescription()
		elif CoinFlip():
			#ass
			sTweet += Fantasies.GetWord(NotList = [sFantasy1,sFantasy2]) + ", and his " + self.MaleBodyParts.Ass.FloweryDescription()
		else:
			#sexing 
			sTweet += self.MaleBodyParts.Ass.FloweryDescription() + ", "
			sTweet += "and the way he " + WordList(["fucked me on the kitchen table",
												   "bent me over the billiard table and fucked me",
												   "fucked me on top of a grand piano",
												   "pulled my hair when he did me doggy-style",
												   "fucked me on my parents waterbed",
												   "would spurt his load all over my tits",
												   "would make love to me while we listened to Nickleback",
												   "would nibble my sensitive nipples",
												   "looked when he fucked me that one night at the gym",
												   "went down on me in the back of an Uber",
												   "looked having sex with that guy from Craigslist",
												   "fingered me at last summer's pool party",
												   "pushed me up against the wall and fingered my pussy",
												   "made love to me in the janitor's closet in high school"]).GetWord()

			
		sTweet += ".\""
		
		return sTweet
		
class Generator56(Generator):
	ID = 56
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName1 = self.FemaleName.FirstName()
		sHerName2 = self.FemaleName.FirstName()
		
		while sHerName1 == sHerName2:
			sHerName2 = self.FemaleName.FirstName()
		
		sHerSkinHair1 = WordList(['blonde', 'brunette', 'redhead', 'Asian', 'black girl', 'latina']).GetWord()
		sHerSkinHair2 = WordList(['blonde', 'brunette', 'redhead', 'Asian', 'black girl', 'latina']).GetWord(NotList = [sHerSkinHair1])

		SceneForeplay = SceneSelector().GetScene(Tags = {exutil.TAG_FOREPLAY}, sHisName = sHisName, sHerName = sHerName2)
		ScenePosition = SceneSelector().GetScene(Tags = {exutil.TAG_POSITION}, sHisName = sHisName, sHerName = sHerName2)
		
		sTweet = "'Oh " + sHerName1 + ", baby,' said " + sHisName + " to the vivacious " + sHerSkinHair1 + " lying naked next to him, 'You're so sexy.' He " + WordList(['gently', 'tenderly', 'delicately', 'softly']).GetWord() + " carressed " + sHerName1 + "'s "
		Parts = self.FemBodyParts.GetRandomIntimateParts(iNum = 3, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and her " + part + "."
		sTweet += "\n\nA long arm snaked around and grabbed his " + self.MaleBodyParts.Penis.FloweryDescription() + "."
		sTweet += "\n\n'I haven't forgotten about you, " + sHerName2 + ",' " + sHisName + " said, turning to the sumptuous " + sHerSkinHair2 + " lying on the other side of him. "
		if CoinFlip():
			sTweet += SceneForeplay.Scene() + "\n\n"
		else:
			sTweet += ScenePosition.Scene() + "\n\n "
		sTweet += "'Hey!' complained " + sHerName1 + ", 'don't forget about me!'\n\n"
		
		Swears = WordList(["Oh God", "Fuck", "Jesus"])
		sTweet += "'" + Swears.GetWord() 
		sTweet += WordList([", mom, wait your turn,' snapped " + sHerName2 + ".",
							", " + sHerName1 + ", can't you wait your turn?' snapped her sister.",
							", " + sHerName1 + ", can't you wait your turn?' snapped her best friend.",
							", " + sHerName1 + ", can't you wait your turn?' snapped her bridesmaid.",
							", " + sHerName1 + ", can't you wait your turn?' snapped her daughter.",
							", " + sHerName1 + ", can't you wait your turn?' snapped her sister-in-law.",
							", " + sHerName1 + ", can't you wait your turn?' snapped her step-daughter."]).GetWord()

		return sTweet
		
class Generator57(Generator):
	ID = 57
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		
		sEjaculated = WordList(["gasped", "exclaimed", "blurted", "burst out"]).GetWord()
		sShockedExclaim = WordList(["Oh fuck", "Shit", "What the fuck", "Holy shit", "Holy fuck", "Holy fucking shit", "Oh shit", "Fuck"]).GetWord()
		
		Face = self.FemBodyParts.Face 
		Ass = self.FemBodyParts.Ass
		Anus = Ass.Anus 
		Breasts = self.FemBodyParts.Breasts
		Nipples = Breasts.Nipples 
		Vag = self.FemBodyParts.Vagina
		Clit = Vag.Clitoris 
		Hips = self.FemBodyParts.Hips
		
		sRelation = WordList(["mom", "dad", "older brother", "step-mom", "step-dad", "sister", "roommate"]).GetWord()
		sToy = WordList(["a curling iron", "a Ken doll", "a spatula", "a banana", "a pickle", "a cucumber", 
						 "a candle", "an electric toothbrush", "my toothbrush", "a rolled up magazine", 
						 "a rolling pin", "a screwdriver", "a baguette", "a shampoo bottle", 
						 "a baseball bat", "my TV remote", "an eggplant", "corn on the cob", "Coke bottle", 
						 "a plunger", "a crucifix", "a toothpaste tube", "a bowling pin", "a broomstick",
						 "my flute", "my clarinet", "my giant foam finger"]).GetWord()
		sHole = Vag.InnerVag.RandomDescription()

		sTweet += sHerName + " flung herself down on the bed. Lifting her hips she " + WordList(["pulled", "slid"]).GetWord() + " down her panties. "
		sTweet += "Then she began to "
		sTweet += WordList(["gently", "tenderly", "vigorously", "energetically", "ardently", "fervently"]).GetWord() + " "
		sTweet += WordList(["massage", "pleasure", "rub", "caress", "stroke", "stimulate", "masturbate", "fondle", "finger"]).GetWord() + " "
		sTweet += "her " + Vag.RandomDescription() + ". She spread apart her " + Vag.OuterLabia.RandomDescription() + " and gently teased her " + Vag.Clitoris.RandomDescription() + ".\n\n"
		sTweet += sHerName + " " + WordList(["reached under her pillow", "felt under the covers", "reached behind the night-stand"]).GetWord() + " and found her favorite object. "
		sTweet += "Carefully, she inserted it into her " + Vag.InnerVag.RandomDescription() + " and then began to "
		sTweet += WordList(["thrust it forcefully and repeatedly into her " + sHole,
							"saw it in and out of her " + sHole, 
							"violently penetrate her " + sHole,
							"impale her " + sHole + " with it",
							"plunge it deep into her " + sHole,
							"use her " + Vag.RandomDescription(bAllowLongDesc = False) + " with it", 
							"wantonly stuff her " + sHole + " with it",
							"grind her " + Vag.RandomDescription(bAllowLongDesc = False) + " on it"]).GetWord() + ".\n\n"
		sTweet += "Suddenly, the door flew open and her " 
		if CoinFlip():
			sTweet += WordList(["older brother", "dad", "step-dad", "step-brother", "step-son"]).GetWord() + " walked in.\n\n"
			sTweet += "\"" + sShockedExclaim + "!\" he " + sEjaculated + ". "
			sTweet += "\"Is that " + sToy + "?!?"
		else:
			sTweet += WordList(["mom", "step-mom", "sister", "step-sister", "college roommate", "best friend"]).GetWord() + " walked in.\n\n"
			sTweet += "\"" + sShockedExclaim + "!\" she " + sEjaculated + ". "
			sTweet += "\"Are you using " + sToy + "?!?\""

		return sTweet
		
class Generator58(Generator):
	ID = 58
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Cock = self.MaleBodyParts.Penis
		Used = []
		
		ShortPenis = WordList(['dick','cock','penis','prick','dong','wiener','dingus','choad','knob','pecker','schlong','johnson','tool','willy','snake','ding-a-ling'])

		sShort1 = ShortPenis.GetWord(NotList = Used)
		Used.append(sShort1)
		sShort2 = ShortPenis.GetWord(NotList = Used)
		Used.append(sShort2)
		
		MediumPenis = WordList(['dick', 'dong', 'Johnson', 'schlong', 'cucumber', 'erection','joystick','hard-on','shaft','pole','phallus','pipe','rod','ramrod','serpent','stalk','manhood','lizard','cock','chubby','piston','disco stick','eggroll','popsicle','boner','sausage','anaconda', 'stiffy', 'beef snake', 'beef bayonet'])
		
		sShort3 = MediumPenis.GetWord(NotList = Used)
		Used.append(sShort3)
		sMedium1 = MediumPenis.GetWord(NotList = Used)
		Used.append(sMedium1)
		
		
		SillyPenis = WordList(['baloney pony', 'custard launcher', 'fire hose', 'fuck-pole', 'hot-rod', 'jade stalk', 'love muscle', 'meat puppet', 'bratwurst', 'meat popsicle', 'pork sword', 'sex salami', 'man cannon', 'bmanhood', 'baby maker', 'skin flute', 'trouser snake', 'third leg', 'tube steak', 'pocket monster', 'one-eyed snake', 'jackhammer', 'rape tool', 'pleasure pump', 'lap rocket', 'knob goblin', 'love lever'])
		
		sMedium2 = SillyPenis.GetWord(NotList = Used)
		Used.append(sMedium2)
		sSilly1 = SillyPenis.GetWord(NotList = Used)
		Used.append(sShort3)
		
		RidicPenis = WordList(['Semen Demon', 'Pocket rocket', 'Sexcalibur', 'Yogurt hose', 'Flesh tower', 'Piss weasel', 'Fudge packer', 'Pink torpedo', 'One-eyed wonder weasel', '$5 footlong', 'Winkie', 'Love burrito', 'Donkey Kong', 'King Dong', 'Steamin\' Semen Roadway', 'Lady dagger', 'Vlad the Impaler', 'Weapon of Ass Destruction', 'Uncle Reamus', 'Puff the One-Eyed Dragon', 'Rumpleforeskin', 'Prince Everhard of the Netherlands', 'Moby Dick', 'Long Dong Silver', 'Cocktapus', 'Clam hammer', 'The Dicktator', 'Jurassic Pork', 'Woody Womb Pecker', 'Russell the Love Muscle'])
		sRidic = RidicPenis.GetWord(NotList = Used)
		
		sActualName = ""
		iRand = randint(1,4)
		if iRand == 1:
			sActualName = "Little " + sHisName
		elif iRand == 2:
			sActualName = sHisName + " Jr." 
		elif iRand == 3:
			sActualName = "Tiny " + sHisName
		else:
			sActualName = "Baby " + sHisName
		
		if CoinFlip():
			sTweet = sHerName + " undid " + sHisName + "'s heavy belt buckle and pulled his blue jeans down his " + WordList(["lean", "bony", "muscular", "narrow", "powerful"]).GetWord() + " hips. "
		else:
			sTweet = sHerName + " unzipped " + sHisName + "'s zipper. "
		sTweet += "\"Ooh, baby, what do we have here?\" she " + WordList(["purred", "cooed", "growled sexily"]).GetWord() + ". \"Is it " + AddArticles("'" + sShort1 + "'") + "? " + AddArticles("'" + sShort2 + "'").capitalize() + "? Maybe it's " + AddArticles("'" + sShort3 + "'") + "!\"\n"
		sTweet += "She began to stroke it up and down. " 
		sTweet += "\"It's growing " + WordList(['bigger','longer','thicker']).GetWord() + " now,\" she said. \"Maybe it's " + AddArticles("'" + sMedium1 + "'") + " or " + AddArticles("'" + sMedium2 + "'") + "?\" "
		sTweet += "She gave the underside of the shaft a long, slow lick with her tongue. "
		sTweet += sHisName + " groaned with pleasure.\n"
		sTweet += "\"Ooh, I know... you call it your '" + sSilly1 + "' don't you? No, I've got it: '" + sRidic + "'!\" "
		sTweet += "He shook his head and moaned. "
		sTweet += "\"Tell me and I'll " + WordList(["suck you off", "deep throat you", "let you cum all over my tongue", "let you throat fuck me", "let you nut in my mouth", "suck your hairy balls", "let you splooge on my tits"]).GetWord() + ", " + sHisName +"!\" she purred.\n"
		sTweet += "\"I just call it my... '" + sActualName + "!'\" he " + WordList(['whispered','whimpered','moaned','groaned','gasped']).GetWord() + "."

		return sTweet
		
# Candice walked stiffly down the stairs, groaning with every step. "Oh god," she said. "That's the last time I
# let a burly Italian construction worker fist my anus!"
class Generator59(Generator):
	ID = 59
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Man = titpeople.MaleChar(iNumMinCBits = 2, iNumMaxCBits = 3, bAllowGang = False, bAddArticle = False,
									bAllowAttitude = False, bAllowGenMod = False, bAllowTrope = False, 
									bAllowMaritalStatus = False, bAllowTitle = False)
		Verbs = WordList(['fist','fist','cream pie','stuff','ream','pound','nail','plow','drill','ram','pop'])
		Anus = self.FemBodyParts.Ass.Anus 
		
		sTweet += self.FemaleName.FirstName() + " walked stiffly down the " + WordList(['stairs','steps','hall','sidewalk','street']).GetWord()
		sTweet += ", groaning with every step. \"" + self.Exclamation.GetWord(bExMk = False, bHappy = False).capitalize() + ",\" " 
		sTweet += "she said. \"That's the last time I let " + AddArticles(Man.Desc).lower() + " " 
		sTweet += Verbs.GetWord() + " my " + Anus.ShortDescription(sNot = 'fissure') + "!\""

		return sTweet
		
# "Wizard!" called out the little bosomy princess in an imperious voice, "I have come for your aid. You must give me a magical 
# talisman with which I can free my younger sister from the Tentacle Beast!" She swept into the room in a long plum gown 
# which left little to the imagination. The Wizard was dazed by the beauty of her full, sweet lips; her yielding flesh; and 
# her pert behind.
#
# "Yes your highness, I have just the thing," he said. He handed her a strange, be-jeweled object. "You must wear this at all 
# times," he said.
# 
# "What is this?" she asked.
#
# "'Tis the legendary anal hook of Devaxatar!"
class Generator60(Generator):
	ID = 60
	Priority = 2 #2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sMage = WordList(['Wizard','Sorcerer','Warlock','Enchanter']).GetWord()
		PrincessAdjs1 = WordList(['young','nubile','beautiful','sexy','virginal','vivacious','ripe','teenage',
								  'little','cute','tender','regal','noble','sumptuous'])
		PrincessAdjs2 = WordList(['pale','black','slender','willowy','curvy','voluptuous','ample-bosomed',
								  'apple-bottomed','full-figured','bosomy','bubble-butt','curvaceous',
								  'jiggling','flexible','nubile','young','ripe','petite','plump',
								  'round-bottomed','Rubenesque','shapely','tender','tight-bodied',
								  'top-heavy','pale','black','black','redheaded','blonde','brunette'])
		sPrincessAdj1 = PrincessAdjs1.GetWord()
		sPrincessAdj2 = PrincessAdjs2.GetWord(NotList = [sPrincessAdj1])
		
		Evils = WordList(["defeat the Dark Lord",
						  "free my younger sister from the Tentacle Beast",
						  "return my father the king to human form",
						  "stop the Goblin King from taking our women",
						  "stop the evil queen from stealing the seed of the kingdom's young men",
						  "free my sister from the horny dragon",
						  "free my sister from the horny barbarian horde",
						  "free the queen from the horny barbarian horde",
						  "restore the queen's virtue",
						  "restore my sister's virtue",
						  "free the village women from Marfang's wicked sex dungeons",
						  "free the queen from the humiliating mind control spell",
						  "free my father the king from the Curse of Eternal Horniness",
						  "free my brother the prince from the Curse of Eternal Horniness",
						  "stop the evil queen from stealing the seed of my brother the prince",
						  "stop the evil queen from seducing my brother the prince",
						  "free my brother the prince from the curse of the everlasting erection",
						  "free my father the king from the curse of the everlasting erection",
						  "stop the libidinous spirits from invading my tender sister's chambers each night",
						  "stop my evil twin brother from making me his bride"])
						  
		DressAdjs = WordList(['long','floor-length','diaphanous','gauzy','revealing','strapless','plunging',
							  'sumptuous','translucent','slinky','form-fitting','daring'])
		DressColors = WordList(['red','crimson','ruby','scarlet','coral','maroon','rose','cerise','fuchsia','garnet','russet','vermillion',
								'cerulean','azure','sapphire','indigo',
								'emerald','sea green','chartreuse','jade','viridian',
								'mauve','violet','lavender','lilac','periwinkle','plum',
								'yellow','lemon','cream','ivory','alabaster','umber',
								'silver','gold'])
								
		sArtifactAdj = WordList(['magical','enchanted','legendary','ancient','arcane','mystic','runic','sorcerous','spellbound']).GetWord()
		sArtifact = WordList(['butt plug','anal beads','dildo','vibrator','ben wa balls','clit clamp','speculum','ball gag',
							  'pony tail anal plug','chastity belt','strap-on','anal hook','nipple clamps','dog collar',
							  'spreader bar']).GetWord()
		sMagicWord = WordList(['Aether','Theophilus','Zanotar','Xholus','Endomius','Sokranos','Devaxatar',
							   'Gorth','Evanora','Locasta','Minerva','Morrigan','Alatar','Gwydion','Ommin',
							   'G','Rasputin','Gloompa','Ishabar','Ashtar','Djinnana','Nimh',
							   'Gongor','Hogfarts','Dogwarts','Glindolf','Dimpledoor','Dirth Vater','Fred']).GetWord()
		
		sTweet += "\"" + sMage.capitalize() + "!\" "
		sTweet += "called out the " + sPrincessAdj1 + " " + sPrincessAdj2 + " princess in " + WordList(['a commanding','a high','an imperious','a thrilling']).GetWord() + " voice, "
		sTweet += "\"I have come for your aid. You must give me a magical talisman with which I can " + Evils.GetWord() + "!\" "
		sTweet += "She swept into the room in a " + DressAdjs.GetWord() + " " + DressColors.GetWord() + " gown which left little to the imagination. "
		sTweet += "The " + sMage + " was " + WordList(['stunned','awed','astounded','dazed','overwhelmed']).GetWord() + " by the beauty of "
		sTweet += self.FemBodyParts.DescRandomNakedParts(iNum = 3, bAss = True, sPossessive = "her") + ".\n\n"
		sTweet += "\"Yes your highness, I have just the thing,\" he said. He handed her a strange, " + WordList(['be-jeweled','gleaming','shiny','lustrous','sparkling']).GetWord() + " object. \"You must wear this at all times,\" he said.\n\n"
		sTweet += "\"What is this?\" she asked.\n\n"
		sTweet +=  "\"'Tis the " + sArtifactAdj + " " + sArtifact + " of " + sMagicWord + "!\""

		return sTweet
		
class Generator61(Generator):
# Sean walked into the bedroom and froze. His husband Desmond was on his knees on the bed, naked. Another 
# man was behind him, his hugely erect flesh-bayonette burrowing passionately between Desmond's naked 
# buttocks with every thrust.
# 'My god, Desmond', he shouted angrily. 'You and your volleyball coach??']
	ID = 61
	Priority = 4
	Type = exutil.GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		
		
		iRand = randint(1,4)
		
		if iRand == 1:
			#Woman cheating on man
			sHisName = self.MaleName.FirstName()
			sHerName = self.FemaleName.FirstName()
			
			MFWBNotList = ['brother-in-law','fiancé','cute roommate','baby daddy','fiancé','boyfriend',
							'husband','daddy','dom','friend-with-benefits','hubby','lord','master',
							'roommate','prince','photographer']
			Cock = self.MaleBodyParts.Penis 
			
			sTweet = sHisName + " walked into the bedroom and froze. His " + self.FemaleSO.GetPerson() + " " + sHerName + " "
			sTweet += "and another man were naked on the bed. She was bouncing up and down on his " + Cock.RandomDescription(bAllowShortDesc = False) + ".\n\n"
			sTweet += "'My god, " + sHerName + "', " + sHisName + " shouted angrily. 'You and your " + self.MFWB.GetPerson(NotList = MFWBNotList) + "??'"
		elif iRand == 2:
			#Man cheating on woman
			sHisName = self.MaleName.FirstName()
			sHerName = self.FemaleName.FirstName()
			
			FFWBNotList = ['soccer mom','one true love','dominatrix','fiancé','cute roommate','girlfriend',
							'mother-in-law','next-door neighbor','roommate\'s girlfriend','wife']
			Breasts = self.FemBodyParts.Breasts 
			sVerbed = WordList(["rode","pistoned into","fucked","drilled","pounded","bored into","hammered","impaled","ploughed","ravished","stuffed"]).GetWord()
			
			sTweet = sHerName + " walked into the bedroom and froze. Her " + self.MaleSO.GetPerson() + " " + sHisName + " "
			sTweet += "was on the bed between the legs of a naked woman. Her " + Breasts.RandomDescription(bAllowShortDesc = False) + " " 
			sTweet += WordList(['bounced vigorously','flopped about']).GetWord() + " as he " + sVerbed + " her " + WordList(["passionately","deeply"]).GetWord() + ".\n\n"
			sTweet += "'My god, " + sHisName + "', she shouted angrily. 'You and your " + self.FFWB.GetPerson(NotList = FFWBNotList) + "??'"
		elif iRand == 3:
			#Woman cheating on woman
			sHerName1 = self.FemaleName.FirstName()
			sHerName2 = self.FemaleName.FirstName()
			
			FFWBNotList = ['soccer mom','one true love','dominatrix','fiancé','girlfriend',
							'mother-in-law','next-door neighbor','roommate\'s girlfriend','wife']
			Breasts = self.FemBodyParts.Breasts  
			
			sTweet = sHerName1 + " walked into the bedroom and froze. Her " + self.FemaleSO.GetPerson() + " " + sHerName2 + " "
			sTweet += "was naked on the bed with another woman between her legs. The woman was " 
			sTweet += "finger-banging her so hard that her " + Breasts.RandomDescription(bAllowShortDesc = False) + " were bouncing up and down as she moaned " + WordList(['passionately','huskily']).GetWord() + ".\n\n"
			sTweet += "'My god, " + sHerName2 + "', " + sHerName1 + " shouted angrily. 'You and your " + self.FFWB.GetPerson(NotList = FFWBNotList) + "??'"
			
		else:
			#Man cheating on man
			sHisName1 = self.MaleName.FirstName()
			sHisName2 = self.MaleName.FirstName()
			
			MFWBNotList = ['brother-in-law','fiancé','baby daddy','fiancé','boyfriend',
							'husband','daddy','dom','friend-with-benefits','hubby','lord','master',
							'prince','photographer']
			Cock = self.MaleBodyParts.Penis 
			Ass = self.MaleBodyParts.Ass
			sVerbing = WordList(['pounding','drilling','slamming','burrowing','plowing']).GetWord()
			
			sTweet = sHisName1 + " walked into the bedroom and froze. His " + self.MaleSO.GetPerson() + " " + sHisName2 + " "
			sTweet += "was on his knees on the bed, naked. Another man was behind him, his " + Cock.RandomDescription(bAllowShortDesc = False) + " " 
			sTweet += sVerbing + " " + WordList(["passionately","deeply"]).GetWord() + " "
			sTweet += "between " + sHisName2 + "'s " + Ass.RandomDescription(bAllowShortDesc = False) + " with every thrust.\n\n"
			sTweet += "'My god, " + sHisName2 + "', he shouted angrily. 'You and your " + self.MFWB.GetPerson(NotList = MFWBNotList) + "??'"

		return sTweet
		
# 'Gosh, Eduardo,' Tonya panted. 'I need you right now. I want you to pull my panties off, bend me over, 
# spank my trim backside, and then fill me with your big fucking love-meat. Bang my cherry, velvet, 
# glazed entrance until you squirt inside it. I need you to fill me with your delicious, tasty, glossy 
# cream, right here, right now, at the gym!'
class Generator62(Generator):
	ID = 62
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sUndress = WordList(["rip my panties off","pull my panties down","rip my jeans off",
							 "peel my jeggings off","pull my yoga pants down","pull my dress up",
							 "rip my dress off","pull my skirt down","rip my bikini off",
							 "rip my scanty lingerie off","pull my bikini bottoms down",
							 "rip my pantyhose open","pull my Daisy Dukes down",
							 "pull my thong down"]).GetWord()
					
		sRealLocation = WordList(["this Wendy's","this Shake Shack","Applebee's","this Krispy Kreme",
								  "this CVS Pharmacy","this McDonald's","this Pizza Hut","this Taco Bell",
								  "this Chipotle","Ying's Takeout","the DMV","this gay bar",
								  "this Chili's","this Arby's","Subway Sandwiches",
								  "the registrar's office","the bridal shower","this Bible study",
								  "this AA meeting","Whole Foods","this Dunkin' Donuts","this Starbucks",
								  "Senor Jose's Taco Truck","the public library","the post office",
								  "the conference room","Bob's BBQ","the Apple Store",
								  "our Bat Mitzvah","the PTA meeting"]).GetWord()
		
		sTweet = "'Ohh, " + sHisName + ",' " + sHerName + " " + self.VMoan.Past() + ". "
		if CoinFlip():
			sTweet += "'I want you so bad. I want you to " + sUndress + ", spread my legs and " + WordList(["fill me","stuff me", "impale me","enter me","pound me","ravish me"]).GetWord() + " with your big " + self.MaleBodyParts.Penis.RandomDescription() + ". "
		else:
			sTweet += "'I want you so bad. I want you to " + sUndress + ", bend me over, spank my " + self.FemBodyParts.Ass.MediumDescription() + ", and then " + WordList(["fill me", "stuff me", "impale me", "enter me"]).GetWord() + " with your big " + self.MaleBodyParts.Penis.RandomDescription() + ". "
		
		sTweet += self.VThrust.Present().capitalize() + " my " + self.FemBodyParts.Vagina.RandomDescription()
		
		iRand = randint(1,4)
		if iRand == 1:
			 sTweet += " until you " + self.VEjac.Present() + " inside it. Fill me with your " + self.Semen.RandomDescription(bAllowShortDesc = True) + "!'\n\n"
		elif iRand == 2:
			sTweet += ". Then I want you to " + self.VEjac.Present() + " your " + self.Semen.RandomDescription(bAllowShortDesc = True) + " all over my " + self.FemBodyParts.Breasts.RandomDescription() + "!'\n\n"
		elif iRand == 3:
			sTweet += ". And then I want you to " + self.VThrust.Present() + " my " + self.FemBodyParts.Ass.RandomDescription() + " deep and hard until you " + self.VEjac.Present() + " inside my " + self.FemBodyParts.Ass.Anus.RandomDescription() + "!'\n\n"
		else:
			sTweet += ". Then I want you to " + self.VEjac.Present() + " your " + self.Semen.RandomDescription(bAllowShortDesc = True) + " "
			sTweet += WordList(["all over my face","in my mouth","all over my naked body","down my throat","in my ass","all over my ass","all over my pussy"]).GetWord() + "!'\n\n"
		
		sTweet += "'Excuse me ma'am,' said " + sHisName + ", 'I'm afraid I'm going to have to ask you to leave " + sRealLocation + ".'"
		
		
		return sTweet

# "Oh Quinn!" "Oh Kaitlyn!" The two young lovers writhed naked on the satin covers, their limbs entwined.

# "Your plump backside ignites my loins with ardour!" breathed Quinn.

# "I want you to fill my quim," breathed Kaitlyn. She whimpered as he entered her with his erect rod. Before 
# long, Quinn reached his zenith and pumped his salty seed into her gushing womb.

# "Kaitlyn," he panted, "I want to be with you always!"

# "But you know we cannot," she said, "You're shorter than I am!"
class Generator63(Generator):
	ID = 63
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		bUsedBonus = False 
		iRand = randint(1,4)
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		MaleRelations = WordList(["father","brother","best friend","son","twin brother",
								  "step-brother","step-son","uncle","grandfather","cousin"])
		Occupations = WordList(["Blacksmith","Tanner","Brewer","Woodsman","Fisherman","Baker","Candlemaker",
								"Minstrel","Bricklayer","Jester"])
		Disqualifiers = WordList(["a priest","shorter than I am","a dwarf","an orc"])
		
		sSemenAdj = WordList(['sweet','milky','burning','salty','white hot','silken','virile']).GetWord()
		sSemen = WordList(['seed','seed','cream','jizm','milk','man-milk']).GetWord()
		sPenisAdj = WordList(['stiff','erect','burning','lengthy','throbbing','virile','girthy','lusty']).GetWord()
		sPenis = WordList(['manhood','phallus','member','flesh sword','rod']).GetWord()
		sWombAdj = WordList(['aching','welcoming','fertile','gushing','lusty','yearning']).GetWord()
		
		#Line: exclamations
		sTweet = "\"Oh " + sHisName + "!\" \"Oh " + sHerName + "!\" "
		
		#Line 1
		if CoinFlip():
			sTweet += "The two star-crossed lovers writhed naked on the " + WordList(['silk','satin','velvet']).GetWord() + " "
			sTweet += "covers, their limbs " + WordList(['entangled','intertwined','entwined']).GetWord() 
		else:
			sTweet += "Their lips met as they embraced naked " + WordList(['beneath the trees','in the soft grass','in the shadow of the tower','on softly scented heather','in their secret bower']).GetWord() + ", "
			sTweet += "their " + WordList(['bodies','bodies','flesh','skin']).GetWord() + " " 
			sTweet += WordList(['glistening','gleaming']).GetWord() + " "
			sTweet += "with " + WordList(['sweat','dew','oil']).GetWord()
		sTweet += ".\n\n"
		
		#Line 2
		sPassion = WordList(['passion','desire','ardour','lust','sinful longing']).GetWord()
		if CoinFlip():
			sTweet += "\"My loins are inflamed with " + sPassion + " for you!\" "
		else:
			sTweet += "\"Your " 
			if CoinFlip():
				sTweet += WordList(["very touch","nubile naked body","sweet derrier","plump backside","virgin cherry","sweet little rump","round bottom","wanton manner","shaved twat"]).GetWord() + " "
				sTweet += WordList(['ignites','swells','fires']).GetWord() + " "
			else:
				sTweet += WordList(["pale thighs","taut nipples","wanton ways","wanton curves","womanly delights","dangling labia","succulent tits","erect nipples"]).GetWord() + " "
				sTweet += WordList(['ignite','swell','fire','engorge']).GetWord() + " "
			sTweet += "my loins with " + sPassion + "!\" " 
		sTweet +=  WordList(['whispered','breathed']).GetWord() + " " + sHisName + ". "
		
		if iRand == 1:
			#do bonus line
			sTweet += "He " + WordList(['tenderly','gently','softly']).GetWord() + " "
			sTweet += WordList(['carressed','touched','stroked','kissed','sucked on']).GetWord() + " her "
			sTweet += WordList(['ripe','fulsome','nubile','supple','plump','quivering','budding']).GetWord() + " breasts."
		sTweet += "\n\n"
			
		#Line 3
		if CoinFlip():
			sTweet += "\"" + WordList(['Slay','Take','Ravish','Impale']).GetWord() + " me with your "
			sTweet += WordList(['meat lance','flesh sword','lady dagger','sturdy wood','fuck-staff','flesh serpent','hard wood','man sword','meat pole','man-snake','jizz cannon','man cannon','cream cannon']).GetWord()
			sTweet += "!\" "
		elif CoinFlip():
			sTweet += "\"I want you to fill my " 
			if CoinFlip():
				sTweet += "virgin "
			sTweet += WordList(['womanhood','passage','womb','quim','hole','snatch','sex']).GetWord() + ",\" "
		else:
			sTweet += "\"" + WordList(["My body is", "My young body is", "My loins are", "My virgin body is"]).GetWord() + " "
			sTweet += WordList(['consumed','aching','burning','horny','yearning']).GetWord() + " with " 
			sTweet += WordList(['passion','desire','need','hunger','lust']).GetWord() + " for you, "
			sTweet += WordList(['my sweet','my love','my sweet love','daddy']).GetWord() + ",\" "
		sTweet += WordList(['sighed','gasped','breathed','moaned']).GetWord() + " " + sHerName + ". "
		
		if iRand == 2:
			#do bonus line
			sTweet += "Her " + WordList(['tender','unsullied','secret','womanly','down-thatched','shaven','sinful','lustful','delicate','forbidden']).GetWord() + " "
			sTweet += WordList(['flower was','petals were','nether-lips were','flesh blossom was']).GetWord() + " "
			sTweet += WordList(['wet','moist','glistening','sopping','gushing']).GetWord() + " with the "
			sTweet += WordList(['dew','honey','sweet juices','juices']).GetWord() + " of her desire. "
			
		#Line 4
		if CoinFlip():
			sTweet += "She " + WordList(['gasped','moaned','sighed','cried out','wailed','whimpered']).GetWord() + " "
			sTweet += "as he " + WordList(['entered her','delved into her','thrust into her','defiled her','impaled her']).GetWord() + " "
		else:
			sTweet += "She opened to him and he " + WordList(['eagerly','ardently','vigorously','willingly']).GetWord() + " "
			sTweet += WordList(['thrust','burrowed','delved']).GetWord() + " into her "
		sTweet += "with his " + sPenisAdj + " " + sPenis 
		
		if iRand == 3:
			#do bonus line
			if CoinFlip():
				sTweet += ", as if he would rend her assunder"
			else:
				sTweet += ", parting her tender flesh-curtains"
		sTweet += ". "
			
		#Line 5
		sTweet += "Before long, " + sHisName + " reached his " + WordList(['climax','climax','zenith']).GetWord() + " and "
		if CoinFlip():
			sTweet += "his " + sSemenAdj + " " + sSemen + " " + WordList(['burst','erupted']).GetWord() + " "
			sTweet += "deep within her " + sWombAdj + " womb"
		else:
			sTweet += WordList(['poured','pumped','ejaculated']).GetWord() + " his " + sSemenAdj + " " + sSemen + " "
			sTweet += "into her " + sWombAdj + " womb"
		sTweet += ".\n\n"
		
		#Line 6
		sTweet += "\"" + sHerName + ",\" he panted, "
		sTweet += "\"I want to be with you " + WordList(['forever','always','for eternity']).GetWord() + "!\""
		sTweet += "\n\n"
		
		#Line 7
		sTweet += "\"But you know we cannot,\" she said, \""
		sTweet += WordList(["I am married to your " + MaleRelations.GetWord(),
							  "I am fucking " + names.PlainNamesMale().FirstName() + " the " + Occupations.GetWord(),
							  "I am married to " + names.PlainNamesMale().FirstName() + " the " + Occupations.GetWord(),
							  "I am having " + names.PlainNamesMale().FirstName() + " the " + Occupations.GetWord() + "'s baby",
							  "I am pregnant with your " + MaleRelations.GetWord() + "'s baby",
							  "I am pregnant with the king's baby",
							  "You're my " + MaleRelations.GetWord(),
							  "You're only a poor " + Occupations.GetWord(),
							  "You're a priest",
							  "I'm a nun",
							  "You are shorter than I am",
							  "You're a dwarf",
							  "You're not Jewish"
							]).GetWord()
		sTweet += "!\""
		
		return sTweet
		
class Generator64(Generator):
	ID = 64
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Species = WordList([['minotaur','minotaurs','muscle-bound'],
							['centaur','centaurs','handsome'],
							['cyclops','cylopses','huge'],
							['ogre','ogres','hulking'],
							['half-dragon','half-dragons','scaly'],
							['elf','elves','strange'],
							['dwarf','dwarves','stocky'],
							['gnome','gnomes','little'],
							['goblin','goblins','green-skinned'],
							['hobgoblin','hobgoblins','red-eyed'],
							['bugbear','bugbears','red-eyed'],
							['troll','trolls','hulking'],
							['goat man','goat men','horny'],
							['merman','mermen','glistening'],
							['werewolf','werewolves','hairy'],
							['vampire','vampires','pale'],
							['Martian','Martians','green-skinned'],
							['gargoyle','gargoyles','stone-skinned'],
							['demon','demons','horned'],
							['dark elf','dark elves','pale-skinned'],
							['kobold','kobolds','scaly little'],
							['griffin','griffins','powerful'],
							['cat person','cat people','furry'],
							['yeti','yeties','furry'],
							['sasquatch','sasquatches','hairy'],
							['golem','golems','clay'],
							['leprechaun','leprechauns','mischievous'],
							['gremlin','gremlins','mischievous'],
							['imp','imp','yellow-eyed'],
							['red cap','red caps','red-capped'],
							['incubus','incubi','horned'],
							['faun','fauns','be-hooved'],
							['ent','ents','tree-like'],
							['djinn','djinni','blue'],
							['mothman','mothmen','winged'],
							['angel','angels','winged'],
							['sphinx','sphinxes','mysterious'],
							['ghoul','ghouls','chilling'],
							['orc','orcs','muscular'],
							['weretiger','weretigers','fearsome'],
							['werebear','werebear','massive'],
							['zombie','zombies','decaying'],
							['wraith','wraiths','ghastly']
						]).GetWord()
		sCreatureSingle = Species[0]
		sCreaturePlural = Species[1]
		sCreatureAdj = Species[2]
		
		sGirlType = WordList(['princess','princess','maid','maiden','milk maid','wench']).GetWord()
		GirlAttitudes = WordList(['saucy','cheeky','impertinent','naughty','meddlesome','brazen','bold','feisty'])
		
		sPenisTextures = WordList(["scaly","smooth","lumpy","hairy","fuzzy","feathered","oily","veiny",
								  "glistening","pulsating","glowing","throbbing","warty","pimpled",
								  "rough","spike-studded","sticky","shiny","spiny"
								  ]).GetWord()
		sPenisColors = WordList(["scarlet","orange","green","purple","yellow","jet black","pale","red",
								"bright orange","bright green","dark purple","bright yellow","bright red",
								"varicolored","rainbow-striped",
								"orange-striped","green-striped","purple-striped","yellow-striped",
								"green-spotted","purple-spotted","orange-spotted","yellow-spotted","red-spotted","orange-spotted","black-spotted","white-spotted"
						      ]).GetWord()
		sTipColors = WordList(["scarlet","orange","green","purple","yellow","jet black","pale","red",
							  "bright orange","bright green","dark purple","bright yellow","bright red"]).GetWord(NotList = [sPenisColors])
		sPenisShapes = WordList(["crooked","bulbous","serpentine","narrow","fat","long","drooping",
								 "gnarled","bent","rigid","ridged"]).GetWord()
		sBallAdjs = WordList(["pendulous","extremely low-hanging","massive","engorged","swollen","hairy","warty",
							 "enormous","shiny","veiny","pulsating","glowing","throbbing","pimpled",
							 "spike-studded","gleaming","over-sized","tiny","shrunken","vestigal",
							 "bloated"]).GetWord(NotList = [sPenisShapes])
		sHerName = self.FemaleName.FirstName()
		
		#Line 1
		sTweet = sHerName + " " + WordList(['looked','stared','gazed']).GetWord() + " wide-eyed at the " + sCreatureSingle + ". "
		sTweet += "\""
		
		sTweet += WordList(["Might I ask you something, sir?",
							"Might I be so bold as to ask you a question?",
							"If... if I may sir... may I ask you something?",
							"Would you... do you think you might answer me one question?",
							"May I ask a question about your kind, sir?",
							"Might I inquire about something?",
							"I've always wondered whether " + sCreaturePlural + ", well...",
							"I've always been curious about whether " + sCreaturePlural + ", well..."
						  ]).GetWord()
		sTweet += "\" the " + sGirlType + " said. "
		
		#Line 2
		if CoinFlip():
			sTweet += "\"" 
			sTweet += "You're the first " + WordList([sCreatureSingle,"one"]).GetWord() + " I've ever met!"
		else:
			sTweet += "\""
			sTweet += "I've never met " + AddArticles(sCreatureSingle) + " before!"
		sTweet += "\"\n\n"
		
		#Line 3
		sTweet += "\"" + WordList(["I am as you see me",
								   "I am much like all the others",
								   "I hope I'm everything you imagined",
								   "My kind are scarce in these lands",
								   "My kind are few these days, 'tis true",
								   "My kind mostly prefer to remain unseen"]).GetWord()
		sTweet += ",\" "
		sTweet += WordList(['rumbled','growled','said','laughed','replied','chuckled','purred']).GetWord() + " "
		sTweet += "the " + sCreatureAdj + " " + sCreatureSingle + ". \""
		
		#Line 4
		sTweet += WordList(["Ask","Ask your question","Inquire away","You may ask your question",
							"I'll try my best to answer your question","You may ask",
							"I'll try my best to satisfy your curiosity",
						  ]).GetWord() + ", "
		sWomanAdj = WordList(['little','young','tiny','mortal','human','small','pretty','tasty','lovely'] + GirlAttitudes.List).GetWord()
		sWomanNoun = WordList(['female','creature','thing','woman','girl','human','morsel','woman','nymph']).GetWord(NotList = [sWomanAdj])
		sTweet += sWomanAdj + " " + sWomanNoun + "!\"\n\n"
		
		#Line 5
		if CoinFlip():
			sTweet += "\"" + WordList(["Are... are you like","Do you have parts like",
									   "Are you equipped like","Are you hung as is"]).GetWord() + " "
			sTweet += WordList(['a human man','a mortal man','a human male','a man']).GetWord() + " "
			sTweet += "down there?\" "
		else:
			sPenises = WordList(['cocks','dicks','dongs','pricks','schlongs']).GetWord()
			sTweet += "\"Is it true what they say about " + sCreatureSingle + " " + sPenises + "?\" "
		
		sTweet += "she asked " + WordList(['tremulously','timidly','hesitantly','shyly']).GetWord() + "\n\n"
		
		#Line 6
		sTweet += "\"" + WordList(["See for yourself","Look for yourself","You tell me","Decide for yourself"]).GetWord() + ",\" "
		sTweet += "he replied. He " 
		sTweet += WordList(["unbuckled his belt and pulled down his trousers",
							"opened his trousers",
							"pulled aside his loincloth",
							"tore off his loincloth",
							"lifted his loincloth",
							"tore off his codpiece",
							"pulled off his codpiece"]).GetWord() + ", "
		sTweet += WordList(["revealing","unfurling","exposing"]).GetWord() + " "
		
		sGenitalia = ""
		iRand = randint(1,20)
		
		if iRand % 2 == 0:
		#even 
			sGenitalia += WordList(['two','two','two','three','three','five','a multitude of']).GetWord() 
		else:
		#odd 
			sGenitalia += WordList(['an enormous','a massive','a huge','an oversized','a magnificent',
								'an arm-length', 'an eight-inch', 'a ten-inch', 'an eleven-inch',
								'a twelve-inch', 'a two-foot']).GetWord() 
		
		if iRand %5 == 0:
		#divisible by 5 (5,10,15,20) 
			sGenitalia += " " + sPenisTextures
			
		if iRand %4 == 0:
		#divisible by 4 (4,8,12,16,20)
			sGenitalia += " " + sPenisShapes 
			
		if iRand in [1,2,3,5,7,11,13,17,19]:
		#prime + 1
			sGenitalia += " " + sPenisColors
			
		sGenitalia += " "
		if iRand % 2 == 0:
			sGenitalia += WordList(['cocks','dicks','dongs','members','penises','phalluses','pricks']).GetWord() + " "
			sGenitalia += "sprouting " + WordList(['from his groin','from his crotch','between his legs']).GetWord() 
		else:
			sGenitalia += WordList(['cock','dick','dong','member','penis','phallus','prick']).GetWord() 
				
		if iRand <= 10:
			if iRand % 2 == 0:
				sGenitalia += " " + WordList(["that dangled to his knees",
											  "with a drop of viscous fluid clinging to each cock-hole",
											  "with wisps of smoke escaping each cock-hole",
											  "each with a drop of pre-cum on the tip",
											  "that were all fully engorged",
											  "that all sprang up fully erect",
											  "with a large golden ring around the base of each",
											  "with a ring piercing the flesh beneath each head",
											  "that were oozing a thick, creamy fluid",
											  "that were covered in sorcerous runes",
											  "that were tattooed with strange runes"]).GetWord()
			else:
				sGenitalia += " " + WordList(["that dangled to his knees",
											  "dangling flacidly","hanging limply",
											  "with a drop of viscous fluid clinging to the cock-hole",
											  "with a drop of pre-cum on the tip",
											  "with a wisp of smoke escaping the cock-hole",
											  "that was fully engorged",
											  "which immediately sprang up fully erect",
											  "which immediately began to grow turgid",
											  "with a large golden ring around the base",
											  "with a ring piercing the flesh beneath the head",
											  "that was oozing a thick, creamy fluid",
											  "that was covered in sorcerous runes",
											  "that was tattooed with strange runes"]).GetWord()
		
		if iRand %3 == 0:
		#divisible by 3	{3,6,9,12,15,18)
			if iRand % 2 == 0:
				sGenitalia += ". Each one had " + AddArticles(sTipColors) + " tip"
			else:
				sGenitalia += ". It had " + AddArticles(sTipColors) + " tip"
			
		sGenitalia += ". "
		if CoinFlip():
			sGenitalia += "He had "
			if iRand > 5:
				sGenitalia += WordList(["two","two","two","three","three","four","five","six","eight",
										"at least a dozen"]).GetWord() + " "
				sGenitalia += sBallAdjs + " " + WordList(['ballsacks','bollocks','gonads','testicles']).GetWord()
				sGenitalia += "."
			else:
				sGenitalia += "a single " + sBallAdjs + " "
				sGenitalia += WordList(['ballsack','scrotum','testicle']).GetWord()
				sGenitalia += "."
		
		sTweet += sGenitalia + "\n\n"
				
		#Line 7
		iRand = randint(1,3)
		if iRand == 1:
		#she bends over for him
			Ass = self.FemBodyParts.Ass 
			Vag = self.FemBodyParts.Vagina
			if CoinFlip():
				sTweet += sHerName + " "
			else:
				sTweet += "The " + sGirlType + " "
			sTweet += "turned around, hiked up her skirts, and bent over. "
			sTweet += "She spread apart her " + Ass.RandomDescription() + " "
			sTweet += "with her hands to " + WordList(['reveal','expose','bare','show him','display']).GetWord() + " "
			if CoinFlip():
				sTweet += "her " + Vag.ShortDescription()
			else:
				sTweet += "her " + Ass.Anus.ShortDescription() 
			sTweet += ". \"" + WordList(["Nothing ventured, nothing gained","I can work with that","I've had worse",
										 "Let's see what you can do","Fuck it, I'm horny!",
										 "I want you to pound my filthy holes with that thing!",
										 "Oh daddy, I'm such a horny little slut!",
										 "Put a baby " + sCreatureSingle + " in me, daddy!",
										 "Pull my hair while you fuck me,",
										 "I like to be spanked while I'm getting fucked,",
										 "Promise you'll pull out, okay?",
										 Vag.ShortDescription().capitalize() + " only, no butt stuff,",
										 "Ever fucked a human female?",
										 "Fuck me!",
										 "You showed me yours, now let me show you mine,",
										 "Be gentle, it's my first time,",
										 "I want you to " + WordList(["violate","defile"]).GetWord() + " my " + Ass.Anus.ShortDescription() + ",",
										 "I want you to " + WordList(["violate","defile","deflower"]).GetWord() + " my " + Vag.ShortDescription() + ",",	
										 "Fill my holes with that nasty thing,",
										 "Don't hold back, I like it rough!","At last I've found a real man!",
										 "I've been a naughty little girl, Mr. " + sCreatureSingle + "!",
										 "Pound me like I'm your little " + sCreatureSingle + " bitch,",
										 "Pound me like one of your " + sCreatureSingle	+ " girls!",
										 "Do you " + sCreaturePlural + " like to do it in the pussy or the ass?"
									    ]).GetWord()
			sTweet += "\" she said."
		elif iRand == 2:
		#she goes down on her knees for him
			Tits = self.FemBodyParts.Breasts
			Mouth = self.FemBodyParts.Lips
			Penis = self.MaleBodyParts.Penis
			if CoinFlip():
				sTweet += sHerName + " "
			else:
				sTweet += "The " + sGirlType + " "
			sTweet += "dropped to her knees, opened her " + Mouth.RandomDescription() + " "
			sTweet += "and stuck out her tongue. \"" 
			sTweet += WordList(["Let me suck on it,","Can I have a taste, daddy?",
							    "Fill my mouth with " + sCreatureSingle + " cum,",
								"Cover my tits in " + sCreatureSingle + " cum,",
								"I'll bet I've tasted worse,",
								"Nothing ventured, nothing gained","Try not to get cum in my hair,",
								"I'm thirsty for some " + sCreatureSingle + " " + self.Semen.ShortDescription() + "!",
								"May I please suck it?","Gag me with it!",
								"Don't mind if I do!",
								"Put that " + sCreatureSingle + " " + Penis.ShortDescription() + " in my mouth!",
								"I give " + WordList(['excellent','amazing','incredible']).GetWord() + " head,",
								"Us human girls give excellent head!",
								"Us human females are really good at sucking " + Penis.ShortDescription() + ",",
								"Ever had your " + Penis.ShortDescription() + " sucked by a human?",
								"I've always wanted a taste of " + sCreatureSingle + " " + Penis.ShortDescription() + "!"
							   ]).GetWord()
			sTweet += "\" she said."
		else:
		#she spreads her legs for him 
			Legs = self.FemBodyParts.Legs 
			Vag = self.FemBodyParts.Vagina 
			if CoinFlip():
				sTweet += sHerName + " "
			else:
				sTweet += "The " + sGirlType + " "
			sTweet += "took off her clothes, lay back and spread her " + Legs.RandomDescription() + ". "
			sTweet += "\"" + WordList(["Nothing ventured, nothing gained!","I can work with that!","I've had worse,",
									   "Let's see what you can do,","Fuck it, I'm horny!",
									   "Go slow, I'm a virgin,",
									   "Be gentle, it's my first time,",
									   "I want you in my virgin " + Vag.ShortDescription() + "!",
									   "I'm a " + WordList(['filthy','dirty','naughty']).GetWord() + " " + WordList(['slut','whore']).GetWord() + " for " + sCreaturePlural.lower() + ",",
									   "Won't you pound my " + Vag.RandomDescription() + ", sir?",
									   "Won't you stuff my " + Vag.RandomDescription() + ", sir?",
									   "Now, you're not allowed to cum inside me,",
									   "Can't be worse than my husband,",
									   "Put a baby " + sCreatureSingle + " in me, daddy!",
									   "Promise you'll pull out, okay?",
									   "You showed me yours, now let me show you mine,",
									   "Pound me like I'm your little " + sCreatureSingle + " bitch!",
									   "Do you know what to do with " + AddArticles(Vag.ShortDescription()) + "?",
									   "You're clearly a " + sCreatureSingle + ", but are you also a man?",
									   "Do me like one of your " + sCreatureSingle + " girls!"
									 ]).GetWord()
			sTweet += "\" she said."
		
		return sTweet
		
# "Oh Vicenzo!" she gasped as he nibbled gently on her lush, firm globes. "I must tell you something!"
# "What is it, my sweet?" he asked, squeezing her ripe buttocks.
# "I'm secretly married - to your father!"
class Generator65(Generator):
	ID = 65
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location()
		Scene = SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX,exutil.TAG_PEN}, Location = Location)
		sScene1 = Scene.SceneShortDesc3P
		
		sGerund = self.VForeplay.Gerund()
		sPornoType = WordList(['ass-to-ass','ass-to-mouth','anal gape','public humiliation','gang-bang','interracial gang-bang',
							   'furry','furry gang-bang','interracial anal','double anal penetration']).GetWord()
		
		BodyParts = self.FemBodyParts
		SelectedPart = WordList([BodyParts.Breasts,BodyParts.Breasts.Nipples,BodyParts.Vagina,BodyParts.Vagina.OuterLabia,
							     BodyParts.Vagina.InnerLabia,BodyParts.Ass,BodyParts.Ass.Anus,BodyParts.Thighs,
								 BodyParts.Vagina.InnerVag,BodyParts.Vagina.Clitoris]).GetWord()

		sMaleRelation = WordList(['father','son','brother','best friend','boss']).GetWord()
		sFemaleRelation = WordList(['mother','step-mother','sister','step-sister','step-daughter']).GetWord()
		sSecret = WordList(["I'm secretly married - to your " + sMaleRelation, 
							"I'm pregnant - with your " + sMaleRelation + "'s baby",
							"I had a threesome - with your " + sMaleRelation + " and a hooker",
							"I let your " + sMaleRelation + " ride me bareback - and now I'm pregnant",
							"I slept with your " + sMaleRelation + " - and he gave me chlamydia",
							"Last night your " + sFemaleRelation + " went down on me - and I think I might be a lesbian",
							"Last night I ate your " + sFemaleRelation + "'s pussy - and she came on my face",
							"Last night I went down on your " + sFemaleRelation + " - and now we're getting married",
							"I sucked your " + sMaleRelation + "'s dick - " + Location.NamePrep,
							"I fucked your " + sMaleRelation + " - " + Location.NamePrep,
							"I went down on a woman " + Location.NamePrep + " - and it was your " + sFemaleRelation,
							"I gave a blowjob to a guy " + Location.NamePrep + " - and it was your " + sMaleRelation,
							"Your " + sMaleRelation + " has been inside my ass" ,
							"I let men pee in my mouth - for money",
							"I'm not " + sHerName + " - I'm her twin sister",
							"After last night's game - I let the entire " + WordList(['football team','hockey team','basketball team','bowling team','baseball team']).GetWord() + " ride me bareback",
							"I'm being black-mailed by your " + sMaleRelation + " - for anal sex",
							"The DNA test came back - and it says that I'm your " + WordList(['mother','sister','first cousin','daughter']).GetWord(),
							"Someone leaked a sex tape of me - giving a blowjob to your " + sMaleRelation,
							"Someone leaked a sex tape of me - sixty-nining your " + sFemaleRelation,
							"I lied about being a virgin - I'm having sex with your " + sMaleRelation,
							"I'm not a virgin anymore - I fucked your " + sMaleRelation + " " + Location.NamePrep,
							"I let your " + sMaleRelation + " do my " + WordList(['bunghole','cornhole','dirt-pipe','fart blaster','heinie hole','poop-chute','poop-trap','pooper']).GetWord() + " - and he gave me chlamydia",
							"I'm not really a virgin - your " + sMaleRelation + " rode me bareback",
							"I do porn - and it's " + sPornoType + " porn",
							"I starred in a porno - and it was " + sPornoType + " porn",
							"I starred in a " + sPornoType + " porno - with your " + sFemaleRelation,
							"I'm black-mailing your " + WordList([sMaleRelation,sFemaleRelation]).GetWord() + " - for sexual favors!"
						  ]).GetWord()

		sTweet += "\"Oh " + sHisName + "!\" she " + self.VMoan.Past() + " "
		sTweet += "as " + sScene1 + ". "
		sTweet += "\"I must tell you something!\"\n\n"
		sTweet += "\"What is it, my " + WordList(["sweet","honey muffin","dumpling","bon bon","coco bean","honey pot",
												  "cream puff","lambchop","love muffin","muppet","puddin' pop",
												  "poopsie","darling","smooch pickle","sugar plum","sweat pea",
												  "angel","apple pie","baby girl","boo bear","sugar bunny",
												  "honey bunny","buttercup","cupcake","dove","gum drop","honey bunch",
												  "June bug","lovey dovey","peach","peaches-and-cream","pumpkin",
												  "turtle dove","wifey"
												]).GetWord().title() + "?\" he asked, "
		sTweet += sGerund + " her " + SelectedPart.RandomDescription(bAllowLongDesc = False) + ".\n\n"
		sTweet += "\"" + sSecret + "!\""

		return sTweet

# Raoul rapped on the door and a woman opened it. "I've been waiting for you!" she purred.
# Raoul's jaw dropped open. She was stark naked, with tan skin and perfect lush DD tatas. A clit piercing winked at him
# between her legs. 
# "Ah, here's your deep-dish pizza with banana peppers and double meat," he stammered. 
class Generator66(Generator):
	ID = 66
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		
		sPizzaType = WordList(['deep dish','extra-large','stuffed crust']).GetWord()
		PizzaMeatToppings = WordList(['beef','meatballs','pepperoni','sausage','salami','hot dog', 'meat lovers'])
		PizzaExtraToppings = WordList(['eggplant','anchovies','banana peppers','broccoli','garlic','jalapeno peppers','onions','pineapples','spinach','parmsesan cheese'])
		PizzaBonus = WordList(['double cheese','double meat','cheesy breadsticks','sausage on the side','creamy ranch dressing'])
		
		sPizza = sPizzaType + " " + PizzaMeatToppings.GetWord() + " pizza with " + PizzaExtraToppings.GetWord() + " and " + PizzaBonus.GetWord()
		
		WomanBody = self.FemBodyParts 
		WomanSkin = self.FemBodyParts.Skin 
		WomanTits = self.FemBodyParts.Breasts
		WomanNips = self.FemBodyParts.Breasts.Nipples
		WomanLegs = self.FemBodyParts.Legs 
		WomanAss = self.FemBodyParts.Ass 
		WomanPussy = self.FemBodyParts.Vagina
		
		AssNPs = WordList(['ass','ass','backside','bottom','butt','heinie','rump'])
		AssAdjs = WordList(['broad','bubble-shaped','curvaceous','cute','nubile','pert',
							'plump','ripe','round','shapely','thick','trim','round, full',
							'ripe and round','very shapely','juicy'])
		sAss = AssAdjs.GetWord() + " " + AssNPs .GetWord()
		
		NippAdjs = WordList(['chocolate','dark','enormous','erect','inch-long','eraser','pert','perky',
							  'puffy','rosebud','rose-colored','stiff','succulent','swollen','tiny',
							  'wide','large'])
							  
		BreastAdjs = WordList(['bouncy','bountiful','double-D','enormous fake','full','heavy','jiggling',
								'juicy','luscious','lush','magnificent','nubile','pendulous','perky','pert',
								'petite','plump','proud','ripe','ripe, nubile','round','statuesque','stunning',
								'sumptuous','supple','swollen','voluptuous','full, pendulous','small, perky',
								'bouncy double-D', 'fake double-D','large, jiggling','big juicy','tight',
								'grapefruit-sized','ripe, swelling','heavy, juicy','heavy, luscious',
								'round, heavy','pillowy'])
								
		PussyAdjs = WordList(['bare','dewy','downy','down-thatched','fat','fat','flushed',
								   'fur-lined','girlish','hairless','lush','naked','peach-fuzzed','pink',
								   'plump','puffy','shameless','shaved','shaven','silken','slick',
								   'smooth','sweet','swollen','tender','lewd','tight'])
		
		SkinAdjs = WordList(['bronzed','freckled','pale','glistening','porcelain','flawless','sun-kissed',
							 'youthed','tanned', 'creamy'])
							 
		LegsAdjs = WordList(['athletic','coltish','elegant','graceful','lithe','long','long',
							 'muscular','shapely','smooth','smooth-shaven','toned'])
		
		sTweet = sHisName + " " + WordList(['rapped','knocked','banged']).GetWord() + " on the door and "
		sTweet += "a " + WordList(['redheaded','blonde','brunette']).GetWord() + " woman opened it. "
		#sTweet += "\"I've been waiting for you!\" she " + WordList(['purred','purred','growled','growled','said throatily','moaned']).GetWord() + ".\n\n"
		sTweet += "She " + WordList(['was stark naked','was buck naked','was completely naked',
									 'was in nothing but her birthday suit','wasn\'t wearing a stitch of clothing',
									 'had no clothes on','was stripped to the skin',
									 'wearing nothing but a pair of red heels',
									 'was shamelessly naked']).GetWord() 
		sTweet += ". "
		
		iRand = randint(1,6)
		
		if iRand == 1:
			sTweet += "His wide eyes took in every inch of her bare, " + SkinAdjs.GetWord() + " skin, " 
			sTweet += "from her " + BreastAdjs.GetWord() + " " + WomanTits.ShortDescription() + " "
			sTweet += "down to her " + LegsAdjs.GetWord() + " legs "
			sTweet += "and the " + WordList(['patch of dark pubes','trim triangle of pubes',
											 'thatch of soft pubes','curly pubes', 
											 'peach-fuzzed pubic mound']).GetWord() + " "
			sTweet += "nestled between them."
		elif iRand == 2:
			sPussyAdj1 = PussyAdjs.GetWord() 
			sTweet += "Her " + AssNPs.GetWord() + " was " + AssAdjs.GetWord() + " "
			sTweet += "and her " + WomanTits.ShortDescription() + " " + BreastAdjs.GetWord() + ". "
			sTweet += "Her " + WomanPussy.ShortDescription() + " was " + sPussyAdj1 + " and " + PussyAdjs.GetWord(NotList = [sPussyAdj1]) + ". "
			sTweet += "She had steel rings piercing her " + NippAdjs.GetWord() + " nipples. "
		elif iRand == 3:
			sTweet += "He had never seen a woman with such "
			sTweet += BreastAdjs.GetWord() + " " + WomanTits.ShortDescription() + " "
			sTweet += "or such " + WomanLegs.MediumDescription() + ". "
			sTweet += "He could clearly see her " + PussyAdjs.GetWord() + " " + WomanPussy.ShortDescription() + ". "
			sTweet += "It looked good enough to eat. "
			sTweet += "For that matter, so did her " + AssAdjs.GetWord() + " " + WomanAss.ShortDescription() + ". "
		elif iRand == 4:
			sLegsAdj1 = LegsAdjs.GetWord()
			sTweet += "She was young and her body was extremely fit. "
			sTweet += "Her " + WordList(['small','petite','budding','pert','perky','nubile','ripe']).GetWord() + " "
			sTweet += WordList(['breasts','tits','titties','boobs']).GetWord() + " "
			sTweet += "were high and tight. "
			sTweet += "Her legs were " + sLegsAdj1 + " and " + LegsAdjs.GetWord(NotList = [sLegsAdj1]) + " "
			sTweet += "and her " + WomanAss.ShortDescription() + " " + AssAdjs.GetWord() + "."
		elif iRand == 5:
			sBreastAdj1 = BreastAdjs.GetWord()
			sAssAdj1 = AssAdjs.GetWord()
			sPussyAdj1 = PussyAdjs.GetWord()
			sTweet += "His jaw dropped at the sight of her smooth, " + SkinAdjs.GetWord() + " skin, "
			sTweet += "her " + sBreastAdj1 + ", " + BreastAdjs.GetWord(NotList = [sBreastAdj1]) + " " + WomanTits.ShortDescription() + ", "
			sTweet += "her " + sAssAdj1 + ", " + AssAdjs.GetWord(NotList = [sAssAdj1]) + " " + AssNPs.GetWord() + ", "
			sTweet += "and her shameless, " + sPussyAdj1 + ", " + PussyAdjs.GetWord(NotList = [sPussyAdj1]) + " " + WomanPussy.ShortDescription() + ". "
		else:
			sPussyAdj1 = PussyAdjs.GetWord()
			sTweet += "Her nude body was stunning. She had " + BreastAdjs.GetWord() + " " + WomanTits.ShortDescription() + " "
			sTweet += "with " + NippAdjs.GetWord() + " nipples, "
			sTweet += "a " + sAss + ", and her legs were long and " + LegsAdjs.GetWord(NotList = ['long']) + ". "
			sTweet += "She was standing with legs apart "
			sTweet += "and he could clearly see her shameless, " + sPussyAdj1 + ", " + PussyAdjs.GetWord(NotList = [sPussyAdj1]) + " " + WomanPussy.ShortDescription() + " "
			if CoinFlip():
				sTweet += "and the " + WordList(['little folds','purple lips','pink ruffle']).GetWord() + " of her labia dangling from it. "
			else:
				sTweet += "and a shiny metal clit piercing which seemed to wink at him." 
		
		sTweet += "\n\n"
		sTweet += "\"I've been waiting for you!\" she " + WordList(['purred','purred','growled','said in a sultry growl','said throatily','moaned','purred in a sultry voice']).GetWord() + ".\n\n"
		sTweet += "\"" + WordList(["Uhhh","Umm","Er","Ah","Uhhh, ma'am","Uhhh, thank you for choosing Big Dave's Pizza Shack"]).GetWord() + ", "
		sTweet += "here's your " + sPizza + ",\" he said."
		return sTweet
		
# Karina leaned back on the {bed/toilet/bathroom floor}. Her skirt was hiked up over her waist and her panties were 
# wadded up around one ankle. With one hand she tweaked her erect right nipple. With the other she was {plunging 
# {two/three} fingers {or a whole fist} in and out of her {tight pussy/pert asshole} as the naughty scene played out 
# in her imagination. "Ohh, Mr. Jefferson!" she moaned. "You're the best Algebra teacher ever!"
class Generator67(Generator):
	ID = 67
	Priority = 2

	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sPanted = WordList(['panted','gasped','moaned','sighed aloud']).GetWord()
		sHerName = self.FemaleName.FirstName()
		
		Tits = self.FemBodyParts.Breasts 
		Vag = self.FemBodyParts.Vagina
		Ass = self.FemBodyParts.Ass
		
		sTweet = sHerName + " leaned back on " + WordList(['the mattress','the toilet','the bathroom floor',
															   'the gravel hiking trail','the washing machine',
															   'her parents bed','the carpet',
															   'the locker room floor']).GetWord() + ". "
		sTweet += "Her " + WordList(['skirt was hiked up over her waist',
									 'panties were in a wad on the floor',
									 'panties were around one ankle',
									 'clothes were on the floor and she was naked',
									 'cutoff shorts were pulled down around her thighs',
									 'thong was pulled to one side']).GetWord() + ". "
		sTweet += "With her left hand " + WordList(['she tweaked the erect nub of her nipple',
												    'she squeezed her ' + Tits.ShortDescription(),
												    'she rubbed her clit',
												    'she fingered her ' + Ass.Anus.MediumDescription()]).GetWord() + ". "
		sTweet += "With her right " + WordList(['hand she had two fingers in',
												'hand she had three fingers in',
												'she shoved her entire fist deep into',
												'she inserted a steel dildo into',
												'she inserted the handle of her hairbrush deep into',
												'she thrust a 13-inch black dildo deep into']).GetWord() + " "
		sTweet += "her " + Vag.RandomDescription() + " "
		sTweet += "as she lost herself in " + WordList(['lustful','naughty','forbidden','shameless','wanton','filthy',
														'dirty','illicit']).GetWord() + " fantasy."
		sTweet += "\n\n"
		
		if CoinFlip():
			sTweet += "\"Oh " + WordList(['daddy','step-dad','uncle','step-brother','grand-dad']).GetWord() + "!\" "
			sTweet += "she " + sPanted + ", \""
			sTweet += "I've wanted you for so long!\""
		else:			
			sTweet += "\"Oh Mr. " + WordList(['Johnson','Smith','Williams','Wilson','Jones','Jackson','Stevens',
											  'Adams','Walker','Patterson','Jenkins','Long','Lee','Simmons']).GetWord() + "!\" "
			sTweet += "she " + sPanted + ", \""
			sTweet += "You're the best " + WordList(['algebra teacher','English teacher','gym coach',
													 'Sunday School teacher','boss','professor',
													 'guidance counselor','sex ed teacher',
													 'youth pastor','principal','minister']).GetWord() + " "
			sTweet += "ever!\""
							
		
		return sTweet
				
# "We can't tell my husband about this," said {Karen/Bill} to the three naked black sailors that were taking turns pounding
# her ass.
class Generator68(Generator):
	ID = 68
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sMenAdj1 = WordList(['Bearded','Beefcake','Beefy','Brawny','Burly','Chiseled','Hairy','Handsome','Handsome',
							 'Hulking','Hunky','Muscular','Muscular','Mustachioed','Sexy','Strapping','Strong',
							 'Tall','Tattooed',"Donkey-Dicked",'Girthy','Hard','Horse-Cock','Hung','Rock-Hard',
							 'well-endowed','well-hung']).GetWord().lower()
		sMenAdj2 = WordList(['black','black','blonde','copper-tanned','Italian','latino','Scottish',
							 'Scandanavian']).GetWord()
		sMen = WordList(["businessmen","Chippendales dancers","coal miners","construction workers","cops",
						 "cowboys","dwarves","farm hands","football players","frat boys","gangstas",
						 "long haul truckers","lumberjacks","army boys","MMA fighters","plumbers","roadies",
						 "sailors","sumo wrestlers"]).GetWord()
		sNum = WordList(["two","two","three","three","three","four","four","five","ten","twenty","three dozen"]).GetWord()
		sVerb = self.VThrust.Gerund()
		
		if CoinFlip():
		#woman 
			sHerName = self.FemaleName.FirstName()
			
			sTweet += "\"We can't let my husband find out about this,\" said " + sHerName + " to the "
			sTweet += sNum + " " + WordList([sMenAdj1,sMenAdj1 + " " + sMenAdj2,sMenAdj2]).GetWord() + " " + sMen + " "
			sTweet += "that were taking turns " + sVerb + " her "
			if CoinFlip():
				Pussy = self.FemBodyParts.Vagina
				sTweet += Pussy.ShortDescription() 
			else:
				Ass = self.FemBodyParts.Ass
				sTweet += Ass.ShortDescription()
			sTweet += "."
		else:
		#man 
			sHisName = self.MaleName.FirstName()
			Ass = self.MaleBodyParts.Ass
			
			sTweet += "\"We can't let my wife find out about this,\" said " + sHisName + " to the "
			sTweet += sNum + " " + WordList([sMenAdj1,sMenAdj1 + " " + sMenAdj2,sMenAdj2]).GetWord() + " " + sMen + " "
			sTweet += "that were taking turns " + sVerb + " his " + Ass.ShortDescription() + "."

		return sTweet
		
# "Make love to me, Vicenzo!" Delilah said. "Make love to me right here in this Starbucks bathroom! Make love to my 
# sweet wet cunt!"		
class Generator69(Generator):
	ID = 69
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		Location.NamePrep 
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "\"Make love to me, " + sHisName + "!\" " + sHerName + " said. "
		sTweet += "\"Make love to me right now, right here " + Location.NamePrep + "! " 
		
		iRand = randint(1,4)
		
		if iRand == 1:
		#tits
			Tits = self.FemBodyParts.Breasts
			Dick = self.MaleBodyParts.Penis 
			
			if CoinFlip():
				sTweet += "Rub your " + Dick.FloweryDescription() + " all over my " + Tits.RandomDescription() + "!\""
			else:
				sThrust = WordList(['fuck','ravish','thrust into']).GetWord()
				
				sTweet += sThrust.capitalize() + " my " + Tits.RandomDescription() + " with your " + Dick.RandomDescription() + "!\""
		elif iRand == 2:
		#pussy 
			Pussy = self.FemBodyParts.Vagina
			sThrust = self.VThrust.Present()
			
			if CoinFlip():
				sTweet += "Bend me over and "
				sTweet += sThrust + " my " + Pussy.FloweryDescription() + "!\""
			else: 
				sTweet += "Spread my legs and "
				sTweet += sThrust + " my " + Pussy.FloweryDescription() + "!\""
		elif iRand == 3:
		#ass 
			Ass = self.FemBodyParts.Ass
			sThrust = self.VThrust.Present()
			
			sTweet += sThrust.capitalize()  + " my " + Ass.FloweryDescription() + "!\""
		else:
		#asshole 
			Ass = self.FemBodyParts.Ass
			Asshole = self.FemBodyParts.Ass.Anus
			
			sTweet += "Spread my " + Ass.ShortDescription() + " and make love to my " + Asshole.FloweryDescription() + "!\""

		return sTweet
		
# Brad undid his buckle and unzipped pants, freeing his dick. "Suck it," he commanded. Obediently, Sarah wrapped her 
# red lips around his meaty member. "Let's see how deep you can take it," he said. Sarah supressed her gag reflex as 
# she felt his fat fuck-pole going down her throat. Brad began thrusting in and out, fucking her mouth forcefully. 
# Streaks of eyeliner were running down her face. Brad groaned and then began to pump his hot jizz down her throat and
# into her belly.

# Sarah sat bolt upright in the tangled sheets of her bed. "Fuck!" she said. "That was only a dream??"		
class Generator70(Generator):
	ID = 70
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Penis = self.MaleBodyParts.Penis 
		Tip = self.MaleBodyParts.Penis.Head 
		Mouth = self.FemBodyParts.Mouth 
		Semen = self.Semen 
		
		SemenNoun = WordList(['jizm','jizz','load','man-milk','man-seed','seed','semen','semen',
							  'sperm','sperm','splooge','spunk'])
		SemenAdjs = WordList(['creamy','gooey','milky','nasty','oozing','ropy','salty',
							  'sloppy','sticky','thick','warm','white-hot','hot'])
		sSemenNoun1 = SemenNoun.GetWord()
		sSemenNoun2 = SemenNoun.GetWord(NotList = [sSemenNoun1])
		
		sNutsNoun = Penis.Testicles.ShortDescription()
		
		sVCumming = self.VEjac.Gerund()
		
		bAddLenCheck = False 
		
		sTweet = sHisName + " "
		if CoinFlip():
			sTweet += "undid his belt buckle and pulled his dick out of his pants. "
		else:
			sTweet += "unzipped and pulled his pants down. He held his dick in front of her face. "
		sTweet += "\"" + WordList(['Suck it','Suck on it','Take me in your mouth','Suck me off',
								   'Put my ' + Penis.ShortDescription() + ' in your mouth',
								   'Suck on my ' + Penis.RandomDescription(bAllowLongDesc = False),
								   'Service me with your mouth']).GetWord() + ",\" he commanded. "
		sTweet += sHerName + " " + WordList(['obediently','submissively']).GetWord() + " "
		sTweet += "wrapped her " + WordList(['full','red','cherry red','moist','black-painted','scarlet']).GetWord() + " "
		sTweet += "lips around his " + Tip.RandomDescription(bAllowShortDesc = False) + ". "
		sTweet += "\"" + WordList(["Let's see how deep you can take it,",
								   "I want you to gag on it,",
								   "C'mon, choke on it,",
								   "Good girl. Take it deep,",
								   "Take it deep in your throat like a good little slut,",
								   "You want more, don't you little slut?",
								   "I want you to take it all, little cock-sock,"]).GetWord() + "\" he said. "
		sTweet += "She nearly " + WordList(['gagged','choked']).GetWord() + " "
		sTweet += "as he thrust his " + Penis.MediumDescription(bAddLen = True) + " " 
		sTweet += "down her throat. He began fucking her " + WordList(['face','mouth']).GetWord() + " " 
		sTweet += WordList(['forcefully','vigorously','powerfully','furiously','hard']).GetWord() + ". " 
		sTweet += "His " + WordList(['hairy','wrinkled','pendulous']).GetWord() + " "
		if sNutsNoun[-1:] == 's':
			sTweet += sNutsNoun + " were slapping against her chin. "
		else:
			sTweet += sNutsNoun + " was slapping against her chin. "
		sTweet += WordList(['Tears of black eyeliner were dripping down her face.',
							'Saliva was dribbling down it.']).GetWord() + " "
		sTweet += "\n\n"
		sTweet += "\"" + WordList(["I'm cumming!","I'm gonna cum!","Oh fuck I'm cumming!"]).GetWord() + "\" "
		sTweet += "he " + WordList(['gasped','groaned','moaned','cried']).GetWord() + ". "
		sTweet += "She felt him pumping " + SemenAdjs.GetWord() + " " + sSemenNoun1 + " down her throat. "
		sTweet += "She couldn't take it all! She was " + WordList(['choking on','gagging on']).GetWord() + " " 
		sTweet += "his " + sSemenNoun2 + "!\n\n"
		
		sTweet += ". . .\n\n"
		
		sTweet += sHerName + " sat bolt upright in bed. "
		sTweet += "\"" + WordList(["What the fuck!","Oh my god!","Holy shit!","Fuck me!"]).GetWord() + "\" she "
		sTweet += WordList(['gasped','panted','exclaimed','said']).GetWord() + ". "
		
		sTweet += "\"Did I just have a sex dream about "
		sTweet += WordList(["my sister's boyfriend","my best friend's boyfriend","my new step-dad",
							"my pastor","my priest","my step-son","my pool boy","my brother",
							"my English teacher","my biology professor","my father-in-law",
							"my boss","my manager","my mom's boyfriend","my algebra teacher",
							"my accountant","my sister's husband","my brother-in-law",
							"my step-brother","my co-worker","my gym coach","psychiatrist",
							"one of my son's friend","the guy from accounting",
							"one of my students","one of my husband's friends",
							"the IT guy","the drywall installer","the handy man",
							"my biology teacher","my history teacher","my orthodontist",
							"my mom's boyfriend","my daughter's boyfriend","youth pastor",
							"my best friend's husband","my French teacher","my Uber driver",
							"Dr. " + names.RegularLastNames().GetWord(),
							"Mr. " + names.RegularLastNames().GetWord(),
							"Professor " + names.RegularLastNames().GetWord()
							]).GetWord() + "?!?\""
		
		return sTweet
		
 # "Brad," said Sarah as they shared a milkshake, "We've been going together for months now. I've never felt like 
 # this about any other guy before. I love you, and I'm ready to do something special with you, something that I've 
 # never done with any other guy. 
 
 # I want you to fuck my heinie hole."
class Generator71(Generator):
	ID = 71
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		
		sVerb = WordList(['desecrate','defile','do','do','drill','fuck','fuck','fuck','fuck',
						  'impale','jackhammer','nail','pound','pound','pound','ravish','ream','ream',
						  'stuff','stuff','violate','deflower','deflower','cum in','cream-pie','gape',
						  'ass-fuck','rape','fuck the shit out of','butt-fuck']).GetWord()
						  
		sAss = WordList(self.FemBodyParts.Ass.Anus.GetNounList() + ['ass','heinie','rump','tushie','butt']).GetWord(NotList = [sVerb,'knot','bowels'])
		
		#print("\nsVerb = " + sVerb)
		#print("\nsAss = " + str(sAss))
		
		sTweet += "\"" + sHisName + ",\" said " + sHerName + " " + WordList(['earnestly','sincerely','ardently']).GetWord() + " "
		sTweet += "as they " + WordList(['shared a milkshake','sat beneath the starry sky','walked along the river',
										  'walked along the beach','snuggled in front of the fire',
										  'snuggled in front of the television','walked through the park holding hands',
										  'shared a cup of hot choolate','lay on the bed looking up at the ceiling',
										  'sat holding hands','walked hand-in-hand through the park',
										  'held hands at the beach','kissed on the front step'
										]).GetWord() + ", "
		sTweet += "\"We've been " + WordList(['going together','dating','seeing each other','together','going steady']).GetWord() + " "
		sTweet += "for almost " + WordList(["three days","six weeks","four months","six months","eight months","nine months","a year","two years"]).GetWord() + " now. "
		sTweet += "You're not like any guy I've ever " + WordList(['dated','met']).GetWord() + ". "
		sTweet += "I think I'm finally ready.\"\n\n"
		sTweet += "\"Ready for what?\" asked " + sHisName + ".\n\n"
		sTweet += "\"I want you to " + sVerb + " my " + sAss + ".\""

		return sTweet

# Dave walked into the {apartment/house}. "Janet, I'm home!" he announced. 
#
# The bedroom door opened and a woman walked out. She had {sexy body} description and her naked body gleamed with 
# baby oil.
# "Janet's not here," she said. "{And unlike her, I do anal./I guess you'll have to fuck me, instead./
# But she says to tell you Happy Birthday./So are you gonna BE a pussy or EAT a pussy?/So take off your pants
# and let me get to work on that cock./So why don't you get naked and join me in the shower?/It's just you,
# me, and your big cock./It's just you, me, and my twin sister./Just me. And I'm horny and dripping wet./
# But I'll bet my pussy feels as good as hers./So bend me over that couch and put a baby in me./And unlike her,
# I give excellent head./Now pull your pants down so I can suck that cock.
class Generator72(Generator):
	ID = 72
	Priority = 2 #3

	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName() 
		sHerName = WordList(['Alice','Ann','Barbara','Beth','Carol','Christy','Cindy','Cynthia','Darlene',
							 'Debbie','Gladys','Jane','Janet','Jenny','Jill','Joyce','Karen','Kimberly',
							 'Lisa','Marsha','Martha','Nancy','Patricia','Patty','Sarah','Sharon','Sherry',
							 'Susan','Suzie','Tammy','Wendy']).GetWord()
		
		sPenis = self.MaleBodyParts.Penis.ShortDescription()
		sLabia = self.FemBodyParts.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = False)
		
		sTweet = sHisName + " walked into the " + WordList(['apartment','house']).GetWord() + ". "
		sTweet += "\"" + sHerName + ", I'm home!\" he " + WordList(['announced','called out','called','shouted']).GetWord() + ".\n\n"
		sTweet += "The bedroom door opened and " + WordList(['a naked woman','a completely nude woman',
															 'a woman wearing nothing but red heels',
															 'a woman who was completely nude except for a pair of sneakers',
															 'a woman wearing nothing but an open bathrobe',
															 'a woman in a see-thru negligee']).GetWord() + " walked out. "
		sTweet += "She had " 
		sTweet += self.FemBodyParts.DescRandomNakedParts(iNum = 4, bAllowLongDesc = True, sDivideChar = ";", bAss = True, bPussy = True) + ". "
		sTweet += WordList(["She was wearing a clit piercing",
									 "She had a tattoo above her pussy that read '" + WordList(['slut','whore','fuck-hole','fuck me','Daddy\'s Hole']).GetWord() + "'",
									 "He could clearly see her " + sLabia,
									 "Her skin was gleaming with baby oil"]).GetWord() + ".\n\n"
		sTweet += "\"" + sHerName + " isn't here,\" she purred. "
		sTweet += "\"" + WordList(["And unlike her, I do anal.",
								 "I guess you'll have to fuck me, instead.",
								 "But she says to tell you Happy Birthday.",
								 "So are you gonna BE a pussy or EAT a pussy?",
								 "So take off your pants and let me get to work on that " + sPenis + ".",
								 "So why don't you get naked and join me in the shower?",
								 "So it's time to spend some quality time with your " + WordList(['mother-in-law','sister-in-law','step-daughter','housekeeper']).GetWord() + ".",
								 "So why don't you get naked and join me in the shower?",
								 "It's just you, me, and your big " + sPenis + ".",
								 "It's just you, me, and my twin sister.",
								 "Just me. And I'm dripping wet and horny as hell.",
								 "But I'll bet my pussy feels as good as hers.",
								 "So bend me over that sofa and put a baby in me.",
								 "And unlike her, I give excellent head.",
								 "And unlike her, I'm not banging your nextdoor neighbor.",
								 "Now pull your pants down so I can suck that " + sPenis + ".",
								 "Now pull your pants down so I can put that " + sPenis + " in my mouth.",
								 "Just me. And I'm SURE you wouldn't be interested in fucking a pornstar.",
								 "But I'm much more fun than that little whore.",
								 "She'll watch us on the webcam.",
								 "Now do you want to " + self.VSex.Present() + " my " + self.FemBodyParts.Ass.Anus.ShortDescription() + " or not?"
							   ]).GetWord() + "\""
		

		return sTweet

 # "I forbid you to see Chad any more," raged Candy's father.
 #
 # "I'm eighteen now, you can't stop me!" retorted Candy. "I'm going to let Chad anally deflower me in public, and
 # that's final!"
class Generator73(Generator):
	ID = 73
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		
		sTweet = "\"I forbid you from seeing " + sHisName + " "
		sTweet += WordList(["any more","any longer","again","ever again"]).GetWord() + "!\" "
		sTweet += WordList(["raged","roared","yelled","fumed"]).GetWord() + " " 
		sTweet += sHerName + "'s father.\n\n"
		
		sTweet += "\"" + WordList(["I'm eighteen now","I'm a grown woman now","You're not my real dad",
								   "I'm eighteen years old","I'm not a little girl anymore",
								   "I'm 18 now and I can make my own decisions",
								   "I'm an adult and I can make my own decisions"]).GetWord() + ", "
		sTweet += "you can't stop me!\" retorted " + sHerName + ". "
		sTweet += "\"" + sHisName + " and I are in love! "
		sTweet += WordList(["I'm going to let him deflower me in public",
						    "I'm giving him my anal virginity",
							"He's taking my anal virginity",
						    "I'm getting a tattoo of his face on my ass",
						    "I'm getting his name tattooed on my ass",
						    "I'm starring in a porn video with him",
							"I'm starring in the porno he's making",
						    "I'm getting his tattoo of his name on my face",
						    "He's taking my anal virginity at the prom",
						    "I'm getting gang-banged by his " + str(randint(2,20)) + " friends",
						    "I'm getting a full-sized tattoo of his " + self.MaleBodyParts.Penis.ShortDescription(),
						    "I'm getting his name tattooed around my " + self.FemBodyParts.Ass.Anus.ShortDescription(),
						    "I'm trying hardcore bondage with him at the underground sex dungeon",
							"I'm going with him to the underground sex club",
						    "I'm wearing this butt plug with his name carved on it",
						    "I'm getting silicon breast implants",
							"I'm getting a silicon butt implant",
						    "I'm joining the " + WordList(["three","six","seven","ten","two dozen"]).GetWord() + " other wives in his harem",
						    "I'm joining his nudist colony",
						    "I'm joining his weird sex cult",
							"I'm marrying a " + str(randint(45,97)) + "-year old man",
							"I'm marrying a " + str(randint(45,97)) + "-year old man",
							"He is going to deflower me live on the internet",
							"We're having a threesome with a prostitute",
							"We are doing a gangbang together",
							"I'm having a threesome with him and his brother",
							"I'm sleeping with him and his girlfriend",
							"I'm sleeping with him and his wife",
							"I'm getting my clit pierced",
							"I'm getting those labia piercings",
							"I'm getting nipple rings",
							"I'm buying him a motorbike with my college savings",
							"I'm wearing a thong to prom",
							"I'm marrying him so he can get his green card",
							"He's popping my cherry at the prom",
							"We're signing a fifty-year variable-rate mortgage",
							"I'm moving out so I can live with him in his Volkswagon Bus",
							"I'm not wearing my chastity belt anymore",
							"I'm not wearing panties to the club",
							"I'm wearing " + WordList(["a sheer latex bodysuit","a sheer body-stocking","a latex nun outfit",
													   "a transparent latex dress","latex fetish gear",
													   "a red latex dress"]).GetWord() + " to prom"
						   ]).GetWord() + " "
		sTweet += "and that's final!\""

		return sTweet
		
# "Hush, my {love/sweet}," said Ronson. "No one can hear us. You know that the {King/Emperor/Duke} has forbidden 
# anal sex." With that he carefully eased his tumescent meat-snake into her tight pooper.
class Generator74(Generator):
	ID = 74
	Priority = 2

	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "\"" + WordList(['Hush','Quiet',]).GetWord() + " my " + WordList(['love','sweet']).GetWord() + ",\" said " + sHisName + ". "
		sTweet += "\"We must let no one hear us. You know that the " + WordList(['King','Duke','Emperor','Sultan','God-King',
																				 'High Council','Overlord','Queen','Empress',
																				 'Queen Mother']).GetWord() + " "
		sTweet += WordList(["has forbidden all","has outlawed all","has banned all"]).GetWord() + " "
		
		iRand = randint(1,4)
		if iRand == 1:
		#anal sex 
			Dick = self.MaleBodyParts.Penis 
			Ass = self.FemBodyParts.Ass.Anus
			sTweet += "anal sex.\" With that he " + WordList(['carefully','gently','softly']).GetWord() + " "
			sTweet += "eased his " + Dick.FloweryDescription() + " into her " + Ass.RandomDescription()
		
		elif iRand == 2:
		#tit-fucking
			Tits = self.FemBodyParts.Breasts 
			Dick = self.MaleBodyParts.Penis 
			sTweet += "titty-fucking.\" With that he began to " + WordList(['thrust','piston','jackhammer']).GetWord() + " "
			sTweet += "his " + Dick.FloweryDescription() + " "
			sTweet += "between her " + WordList(['large','juicy','enormous','heavy','glorious','heaving',
												 'magnificent','generous','pendulous','plump','ripe',
												 'succulent','voluptuous']).GetWord() + ", " 
			sTweet += "oiled-up " + Tits.ShortDescription() 
			
		 
		elif iRand == 3:
		#oral sex 
			Dick = self.MaleBodyParts.Penis 
			
			sTweet += "oral sex.\" " + sHerName + " nodded. "
			sTweet += "Then she opened her " + WordList(['greedy mouth','full lips','candy-colored lips','red lips',
														 'luscious lips','sensual mouth','sweet little mouth',
														 'cherry lips','succulent lips','innocent mouth']).GetWord() + " and "
			sTweet += "took his " + Dick.FloweryDescription() + " down her throat"
		
		else:
		#fisting 
			sTweet += "fisting.\" With that he began to " + WordList(['carefully','gently','slowly']).GetWord() + " "
			sTweet += "insert his four fingers into her " 
			if CoinFlip():
				Asshole = self.FemBodyParts.Ass.Anus 
				sTweet += Asshole.RandomDescription() 
			else:
				Vag = self.FemBodyParts.Vagina
				sTweet += Vag.RandomDescription()
		
		sTweet += ". "

		return sTweet
		
class Generator75(Generator):
	ID = 75
	Priority = 4

	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Moan = self.VMoan 
		
		Fuckup = WordList(["fucking your twin sister", 
							"having anal sex with your step-mom", 
							"eating your best friend's ass", 
							"drilling the entire cheerleading squad",
							"stepping on your cat", 
							"drop-kicking your Pomeranian",
							"finger-banging my secretary", 
							"finger-banging your sister in the butt-hole",
							"mistaking your twin sister for you in the shower",
							"telling your ex that you liked water sports",
							"giving the pool boy a blowjob", 
							"getting an erection during church",
							"calling your mother a 'fat whore'", 
							"titty-fucking your best friend",
							"sexting with your sister", 
							"showing all my friends those pictures", 
							"sending your best friend my dick pics",
							"letting your labradoodle escape", 
							"suggesting you get breast implants", 
							"puking in your mom's spaghetti",
							"putting it in your pooper without permission",
							"wearing your lingerie", 
							"farting in your face during sex", 
							"using your favorite panties as a cum rag",
							"showering with the hot next-door neighbor",
							"investing our savings in Bitcoin", 
							"what I did in the sauna with Raoul", 
							"refusing to eat your ass", 
							"getting cum in your eye at church",
							"not being able to find your g-spot", 
							"staring at your mom's tits", 
							"puting your vibrator up my ass",
							"giving you chlamydia", 
							"tea-bagging you in your sleep",
							"screwing your maid of honor",
							"fucking all the bridesmaids",
							"calling you 'Karen' in bed", 
							"buying you a Nickleback album for your birthday",
							"shaving your maltipoo", 
							"dying your pubes purple", 
							"sharing your mom's nude selfies online",
							"telling your ex you put a shampoo bottle in your ass",
							"giving the Uber driver a blowjob",
							"eating out that hot bikini model", 
							"getting a handjob from your mother",
							"calling your mother 'a raging thunder-cunt'"])
		
		SceneSelect = SceneSelector()
		Scene1 = SceneSelect.GetScene(Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName)	
		
		sTweet = "Their makeup sex was passionate and intense. "
		sTweet += Scene1.Scene() + "\n\n"
		sTweet += "\"I love you so much, baby,\" he " + Moan.Past() + ", "
		sTweet += "\"Can you ever forgive me for " + Fuckup.GetWord() + "?\""

		return sTweet
		
class Generator76(Generator):
	ID = 76
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Private)
		
		Tits = self.FemBodyParts.Breasts 
		Ass = self.FemBodyParts.Ass 
		
		sTweet += Location.BeginDesc + " "
		sTweet += "The girl " + Location.RemoveFemaleClothing() + ". "
		sTweet += sHisName + " swallowed the lump in his throat.\n\n"
		
		iRand = randint(1,6)
		if iRand == 1:
		#Anal Annie
			sHerName = WordList(['Annie','Anne','Alana','Alice','Alexis','Amber','Amy','Anastasia','Angie','Anita','Annabel','Aria','Ava']).GetWord()
			sTweet += "She turned around, bent over, and spread her " + Ass.RandomDescription() + ", revealing her " + Ass.Anus.RandomDescription() + ". "
			sTweet += "\"Wanna find out why they call me 'Anal " + sHerName + "'?\" she asked."
		elif iRand == 2:
		#Blowjob Betsy
			sHerName = WordList(['Babs','Barbara','Beatrice','Beatrix','Bella','Beth','Betsy','Bianca','Brenda','Brielle','Brigitte','Britney']).GetWord()
			sTweet += "She dropped to her knees and began unbuckling his pants. "
			sTweet += "\"Wanna find out why they call me 'Blowjob " + sHerName + "'?\" she asked."
		
		elif iRand == 3:
		#Hand-job Harriet
			sHerName = WordList(['Harmony','Heather','Heidi','Hailey','Harriet','Hatty','Heaven','Honey','Holly']).GetWord()
			sTweet += "She dropped to her knees and began unbuckling his pants. "
			sTweet += "\"Wanna find out why they call me 'Handjob " + sHerName + "'?\" she asked."
		elif iRand == 4:
		#Deep-throat Donna 
			sHerName = WordList(['Daisy','Dalia','Dani','Danielle','Daphne','Deanna','Delilah','Delores','Donna','Dorothy','Deanna']).GetWord()
			sTweet += "She dropped to her knees and began unbuckling his pants. "
			sTweet += "\"Wanna find out why they call me 'Deep-Throat " + sHerName + "'?\" she asked."
		elif iRand == 5:
		#Facial Fannie
			sHerName = WordList(['Felicity','Fiona','Flora','Francisca','Frida','Fannie','Flo','Florence','Farah']).GetWord()
			sTweet += "She dropped to her knees and began unbuckling his pants. "
			sTweet += "\"Wanna find out why they call me 'Facial " + sHerName + "'?\" she asked."
		else:
		#Tit-job Tanya
			sHerName = WordList(['Tabitha','Tamara','Tammy','Tanya','Tasha','Tawny','Teresa','Terri','Tia','Tiffany','Tilda','Tori','Tracy','Trish']).GetWord()
			sTweet += "She squeezed her " + Tits.RandomDescription(bAllowLongDesc = False) + " together. "
			sTweet += "\"Wanna find out why they call me 'Tit-job " + sHerName + "'?\" she asked."
							
		return sTweet
		
# "Mrs. Philmore!" gasped Todd to his next-door neighbor, "Your bunghole is so tight!"
class Generator77(Generator):
	ID = 77
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		
		LastNames = WordList(names.InnuendoLastNames().List + names.PlainLastNames().List) 
					 
		Women = WordList(["next-door neighbor","best friend's mom","math teacher","chemistry teacher",
						  "biology teacher","sex ed teacher","land lady","boss","new step-mom",
						  "new step-mother","mother-in-law","nurse","friend's mom","girlfriend's mom",
						  "librarian","math tutor","French teacher","Spanish teacher","nanny",
						  "secretary","wedding planner"])
						  
		NaughtyHoles = WordList(['anus','arse-cunt','asshole','backdoor','bunghole','butthole',
								 'butt hole','corn hole','dirt-pipe','heinie hole','poop-chute',
								 'poop-trap','pooper','rectum','coochie','cunny','cunt',
								 'fuckhole','pussy','snatch','twat','vagina','cock-sock',
								 'cunt-hole','fuck-tunnel','honey hole','keyhole','love-tunnel',
								 'vag','cooter','hoo-hah','clam','cupcake','clunge','lady-cave',
								 'sex cave','pie','brown star','bum hole','booty hole',
								 'chocolate pocket','pink pocket','fish taco','arsehole'])
								 
				 
		sTweet = "\"Mrs. " + LastNames.GetWord() + "!\" " + sHisName + " " + WordList(['panted','gasped']).GetWord() + " to his " + Women.GetWord() + ", "
		sTweet += "\"Your " + NaughtyHoles.GetWord() + " feels so tight!\""

		return sTweet

# Woman walks through a public place looking uncomfortable. A man says, "Can I help you with something, miss?"
# "Ggggghhhhhhhuh" she says, as the remote-controlled vibrator in her {ass/pussy} began to buzz again.
class Generator78(Generator):
	ID = 78
	Priority = 3
	
	def GetLetterStr(self, sLetter, iMaxNum):
		sReturn = ""
		iNum = randint (3, iMaxNum)
		for i in range(iNum):
			sReturn += sLetter 
			
		return sReturn 
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		
		Places = WordList([["Starbucks","barista"],
						   ["Applebee's","waiter"],
						   ["office","receptionist"],
						   ["hotel","bellhop"],
						   ["The Gap","salesman"],
						   ["the bank","teller"],
						   ["CVS Pharmacy","pharmacist"],
						   ["Olive Garden","waiter"],
						   ["Barnes & Noble","sales associate"],
						   ["Apple Store", "genius"],
						   ["Whole Foods", "stock boy"],
						   ["Best Buy", "sales associate"],
						   ["gym", "personal trainer"],
						   ["mall", "security guard"],
						   ["store", "sales clerk"],
						   ["restaurant", "waiter"],
						   ["pub","bartender"],
						   ["drug store","sales clerk"],
						   ["movie theater","usher"],
						   ["grocery store", "bag boy"],
						   ["McDonald's","cashier"],
						   ["Red Lobster","waiter"],
						   ["menswear section","sales associate"],
						   ["pool area","lifeguard"],
						   ["men's room","man"],
						   ["men's locker room","man"],
						   ["used car lot","salesman"],
						   ["library","librarian"],
						   ["computer lab","student"],
						   ["shopping center","salesman"],
						   ["pool area","cabana boy"],
						   ["department store","salesman"],
						   ["fancy restaurant","waiter"],
						   ["church","priest"],
						   ["study room","student"],
						   ["student lounge","RA"],
						   ["church","minister"],
						   ["auto-parts store", "sales clerk"],
						   ["doctor's waiting room","male nurse"],
						   ["Wal-Mart","clerk"],
						   ["sporting goods section","sales associate"]]).GetWord()
		
		sPlace = Places[0]
		sMan = Places[1]
						   
		sManDescriptor = WordList(["an earnest","a sandy-haired","a gray-haired","a red-haired","a serious",
								   "a flabby","a pale","a freckled","a teenage","a polite","a young",
								   "a grizzled","a nervous","a harried-looking","a bored","a surprised",
								   "a uniformed","a rumpled-looking","a bearded","a tubby","a tall, awkward",
								   "a sleepy","a startled","a homely","a friendly","a leering","a greasy",
								   "a pimply","a wide-eyed"]).GetWord()
								   
		sFillWords = WordList(["Excuse me", "Uh", "Uhhhh", "Er", "Errrr", "Um", "Ummmm","Ah","Ahhh"]).GetWord()
		sMoveAdjs = WordList(["slowly","gingerly","carefully","hesitantly","nervously","dazedly"]).GetWord()
		sAttitude = WordList(["hoping no one would notice her",
							   "biting her lip",
							   "completely naked",
							   "covering her bare breasts with her arms",
							   "trying desperately to cover her naked body",
							   "her hands clasped over her shaved, dripping-wet pussy",
							   "her hands clenched over her moist, pulsating pussy",
							   "her erect nipples clearly visible through her thin white t-shirt",
							   "wishing she was wearing underwear",
							   "her legs shaking",
							   "biting her lip in agonized pleasure",
							   "red-faced and naked",
							   "red-faced and naked from the waist down",
							   "wearing nothing but red high-heels",
							   "panting slightly",
							   "her face flushed red",
							   "her knees wobbling",
							   "lost in a haze of pleasure",
							   "a trickle of moisture running down her thigh",
							   "a trickle of goo running down her thigh",
							   "trying to avoid eye-contact",
							   "trying to be as quiet as possible",
							   "her hand clasped to her crotch",
							   "as she tried to choke down a moan of pleasure",
							   "biting her tongue to keep from moaning",
							   "hoping no one would notice the damp patch on her crotch",
							   "trying to cover herself as casually as possible",
							   "as she tried to supress another moan"]).GetWord()
		sMoan = WordList(["moaned","whimpered","gasped","panted","cried","shrieked","exclaimed","groaned"]).GetWord()
		sHole1 = WordList(["coochie","pussy","quim","twat","vag","vagina","ass","asshole",
						   "back-passage","backdoor","back passage","butthole","rear entrance",
						   "rectum"]).GetWord()
		sHole2 = WordList(["coochie","pussy","quim","twat","vag","vagina","ass","ass","asshole",
						   "cunt","butt","fuck-hole","tush","butthole","rear","rectum","bum"]).GetWord()
							   
		sTweet = sHerName + " "
		sTweet += "walked " + sMoveAdjs + " "
		sTweet += "through the " + sPlace + ", " 
		sTweet += sAttitude + ".\n\n"
		sTweet += "\"" + sFillWords + ", can I help you miss?\" asked " + sManDescriptor + " " + sMan + ".\n\n"
		
		sExclamation = ""
		if CoinFlip():
		#tell man that she is wearing a vibe  
			sVerb = WordList(["shoved up","stuffed up","jammed up","in","jammed in","inserted up"]).GetWord()
			sTweet += "\"I've got a vibrator " + sVerb + " my " + sHole2 + ",\" she " + sMoan + "." 
		else:
		#nonsense words as vibe buzzes 
			Nonsense = []
			Nonsense.append("Oh God")
			Nonsense.append("O" + self.GetLetterStr("h",5) + " God")
			Nonsense.append("Oh fuck")
			Nonsense.append("Holy shit")
			Nonsense.append("Holy motherfucking shit")
			Nonsense.append("Holy motherfucking s" + self.GetLetterStr("h",5) + self.GetLetterStr("i",9) + "t")
			Nonsense.append("Oh fuck! Baby")
			Nonsense.append("Oh fuck " + self.GetLetterStr("ohfuck",5))
			Nonsense.append("Oh fuck me")
			Nonsense.append("Oh fuck m" + self.GetLetterStr("e",10))
			Nonsense.append("Oh fuck I'm cummin" + self.GetLetterStr("g",8))
			Nonsense.append("Shit! Oh God")
			Nonsense.append("Oh fuck! Ye" + self.GetLetterStr("s",6))
			Nonsense.append("Oh shit! Oh god" + self.GetLetterStr("ohgod",6))
			Nonsense.append("A" + self.GetLetterStr("h",10))
			Nonsense.append("Oh G" + self.GetLetterStr("o",10) + "d")
			Nonsense.append("Sh" + self.GetLetterStr("i",10) + "t")
			Nonsense.append("Oh f" + self.GetLetterStr("u",10) + "ck")
			Nonsense.append("H" + self.GetLetterStr("n",10) + "g")
			Nonsense.append("G" + self.GetLetterStr("u",10) + "hh")
			Nonsense.append("Mmm-h" + self.GetLetterStr("m",10))
			Nonsense.append("N" + self.GetLetterStr("n",5) + self.GetLetterStr("o",5))
			Nonsense.append("Y" + self.GetLetterStr("e",5) + self.GetLetterStr("s",7))
			Nonsense.append("I'm comi" + self.GetLetterStr("n",6) + self.GetLetterStr("g",3))
			
			sExclamation = Nonsense[randint(1,len(Nonsense) - 1)]
			
			sTweet += "\"" + sExclamation + "!\" she " + sMoan + " as the remote-controlled vibrator in her " + sHole1 + " began to buzz again."

		return sTweet
	
# "No! This is so wrong!" protested Todd. 
# "It feels so good though, doesn't it baby?" cooed Sapphire. "Come on. Fuck me hard with that big 7-inch 
# cock of yours. Fill me with your cream."
# "Oh shit. Yes! Yes!!!" moaned Todd. Then he bucked his hips and began to fill his step-mom's asshole with cum.
class Generator79(Generator):
	ID = 79
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sHoney = WordList(['honey','sweetie','sugar','baby']).GetWord()
		sForbiddenLover = WordList(["step-mom","step-mother","mother-in-law","cousin","step-sister",
								"adopted sister","sister-in-law","sister-in-law","girlfriend's mom",
								"girlfriend's sister","girlfriend's twin sister","step-daughter",
								"math teacher","English teacher","boss","boss's wife",
								"daughter's best friend","wife's best friend","brother's girlfriend",
								"father's girlfriend","son's girlfriend","nextdoor neighbor",
								"babysitter","brother's wife"]).GetWord()
		
		Vag = self.FemBodyParts.Vagina 
		Anus = self.FemBodyParts.Ass.Anus 
		Cock = self.MaleBodyParts.Penis
		
		sTweet = "\""
		
		# Male Protests
		Protests = []
		Protests.append("We shouldn't be doing this! It's wrong!")
		Protests.append("No! This is so wrong! We should stop!")
		Protests.append("We should stop! This is wrong!")
		Protests.append("No. We should stop. This isn't right!")
		Protests.append("We'd better stop. This isn't right!")
		Protests.append("We'd better stop. We shouldn't be doing this!")
		Protests.append("We shouldn't be doing this! It's wrong!")
		Protests.append("This isn't right. We'd better stop.")
		Protests.append("This is wrong, " + sHerName + ". Let's stop before we go any further!")
		Protests.append("This isn't right, " + sHerName + "! We'd better stop!")
		Protests.append("We shouldn't be doing this, " + sHerName + "! It's wrong!")
		Protests.append("This isn't right, " + sHerName + "! We have to stop!")
		Protests.append("No more. This isn't right. Let's stop before we go too far!")
		
		sTweet += Protests[randint(0,len(Protests) - 1)] + "\" protested " + sHisName + ". "
		sTweet += "The two of them were in bed, their naked bodies " + WordList(['heaving','writhing','sweaty','flushed','glistening']).GetWord() + " with " 
		sTweet += WordList(['passion','lust','desire','forbidden passion','forbidden lust', 'forbidden desire']).GetWord () + ".\n\n"
		
		#Female temptations
		Tempt = []
		Tempt.append("It feels so good though, doesn't it " + sHoney + "?")
		Tempt.append("Don't you like this, " + sHoney + "? Doesn't it feel good?")
		Tempt.append("Don't stop, " + sHoney + ". It feels so good!")
		Tempt.append("I know you want this, " + sHoney + ". You've wanted it for a long time,")
		Tempt.append("Don't you like this, " + sHoney + "? Doesn't it feel good?")
		Tempt.append("Don't you want me? Don't I make you feel good, " + sHoney + "?")
		Tempt.append("Come on " + sHoney + ", I know you want this. You want it so bad, don't you?")
		Tempt.append("But you want this so bad, don't you " + sHoney + "?")
		Tempt.append("But you want this bad, don't you " + sHoney + "?")
		Tempt.append("But you want this, don't you " + sHoney + "?")
		
		sTweet += "\"" + Tempt[randint(0,len(Tempt) - 1)] + "\" "
		sTweet += WordList(['cooed','purred']).GetWord() + " " + sHerName + ". \"" 
		sTweet += WordList(["Fuck me hard", "Fuck me like a whore", "Fuck my brains out",
							"Pound me hard", "Pound me", "Pound me like a whore",
							"Fill me","Impale me","Stuff me","Ravish me","Nail me",
							"Cum inside me","Defile me","Take me hard","Fill me up",
							"Stuff my hole","Fill my hole","Defile my hole",
							"Impale my hole","Stuff my filthy hole","Give it to me hard",
							"Use my hole","Use me like a whore",
							"Impale my naughty hole"]).GetWord() + " with that "
		
		#Cock description 
		CockDesc = []
		CockDesc.append("big " + Cock.ShortDescription())
		CockDesc.append("big, " + Cock.MediumDescription())
		CockDesc.append(Cock.FloweryDescription())
		sTweet += CockDesc[randint(0,len(CockDesc) - 1)] + " of yours!\"\n\n"
		
		sTweet += sHisName + " could hold back no longer. "
		
		#Man says he's going to cum 
		sTweet += "\"Oh " + WordList(['shit','fuck','god','Jesus Christ', 'hell yes','shit yes','fuck yes']).GetWord() + "! " 
		if CoinFlip():
			sTweet +=  WordList(["Yes! Yes!!","Yes! I'm cumming","I'm gonna cum","Yes! I'm gonna cum","I'm cumming",
								 sHerName + "! I'm cumming!", "Oh " + sHerName + "! I'm cumming!",
								 sHerName + "! Oh yes! I'm cumming!", "Oh " + sHerName + "! Yes!"]).GetWord() 
							 
		
			sTweet += "!\" he moaned. "
			
			sHole = ""
			if CoinFlip():
			#pussy 
				if CoinFlip():
					sHole += Vag.InnerVag.ShortDescription() 
				else:
					sHole += Vag.ShortDescription()
			else:
			#ass
				sHole += WordList(['ass','anus','asshole','butt-hole','rear-entrance','rectum','bowels']).GetWord() 
			
			#Climax
			if CoinFlip():
				sTweet += "Then he " + WordList(["bucked his hips", "thrust deep"]).GetWord() + " and began to fill his "
				sTweet += sForbiddenLover + "'s " + sHole + " with his " + self.Semen.RandomDescription() + "."
			else:
				sTweet += "Then he began to pump " + self.Semen.RandomDescription() + " deep into "
				sTweet += "his " + sForbiddenLover + "'s " + sHole + "."
		else: 
			sTweet += WordList(["Yes! Yes!!","I'm gonna cum","Yes! I'm gonna cum",
								 sHerName + "! I'm gonna cum!", "Oh " + sHerName + "! I'm gonna cum!",
								 sHerName + "! Oh yes! I'm gonna cum!", "Oh " + sHerName + "! Yes!"]).GetWord() 
								 
			sTweet += "! I'm gonna cum inside my " + sForbiddenLover + "!!\""
		return sTweet
		
# "Marry me, Simone!" he moaned. 
# "But we are married!" she replied in confusion.
# "Yes," he said, "but not to each other."
class Generator80(Generator):
	ID = 80
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location()
		# Tags = {exutil.TAG_DONE_TO_HER}, NotTags = {exutil.TAG_CLIMAX,exutil.TAG_PEN}
		
		sTweet = Location.BeginDesc + " "
		
		if CoinFlip():
		#he proposes
			sTweet += SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, Tags = {exutil.TAG_DONE_TO_HIM}, Location = Location).Scene() + "\n\n"
			sTweet += "\"Marry me, " + sHerName + ",\" he " + self.VMoan.Past() + ".\n\n"
			sTweet += "\"But we ARE married!\" she replied in confusion.\n\n"
			sTweet += "\"Yes,\" he said, \"but not to each other.\""
		else: 
		#she proposes 
			sTweet += SceneSelector().GetScene(sHisName = sHisName, sHerName = sHerName, Tags = {exutil.TAG_DONE_TO_HER}, Location = Location).Scene() + "\n\n"
			sTweet += "\"Marry me, " + sHisName + ",\" she " + self.VMoan.Past() + ".\n\n"
			sTweet += "\"But we ARE married!\" he replied in confusion.\n\n"
			sTweet += "\"Yes,\" she said, \"but not to each other!\""

		return sTweet
		
# interracial
class Generator81(Generator):
	ID = 81
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlRace = WordList(["an Asian girl","a black girl","a Japanese girl",
							 "a redhead","a white chick","a fiery latina",
							 "a plus-sized woman","a black chick",
							 "a hispanic chick","a mature woman",
							 "your best friend's mom","your teacher",
							 "your boss","your boss's wife","your step-mom",
							 "a MILF","a black MILF","your mother-in-law",
							 "your black mother-in-law","your hispanic maid",
							 "a big black girl","a hispanic girl",
							 "a Japanese schoolgirl","a firecrotch",
							 "a blonde chick","a sweet little Asian girl",
							 "your Asian secretary"
							])
							 
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		ProtestReasons = WordList(["I have a girlfriend!","I'm engaged to be married!","I'm a married man!","I have a wife!"])
		SexyVoice = WordList(["purred","growled throatily","said in a husky voice","growled in a husky voice"])
		VerbFuck = WordList(["to be with","to do it with","to fuck","to bang","to make love to",
							 "to screw","to bone","to screw"])
		
		iRand = randint(1,3)
		
		if iRand == 1:
		# she bends over and takes off her panties
			sTweet += sHerName + " bent over in front of " + sHisName + ", "
			sTweet += "giving him an excellent view of her " + self.FemBodyParts.Ass.ShortDescription() + ". "
			sTweet += "She sensually slipped her " + WordList(['panties','cute pink panties','lacey panties',
															'red silk panties','skimpy thong',
															'skimpy bikini bottom']).GetWord() + " "
			sTweet += "over her " + self.FemBodyParts.Hips.GetAdj() + " hips, "
			sTweet += "exposing her " + self.FemBodyParts.Vagina.RandomDescription() + ".\n\n"
			sTweet += sHisName + " swallowed the lump in his throat. \"Oh God!\" he said. "
			sTweet += "\"You're so fucking " + WordList(['hot','sexy']).GetWord() + "! "
			sTweet += "But I can't! " + ProtestReasons.GetWord() + "\"\n\n"
			sTweet += "\"Come on baby,\" she " + SexyVoice.GetWord() + ", shaking her " + self.FemBodyParts.Ass.RandomDescription() + ". "
		
		elif iRand == 2:
		# she pulls his dick out and starts to give him a blowjob
			sTweet += sHerName + " knelt in front of him and " + WordList(["unbuckled his belt","pulled down his zipper"]).GetWord() + ". "
			sTweet += "Then she pulled his pants down, exposing his " + self.MaleBodyParts.Penis.ShortDescription() + ". "
			sTweet += WordList(["It was already hard","It was already turgid with excitement",
								"It was already engorged with anticipation",
								"It was already erect, and a bead of precum hung from the tip",
								"It was already stiffly erect"
							  ]).GetWord() + ".\n\n"
			sTweet += sHisName + " swallowed the lump in his throat. \"Oh God!\" he said. "
			sTweet += "\"You're so fucking " + WordList(['hot','sexy']).GetWord() + "! "
			sTweet += "But I can't! " + ProtestReasons.GetWord() + "\"\n\n"
			sTweet += "\"Come on baby,\" she " + SexyVoice.GetWord() + ", placing a kiss on his " + self.MaleBodyParts.Penis.RandomDescription() + ". "
		
		else:
		# she takes her top off and shows him her breasts
			sTweet += sHerName + " pulled her " + WordList(["sports bra","lacey bra","thin white t-shirt","skimpy bikini top"]).GetWord() + " "
			sTweet += "over her head, exposing her " + self.FemBodyParts.Breasts.RandomDescription() + ". "
			sTweet += sHisName + " swallowed the lump in his throat. \"Oh God!\" he said. "
			sTweet += "\"You're so fucking " + WordList(['hot','sexy']).GetWord() + "! "
			sTweet += "But I can't! " + ProtestReasons.GetWord() + "\"\n\n"
			sTweet += "\"Come on baby,\" she " + SexyVoice.GetWord() + ", taking both his hands and guiding them to her " + self.FemBodyParts.Breasts.ShortDescription() + ". "
		
		Temptations = []
		Temptations.append("\"I know you've always wanted " + VerbFuck.GetWord() + " " + GirlRace.GetWord() + "!\"")
		Temptations.append("\"I won't tell. This could be your one chance " + VerbFuck.GetWord() + " " + GirlRace.GetWord() + "!\"")
		Temptations.append("\"Don't you want to know what it's like " + VerbFuck.GetWord() + " " + GirlRace.GetWord() + "?\"")
		Temptations.append("\"Haven't you always fantasized about " + WordList(["banging","fucking","sleeping with","doing it with","being with"]).GetWord() + " " + GirlRace.GetWord() + "?\"")
		Temptations.append("\"Don't tell me you're going to pass up the chance " + VerbFuck.GetWord() + " " + GirlRace.GetWord() + "?\"")
		
		sTweet += Temptations[randint(0,len(Temptations) - 1)]

		return sTweet
		
# Veronica groaned with pleasure as her tall, strapping massage therapist kneaded her sore muscles. 
# "Oh fuck, that feels amazing," she said. "Tell me, Brad... do you give happy endings?"
# Brad squirted more oil into his hands and rubbed them together. "For you Mrs Johnson, anything," he said. 
# Then he spread her legs open and began to tenderly finger her anus.
class Generator82(Generator):
	ID = 82
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ['hung','thatched','taut','tight','husky']
		
		sHerName = self.FemaleName.FirstName()
		sHisName = self.MaleName.FirstName()
		
		sManAdj1 = self.MaleBodyParts.GetAdj(NotList = ManNotList)
		sManAdj2 = self.MaleBodyParts.GetAdj(NotList = ManNotList + [sManAdj1])
		
		sTweet += sHerName + " " + WordList(["moaned","groaned","sighed"]).GetWord() + " with pleasure as "
		sTweet += "her " + sManAdj1 + ", " + sManAdj2 + " massage therapist "
		sTweet += WordList(["rubbed","massaged","kneaded","rubbed down"]).GetWord() + " "
		sTweet += "her " + WordList(["sore","aching"]).GetWord() + ", naked " 
		sTweet += WordList(["body","body","ass","thighs"]).GetWord() + ". "
		sTweet += "\"" + self.Exclamation.GetWord(bHappy = True).capitalize() + "\" "
		sTweet += "she " + WordList(["exclaimed","sighed"]).GetWord() + ", "
		sTweet += "\"that feels " + WordList(["amazing","divine","incredible","so good","wonderful"]).GetWord() + "! "
		sTweet += "Tell me, " + sHisName + "... do you give happy endings?\"\n\n"
		sTweet += sHisName + " squirted more " + WordList(["oil","lotion"]).GetWord() + " "
		sTweet += "into his hands and rubbed them together. "
		sTweet += "\"For you Mrs. " + names.AllLastNames().GetWord() + ", anything,\" he said. "
		if CoinFlip():
			
			if CoinFlip():
				sTweet += "Then he spread her " + self.FemBodyParts.Legs.RandomDescription(bAllowLongDesc = False) + " apart and "
				sTweet += "began to " + WordList(["tenderly","gently","sensually"]).GetWord() + " "
				sTweet += WordList(["lick","finger","rub","stroke","carress","fist","insert two fingers into","eat","tongue"]).GetWord() + " her "
				sTweet += self.FemBodyParts.Vagina.RandomDescription()
			else:
				sTweet += "Then he spread her " + self.FemBodyParts.Ass.RandomDescription(bAllowLongDesc = False) + " apart and "
				sTweet += WordList(["tenderly","gently","sensually"]).GetWord() + " began to "
				sTweet += WordList(["lick","finger","rub","stroke","carress","fist","insert two fingers into","eat","rim"]).GetWord() + " her "
				sTweet += self.FemBodyParts.Ass.Anus.RandomDescription()
		else:
			sTweet += "Then he began to " + WordList(["rub","carress","squeeze","massage","rub oil onto","massage oil into"]).GetWord() + " "
			sTweet += "her " + self.FemBodyParts.Breasts.RandomDescription()
			if CoinFlip():
				sTweet += " and her " + self.FemBodyParts.Breasts.Nipples.RandomDescription()
		sTweet += "."
			

		return sTweet
		
# "Oh, I'll never find love!" wept Mary Jane. "What man would want a {plain-looking/chubby}, {nerdy/geeky} 
# {waitress/barista/accountant}, especially one with a pair of enormous, swollen, DDD breasts???"
# fallen arches? 
class Generator83(Generator):
	ID = 83
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tits = self.FemBodyParts.Breasts 
		sTitsAdj1 = Tits.GetAdj()
		sTitsAdj2 = Tits.GetAdj() 
		while sTitsAdj2 in sTitsAdj1 or sTitsAdj1 in sTitsAdj2:
			sTitsAdj2 = Tits.GetAdj() 
			
		Ass = self.FemBodyParts.Ass
		sAss = Ass.ShortDescription()
		
		sAssAdj1 = Ass.GetAdj()
		sAssAdj2 = Ass.GetAdj() 
		while sAssAdj1 in sAssAdj2 or sAssAdj2 in sAssAdj1:
			sAssAdj2 = Ass.GetAdj()
			
		sAssArticle = ""
		if sAssAdj1[0] in ['aeiou']:
			sAssArticle = "an "
		elif sAss not in ['buttocks','buns','cheeks']:
			sAssArticle = "a " 
		
		sHerName = names.PlainNamesFemale().FirstName()
		
		PlainAdj1 = WordList(['chubby','freckled','frumpy','plain-looking','short','skinny'])
		sPlainAdj1 = PlainAdj1.GetWord()
		PlainAdj2 = WordList([str(randint(27,48)) + '-year-old','awkward','bookish','ginger','inexperienced',
							 'geeky','nerdy','shy','uptight','curly-haired'])
		sPlainAdj2 = PlainAdj2.GetWord() 
		BoringJobs = WordList(['accountant','barista','civil servant','clerk','dog walker',
							   'grad student','librarian','nail technician','office manager','secretary',
							   'shift supervisor','teaching assistant','third-grade teacher','Uber driver',
							   'Wal-Mart greeter','waitress'])
		sBoringJob = BoringJobs.GetWord()

		
		sTweet = "\"Oh! I shall never find " + WordList(['love','romance','the man of my dreams','true love','true romance']).GetWord() + "!\" "
		sTweet += WordList(['sighed','cried','wept']).GetWord() + " " + sHerName + ". "
		sTweet += "\"What man would want " + AddArticles(sPlainAdj1) + ", " + sPlainAdj2 + " " + sBoringJob + ", "
		sTweet += "especially one with a pair of " + sTitsAdj1 + ", " + sTitsAdj2 + " "  
		sTweet += WordList(['D-cup','DD-cup','DDD-cup','double-D','triple-D']).GetWord() + " " + Tits.ShortDescription() + " "
		
		
		Endings = []
		Endings.append("and " + sAssArticle + sAssAdj1 + ", " + sAssAdj2 + " " + sAss)
		Endings.append("and " + sAssArticle + sAssAdj1 + ", " + sAssAdj2 + " " + sAss)
		Endings.append("who is really into anal sex")
		Endings.append("who is extremely skilled at deep-throating")
		Endings.append("who is always thinking about sex")
		Endings.append("who is constantly horny for dick")
		Endings.append("who loves to suck dick")
		Endings.append("who loves to go topless")
		Endings.append("who is also an erotic nude model")
		Endings.append("and an open-minded twin sister")
		Endings.append("who gives incredible tit-jobs")
		Endings.append("who loves threesomes")
		
		sTweet += Endings[randint(0,len(Endings)-1)] + "??\""

		return sTweet

# "Oh baby," said Brad passionately, "I want you so bad!" Calliope was naked in his arms. 
# He put his hand between her pale thighs and spread them apart. He ground his fat hard-on against her moist vagina.
# "No Brad, wait!" said Calliope breathlessly. "I'm saving my pussy for marriage. But I'll let you fuck my 
# virgin ass."		
class Generator84(Generator):
	ID = 84
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Tits = self.FemBodyParts.Breasts
		Dick = self.MaleBodyParts.Penis 
		Pussy = self.FemBodyParts.Vagina 
		Thighs = self.FemBodyParts.Thighs 
		Legs = self.FemBodyParts.Legs
		Ass = self.FemBodyParts.Ass 
		
		sPussy = Pussy.ShortDescription(NotList = ['flower'])
		sDick = Dick.RandomDescription(bAllowLongDesc = False, NotList = ['beautiful'])
		sAss = Ass.RandomDescription(NotList = ['cheeks','buns','buttocks','fuckable','sweet','bountiful','glistening'])
		sAnus = Ass.Anus.ShortDescription(NotList = ['knot']) 
		
		ToENotList = ['dear']
		sToE1 = self.TermsOfEndearment.GetWord(NotList = ToENotList)
		sToE2 = self.TermsOfEndearment.GetWord(NotList = ToENotList)
		sToE3 = self.TermsOfEndearment.GetWord(NotList = ToENotList)
		
		sTweet = "\"Oh " + sToE1 + ",\" "
		sTweet += "said " + sHisName + " " + WordList(['passionately','ardently','huskily']).GetWord() + ", "
		sTweet += "\"" + WordList(["I want you so bad","I need you so bad","I want you right now",
								   "I want to take you right now","I want to deflower you right now",
								   "I want to pop your cherry right now",
								   "You're so fucking sexy"]).GetWord() + "!\" "
		sTweet += sHerName + " was naked underneath him. "
		if CoinFlip():
			if CoinFlip():
				sTweet += "He put his hand between her " + Thighs.RandomDescription() + " "
				sTweet += "and spread them apart.\n\n"
			else:
				sTweet += "He put his hand between her " + Legs.RandomDescription(bAllowLongDesc = False) + " "
				sTweet += "and spread them apart.\n\n"
		else:
			if CoinFlip():
				sTweet += "He squeezed her " + Tits.RandomDescription() + " " 
			else:
				sTweet += "He kissed her " + Tits.RandomDescription() + " " 
			sTweet += "and then began to suck eagerly on her " + Tits.Nipples.RandomDescription() + ".\n\n"
		sTweet += sHerName + " felt his " + sDick + " "
		if CoinFlip():
			sTweet += "probing her " + Pussy.InnerLabia.RandomDescription(bAllowLongDesc = False) + ". "
		else: 
			sTweet += "pressing against her " + Pussy.OuterLabia.RandomDescription(bAllowLongDesc = False) + ". "
		sTweet += "\"No " + sHisName + ", wait!\" she said breathlessly. "
		sTweet += "\"I'm saving my " + sPussy + " for marriage.\"\n\n"
		sTweet += "\"" + WordList(["Awww, please, " + sToE2,"Awww, c'mon " + sToE2,
								  "But " + sToE2 + ", I want you so bad",
								  "But " + sToE2 + ", I want you so bad",
								  "But " + sToE2 + ", please",
								  "C'mon " + sToE2 + ", I'm so horny for you",
								  "But " + sToE2 + ", I'm so hard",
								  "C'mon " + sToE2 + ", I'll just put the tip in",
								  "C'mon " + sToE2 + ", I'm ready to go"]).GetWord() + "!\" he whined.\n\n"
		sTweet += "\"It's okay, " + sToE3 + ",\" she said. \""
		sTweet += WordList(["You can stick it inside my " + sAnus,
						    "You may put it inside my " + sAnus,
							"You can stick it inside my " + sAnus,
							"You may stuff my " + sAnus,
							"You may fuck my " + sAnus,
							"You may fuck me in the " + sAnus,
							"You may fuck me in my ass",
							"You may fuck my " + sAss]).GetWord()
		sTweet += " instead!\""
		
		return sTweet 
		
# "Just think," she said excitedly to her best friend Amy, "in less than three days Brad 
# and I will be married, and my name will be MRS Ivana Seymour-Butts!"
class Generator85(Generator):
	ID = 85
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sBFFName = names.PlainNamesFemale().FirstName()
		sRegularMaleFirstName = self.MaleName.FirstName()
		sBrideName = names.GetInnName(shutil.Gender.Female)
		sHusbandName = names.GetInnName(shutil.Gender.Male)
		
		if CoinFlip():
			sTweet = "\"Just think,\" she gushed excitedly to her best friend " + sBFFName + ", "
		else:
			sTweet = "\"Can you believe it?\" she exclaimed excitedly to her best friend " + sBFFName + ". "
		sTweet += "\"" + WordList(["in less than a week", "in less than three days", "in less than two days",
								   "twenty-four hours from now","thirty-six hours from now","in less than a month",
								   "one week from now","four days from now","by next Saturday",
								   "by next Sunday"]).GetWord() + " "
		if CoinFlip(): 
		#male first name
			sTweet += "I'll be married and I'll offically be MRS. " + sHusbandName
		else:
		#female first name
			sTweet += sRegularMaleFirstName + " and I will be married and my name will be MRS. " + sBrideName
		sTweet += "!\""
		
		return sTweet

# Same as 57, but in the ass		
class Generator86(Generator):
	ID = 86
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = self.FemaleName.FirstName()
		
		sEjaculated = WordList(["gasped", "exclaimed", "blurted", "burst out"]).GetWord()
		sShockedExclaim = WordList(["Oh fuck", "Shit", "What the fuck", "Holy shit", "Holy fuck", "Holy fucking shit", "Oh shit", "Fuck"]).GetWord()
		Vag = self.FemBodyParts.Vagina
		Clit = self.FemBodyParts.Vagina.Clitoris
		Face = self.FemBodyParts.Face 
		Ass = self.FemBodyParts.Ass
		Anus = Ass.Anus 
		Breasts = self.FemBodyParts.Breasts
		Nipples = Breasts.Nipples 
		Clit = Vag.Clitoris 
		Hips = self.FemBodyParts.Hips
		
		sRelation = WordList(["mom", "dad", "older brother", "step-mom", "step-dad", "sister", "roommate"]).GetWord()
		sToy = WordList(["a curling iron", "a Ken doll", "a spatula", "a banana", "a pickle", "a cucumber", 
						 "a candle", "an electric toothbrush", "my toothbrush", "a rolled up magazine", 
						 "a rolling pin", "a screwdriver", "a baguette", "a shampoo bottle", 
						 "a baseball bat", "my TV remote", "an eggplant", "corn on the cob", "Coke bottle", 
						 "a plunger", "a crucifix", "a toothpaste tube", "a bowling pin", "a broomstick",
						 "my flute", "my clarinet", "my giant foam finger"]).GetWord()
		sHole = Vag.InnerVag.RandomDescription()
		
		sTweet += sHerName + " lay back on the bed and moaned as she "
		sTweet += WordList(["gently", "tenderly", "vigorously", "energetically", "ardently", "fervently"]).GetWord() + " "
		sTweet += WordList(["massaged", "pleasured", "rubbed", "caressed", "stroked", "stimulated", "masturbated", 
							"fondled", "fingered"]).GetWord() + " "
		sTweet += "her " + Vag.RandomDescription() + ". "
		sTweet += "She spread apart her " + Vag.OuterLabia.RandomDescription() + " "
		sTweet += "and gently teased her " + Vag.Clitoris.RandomDescription() + ".\n\n"
		sTweet += "She " + WordList(["reached under her pillow", "felt under the covers", "reached behind the night-stand"]).GetWord() + " "
		sTweet += "and found her favorite object and a bottle of lube. "
		sTweet += "After lubing it up, she very carefully inserted it into her " + Anus.RandomDescription() + ". "
		sTweet += "She " + WordList(["moaned","sighed","gasped"]).GetWord() + " with pleasure as she "
		sTweet += WordList(["thrust it forcefully in and out",
							"slid it gently in and out",
							"impaled herself with it",
							"plunged it deep inside",
							"shoved it deeper", 
							"stuffed it deeper and deeper"]).GetWord() + ".\n\n"
							
		sTweet += "Suddenly, the door flew open and her " 
		if CoinFlip():
			sTweet += WordList(["older brother", "dad", "step-dad", "step-brother", "step-son"]).GetWord() + " walked in.\n\n"
			sTweet += "\"" + sShockedExclaim + ", " + sHerName + "!\" he " + sEjaculated + ", "
			
		else:
			sTweet += WordList(["mom", "step-mom", "sister", "step-sister", "college roommate", "best friend"]).GetWord() + " walked in.\n\n"
			sTweet += "\"" + sShockedExclaim + ", " + sHerName + "!\" she " + sEjaculated + ", "

		sTweet += "\"Do you have " + sToy + " in your ass?!?"
		return sTweet
		
class Generator87(Generator):
	ID = 87
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		BlueCollarNotList = ['serf','stable boy','peasant','paige','tax payer','page']
		PenisNotList = ['carefully','man-scaped','package','massively','burning','unfurled',
					    'naked','lovingly','member','hardening']
		VagNotList = ['womanhood','flower','muff','peach']
		sHisFakeName = names.ClassyNamesMale().FirstName()
		sHisPlainName = names.PlainNamesMale().FirstName()
		BigCities = WordList(['New York','Paris','Los Angeles','London','Dubai','Milan','San Francisco','Prague',
							  'Hong Kong','Ibiza','Macao','Havanna','Berlin','Sydney'])
		HornyTerms = WordList(['all revved up','hot and ready','hot and horny','horny AF',
									   'horny as fuck','all turned on','wet as fuck','all warmed up',
									   'crazy horny'])
							  
		sTweet += "\"The truth is, I'm not really " + sHisFakeName + " from " + BigCities.GetWord() + ",\""
		sTweet += " he " + WordList(['admitted','confessed']).GetWord() + ". "
		sTweet += "\"My name is " + sHisPlainName + ", "
		sTweet += "and I'm a " + self.BlueCollar.GetWord(NotList = BlueCollarNotList) + " "
		sTweet += "from " + sharedmisc.DullPlaces().GetWord() + ".\"\n\n"
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet += "\"I don't care where you're from,\" she said. "
		elif iRand == 2: 
			sTweet += "\"I don't give a fuck,\" she said. "
		else: 
			sTweet += "\"I don't care what your name is,\" she said. "
		
		if iRand == 2:
			sTweet += "\"I'm " + HornyTerms.GetWord() + ", so right now your 'job' is to "
		else:
			sTweet += "\"I'm " + HornyTerms.GetWord() + " right now, so I need you to "
		if CoinFlip():
			sTweet += "pull out that " + self.MaleBodyParts.Penis.RandomDescription(bAllowLongDesc = False, NotList = PenisNotList) + " of yours "
			sTweet += WordList(["so I can suck you off","and put it in my mouth","and fuck my mouth with it",
								"and put it between my tits","and tit-fuck me",
								"and stick it down my throat",
								"and cover my titties in " + self.Semen.ShortDescription(),
								"and fuck my brains out with it","and pound me til I can't walk",
								"and fuck the shit out of me with it",
								"and start filling my holes with it",
								"and stuff it in my ass"
							   ]).GetWord() + "."
		else:
			sTweet += "" + WordList(["bend me over","pull my hair","rip my panties off",
									 "suck on my titties","play with my tits","squeeze my ass",
									 "grab me around the neck","pull my panties down",
									 "rip this dress off me","lube up","lube me up"]).GetWord() + " and "
			sTweet += WordList(["pound","stuff","ream","plough","jackhammer","fuck","bang"]).GetWord() + " "
			if CoinFlip():
				sTweet += "my " + sharedmisc.VaginaSlang().GetWord(NotList = VagNotList) + " "
			else:
				sTweet += "my " + WordList(['ass','anus','asshole','butthole','rectal cavity','starfish','bunghole',
											'corn hole','dirt-pipe','fart blaster','heinie hole','poop-chute',
											'poop-trap','shit-hole']).GetWord() + " "
			sTweet += WordList(["until I can't walk","until my legs shake","until I'm dizzy",
								"until I can't walk straight","until it's raw","until I can't see straight",
								"until the " + self.Semen.ShortDescription() + " runs down my thighs",
								"all " + WordList(['fucking','goddamn','damn']).GetWord() + " " + WordList(['night','weekend']).GetWord(),
								"until I cum","until I squirt","until I scream","like you're my ex-husband"
								]).GetWord() + "."
				
		sTweet += "\""

		return sTweet
		
# class Generator88(Generator):
	# ID = 88
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# sTweet += "This is a bot.\n\n"
		# sTweet += "Every few hours it generates a 'sex scene' based on a template filled in with some randomized phrases. Then it posts it to this twitter.\n\n"
		# sTweet += "Sometimes the results are nonsense. Or funny. Or sexy. Or wildly inappropriate. You never know what the bot will do next.\n\n"
		# sTweet += "Liking and retweeting the bot keeps twitter from flagging it as a spam bot. Thank you for doing that.\n\n"
		# sTweet += "Follow if you dare!"

		# return sTweet
		
# "I'm a sheltered Amish school-marm," she thought. "What am I doing giving giving a full-frontal massage to 
# a handsome muscular Italian hitman on my parent's bed?"
# class Generator82(Generator):
	# ID = 89
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet

class Generator90(Generator):
	ID = 90
	Priority = 5
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		PenisNotList = ['hard','thick','long','engorged','swollen','length','erect']
		sTweet = self.MaleName.FirstName() + " approached the bed completely naked. "
		sTweet += self.FemaleName.FirstName() + " drank in "
		if CoinFlip():
			sTweet += "his " + self.MaleBodyParts.Eyes.RandomDescription(bAllowShortDesc = False) + ", "
		else:
			sTweet += "his " + self.MaleBodyParts.Jaw.RandomDescription(bAllowShortDesc = False) + ", "
		sTweet += self.MaleBodyParts.DescRandomNakedParts(iNum = 4, sDivideChar = ";",bAss = True, bPenis = False, sPossessive = "his")
		sTweet += ".\n\n"
		sTweet += "She "
		if CoinFlip(): 
			sTweet += "reached down between her " + WordList(['legs','thighs']).GetWord() + " "
			sTweet += "and " + WordList(["sensually ","slowly ","gently ", ""]).GetWord()
			sTweet += WordList(["rubbed","fingered","stroked","carressed","spread apart","massaged",
							    "masturbated","teased"]).GetWord() + " " 
			if CoinFlip():
				sTweet += "her " + self.FemBodyParts.Vagina.RandomDescription() + ". "
			else:
				sTweet += "her " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + ". "
		else:
			sTweet += WordList(["sensually ","slowly ","gently ", ""]).GetWord()
			if CoinFlip():
				sTweet += WordList(["cupped","carressed","teased","stroked","squeezed"]).GetWord() + " "
				sTweet += "her " + self.FemBodyParts.Breasts.RandomDescription() + ". "
			else:
				sTweet += WordList(["carressed","teased","stroked","squeezed","rubbed","pinched"]).GetWord() + " "
				sTweet += "her " + self.FemBodyParts.Breasts.Nipples.RandomDescription() + ". "
		sTweet += "\"Do you " + WordList(['like','want']).GetWord() + " this, " + self.TermsOfEndearment.GetWord() + "?\" "
		sTweet += "she asked. He didn't reply, but his " + self.MaleBodyParts.Penis.RandomDescription(bAllowLongDesc = False, NotList = PenisNotList) + " "
		sTweet += WordList(["thickened","lengthened","rose","swelled","became engorged","hardened",
							"began to grow"]).GetWord() + " "
		sTweet += "in anticipation."

		return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet

# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator82(Generator):
	# ID = 82
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		

				
class GeneratorSelector():
	GeneratorList = []
	
	def __init__(self):
		for subclass in Generator.__subclasses__():
			item = subclass()
			for x in range(0, item.Priority):
				self.GeneratorList.append([item.ID, item])
			
	def RandomGenerator(self, bAllowPromo = True, Type = None):
		Generator = None
		AllowedTypes = []
		
		if not Type is None:
			AllowedTypes = [Type] 
		else:
			AllowedTypes = [exutil.GeneratorType.Normal, exutil.GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(exutil.GeneratorType.Promo)
			
		#print("RandomGenerator() Allowed types: " + str(AllowedTypes))
		if len(self.GeneratorList) > 0:

			Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
			while not Generator.Type in AllowedTypes:
				Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
				
		return Generator 
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		