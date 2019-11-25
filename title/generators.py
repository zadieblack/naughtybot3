#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from util import *
from title.util import *
from names import *
from title.people import *
from title.texttoimg import *
from title.characters import TempType
import misc
import title.misc as titmisc
import title.chargenerator as char

PromoHistoryQ = HistoryQ(2)

class Generator():
	ID = -1
	# each generator should have a unique ID
	Priority = 1
	# increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
	Type = GeneratorType.Normal
	# most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
	
	def SetPriority(self, sText, List, iPriority):
		for x in range(iPriority):
			List.append(sText)
		
	def _getFMs_(self):
		FMs = ""
		
		iRandLen = randint(4,10)
		for x in range(1, iRandLen):
			iRandChoice = randint(1,3)
			if iRandChoice == 1:
				FMs += "F"
			else:
				FMs += "M"
				
		if "M" not in FMs:
			FMs += "M"
		elif "F" not in FMs:
			FMs += "F"
		
		return FMs
	
	def GenerateTweet(self):
		self.VerbsBy = misc.BookVerbsBy()
		self.VerbsTo = misc.BookVerbsTo()
		self.Gerunds = misc.BookGerunds()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		self.SubtitleCoda = titmisc.SubtitleCoda()
		
		return ""

def GetTweetGenerator(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
	gen = None
	GenType = None 
	
	if not Type is None:
		GenType = Type 
	else:
		GenType = None 
	#print("GetTweet() Generator Type is " + str(GenType))
	
	iSwitch = 999
	
	GenSel = GeneratorSelector()
	if bTest:
		gen = GenSel.GetGenerator(iGeneratorNo)
		if gen == None:
			gen = Generator()
	else:
		gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
		
	return gen
	
def GetTweet(bTest, bTweet, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetHistoryQ = None, bAllowFavTweets = True):
	sTweet = ""
	if not bTest and bAllowFavTweets:
		sTweet = GetNextFavTitleFromFile()
	else:
		Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = bAllowPromo)
		# print("Generator ID: " + str(Gen.ID))
		if not TweetHistoryQ is None:
			while bTweet and not TweetHistoryQ.PushToHistoryQ(Gen.ID):
				# print("Generator ID " + str(Gen.ID) + " already in Q")
				Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = bAllowPromo)
				# print("New generator ID: " + str(Gen.ID))
	
		print("Generator ID: " + str(Gen.ID))
		sTweet = Gen.GenerateTweet()
	
	return sTweet
	
class GeneratorPromo(Generator):
	ID = 0
	Priority = 0
	Type = GeneratorType.Promo
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#sTweet = "Blue Diamond: \U0001F539 Eggplant: \U0001F346 Fire: \U0001F525 Laughing: \U0001F923 Robot: \U0001F916 Green Heart: \U0001F49A Blue Heart: \U0001F499 Purple Heart: \U0001F49C No one under 18: \U0001F51E Winking kiss face: \U0001F618 Star: \U00002B50"

		iRand = randint(1,7)
		while not PromoHistoryQ.PushToHistoryQ(iRand):
			iRand = randint(1,7)

		if iRand == 1:
			sTweet = "Reply to " + WordList(["one of my tweets", "an @bot_lust tweet", "a Flaming Lust Bot tweet"]).GetWord() + " for a fun surprise! " + GetEmoji()
			sTweet += "\n\n\U0001F539Reply \"#book\" and I'll respond with a made-up smutty book title."
			sTweet += "\n\U0001F539Reply \"#lovescene\" to get your own custom love scene!"
		elif iRand == 2:
			sTweet = "Tell your family, friends and lovers to follow " + WordList(["@bot_lust", "Flaming Lust Bot", "me", "this bot"]).GetWord() + " for all the steamy, sweaty, silly action!\n" + GetEmoji(randint(1,3))
		elif iRand == 3:
			sTweet = WordList(["@bot_lust", "Flaming Lust Bot", "this bot"]).GetWord() + " is very naughty, and NOT appropriate for anyone under 18! \U0001F51E\n\nThat includes you, " + WordList(["kid who is hiding their phone behind their math book while they check twitter", str(randint(6,11)) + "th grader who is supposed to be doing homework", str(randint(6,11)) + "th grader who is supposed to be reading"]).GetWord() + "!"
			if CoinFlip(): 
				sTweet += " \U0001F928"
		elif iRand == 4:
			sTweet = "I am a twitter bot\U0001F916 designed to automatically generate " + WordList(["hot", "sexy", "naughty", "steamy"]).GetWord() + "\U0001F525, " + WordList(["filthy", "dirty"]).GetWord() + "\U0001F346, and " + WordList(["funny", "hilarious", "ridiculous", "silly"]).GetWord() + "\U0001F923 scenes from the world's worst smutty romance novel!\n\nReply to one of my tweets " + WordList(["and get a surprise!", "if you want more.", "if you're impatient for my next terrible love scene!"]).GetWord()
		elif iRand == 5:
			if CoinFlip():
				sTweet = "Full disclosure: "
			sTweet += "I am a bot\U0001F916!\n\nBut not the Russian kind of bot, the " + WordList(["funny", "sexy", "naughty", "silly", "dirty"]).GetWord() + " kind of bot!" 
			if CoinFlip():
				sTweet += " " + GetEmoji()
			if CoinFlip():
				sTweet += "\n#botlife #twitterbot"
		elif iRand == 6:
			sTweet = "Look what " + WordList(["my followers are", "people are ", "other twitter users are", "the internet is"]).GetWord() + " saying:\n\n\U00002B50'I am hooked on this ridiculous account!'\n\U00002B50'The stuff this bot comes up with is hysterical. XD'\n\U00002B50'[S]imultaneously hilarious, nauseating, and inspiring'\n\n" + WordList(["Thank you!", "Thanks!", "Thank you all!", "Big bot love to everyone!"]).GetWord() 
			sTweet += " " + GetEmoji(randint(1,3))
		else:
			sTweet = WordList(["I love you", "You're the best", "Big Bot Love", "I \U00002764 you"]).GetWord() + ", followers!"
			if CoinFlip():
				sTweet = "*" + sTweet + "*"
			sTweet += "\n\n" + GetHeartEmoji(randint(1,5))
			
		return sTweet
		
class Generator1(Generator):
	# Blackmailed by the Billionaire Mountain Man 
	ID = 1
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, bAllowTrope = True, bAllowRelate = True)
		
		sTweet = self.VerbsBy.GetWord() + " By\n" + Master.Desc
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
		#Girl = char.FemaleChar(TempType = TempType.Flowery, bAddArticle = False, bAllowTrope = True)
		Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowRelate = True, bAllowTrope = True)
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace"]) + " by\n" + Master.Desc
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowRelate = True, bAllowTrope = True)
			
		sTweet = self.VerbsTo.GetWord() + " To\n" + Master.Desc

		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 2
	
	Master = MaleChar()
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
		#Girl = char.FemaleChar(TempType = TempType.Flowery, bAddArticle = False, bAllowTrope = True)
		Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowRelate = True, bAllowTrope = True)
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		GenNotList = ["BDSM"]
		Girl = char.FemaleChar(TempType = TempType.Medium, bAllowTrope = True, NotList = GenNotList)
		Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True,NotList = GenNotList)
		#Girl = FemaleChar(iNumMaxCBits = 2, NotList = ['BDSM'])
		#Master = MaleChar(iNumMaxCBits = 2, NotList = ['BDSM'], bAllowGang = False)
			
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc
		if CoinFlip():
			if CoinFlip():
				sTweet += ":\nA BDSM " + self.SubtitleCoda.GetWord()
			else:
				sTweet += ":\nA Hot Ménage"
		
		return sTweet
		
class Generator6(Generator):
	# Seduced in the Bed of the Billionaire	
	ID = 6
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", 
					"Gifted", "Pledged", "Bed", "Sex Dungeon","Basement"]
		
		#Girl = char.FemaleChar(TempType = TempType.Medium, bAllowTrope = True, NotList = GenNotList)
		Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True,bAddTheArticle = True)
		#Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = NotList, bAddArticle = True)
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		else:
			sTweet = self.VerbsBy.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		
		return sTweet
		
# class Generator7(Generator):
	# # The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	# ID = 7
	# Priority = 1
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Master1 = MaleChar(iNumMaxCBits = 2, bAllowGang = False)
		# Master2 = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		# Girl = FemaleChar(iNumMaxCBits = 2)
		# sTweet = "The " + Girl.Desc + ",\nThe " + Master1.Desc + ",\n& " + Master2.Desc + ":\n"
		# if CoinFlip():
			# sTweet += "A Hot Ménage"
		# else:
			# sTweet += "A " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		# return sTweet

class Generator8(Generator):
	# My Boyfriend is a Secret Daddy Dom 
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single"]
		Girl = char.FemaleChar(TempType = TempType.Medium, bAllowTrope = True, NotList = NotList)
		Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True,NotList = NotList,bAddAnArticle = True)
		#Girl = FemaleChar(iNumMaxCBits = 2)
		#Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single"])
		sTweet = "My " + WordList(["Boyfriend", "Hot Date", "Fiancé", "Blind Date", "Kidnapper"]).GetWord() + " is " + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + AddArticles(Girl.Desc, bMakeUpper = True) + " " + self.SubtitleCoda.GetWord()
		else:
			sTweet += "!"
			
		return sTweet
		
class Generator9(Generator):
	# The Secretary and the Space Werewolf 
	ID = 9
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["BDSM"]
		Girl = char.FemaleChar(TempType = TempType.Medium, bAllowRelate = True, bAllowTrope = True, bAllowSpecies = False, NotList = NotList)
		Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True, bAddTheArticle = True, sPosArticle = "Her", NotList = NotList)
		
		sTweet = "The " + Girl.Desc + "\nand\n" + Master.Desc 
		sTweet += ":\n" + AddArticles(WordList([self._getFMs_(), 
												"BDSM", 
												misc.SexyAdjs().GetWord().capitalize()]).GetWord()) + " " 
		sTweet += self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = char.MaleChar(bAddTheArticle = True, sPosArticle = "My", bAllowRelate = True)

		sTweet = "Baby For " + Master.Desc

		return sTweet
		
# class Generator11(Generator):
	The Millionaire Sherrif's Virgin
	# ID = 11
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Master = char.MaleChar(TempType = TempType.Medium)
		# Girl = char.FemaleChar(bAllowRelate = True)
		
		# sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc

		# return sTweet
		
# class Generator12(Generator):
	# # Babysitter to the Billionaire Uniporn
	# ID = 12
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar(iNumMaxCBits = 2)
		# Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		# sTweet = Girl.Desc + "\nto\n" + Master.Desc
		
		# return sTweet
		
# class Generator13(Generator):	
	# # Babysitter for the Billionaire Uniporn
	# ID = 13
	# Priority = 3
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar(iNumMaxCBits = 2)
		# Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		# sTweet = Girl.Desc + "\nfor\n" + Master.Desc
		# if CoinFlip():
			# sTweet += ":\n" + WordList(["An " + self._getFMs_(),"A BDSM","A Forbidden"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		# return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GangNot = ["Dapper","Gang-Bang"]
		
		GoodGirl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowSexuality = False, bAllowSpecies = False)
		BadGirl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = True)
		MasterGang = MaleGangChar(iNumMaxCBits = 3, NotList = GangNot, bAllowAttitude = False)
		
		Tweets = []
		
		Tweets.append(GoodGirl.Desc + "\nHas a Gang Bang with\nThe " + MasterGang.Desc) 
		Tweets.append(BadGirl.Desc + "\nHas a Gang Bang with\nThe " + MasterGang.Desc )
		Tweets.append(GoodGirl.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\nThe " + MasterGang.Desc)
		Tweets.append(BadGirl.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\nThe " + MasterGang.Desc)
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]
		
		return sTweet
		
# class Generator15(Generator):
	# # The Small-Town Virgin's First Porno
	# ID = 15
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowSexuality = False, bAllowTitle = False)
		
		# sTweet = Girl.Desc + "'s\nFirst Porno"
		# if CoinFlip():
			# sTweet += ":\nAn " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()

		# return sTweet
		
# class Generator16(Generator):
	# # The Small-Town Virgin's First Time
		
	# ID = 16
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["MILF", "Concubine", "Wife", "Pregnant", "Mom", "Sex", "Divorced", "Virgin"], bAddArticle = True, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False)

		# sTweet = Girl.Desc + " " + WordList(["Virgin", "Virgin", "Virgin", "Anal Virgin"]).GetWord() + "'s\nFirst Time"
		# if CoinFlip():
			# sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Secret", "An S&M", "A Rough Sex", "An Anal", "A Gang-Bang"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		# return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Mountain Man Biker Gang 
	ID = 17
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlNotList = ["Recently-Divorced","Sassy","Tanned","Kitten","Harem","Ice Queen","MILF"]
		Subtitles = []
		
		Master = MaleChar(iNumMaxCBits = 3)
		Gang = MaleGangChar(iNumMaxCBits = 3)
		
		VerbNotList = ['Taken']
		sTweet = self.VerbsBy.GetWord(NotList = VerbNotList) + ":\n"
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = GirlNotList, bAllowClothing = False, bAllowSexuality = False, bAllowGenMod = False, bAllowSpecies = False, bAllowTitle = False)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Gang.Desc)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Master.Desc)
		Subtitles.append(AddArticles(Girl.Desc) + "\n" + WordList(['Adventure','Encounter','Liason','Experience','Episode','Rendezvous']).GetWord())
		
		sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlNotList = ["Sex", "Lesbian","BDSM","Tanned","Recently-Divorced","Sassy","Tanned","Kitten","Harem","Ice Queen","MILF"]
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = GirlNotList, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowClothing = False, bAllowSexuality = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet += "\"" + WordList(["S@*#!", "Oh No!", "Uh Oh!", "Whoops!", "WTF?!?", "Oh F*@%!"]).GetWord() + " " 
		sTweet += "My\n" + Girl.Desc + " " + WordList(["Girlfriend", "Bride", "Wife", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Step-Sister", "Twin Sister", "Mom", "Wife"]).GetWord() + "\n"
		sTweet += "Is " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", 
									"An Anal Porn Star", "An Erotic Model", "A Kinky Fetish Model", "A Slut", "A Butt Slut", "A High-Class Hooker",
									"A Slutty Bikini Model", "A Wanton Slut", "An Erotica Author"]).GetWord() + "!\""
		
		return sTweet
		
class Generator19(Generator):
	# Full Frontal for the Shy Amish Virgin: A BDSM Romance
	ID = 19
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["Naked", "Nude", "Nudist"], bAddArticle = True)
		Master = MaleChar(iNumMaxCBits = 3)
		
		if CoinFlip():
			sTweet = "Full Frontal Nudity for\n" + Girl.Desc
		else:
			if CoinFlip():
				sTweet = WordList(["Naked in Public", "Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["For\nThe", "For\nMy"]).GetWord() + " " + Master.Desc
			else:
				sTweet = WordList(["Stripped Bare", "Stripped Naked", "Stripped in Public", "Commanded to Strip", "Commanded to Strip in Public", "Forced to Go Naked in Public", "Ordered to Strip"]).GetWord() + " " + WordList(["By\nThe", "By\nMy"]).GetWord() + " " + Master.Desc
		
		# if CoinFlip():
			# sTweet += ":\n" + WordList(["An " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "A Submissive"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, bAddArticle = False, bAllowRelate = False)
		Gang = MaleGangChar(iNumMaxCBits = 3, bAddArticle = False)
		
		sTweet = ""

		sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
		sTweet = "\"I Was " + sVerbBy
		sTweet += " By\n"
		if CoinFlip():
			sTweet += AddArticles(Master.Desc)
		else:
			sTweet += Gang.Desc
		sTweet += ",\nAnd I Liked It\""

		return sTweet
		
class Generator21(Generator):
	# Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
	ID = 21
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = self.VerbsBy.GetWord()  + " By\n"
		sTweet += Master.Desc 
		#sTweet += AddArticles(Girl.Desc) + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
	ID = 22
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlGood = FemaleChar(iNumMaxCBits = 2, Type = GirlType.Good)
		GirlLes = LesbianChar(iNumMaxCBits = 3)
		GirlBad = LesbianChar(iNumMaxCBits = 3, Type = GirlType.Bad)

		
		if CoinFlip():
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlLes.Desc
		else:
			sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlBad.Desc
		sTweet += ":\n" + WordList(["A Lesbian","A Secret Lesbian","A Taboo Lesbian","A Forbidden",  "An FF",]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator23(Generator):
	# The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
	ID = 23
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = title.names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar(iNumMaxCBits = 2).Desc)
		GayTitles.append("The " + GayChar(iNumMaxCBits = 2).Desc + "\nand\nThe " + GayChar().Desc) 
		GayTitles.append("The " + MaleChar(iNumMaxCBits = 2, bAllowGang = False).Desc + "\nand\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + GayChar().Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret Gay","A Taboo","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator24(Generator):
	# Deep-Throating My Well-Hung Sumo-Wrestler Step-Dad
	ID = 24
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Gerunds = WordList(['Bedding','Cuddling','Deep-Throating','Double-Teaming','Dry-Humping','Fellating','Going Down on',
							'Hooking Up With','Humping','Jerking Off','Licking','Pegging','Riding','Rimming','Shagging',
							'Showering With','Sixty-Nining','Sleeping With','Spooning','Straddling','Teasing'])
		Master = MaleChar(iNumMaxCBits = 4, bAddArticle = True, bAllowRelate = True)
	
		sTweet = Gerunds.GetWord() + " " + Master.Desc
		
		return sTweet
		
class Generator25(Generator):
	# Greg Gets Pounded In The Butt By The Motorcycle Gang
	ID = 25
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHisName = title.names.NamesMale().FirstName()

		GayTitles = []
		
		GayTitles.append("Pounded In The Butt By\nThe Gay " + MaleGangChar().Desc)
		GayTitles.append("Pounded In The Butt By\n" + GayChar(bAddArticle = True).Desc)
		GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By\nThe " + GayChar().Desc)
		GayTitles.append(sHisName + " and\nThe " + WordList(["Well-Hung", "Well-Endowed"]).GetWord() + " " + GayChar(iNumMaxCBits = 2, NotList = ["Well-Hung", "Well-Endowed"]).Desc)
		
		sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
		sTweet += ":\n" + WordList(["A Gay","A Secret","A Taboo Gay","A Forbidden", "A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
# class Generator26(Generator):
	# # Hotwife for Daddy: A BDSM Romance 
	# ID = 26
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar()
		
		# sTweet = AddArticles(Girl.Desc) + "\nFor Daddy:\n"
		# sTweet += WordList(["A BDSM","An " + self._getFMs_() + "", "A Taboo", "A Forbidden", "A Forbidden", "A Naughty"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		# return sTweet
		
class Generator27(Generator):
	# The Shy Lesbian Gymnast Wore Black
	ID = 27
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"], bAddArticle = True, bAllowRelate = True)
		
		sTweet = Girl.Desc + "\nWore " + WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "A Strap-On"]).GetWord() + ":\n"
		sTweet += "A " + WordList(["FemDom", "Dominatrix", "BDSM", "Cuckold", "MILF"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet

class Generator28(Generator):
	#Cuckolded By My Amish Maiden Hotwife
	ID = 28
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, bAddEndNoun = False, bAllowMaritalStatus = False, NotList = ['Single', 'Divorced'])
		
		if CoinFlip():
			sTweet = "Cuckolded By My\n" + Girl.Desc + " " + WordList(['Wife', 'Wife', 'Hotwife', 'Fiancé', 'Girlfriend', 'Mistress']).GetWord()
		else:
			sTweet = "My " + WordList(['Wife', 'Wife', 'Hotwife', 'MILF']).GetWord() + " And The\n" + MaleChar(bAllowMaritalStatus = False).Desc + ":\nA Cuckold " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator29(Generator):
	# Blackmailing My Step-Dad's Busty Ballerina
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlNotList = ["Girlfriend", "Mom", "Dad", "Sister", "Divorced", "Single", "Hotwife", "Virgin", 
						"Pastor's Wife", "Housewife", "Lesbian", "Bridesmaid", "Nun"]
		Girl = FemaleChar(iNumMaxCBits = 3, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False, NotList = GirlNotList, bAllowSexuality = False)
		
		iRand = randint(1,4)
		sTweet = self.Gerunds.GetWord() + " "
		if iRand == 1:
			sTweet += "My " + WordList(["Father's", "Dad's", "Step-Dad's"]).GetWord() + "\n"
			sTweet += Girl.Desc + " " + WordList(["Wife", "Girlfriend", "Fiancé", "Hotwife", "Bride"]).GetWord()
		elif iRand == 2:
			sTweet += "My " + WordList(["Son's", "Step-Son's"]).GetWord() + "\n"
			sTweet += Girl.Desc + " " + WordList(["Wife", "Wife", "Girlfriend", "Fiancé", "Hotwife", "Bride"]).GetWord()
		elif iRand == 3:
			sTweet += "My " + WordList(["Best Friend's", "Neighbor's", "Boss's"]).GetWord() + "\n"
			sTweet += Girl.Desc + " " + WordList(["Bride", "Wife", "Wife", "Girlfriend", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Hotwife", "Mom", "Step-Mom"]).GetWord()
		else: 
			sTweet += "My " + WordList(["Sister's","Step-Sister's","Mom's","Step-Mom's","Daughter's","Step-Daughter's"]).GetWord() + "\n"
			sTweet += "Lesbian " + Girl.Desc + " " + WordList(["Wife", "Girlfriend"]).GetWord()
		
		return sTweet
		
class Generator30(Generator):
	# Bubbly & Plump: 
	# The Chaste Small-Town Girl Barista 
	# Rides a Veiny 9-inch Dick
	ID = 30
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotGirlList = ["Harem Princess","Slave","Queen","Heiress","Divorced"]
		AdjNotList = ["Bikini-Bod","Anal Virgin","Shave","Big-Titty","Little"]
		
		PhysChars = title.misc.PhysCharFemale()

		sAdj1 = title.misc.AttitudeGoodFemale().GetWord(NotList = AdjNotList)
		sAdj2 = PhysChars.GetWord(NotList = AdjNotList + [sAdj1])
			
		NotGirlList = NotGirlList + [sAdj1,sAdj2]
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, Type = GirlType.Good, NotList = NotGirlList,
							bAllowSpecies = False, bAllowSexuality = False, bAllowClothing = False, bAllowTitle = False, 
							bAllowAttitude = False, bAllowPhysChar = False,
							bAddArticle = True) 
		
		sTweet = sAdj1 + " & " + sAdj2 + ":\n"
		sTweet += Girl.Desc + "\n"
			
		iRand = randint(1,15)
		if iRand < 3:
			sTweet += "Exposes Her Naked Body " + WordList(["in a Wal-Mart","on Main Street","at the Grocery Store",
															"at the Mall","Downtown","on Campus","in Traffic",
															"at the Office","on the Beach","at the Park",
															"at Disneyland","on the Jumbotron"]).GetWord()
		elif iRand == 3:
			sTweet += "Has Her First " + WordList(["Threesome","Three-Way","Orgy"]).GetWord()
		elif iRand == 4:
			sTweet += "Has a " + WordList(["4","5","6","8","10","12","20","30","60"]).GetWord() + "-guy Gangbang"
		elif iRand == 5:
			sTweet += "Gets Her Cherry Popped"
		elif iRand == 6:
			sTweet += "Gets Her Anal Cherry Popped"
		elif iRand == 7:
			sTweet += "Goes Down On " + WordList(["a Butch Lesbian","Another Woman","Her Best Friend","Her Lesbian Boss",
												  "Her Maid of Honor","Her Bridesmaid","Her Mother-in-Law"]).GetWord()
		elif iRand == 8:
			sTweet += "Makes a Porno"
		elif iRand == 9:
			sTweet += "Tries Anal"
		elif iRand == 10:
			sTweet += "Wears a Butt Plug"
		elif iRand == 11:
			sTweet += "Tries a Glory Hole"
		elif iRand == 12:
			sTweet += "Pounds " + NamesMale().FirstName() + " with a Strap-On"
		else:
			ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
						  "Throbbing","Meaty","Burning","Dripping","Lustful","Passionate","Massive","Fat",
						  "Throbbing","Pulsating","Dripping","Black","Stiff","Girthy"])
			sTweet += WordList(["Rides","Sucks","Mounts","Takes"]).GetWord() + " "
			sTweet += AddArticles(ErectAdjs.GetWord()) + " " 
			sTweet += WordList(["Seven","Seven 1/2","Eight","Eight 1/2","Nine","Nine 1/2","Ten","Ten 1/2",
								"Eleven","Eleven 1/2","Twelve","Thirteen","Fourteen"]).GetWord() + "-inch "
			sTweet += WordList(["Dick","Cock","Boner","Prick","Tool"]).GetWord()
			
			

		return sTweet
		
class Generator31(Generator):
	# Wanton & Willing: 
	# My Kinky Lesbian Leather-Clad Dominatrix
	# Pegs Me With a Strap-On
	ID = 31
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotGirlList = ["Harem Princess"]
		Girl = FemaleChar(iNumMinCBits = 3, Type = GirlType.Bad, NotList = NotGirlList, bAllowSpecies = False)

		sAdj1 = ""
		sAdj2 = ""
		if CoinFlip():
			sAdj1 = title.misc.PhysCharFemale().GetWord()
			sAdj2 = title.misc.AttitudeBadFemale().GetWord()
		else:
			sAdj1 = title.misc.AttitudeBadFemale().GetWord()
			sAdj2 = title.misc.PhysCharFemale().GetWord()
			
		sHerName = NamesFemale().FirstName()
		
		sTweet = sAdj1 + " & " + sAdj2 + ":\n"
		
		if CoinFlip():
			sTweet += "My " + Girl.Desc + "\n"
		else:
			sTweet += sHerName + " the " + Girl.Desc + "\n"
			
		iRand = randint(1,13)
		if iRand < 3:
			ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
						  "Throbbing","Meaty","Burning","Dripping","Purple","Red","Fleshy","Lustful","Passionate",
						  "Throbbing","Pulsating","Vigorous","Virile","Moist","Black","Stiff","Girthy"])
			sTweet += "Gets a " + ErectAdjs.GetWord() + " " + str(randint(7,12)) + "\" Surprise"
		elif iRand == 3:
			sTweet += "Makes Her First " + WordList(["Lesbian","Hardcore","Anal","Gangbang","Creampie","Bondage"]).GetWord() + " Porno"
		elif iRand == 4:
			sTweet += "Gets Her " + WordList(["Nipples","Clit","Labia","Taint","Ass Dimples"]).GetWord() + " Pierced"
		elif iRand == 5:
			Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
			"at the Chic-fil-a","in the Ball Pit","at the Park","at the Beach","Under an Overpass","at the Gym",
			"on the Eliptical Machine at the Gym","at the Seafood Restaurant","at the Museum","at Burger King",
			"at the Library","at the Farmer's Market","next to the Duck Pond","at Church","at the Bar",
			"in the Window Display of a Shoe Store","at Wal-Mart","at Starbucks","at School","on Campus",
			"in the Church Graveyard","at a Construction Site","at Rush Hour Traffic","at Her Uber Driver",
			"on a Hotel Balcony","Beside the Bike Path","at the Mail Man","at the Amazon Delivery Guy",
			"Behind the Bleachers","In the Back of a Ford 150","In a Movie Theater","at Chipotle","at Barnes & Noble",
			"at Whole Foods","at the Mall","at the CVS"
			])
			sTweet += "Flashes Her " + WordList(["Tits","Ass","Pussy"]).GetWord() + " " + Places.GetWord()
		elif iRand == 6:
			sTweet += "Has Her First " + WordList(["Threesome","Foursome","Fivesome","Orgy","Gang Bang","Black Gang Bang"]).GetWord()
		elif iRand == 7:
			sTweet += "Has a " + WordList(["Dick","Cock","Penis","Prick"]).GetWord()
		elif iRand == 8:
			sTweet += "Tries a Glory Hole"
		elif iRand == 9:
			sTweet += "Gets " + WordList(["Fisted","Fisted","Anal Fisted"]).GetWord()
		elif iRand > 10 and iRand < 12:
			sTweet += WordList(["Wants","Craves","Is Horny for","Begs for"]).GetWord() + " " 
			sTweet += WordList(["Her Neighbor's","Her Step-Brother's","Her Professor's","Her Teacher's","Her Boss's",
								"Her Step-Dad's","Her Uncle's","Her Gym Coach's","Her Gynecologist's","A Stranger's"]).GetWord() + " "
			sTweet += WordList(["Dick","D","Cock","Hard Cock","Fat Dick","Dingus","Meat Stick","Flesh Pole","Fat Boner"]).GetWord()
		else: 
			sTweet += "Is Wearing " + WordList(["a Butt Plug","an Anal Hook","Nipple Clamps","a Ball Gag","a Clit Clamp",
												"Crotchless Panties","a Strap-On","a Remote-Controlled Vibrator",
												"Anal Beads"]).GetWord()
		return sTweet
		
