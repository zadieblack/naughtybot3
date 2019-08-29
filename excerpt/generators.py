#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *

import excerpt.util as exutil
import excerpt.locations as locations

from excerpt.util import CoinFlip
from excerpt.util import WordList
from excerpt.util import AddArticles

from excerpt.locations import LocationSelector

import excerpt.bodyparts as bodyparts
import excerpt.verbs as verbs
import excerpt.misc as misc
import excerpt.scenes as scenes
import excerpt.names as names

from excerpt.scenes import SceneSelector

import excerpt.bodyparts as bodyparts
import excerpt.verbs as verbs
import excerpt.misc as misc
import excerpt.scenes as scenes
import excerpt.names as names

import excerpt.people as people
import excerpt.texttoimg as texttoimg
import title.people as titpeople

PromoHistoryQ = exutil.HistoryQ(2)
	
def ChopTweet(sTweet, sPrefix):
	# This function is no longer in use since the bot was switched to tweeting images. However since it is useful for splitting text over 280 chars into multiple tweets, I'm leaving it in for future reference
	Tweets = []
	iTargetLen = MAX_TWITTER_CHARS - 4
	iTweetNo = 1
	
	iLastChar = iTargetLen
	sTweet = sPrefix + str(iTweetNo) + ") " + sTweet
	while not sTweet[iLastChar].isspace():
		iLastChar = iLastChar - 1
	
	Tweets.append(sTweet[0:iLastChar])
	sTweet = sTweet[iLastChar + 1:]
	iTweetNo = iTweetNo + 1
	sTweet = str(iTweetNo) + ") " + sTweet
		
	while len(sTweet) > iTargetLen:
		iLastChar = iTargetLen
		
		while not sTweet[iLastChar].isspace():
			iLastChar = iLastChar - 1
			
		Tweets.append(sTweet[0:iLastChar])
		sTweet = sTweet[iLastChar + 1:]
		iTweetNo = iTweetNo + 1
		sTweet = str(iTweetNo) + ") " + sTweet
		
	Tweets.append(sTweet)
	
	return Tweets

def AddHashtag(Tweets):
	# if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
	if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
		sHashtag = "\n#" + misc.Hashtags().GetWord()
		if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
			Tweets[len(Tweets) - 1] += sHashtag

	return Tweets
	
def GetChoppedTweets(bTest, iGeneratorNo = 0, sPrefix = "", bAllowPromo = True):
	# This function is no longer in use since the bot was switched to tweeting images. However since it is useful for splitting text over 280 chars into multiple tweets, I'm leaving it in for future reference
	Tweets = [1]
	Gen = None 
	sTweetStr = ""
	
	#print("Prefix is [" + sPrefix + "]")
	Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = bAllowPromo)
	if not Gen is None:
		sTweetStr = Gen.GenerateTweet()

		if len(sTweetStr) > 0:
			if not Gen.Type == GeneratorType.Promo:
				SaveImg(CreateImg(sTweetStr))
			if IsTweetTooLong(sPrefix + sTweetStr):
				Tweets = ChopTweet(sTweetStr, sPrefix)
			else:
				Tweets[0] = sPrefix + sTweetStr
			if not Gen.Type == GeneratorType.Promo:
				Tweets = AddHashtag(Tweets)	
		else: 
			Tweets[0] = sTweetStr

	return Tweets

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
		self.BadGirlName = misc.BadGirlNames()
		
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
	ID = 1
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		# The baron desecrated Jacinda's well-used muffin with his thick pole.	
		sVerb = self.VForeplay.Present()
		sTweet = "The " + self.WealthyMan.GetPerson() + " " + self.VThrust.Past() + " " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n'" + sVerb.capitalize() + " my " + self.FemBodyParts.Breasts.RandomDescription() + "!' she " + self.VMoan.Past() + ". '" + sVerb.capitalize() + " them and fill me with your " + self.Semen.FloweryDescription() + "!'"
		
		return sTweet
		
class Generator2(Generator):
	# Spreading open her supple buttocks with his rough hands, he desecrated her well-used anus with his erect boner. 'Fuck me,
	# Jordan!' she screamed. 'Pound me like your wife!'	
		
	ID = 2
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		self.MaleBodyParts = bodyparts.BodyMale()
		self.FemBodyParts = bodyparts.BodyFemale()
		self.MaleName = names.NamesMale()
		self.FemaleName = names.NamesFemale() 
		self.VThrust = verbs.VerbThrust()
		
		sTweet = "Spreading open " + self.FemaleName.FirstName() + "'s " + self.FemBodyParts.Ass.RandomDescription() + " with his rough hands, he " + self.VThrust.Past() + " her " + self.FemBodyParts.Ass.Anus.RandomDescription() + " with his " + self.MaleBodyParts.Penis.RandomDescription() + ".\n\n"
		sTweet += "'Do me, " + self.MaleName.FirstName() + "!\' she " + self.VMoan.Past() + ". '" + self.VThrust.Present().capitalize() + " me like I'm your " + self.FFWB.GetPerson() + "!'"
		
		return sTweet