class Generator32(Generator):
	#Stripping For My Best Friend's Cocky Coal-Miner Brother 
	ID = 32
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		#print(misc.RelateMale().List + misc.MaritalStatusMale().List)
		if CoinFlip():
			Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ['Single', 'Man', 'Dad', 'Father', 'Brother', 'Son'], bAllowMaritalStatus = False, bAllowRelate = False)
			if Master.Desc[-3:] == "Man":
				sMaster = Master.Desc[0:-4]
			else:
				sMaster = Master.Desc
			sTweet = WordList(["Sleeping With", "Hooking Up With", "Tempting", "Seducing", "Bedding", "Stripping For", "Secretly Watching", "Showering With", "Spying On", "Sharing", "Playing With", "Claimed By", "Taken By", "Deflowered By", "Dominated By", "Blackmailed By", "Stripped By", "Tied to the Bed By", "Pleasured By", "Spanked By", "Ravished By", "Taken Hard By", "Massaged By", "Going Down On", "Impregnated By"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Daughter", "Sister", "Step-Sister", "Step-Daughter"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Boyfriend", "Fiancé", "Husband", "Hubby"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Step-Mom", "Mom", "Mother"]).GetWord() + "'s\n"
				sTweet += sMaster + " " + WordList(["Brother", "Boyfriend", "Boyfriend", "Step-Brother"]).GetWord()
			else:	
				sTweet += "My Best Friend's\n"
				sTweet += sMaster + " " + WordList(["Son", "Brother", "Boyfriend", "Fiancé", "Husband", "Dad", "Father", "Hubby", "Step-Dad"]).GetWord()
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, NotList = ['Single','Virgin', 'Girl', 'Woman', 'Mom', 'Sister', 'Mother', 'Daughter', 'Lesbian', 'Maiden', 'Wife'], bAllowMaritalStatus = False, bAllowRelate = False, bAllowTitle = False)
			if Girl.Desc[-4:] == "Girl":
				sGirl = Girl.Desc[0:-5]
			elif Girl.Desc[-5:] == "Woman":
				sGirl = Girl.Desc[0:-6]
			else:
				sGirl = Girl.Desc
			sTweet = WordList(["Sleeping With", "Seducing", "Massaging", "Bedding", "Undressing", "Secretly Watching", "Spying On", "Sharing", "Showering With", "Stripping", "Playing With", "Claiming", "Spanking", "Punishing", "Deflowering", "Going Down On", "Blackmailing", "Pleasuring", "Impregnating"]).GetWord() + "\n"
			if CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Brother", "Step-Brother", "Step-Son", "Son"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Girlfriend", "Fiancé", "Wife"]).GetWord()
			elif CoinFlip():
				sTweet += "My " + WordList(["Best Friend", "Father", "Dad", "Step-Dad"]).GetWord() + "'s\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Girlfriend", "Step-Sister"]).GetWord()
			else:
				sTweet += "My Best Friend's\n"
				sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Step-Sister", "Daughter", "Step-Daughter", "Fiancé", "Wife", "Step-Mom", "Mom", "Mother"]).GetWord()
			
		return sTweet
		
class Generator33(Generator):
	#Milking Marie: A Pan-sexual Cheerleader Affair
	ID = 33
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 4)
		sTweet = sVerb + " " + self.HerName + ":\n"
		sTweet += AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord()

		return sTweet
		
# Rimming the Uptight Librarian Futa
# and her Mom
class Generator34(Generator):
	ID = 34
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True)
		sTweet = sVerb + " " + Girl.Desc
		
		sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 
											'Twin Sister', 'Best Friend', 'Lesbian Lover', 'Mom']).GetWord()

		return sTweet
		
class Generator35(Generator):
	ID = 35
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = WordList(['Arousing',
			'Bedding',
			'Bending Over For',
			'Cuckolding',
			'Deep-Throating',
			'Dominating',
			'Fellating',
			'Gagging On',
			'Going Down On',
			'Massaging',
			'Pegging',
			'Playing With',
			'Pleasing',
			'Riding',
			'Rimming',
			'Seducing',
			'Sitting On',
			'Sharing',
			'Showering With',
			'Smothering',
			'Straddling',
			'Stroking',
			'Stripping For',
			'Submitting To',
			'Swallowing',
			'Teaching',
			'Teasing',
			'Tempting',
			'Touching Myself For',
			'Whipping']).GetWord()
		
		Master = MaleChar(iNumMinCBits = 2, bAllowGang = False)
		sTweet = sVerb + " Mr. " + AuthorLastNames().GetWord() + ":\n"
		sTweet += "My " + self.SubtitleCoda.GetWord(NotList = ['Story']) + " With A\n" + Master.Desc

		return sTweet
		
class Generator36(Generator):
	#Turned Gay
	ID = 36
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAllowSexuality = False)
			
			if CoinFlip():
				Lesbian = LesbianChar(bAddArticle = True, NotList = ['wife','girlfriend', 'married'])
				sTweet = "Turned Lesbo by " + Lesbian.Desc
			else:
				Lesbian = LesbianChar(NotList = ['wife','girlfriend', 'married', 'lesbian'])
				sTweet = "Straight " + Girl.Desc + "\nfor the \nLesbian " + Lesbian.Desc 
			
		else:
			Man = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
			
			if CoinFlip():
				Gay = GayChar(bAddArticle = True, NotList = ['husband','boyfriend', 'married'])
				sTweet = "Turned Gay by " + Gay.Desc
			else:
				Gay = GayChar(NotList = ['husband','boyfriend', 'married', 'gay'])
				sTweet = "Straight " + Man.Desc + "\nfor the\nGay " + Gay.Desc 

		return sTweet
		
class Generator37(Generator):
	# Showering With My Step-Mom
	ID = 37
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		
		Relations = title.misc.RelateFemale()
		Gerunds = self.Gerunds
		
		Tweets.append("My " + FemaleChar(bAddEndNoun = False).Desc + " " + Relations.GetWord(NotList = ['Girlfriend', 'Wife', 'Mistress']) + ":\n" + AddArticles(WordList(['Taboo', 'Taboo', 'Naughty', 'Forbidden', 'Secret', 'Erotic', 'Steamy']).GetWord()) + " " + self.SubtitleCoda.GetWord())
		Tweets.append(Gerunds.GetWord() + " My " + FemaleChar(bAddEndNoun = False).Desc + " " + Relations.GetWord(NotList = ['Girlfriend', 'Wife', 'Mistress']))
		Tweets.append("My " + Relations.GetWord() + "\nIs A\n" + FemaleChar(bAddEndNoun = True).Desc)
		Tweets.append(Gerunds.GetWord() + " "  + self.HerName + ":\n" + AddArticles(Relations.GetWord(NotList = ['Wife','Girlfriend', 'Mistress'])) + " " + self.SubtitleCoda.GetWord())
		
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]

		return sTweet
		
class Generator38(Generator):
	# My New Step-Dad Is A Visibly-Erect Centaur
	ID = 38
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		
		NotList = ['Husband', 'Boyfriend', 'Hubby', 'Widower', 'Fiancé']
		Relations = title.misc.RelateMale()
		Gerunds = self.Gerunds
		
		Tweets.append("Me And My\n" + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList) + ":\n" + AddArticles(WordList(['Taboo', 'Taboo', 'Naughty', 'Forbidden', 'Secret', 'Erotic', 'Steamy']).GetWord()) + " " + self.SubtitleCoda.GetWord())
		Tweets.append(self.VerbsBy.GetWord() + " By My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList))
		Tweets.append(self.VerbsTo.GetWord() + " To My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList))
		Tweets.append("My New " + Relations.GetWord() + "\nIs A\n" + MaleChar(bAddEndNoun = True, bAllowGang = False, bAllowMaritalStatus = False).Desc)
		Tweets.append(self.VerbsBy.GetWord() + " By My " + Relations.GetWord(NotList = NotList) + ":\n" + AddArticles(MaleChar(bAllowGang = False, bAllowMaritalStatus = False).Desc) + " " + self.SubtitleCoda.GetWord())
		Tweets.append("\"Oh No! " + WordList(["I'm In Love With", "I Have A Crush On", "I Slept With", "I'm Being Blackmailed By", "I'm Horny For", "I'm Turned On By"]).GetWord() + " My " + MaleChar(bAddEndNoun = False, bAllowGang = False, bAllowMaritalStatus = False).Desc + " " + Relations.GetWord(NotList = NotList) + "\"!")
		
		sTweet = Tweets[randint(0, len(Tweets) - 1)]

		return sTweet
		
class Generator39(Generator):
	# Taken Hard By My Big Black Biker 
	ID = 39
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Tweets = []
		NotList = ["Big", "Black", "BBC"]
		
		Tweets.append(self.VerbsBy.GetWord() + " by the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.VerbsTo.GetWord() + " to the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Gets " + self.VerbsBy.GetWord() + "\nby the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Gets " + self.VerbsTo.GetWord() + "\nto the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " and the\nBig Black " + MaleChar(NotList = NotList, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc)
		Tweets.append(self.HerName + " Goes Black for the\n" + MaleChar(NotList = NotList, bAddEndNoun = False, bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False).Desc + " BBC")
		Tweets.append(FemaleChar(Type = GirlType.Good, bAddArticle = True, NotList = ["Black", "Ebony"]).Desc + "\nGoes Black")

		sTweet = Tweets[randint(0, len(Tweets) - 1)]
		
		return sTweet

# class Generator40(Generator):
	# # I Was Ridden Bareback By A Burly Lumberjack Businessman, And He's Not My Husband!
	# ID = 40
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# NotVerbs = ['Tempted', 'Beaten', 'Broken', 'Captured', 'Caught', 'Charmed', 'Cuddled', 'Hotwifed', 'Ruled', 'Seduced', 'Tamed', 'Trained']
		
		# Master = MaleChar(iNumMaxCBits = 4, bAllowGang = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False)
		# if CoinFlip():
			# sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nAnd He's Not Her Husband!"
		# else:
			# sTweet = "I Was " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nWho Was Not My Husband!"

		# return sTweet
		
class Generator41(Generator):
	#Seducing Sheryl: The Virginal Nurse and the Big Titty Dominatrix
	ID = 41
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Gerunds = WordList(["Seducing", "Tempting", "Corrupting", "Degrading", "Debauching", "Perverting", "Whipping",
							"Fisting", "Sixty-Nining", "Scissoring", "Tribbing", "Fingering"])
		GoodGirl = FemaleChar(Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowGenMod = False, bAllowPregState = False, bAllowMaritalStatus = False, bAllowSexuality = False, bAllowSpecies = False)
		BadGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = True, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet = Gerunds.GetWord() + " " + self.HerName + ":\n"
		sTweet += GoodGirl.Desc + "\nand\n" + BadGirl.Desc 

		return sTweet
		
class Generator42(Generator):
	# Charmed by the Hot Italian Count
	ID = 42
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]
		Nation = title.misc.NationMale()
		Title = title.misc.TitlesMale()
		
		Master = MaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowRelate = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowTitle = False, bAllowAge = False, bAllowProf = False)
		
		Tweets = []
		
		Tweets.append(self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]) + "\nby the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())
		Tweets.append("In the " + WordList(["Bed", "Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem"]).GetWord() + " of the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())
		Tweets.append(self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Public"]) + "\nin the " + WordList(["Bed", "Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem"]).GetWord() + " of the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord())

		return Tweets[randint(0, len(Tweets) - 1)]

class Generator43(Generator):
	# Secret Baby for the Well-Hung Italian Count 
	ID = 43
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Nation = title.misc.NationMale()
		Title = title.misc.TitlesMale()
		
		Master = MaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowRelate = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowTitle = False, bAllowAge = False, bAllowProf = False)
		sTweet = WordList(["Secret Baby", "Illegal Baby", "Baby", "Twin Babies", "Secret Twin Babies", "Fertile Surrogate", "Secret Surrogate", "Pregnant", "Secretly Pregnant", "Illegally Pregnant"]).GetWord() + " for the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord()
		
		return sTweet
		
# class Generator44(Generator):
	# # The Amish French Maid Goes Dogging 
	# ID = 44
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Girl = FemaleChar(iNumMaxCBits = 4, bAddArticle = True, bAllowRelate = True, bAllowSexuality = False, bAllowSpecies = False)
		# Suffixes = WordList(["Spreads Her Legs", "Spreads Her Legs", "Rides Again", "Puts Out", "Takes It Deep", "Rides A Big One", "Spreads Her Cheeks", "Takes A Roll In The Hay", "Assumes the Position", "Goes Down", "Has a Quickie", "Bends Over", "Goes Dogging", "Gets Laid", "Knocks Boots", "Does the Rumpy Pumpy", "Gets Off", "Goes All The Way", "Drops Her Pants"])

		# sTweet = Girl.Desc + "\n" + Suffixes.GetWord()
		
		# return sTweet
		
class Generator45(Generator):
	# Naked in the Park: A Sweet Wholesome Cheerleader Adventure
	ID = 45
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NudeActions = WordList(["Naked", "Flashing", "Streaking", "Topless", "Pantsless", "Exposing Herself", "Nude"])
		Places = WordList(["in the Park", "on Main Street", "at the Bank", "at the Bar", "in the Pub", "at the Grocery Store", "at the Gym", "at the Beach", "on Campus", "at the Museum"])
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Nudist"], bAllowClothing = False, bAllowSpecies = False, bAllowSexuality = False)
		
		sTweet = NudeActions.GetWord() + " " + Places.GetWord() + ":\nA " + Girl.Desc + " Adventure"
		return sTweet

class Generator46(Generator):
	ID = 46
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		if CoinFlip():
			Master = MaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["boyfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False, bAllowTrope = False)
			Relations = title.misc.RelateMale()
			Prefix = WordList(["Secretly In Love With"])
			sTweet = Prefix.GetWord() + "\nMy " + Master.Desc + " " + Relations.GetWord(NotList = ["Boyfriend", "Husband", "Hubbie", "Widower", "Fiancé"])
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["girlfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False, bAllowTrope = False)
			Relations = title.misc.RelateFemale()
			Prefix = WordList(["Secretly In Love With"])
			sTweet = Prefix.GetWord() + "\nMy " + Girl.Desc + " " + Relations.GetWord(NotList = ["Girlfriend", "Mistress", "Wife"])
		return sTweet
		
# class Generator47(Generator):
	# # My Step-Dad Transforms Into A Cocky Gentleman Mer-Man!
	# ID = 47
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Relate = title.misc.RelateMale()
		# Species = title.misc.SpeciesMale()
		# VerbTrans = WordList(["Transforms", "Transforms", "Changes", "Shifts", "Morphs", "Metamorphs"])
		
		# Master = MaleChar(bAddEndNoun = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowRelate = False, bAllowSpecies = False, bAllowTitle = False)
		
		# sTweet = "My " + Relate.GetWord() + " " + VerbTrans.GetWord() + "\ninto a\n" + Master.Desc + " " + Species.GetWord() + "!"

		# return sTweet
		
class Generator48(Generator):
	# Lusting For the Wicked Blonde Fetish Model
	ID = 48
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		HairTropes = WordList(["Fiery Redhead", "Wholesome Blonde", "Clueless Blonde", "Nerdy Asian", 
			"Asian Schoolgirl", "Spicy Latina", "Haughty Redhead", "Hot-Blooded Italian", "Submissive Asian",
			"Brainy Brunette", "Sassy Black", "Bootylicious Black", "Wicked Blonde", "Shy Brunette",
			"Muscular Blonde", "Snooty French", "Hot-Blooded Gypsy", "Sensual Russian", "Mysterious Geisha",
			"Athletic Brunette"])
		Girl = FemaleChar(iNumMaxCBits = 2, bAllowAge = False, bAllowAttitude = False, bAllowMaritalStatus = False, bAllowPhysChar = False, bAllowRelate = False, bAllowNation = False, bAllowSkinHairColor = False, bAllowSpecies = False)
		
		sTweet = self.Gerunds.GetWord() + " the " + HairTropes.GetWord() + " " + Girl.Desc 

		return sTweet		
		
class Generator49(Generator):
	ID = 49
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		PublicPlaces = WordList(["at the Bowling Alley", 
			"in the Produce Section", 
			"in the Baked Goods Section",
			"in the Bakery",
			"at the Wine Tasting",
			"on the Coffee Table", 
			"in the Restroom at Chiopotle", 
			"Behind the Chic-fil-a", 
			"in the Ball Pit", 
			"in the Whole Foods Parking Lot",
			"in the Men's Restroom",
			"in the Women's Restroom",
			"in the Park",
			"at the Beach",
			"on the Eliptical Machine at the Gym",
			"at the Seafood Restaurant",
			"at the Museum",
			"at the Library",
			"at the Farmer's Market",
			"next to the Duck Pond",
			"in the Window of a Shoe Store",
			"in the Hunting Section at a Wal-Mart",
			"in the Church Graveyard",
			"in the Old Castle Ruins",
			"at the Old Manor House",
			"in the Abandoned Mansion",
			"at the Construction Site",
			"next to the Assembly Line",
			"on a Hotel Balcony"
			])
		
		Verbs = WordList(["Claimed", "Claimed",
			"Mounted",
			"Pleasured",
			"Ravished",
			"Taken","Taken","Taken"])
			
		Adverbs = WordList(["Hard","Hard","Hard",
			"Forcefully",
			"Passionately",
			"Roughly",
			"Ruthlessly",
			"Vigorously"])
			
		Master = MaleChar(bAddArticle = True)
		
		if CoinFlip():
			sTweet = Verbs.GetWord()
		else:
			sTweet = Verbs.GetWord() + " " + Adverbs.GetWord() 

		sTweet += "\n" + PublicPlaces.GetWord() + " by\n" + Master.Desc

		return sTweet
		
class Generator50(Generator):
	ID = 50
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Adjective = WordList(["Light ","Light ",
			"Friendly ",
			"Gentle ",
			"Mild ",
			"","","","","","",""])
		
		NaughtinessStraight = WordList(["Anal", 
			"Anal Sex",
			"Ass-Eating",
			"BDSM",
			"Blowjob",
			"Bondage",
			"Bukkake",
			"Butt Sex",
			"Butt Stuff",
			"Creampie",
			"Cunnilingus",
			"Deep Throat",
			"Dry-Humping",
			"Dogging",
			"Edging",
			"Fellatio",
			"Fingering",
			"Footjob",
			"Foreplay",
			"Fucking",
			"Hand-Job",
			"Jerking Off",
			"Masturbation",
			"Mutual Masturbation",
			"Nipple Play",
			"Pegging",
			"Rape Play",
			"Rimming",
			"Sex",
			"Spanking",
			"Spooning Naked",
			"Striptease",
			"Tantric Sex",
			"Tea-bagging",
			"Titty Fuck",
			"69ing",
			"Water Sports",
			"Wife-Swapping"])
			
		NaughtinessGay = WordList(["Anal", 
			"Anal Sex",
			"Ass-Eating",
			"Butt Sex",
			"Butt Stuff",
			"Deep Throat",
			"Edging",
			"Fellatio","Fellatio",
			"Gay Sex", "Gay Sex", "Gay Sex",
			"Hand-Job",
			"Jerking Off",
			"Masturbation",
			"Mutual Masturbation",
			"Nipple Play",
			"Rimming",
			"Spanking",
			"Spooning Naked",
			"Striptease",
			"Tea-bagging",
			"69ing",
			"Water Sports"])
			
		NaughtinessLez = WordList(["Ass-Eating",
			"BDSM",
			"Bondage",
			"Butt Stuff",
			"Cunnilingus",
			"Dry-Humping",
			"Finger Bang",
			"Fingering",
			"Fisting",
			"Masturbation",
			"Muff Diving",
			"Mutual Masturbation",
			"Tit Play",
			"Pegging",
			"Rimming",
			"Rug Munching",
			"Spanking",
			"69ing",
			"Water Sports"])
			
		FriendsGen = WordList(["Brother and Sister",
			"Colleagues",
			"Cousins","Cousins",
			"Co-workers","Co-workers",
			"Good Friends",
			"Friends",
			"Platonic Friends",
			"Roommates",
			"Siblings",
			"Step-Siblings",
			"Study Buddies",
			"Teacher and Student",
			"Teammates"])
			
		FriendsGay = WordList(["Boys",
			"Bros",
			"Brothers",
			"Buddies",
			"Cellmates",
			"Cowboys",
			"Dads",
			"Dudes",
			"Good Friends",
			"Fraternity Brothers",
			"Friends",
			"Lumberjacks",
			"Married Men",
			"Monks",
			"Priests",
			"Roommates",
			"Sailors",
			"Step-Brothers",
			"Straight Friends",
			"Twin Brothers"])
		
		FriendsLez = WordList(["Cellmates",
			"Cheerleaders",
			"Cousins","Cousins",
			"Coworkers",
			"Girls",
			"Girlfriends",
			"Married Women",
			"Moms",
			"Nuns",
			"Nurses",
			"Sisters",
			"Sorority Sisters",
			"Step-Sisters",
			"Twin Sisters"])
		
		sTweet = "What's a Little " + Adjective.GetWord()
		
		iRand = randint(1,3)
		if iRand == 1:
			#straight
			sTweet += NaughtinessStraight.GetWord() + " Between " + FriendsGen.GetWord()
		elif iRand == 2:
			#gay
			sTweet += NaughtinessGay.GetWord() + " Between " + FriendsGay.GetWord()
		else:
			#lesbian
			sTweet += NaughtinessLez.GetWord() + " Between " + FriendsLez.GetWord()
				
		sTweet += "?"
		return sTweet

class Generator51(Generator):
	ID = 51
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sName = self.HerName 
		Girl = None
		
		Places = WordList(["Land", "Kingdom", "Planet", "World", "Lost Land", "Lost World", "Forgotten Kingdom", "Island", 
						   "Lost Island", "Zone", "Forbidden Zone"])
		Beings = WordList(["Penisaurs", "Dong-o-saurs", "Fuck Men", "Ass-Eaters", "Ass Apes", "Cock-o-saurus Rex", 
						   "Tri-cock Men", "Sex Robots", "Dildo-Bots", "Uniporns", "Girthy Griffons", "Boner Beasts", 
						   "Homo Erectus", "Horny Mermen", "Barewolves", "Lepra-dongs", "Semen Centaurs", "Cum Imps", 
						   "Dick Dwarves", "Anal Elves", "Anal Aliens", "Naked Barbarians", "Naked Cowboys", 
						   "Massive Martians", "Cum Commandos", "Knob Goblins", 
						   "Turgid Trolls", "Bukkake Basilisks", "Bukkake Bugbears", "Blowjob Bugbears",
						   "Double-Dick Demons","Tea-Bagging Tyrannosaurs","Tea-Bagging Trolls","Frottage Fairies",
						   "Muff-Diving Mermaids","Muff-Diving Medusas","Dry-Humping Druids","Anal Angels",
						   "Ass-Eating Angels","Ass-Eating Aliens","Sex Serpents","Penis Pythons"])
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
			
		sTweet = sName + " the " + Girl.Desc + " in:\n"	
		sTweet += "The " + Places.GetWord() + " of the " + Beings.GetWord()

		return sTweet
		
# My Hot Redhead Teacher
# Is Secretly
# A Stripper!
class Generator52(Generator):
	ID = 52
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])

		SexyAdjs = WordList(["Hot","Sexy","Cute","Busty","Stacked","Thicc","Tanned","Bikini-Bod",
							 "Chesty","Young","Nubile"
							])
		sSexyAdj = SexyAdjs.GetWord()
		GoodJobs = WordList(["Teacher","English Teacher","Yoga Instructor","Librarian","Nanny","Math Tutor","Babysitter",
							 "Nurse","Piano Teacher","Dance Teacher","Algebra Teacher","Biology Teacher","Personal Trainer",
							 "House Maid","French Maid","Secretary","Intern","Assistant","Physical Therapist","Therapist",
							 "Violin Teacher","Dance Instructor","Gym Coach","Volleyball Coach"
							 ])
		sJob = GoodJobs.GetWord()
		
		GirlNotList = [sSexyAdj,sJob,'Slave Girl','Concubine']
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, Type = GirlType.Good, NotList = GirlNotList, bAddArticle = False, bAddEndNoun = False,
							bAllowTitle = False, bAllowSexuality = False, bAllowClothing = False, bAllowGenMod = False, bAllowPregState = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowAge = False)

		BadGirlNotList = ['Nun','Nurse','Gymnast','Masseuse','Cheerleader','Starlet','Secretary','Housewife','Fashion Model','French Maid']
		if CoinFlip():
			sTweet += Exclamations.GetWord() + " "
		if CoinFlip():	
			sTweet+= "My " + sSexyAdj + " " + Girl.Desc + " " + GoodJobs.GetWord() + " Is Secretly\n" + AddArticles(title.misc.ProfBadFemale().GetWord(NotList = BadGirlNotList)) + "!"
		else:
			sTweet+= "My " + sSexyAdj + " " + Girl.Desc + " " + GoodJobs.GetWord() + " Is Secretly\n" + AddArticles(title.misc.SpeciesFemale().GetWord() + " " + title.misc.ProfBadFemale().GetWord(NotList = BadGirlNotList)) + "!"
		
		return sTweet	
		
# Daddy Found Out
# His Sweet Little Step-Daughter 
# Is a Sassy Asian Stripper 
# And Now He's Pissed!
class Generator53(Generator):
	ID = 53
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NiceAdjs1 = WordList(["Bashful","Chaste","Conservative","Demure","Innocent",
							 "Modest","Sheltered","Shy","Tender","Wholesome","Introverted","Bubbly",
							 "Sweet","Sweet","Sweet","Little","Little"])
		NiceAdjs2 = WordList(["Christian","Christian","Mormon","Virgin","All-American",
							 "Athletic","Blonde","British","Brunette","Cheerleader","Dark-Skinned","Curvy",
							 "Ebony","French","Gymnast","Redheaded","Mormon","Curly-Haired"])
		sNiceAdj1 = NiceAdjs1.GetWord()
		sNiceAdj2 = NiceAdjs2.GetWord()
		
		RelateGirls = WordList(["Step-Daughter","Daughter"])
		
		BadGirlNotList = ['Nun','Nurse','Gymnast','Masseuse','Cheerleader','Starlet','Secretary','Housewife','Fashion Model','French Maid']
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, bAddArticle = False, Type = GirlType.Bad, NotList = BadGirlNotList, 
							bAllowAge = False, bAllowClothing = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowTrope = False, bAllowPhysChar = False, bAllowRelate = False)
		
		sTweet = "Daddy Found Out\nThat His " + sNiceAdj1 + " " + sNiceAdj2 + " " + RelateGirls.GetWord() + "\n"
		sTweet += "Is " + AddArticles(Girl.Desc) + "\nAnd Now He's Pissed!"

		return sTweet	
		
# 8" of Steel:
# The Feisty Princess (Nubile Queen / Virginal Priestess)
# Encounters 
# The Strapping Naked Half-Orc Barbarian 
class Generator54(Generator):
	ID = 54
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Weapons = WordList(['Steel','Molten Steel','Iron','Molten Iron','Hot Steel','Burning Steel','Hot Iron','Smoldering Steel'])
		LadyAdjs1 = WordList(['Feisty','Nubile','Virginal','Saucy','Wanton','Chaste','Demure','Virginal',
							  'Winsome','Brazen','Sassy','Willing','Lonesome','Sheltered','Blossoming'])
		LadyAdjs2 = WordList(['Buxom','Ample-Bosomed','Apple-Bottomed','Bosomy','Jiggling','Little','Naked','Narrow-Waisted',
							  'Nude','Petite','Plump','Ripe','Rubenesque','Shapely','Slender','Willowy','Statuesque',
							  'Tender','Voluptuous','Young','Undressed','Elf','Elven'])
		Ladies = WordList(['Princess','Queen','Maiden','Priestess','Maid','Nun','Damsel','Handmaiden','Elf Maiden'])
		MaleAdjs1 = WordList(['Beefy','Brawny','Bearded','Broad-Chested','Enormous','Hairy','Handsome','Huge','Muscle-Bound',
							  'Muscular','Strapping','Hunky'])
		MaleAdjs2 = WordList(['Powerful','Shirtless','Naked','Nude','Brazen','Rakish','Roguish','Cocky','Cocksure',
							  'Gruff','Dominant','Horny','Lustful','Randy','Savage','Wanton'])
		DickAdjs = WordList(['Donkey-Dicked','Engorged','Erect','Fully Erect','Girthy','Hard','Horse-Cock',
							  'Hugely Erect','Hung','Hung','Massively Erect','Rock-Hard','Throbbing',
						      'Visibly Aroused','Visibly Erect','Well-Hung','Well-Hung','Well-Endowed',
							  'Well-Endowed','Virile'])
		MaleSpecies = WordList(['Dark Elf','Demon','Dwarf','Centaur','Gargoyle','Giant','Goat Man','Goblin',
								'Half-Orc','Lizard Man','Orc','Vampire','Werewolf','Dragon Man','Half Dragon',
								'Minotaur'])
		MaleClass = WordList(['Barbarian','Warrior','Knight','Ranger','Bandit','Highwayman','Prince','Duke','Mercenary',
								'Paladin','Monk','Rogue','Thief','Warlock','Sorcerer','Hunter','Swordsman','Soldier',
								'Troubador','Woodsman','Blacksmith'])
								
		iLength = randint(8,12)
		sTweet = str(iLength) + " Inches of " + Weapons.GetWord() + ":\n"
		sTweet += "The " + LadyAdjs1.GetWord() + " " + LadyAdjs2.GetWord() + " " + Ladies.GetWord() + "\n"
		sTweet += "Encounters\n"
		
		sMonster = ""
		if CoinFlip():
			sMonster += MaleAdjs1.GetWord() + " "
		if CoinFlip():
			sMonster += MaleAdjs2.GetWord() + " "
		if CoinFlip():
			sMonster += DickAdjs.GetWord() + " "
			
		#print("Monster string is [" + sMonster.strip() + "]")
		if sMonster.strip():
			sMonster = AddArticles(sMonster)
		else:
			sMonster = "The " + sMonster
			
		iRand = randint(1,5)
		if iRand == 1 or iRand == 2:
			sMonster += MaleSpecies.GetWord()
		elif iRand == 3 or iRand == 4:
			sMonster += MaleClass.GetWord()
		else:
			sMonster += MaleSpecies.GetWord() + " " + MaleClass.GetWord()
			
		sTweet += sMonster

		return sTweet	
		
# The Sarah Sandwich:
# Fireman on Top,
# Fireman on the Bottom,
# Kinky Airline Stewardess in the Middle
class Generator55(Generator):
	ID = 55
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemmeNames = WordList(['Amy','Alicia','Alice','Alexis','Amanda','Amber','Angelica','Anita','Anna','Ava','Bella','Belle','Bianca',
							   'Daphne','Delilah','Delores','Donna','Doris','Eliza','Elizabeth','Emma','Ericka','Esmerelda',
							   'Estelle','Felicia','Felicity','Fiona','Francesca','Georgina','Gisele','Inya','Isabelle',
							   'Jacinda','Jackie','Jasmine','Josephine','Julie','Juliette','Karen','Katrina','Laurel','Lola',
							   'Marianna','Marilyn','Marsha','Melina','Molly','Natasha','Olivia','Phillippa',
							   'Phoebe','Piper','Regina','Rosie','Ruby','Ruth','Sabrina','Sharon','Sylvia','Vanessa','Veronica'
							   ])
		sJob1 = title.misc.ProfMale().GetWord()
		sJob2 = title.misc.ProfMale().GetWord()
		
		GirlNotList = ['Queen','Princess','Single','Concubine','Slave']
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, NotList = GirlNotList, 
							bAllowAttitude = False, bAllowAge = False, bAllowClothing = False, bAllowGenMod = False, bAllowRelate = False)
		sHerName = FemmeNames.GetWord()
		
		sTweet = "The " + sHerName + " Sandwich:\n"
		sTweet += sJob1 + " on Top,\n"
		sTweet += sJob2 + " on the Bottom,\n"
		sTweet += Girl.Desc + " in the Middle"

		return sTweet	
		
# The Kinky Brazillian Bikini Model
# is hot for
# Bald Men!
class Generator56(Generator):
	ID = 56
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FirstAdjs = WordList(['Sultry','Sexy','Stunning','Hot','Bubbly','Perky','Gorgeous','Foxy','Sensual',
							  'Passionate','Seductive','Slinky','Spicy','Luscious','Stunning','Nympho'])
		RaceHairColor = WordList(['Korean','Japanese','Brazilian','Argentinian','Swedish','Eastern European','Latvian',
								  'Coffee-Skinned','Black','Blue-Eyed','Green-Eyed','Redheaded','Platinum Blonde',
								  'South African','Icelandic','Irish','Pale','Porcelain-Skinned','Chinese',
								  'Italian','French','Latina','Columbian'])
		PhysAdjs = WordList(['Tall','Stacked','Leggy','Willowy','Slender','Bronzed','Voluptuous','Statuesque','Skinny',
							 'Jiggling','Tanned','Bubble-Butt','Tight-Bodied','Full-Figured','Curvaceous','Juicy'])
		ExoticGirlJobs = WordList(['Bikini Model','Supermodel','Fashion Model','Flight Attendant','Lingerie Model',
									'Masseuse','Playboy Centerfold','Penthouse Pet','Erotic Model','Beach Bunny',
									'Beauty Queen','Actress','Starlet','Movie Star'])
		PreFetishes = WordList(['Middle-Aged','Dad Bod','Overweight','Stay-at-Home','Chubby','Nerdy','Geeky','Awkward',
							 'Anti-Social','Unemployed','Flabby','Paunchy','Short'])
		PostFetishes = WordList(['Bald Spots','Micro Penises','Micro Penises','Beer Bellies','Dad Bods','Bacne','Social Anxiety',
								 'Drinking Problems','Sleep Apnea'])
		PhysAttr = WordList(['Black','Bearded','Bald','Balding','Curly-Haired','Jewish','Canadian',
							 'Red-Headed','Ginger','Brown-Haired','Graying','British','Asian','Indian','Polish','Danish',
							 'Pale','Suburban'])
		Men = WordList(['Men','Dads','Middle Managers','Construction Workers','Doctors','College Students','Virgins',
						'Cops','Male Nurses','Fire Fighters','Ball Boys','Web Designers','Gym Coaches',
						'Professors','Engineers','Software Engineers','Lawyers','Preachers','Ministers',
						'Youth Ministers','Car Salesmen','English Teachers','Math Teachers','IT Technicians',
						'Guitar Teachers','Realtors','Waiters','Ex-Cons','Hipsters','Single Dads',
						'Walmart Greeters','Security Guards','Uber Drivers','Old Guys','Guys','Dudes','Janitors',
						'Consultants','Tax Preparers','Accountants','Insurance Adjustors','Roofing Contractors',
						'Golf Caddies','Plumbers','Truckers','Drywall Installers','Parole Officers',
						'Corrections Officers','Dungeon Masters'])
									
		sExoticGirl = ""
		if CoinFlip():
			sExoticGirl += FirstAdjs.GetWord() + " "
		if CoinFlip():
			sExoticGirl += RaceHairColor.GetWord() + " "
		if CoinFlip():
			sExoticGirl += PhysAdjs.GetWord() + " "
		sExoticGirl += ExoticGirlJobs.GetWord()
		
		if CoinFlip():
			sMan = PreFetishes.GetWord() + " " + PhysAttr.GetWord() + " " + Men.GetWord()
		else:
			sMan = PhysAttr.GetWord() + " " + Men.GetWord() + " with " + PostFetishes.GetWord()
		
		sTweet = "This " + sExoticGirl + "\n" + WordList(['is hot for','has a thing for']).GetWord() + "\n" + sMan + "!"

		return sTweet	
		
# Taken in the Locker Room 
# by an Entire Team of 
# Muscular Lumberjack Hockey Players
class Generator57(Generator):
	ID = 57
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(['Taken','Gang-Banged','Shared','Claimed','Taken Hard','Claimed Hard','Tied Up & Used','Deflowered',
						  'Fisted','Motor-Boated','Impregnated','Fertilized','Mounted Bareback','Ridden Hard','Pleasured',
						  'Ravished','Satisfied','Oiled Up','Paddled'])
		Teams = WordList(['Hockey Players','Football Players','Basketball Players','Sumo Wrestlers','Rugby Players',
						  'Baseball Players','Olympic Swimmers','Wrestlers','Soccer Players'])
		sTeam = Teams.GetWord()
		MenNotList = [sTeam, 'Single']
		Men = MaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAddArticle = False, bAllowGang = False, NotList = MenNotList,
						bAllowAge = False, bAllowAttitude = False, bAllowGenMod = False, bAllowRelate = False, bAllowTitle = False)
	
		sTweet += Verbs.GetWord() + " in the Locker Room\nby an Entire Team of\n" + Men.Desc + " " + Teams.GetWord()

		return sTweet	
		
# I hooked up with a strapping leather cowboy
# and now I'm pregnant!
class Generator58(Generator):
	ID = 58
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ["Widowed"]
		HookUpPhrases = WordList(["Hooked Up With", "Had a One Night Stand With", "Slept With", "Banged", "Had a Quickie With", "Fooled Around With"])
		MaleRelatives = WordList(["Step-Dad", "Step-Brother", "Brother", "Brother-in-Law", "Father", "Dad", "Daddy", "Step-Father"])
		Man = MaleChar(iNumMaxCBits = 4, NotList = ManNotList, bAddArticle = False, bAllowRelate = True, bAllowSpecies = True, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False)
		sMan = Man.Desc 
		
		if FoundIn(sMan, MaleRelatives.List):
			sTweet = "I " + HookUpPhrases.GetWord() +" My " + sMan + "\nAnd Now I'm Pregnant!"
		else:
			sTweet = "I " + HookUpPhrases.GetWord() +" " + AddArticles(sMan) + "\nAnd Now I'm Pregnant!"
		return sTweet
	
# # The hot bikini model prom queen
# # is secretly a lesbian 	
# class Generator59(Generator):
	# ID = 59
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# sHotAdjs = WordList(["Dirty", "Hot", "Sexy", "Busty", "Jiggly", "Stacked", "Athletic", "Slender", "Apple-Bottomed", "Curvaceous", "Flexible"])
		# sGirlAdjs = WordList(["Blonde", "Redhead", "Asian", "Chocolate", "Giggly", "Flirty", "Curly-Haired", "Tattooed"])
		# GirlNouns = WordList(["Schoolgirl", "Bimbo", "Cheerleader", "Bikini Model", "Prom Queen", "Teen", "Coed", "Gymnast",
								# "Baby-Sitter", "Fashion Model", "Beach Bunny", "Surfer Girl", "Goth Girl"])
		# sNoun1 = GirlNouns.GetWord()
		# sNoun2 = GirlNouns.GetWord(NotList = [sNoun1])

		# sTweet = "The " + sHotAdjs.GetWord() + " " + sGirlAdjs.GetWord() + " "
		# sTweet += sNoun1 + " " + sNoun2 + "\n"
		# sTweet += "Is Secretly a Lesbian!" 
		# return sTweet		
		
# Sweet Little Amy
# The Swedish Schoolgirl 
# and her 
# Adventure with the
# Magic Butt Plug
class Generator60(Generator):
	ID = 60
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		SweetAdjs = WordList(['Sweet', 'Sweet', 'Cute', 'Blonde','Innocent','Bashful','Naive'])
		NiceNames = WordList(['Amy','Angelica','Annie','Charity','Daisy','Daphne','Elsie',
							  'Emmy','Frances','Gertrude','Greta','Jeanie','Lacey','Lizzy',
							  'Mabel','Mary','Maryanne','Molly','Nancy','Nell','Olive','Phoebe',
							  'Rosie','Shelly','Sophie','Summer','Virginia'])
		NiceGirlAdjs = WordList(['All-American','Amish','Apple-Bottomed','Athletic','Asian','Blue-Eyed',
								 'Busty','Buxom','Country','Curvy','Freshman','Korean','Leggy','Modest','Nubile',
								 'Pale','Repressed','Small-Town','Swedish','Teen Beauty Queen','Virgin'])
		NiceGirlNouns = WordList(['Babysitter','Cheerleader','Coed','Daddy\'s Girl','Farmer\'s Daughter',
								  'Freshman','Geek Girl', 'Gymnast','Maiden','Nerd Girl','Schoolgirl','Southern Belle',
								  'Step-Daughter','Teen Model','Virgin'])
		ObjectAdjs = WordList(['Demon-Possessed','Enchanted','Haunted','Magic','Magical'])
		ObjectNouns = WordList(['Anal Beads','Anal Hook','Ball Gag','Ben Wa balls','Bull Dyke','Butt Plug',
								'Clit Clamp','Clit Pump','Crotchless Panties','Dildo','11\" Dildo',
								'Double-Ended Dildo','Gimp Mask','Hitachi Magic Wand','Leather Riding Crop',
								'Nipple Clamps','Orgasmatron','Pearl Necklace','Rabbit Vibe','Rubber Fetish Suit','Sex Doll',
								'Sex Swing','Spreader Bar','Speculum','Strap-On','Sybian','Thong','Vibrator'])
		sNice1 = ""
		sNice2 = ""
		
		sTweet += NiceNames.GetWord() + " the " 
		if CoinFlip():
			sTweet += SweetAdjs.GetWord() + " "
		sTweet += "Little "
		if CoinFlip():
			sNice1 = NiceGirlAdjs.GetWord()
			sTweet += sNice1 + " "
		sNice2 = NiceGirlAdjs.GetWord(NotList = [sNice1])
		sTweet += sNice2 + " " + NiceGirlNouns.GetWord(NotList = [sNice1, sNice2]) + "\nand her\nAdventure with\n"
		sTweet += "The " + ObjectAdjs.GetWord() + " " + ObjectNouns.GetWord()
		
		return sTweet	
		
# Transformation:
# From Sweet Innocent All-American Schoolgirl
# to
# Leather-Clad Bondage Slut 
class Generator61(Generator):
	ID = 61
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirlNotList = ["Tanned","Concubine","Recently-Divorced","Big Titty","Busty","Hot",
							"Juicy","Leggy","Naked","Nude","Shaved","Voluptuous","Young",
							"Pregnant","Jiggling","Wet Nurse","Sassy","Geisha","Baroness",
							"Duchess","Slave Girl","Slave","MILF","HuCow","Kitten"]
		BadGirlNotList = ["Virgin","Married","Nursing"]
		GoodGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Good, bAddArticle = False, NotList = GoodGirlNotList, bAllowRelate = False, bAllowPregState = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = False, bAllowGenMod = False, bAllowClothing = False)
		BadGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = False, NotList = BadGirlNotList, bAllowRelate = False, bAllowSexuality = True, bAllowMaritalStatus = False, bAllowSpecies = True, bAllowNation = False, bAllowTitle = False)
		
		sTweet = "Transformed:\nfrom\n" + GoodGirl.Desc + "\nto\n" + BadGirl.Desc

		return sTweet	
		
# Help!
# A husky investment banker
# has me chained up in his basement (garage/sex dungeon)
# naked!
class Generator62(Generator):
	ID = 62
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Exclamations = WordList(["Help!", "Help!", "Oh No!", "Uh Oh!", "What Do I Do?!?"])
		BadPlaces = WordList(["Basement", "Basement", "Dungeon", "Garage", "Attic", "Man Cave", "Den", "Sex Dungeon", "Cellar", "Secret Lair", "Secret Hideout", "Secret Love-Nest", "Swanky Bachelor Pad"])
		BadMan = MaleChar(iNumMaxCBits = 4, bAddArticle = False, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False)
		
		sTweet = "\"" + Exclamations.GetWord() + "\n" + AddArticles(BadMan.Desc) + "\nHas Me Chained Up In His " + BadPlaces.GetWord() + ",\nNaked!\""

		return sTweet	
		
# The Busty Blonde Flight Attendant's 
# Topless Miami Vacation
class Generator63(Generator):
	ID = 63
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = None
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False)
		else:
			Girl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = True, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = True, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False)
		VacType = WordList(["Topless", "Nudist", "Fully Nude", "Naked", "Fully Nude", "Naked"])
		VacPlace = WordList(["Miami", "Carribean", "Spanish", "Italian", "Greek", "Cancún", "Hawaiian", "Los Angeles", "Bangkok", 
							 "Las Vegas", "Macau", "Ibiza", "Jamaica", "New Orleans", "Rio", "Berlin", "Bali", "Goa", "Australian",
							 "Amsterdam", "Lagos", "Bora Bora", "Thai", "Fiji"])
		VacWord = WordList(["Vacation", "Vacation", "Getaway", "Holiday", "Spring Break"])
							 
		sTweet = Girl.Desc + "'s\n" + VacType.GetWord() + " " + VacPlace.GetWord() + " " + VacWord.GetWord()
			
		return sTweet	
		