class Generator3(Generator):
	# 'Please, no!' she said, squirming as he bayonetted her pink cooch. 'Not while my yoga teacher is watching!'
	ID = 3
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'Please, no!' " + self.FemaleName.FirstName() + " " + self.VMoan.Past() + ", squirming with pleasure "
		sTweet += "as " + self.MaleName.FirstName() + " " + self.VThrust.Past() + " "
		sTweet += "her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". "
		sTweet += "'Not while my " + self.MFWB.GetPerson() +" is watching!'"
		
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
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
			
		sTweet = "'Oh, " + self.MaleName.FirstName() + ",' she " + self.VMoan.Past() + " in his " + self.MaleBodyParts.Arms.MediumDescription() + ", 'I'm so thirsty for your " + self.Semen.RandomDescription() + "!'\n\n'But " + self.FemaleName.FirstName() + ",' he said, 'You're my " + self.FFWB.GetPerson() + "!'"
		
		return sTweet
		
class Generator6(Generator):
	# 'You don't have to hide the truth from me, Honey,' he said, 'Tom is a successful opthamologist and I'm just a lowly roadie!' 
	# 'That's true,' she said, 'But YOU have a 8 1/2 inch fuck-pole!'	
	ID = 6
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sRivalName = self.MaleName.FirstName()
		sTweet = "'You don't have to hide the truth from me, " + self.FemaleName.FirstName() + ",' he said, '" + sRivalName + " is a successful " + self.WhiteCollar.GetPerson() + " and I'm just a lowly " + self.BlueCollar.GetPerson() + "!'\n\n'I don't care about " + sRivalName + ",' she said, 'You're the one I want. And anyway, you have a " + self.MaleBodyParts.Penis.ShortDescription(bAddLen = True) + "!'"
		
		return sTweet
		
class Generator7(Generator):
	# Charity bit her lip as Tristan fondled her heaving bosoms. 'Oh god,' she said, 'What would my pastor say if he saw that I was letting my pool boy pump into my crack?'	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location()
		
		if CoinFlip():
			sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on " + Location.LyingOn + ", her " + self.FemBodyParts.Breasts.RandomDescription() + " " + WordList(["heaving", "quivering", "trembling", "shuddering", "rising and falling"]).GetWord() + " as " + self.MaleName.FirstName() + " lubed up her " + self.FemBodyParts.Ass.Anus.RandomDescription() + ". '" + self.Exclamation.GetWord().capitalize() + "' she " + self.VMoan.Past() + ", 'What would Father " + self.MaleName.FirstName() + " say if he knew that my " + self.MFWB.GetPerson() + " was " + self.VThrust.Gerund() + " my " + self.FemBodyParts.Ass.ShortDescription() + " " + Location.NamePrep + "?'"
		else:
			sTweet = self.FemaleName.FirstName() + " bit her lip. She lay on " + Location.LyingOn + ", her " + self.FemBodyParts.Breasts.RandomDescription() + " " + WordList(["heaving", "quivering", "trembling", "shuddering", "rising and falling"]).GetWord() + " as " + self.FemaleName.FirstName() + " lubed up a " + str(randint(8,16)) + " 1/2\" " + WordList(["black", "pink", "steel", "vibrating"]).GetWord() + " strap-on. '" + self.Exclamation.GetWord().capitalize() + "' she " + self.VMoan.Past() + ", 'What would Father " + self.MaleName.FirstName() + " say if he knew that my " + self.FFWB.GetPerson() + " was " + self.VThrust.Gerund() + " my " + self.FemBodyParts.Ass.ShortDescription() + " " + Location.NamePrep + "?'"
		
		return sTweet