# 'Oh $@*#!'
# My new stepmom is a 
# Tanned Swedish Masseuse
# and 
# Her Ass Looks Amazing! 
class Generator64(Generator):
	ID = 64
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Exclamations = WordList(["Oh S@*#!", "Uh Oh!", "WTF?!?", "Oh F*@%!"])
		Relatives = WordList(["Stepmom", "Stepmom", "Step-Sister", "Sister-in-Law", "Step-Daughter"])
		Ender = WordList(["Her Ass Looks Amazing", "She's At Least A Double-D", "She Likes To Sunbathe Nude", 
						  "She Doesn't Wear Panties", "She Likes To Go Braless", "She Likes To Go Commando", 
						  "She's A Shameless Nudist", "She Showers With The Door Open", "Her Boobs Are Incredible",
						  "She Shaves Herself Down There", "She Has The Body Of A Porn Star", "She Has Enormous Coconuts",
						  "And I've Seen Her Tits","And She Is Stacked"])
		Girl = FemaleChar(iNumMaxCBits = 4, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False, bAllowPregState = False)

		sTweet = Exclamations.GetWord() + "\nMy New " + Relatives.GetWord() + " Is\n" + AddArticles(Girl.Desc) + "\nAnd " + Ender.GetWord()
		
		return sTweet	
		
# Anita Gets Serviced 
# By Five Naked Cowboys 
class Generator65(Generator):
	ID = 65
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(["Serviced","Pleasured","Taken","Satisfied","Shared","Ravished","Mounted","Treated Like A Lady"])
		Numbers = WordList(["Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
							"Thirteen"])
		Adjs = WordList(["Burly","Hairy","Mustachioed","Muscular","Bald","Beefy","Chiseled","Handsome",
						 "Tall","Hung","Hunky","Well-Endowed","Sexy","Rock Hard","Strapping","Strong",
						 "Gruff","Cocky","Powerful","Horny","Skillful","Tattooed"])
		Men = WordList(["Bikers","Cops","Cowboys","Firemen","Football Players","Gangsters","Knights",
						"Weight Lifters","Mountain Men","Pirates","Scottsmen","Sumo Wrestlers","Werewolves",
						"Viking Warriors","Bull Riders","Chippendales Dancers","Construction Workers",
						"Defensive Linemen","Gladiators","MMA Fighters","Sailors","Gentleman","Older Men"])
		
		sTweet = self.HerName + " Gets " + Verbs.GetWord() + " By\n"
		sTweet += Numbers.GetWord() + " " +Adjs.GetWord() + " Naked " + Men.GetWord()

		return sTweet	

# The Bride Wore a Ball Gag		
class Generator66(Generator):
	ID = 66
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		BrideWore = WordList(['Latex','Black Leather','Body Paint','a Spreader Bar','a Speculum','a Clit Pump','Nipple Clamps',
							  'a Ball Gag','a Leash','a Butt Plug','an Anal Plug','a Vibrator','Crotchless Panties',
							  'Assless Leather Chaps','an Anal Tail Plug','a Steel Collar','a Chain-mail Bikini',
							  'a Clit Clamp','a Gimp Mask','a Leather Body Harness','Chocolate Lingerie','a Cupless Bra',
							  'a Leather Catsuit','Crotchless Pantyhose','a Fishnet Bodystocking','a Chastity Belt',
							  '9-inch Heels','Thigh-High Boots','a Steel Bra','a Leather Bikini','a G-string',
							  'Pasties and a G-string','Handcuffs','a Sheer Black Bodysuit','Spiked Heels',
							  'a Strap-On', 'a Black Leather Tail','Nothing','Black Latex','Red Leather','Red Latex',
							  'a Black Body Harness','a Black Bodystocking','a Red Sheer Bodystocking',
							  'a Black Sheer Bodystocking','a Black Leather Bikini','Black Pasties','Red Pasties'])
							  
		sTweet = "The Bride Wore " + BrideWore.GetWord()

		return sTweet	
		
# # "Go easy on me! I'm a teenage coed nun
# # and its my first time
# # doing anal!"
# class Generator67(Generator):
	# ID = 67
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# Beginnings = WordList(["Please Go Easy On Me", "Please Be Gentle With Me", "Please Be Gentle", "Please Go Slow", 
							   # "Please Be Careful"])
		# FirstTimes = WordList(["Doing Anal", "With A Girl", "With Another Woman", "Doing Butt Stuff", 
							   # "Wearing a Butt Plug", "In a Gimp Mask", "Being Punished With a Riding Crop",
							   # "In a Sex Swing", "Deep Throating", "Being Choked", "Trying Erotic Asphyxiation", 
							   # "Wearing Nipple Clamps", "In a Sex Dungeon", "Doing It in Public", "Swallowing",
							   # "With One This Big", "Trying Bukkake", "Trying Double Penetration",
							   # "With Two Dudes", "With Three Guys At Once", "Trying a Gang Bang",
							   # "With an Older Man", "Doing Hardcore Bondage Play", "Wearing a Ball Gag",
							   # "Trying Water Sports"])
		# Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False, bAllowPregState = False)

		# sTweet = "\"" + Beginnings.GetWord() + "!\nI'm " + AddArticles(Girl.Desc) + "\nAnd Its My First Time\n" + FirstTimes.GetWord() + "!\""

		# return sTweet	
		
# I know I'm married,
# but it can't hurt if I try rimming
# with this Italian Don Juan cowboy 
# just this once!
class Generator68(Generator):
	ID = 68
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		SexActs = WordList(["69 with","have Anal Sex with","try BDSM with","get a Dirty Sanchez from","try Double Penetration with",
							"try Erotic Asphyxiation with","try Leather Bondage with","try Face-Sitting with","get Fisted by",
							"get Rimmed by", "try Rimming","try Water Sports with","try Whips and Chains with",
							"try Spooning Naked with","try Age Play with","do Butt Stuff with","try Edging with",
							"get My Ass Eaten by","try Eating the Ass of","perform an Erotic Massage on",
							"do a Strip Tease for","give a Footjob to","try Nipple Play with","Go Down On",
							"give a Tit-Job to","get Cunnilingus from","get Eaten Out by","get Fingered by"])
		
		Man = MaleChar(iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, bAllowAge = False, bAllowRelate = False, bAllowSpecies = True, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowTrope = False)
		
		sTweet = "\"I Know " + WordList(["I'm Married","I'm Married","I'm Engaged","I Have a Boyfriend"]).GetWord() + ", But\n"
		sTweet += "It Can't Hurt If I " + SexActs.GetWord() + " " + AddArticles(Man.Desc + " " + title.misc.ProfMale().GetWord()) + "\n"
		sTweet += "Just This Once!\""

		return sTweet	
		
# The wholesome blonde Christian girl spreads her legs (bends over/drops her panties/puts out)
# for the cocky Italian DILF!
class Generator69(Generator):
	ID = 69
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Actions = WordList(["Spreads her Legs for","Spreads her Legs for","Bends Over for","Drops Her Panties for","Goes Down On","Lifts her Skirt for","Spreads her Thighs for","Spreads her Cheeks for","Opens Her Legs for","Lubes Herself Up for"])
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
		
		Man = MaleChar(iNumMaxCBits = 3, bAddArticle = False, bAllowRelate = False, bAllowMaritalStatus = True, bAllowGang = False, bAllowTitle = True)
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet = "The " + Girl.Desc + "\n" + Actions.GetWord() + "\nThe " + Man.Desc 
		elif iRand == 2:
			sTweet = NamesFemale().FirstName() + " the " + Girl.Desc + "\n" + Actions.GetWord() + "\nThe " + Man.Desc 
		else:
			sTweet = "My " + Girl.Desc + "\n" + Actions.GetWord() + "\n" + AddArticles(Man.Desc)
			
		return sTweet	
		
# I shot a porn scene
# with a handsome BBC construction worker
class Generator70(Generator):
	ID = 70
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Beginnings = WordList(["I Shot a Porn Scene", "I Made a Porn Video", "I Made a Porno", "I Shot a Porn Video", "I Did Porn"])
		Endings = WordList(["And His Friends", "And I Liked It", "While My Husband Watched", "And I Didn't Get Paid", 
							"And I Was Paid $60", "And Now I'm Pregnant", "While My Boyfriend Watched", "While My Girlfriend Watched",
							"And My " + WordList(["Dad","Brother","Step-Dad","Step-Brother"]).GetWord() + " Saw It",
							"And His " + str(randint(2,13)) + " Friends", "And I Didn't Tell My Boyfriend", "And I Didn't Tell My Dad",
							"And My Dad Found Out"])
							
		Man = MaleChar(iNumMaxCBits = 3, bAddArticle = False, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = True, bAllowGang = False, bAllowTitle = False)

		sTweet = "\"" + Beginnings.GetWord() + "\nwith\n" + AddArticles(Man.Desc)
		if CoinFlip():
			sTweet+= "\n" + Endings.GetWord()
		sTweet += "\""
		
		return sTweet	
		
class Generator71(Generator):
	ID = 71
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Beginnings = WordList(["I Shot a Lesbian Porn Scene", "I Made a Lesbian Porn Video", "I Made Lesbian Porn", "I Shot a Lesbian Porn Video", "I Did Lesbian Porn"])
		Endings = WordList(["And Her Friends", "And I Liked It", "While My Husband Watched", "And I Didn't Get Paid", 
							"And I Was Paid $50", "While My Boyfriend Watched", "While My Girlfriend Watched",
							"And My " + WordList(["Dad","Brother","Step-Dad","Step-Brother"]).GetWord() + " Saw It",
							"And Her " + str(randint(2,13)) + " Friends", "And I Didn't Tell My Boyfriend", "And I Didn't Tell My Mom",
							"And My Mom Found Out", "While My Wife Watched", "And I Didn't Tell My Girlfriend"])
							
		Girl = FemaleChar(iNumMaxCBits = 3, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowMaritalStatus = True, bAllowTitle = False)

		sTweet = "\"" + Beginnings.GetWord() + "\nwith\n" + AddArticles(Girl.Desc)
		if CoinFlip():
			sTweet+= "\n" + Endings.GetWord()
		sTweet += "\""

		return sTweet	
		
# My New Coworker
# is a Strapping Long Haul Truckers
# and He Sucked My Titties 
class Generator72(Generator):
	ID = 72
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ["Single"]
		Man = MaleChar(iNumMaxCBits = 3, NotList = ManNotList, bAddArticle = False, bAllowGang = False,
						bAllowRelate = False, bAllowSpecies = True, bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = True, bAllowTrope = False)
		Relations = WordList(["Co-worker","Boss","Boss","Step-Brother","Brother-in-Law","Son-in-Law","Step-Son",
								"Tutoring Student","Gym Coach","Personal Trainer","Massage Therapist",
								"Nextdoor Neighbor","Math Teacher","Math Tutor","English Teacher",
								"Literature Professor","Tennis Coach","Pool Boy"
								])
		NaughtyStuff = WordList(["He Ate Me Out","He Ate My Ass","He Sucked My Titties","I Let Him Finger Me",
								"We Sixty-nined","I Let Him Fist Me","I Let Him Shave My Cooch","I Gave Him Head",
								 "I Gave Him a Hand-Job","I Gave Him a Foot-Job","I Let Him Play With My Titties",
								 "He Whipped My Bare Ass With a Riding Crop","I Sat On His Face",
								 "He Spanked My Ass","I Gave Him Road Head","I've Seen Him Naked",
								 "We Showered Together","I Jerked Him Off","I Dry-Humped Him",
								 "I Gave Him a Rim-Job","He Wears a Cock Ring","He Has a Cock Piercing",
								 "He Likes to be Pegged","We Did Butt Stuff","I Went Down On Him",
								 "He Went Down On Me"])

		sTweet = "\"My New " + Relations.GetWord() + " is\n"
		sTweet += AddArticles(Man.Desc) + "\n"
		sTweet += "and\n" + NaughtyStuff.GetWord() + "!\""
		
		return sTweet	

		return sTweet	
		
class Generator73(Generator):
	ID = 73
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
						  
		BadResult = WordList(["an Amateur Porn Star","an Anal Bimbo","a Naughty Bikini Model","a Foul-Mouthed Skank","a High-Class Call Girl","a $1000-an-hour Hooker","a Leather Bondage Submissive",
							  "a Hotwife","a Porn Star","a Sex Addict","a Sex Slave","a Slut","a Shameless Exhibitionist","a Stripper","a Topless Spring Break Party Girl"])									  
		sTweet = "I Turned My " + sNiceGirl + "\ninto " + BadResult.GetWord() + "!"

		return sTweet	
		
class Generator74(Generator):
	ID = 74
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
		
		NaughtyStuff = WordList(["69ing", "an Anal Hook","Anal Sex","BBC","BDSM","Bukkake","a Butt Plug","a Clit Clamp","a Dirty Sanchez","Double Penetration","Erotic Asphyxiation","a Gang Bang",
									 "an Interracial Threesome", "Leather Bondage","Lesbian Sex","Face-Sitting","Fisting","an Orgy","Nipple Clamps","Nudism","Rimming","Sex With Another Woman","Spanking",
									 "Stripping at a Club","Swinging","a Threesome","Watching Porn","Water Sports","Whips and Chains","Wife Swapping"])
		Reactions = WordList(["Now She Can't Get Enough","She Loves It","She Wants More","Now She Won't Stop","Now She Won't Quit","Now She's Insatiable",
							  "It Turned Her Into A Slut","It Turned Her Into A Sex-Crazed Bimbo","Now She's a Sex Addict","It Turned Her Into A Ho","It Turned Her Into a Lesbian",
							  "Now She's a Professional Porn Star", "She Decided to Become a Porn Star","Now All She Does Is Masturbate","It Was Awkward and Not Really Her Thing"])

		sTweet = "My " + sNiceGirl + "\nTried " + NaughtyStuff.GetWord() + "\nAnd " + Reactions.GetWord() + "!"
				
		return sTweet	

class Generator75(Generator):
	ID = 75
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
		
		if CoinFlip():
			sTweet += Exclamations.GetWord() + " "
		sTweet += "My " + sNiceGirl + " Went Black and She Won't Come Back!"

		return sTweet	
		
# My New Neighbor is a 
# Tanned Redheaded Secretary
# and 
# I Ate Her Out
class Generator76(Generator):
	ID = 76
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel","Maiden","Fetish","Call-Girl"]
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = WomanNotList, bAddArticle = False, bAllowClothing = True, bAllowRelate = False, bAllowSexuality = True, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = True, bAddEndNoun = True)
		Relations = WordList(["Dad's New Girlfriend","New Next Door Neighbor","New Co-worker","New Boss","New Step-Sister",
								"New Step-Daughter","Daughter's New Best Friend","New Student","New Secretary",
								"New Sister-in-Law","New Girlfriend's Sister","New Assistant","New Gym Coach",
								"New Math Tutor","New English Teacher","Dad's New Wife","New Step-Mom"])
		NaughtyStuff = WordList(["I Ate Her Out","I Ate Her Ass","I Sucked Her Titties","I Finger-Banged Her",
								 "I Gave Her a Pearl Necklace","I Gave Her a Rim Job","We Sixty-nined","I Fisted Her",
								 "She Asked Me to Shave Her Cooch","I Took Pictures of Her Doing Nude Yoga","She Sucked Me Off",
								 "She Gave Me a Hand-job","She Gave Me a Foot-Job","I Gave Her a Booty Massage... Naked",
								 "She Let Me Play With Her Titties","She Likes to Wear Nipple Clamps",
								 "I Whipped Her Bare Ass With a Riding Crop","She Sat On My Face",
								 "She Smothered Me With Her Ass","She Pegged Me With a Strap-On","I Knocked Her Up",
								 "I Spanked Her Bare Ass With a Steel Paddle","I Rimmed Her Butt-hole",
								 "I've Seen Her Naked","She Let Me Soap Her Up in the Shower","I Got her Pregnant",
								 "She Let Me Play With Her Hard Nips","She Let Me Play With Her Nipple Piercings"])
		sTweet = "\"My " + Relations.GetWord() + " is\n"
		sTweet += AddArticles(Girl.Desc) + "\n"
		sTweet += "and\n" + NaughtyStuff.GetWord() + "!\""
		
		return sTweet	
		
# "I was a fertile harem girl
# for a strapping black cowboy sheikh"
class Generator77(Generator):
	ID = 77
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		MateAdjs1 = WordList(["Fertile","Nubile","Breeding","Yielding","Pregnant","Kept","Blushing","Virginal",
							 "Willing","Lactating","Ripe","Submissive","Subservient","Wide-Eyed","Conjugal",
							 "Naive Young","Innocent","Bashful"])
		MateAdjs2 = WordList(["Buxom","Petite","Voluptuous","Small-Town","Dark-Eyed","Dark-Skinned","Blonde",
							  "Brunette","Redheaded","Chubby","BBW","Slender","Coed","Country Girl","Wide-Hipped",
							  "Full-Bodied","Nude","Shaved"])
		MateNouns = WordList(["Harem Girl","Bride","Mate","Concubine","Courtesan","Mistress","Princess","Wife"])
		ManAdjs = WordList(["Naked","Strapping","Nudist","Well-Hung","Virile","Muscular","Burly",
							 "Hunky","Bald","Well-Endowed","Beefcake","Girthy","Handsome","Mustachioed",
							 "Rock-Hard","Horny","Wicked","Kinky","Sensual","Naughty","Throbbing"])
		ManNouns = WordList(["Sheikh","Shah","Prince","Sultan","King","Vizir","Maharaja"])
		sManAdj = ManAdjs.GetWord()
		Man = MaleChar(iNumMaxCBits = 2, NotList = [sManAdj], bAddArticle = False, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowNation = False, bAddEndNoun = False)

		sMate = ""
		if CoinFlip():
			sMate = MateAdjs1.GetWord() + " " + MateAdjs2.GetWord() + " " + MateNouns.GetWord()
		else:
			sMate = MateAdjs1.GetWord() + " " + MateNouns.GetWord()
		
		iRand = randint(1,2)
		if iRand == 1:
			sTweet += "I Was " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc + " " + ManNouns.GetWord())
		elif iRand == 2:
			sTweet += "I Was " + WordList(["Sold","Gifted","Mated","Bound","Betrothed","Promised","Married","Bred"]).GetWord() + " as " + AddArticles(sMate) + "\nto\n" + AddArticles(sManAdj + " " + Man.Desc + " " + ManNouns.GetWord())
		# else:
			# sTweet += "I Was " + WordList(["Pledged","Trained"]).GetWord() + " as " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc)

		return sTweet	
	
# His for the Fisting:
# A Submissive Nubile Black Flight-Attendant Story	
class Generator78(Generator):
	ID = 78
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		Gerunds = WordList(["69ing","Ass-Eating","Bedding","Binding","Breaking","Breeding","Caning","Claiming","Deflowering",
						    "Defiling","Dominating","Edging","Exposing","Fingering","Fisting","Impregnating","Ogling","Milking","Motor-Boating",
							"Paddling","Peeing On","Penetrating","Pleasuring","Porking","Pumping","Rimming","Sharing","Shaving","Spanking","Spraying","Spread-Eagling",
							"Spit-Roasting","Stripping","Stuffing","Taking","Tasting","Tea-Bagging","Touching","Toying","Whipping",
							"Undressing","Using","Video-Taping"])
		SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
		sSubAdj = SubAdjs.GetWord()
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = [sSubAdj], bAddArticle = False, bAllowClothing = True, bAllowRelate = True, bAllowSexuality = True, bAllowSpecies = True, bAllowMaritalStatus = True, bAllowTitle = True)
		
		sTweet = "His for the " + Gerunds.GetWord() + ":\n"
		sTweet += AddArticles(sSubAdj + " " + Girl.Desc) + " Story"
		return sTweet	
		
class Generator79(Generator):
	ID = 79
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		VerbsTo = WordList(["69","Anally Deflower","Bone","Chain Up","Claim","Claim Hard","Command","Deflower",
							"Degrade","Dominate","Enslave","Gag","Hotwife","Humiliate","Hypnotize","Impregnate",
							"Knock-Up","Lick","Master","Mind Control","Motor-Boat","Mount Roughly","Paddle",
							"Pee On","Penetrate","Pervert","Possess","Publicly Expose","Punish","Ride Hard","Shave",
							"Splooge On","Suck On","Take From Behind","Tame","Tea-Bag","Wife-Swap","Undress",
							"Use Sexually","Video-Tape"])

		SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
		sSubAdj = SubAdjs.GetWord()
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = [sSubAdj], bAddArticle = False, bAllowClothing = True, bAllowRelate = True, bAllowSexuality = True, bAllowSpecies = True, bAllowMaritalStatus = True, bAllowTitle = True)
		
		sTweet = "His To " + VerbsTo.GetWord() + ":\n"
		sTweet += AddArticles(sSubAdj + " " + Girl.Desc) + " Story"

		return sTweet	
		
# # When the Princess
# # Met the Cowboy...
# # ...and they had wild interracial sex!
# class Generator80(Generator):
	# ID = 80
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# SexAdjs1 = WordList(["Wild","Illicit","Unbridled","Unprotected","Passionate","Hate-Fueled",
								# "Interracial","Wall-Banging","Steamy","Wanton","Lustful","Hot",
								# "Steamy","Lust-Fueled","Loud","Filthy"])
		# SexAdjs2 = WordList(["Illicit","Unbridled","Unprotected","Passionate","Extramarital",
								# "Interracial","Wild","Loud","Kinky"])
		# sSexAdj1 = SexAdjs1.GetWord()
		# sSexAdj2 = SexAdjs2.GetWord(NotList = [sSexAdj1])
		
		# ManNotList = []
		# Man = MaleChar(iNumMaxCBits = 3, iNumMinCBits = 2, NotList = ManNotList, bAddArticle = False, bAllowGang = False, bAllowRelate = False, bAllowAttitude = False, bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, bAllowNation = False)
		# GirlNotList = []
		# Girl = FemaleChar(iNumMaxCBits = 3, iNumMinCBits = 2, NotList = GirlNotList, bAddArticle = False, bAllowRelate = False, bAllowAttitude = False, bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, bAllowNation = False)

		# sTweet = "When the " + Girl.Desc + "\n"
		# sTweet += "Met the " + Man.Desc + "\n"
		
		# iRand = randint(1,3)
		# if iRand == 1:
			# PublicPlaces = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section",
				# "on the Coffee Table","in the Restroom at Chiopotle","Behind the Dumpster","Behind the Chic-fil-a", 
				# "in the Ball Pit", "in the Whole Foods Parking Lot","in the Men's Room","in a Stall in the Ladies Room",
				# "on a Bench in the Park","Under the Boardwalk at the Beach","on the Eliptical Machine at the Gym",
				# "at the Seafood Restaurant","in the Locker Room Showers","at the Museum","in the Non-Fiction Section at the Library",
				# "at the Farmer's Market","in the Window of a Shoe Store","in the Auto Parts Section at a Wal-Mart",
				# "in the Church Graveyard","in the Back of a Church","in a House They Broke Into","in a Motel 6",
				# "next to the Assembly Line","on a Hotel Balcony","in Her Parents Bedroom","on the Floor of the Restroom",
				# "in a Truck Stop Bathroom","in a Parking Garage","in a Changing Room"
				# ])
			# sTweet += "...and They Had " + sSexAdj1 + ", " + sSexAdj2 + " Sex " + PublicPlaces.GetWord() + "!"
		# elif iRand == 2:
			# Gangs = WordList(["a Construction Crew","a Biker Gang","a Basketball Team","the Football Team","some Carnies",
								# "a Chain Gang","some Chippendales Dancers","some Coal Miners","the Cops","some Cowboys","some Firemen",
								# "a Hockey Team","Identical Triplets","a Men's Volleyball Team","the Guys at the Gym",
								# "some Rednecks","some Mountain Men","a Band of Pirates","a Rock Band","some Pro Wrestlers",
								# "some Sumo Wrestlers","a Rugby Team","a S.W.A.T. Team","a Viking Horde","a Werewolf Pack",
								# "a Group of Sailors","some Fraternity Brothers","some Professional Bull Riders",
								# "the Kappa Omega Kappa Fraternity House","some Gay-for-Pay Porn Stars"])
			# sTweet += "...and They Had " + WordList(["Group Sex","an Orgy","a Gang Bang"]).GetWord() + " With " + Gangs.GetWord() + "!"
		# else:
			# sTweet += "...and They Had " + sSexAdj1 + ", " + sSexAdj2 + " Sex!"
		
		# return sTweet	
		