class Generator8(Generator):
	#Bianca bit her lip as he caressed her youthful thighs. 'Ferdinand!' she said, 'My urologist is in the next room!' 
	#'Should we invite him?' he asked innocently, inserting a finger into her love channel.	
	ID = 8
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Location = locations.LocationSelector().Location(InOut = exutil.LocInOutType.Indoors)
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		sInsertedObject = WordList(["a finger", "two fingers", "three fingers", "a nine-inch steel dildo", 
									"a large eggplant","a ketchup bottle", "a wine bottle", 
									"an enormous black vibrator", "a huge black dildo", "a second dildo",
									"four fingers", "her wadded up dirty panties", "a thumb", "a toe",
									"a strap-on"]).GetWord()
		
		if CoinFlip():
			sTweet = self.FemaleName.FirstName() + " bit her lip as he " + self.VForeplay.Past() + " her " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " " + Location.NamePrep + ". "
			sTweet += "'" + sHisName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson()
			if CoinFlip():
				sTweet += ", " + self.MaleName.FirstName()
			sTweet += " is right outside!'\n\n'Do you think he'd like to join us?' " + sHisName + " asked innocently, "
			sTweet += "inserting " + sInsertedObject + " into her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + "."
		else:
			sTweet = self.FemaleName.FirstName() + " bit her lip as " + sHerName + " " + self.VForeplay.Past() + " her " + self.FemBodyParts.GetRandomBodyParts(1, True, True)[0] + " " + Location.NamePrep + ". "
			sTweet += "'" + sHerName + "!' she " + self.VMoan.Past() + ", 'My " + self.MFWB.GetPerson() 
			if CoinFlip():
				sTweet += ", " + self.MaleName.FirstName()
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
	#'Oh lord, what a day it has been,' said the dutchess. Ripping open her blouse, she exposed her massive double-D mammaries. 'Come, my little fry cook, I need you to nibble on my buns and then to cover my hard nipples in your salty man jam.'
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
	# 'Oh God, Julia,' he said, 'You are so beautiful. I love your supple skin, your sumptuous hips, your perfect thighs, the way
	# you look with my ballsack in your mouth.'
	ID = 11
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'" + self.Exclamation.GetWord(bExMk = False, bHappy = True).capitalize() + ", " + self.FemaleName.FirstName() + ",' he " + self.VMoan.Past() + ", 'You are so beautiful. I love your "
		for part in self.FemBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False):
			sTweet += part + "; "
		sTweet += "and the way you look with " 
		if CoinFlip():
			if CoinFlip():
				sTweet += "my " + self.MaleBodyParts.Penis.GetRandomPenisPart() + " in your " + self.FemBodyParts.Mouth.RandomDescription(bAllowShortDesc = True) + ".'"
			else:
				sTweet += "my " + self.Semen.RandomDescription(bAllowShortDesc = True) + " "
				if CoinFlip():
					if CoinFlip():
						sTweet += "on your " + WordList(["angelic", "innocent", "pretty"]).GetWord() + " face."
					else:
						sTweet += "dripping from your chin."
				else:
					sTweet += "on your " + self.FemBodyParts.Breasts.RandomDescription() + "."
		else:
			if CoinFlip():
				sTweet += "my " + self.MaleBodyParts.Penis.Testicles.RandomDescription() + " slapping against your chin."
			else:
				sTweet += "your " + self.FemBodyParts.Lips.RandomDescription(bAllowShortDesc = True) + " around my " + self.MaleBodyParts.Penis.RandomDescription(bAllowShortDesc = True) + "."
		
		return sTweet
		
class Generator12(Generator):
	# Ginger's robe fell to the floor, and his heart skipped a beat. She had a shapely form with ripe boobs, wide hips, and a 
	# well-used hole. "I can't believe you're my sister," he said.	
	ID = 12
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.FemaleName.FirstName() + "'s robe fell to the floor, and his heart skipped a beat. His lustful gaze took in her "
		
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and her " + part
		sTweet += ".\n\n'" + self.Exclamation.GetWord(bHappy = True).capitalize() + " I can't believe you're my " + self.FFWB.GetPerson() + "!' he " + self.VMoan.Past() + "."
		
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
	Priority = 1
	
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
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "'" + sGirlfriendName + ", my dear, I wrote you a poem,' he said.\n\n"
		sTweet += "'What about?' she asked.\n\n"
		sTweet += "'It's about you, my love,' he said. 'It's about your "
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = True)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and your " + part
		sTweet += ".'\n\n"
		sTweet += "'Oh " + self.MaleName.FirstName() + "!' she sighed."
		
		return sTweet
		
class Generator19(Generator):
	#Unaware Roxanne was watching him, Nicolas pulled his tshirt and jeans off, revealing his broad shoulders, powerful chest, and sinewy thighs. But what made Roxanne's mouth water was the massive, throbbing tool between his legs.	
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sGirlfriendName = self.FemaleName.FirstName()
		sTweet = "Unaware " + sGirlfriendName + " was watching him, " + self.MaleName.FirstName() + " pulled his tshirt and jeans off. Her eyes widened at the sight of his "
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and " + part
		sTweet += ". But what made her mouth water was the " + self.MaleBodyParts.Penis.FloweryDescription() + " dangling between his legs."
		
		return sTweet
		
class Generator20(Generator):
	#Xavier approached the bed, completely naked. A thrill ran through Constance at the sight of his broad shoulders, powerful chest, sinewy thighs, muscular buttocks and swollen man meat. She could hardly believe that in a few minutes this man would be stuffing her virgin pussy.
	ID = 20
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = self.MaleName.FirstName() + " approached the bed completely naked. A thrill ran through " + self.FemaleName.FirstName() + " at the sight of his "
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and " + part
		sTweet += ".\n\nShe could hardly believe that in a few minutes this man would be " + self.VThrust.Gerund() + " her virgin " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + "!"
		
		return sTweet
		
class Generator21(Generator):
	#Candy stroked Lorenzo's turgid meat vigorously. Suddenly his engorged head swelled and spurted gobs of white hot semen on her lips, on her breasts, on her thighs, on her pussy. 'Oh God', she said, 'it's all over my nice Easter Sunday outfit!'
	ID = 21
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = self.FemaleName.FirstName() + " stroked " + self.MaleName.FirstName() + "'s " + self.MaleBodyParts.Penis.RandomDescription() + " vigorously. Suddenly its " + self.MaleBodyParts.Penis.Head.RandomDescription() + " swelled and he " + self.VEjac.Past() + ", sending gobs of " + self.Semen.RandomDescription() + " all over her "
		
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + "; "
			else:
				sTweet += "and her " + part + ".\n\n"
		sTweet += "'" + self.Exclamation.GetWord().capitalize() + "' she said. 'You've ruined my nice " + self.Event.GetWord(bRemoveMy = True) + " dress!'"
		
		return sTweet
		
class Generator22(Generator):
	# John's robe fell to the floor, and Ginger's heart skipped a beat. He had a compact athletic physic with wide shoulders, brawny arms, tight buns, and a 
	# lengthy penis. "I can't believe you're my brother-in-law," she said.	
	ID = 22
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		sTweet = self.MaleName.FirstName() + "'s robe fell to the floor, and " + self.FemaleName.FirstName() + "'s heart skipped a beat. He had "
		
		Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 5, bIncludeInners = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += AddArticles(part) + "; "
			else:
				sTweet += "and " + AddArticles(part) 
		sTweet += ".\n\n'" + self.Exclamation.GetWord().capitalize() + " I can't believe you're my " + self.MFWB.GetPerson() + "!' she said."
		
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
	#Whispering and giggling, they locked themselves in the dressing room. In moments, the man had Angelica bent over the bench in the dressing room, and the two were banging passionately. He was soon exploding deep within her trim entrance as an intense orgasm wracked her body. Warm beads of cream hung from Angelica's lustful cunt and onto the rubber mat. She scooped some up with her fingers and tasted it. Angelica got down on her knees and began to lick the silken cock-snot from his thick erection. Angelica wiggled into her panties.
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
				sTweet += sHerName + " carressed the man's " + self.MaleBodyParts.MediumDescription() + ". "
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
	# 'You're such a slut, Veronica,' he said. 'I *am* a slut,' she said. 'I'm one for *you*, James. I'm a slut for your hard cock in my mouth.' 'You're also a slut because you let me fuck your backdoor in the bathroom at Starbucks,' he said.
	ID = 27
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sBadGirlName = self.BadGirlName.GetWord() 
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
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sFFWB = self.FFWB.GetPerson()
		
		sTweet = sHisName + " walked in and froze. His " + sFFWB + " lay on the bed totally nude. His wide eyes took in her "
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 4, bIncludeInners = True)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += part + ", "
			else:
				sTweet += "and " + part + ".\n\n"
		sTweet += "The naked guy next to her was idly " + self.VForeplay.Gerund() + " her " + self.FemBodyParts.GetRandomHole(bIncludeMouth = False) + ". He looked up at " + sHisName + ". 'You want in?' he asked."
		
		return sTweet
		
class Generator32(Generator):
	#I've got a present for you, she said. What's that? he asked her. She [bent over and pulled her panties aside, revealing her little starfish.] [lifted up her short skirt revealing that she wasn't wearing any panties. He could clearly see her smooth pussy lips and her inner folds.] [pulled her titties out of her blouse. They were large and gleaming with oil.]
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
	#'I own you now,' he said to the babysitter. "I own your your pretty mouth, I own your lickable tits, I own the dripping folds of your cunt and I even own..." He leaned forward, and whispered in her ear, "Your tight little starfish."
	#"Ooh, yes general," she said.
	ID = 33
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTweet = "'I own you now,' said " + self.MaleName.FirstName() + " to his " + self.FFWB.GetPerson() + ". 'I own your " + self.FemBodyParts.Lips.RandomDescription() + ", I own your " + self.FemBodyParts.Breasts.RandomDescription() + ", I own the " + self.FemBodyParts.Vagina.InnerLabia.RandomDescription() + " of your " + self.FemBodyParts.Vagina.ShortDescription() + ", and I even own...' He leaned in and whispered in her ear, 'Your " + self.FemBodyParts.Ass.Anus.RandomDescription() + ".'\n\n"
		sTweet += "'Ooh, yes sir!' she " + self.VMoan.Past() + "."
		
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
	Priority = 1
	
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
							  "you to get your clit pierced"]).GetWord()
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
		