# I Lost My Virginity To 
# A Tanned Leather Cowboy 
# And he was my old 7th grade chemistry teacher
class Generator81(Generator):
	ID = 81
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
		Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
			"Behind the Chic-fil-a", "in the Ball Pit","Behind a Bench in the Park","at the Beach","Under an Overpass",
			"on the Eliptical Machine at the Gym","In the Locker Room Showers","at the Seafood Restaurant","at the Museum",
			"at the Library","at the Farmer's Market","next to the Duck Pond","in the Back of a Church","On Top of the Bar",
			"in the Window Display of a Shoe Store","Under the Boardwalk","in the Hunting Section at a Wal-Mart",
			"in the Church Graveyard","in a White Van Under an Overpass","at the Construction Site","next to the Assembly Line",
			"on a Hotel Balcony","in a Room at a Motel 6","in my Parent's Bedroom","at the Pet Store","Beside the Bike Path",
			"Behind the Bleachers","Behind the Bar","In the Back Seat of a Prius","In the Back of a Ford 150",
			"In the Back Seat of a Volvo","In the Back of a Movie Theater"
			])
		Retailers = WordList(["In-n-Out Burger","Whole Foods","Wal-Mart","Starbucks","Gold's Gym","LA Fitness","Krispy Kreme",
							  "CVS","Target","Chipotle","Burger King","the Mall","IHOP","the Multiplex","an Apple Store"])
		
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, NotList = ManNotList, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowTrope = False, bAllowGenMod = False)

		if CoinFlip():
			sTweet = "I Lost My Virginity\n"
			sTweet += "to " + AddArticles(Man.Desc) + "\n"
		else:
			sTweet = "I Got My Cherry Popped\n"
			sTweet += "by " + AddArticles(Man.Desc) + "\n"
		
		iRand = randint(1,7)
		
		if iRand == 1:
			sTweet += "in the " + WordList(["Men's Room","Women's Restroom","Parking Lot"]).GetWord() + " " 
			sTweet += "at " + Retailers.GetWord()
		
		elif iRand == 2:
			sTweet += Places.GetWord()
		
		elif iRand == 3:
			sTweet += "and " + WordList(["Two","Two","Three","Three","Four","Five","Seven","Nine","Twelve","Thirteen","Twenty"]).GetWord() + " of His Buddies!"
		
		elif iRand == 4:
			iInches = randint(8,12)
			sTweet += "Who Used " + WordList(["a Cucumber","a Banana","an Eggplant","an Electric Toothbrush",
						"a " + str(iInches) + "\" Black Dildo",
						"a " + str(iInches) + "\" Steel Dildo"]).GetWord() + " On Me!"
		elif iRand == 5:
			sTweet += "Who Used To Be My " + WordList(["High School Chemistry Teacher","High School English Teacher","French Teacher",
						"Gym Teacher","6th Grade Teacher","7th Grader Teacher","8th Grade Teacher","Chemistry Teacher","Algebra Teacher",
						"Literature Professor","Boss","Boss at " + Retailers.GetWord(),"Math Tutor","Next Door Neighbor","Gym Coach","Track Coach",
						"Basketball Coach","Pediatrician","Gynecologist"]).GetWord() + "!"
		elif iRand == 6:
			sTweet += "and Then I Realized He Was " + WordList(["My New Step-Dad","My New Step-Brother",
						"My New Next Door Neighbor","My New Brother-in-Law","My Literature Professor",
						"My Biology Professor","My Gynecologist", "My Mom's New Boyfriend"]).GetWord() + "!"
		else:
			sTweet += WordList(["Live on Television!","Live on the Internet!","And He Gave Me $100!",
								"And My Dad Was Pissed When He Found Out!","And I Let His Friends Watch!",
								"And a Cop Caught Us!","And We Filmed the Whole Thing!",
								"In the Basement of His Parents House!","Upstairs at His Parents House!",
								"And He Didn't Pull Out!","And He Did My Ass Too!","And Then My Parents Came Home!",
								"And His Sexy Wife!","And Now I'm Pregnant!"]).GetWord()
		
		return sTweet	
		
# "I'm a Pregnant Asian Waitress
# and
# I'm Stripping 
# For a Well-Hung Millionaire Sheikh!" (alt: I'm a pregnant asian waitress: what am I doing stripping for...??)
class Generator82(Generator):
	ID = 82
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sInnocentAdj = WordList(title.misc.NiceGirlGoodAdjs().List + ["Sweet"]).GetWord()
		
		GirlNotList = ['MILF','Older','Fertile','Slave Girl','Bikini Model','HuCow','Supermodel','Harem Princess',sInnocentAdj]
		Girl = FemaleChar(iNumMaxCBits = 3, iNumMinCBits = 1, NotList = GirlNotList, Type = GirlType.Good, bAddArticle = False, bAllowRelate = False, bAllowAttitude = False, bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, bAllowNation = True, bAllowGenMod = False, bAllowClothing = False, bAllowPhysChar = False, bAllowSexuality = False, bAllowMaritalStatus = False)

		ManNotList = ['Shape-Shifting']
		Man = MaleChar(iNumMaxCBits = 4, iNumMinCBits = 2, NotList = ManNotList, bAddArticle = False, bAllowGang = False, bAllowRelate = False, bAllowAttitude = True, bAllowSpecies = False, bAllowSkinHairColor = True, bAllowTitle = False, bAllowNation = True)
		
		Actions = WordList(["Stripping for","Posing Naked for","Taking Naked Pics for",
							 "Undressing for","Playing Doctor with","Playing 'Naughty Nurse' with",
							 "Giving a Full Frontal Massage to","Taking My Clothes Off for",
							 "Getting Naked for","Dancing Naked for","Modeling Erotic Lingerie for",
							 "Giving a Nude Massage to","Giving a Nude Lap Dance to","Pole Dancing Naked for",
							 "Being Handcuffed to a Bed by","Being Bent Over and Paddled by",
							 "Getting My Bare Bottom Spanked by"])
		sTweet = "\"I'm " + AddArticles(sInnocentAdj + " " + Girl.Desc)
		if CoinFlip():
			sTweet += "!\n" + "What Am I Doing " + Actions.GetWord() + "\n"
			sTweet += AddArticles(Man.Desc) + "?\""
		else:
			sTweet += "\nand I'm " + Actions.GetWord() + "\n"
			sTweet += AddArticles(Man.Desc) + "!\""
		
		return sTweet	
		
#The Virgin Christian Redheaded Librarian
#Tries an Interracial Threesome
class Generator83(Generator):
	ID = 83
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NiceGirl = title.misc.NiceGirl()
		
		NaughtyStuff = WordList(["69", "an Anal Hook","Anal Sex","BBC","BDSM","a Butt Plug","a Clit Clamp",
								 "a Dirty Sanchez","Double Penetration","Erotic Asphyxiation",
								 "an Interracial Threesome", "Leather Bondage","Lesbian Sex","Face-Sitting",
								 "Fisting","Nipple Clamps","Stripping at a Club","a Threesome",
								 "Watching Hardcore Porn","Butt Stuff","Anal Fisting","Edible Lube",
								 "Water Sports","Whips and Chains","Wife Swapping","Anal Beads",
								 "Getting Her Clit Pierced","Eating Ass","Ass-to-Ass","a Clit Pump",
								 "an Ass Vibe","a 12 inch Steel Dildo"])
		Extras = WordList(["with the Pope","with the Dalai Lama","with Miss America","with Her Step-Dad",
						   "with Her Step-Mom","with Her Step-Brother","with Her English Teacher",
						   "with Her Gym Coach","with Her Guidance Counselor","with Her Literature Professor",
						   "with Her Gynecologist","at the Zoo","in a Starbucks Restroom",
						   "in Her Parents Bedroom","in the Locker Room","at College","with Her Best Friend",
						   "with Her Tinder Date","at the Aquarium","with Her SCUBA Partner",
						   "with a Police Officer","with a 65-Year-Old Man","with Her Lab Partner",
						   "on the Coffee Table","on the Dining Room Table","on the Hotel Balcony",
						   "with a Total Stranger"])

		sTweet = "The " + NiceGirl.Desc + "\nTries " + NaughtyStuff.GetWord() 
		if CoinFlip():
			sTweet += "\n" + Extras.GetWord() + "!"

		return sTweet	
		
# Busty Princess Sophie
# Gets Tea-Bagged by the Goat Men
class Generator84(Generator):
	ID = 84
	Priority = 5
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		AdjNotList = ['Small-Town','Sun-Baked','Tanned','Natural','Succubus','Eager','Hot','Bronzed']
		SpecialAdjs = ['MILF','Virgin','Young','Teenage','Teen','Nubile','Supermodel','Submissive','Party Girl',
						'Goth','Tomboy','Schoolgirl','Co-ed','Daddy\'s Girl','BBW','Pixie','Chocolate','Wealthy',
						'Wealthy','Millionaire','Stuck-up','Haughty','Snooty','Snobbish','Rich','Bashful',
						'Blushing']
		Adjs = WordList(SpecialAdjs + title.misc.AttitudeGoodFemale().List + title.misc.NationFemale().List + title.misc.PhysCharFemale().List + title.misc.SkinHairColorFemale().List + title.misc.SpeciesFemale().List)
		Titles = WordList(['Princess','Princess','Princess','Heiress','Heiress','Queen','Duchess','First Lady','Lady',
							'Countess','Contessa'])
		VerbsBy = WordList(['Tea-Bagged','Paddled','Peed On','Used','Stripped in Public','Deflowered',
							'Anally Deflowered','Fisted','Anal Fisted','Beaten with a Belt','Enslaved',
							'Claimed in Public','Dominated in the Dungeon','Impregnated','Knocked Up',
							'Imprisoned in the Sex Dungeon','Milked','Motor-Boated','Mounted Bareback',
							'Paddled','Shaved','Pounded','Spanked','Spanked in Public','Spanked with a Belt',
							'Publically Whipped','Caught on Video','Gagged','Ball-Gagged','Ridden Bareback',
							'Deep Throated','Her Ass Eaten','Her Nipples Pierced','Her Clit Pierced',
							'Penetrated','Her Titties Sucked','Bound and Whipped','Bent Over','Spread-Eagled'])
		GangVerbs = WordList(['Peed On','Used','Bukkaked','Deflowered','Anally Deflowered',
							'Impregnated','Knocked Up','Imprisoned in the Sex Dungeon','Mounted Bareback',
							'Paddled','Pounded','Spanked','Spanked in Public','Ridden Bareback',
							'Double Penetrated','Triple Penetrated','Spit-Roasted','Bukkaked','Shared',
							'Gang-Banged','Bound and Whipped'])
		MaleNotList = ['Business Man','Charming','Sensitive']
		Master = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = True, sPosArticle = "Her", NotList = MaleNotList, bAllowGang = False,
							bAllowTrope = False, bAllowTitle = False, bAllowRelate = True)
		Gang = MaleGangChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = True, sPosArticle = "Her", NotList = MaleNotList, 
							bAllowTrope = False, bAllowProf = False)
		
		if CoinFlip():
			sTweet = self.HerName + " the " + Adjs.GetWord(NotList = AdjNotList) + " " + Titles.GetWord() + "\n"
		else:
			sTweet = Adjs.GetWord(NotList = AdjNotList) + " " + Titles.GetWord() + " " + self.HerName + "\n"
			
		if CoinFlip():
			sTweet += "Gets " + VerbsBy.GetWord() + " by " + Master.Desc
		else:
			sTweet += "Gets " + GangVerbs.GetWord() + " by " + Gang.Desc

		return sTweet	

class Generator85(Generator):
	ID = 85
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
		
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, NotList = ManNotList, bAllowRelate = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowGenMod = False)

		if CoinFlip():
			sTweet = "I Lost My Virginity\n"
			sTweet += "to " + AddArticles(Man.Desc) + "\n"
		else:
			sTweet = "I Got My Cherry Popped\n"
			sTweet += "by " + AddArticles(Man.Desc) + "\n"
		
		sTweet += WordList(["Live on Television!","Live on the Internet!","And He Gave Me $100!",
								"And My Dad Was Pissed When He Found Out!","And I Let His Friends Watch!",
								"And " + WordList(["a Cop","My Dad","the Principal","a Teacher","My Step-Brother","a Stranger"]).GetWord() + " Caught Us!",
								"And We Filmed the Whole Thing!","And Now I'm So Sore I Can Hardly Walk!",
								"In the Basement of His Parents House!","Upstairs at His Parents House!",
								"And He Didn't Pull Out!","And He Did My Ass Too!","And Then My Parents Came Home!",
								"And His Sexy Wife!","And Now I'm Pregnant!","Who Used To Be A Woman!"]).GetWord()

		return sTweet	
		
# I Shared My Innocent Asian Wife 
# with 
# A Well-Hung Beefy Fighter Pilot!
class Generator86(Generator):
	ID = 86
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ["Space","Gladiator","Knight","Viking","Warrior","Shape-Shifting","Ghost"]
		WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel"]
		
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, NotList = ManNotList, bAllowRelate = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowGenMod = False)
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = WomanNotList, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = False, bAddEndNoun = False)
		
		sTweet = "\"I Shared My " + Girl.Desc + " Wife\n"
		sTweet += "With " + AddArticles(Man.Desc) 
		
		if CoinFlip():
			sTweet += "\n" + WordList(["And She Let Me Watch","And I Haven't Seen Her Since","And She Let Him Do Butt Stuff",
										"And She Videoed The Whole Thing For Me", "And Now She Can't Get Enough",
										"And Now She's Insatiable","And It Turned Her Into A Wanton Slut",
										"And She Says He's Bigger Than I Am","On Our Annivesary",
										"As a Special Valentine's Day Gift","And Next Time It's My Turn",
										"And He Sent Me The Pictures","And Now She's Pregnant",
										"And They Let Me Watch","We Met At The Bar","We Found On Craigslist",
										"Who Has a BDSM Sex Dungeon","On Her Birthday","And That Was a Big Mistake",
										"And He Paid Us $10,000"]).GetWord()
		
		sTweet += "!\""
		
		return sTweet	
		
# Filming My Step-Son's Rich Bitch Wife
# In the Shower
# class Generator87(Generator):
	# ID = 87
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# Last Night a Sexy Dominatrix (Honey, A Sexy Dominatrix)
# Forced Me 
# To Eat Her Ass 
class Generator88(Generator):
	ID = 88
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Actions = WordList(["Forced Me\nTo Eat Her Ass","Spanked Me\nWith a Steel Paddle",
							"Whipped Me\nWith a Riding Crop","Dressed Me In Lingerie\nAnd Whipped My Ass",
							"Tied Me to the Bed Naked\nAnd Took Pics","Handcuffed Me\nAnd Whipped My Ass",
							"Forced Me\nTo Eat Her Out","Rode My Face","Smothered Me With Her Ass",
							"Spanked Me\nWith a Wooden Paddle","Beat Me\nWith a Wooden Spoon",
							"Made Me Wear Nipple Clamps","Made Me Wear a Ball Gag",
							"Made Me Wear a Gimp Mask","Made Me\nEat Her Panties","Cuffed Me to My Bed",
							"Rode Me\nWith a Strap-On","Used a Strap-On\nOn My Ass",
							"Made Me\nWear Women's Lingerie","Made Me\nDrink Her Pee",
							"Made Me\nEat Her Ass","Spanked Me\nIn Assless Chaps",
							"Dominated Me\nWith Her Ass","Dominated Me\nIn Her Sex Dungeon",
							"Made Me\nWear a Butt Plug"])
		
		GirlNotList = ['Desperate','Willing','Little','Fashionable','Anal Virgin','Slave']
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, bAddArticle = False, Type = GirlType.Bad, NotList = GirlNotList,
							bAllowTrope = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowRelate = False, bAllowSexuality = False, bAllowTitle = False)
							
		sTweet = "Last Night\n" + AddArticles(Girl.Desc) + "\n" + Actions.GetWord()

		return sTweet	
		
# Sweet Little Sophie 
# The Country Virgin Schoolgirl
# and the
# Swollen 8" Purple Dick
class Generator89(Generator):
	ID = 89
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		SweetAdjs = WordList(['Sweet', 'Sweet', 'Cute', 'Blonde','Innocent','Bashful','Naive'])
		NiceNames = WordList(['Amy','Angelica','Annie','Charity','Daisy','Daphne','Elsie',
							  'Emmy','Frances','Gertrude','Greta','Jeanie','Lacey','Lizzy',
							  'Mabel','Mary','Maryanne','Molly','Nancy','Nell','Olive','Phoebe',
							  'Rosie','Shelly','Sophie','Summer','Virginia'])
							  
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
		
		BigAdjs = WordList(["Massive","Enormous","Girthy","Thick","Lengthy","Oversized","Stacked","Swinging",
							"Monstrous","Big","Giant","Hulking","Hefty","Heavy","Towering"])
		SwoleAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Hard","Erect","Stiff","Tumescent",
							  "Fat","Bulging","Rigid","Fully Erect","Hugely Erect"])
		ExtraAdjs = WordList(["Veiny","Throbbing","Meaty","Burning","Dripping","Purple","Red","Exposed",
							  "Fleshy","Straining","Feverish","Lustful","Passionate","Fervid","Throbbing",
							  "Pulsating","Vigorous","Virile","Dark","Moist","Black","Rampant"])
		DickSyns = WordList(["Dick","Dick","Cock","Cock","Prick","Erection","Member","Phallus","Tool","Hard-On",
							 "Dong","Schlong","Penis"])
		sDick = ""
		
		if CoinFlip():
			sDick = BigAdjs.GetWord() + " " + SwoleAdjs.GetWord() + " " + ExtraAdjs.GetWord() + " " + DickSyns.GetWord()
		else:
			sDick = SwoleAdjs.GetWord() + " " + str(randint(8,12)) + "-inch " + ExtraAdjs.GetWord() + " " + DickSyns.GetWord()

		sTweet = SweetAdjs.GetWord() + " Little " + NiceNames.GetWord() + "\n"
		sTweet += "The " + sNiceGirl + "\nand the " + WordList(["Case of the","Tale of the","Adventure of the","Secret of the","Curse of the"]).GetWord() + "\n"
		sTweet += sDick 
		
		return sTweet	
	
# A Big Day for Veronica:
# The Nubile Nympho Teen Slut 
# Gets Anal Fisted 
class Generator90(Generator):
	ID = 90
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotGirlList = ["Harem Princess"]
		Girl = FemaleChar(iNumMinCBits = 3, Type = GirlType.Bad, NotList = NotGirlList, bAllowSpecies = False)

		
			
		sHerName = NamesFemale().FirstName()
		
		sTweet = "A Big Day for " + sHerName + ":\n"
		sTweet += "The " + Girl.Desc + "\n"
			
		iRand = randint(1,13)
		if iRand < 3:
			ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
						  "Throbbing","Meaty","Burning","Dripping","Purple","Red","Fleshy","Lustful","Passionate",
						  "Throbbing","Pulsating","Vigorous","Virile","Moist","Black","Stiff","Girthy"])
			sTweet += "Gets a " + ErectAdjs.GetWord() + " " + str(randint(8,12)) + "\" Surprise"
		elif iRand == 3:
			sTweet += "Makes Her First " + WordList(["Lesbian","Hardcore","Anal","Gangbang","Creampie","Bondage"]).GetWord() + " Porno"
		elif iRand == 4:
			sTweet += "Gets Her " + WordList(["Nipples","Clit","Labia","Taint","Ass Dimples"]).GetWord() + " Pierced"
		elif iRand == 5:
			Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
			"at the Chic-fil-a","in the Ball Pit","at the Park","at the Beach","Under an Overpass","at the Gym",
			"on the Eliptical Machine at the Gym","at the Seafood Restaurant","at the Museum","at Burger King",
			"at the Library","at the Farmer's Market","next to the Duck Pond","at Church","at the Bar",
			"in the Window Display of a Shoe Store","at Wal-Mart","at Starbucks","at School","on Campus",
			"in the Church Graveyard","at a Construction Site","at Rush Hour Traffic","at Her Uber Driver",
			"on a Hotel Balcony","Beside the Bike Path","at the Mail Man","at the Amazon Delivery Guy",
			"Behind the Bleachers","In the Back of a Ford 150","In a Movie Theater","at Chipotle","at Barnes & Noble",
			"at Whole Foods","at the Mall","at the CVS"
			])
			sTweet += "Flashes Her " + WordList(["Tits","Ass","Pussy"]).GetWord() + " " + Places.GetWord()
		elif iRand == 6:
			sTweet += "Has Her First " + WordList(["Threesome","Foursome","Fivesome","Orgy","Gang Bang","Black Gang Bang"]).GetWord()
		elif iRand == 7:
			sTweet += "Has a " + WordList(["Dick","Cock","Penis","Prick"]).GetWord()
		elif iRand == 8:
			sTweet += "Tries a Glory Hole"
		elif iRand == 9:
			sTweet += "Gets " + WordList(["Fisted","Anal Fisted","Bukkake'd","Double-Penetrated","Spit-Roasted",
										  "Blindfolded and Whipped","Shared with Strangers"]).GetWord()
		elif iRand > 10 and iRand < 12:
			sTweet += WordList(["Gets"]).GetWord() + " " 
			sTweet += WordList(["Her Neighbor's","Her Step-Brother's","Her Professor's","Her Teacher's","Her Boss's",
								"Her Step-Dad's","Her Uncle's","Her Gym Coach's","Her Gynecologist's","A Stranger's"]).GetWord() + " "
			sTweet += WordList(["Dick","D","Cock","Hard Cock","Fat Dick","Dingus","Meat Stick","Flesh Pole","Fat Boner"]).GetWord()
		else: 
			sTweet += "Tries " + WordList(["a Butt Plug","an Anal Hook","Nipple Clamps","a Ball Gag","a Clit Clamp",
												"Crotchless Panties","a Strap-On","a Remote-Controlled Vibrator",
												"Anal Beads"]).GetWord()

		return sTweet	
		
# I Spent the Night With
# A Buff Well-Hung Mossad Agent
# And a Sexy Cheerleader Stripper!
class Generator91(Generator):
	ID = 91
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Prefix = WordList(["I Spent the Night with","I Slept with","I Showered with","I Went Down on","I Made Love to",
							"I Was Pleasured by","I Got Pounded by","I Was Taken Passionately by",
							"I Was Mounted from Behind by","I Had Sex With","I Shared a Night of Passion with",
							"I Had a Steamy Affair with", "I Had an Affair with","I Spent a Wild Night with",
							"I Shared a Night of Lust with","I Had a Forbidden Affair with",
							"I Had a Secret Affair with","I Was Ridden Hard by"])
		
		ManAdjNotList = ['Fine','Naked','Clever','Highly Eligible','Visibly Erect','Bare-Chested']
		ManAdjs = WordList(title.misc.AttitudeMale().List + title.misc.SkinHairColorMale().List + title.misc.NationMale().List + title.misc.PhysCharMale().List + title.misc.DickCharMale().List + ['Older','Married','Heavily-Tattooed','Naked'])
		if CoinFlip():
			sMan = ManAdjs.GetWord(NotList = ManAdjNotList) + " " + title.misc.ProfMale().GetWord()
		else:
			sManAdj1 = ManAdjs.GetWord(NotList = ManAdjNotList)
			sManAdj2 = ManAdjs.GetWord(NotList = ManAdjNotList + [sManAdj1])
			sMan = sManAdj1 + " " + sManAdj2 + " " + title.misc.ProfMale().GetWord()
		
		WomanAdjNotList = ['Little','Natural','Desperate','Moist','Wet','Narrow-Waisted','Flat-Chested','Revealing']
		WomanAdjs = WordList(title.misc.PhysCharFemale().List + title.misc.AttitudeBadFemale().List + ['Older','Pregnant','Cougar','Insatiable','Submissive','Dominant','European','Bisexual','Open-Minded','Pregnant','Teenage','Eager','Nympho','Naughty','Sexy','Horny','Well-Endowed'])
		sWoman = WomanAdjs.GetWord(NotList = WomanAdjNotList) + " " + WordList(['Wife','Girlfriend']).GetWord()
		
		sTweet = "\"" + Prefix.GetWord() + "\n" + AddArticles(sMan) + "\nand his " + sWoman + "!\""

		return sTweet	
		
# "I Gave A Naked Italian Airline Stewardess
# A Full Frontal Massage!"
# class Generator92(Generator):
	# ID = 92
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# Veronica Puts On Latex (Leather/A Butt Plug):
# Let the Hotwife Games Begin! (Bondage/BDSM/Dominatrix)
# class Generator93(Generator):
	# ID = 93
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# "I'm a Stay-at-Home Mommmy Blogger
# And A Billionaire Biker
# Spooned Me Hard!"
# class Generator94(Generator):
	# ID = 94
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# Welcome to Pound Town, Miss Dixon!
class Generator95(Generator):
	ID = 95
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Suffixes = WordList(["berg","berg","ville","ville","town"," Town"," City"])
		sLastName = ""
		sLastName = title.names.LastNames().GetWord() 
		
		if CoinFlip():
			#For a woman
			Prefixes = WordList(["Drill","Fuchs","Cocks","Pound","Ball","Dix","Pricks","Shafts","Bawl","Cox","Pecker",
								 "Bang","Peen","Swallow","Pork"])
								 
			sTweet = "\"Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", " + WordList(["Miss","Mrs"]).GetWord() + " " + sLastName + "!\""
		else:
			#For a man
			Prefixes = WordList(["Beaver","Boob","Ass","Buttes","Kuntz","Slutt","Fuchs","Tits","Brest","Blow","Suck",
								 "Bang","Anal","Muff","Pork","Booty"])
			sTweet = "\"Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", Mr. " + sLastName + "!\""			 

		return sTweet	
		