class Generator37(Generator):
	ID = 37
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Penis = self.MaleBodyParts.Penis 
		
		sManEyes = ""
		sManPenis = ""
		sManTip = ""
		sManBalls = ""
		sManSize = str(randint(7,12))
		sWealthyMan = self.WealthyMan.GetPerson()
		sManAdjs = WordList(["tall", "muscular", "bearded"])
		
		if CoinFlip():
			#wealthy man is a BBC
			sWealthyMan = "black " + sWealthyMan
			sManEyes = "dark, smoldering eyes"
			sManPenis = "black, " + Penis.GetAdj(sNot="black") + " " + Penis.ShortDescription()
			sManTip = "dark, " + Penis.Head.GetAdj(sNot="dark") + " " + Penis.Head.ShortDescription()
			sManBalls = "ebony " + Penis.Testicles.ShortDescription()
		else:
			sManEyes = self.MaleBodyParts.Eyes.RandomDescription()
			sManPenis = Penis.RandomDescription()
			sManTip = Penis.Head.RandomDescription()
			sManBalls = Penis.Testicles.ShortDescription()
			
		if CoinFlip():
			sManSize += " & 1/2\""
		else:
			sManSize += "\""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		sTweet = "'I'm afraid, Miss " + sHerName + ",' said the " + sWealthyMan + ", 'that I'm going to have to tell your " + self.MaleSO.GetPerson() + " about your little... indiscretion.'\n\n"
		sTweet += "'Please don't tell him,' she said, looking up at him " + WordList(["pitifully", "hopefully", "wretchedly", "wistfully", "dejectedly", "breathlessly"]).GetWord() + ". He had " + sManEyes + " and his " + WordList(['brawny','broad','mighty','muscular','powerful','rugged','strong','sturdy','well-built','wide']).GetWord() + " shoulders filled out his sharply-tailored " + WordList(["tuxedo", "three-piece suit", "black suit", "button-down silk shirt", "sport coat", "gray suit"]).GetWord() + " nicely. 'I'll do anything.'\n\n"
		if CoinFlip():
			sTweet += "'You must be punished, Miss " + sHerName + ",' he said. 'Will you do as I say?' She nodded.\n\n"
			sTweet += "'Then bend over and lift your skirt.' " + sHerName + " flushed, but she knew she had no choice. She bent lifted the hem, exposing her bare " + self.FemBodyParts.Ass.MediumDescription(sNot = "bare") + " and her " + self.FemBodyParts.Vagina.RandomDescription() + ". 'No panties?' said the " + sWealthyMan + ", 'My, my, you *are* a " + self.BadGirlName.GetWord() + ".' He unbuckled his belt and pulled it off. She tensed as he approached. He put one hand on her " + self.FemBodyParts.Ass.RandomDescription() + " and raised the belt in his fist.\n\n"
			sTweet += "'I'd tell you this will only sting a little,' he said, 'But " + WordList(["we both know that it is going to hurt", "that would be a lie", "I would never lie to a beautiful woman", "this will definitely leave a mark", "if it didn't hurt, it wouldn't be a punishment"]).GetWord() + ".'"
		else:
			sTweet += "'Anything?' he asked, arching an eyebrow. She nodded mutely. 'On your knees, then,' he said. "
			if CoinFlip():
				sTweet += "He slowly unbuckled his belt. Then he "
			else:
				sTweet += "He "
			sTweet += "unzipped his trousers. "	+ sHerName + "'s eyes widened as his " + sManSize + " " + sManPenis + " unfurled. His " + sManBalls + " was " + Penis.Testicles.GetAdj() + " and " + Penis.Testicles.GetAdj() + ", and his " + sManTip + " was inches from her face.\n\n"
			sTweet += WordList(["'You can start by sucking my " + Penis.ShortDescription() + ",' he said.", "'You can start by deep-throating this,' he said.", "'Now suck on my " + Penis.Testicles.MediumDescription() + ",' he said.", "'You will do what I say,' he said, 'and right now I say suck my " + Penis.ShortDescription() + ".'"]).GetWord()
			
		
		return sTweet
		