# In Love With
# My Innocent Amish Maid's 
# Enormous Coconuts 
class Generator96(Generator):
	ID = 96
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = title.misc.NiceGirl(NotList = ['Wife','Girlfriend'])
		SizeAdj = WordList(['Enormous','Gigantic','Titantic','Humongous','Massive','Sumptuous','Milky','Giant',
							'Honking','Juicy','Jiggling','Double D','Magnificent','Gargantuan','Jumbo',
							'Heavenly'])
		Breasts = WordList(['Coconuts','Tatas','Breasticles','Gazongas','Titties','Mammaries','Melons',
							'Cantaloups','Jugs','Fun-Bags','Jubblies','Knockers','Hooters','Bazooms','Bosoms',
							'Milk Balloons','Juice-Bags','Sweater-Zeppelins','Grapefruits','Pumpkins',
							'Grand Tetons','Hangers','Bongos','Meat-Melons','Love-Pillows','Udders'])
							
		sTweet = WordList(["In Love With","Falling For","Head-Over-Heels For","Captivated By",
						   "Bewitched By","Entranced By","Enraptured By","Spellbound By"]).GetWord()
		sTweet += "\nMy " + Girl.Desc + "'s\n"
		sTweet += SizeAdj.GetWord() + " " + Breasts.GetWord()

		return sTweet	

# The Secretary 
# is wearing
# a butt plug		
class Generator97(Generator):
	ID = 97
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		LadyJobs = WordList(['Airline Stewardess','Babysitter','Ballerina','Barista','Cheerleader',
							'Co-ed','Fashion Model','Flight Attendant','Gymnast','House Maid',
							'Intern','Librarian','Maid','Nanny','Nun','Nurse','Secretary',
							'Supermodel','Teacher','Waitress','Bikini Model','Hooter\'s Waitress',
							'Yoga Instructor','Actress'])
							
		Accessories = WordList(['a Butt Plug','Anal Beads','Nipple Clamps','a Clit Clamp','a Strap-On',
								'an Anal Hook','a Remote-Controlled Vibrator','Crotchless Panties',
								'Edible Panties','Nipple Pasties','a Pony Tail Butt Plug',
								'Assless Chaps','a Ball Gag','a Rubber Fetish Mask','a Latex Body Suit',
								'a Rubber Fetish Suit','a Transparent Bikini','a Chastity Belt'])
								
		sTweet = "The " + LadyJobs.GetWord() + "\nIs Wearing\n" + Accessories.GetWord()

		return sTweet	
		
class Generator98(Generator):
	ID = 98
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = NamesFemale().FirstName()
		
		NaughtyStuff = WordList(["Does Nipple Play with","Gets Fisted by","Tries Bukkake with","Jerks Off",
								 "Tries Forced Feminization with","Gets Spanked by", "Tries Hardcore Bondage with",
								 "Tries Water-Sports with","Sixty-Nines","Gets Erotically Asphyxiated by",
								 "Does Anal with","Does Butt Stuff with","Gets Anal Fisted by",
								 "Tries Double Penetration with","Deep Throats","Gets Tea-Bagged by",
								 "Tries Triple Penetration with","Gets a Dirty Sanchez from",
								 "Gets Whipped By","Gets Hotwifed to","Gags On","Gets Her Ass Eaten by",
								 "Gives a Rim-Job to","Has Twincest with","Tries Leather Bondage with",
								 "Gets Peed on by"])
								 
		MaleAdjs = WordList(title.misc.PhysCharMale().List + title.misc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','DILF','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
		Species = WordList(["Unicorn","Centaur","Werewolf","Merman","Dragon","Goat Man","Dwarf",
							"Space Alien","Tentacle Monster","Pirate","Trapeze Artist","Clown", 
							"Sumo Wrestler","Were-Horse","Werewolf","Dinosaur", "Dinosaur",
							"Vampire","Martian","Contortionist","Warlock","Minotaur",
							"Reverse Centaur","Male Porn Star","Pirate Captain","Giant",
							"Green Beret","Navy SEAL","Priest","Biker","Male Model","Unicorn",
							"Rodeo Clown","Astronaut","Ghost","Zombie"])
							
		sTweet = sHerName + "\n" + NaughtyStuff.GetWord() + "\n"
		sTweet += AddArticles(MaleAdjs.GetWord() + " " + Species.GetWord())

		return sTweet	
		
class Generator99(Generator):
	ID = 99
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHerName = NamesFemale().FirstName()
		
		NaughtyStuff = WordList(["Does Nipple Play with","Gets Fisted by","Tries Bukkake with","Jerks Off",
								 "Tries Forced Feminization with","Gets Spanked by", "Tries Hardcore Bondage with",
								 "Tries Water-Sports with","Sixty-Nines","Gets Erotically Asphyxiated by",
								 "Does Anal with","Does Butt Stuff with","Gets Anal Fisted by",
								 "Tries Double Penetration with","Deep Throats","Gets Tea-Bagged by",
								 "Tries Triple Penetration with","Gets a Dirty Sanchez from",
								 "Gets Whipped By","Gets Hotwifed to","Gags On","Gets Her Ass Eaten by",
								 "Gives a Rim-Job to","Has Twincest with","Tries Leather Bondage with",
								 "Gets Peed on by"])
								 
		MaleAdjs = WordList(title.misc.PhysCharMale().List + title.misc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','DILF','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
		Species = WordList(["Unicorn","Centaur","Werewolf","Merman","Goat Man","Dwarf",
							"Space Alien","Tentacle Monster","Pirate","Trapeze Artist","Were-Horse",
							"Werewolf","Dinosaur", "Dinosaur","Vampire","Martian","Contortionist",
							"Warlock","Minotaur","Reverse Centaur","Giant","Unicorn",
							"Ghost","Zombie"])
		Jobs = WordList(['Airline Pilot','Astronaut','Assassin','Athlete','Attorney','Body Builder',
							'Bodyguard','Boxer','Brain Surgeon','Bull Rider','Business Man',
							'Chippendales Dancer','CIA Agent','Coal Miner','Construction Worker',
							'Cop','Cowboy','Defensive Lineman','Doctor','Fashion Photographer',
							'FBI Agent','Fighter Pilot','Fighter Pilot','Fire Fighter',
							'Green Beret','Gunslinger','Gym Coach','Surgeon','Hitman',
							'Investment Banker','Killer-for-Hire','Lawyer','Long Haul Trucker',
							'Lumberjack','Male Escort','Male Model','Male Nurse','Matador',
							'MI5 Agent','Mossad Agent','MMA Fighter','Navy Seal','Pirate',
							'Preacher','Priest','Private Eye','Professor','Quarterback',
							'Rock Guitarist','Rodeo Clown','Sailor','Secret Agent',
							'Secret Service Agent','Sheriff','Deputy','Snowboarder','Spy',
							'Stockbroker','Stuntman','Sumo Wrestler','Surfer','Tattoo Artist','Trucker',
							'Porn Star','Biker','Contortionist'])
							
		sTweet = sHerName + "\n" + NaughtyStuff.GetWord() + "\n"
		sTweet += AddArticles(Species.GetWord() + " " + title.misc.ProfMale().GetWord())

		return sTweet	

# I Secretly Impregnated 
# My Nudist Mommy-Blogger Sister-in-Law!		
class Generator100(Generator):
	ID = 100
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlAdj = WordList(title.misc.PhysCharFemale().List + ['Fertile','Naked','Sassy','Saucy','Sexy','Black','Ebony','Bisexual'])
		GirlNoun = WordList(title.misc.ProfGoodFemale().List + title.misc.SpeciesFemale().List)
		Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
							"Daughter-in-Law","Cousin"])
						
		sTweet = "I Secretly Impregnated\nMy " 
		if CoinFlip():
			sTweet += GirlAdj.GetWord() + " " + GirlNoun.GetWord() + " " + Relate.GetWord()
		else:
			MaleRelate = WordList(["Best Friend's","Step-Father's","Dad's","Boss's","Neighbor's"])
			sTweet += MaleRelate.GetWord() + "\n" + GirlAdj.GetWord() + " " + GirlNoun.GetWord() + " " + WordList(["Wife","Girlfriend","Fiancé"]).GetWord()

		return sTweet	
		
# Butt Stuff 
# With My 
# Biology Professor (Spanish Teacher / Math Tutor)
# class Generator101(Generator):
	# ID = 101
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
	
# Backdoor Lovin'
# for the 
# Jiggling Farmer's Daughter	
class Generator102(Generator):
	ID = 102
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlAdjs = WordList(['Amish','Country','Small-Town','Young','Nubile','Naive','Newlywed','Virginal',
							 'Virgin','Chaste','Conservative','Submissive','Christian','Mormon','Blushing',
							 'Bashful','Sheltered','Shy','Wholesome','All-American','Geeky','Sweet',
							 'Country','Willing','Jiggling','Busty','Curvy','Horny','Naughty','Slender',
							 'Adventurous','Blossoming','Skinny','Flat-Chested','Round-Bottomed'])
							 
		GirlTropes = WordList(['Babysitter','Cheerleader','Co-ed','House Maid','Housewife','Librarian',
								'Milk Maid','Nanny','Nun','3rd Grade Teacher','1st Grade Teacher','Teacher',
								'5th Grade Teacher','Waitress','Stay-at-Home Mom','Maiden','Girl','Lady',
								'Southern Bell','Farmer\'s Daughter','Pastor\'s Wife','Wife','Prom Queen',
								'Beauty Queen','Virgin','Nurse'])
		
		sTweet = "Backdoor Lovin'\n"
		if CoinFlip():
			sTweet += "for the\n"
			if CoinFlip():
				sAdj1 = GirlAdjs.GetWord()
				sTweet += sAdj1 + " " + GirlTropes.GetWord(NotList = [sAdj1])
			else:
				sAdj1 = GirlAdjs.GetWord()
				sAdj2 = GirlAdjs.GetWord(NotList = [sAdj1])
				sTweet += sAdj1 + " " + sAdj2 + " " + GirlTropes.GetWord()
		else:
			sAdj1 = GirlAdjs.GetWord()
			GirlNotList = ['Girl','Lady','Pastor\'s Wife','Farmer\'s Daughter','Babysitter','House Maid',
							'Wife','Prom Queen','Teacher','Nurse', 'Milk Maid', sAdj1]
			sTweet += "For My\n" + sAdj1 + " " + GirlTropes.GetWord(NotList = GirlNotList) + " " + WordList(["Step-Daughter","Daughter-in-Law","Sister-in-Law","Step-Sister","Step-Mom","Mother-in-Law","MILF","House Maid","Wife","Bride","Babysitter","Teacher","Nurse"]).GetWord()

		return sTweet	
		
# My Mother-in-Law is 
# A Tanned Cheerleader 
# and I Got Her Pregnant!
class Generator103(Generator):
	ID = 103
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlAdj = WordList(title.misc.PhysCharFemale().List + title.misc.NationFemale().List + title.misc.AttitudeGoodFemale().List + title.misc.SkinHairColorFemale().List + ['Fertile','Naked','Sassy','Saucy','Sexy','Black','Ebony','Bisexual'])
		GirlNoun = WordList(title.misc.ProfGoodFemale().List + title.misc.TropesGoodFemale().List + title.misc.SpeciesFemale().List)
		Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
							"Daughter-in-Law","Cousin"])
						
		sTweet = "My " + Relate.GetWord() + " is\n"
		sTweet += AddArticles(GirlAdj.GetWord() + " " + GirlNoun.GetWord()) + ",\n"
		sTweet += "and " + WordList(["I Got Her Pregnant","I Got Her Pregnant","I Knocked Her Up"]).GetWord() + "!"

		return sTweet	
		
# Claimed on the Coffee Table
# by a Burly Centaur Sailor
class Generator104(Generator):
	ID = 104
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(['Claimed','Claimed Forcefully','Claimed Hard','Deflowered','Impregnated','Knocked Up',
							'Motor-Boated','Mounted','Paddled','Pleasured','Ravished','Ravished','Satisfied',
							'Taken','Taken Forcefully','Taken From Behind','Taken Roughly'])
		Location = WordList(['On the Coffee Table','On the Bathroom Floor','On the Kitchen Counter',
							 'In the Back Seat','On a Park Bench','On the Washing Machine',
							 'Under a Jungle Gym','On a Merry-Go-Round','On an Elliptical Machine',
							 'On a Treadmill','On a Trampoline','In a Kiddie Pool','On a See-Saw',
							 'On the Dining Room Table','On an Ikea Futon'])
		ManNotList = ['Single']
		Man = MaleChar(iNumMaxCBits = 3, bAddArticle = False, bAllowGang = False, bAllowTitle = False)
		
		sTweet = Verbs.GetWord() + " " + Location.GetWord() + "\nby " + AddArticles(Man.Desc)

		return sTweet	

# Brigitte Gets Claimed by 
# The Well-Hung Naked Manor Lord 
# On the Back of a Horse		
class Generator105(Generator):
	ID = 105
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Adjs = WordList(['Lustily','Vigorously','Ardently','Passionately','From Behind','Fearlessly',
						'Fervently','Forcefully','Repeatedly','Anally'])
		GirlNames = WordList(['Alice','Alina','Amelia','Anastasia','Anna','Anabel','Beatrice','Belle',
							  'Brigitte','Carmina','Charity','Chastity','Clover','Colette',
							  'Constance','Cordelia','Daphne','Delilah','Delores','Eleanor',
							  'Elizabeth','Emma','Esmerelda','Estelle','Felicia','Felicity',
							  'Fiona','Greta','Isabelle','Josephine','Juliette','Lilah','Margaret',
							  'Mary','Molly','Morgan','Nell','Olive','Ophelia','Rosaline','Rose',
							  'Saffron','Sarah','Sophie','Violet'])
		MaleNouns = WordList(['Barbarian','Warrior','Knight','Bandit','Highwayman','Prince','Duke',
								'Paladin','Monk','Rogue','Thief','Warlock','Hunter','Swordsman','Soldier',
								'Troubador','Woodsman','Blacksmith','Manor Lord','Marquis','Baron','Pirate',
								'Nobleman','Ruffian','Knave','Wizard','Sorcerer','Viking Warrior',
								'Crusader','Cavalier'])
		Suffixes = WordList(['On the Back of a Horse','In the Ruins of a Castle','In the Castle Dungeon',
							 'On Top of a Hay Stack','Behind the Chicken Coop','Behind the Cow Shed',
							 'While her Entire Village Watches',
							 'and His Band of ' + str(randint(3,12)) + ' Merry Men',
							 'and His Band of ' + str(randint(3,12)) + ' Merry Men',
							 'and He Doesn\'t Pull Out!','Even Though She\'s a Nun',
							 'Even Though She\'s a Virgin','In the Enchanted Forest',
							 'And Then By His Brother','In the Royal Bedchamber',
							 'In the Castle Privy','In the Great Hall','Using a Magic Spell',
							 'Using a Broomstick','Wearing a Leather Condom Atop His Cock',
							 'On the Back of a Donkey','Using Forbidden Sex Magic',
							 'in a Turnip Field','in the Village Church','in a Monastary',
							 'and They Live Happily Ever After','and She Finds It Quite Agreeable',
							 'Who is Secretly the King','In the Smithy','In the Tannery',
							 'And He Doth Pleasure Her Greatly','And Verily! she is Well Satisfied',
							 'While a Unicorn Watches','On the Deck of a Pirate Ship',
							 'In the Old Castle Ruins','After They Meet on Tinder',
							 'With a Very Comely Cock','Using a Leather Condom for Protection',
							 'Wearing an Enchanted Cock Ring'])
							 
		ManNotList = ['S.W.A.T. Team','Cyborg','Alien','Single','Taboo','Bareback']
		Man = MaleChar(iNumMaxCBits = 2, iNumMinCBits = 1, bAddEndNoun = False, bAddArticle = True, NotList = ManNotList,
						bAllowAge = False, bAllowRelate = False, bAllowProf = False, bAllowTrope = False, bAllowNation = False, bAllowTitle = False, bAllowMaritalStatus = False)
		sDesc = Man.Desc.strip()
		
		sTweet = GirlNames.GetWord() + " is Claimed " + Adjs.GetWord() + "\n"
		sTweet += "by " + sDesc + " " + MaleNouns.GetWord()
		sTweet += "\n" + Suffixes.GetWord()

		return sTweet	
		
class Generator106(Generator):
	ID = 106
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Adjs = WordList(['Lustily','Vigorously','Ardently','Passionately','From Behind','Fearlessly',
						'Fervently','Forcefully','Repeatedly','Anally'])
		GirlNames = WordList(['Alice','Alina','Amelia','Anastasia','Anna','Anabel','Beatrice','Belle',
							  'Brigitte','Carmina','Charity','Chastity','Clover','Colette',
							  'Constance','Cordelia','Daphne','Delilah','Delores','Eleanor',
							  'Elizabeth','Emma','Esmerelda','Estelle','Felicia','Felicity',
							  'Fiona','Greta','Isabelle','Josephine','Juliette','Lilah','Margaret',
							  'Mary','Molly','Morgan','Nell','Olive','Ophelia','Rosaline','Rose',
							  'Saffron','Sarah','Sophie','Violet'])
		MaleNouns = WordList(['Barbarian','Warrior','Knight','Bandit','Highwayman','Prince','Duke',
								'Paladin','Monk','Rogue','Thief','Warlock','Hunter','Swordsman','Soldier',
								'Troubador','Woodsman','Blacksmith','Manor Lord','Marquis','Baron','Pirate',
								'Nobleman','Ruffian','Knave','Wizard','Sorcerer','Viking Warrior',
								'Crusader','Cavalier'])
							 
		ManNotList = ['S.W.A.T. Team','Cyborg','Alien','Single','Taboo','Bareback']
		Man = MaleChar(iNumMaxCBits = 2, iNumMinCBits = 1, bAddEndNoun = False, bAddArticle = True, NotList = ManNotList,
						bAllowAge = False, bAllowRelate = False, bAllowProf = False, bAllowTrope = False, bAllowNation = False, bAllowTitle = False, bAllowMaritalStatus = False)
		sDesc = Man.Desc.strip()
		
		sTweet = GirlNames.GetWord() + " is Claimed " + Adjs.GetWord() + "\n"
		sTweet += "by " + sDesc + " " + MaleNouns.GetWord()

		return sTweet	
		
# Claimed at Castle Tittyfuck
class Generator107(Generator):
	ID = 107
	Priority = 4
	
	def WordCombiner(self, sFirstWord, sSecWord):
		sCombined = ""
		
		if len(sFirstWord) > 2 and len(sSecWord) > 2:
			if sFirstWord[-2:-1] == sFirstWord[-1:] and sFirstWord[-1:] == sSecWord[0]:
				# if the last two characters of the first word are the same and they are the same as the second word, remove one 
				sCombined = sFirstWord[:-1] + sSecWord
			elif sFirstWord[-2:] == "er" and sSecWord[-2:] == "er":
				# if both words end in 'er', remove the first 'er'
				sCombined = sFirstWord[:-2] + sSecWord
			elif sFirstWord[-1:] == "a" and sSecWord[0] == "a":
				# if the first word ends in 'a' and the second word begins with it, remove one
				sCombined = sFirstWord[:-1] + sSecWord
			elif sFirstWord[-1:] == "r" and sSecWord[0] == "r":
				# if the first word ends in 'r' and the second word begins with it, remove one
				sCombined = sFirstWord[:-1] + sSecWord
			else:
				sCombined = sFirstWord + sSecWord 
		else:
			sCombined = sFirstWord + sSecWord
			
		return sCombined
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Prefix = WordList(["Claimed at", "Enslaved at", "Taken at", "Imprisoned at", "Claimed at","The Dungeons of",
							"The Halls of","The Prisoner of","The Princess of","The Master of","The Baron of",
							"Deflowered at","Despoiled at","Ravished at","Seduced at","The Knight of",
							"The Lady of","The Virgins of","The Baroness of","The Dutchess of",
							"Naked at","The Harem Girls of","The Maidens of","The Queen of",
							"The Mistress of","The Wizard of","Betrayed at"])
		
		FirstNouns = WordList(["cock","cunt","puss","vaj","slut","twat","spunk","prick","butt","tit",
							"squirt","scrotum","taint","bum","face","cunny","labia","bitch","clit","cum",
							"ball","sack","breast","meat","fuck","anus","sphincter","lip","shaft",
							"rack","prick","wang","milk","maiden","splooge","popper","sucker","crotch",
							"titty","milf","dick","lady","fudge","anal","wife","sex","cooch","gagging",
							"groping","coitus","pissing","shafting","man","cherry","cream","coochy",
							"hoar","sucking","anus","rimming"])
		SecNouns = WordList(["cocks","cunts","puss","boobs","sluts","twats","spunk","pricks","butts",
							"tits","titties","squirts","taints","fucker","bitch","clits","slits","cum",
							"balls","sacks","meat","fucks","sphincter","lips","shafts","rack","wangs",
							"milk","maidens","splooge","popper","sucker","crotch","sucker","milf","dicks",
							"thrust","eater","swallow","head","spreader","groper","licker","humper","sex",
							"bottom","cooch","rider","flower","girth","hymen","wood","boner","wood",
							"wood","rump","cream","cooter","hoar","nut","tongue","rimmer"])
		Adjs = WordList(["hard","wet","great","fat","pink","uber","fucker","good","thick","porn",
							"bound","bone","dinky","young","teen","spread","stiff","tight",
							"deep","black","dark","long","moist","gay","cuck","sex",
							"loose","sweet","steel","hard","dark","black","good","iron","harder"])
		Verbs = WordList(["fuck","bang","spunk","smash","piss","cum","grope","squeeze","spurt","rut","pound",
							"wank","milk","suck","splooge","bone","slap","thrust","rub","swallow","cuck",
							"hump","screw","schtup","bonk","jill","gag","wanna","nut","spank","suck"])
		
		sTweet = Prefix.GetWord() + " Castle "
		
		sWord1 = ""
		sWord2 = ""
		
		iRand = randint(1,5)
		if iRand == 1:
			sWord1 = FirstNouns.GetWord()
			sWord2 = Verbs.GetWord(NotList = [sWord1])
		elif iRand == 2:
			sWord1 = FirstNouns.GetWord()
			sWord2 = SecNouns.GetWord(NotList = [sWord1])
		elif iRand == 3:
			sWord1 = Adjs.GetWord()
			sWord2 = FirstNouns.GetWord(NotList = [sWord1])
		elif iRand == 4:
			sWord1 = Adjs.GetWord()
			sWord2 = SecNouns.GetWord(NotList = [sWord1])
		elif iRand == 5:
			sWord1 = Verbs.GetWord()
			sWord2 = "alot"
		elif iRand == 6:
			sWord1 = Adjs.GetWord()
			sWord2 = Verbs.GetWord(NotList = [sWord1])
		else:
			sWord1 = Verbs.GetWord()
			sWord2 = FirstNouns.GetWord(NotList = [sWord1])
			
		sTweet += self.WordCombiner(sWord1, sWord2).capitalize()
			
		return sTweet	
	
# The Buxom Irish Waitress
# Makes Love to a Pirate!	
class Generator108(Generator):
	ID = 108
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist', 'Bare-Shaven']
		Adjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		Man = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, bAllowGang = False, bAddArticle = False, bAllowRelate = False)
		
		sTweet = "The "
		if CoinFlip():
			sTweet += Adjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sTweet += Nations.GetWord(NotList = FemAdjNotList) + " "
		sTweet += Jobs.GetWord() + "\n"
		sTweet += WordList(["Makes Love to","Is Ravished by","Jumps into Bed with","Gets Bedded by","Spends the Night with",
							"Has a Wild Night of Passion with","Has a Forbidden Affair with","Is Claimed by"]).GetWord() + " " 
		sTweet += AddArticles(Man.Desc) + "!"

		return sTweet	
		
class Generator109(Generator):
	ID = 109
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "The " + sGirl + "\n"
		sTweet += "Does " + AddArticles(SexyAdjs.GetWord()) + " Strip-Tease"

		return sTweet	
		
class Generator110(Generator):
	ID = 110
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "The " + sGirl + "\n"
		sTweet += WordList(["Goes Down on","Bends Over for","Drops Her Panties for","Spreads her Cheeks for",
							"Does " + AddArticles(SexyAdjs.GetWord()) + " Strip-tease for", 
							"Gets Naked for","Blows","Gives a Handjob to","Lubes Herself Up for",
							"Flashes her Titties at","Flashes her Coochie at","Pulls Down her Top for",
							"Shaves Her Muff for"]).GetWord() + " " 
		sTweet += self.HisName
		if CoinFlip():
			sTweet += "\nand also " + NamesMale().FirstName() 
			
			if CoinFlip():
				sTweet += "\nAND " + NamesMale().FirstName() 
				
			sTweet += "!"

		return sTweet	
		