class Generator38(Generator):
	# Brad entered the bedroom. Marsha was lying on the bed wearing nothing but red high heels. His gaze lingered on her pert breasts, rounded hips, and lush tush. 
	# 'This is a great birthday present babe, he said.
	# 'This isn't your present,' said Marsha.
	# A tall black woman stepped thru the bathroom door. Her sumptuous breasts were full and heavy and her pussy was shaved bare.
	# 'THIS is your birthday present,' Marsha said.
	ID = 38
	Priority = 1
	
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
			
			Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
			for part in Parts:
				if not part == Parts[len(Parts) - 1]:
					sTweet += part + "; "
				else:
					sTweet += "and " + part
			sTweet += ". 'This is a great birthday present, babe,' he said.\n\n"
			sTweet += "'This isn't your present,' said " + sGiverName + "."
			
		else:
			sGiverName = self.MaleName.FirstName()
			sBirthdayName = self.FemaleName.FirstName()
		
			sTweet = sBirthdayName + " entered the bedroom. " + sGiverName + " was wearing nothing but " + WordList(["a cowboy hat", "a leather jacket", "a cock ring", "a bowtie", "a pair of cowboy boots", "a leather body harness"]).GetWord() + " and his " + self.MaleBodyParts.RandomDescription() + " gleamed with oil. Her gazed lingered on his "
			
			Parts = self.MaleBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False)
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
	Priority = 1
	
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
	#Adam walked into the bedroom and froze. His wife and another man were rolling on the bed and their clothes were strewn about the room.\n\n{sex act}\n\n{'My god, Marsha', he said angrily. 'You and the MaleFWB??' / 'Oh Marsha,' he sighed, 'This is revenge for when I titty-fucked my FemaleFWB, isn't it?' / }
	ID = 41
	Priority = 1
	Type = exutil.GeneratorType.Test
	
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
				sTweet += "'" + sHerName + " you " + self.BadGirlName.GetAdj() + " " + self.BadGirlName.GetWord() + "!', " + sHisName + " said. 'I can't believe you two started without me!'"
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
	Priority = 1
	
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
			
			sTweet += " forever. I want to " + self.VSexActByMale.Present() + " you all night long.'"
		
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
		sSkankDesc = self.BadGirlName.GetAdj() + " " + self.BadGirlName.GetWord()
		
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
	Priority = 1
	
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
		
		if CoinFlip():
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
			
			sTweet += WordList(["'Now remember,' she said, 'Just the tip.'", "'And what do you think of my " + Ass.Anus.ShortDescription() + "?' she asked.", "'Pick a hole, baby,' she said.", "'Remember, no butt stuff', she said.", "'The trick is not to wear anything underneath,' she said.", "'I even shaved my " + Vagina.ShortDescription() + " for you,' she said.", "'And what do you think of my " + Vagina.ShortDescription() + "?', she asked."]).GetWord()
			
		
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
	Priority = 1
	
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
		sTweet += " At last he was " + WordList(["balls-deep", "buried to the hilt", "up to his " + Penis.Testicles.RandomDescription(bAllowShortDesc = True)]).GetWord() + " inside her " + Ass.RandomDescription(bAllowShortDesc = True) + ". "
		sTweet += "'" + self.Exclamation.GetWord(bHappy = True, bExMk = False) + ", " + self.TermsOfEndearment.GetWord() + ", you're so tight!' he " + self.VMoan.Past() + ".\n\n"
		
		iRand = randint(1,6)
		
		if iRand == 1:
			Location = LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
			sTweet += "'" + self.Exclamation.GetWord(bHappy = True, bExMk = False).capitalize() + ", " + sHisName + ",' she " + self.VMoan.Past() + ". 'Make me an anal-" + self.BadGirlName.GetNoun() + " right here " + Location.NamePrep + "!'"
		elif iRand == 2:
			Location = locations.LocationSelector().Location(InOut = exutil.LocInOutType.Outdoors)
			sTweet += "'" + self.Exclamation.GetWord(bHappy = True).capitalize() + "' she " + self.VMoan.Past() + ". 'I love the feeling of " + WordList(["doing anal", "getting butt-fucked", "getting ass-fucked", "having my asshole pounded", "anal penetration"]).GetWord() + " " + Location.NamePrep + "!'"
		elif iRand == 3:
			sTweet += "'I've let at least " + WordList(['a dozen','twenty','two dozen','three dozen','fifty','sixty-nine','a hundred','two hundred']).GetWord() + " guys " + self.VThrust.Present() + " my " + self.FemBodyParts.Vagina.ShortDescription() + ", " + self.TermsOfEndearment.GetWord() + ",' she said. 'But you're the only one I'll ever let " + self.VThrust.Present() + " my " + Anus.ShortDescription() + "!'"
		elif iRand == 4:
			sTweet += sHerName + " " + WordList(["squeezed","clenched","contracted","constricted"]).GetWord() + " her " + WordList(["sphincter", "bowels", "anus", "rectum", "asshole"]).GetWord() + " tightly around his " + Penis.ShortDescription() + ". " + sHisName + " " + self.VMoan.Past() + " aloud. 'That means \"I love you\" " + self.TermsOfEndearment.GetWord() + ",' she said to him."
		elif iRand == 5:
			sTweet += "'Whoops! " + self.Exclamation.GetWord(bHappy = False, bExMk = True).capitalize() + "' " + sHerName + " said. 'Hand me that toilet paper, baby.'"
		else:
			sTweet += "'Hurry up and " + self.VEjac.Present() + ", " + self.TermsOfEndearment.GetWord() + ",' she said. '" + self.MaleName.FirstName() + "'s turn is next.'"
		
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
	Priority = 1
	
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
	Priority = 1
	Type = exutil.GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location(PubPrivType = exutil.LocPubPrivType.Public)
		SceneForeplay = scenes.SceneSelector().GetScene(Tags = {exutil.TAG_FOREPLAY}, sHisName = sHisName, sHerName = sHerName, Location = Location)
		ScenePosition = SceneSelector().GetScene(Tags = {exutil.TAG_POSITION}, sHisName = sHisName, sHerName = sHerName, Location = Location)
		SceneClimax = SceneSelector().GetScene(Tags = {exutil.TAG_CLIMAX}, sHisName = sHisName, sHerName = sHerName, Location = Location)
		
		sTweet += Location.BeginDesc + " " 
		sTweet += SceneForeplay.Scene() + " "
		sTweet += ScenePosition.Scene() + " "
		sTweet += SceneClimax.Scene() + "\n\n"
		sTweet += self.AfterSexPunchline.GetPunchline(exutil.Gender.Male)
	

		return sTweet
		
class Generator52(Generator):
	ID = 52
	Priority = 2
	
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
		
class Generator53(Generator):
	ID = 53
	Priority = 1
	Type = exutil.GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		
		Location = locations.LocationSelector().Location()
		MyScene = scenes.SceneRimjobHim(sHisName = sHisName, sHerName = sHerName, Location = Location)
		
		sTweet = Location.BeginDesc + " "
		
		sTweet += MyScene.Scene()
		#sTweet += "\n\n" + TitFuckScene.ShortScene()
		
		return sTweet
		
# 'Gosh, Eduardo,' Tonya panted. 'I need you right now. I want you to pull my panties off, bend me over, 
# spank my trim backside, and then fill me with your big fucking love-meat. Bang my cherry, velvet, 
# glazed entrance until you squirt inside it. I need you to fill me with your delicious, tasty, glossy 
# cream, right here, right now, at the gym!'
class Generator54(Generator):
	ID = 54
	Priority = 1
	
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
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = self.MaleName.FirstName()
		sHerName = self.FemaleName.FirstName()
		VDrip = verbs.VerbDrip()
		
		sTweet = "'No,', thought " + sHerName + ". 'I can never forgive " + sHisName + " for "
		sTweet += WordList(["sleeping with my twin sister", "having anal sex with my step-mom", "rimming my best friend", "drilling the entire cheerleading squad",
			"spooning naked with my sister-in-law", "stepping on my cat", "refusing to go down on me", "drop-kicking my Pomeranian",
			"playing Fantasy Football on our anniversary", "fingering his secretary", "what happened during the threesome", "fingering his step-daughter's butt-hole",
			"showing up drunk to my niece's Bat Mitzvah", "asking me to get implants", "giving me a wet willy", "mistaking my twin sister for me in the shower",
			"getting drunk at my sister's wedding", "getting that tattoo", "giving me that awful tattoo", "telling my ex I was into water sports",
			"giving the pool boy a blowjob", "losing the wedding ring", "calling my mother a fat whore", "titty-fucking my best friend Sarah",
			"sexting my sister", "showing everyone those pictures", "letting my labradoodle escape", "refusing to marry me",
			"suggesting I get breast enhancement surgery", "ruining my favorite dress with semen stains", "puking in my mom's spaghetti",
			"shaving his chest hair", "wearing my lingerie", "farting in my face while we 69'd", "showering with our neighbor",
			"investing in cryptocurrency", "what he did in the sauna with Raoul", "refusing to eat my ass", "getting cum in my eye at church",
			"not being able to find my clitoris", "what he wrote in my yearbook", "ogling my step-mom's tits", "using my dildo without telling me",
			"giving me chlamydia", "calling me 'Karen' in bed", "shaving my maltipoo", "dying my pubes purple", "sharing my mom's nude selfies online",
			"eating out that model", "calling them my 'piss-flaps'", "calling my mother 'a raging thunder cunt'", "putting it in my pooper"]).GetWord() + ". "
		sTweet += WordList(["I have to cut him out of my life once and for all.", 
			"This time we are really through.",
			"This time he has gone too far. We are finished.",
			"I never want to see him again, ever.",
			"I have to let him go, once and for all."]).GetWord() + " "
		sTweet += "No more will I stare at his picture. No more will I think about his "
		sTweet += WordList(["rugged jaw", "broad chest", "brawny shoulders", "full lips", "silken blonde hair", "chiseled abs"]).GetWord() + " or his "
		
		if CoinFlip():
			#penis
			sTweet += self.MaleBodyParts.Penis.FloweryDescription(bAddLen = True)
			if CoinFlip():
				sTweet += " and the way " + self.Semen.RandomDescription() + " " + VDrip.Past() + " from the " + self.MaleBodyParts.Penis.Head.FloweryDescription() 
		else:
			if CoinFlip():
				#ass
				sTweet += self.MaleBodyParts.Ass.FloweryDescription()
			else:
				#testicles
				sTweet += self.MaleBodyParts.Penis.Testicles.FloweryDescription()
			
		sTweet += "."
		
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
	Priority = 1
	
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
		sTweet += sHerName + " " + WordList(["reached under her pillow", "felt under the covers", "reached behind the night-stand"]).GetWord() + " and found the toy. "
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
			sTweet += "\"Is that " + sToy + "?!?\""

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
	Priority = 1
	
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
	Priority = 1
	
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
		sMagicWord = WordList(['Aether','Theophilus','Zanotar','Xholus','Endomius','Sokranos','Devaxatar','Elphias','Tamsin',
							   'Gorth','Evanora','Locasta','Minerva','Morrigan','Alatar','Gwydion','Ommin','Grimmassi','Rasputin']).GetWord()
		
		sTweet += "\"" + sMage.capitalize() + "!\" "
		sTweet += "called out the " + sPrincessAdj1 + " " + sPrincessAdj2 + " princess in " + WordList(['a commanding','a high','an imperious','a thrilling']).GetWord() + " voice, "
		sTweet += "\"I have come for your aid. You must give me a magical talisman with which I can " + Evils.GetWord() + "!\" "
		sTweet += "She swept into the room in a " + DressAdjs.GetWord() + " " + DressColors.GetWord() + " gown which left little to the imagination. "
		sTweet += "The " + sMage + " was " + WordList(['stunned','awed','astounded','dazed','overwhelmed']).GetWord() + " by the beauty of "
		Parts = self.FemBodyParts.GetRandomBodyParts(iNum = 3, bIncludeInners = False, bIncludeIntimate = False)
		for part in Parts:
			if not part == Parts[len(Parts) - 1]:
				sTweet += "her " + part + "; "
			else:
				sTweet += "and her " + part + ".\n\n"
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
	Priority = 1
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
	Priority = 1
	
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
		
# class Generator62(Generator):
	# ID = 62
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator63(Generator):
	# ID = 63
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator63(Generator):
	# ID = 63
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator64(Generator):
	# ID = 64
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator65(Generator):
	# ID = 65
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
# class Generator66(Generator):
	# ID = 66
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
 # class Generator67(Generator):
	# ID = 67
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
				
 # class Generator68(Generator):
	# ID = 68
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
				
 # class Generator69(Generator):
	# ID = 69
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet
		