class Generator111(Generator):
	ID = 111
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "The " + sGirl + "\n"
		sTweet += "Tries " + WordList(["a Butt Plug","an Anal Hook","Leather Bondage","Lesbian Sex",
									   "Butt Stuff","Auto-erotic Asphyxiation","Choking Play",
									   "a Sex Swing","Scissoring","Tribbing","Deep Throat",
									   "a Glory Hole","a Swingers Party","Fisting","an Enema",
									   "Nude Wrestling","Bareback Sex","Doggy Style","Anal"]).GetWord() + "!"

		return sTweet	
		
class Generator112(Generator):
	ID = 112
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "My " + sGirl + "\n"
		sTweet += "Isn't Wearing Any Panties!"

		return sTweet	
		
class Generator113(Generator):
	ID = 113
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = AddArticles(sGirl) + "\n"
		sTweet += WordList(['Scissors','Eats Out','Fists','Finger Bangs','Goes Down On','Seduces',
							'Has ' + SexyAdjs.GetWord() + ' Lesbian Sex With']).GetWord(NotList = ['Sexy']) + " "
		sTweet += self.HerName 
			
		return sTweet	
		
class Generator114(Generator):
	ID = 114
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "My " + sGirl + "\n"
		sTweet += "Is Wearing " + WordList(['a Strap-On','a Latex Bodysuit','a Chainmail Bikini','a Thong',
											'a Micro Bikini','a Butt Plug','Nipple Clamps',
											'Crotchless Panties','Assless Chaps','a Ponytail Butt Plug',
											'a Ball Gag','a Sheer Bodystocking','a Fishnet Bodystocking',
											'a Chastity Belt','a Leather Bustier','Sexy Lingerie',
											'a Dog Collar','a Leash','a Seethru Bikini']).GetWord() + "!"

		return sTweet	
		
# The Perky Flight Attendant
# Plays Naked Football!
class Generator115(Generator):
	ID = 115
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()
		SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
		Man = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, bAllowGang = False, bAddArticle = False, bAllowRelate = False)
		
		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "The " + sGirl + "\n"
		sTweet += "Plays " + WordList(['Nude','Naked']).GetWord() + " " 
		sTweet += WordList(["Football","Volleyball","Volleyball","Basketball","Soccer","Golf","Frisbee",
							"Capture the Flag","Hide-and-Seek","Twister","Tennis","Polo","Rugby",
							"Curling","Lacrosse","Baseball","Quidditch","Roller Derby"]).GetWord() + "!"

		return sTweet	

# My Flirty Italian Milk Maid
# Is A Wanton Hotwife!
class Generator116(Generator):
	ID = 116
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist','Unshaven']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()

		sGirl = ""
		sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
		sTweet = "My " + sGirl + "\n"
		sTweet += "Is " + AddArticles(WordList(['Willing','Wanton','Open-Minded','Naughty','Adventurous',
												'Horny','Sexy','Lustful','Experienced','Excited',
												'Fertile','Shameless']).GetWord()) + " Hotwife!" 

		return sTweet	
		
# A Big-Titty German Waitress
# Urinates on Dick!
class Generator117(Generator):
	ID = 117
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjNotList = ['Naked','Nudist']
		FemAdjs = WordList(title.misc.AttitudeGoodFemale().List + title.misc.PhysCharFemale().List)
		Nations = WordList(['All-American','Asian','Brazillian','Columbian','Country','Czech',
							'Eastern European','French','German','Irish','Italian','Japanese',
							'Korean','Latina','Mexican','Russian','Small-Town','Swedish',
							'Spanish','Mid-Western'])
		Jobs = title.misc.ProfGoodFemale()

		sGirl = ""
		if CoinFlip():
			sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
		if CoinFlip():
			sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		if not sGirl:
			if CoinFlip():
				sGirl += FemAdjs.GetWord(NotList = FemAdjNotList) + " "
			else:
				sGirl += Nations.GetWord(NotList = FemAdjNotList) + " "
		sGirl += Jobs.GetWord()
		
	
		sTweet = AddArticles(sGirl) + "\n"
		sTweet += WordList(['Pees on','Fists','Paddles','Whips','Ties Up','Pegs','Uses a Steel Dildo on',
							'Uses a Riding Crop on','Takes a Shit on','Urinates on','Punishes',
							'Chokes']).GetWord() + " " 
		sTweet += self.HisName + "!"

		return sTweet	
	
# I Found Out I Was a Lesbian
# When an Oiled-Up Flight Attendant Ate My Ass 	
class Generator118(Generator):
	ID = 118
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		CharNotList = ['Uptight','Virgin','Male Model','Quarterback','Male Stripper','Camp Counselor','Business Man','Slave',
						'Defensive Lineman','Virtuous']
		Lesbian1 = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, NotList = CharNotList,
								bAllowMaritalStatus = False, bAllowSexuality = False, bAllowPregState = False, bAllowTitle = False)
		Lesbian2 = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 1, bAddArticle = False, bAddEndNoun = False, NotList = CharNotList,
								bAllowMaritalStatus = False, bAllowSexuality = False, bAllowPregState = False, bAllowProf = False, bAllowTitle = False)
		GirlJobs = title.misc.ProfFemale()
		GuyJobs = title.misc.ProfMale()
								
		sTweet = "I Found Out I Was a Lesbian When\n"
		if CoinFlip():
			sTweet += AddArticles(Lesbian1.Desc) + " " + GirlJobs.GetWord()
		else:
			sTweet += AddArticles(Lesbian2.Desc) + " Lady " + GuyJobs.GetWord()
		sTweet += "\n" + WordList(["Ate My Ass", "Ate Me Out", "Ate My Pussy", "Licked My Snatch", "Scissored Me",
								   "Rode My Face", "Rode Me With a Strap-On", "Fisted Me", "Fisted My Butt",
								   "Sucked My Tits", "Ate My Snatch", "Rimmed My Butthole",
								   "Sucked My Titties"]).GetWord()
								   
		return sTweet	
		
class Generator119(Generator):
	ID = 119
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlNotList = ['Single']
		Girl = FemaleChar(iNumMinCBits = 2, iNumMaxCBits = 3, bAddArticle = True, Type = GirlType.Good, NotList = GirlNotList,
							bAllowSexuality = False)
		
		sTweet = Girl.Desc + "\nGets An Enema"

		return sTweet	
		
class Generator120(Generator):
	ID = 120
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GuyNotList = ['Single']
		Guy = MaleChar(iNumMinCBits = 2, iNumMaxCBits = 3, bAddArticle = True, bAllowGang = False, NotList = GuyNotList,
						bAllowTrope = False, bAllowTitle = False, bAllowSpecies = False)
		
		sTweet = Guy.Desc + "\nGets An Enema"

		return sTweet	
		
# Massaging Mrs. Mountcox:
# A Sadistic Bisexual MILF Story
class Generator121(Generator):
	ID = 121
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Gerunds = WordList(['Blackmailing','Dominating','Enslaving','Fisting','Hot-Dogging','Licking',
							'Massaging','Milking','Mind Controlling','Motor-Boating','Motor-Boating',
							'Mounting','Paddling','Riding','Rimming','Sixty-nining','Showering With',
							'Showering With','Spanking','Stripping','Undressing','Videoing',
							'Whipping','Filling','Drilling','Pounding','Servicing','Satisfying',
							'Nailing','Caning','Humping'])
							
		MILFNotList = ['Virgin','Virginal','Maiden','Chaste','Sheltered','Sparkling','Straight','Spirited',
					   'Sweet','Virtuous','Anal Virgin','Angelic','Small-Town Girl','Tomboy','Lesbian',
					   'Little']
		MILF = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, NotList = MILFNotList,
							bAllowAge = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowProf = False,
							bAllowRelate = False, bAllowTitle = False, bAllowTrope = False, bAllowSpecies = False)
							
		sTweet = Gerunds.GetWord() + " Mrs. " + AuthorLastNames().GetWord() + ":\n"
		sTweet += AddArticles(MILF.Desc) + " MILF " + WordList(['Story','Encounter','Rendevous','Affair','Adventure']).GetWord()

		return sTweet	
		
# Speculum for the Horny Mexican MILF
class Generator122(Generator):
	ID = 122
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NaughtyStuff = WordList(['Anal Beads','Anal Hook','Ball Gag','Butt Plug','Clit Clamp','Clit Pump',
								 'Steel Dildo','12-inch Dildo','Double-Ended Dildo','Gimp Mask',
								 'Nipple Clamps','Pearl Necklace','Sex Swing','Spreader Bar','Speculum',
								 'Strap-On','Sybian','Anal Dildo','Anal Vibe','Butt Stuff','Fisting',
								 'Anal Fisting','Bondage Play','Dog Collar','Chastity Belt',
								 'Pony Play','Ponytail Anal Plug','Horse Whip','Gang Bang',
								 'Public Nudity'])
								 
		MILFNotList = ['Virgin','Virginal','Maiden','Chaste','Sheltered','Sparkling','Straight','Spirited',
					   'Sweet','Virtuous','Anal Virgin','Angelic','Small-Town Girl','Tomboy','Lesbian',
					   'Little']
		MILF = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, NotList = MILFNotList,
							bAllowAge = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowProf = False,
							bAllowRelate = False, bAllowTitle = False, bAllowTrope = False)
							
		sTweet = NaughtyStuff.GetWord() + " for the " + MILF.Desc + " MILF"

		return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# The Ghost of Richard Nixon
# Ploughed My Girlfriend 
class Generator124(Generator):
	ID = 124
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Undead = WordList(['Undead','The Ghost of','Zombie','Vampire','Werewolf'])
		Celebs = WordList(['Richard Nixon','JFK','Abraham Lincoln','Elvis Presley','Winston Churchill','Mahatma Gandhi',
							'Jim Morrison','Tupac','Buddy Holly','George Washington','Albert Einstein','Mao Zedong',
							'Humphrey Bogart','Babe Ruth','Colonel Sanders','Napoleon','Bela Lugosi','Groucho Marx',
							'Steve Jobs','Mr Rogers','Marlon Brando','Bing Crosby','Jimmy Stewart','Clark Gable',
							'James Dean','H.P. Lovecraft','Orson Welles','Henry Kissinger','Sonny Bono','Jimmy Hoffa',
							'Charlton Heston','Hugh Hefner','Yul Brynner','Carl Sagan','Yuri Gagarin','Jerry Lewis',
							'Benny Hill','Bob Ross','Joe DiMaggio','Don Knotts','Vincent Price','Adam West',
							'Frank Sinatra','Casey Kasem','Karl Marx','Jacques Cousteau','Salvador Dali'])
		Verbs = WordList(['Plowed','Banged','Porked','Drilled','Humped','Made Love to','Nailed','Reamed',
						  'Screwed','Shagged','Stuffed','Cream-pied','Ravished','Ate Out','Sixty-nined',
						  'Boned',])
		
		GirlNotList = ['Single','Mature Woman','Virgin','Unshaven','Maiden','Married','Recently-Divorced']
		Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, NotList = GirlNotList,
			bAllowProf = False, bAllowPregState = False, bAllowClothing = False, bAllowAttitude = False, bAllowSpecies = False,
			bAllowTitle = False, bAllowTrope = False, bAllowGenMod = False, bAllowSexuality = False, 
			bAllowMaritalStatus = False,)
		
		sTweet = Undead.GetWord() + " " + Celebs.GetWord() + " " + Verbs.GetWord() + " My " + Girl.Desc + " " + WordList(["Wife","Wife","Girlfriend"]).GetWord() + "!"					

		return sTweet	
		
class Generator125(Generator):
	ID = 125
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = title.misc.NiceGirl()
		
		Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
		
		sTweet = "The " + Girl.Desc + "\nGets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace","Cuddled"]) + " by " + Master.Desc
		
		return sTweet	
		
class Generator126(Generator):
	# Sitting On My Well-Hung Sumo-Wrestler Step-Dad's Face
	ID = 126
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 4, bAddArticle = True, bAllowGang = False, bAllowRelate = True)
	
		sTweet = WordList(["Sitting on","Riding","Straddling"]).GetWord() + " " + Master.Desc + "'s Face"
		
		return sTweet
		
# Isabelle Gets Naked for the Fully-Engorged Dinosaur S.W.A.T. Team
class Generator127(Generator):
	ID = 127
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Gang = MaleGangChar(iNumMinCBits = 2, iNumMaxCBits = 3)
		
		sTweet = self.HerName + " Gets Naked for the " + Gang.Desc 

		return sTweet	
		
# Pounded by the Alien Space Trucker Men
# on Uranus
class Generator128(Generator):
	ID = 128
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(['Boned','Bred','Claimed','Cream-Pied','Drilled','Fisted','Humped','Mounted',
						  'Nailed','Pleasured','Plowed','Porked','Ravished','Reamed','Punished',
						  'Rimmed','Spanked','Shagged','Shaved','Stuffed','Taken','Whipped','Licked',
						  'Pegged'])
		AlienPrefixes = WordList(['Alien','Space','Space Alien'])
		AlienNouns = WordList(['Body Builders','Bull Riders','Chippendales Dancers','Coal Miners',
								'Construction Workers','Cops','Cowboys','Defensive Linemen','Doctors',
								'Fire Fighters','Frat Boys','Long Haul Truckers','Lumberjacks',
								'Male Escorts','Male Models','Male Nurses','Male Strippers',
								'Matadors','Pirates','Roadies','Rodeo Clowns','Sailors','Stuntmen',
								'Sumo Wrestlers','Surfers','Surgeons','Biker Gang','DILFs','Jocks',
								'Billionaires','Millionaires','Sugar Daddies','Leather Daddies',
								'Bounty Hunters','Barbarians','Businessmen','Werewolves',
								'Drag Queens','Muscle Marys'])
		MaleNotList = ['Space']
		Alien1 = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = False, bAllowGang = False, NotList = MaleNotList,
			bAllowMaritalStatus = False, bAllowProf = False, bAllowTitle = False, bAllowTrope = False, bAllowNation = False)
		Alien2 = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddArticle = False, bAddEndNoun = True, bAllowGang = False, NotList = MaleNotList,
			bAllowMaritalStatus = False, bAllowProf = True, bAllowTitle = False, bAllowTrope = False, bAllowNation = False)
		
		sTweet = Verbs.GetWord() + " by the "
		if CoinFlip():
			sTweet += Alien1.Desc + " " + AlienPrefixes.GetWord() + " " + AlienNouns.GetWord() + " "
		else:
			sTweet += Alien2.Desc + " Space Men "
		sTweet += "on Uranus!"

		return sTweet	
		
class Generator129(Generator):
	ID = 129
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Race = WordList(['Black','Black','Black','White','White','Asian','Asian'])
		
		GirlNotList = ['Call-Girl','Escort','Slave','Whore']
		GirlAdj = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 1, bAddArticle = False, bAddEndNoun = False, NotList = GirlNotList,
			bAllowAge = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowNation = False, bAllowRelate = False,
			bAllowSexuality = False, bAllowSkinHairColor = False, bAllowSpecies = False, bAllowTitle = False, bAllowProf = False, 
			bAllowTrope = False)
		GirlNoun = WordList(title.misc.TitlesFemale().List + title.misc.TropesFemale().List + title.misc.ProfFemale().List)
		GirlSpecies = WordList(['Mermaid','Succubus','Futa','Undead','Zombie','Vampire','Fairy','Elf'])
		
		sHerRace = WordList(['Black','Black','Black','White','White','Asian','Asian','Latina','Latina']).GetWord()
		sHerSpecies = GirlSpecies.GetWord()
		
		ManNotList = ['Bob']
		Man = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 1, bAddArticle = False, bAllowGang = False, NotList = ManNotList,
					   bAllowAge = False, bAllowAttitude = False, bAllowGenMod = False, bAllowMaritalStatus = False,
					   bAllowPhysChar = False, bAllowDickChar = False, bAllowNation = False, bAllowSpecies = False,
					   bAllowSkinHairColor = False, bAllowRelate = False, bAllowTitle = False)
		ManSpecies = WordList(['Merman','Centaur','Minotaur','Zombie','Werewolf','Dwarf',
							   'Demon','Gargoyle','Were-Shark','Zombie','Goat Man'])

		ManRace = WordList(['Black','Black','Black','White','White','Asian','Asian','Latino','Latino'])
		sHisRace = ManRace.GetWord(NotList = [sHerRace])
		sHisSpecies = ManSpecies.GetWord(NotList = [sHerSpecies])
		
		while sHisRace == 'Latino' and sHerRace == 'Latina':
			sHisRace = ManRace.GetWord(NotList = [sHisRace])
							
		iRand = randint(1,3)
		if iRand == 1:
			print("<A>")
			sTweet = GirlAdj.Desc + " " + sHerRace + " " + GirlNoun.GetWord(NotList = GirlNotList) + " for the " + sHisRace + " " + Man.Desc
		elif iRand == 2:
			print("<B>")
			sTweet = GirlAdj.Desc + " " + sHerSpecies + " " + GirlNoun.GetWord(NotList = GirlNotList) + " for the " + sHisRace + " " + Man.Desc
		else:
			print("<C>")
			sTweet = sHerRace + " " + sHerSpecies + " " + GirlNoun.GetWord(NotList = GirlNotList) + " for the " + sHisRace + " " + Man.Desc

		return sTweet	
		
# Black Merman Quarterback for the White Playboy Centerfold
class Generator130(Generator):
	ID = 130
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GirlNotList = ['Call-Girl','Escort','Slave','Whore']
		GirlNoun = WordList(title.misc.TropesFemale().List + title.misc.ProfFemale().List)
		GirlSpecies = WordList(['Mermaid','Succubus','Futa','Undead','Zombie'])
		
		sHerRace = WordList(['Black','Black','Black','White','White','Asian','Asian','Latina','Latina']).GetWord()
		sHerSpecies = GirlSpecies.GetWord()
		
		ManNotList = ['Bob']
		ManAdj = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 1, bAddArticle = False, bAddEndNoun = False, bAllowGang = False, NotList = ManNotList,
					   bAllowAge = False, bAllowAttitude = True, bAllowGenMod = True, bAllowMaritalStatus = False,
					   bAllowPhysChar = True, bAllowDickChar = True, bAllowNation = False, bAllowSpecies = False,
					   bAllowSkinHairColor = False, bAllowRelate = False, bAllowProf = False, bAllowTrope = False,
					   bAllowTitle = False)
		ManNoun = WordList(title.misc.TropesMale().List + title.misc.ProfMale().List + title.misc.TitlesMale().List)
		ManSpecies = WordList(['Merman','Centaur','Minotaur','Zombie','Werewolf','Dwarf',
							   'Demon','Gargoyle','Were-Shark','Zombie','Goat Man'])
		ManRace = WordList(['Black','Black','Black','White','White','Asian','Asian','Latino','Latino'])
		sHisRace = ManRace.GetWord(NotList = [sHerRace])
		sHisSpecies = ManSpecies.GetWord(NotList = [sHerSpecies])
		while sHisRace == 'Latino' and sHerRace == 'Latina':
			sHisRace = ManRace.GetWord(NotList = [sHisRace])
		
		iRand = randint(1,3)
		if iRand == 1:
			print("<A>")
			sTweet = ManAdj.Desc + " " + sHisRace + " " + ManNoun.GetWord(NotList = ManNotList) + " for the " + sHerRace + " " + GirlNoun.GetWord(NotList = GirlNotList)
		elif iRand == 2:
			print("<B>")
			sTweet = ManAdj.Desc + " " + sHisSpecies + " " + ManNoun.GetWord(NotList = ManNotList) + " for the " + sHerRace + " " + GirlNoun.GetWord(NotList = GirlNotList)
		else:
			print("<C>")
			sTweet = sHisRace + " " + sHisSpecies + " " + ManNoun.GetWord(NotList = ManNotList) + " for the " + sHerRace + " " + GirlNoun.GetWord(NotList = GirlNotList)


		return sTweet	
		
# I watched my wife and an Italian cowboy dinosaur make a porno!
class Generator131(Generator):
	ID = 131
	Priority = 5
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		MaleNotList = ["Taboo"]
		FemRelative = WordList(["Sister", "Wife", "Bride", "Girlfriend", "Lesbian Bride", "Daughter", "Step-daughter",
								 "Mother-in-Law", "Mom", "Fiancé", "Young Wife", "New Bride", "Highschool Sweetheart",
								 "Teenage Daughter","Blushing Bride","Virgin Girlfriend","Conservative Girlfriend",
								 "Conservative Step-Mom", "Hot Sister", "Hot Step-Sister", "Gay Dad","Gay Step-Dad",
								 "Religious Step-Mom","Gay Husband","Gay Boyfriend","Uptight Wife", "Uptight Fiancé"]).GetWord()
			
		sTweet = "I Watched My " + FemRelative + "\n"
		
		if CoinFlip():
			MalePornStar = MaleChar(iNumMinCBits = 2, iNumMaxCBits = 3, bAddArticle = False, bAllowGang = False, NotList = MaleNotList,
				bAllowTitle = False, bAllowAttitude= False, bAllowMaritalStatus = False, bAllowProf = True, 
				bAllowTrope = True, bAllowNation = True)
			
			sTweet += "and " + AddArticles(MalePornStar.Desc) + "\n"
			sTweet += "Make a Porno"
		else:
			GangNotList = ["Taboo"]
			MaleGang = WordList(['Basketball Players','Bikers','Carnies','Chippendales Dancers','Coal Miners',
								 'Construction Workers','Cops','Cowboys','DILFs','Dwarves','Firemen',
								 'Gangstas','Goblins','Centaurs','Hockey Players','Rugby Players',
								 'Long Haul Truckers','Men at the Gym','Frat Brothers','Mer-men',
								 'Mountain Men','Navy Seals','Pirates','Pro Wrestlers','Roadies',
								 'Men of Seal Team Six','Scottsmen','Sumo Wrestlers','Vikings','Werewolves',
								 'Lawyers','Navy Boys','Bad Boys','Jocks','Surfers','Luchadors','Lumberjacks',
								 'Male Strippers','MMA Fighters','Rodeo Clowns','Dinosaurs','T-Rexes']).GetWord()
			GangNotList = GangNotList + [MaleGang]
			MaleGangAdjs = MaleGangChar(iNumMinCBits = 1, iNumMaxCBits = 2, bAddEndNoun = False, NotList = GangNotList, 
				bAllowAttitude= False, bAllowProf = True, bAllowTrope = False, bAllowNation = True)
			
			
			sNum = WordList(["Two","Two","Three","Three","Four", "Five","Seven", "Nine", "Ten","A Dozen", "17", 
							 "Two Dozen", "Hundreds of"]).GetWord()
			
			sTweet += "Make a Porno\n"
			if CoinFlip():
				sAdjs = MaleGangAdjs.Desc
				if not sAdjs == "":
					sTweet += "with " + sNum + " " + MaleGangAdjs.Desc + " " + MaleGang 
				else:
					sTweet += "with " + sNum + " " + MaleGang 
			else:
				sTweet += "with " + sNum + " " + MaleGang 
			
		
		
		return sTweet	
		
# In Love With
# My Dentist's 
# Magnificent Meat-Missile
class Generator132(Generator):
	ID = 132
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Guy = WordList(['Attorney','Blind Date','Body Guard','Boss','Camp Counselor','Captain','Coach','Date',
						'Doctor','Duke','Gym Coach','King','Marriage Counselor','Manor Lord','Mechanic',
						'Minister','New Boyfriend','Pastor','Personal Trainer','Plumber','Priest','Pool Boy',
						'Prince','Professor','Step-brother','Step-father','Step-son','Teacher',
						'Divorce Attorney','Yoga Teacher','Physical Therapist','Dentist']).GetWord()
		CockSizeAdj = WordList(['Engorged','Enormous','Gigantic','Titantic','Humongous','Massive','Regal','Giant',
								'Big Honking','Magnificent','Gargantuan','Jumbo','Super-Sized','Lengthy','Turgid',
								'Pulsating','Throbbing','Rock-hard','Towering','Turgid','Tumescent','Girthy',
								'Donkey-Sized','Horse-Sized','King-Sized','Tumescent','XL','Arm-length',
								'Black','Big Black','Enormous Fucking','8-inch','10-inch','12-inch',
								'Handsome','Beautiful','Glistening']).GetWord()
		Cock = WordList(['Beef Bayonette','Boner','Cock','Cocksickle','Dick','Erection','Hard-on','Joystick','Knob',
						 'Meat','Meat-Missile','Member','Package','Penis','Phallus','Sausage','Schlong','Shaft',
						 'Tool','Trouser Snake','Disco Stick','Prick','Banana']).GetWord(NotList = [CockSizeAdj])
		BallSizeAdj = WordList(['Enormous','Gigantic','Grapefruit-Sized','Huge','Humungous','Jumbo',
								'Low-hanging','Massive','Pendulous','Swollen','Heavy','XL','XXL',
								'Swaying','Hairy']).GetWord()
		Balls = WordList(['Balls','Ballsack','Nuts','Scrotum','Silk Purse','Testicles']).GetWord(NotList = [BallSizeAdj])
							
		sTweet = WordList(["In Love With","Falling For","Head-Over-Heels For","Captivated By",
						   "Bewitched By","Entranced By","Enraptured By","Spellbound By",
						   "Enchanted By","Charmed By","Surprised By","Dazzled By","Flustered By",
						   "Shook By","Overcome By","Astonished By","Breathless From",
						   "Hypnotized By","Delighted By","Beguiled By","Transfixed By",
						   "Seduced By","Ensorcelled By","Gaga About","Infatuated With",
						   "Enamoured By","Swept Away By","Transfixed By"]).GetWord()
						   
		sTweet += "\nMy " + Guy + "'s\n"
		
		iRand = randint(1,3)
		if iRand == 1:
			sTweet += BallSizeAdj + " " + Balls
		else:
			sTweet += CockSizeAdj + " " + Cock

		return sTweet	
		