def GetImgTweetText(gen):
	#the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
	sText = ""
	
	TweetText = []
	TitleBuilder = misc.BookTitleBuilder()
	BookSeller = misc.BookSellers()
	Hashtag = misc.Hashtags()
	SexyAdj = misc.SexyAdjs()
	FavWord = WordList()
		
	if gen.Type != exutil.GeneratorType.BookTitle:
		sText = "'" + TitleBuilder.GetTitle() + "' is coming soon on " + BookSeller.GetWord() + "!"
		for _ in range(4):
			TweetText.append(sText)
		#=============================

		sText = "Check out this " + SexyAdj.GetWord() + " excerpt from '" + TitleBuilder.GetTitle() + "', available soon on " + BookSeller.GetWord() + "!"
		for _ in range(4):
			TweetText.append(sText)
		#=============================
		
	sText = WordList(["Don't hate", "Don't be hatin'", "Don't be hatin' on", "Don't hate on"]).GetWord() + " " + WordList(["me because I'm", "Flaming Lust Bot because it's", "@bot_lust because its", "this bot because it's"]).GetWord() + " " + WordList(["beautiful", "sexy", "hot", "sexxxaaayyyy", "sexy af", "sexxxy", "the hotness", "totes sexy", "sexy for reals"]).GetWord() + ". " + exutil.GetEmoji()
	TweetText.append(sText)
	#=============================
	
	if CoinFlip():
		sText = "This tweet brought to you by"
	else: 
		sText = "Brought to you by"
	sText += " the letters 'S', 'E', and 'X', and by the number 69. " + exutil.GetEmoji()
	TweetText.append(sText)
	#=============================
	
	sText = "\U0001F525I know " + WordList(["you like reading these", "you're into this", "you freaky", "you're into this bot", "you love these", "these kinda get you off", ]).GetWord() + ".\U0001F525 " + WordList(["Don't worry, I won't tell", "Don't worry, your secret is safe with me", "It's cool, it will be our little secret", "No one has to know", "Don't worry, it can stay between you and me"]).GetWord() + ". " + exutil.GetEmoji()
	TweetText.append(sText)
	#=============================

	sText = WordList(["The sex acts", "The sexual positions", "The " + misc.SexyAdjs().GetWord() + " scenarios"]).GetWord() + " depicted are " + WordList(["computer-generated", "algorithmically generated", "entirely fictional", "bot-generated", "extremely hot"]).GetWord() + " and have not been approved by " + WordList(["a doctor","a physician", "a licensed medical practicitioner", "the AMA", "a licensed physician", "a licensed professional"]).GetWord() + ". Do not attempt."
	TweetText.append(sText)
	#=============================
	
	sText = WordList(["You have to retweet this", "Please retweet this", "Favorite this", "Fave this", "You have to favorite this"]).GetWord() + " if it " + WordList(["made you giggle", "made you laugh", "made you smile", "got you hot", "made you blush", "made you grin", "made your privates all tingly", "made your naught bits all tingly", "turned you on", "made you feel hot", "got you going", "did it for you", "made your naughty bits feel good"]).GetWord() + ". " + WordList(["Seriously.", "For real.", "Seriously, though.", "For real, though.", "Okay?", "Pinky swear?"]).GetWord() 
	TweetText.append(sText)
	#=============================
	
	sText = WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + " @erotica_ebooks for more " + WordList(["made-up ebook titles", "funny erotica titles", "machine-generated silliness", "#botlaughs", "ridiculousness", "steamy bot-generated content"]).GetWord() + "!"
	for _ in range(2):
		TweetText.append(sText)
	#=============================
	
	FavWord.List += bodyparts.AnusFemale().NounList
	FavWord.List += bodyparts.Penis().NounList
	FavWord.List += bodyparts.Vagina().AdjList
	FavWord.List += bodyparts.Testicles().NounList 
	FavWord.List += ['bunghole', 'crevice', 'fissure', 'pendulous', 'beefy', 'ravish', 'ample', 'nubile', 'panties', 'lust', 'throbbing', 'turgid', 'tumescent', 'meat', 'gooey', 'juicy', 'moist', 'taint', 'labia', 'pubes', 'scrotal']

	if CoinFlip():
		sText = "My favorite word is '" + FavWord.GetWord() + "'"
	else:
		sText = "The password is '" + FavWord.GetWord() + "'"
	for _ in range(4):
		TweetText.append(sText)
	#=============================

	# it seems that adding any kind of hashtag at all to a bot may lead to shadowbans. so for now I'm not using this.
	iRand = randint(1,6)
	if iRand == 6:
		sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
		while exutil.IsTweetTooLong(sText):
			sText = TweetText[randint(0, len(TweetText) - 1)] + " #" + Hashtag.GetWord()
	else:
		sText = TweetText[randint(0, len(TweetText) - 1)] 
		
	while exutil.IsTweetTooLong(sText):
		sText = TweetText[randint(0, len(TweetText) - 1)] 
	
	return sText 
				
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
		