# Forbidden Heat
# A pseudo-incest gorilla double anal story
class Generator133(Generator):
	ID = 133
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sTitle1 = WordList(['Forbidden','Taboo','Lustful','Secret','Dirty','Naked','Sinful','Wicked',
							'Dangerous','Indecent','Twisted','Throbbing','Hard','Untamed',
							'Sexual','Steamy','Naked','Bound',
							'Passionate','Devil\'s','Lesbian','Sizzling','Caged','Desperate',
							'Cocky','Scandalous','Professional','Submissive'
						  ]).GetWord()
		sTitle2 = WordList(['Desire','Heat','Secret','Virgin','Sins','Pleasures','Temptation','Cowboy',
							'Lust','Release','Danger','Rendevous','Obsession','Persuasion','Embrace',
							'Kiss','Lovers','Passion','Daddy','Bachelor','Shame','Scoundrel',
							'Seduction','Surrender','Angel','Bad Boy','Possession','Climax',
							'Beauty','Touch','Gentleman','Princess','Flower',
							'Diaries','Lies','Fire','Desperado','Liason','Tease',
							'Secretary','Fantasy','Outlaw'
						  ]).GetWord(NotList = [sTitle1])
						  
		sSubTitle1 = WordList(['Non-Consensual','Interracial','Pseudo-Incest','Dominant','Submissive',
							   'Twincest','Cuckold','BDSM','Lesbian','Exhibitionist','Trans','Anal']).GetWord(NotList = [sTitle1,sTitle2])
		sSubTitle2 = WordList(["Unicorn", "Centaur", "Werewolf", "Mermaid", "Merman", "Mer-MILF", "Dragon", "Orc", "Goat-Man", 
								"Dwarf", "Futanari", "Space Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-Horse", 
								"Gorilla", "Dinosaur", "Dinosaur", "Velociraptor", "Zombie", "Bodybuilder","Martian",
								"Troll","Goblin","Vampire","Step-Dad","Dwarf","Housewife","Cheerleader","Hotwife",
								"Lumberjack","Biker","Viking","Gargoyle","Construction Worker","Cowboy","Fireman",
								"Pro-Wrestler","Priest","Luchador","Furry","Japanese Schoolgirl","Teacher","Viking",
								"Nun"]).GetWord(NotList = [sTitle1,sTitle2,sSubTitle1])
		sSubTitle3 = WordList(["Anal", "Double Anal", "Nipple Play", "Fisting", "Incest", "Twincest", "Threesome", 
							   "Foursome", "Fivesome", "Bukkake", "Feminization", "Paddling", "Rope Play", 
							   "Water-Sports", "Wife Swapping", "Sixty-Nine", "Erotic Asphyxiation", "Orgy", "Gangbang", 
							   "Reverse Gangbang", "Milking", "Double Penetration", "Triple Penetration", 
							   "Pee-Drinking", "Dirty Sanchez", "Sodomy", "Age Play", "BDSM", "Fisting","Toe Sucking",
							   "Anal Fisting", "Fem-dom","Tea-Bagging","Spanking","Lactation","Cuckolding",
							   "Cuck-Queaning","Enema","Rimming", "Leather Bondage","Public Humiliation","Cum-Drinking",
							   "Fellatio","Choking","Glory Hole","Cum-Swapping","Analingus","Ass-Eating","Ass-to-Ass",
							   "Menage","Lactation","Frottage"
							   ]).GetWord(NotList = [sTitle1,sTitle2,sSubTitle1,sSubTitle2])

		sTweet = "~" + sTitle1.upper() + " " + sTitle2.upper() + "~\n\n"
		sTweet += AddArticles(sSubTitle1).lower() + " " + sSubTitle2.lower() + " " + sSubTitle3.lower() + " story"
		
		return sTweet	
		
# Taken by her Lesbian Centaur Boss
class Generator134(Generator):
	ID = 134
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		VerbNot = ['Impregnated','Bred','Hunted']
		sVerb = self.VerbsBy.GetWord(NotList = VerbNot)

		sTweet = sVerb + " by "
		if CoinFlip():
		#gay male
			Orientation = WordList(['Gay','Gay','Androgynous','Bisexual','Transgender','Otherkin',
									'Gender-fluid','Gender-queer','Non-Binary','Pansexual','Polysexual'])
			Species = WordList(['Alien','Alpha Wolf','Centaur','Centaur','Cyborg','Demon',
								'Dinosaur','Dinosaur','Dwarf','Gargoyle','Goat-Man',
								'Man-o-taur','MANtelope','MANticore','Mer-man','Mer-man',
								'Swamp Creature','Tentacle Monster','Undead',
								'Vampire','Vampire','Were-Horse','Were-Shark','Werewolf',
								'Werewolf','Zombie','Chippendales Dancer','Coal Miner',
								'Construction Worker','Cop','Cowboy','Farm Hand',
								'Football Players','Frat Boy','Gangsta','Long Haul Trucker',
								'Lumberjack','MMA Fighter','Sailor','Sumo Wrestler',
								'Millionaire','Billionaire'])
			Relations = WordList(['Blind Date','Body Guard','Boss','Camp Counselor','Coach',
						'Doctor','Duke','Gym Coach','Marriage Counselor','Manor Lord','Mechanic',
						'Minister','New Boyfriend','Pastor','Personal Trainer','Plumber','Priest','Pool Boy',
						'Prince','Professor','Step-brother','Step-father','Step-son','Teacher',
						'Divorce Attorney','Yoga Teacher','Physical Therapist','Dentist','Youth Pastor',
						'Principal'
						])
			sTweet += "his " + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
		else:
		#lesbian female
			Orientation = WordList(['Lesbian','Lesbian','Dyke','Androgynous','Bisexual','Transgender','Otherkin',
									'Gender-fluid','Gender-queer','Non-Binary','Pansexual','Polysexual'])
			Species = WordList(['Elf','Fairy','Futa','Futanari','Green-Skinned Alien',
								'Mermaid','Mermaid','Mermaid','Nymph','Succubus','Succubus',
								'Vampire','Cougar','MILF','Step-Daughter',
								'Zombie'])
			Relations = WordList(['Teacher','English Teacher','Yoga Instructor','Nanny','Math Tutor',
								  'Babysitter','Nurse','Piano Teacher','Biology Teacher','Personal Trainer',
								  'Housekeeper','French Maid','Secretary','Therapist',
								  'Gym Coach','Volleyball Coach','Nun','Nurse','Massage Therapist',
								  'Cheerleading Captain','Secretary','Fashion Model',
								  'Stripper','Step-Mom','Mother-in-Law','Principal','Waitress',
								  'Manager'])
			sTweet += "her " + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
		return sTweet	
		
# MILKED by my biker step-son
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
	
#Ass Eating 101:
# My date with the principal
class Generator136(Generator):
	ID = 136
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		LastNames = WordList(['Beaver',
							  'Bell',
							  'Bottoms',
							  'Brown',
							  'Butts',
							  'Chang',
							  'Church',
							  'Clark',
							  'Cox',
							  'Cummings',
							  'Davis',
							  'Devlyn',
							  'Goodbody',
							  'Gray',
							  'Green',
							  'Hancock',
							  'Hill',
							  'Jefferson',
							  'Johnson',
							  'Jones',
							  'King',
							  'Lee',
							  'Long',
							  'Lopez',
							  'Moore',
							  'Moorecox',
							  'Muncher',
							  'Peach',
							  'Pearl',
							  'Peckwood',
							  'Peters',
							  'Philmore',
							  'Popper',
							  'Robinson',
							  'Rogers',
							  'Ross',
							  'Sanderson',
							  'Smith',
							  'St. Claire',
							  'Taylor',
							  'Wang',
							  'White',
							  'Williams',
							  'Wilson',
							  'Woody'
							])
		
		SexActs = WordList(['Analingus',
							'Anal Creampie',
							'Anal Fisting',
							'Anal Insertion',
							'Anal Sex',
						    'Ass Eating',
							'Breast Play',
							'Cum Swapping',
							'Deep Throating',
							'Doggy Style',
							'Double Penetration',
							'Face-Sitting',
							'Fingering',
							'Forced Orgasm',
							'Giving Head',
							'Glory Holes',
							'Hand-jobs',
							'Hot-Dogging',
							'Ménage à Trois',
							'Motor-boating',
							'Muff-Diving',
							'Reverse Cowgirl',
							'Rimming',
							'Road Head',
							'Sixty-Nining',
							'Sodomy',
							'Strap-Ons',
							'Threesomes',
							'Tribbing'
						  ])

		ElderJobs = WordList(["Algebra Teacher",
							 "Anatomy Professor",
							 "Anatomy Teacher",
							 "Biology Professor",
							 "Biology Teacher",
							 "Criminal Law Professor",
							 "French Teacher",
							 "Guidance Counselor",
							 "Gym Coach",
							 "History Teacher",
							 "Lit Professor",
							 "Math Teacher",
							 "Music Teacher",
							 "Personal Tutor",
							 "Principal",
							 "Professor",
							 "Sex-Ed Teacher",
							 "Spanish Teacher",
							 "Women's Studies Professor"
						   ])
		
		sTweet = SexActs.GetWord() + " 101:\n"
		sTweet += "My Date With "
		
		Dates = []
		Dates.append("My " + ElderJobs.GetWord())
		Dates.append("Mr. " + LastNames.GetWord() + ", My " + ElderJobs.GetWord(NotList = ['Professor']) + ")")
		Dates.append("Ms. " + LastNames.GetWord() + ", My " + ElderJobs.GetWord(NotList = ['Professor']))
		
		sTweet += Dates[randint(0,len(Dates) - 1)]

		return sTweet	
		
# Taken in the Graveyard by the Strapping Truck-Driver Zombie 
class Generator137(Generator):
	ID = 137
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(["Bedded",
			"Boned",
			"Claimed", "Claimed",
			"Deflowered",
			"Mounted",
			"Pleasured",
			"Ravished",
			"Taken","Taken","Taken"])
			
		Adverbs = WordList(["Hard","Hard",
			"Forcefully",
			"Passionately",
			"Roughly",
			"Ruthlessly",
			"Vigorously","Vigorously"])
			
		sVerbPhrase = Verbs.GetWord()
		if CoinFlip():
			sVerbPhrase += " " + Adverbs.GetWord()
			
		Places = WordList(['in the Graveyard','in the Graveyard','in the Mausoleum',
						   'in the Sepulcher','in the Morgue','in the Mortuary',
						   'in the Haunted House','at the Tomb','in a Casket',
						   'in a Coffin'])
			
		MaleNotList = ['copper']
		Man = MaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, bAddArticle = False, bAddEndNoun = False, bAllowGang = False, NotList = MaleNotList,
				bAllowTitle = True, bAllowAttitude= False, bAllowMaritalStatus = False, bAllowProf = False, 
				bAllowTrope = True, bAllowNation = False, bAllowSpecies = False, bAllowAge = False)
				
		ManNouns = WordList(['Ghost','Zombie','Vampire','Werewolf','Ghoul','Skeleton','Mummy','Corpse',
							 'Serial Killer'])
							 
		sTweet = sVerbPhrase + "\n" + Places.GetWord() + " by the\n" + Man.Desc + " " + ManNouns.GetWord()

		return sTweet	
		
#I Was Scissored by a Witch, and I Liked It!
class Generator138(Generator):
	ID = 138
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Verbs = WordList(["Ravished","Fingered","Milked","Scissored","Fisted",
						  "Kissed","Eaten Out","Sixty-Nined","Finger-Banged",
						  "French Kissed","Taken with a Broomstick",
						  "Penetrated with a Broomstick",
						  "Defiled with a Broomstick",
						  "Ravished with a Broomstick"])
			
		if CoinFlip():
			NotFemList = ['anal','tease','virgin','fertile','small-town','tender','revealing','mature woman']
			Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = False, bAddEndNoun = False, NotList = NotFemList,
								bAllowSexuality = False, bAllowMaritalStatus = False, bAllowProf = False, bAllowTitle = False,
								bAllowGenMod = False)
								
			sTweet = "I Was " + Verbs.GetWord() + " by " + AddArticles(Girl.Desc) + " Witch, And I Liked It!"
								
		else:
			NotFemList = ['anal','devlish','tease','virgin','fertile','small-town','submissive','tender','masseuse','mature','little']
			Girl = FemaleChar(iNumMinCBits = 1, iNumMaxCBits = 2, Type = GirlType.Bad, bAddEndNoun = True, NotList = NotFemList,
								bAllowSexuality = False, bAllowMaritalStatus = False, bAllowAttitude = False, 
								bAllowGenMod = False, bAllowSpecies = False, bAllowTitle = False)
			
			sTweet = "I Was " + Verbs.GetWord() + " by an Undead " + Girl.Desc + ", And I Liked It!"

		return sTweet	
	
# My Innocent Sheltered Step-Mom 
# Wore a Butt Plug
# To Church	
class Generator139(Generator):
	ID = 139
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NiceGirlAdjs = WordList(['Amish','Chaste','Christian','Conservative','Innocent','Modest',
								 'Mormon','Sheltered','Shy','Small-Town','Uptight','Wholesome'])
		PhysAdjs = WordList(['Busty','Bubble-Butt','Curvy','Bikini-Bod','Stacked','Slender',
							 'Full-Bodied','Large Breasted','Round-Bottomed','Petite',
							 'Statuesque','Fat-Bottomed'])
		NiceGirlNouns = WordList(['Housewife','Nanny','Step-Mother','Secretary','Step-Daughter',
								  'Step-Sister','Yoga Instructor','Girlfriend','Fiancé','Wife',
								  'Mom','Sister','Sister-in-Law','Babysitter'])
	
								
		KinkNouns = WordList(['Wore Anal Beads','Wore an Anal Hook','Wore a Ball Gag',
								'Wore a Butt Plug','Went Commando','Wore a Clit Clamp',
								'Wore a Clit Pump','Wore Crotchless Panties','Wore a Chastity Belt',
								'Wore Nipple Clamps','Wore a Remote Controlled Vibrator',
								'Wore a Rubber Fetish Suit','Wore a Speculum','Wore a Strap-On',
								'Wore a Cupless Bra','Went Topless','Went Nude',
								'Wore a See-Thru Dress','Wore a Dog Collar','Wore Nothing But High Heels',
								'Went Stark Naked','Wore Nipple Pasties',
								'Wore a Skirt With No Panties'])
								
		sTweet = "My " + NiceGirlAdjs.GetWord() + " "
		if randint(1,3) == 3:
			sTweet += PhysAdjs.GetWord() + " "
		sTweet += NiceGirlNouns.GetWord() + "\n"
		sTweet += KinkNouns.GetWord() + "\n" 
		sTweet += WordList(["To Church","To Church","To the Office","To Class","To the Grocery Store",
							"To the Gym","To Sunday School","To Our Yoga Class"]).GetWord()

		return sTweet	
		
# I Sucked On My Mother-in-Law's Massive Mammaries 
class Generator140(Generator):
	ID = 140
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemRelations = WordList(['Mother-in-Law','Sister-in-Law','Daughter-in-Law','Step-Mom',
								 'Friend\'s Mom','English Teacher','Babysitter','Boss',
								 'Boss\'s Wife','Mom','Teacher','Secretary','Best Friend'])

		TitsAdjB = WordList(['Bare','Big','Boobalicious','Bouncing','Bountiful'])
		TitsAdjC = WordList(['Collossal','Creamy'])
		TitsAdjD = WordList(['Delicious','Double-D'])
		TitsAdjF = WordList(['Firm','Fulsome'])
		TitsAdjG = WordList(['Gargantuan','Gigantic','Generous'])
		TitsAdjH = WordList(['Heaving','Heavy','Huge'])
		TitsAdjJ = WordList(['Giant','Gigantic','Generous','Jiggling','Juicy','Jumbo'])
		TitsAdjK = WordList(['Nubile','Nibble-able','Naughty'])
		TitsAdjL = WordList(['Lickable','Lovely','Luscious'])
		TitsAdjM = WordList(['Magnificent','Massive'])
		TitsAdjN = WordList(['Nubile','Nibble-able','Naughty','Nude'])
		TitsAdjP = WordList(['Plush','Plump','Pendulous','Perky'])
		TitsAdjR = WordList(['Ripe','Robust','Round'])
		TitsAdjSw = WordList(['Sweet','Swollen','Sumptuous','Succulent','Supple'])
		TitsAdjT = WordList(['Tasty','Titanic','Tender','Tremendous'])
							
		TitsNouns = WordList(['Bangers','Bazooms','Boobies','Boobs','Bosoms','Breasts','Cantaloups','Coconuts','Dumplings','Gazongas',
							  'Globes','Hams','Hooters','Honkers','Jugs','Knockers','Love Balloons',
							  'Mammaries','Meat Melons','Melons','Pillows','Puppies','Rack',
							  'Sweater-Puppies','Sweater-Zeppelins','Tatas','Tits','Titties'])
							  
		sTitsNoun = TitsNouns.GetWord()
		sTitsAdj = ""
		if sTitsNoun[0].lower() == 'b':
			sTitsAdj = TitsAdjB.GetWord()
			
			
		elif sTitsNoun[0].lower() == 'c':
			sTitsAdj = TitsAdjC.GetWord()
			
		elif sTitsNoun[0].lower() == 'd':
			sTitsAdj = TitsAdjD.GetWord()
			
		elif sTitsNoun[0].lower() == 'g':
			sTitsAdj = TitsAdjG.GetWord()
			
		elif sTitsNoun[0].lower() == 'h':
			sTitsAdj = TitsAdjH.GetWord()
			
		elif sTitsNoun[0].lower() == 'j':
			sTitsAdj = TitsAdjJ.GetWord()
			
		elif sTitsNoun[0].lower() == 'k':
			sTitsAdj = TitsAdjK.GetWord()
			
		elif sTitsNoun[0].lower() == 'm':
			sTitsAdj = TitsAdjM.GetWord()
			
		elif sTitsNoun[0].lower() == 'n':
			sTitsAdj = TitsAdjN.GetWord()
			
		elif sTitsNoun[0].lower() == 'p':
			sTitsAdj = TitsAdjP.GetWord()
		
		elif sTitsNoun[0].lower() == 'r':
			sTitsAdj = TitsAdjR.GetWord()
			
		elif sTitsNoun[0:2].lower() == 'sw':
			sTitsAdj = TitsAdjSw.GetWord()
			
		else: 
			sTitsAdj = TitsAdjT.GetWord()
		
							  
		sTweet += "I " + WordList(['Motor-boated','Played with','Sucked on','Sucked','Milked',
									'Fooled Around With']).GetWord() + " My "
		sTweet += FemRelations.GetWord() + "'s " + sTitsAdj + " " + sTitsNoun 

		return sTweet	
		
class Generator141(Generator):
	ID = 141
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ForbiddenFems = WordList(["Mom","Step-Mom","Step-Sister","Mother-in-Law","Aunt","Sister-in-Law",
								  "Daughter","Step-Daughter","Teacher","Secretary","Maid","Nurse",
								  "Twin Sister","Co-ed Student"])
		BodyParts = WordList(["Ass","Ass","Ass","Thighs","Thighs","Boobs","Tits","Melons","Knockers","Hips","Nipples","Nips",
							  "Coconuts","Titties","Jugs","Sweater-Puppies","Sweater-Zeppelins","Buns",
							  "Booty","Tush","Buttocks","Behind"])
		Adjs = WordList(["Thick","Chubby","Juicy","Ample","Fat","Jiggling","Generous","Ripe",
						 "Voluptuous","Wide","Shapely","Smooth","Phat","Enormous","Rippling",
						 "Big","Chunky","Large","Curvy","Milky","Quivering"])
		sTweet += "Hypnotized by her " + ForbiddenFems.GetWord() + "'s\n"
		sTweet += Adjs.GetWord() + " "
		sTweet += "Lesbian " + BodyParts.GetWord()

		return sTweet	
		
class Generator999(Generator):
	ID = 999
	Priority = 0
	Type = GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		iNum = 0
		
		if iNum != 0:
		
			sTweet += "Female: " + GetInnName(Gender.Female,iNum)
			sTweet += "\n"
			sTweet += "Male: " + GetInnName(Gender.Male,iNum)
		else:
			sTweet += "Female: " + GetInnName(Gender.Female)
			sTweet += "\n"
			sTweet += "Male: " + GetInnName(Gender.Male)

		return sTweet	
		
class Generator1000(Generator):
	ID = 1000
	Priority = 0
	Type = GeneratorType.Test
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		FemAdjList = titmisc.AgeFemaleNoun().List + titmisc.AgeFemaleAdj().List + titmisc.AttitudeFemale().List + titmisc.ClothingFemale().List + titmisc.GenModFemale().List + titmisc.MaritalStatusFemale().List + titmisc.NationFemale().List + titmisc.PhysCharFemale().List + titmisc.PregState().List + titmisc.SexualityFemale().List + titmisc.SkinHairColorFemale().List
		FemNounList = titmisc.ProfFemale().List + titmisc.RelateFemale().List + titmisc.SpeciesFemale().List + titmisc.TropesFemale().List
		#List1 = titmisc.SpeciesFemale().List

		#List2 = sorted(List1)
		
		# List1 = ["strict","stuffy","surly","pseudonymous"]
		# List2 = ["buddy","stranger","psycho"]
		
		aFemResult = GetRhymingPair(FemAdjList,FemNounList)
		sTweet = "Female: " + aFemResult[0] + " " + aFemResult[1] + "\n"
		
		ManAdjList = titmisc.AgeMaleAdj().List + titmisc.AttitudeMale().List + titmisc.GenModMale().List + titmisc.MaritalStatusMale().List + titmisc.NationMale().List + titmisc.PhysCharMale().List + titmisc.DickCharMale().List + titmisc.SkinHairColorMale() .List
		ManNounList = titmisc.ProfMale().List + titmisc.RelateMale().List + titmisc.SpeciesMale().List + titmisc.TitlesMale().List + titmisc.TropesMale().List + titmisc.TropesMale().List 
		
		aManResult = GetRhymingPair(ManAdjList,ManNounList)
		sTweet += "Male: " + aManResult[0] + " " + aManResult[1] + "\n"
		# sNoun = NounList[randint(0,len(NounList) - 1)]
		# sAdj = GetRhymingWord(word = sNoun, list = AdjList)
		
		# if sAdj:
			# sTweet = "Rhyming phrase: [" + sAdj + " " + sNoun + "]"
		# else:
			# sTweet = "No rhyme found for " + sNoun 

		return sTweet	
		
class Generator1001(Generator):
	ID = 1001
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		#print("Generator1001.GenerateTweet() started")
		Girl = char.FemaleChar(TempType = TempType.Flowery, bAddTheArticle = False, bAllowTrope = True, SelectTemplateID = 14)
		Guy = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = False, bAllowTrope = True, bAllowRelate = True, bAllowAge = False, bAllowMaritalStatus = False, bAddEndNoun = False)
		
		
		
		#print("Generator1001.GenerateTweet() FemaleChar created, building tweet")
		sTweet += Girl.Desc + " Gets Sexed the Hell Up!\n"
		sTweet += Guy.Desc + " Takes My Wife Hard From Behind!\n"

		return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator100(Generator):
	# ID = 100
	# Priority = 2
	
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
			AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(GeneratorType.Promo)
			
		#print("RandomGenerator() Allowed types: " + str(AllowedTypes))
		if len(self.GeneratorList) > 0:

			Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
			while not Generator.Type in AllowedTypes:
				Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
				
		return Generator 
		
	def GetGeneratorsSequential(self, bAllowPromo = True, Type = None):
		GeneratorList = []
		AllowedTypes = []
		
		if not Type is None:
			AllowedTypes = [Type] 
		else:
			AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
		
		if bAllowPromo:
			AllowedTypes.append(GeneratorType.Promo)

		for subclass in Generator.__subclasses__():
			gen = subclass()

			if gen.Type in AllowedTypes:
				GeneratorList.append(gen)
			
		return GeneratorList  
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		