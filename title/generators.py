#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from title.util import *
from title.misc import *
from title.names import *
from title.people import *
from title.texttoimg import *

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
		#self.Girls = BookGirls()
		#self.GirlsBasic = BookGirlsBasic()
		#self.GirlAdjs = BookGirlAdjs()
		#self.GirlCompAdjs = BookGirlCompAdjs()
		#self.Masters = BookMasters()
		#self.MastersBasic = BookMastersBasic()
		#self.MasterGangs = BookMasterGangs()
		#self.MasterAdjs = BookMasterAdjs()
		#self.MasterCompAdjs = BookMasterCompAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()
		self.Gerunds = BookGerunds()
		self.HerName = NamesFemale().FirstName()
		self.HisName = NamesMale().FirstName()
		self.SubtitleCoda = SubtitleCoda()
		
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
		sTweet = title.util.GetNextFavTitleFromFile()
		
	if sTweet == "":
		Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = True)
		# print("Generator ID: " + str(Gen.ID))
		while bTweet and not TweetHistoryQ.PushToHistoryQ(Gen.ID):
			print("Generator ID " + str(Gen.ID) + " already in Q")
			Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = True)
			print("New generator ID: " + str(Gen.ID))
	
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
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
	
		sTweet = self.VerbsBy.GetWord() + " By\n" + Master.Desc
		
		return sTweet
		
class Generator2(Generator):
	# Veonica Gets Blackmailed by the Billionaire Mountain Man 
	ID = 2
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace"]) + " by\n" + Master.Desc
		
		return sTweet

class Generator3(Generator):
	# Married to the Alpha Wolf
	ID = 3
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "My")
			
		sTweet = self.VerbsTo.GetWord() + " To " + Master.Desc
		# if CoinFlip():
			# sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "An Erotic"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator4(Generator):
	# Veronica Gets Married to the Alpha Wolf	
	ID = 4
	Priority = 2
	
	Master = MaleChar()
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her")
		
		sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
		
		return sTweet
		
class Generator5(Generator):
	# The President's Amish Milkmaid
	ID = 5
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ['BDSM'])
		Master = MaleChar(iNumMaxCBits = 2, NotList = ['BDSM'], bAllowGang = False)
			
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
		
		NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", "Gifted", "Pledged", "Bed", "Sex Dungeon"]
		
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = NotList, bAddArticle = True)
		
		if CoinFlip():
			sTweet = self.VerbsTo.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		else:
			sTweet = self.VerbsBy.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
		
		return sTweet
		
class Generator7(Generator):
	# The Virgin, The Werewolf, and The Billionaire Manticore: A Hot Menage	
	
	ID = 7
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master1 = MaleChar(iNumMaxCBits = 2, bAllowGang = False)
		Master2 = MaleChar(iNumMaxCBits = 3, bAddArticle = True)
		Girl = FemaleChar(iNumMaxCBits = 2)
		sTweet = "The " + Girl.Desc + ",\nThe " + Master1.Desc + ",\n& " + Master2.Desc + ":\n"
		if CoinFlip():
			sTweet += "A Hot Ménage"
		else:
			sTweet += "A " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet

class Generator8(Generator):
	# My Boyfriend is a Secret Daddy Dom 
	ID = 8
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single"])
		sTweet = "My " + WordList(["Boyfriend", "Hot Date", "Fiancé", "Blind Date", "Kidnapper"]).GetWord() + " is a\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + AddArticles(Girl.Desc) + " " + self.SubtitleCoda.GetWord()
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
		
		Girl = FemaleChar(iNumMaxCBits = 2, NotList = ["BDSM"], bAllowRelate = True)
		Master = MaleChar(iNumMaxCBits = 2, NotList = ["BDSM"], bAllowRelate = True)
		
		sTweet = "The " + Girl.Desc + "\nand\nThe " + Master.Desc 
		sTweet += ":\nA " + WordList([self._getFMs_(), "BDSM", title.misc.SexyAdjs().GetWord().capitalize()]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator10(Generator):
	# Baby for the Stay-at-Home Manticore
	ID = 10
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, bAllowRelate = True)

		sTweet = "Baby For " + Master.Desc

		return sTweet
		
class Generator11(Generator):
	# The Millionaire Sherrif's Virgin
	ID = 11
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, bAllowRelate = True)
		Master = MaleChar(iNumMaxCBits = 2)
		
		sTweet = "The " + Master.Desc + "'s\n" + Girl.Desc

		return sTweet
		
class Generator12(Generator):
	# Babysitter to the Billionaire Uniporn
	ID = 12
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		sTweet = Girl.Desc + "\nto\n" + Master.Desc
		
		return sTweet
		
class Generator13(Generator):	
	# Babysitter for the Billionaire Uniporn
	ID = 13
	Priority = 3
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Master = MaleChar(iNumMaxCBits = 2, bAddArticle = True)
		
		sTweet = Girl.Desc + "\nfor\n" + Master.Desc
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(),"A BDSM","A Forbidden"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
	
class Generator14(Generator):
	# The Virgin Call-Girl's Gang Bang
	ID = 14
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirl1 = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowSexuality = False)
		GoodGirl2 = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAllowClothing = False, bAllowSexuality = False, bAllowTitle = False)
		BadGirl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = True)
		MasterGang = MaleGangChar(iNumMaxCBits = 3, NotList = ["Gang-Bang"])
		
		Tweets = []

		Tweets.append(GoodGirl1.Desc + "'s\nGang Bang:\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord())
		Tweets.append(BadGirl.Desc + "'s\n" + title.misc.SexyAdjs().GetWord().capitalize() + " Gang Bang:\nA " + self._getFMs_() + " " + self.SubtitleCoda.GetWord())
		Tweets.append("Gang-Banged By\nThe " + MasterGang.Desc + ":\nA " + GoodGirl2.Desc + " " + self.SubtitleCoda.GetWord())
		Tweets.append("Shared By\nThe " + MasterGang.Desc + ":\nA " + GoodGirl2.Desc + " " + self.SubtitleCoda.GetWord())
		
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
		
class Generator16(Generator):
	# The Small-Town Virgin's First Time
		
	ID = 16
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["MILF", "Concubine", "Wife", "Pregnant", "Mom", "Sex", "Divorced", "Virgin"], bAddArticle = True, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False)

		sTweet = Girl.Desc + " " + WordList(["Virgin", "Virgin", "Virgin", "Anal Virgin"]).GetWord() + "'s\nFirst Time"
		if CoinFlip():
			sTweet += ":\n" + WordList(["A " + self._getFMs_(), "A BDSM", "A Secret", "An S&M", "A Rough Sex", "An Anal", "A Gang-Bang"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator17(Generator):
	# Enslaved: The Ebony Older Woman & The Mountain Man Biker Gang 
	ID = 17
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Subtitles = []
		
		Master = MaleChar(iNumMaxCBits = 2)
		Gang = MaleGangChar(iNumMaxCBits = 3)
		
		sTweet = self.VerbsBy.GetWord() + ":\n"
		
		Girl = FemaleChar(iNumMaxCBits = 2)
		Subtitles.append("The " + Girl.Desc + "\n& The " + Gang.Desc)
		Girl = FemaleChar()
		Subtitles.append("The " + Master.Desc + "'s\n" + Girl.Desc)
		Subtitles.append(AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord())
		
		sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
		
		return sTweet
		
class Generator18(Generator):
	# Oh No! My Step-Daughter is a Porn Star
	ID = 18
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, NotList = ["Sex", "Lesbian","BDSM", "Anal", "MILF"], bAddEndNoun = False, bAllowMaritalStatus = False, bAllowClothing = False, bAllowSexuality = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet += "\"" + WordList(["S@*#!", "Oh No!", "Uh Oh!", "Whoops!", "WTF?!?", "Oh F*@%!"]).GetWord() + " " 
		sTweet += "My\n" + Girl.Desc + " " + WordList(["Girlfriend", "Bride", "Wife", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Step-Sister", "Twin Sister", "Mom", "Baby Momma", "One True Love"]).GetWord() + "\nIs " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", "An Anal Porn Star", "An Erotic Model", "A Fetish Model", "A Slut", "A Butt Slut"]).GetWord() + "!\""
		
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
		
		if CoinFlip():
			sTweet += ":\n" + WordList(["An " + self._getFMs_(), "A BDSM", "A Taboo", "A Forbidden", "A Secret", "A Submissive"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator20(Generator):
	# I Was Stripped In Public, And I Liked It
	ID = 20
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		
		Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, bAddArticle = True)
		Gang = MaleGangChar(iNumMaxCBits = 3, bAddArticle = True)
		
		sTweet = ""

		sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
		sTweet = "\"I Was " + sVerbBy
		if not "in public" in sVerbBy.lower():
			sTweet += " By\n"
			if CoinFlip():
				sTweet += Master.Desc
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
		sTweet += Master.Desc + ":\nA " + Girl.Desc + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator22(Generator):
	# The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
	ID = 22
	Priority = 4
	
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
	# Deflowered Live on the Internet: An Amish Futa Princess Experience 
	ID = 24
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(Type = GirlType.Good, NotList = ["Pregnant", "Mom", "MILF", "Concubine", "Wife", "Divorced"])
		
		sTweet = "Deflowered Live"
		if CoinFlip():
			sTweet += "!\n"
		else:
			if CoinFlip():
				sTweet += " on the Interet:\n"
			else:
				sTweet += " on Television:\n"
		sTweet += AddArticles(Girl.Desc) + "\n" + self.SubtitleCoda.GetWord()
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
		
class Generator26(Generator):
	# Hotwife for Daddy: A BDSM Romance 
	ID = 26
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar()
		
		sTweet = AddArticles(Girl.Desc) + "\nFor Daddy:\n"
		sTweet += WordList(["A BDSM","An " + self._getFMs_() + "", "A Taboo", "A Forbidden", "A Forbidden", "A Naughty"]).GetWord() + " " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator27(Generator):
	# The Shy Lesbian Gymnast Wore Black
	ID = 27
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"], bAddArticle = True, bAllowRelate = True)
		
		sTweet = Girl.Desc + "\nWore " + WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "A Strap-On"]).GetWord() + ":\n"
		sTweet += "A " + WordList(["FemDom", "Dominatrix", "BDSM", "Cuckold"]).GetWord() + " " + self.SubtitleCoda.GetWord()

		return sTweet

class Generator28(Generator):
	#Cuckolded By My Amish Maiden Hotwife
	ID = 28
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(bAddEndNoun = False, bAllowMaritalStatus = False, NotList = ['Single', 'Divorced'])
		
		if CoinFlip():
			sTweet = "Cuckolded By My\n" + Girl.Desc + " " + WordList(['Wife', 'Wife', 'Hotwife', 'Fiancé', 'Girlfriend', 'Mistress']).GetWord()
		else:
			sTweet = "My " + WordList(['Wife', 'Wife', 'Hotwife']).GetWord() + " And The\n" + MaleChar(bAllowMaritalStatus = False).Desc + ":\nA Cuckold " + self.SubtitleCoda.GetWord()
		
		return sTweet
		
class Generator29(Generator):
	# Blackmailing My Step-Dad's Busty Ballerina
	ID = 29
	Priority = 1
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Girl = FemaleChar(iNumMaxCBits = 2, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False, NotList = ["Girlfriend", "Mom", "Dad", "Sister", "Divorced", "Single", "Hotwife", "Virgin"])
		
		sTweet = WordList(["Dating", "Sleeping With", "Blackmailing", "Secretly Dating", "Sharing", "Watching", "Filming", "Claiming", "Spanking", "Tying Up", "Dominating", "Exposing", "Undressing", "Hypnotizing", "Impregnating", "Owning", "Punishing", "Spanking", "Paddling", "Training", "Pleasuring"]).GetWord() + " "
		sTweet += "My " + WordList(["Father's", "Dad's", "Step-Dad's", "Best Friend's", "Neighbor's", "Boss's", "Son's", "Step-Son's"]).GetWord() + "\n"
		sTweet += Girl.Desc + " " + WordList(["Wife", "Girlfriend", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Hotwife"]).GetWord()

		return sTweet
		
# class Generator30(Generator):
	# # Hot Ménage a Trois: Dick and Lily and The Well-Hung Bodyguard Sumo-Wrestler
	# ID = 30
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""
		
		# sHisName1 = NamesMale().FirstName()
		# sHisName2 = NamesMale().FirstName()
		# sHerName1 = NamesFemale().FirstName()
		# sHerName2 = NamesFemale().FirstName()
		# sLastName = LastNames().GetWord()
		
		# Girl = FemaleChar(iNumMaxCBits = 3)
		# Lesbo = LesbianChar(iNumMaxCBits = 3)
		# Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False)
		# Gay = GayChar(iNumMaxCBits = 3)
		
		# Menages = []
		
		# sTweet = SexyAdjs().GetWord().capitalize() + " " + WordList(["Ménage", "Ménage a Trois", "Threesome", "Three-Way"]).GetWord() + ":\n"
		
		# Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Girl.Desc)
		# Menages.append(sHisName1 + " and " + sHerName1 + "\nand\nthe " + Master.Desc)
		# Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Lesbo.Desc)
		# Menages.append(sHerName1 + " and " + sHerName2 + "\nand\nthe " + Master.Desc)
		# Menages.append(sHisName1 + " and " + sHisName2 + "\nand\nthe " + Gay.Desc)
		# Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Girl.Desc)
		# Menages.append("Mr. & Mrs. " + sLastName + "\nand\nthe " + Master.Desc)
		
		# sTweet += Menages[randint(0, len(Menages) -1)]

		# return sTweet
		
class Generator31(Generator):
	#Wanton & Willing: My Naked Lesbian Futa Princess
	ID = 31
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ListAdjs = WordList(title.misc.AttitudeFemale().List + title.misc.PhysCharFemale().List)
		sAdj1 = ListAdjs.GetWord()
		sAdj2 = ListAdjs.GetWord(NotList = [sAdj1])
		sHerName = NamesFemale().FirstName()
		
		sTweet = sAdj1 + " & " + sAdj2 + ":\n"
		
		if CoinFlip():
			Girl = FemaleChar(iNumMinCBits = 2)
			sTweet += "My " + Girl.Desc
		else:
			Girl = FemaleChar()
			sTweet += sHerName + " the " + Girl.Desc

		return sTweet
		
class Generator32(Generator):
	#Stripping For My Best Friend's Cocky Coal-Miner Brother 
	ID = 32
	Priority = 4
	
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
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		Girl = FemaleChar(iNumMaxCBits = 3)
		sTweet = sVerb + " " + self.HerName + ":\n"
		sTweet += "A " + Girl.Desc + "\n" + self.SubtitleCoda.GetWord()

		return sTweet
		
class Generator34(Generator):
	ID = 34
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sVerb = self.Gerunds.GetWord()
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = True)
			sTweet = sVerb + " " + Girl.Desc
		else:
			sTweet = sVerb + " " + self.HerName
		
		sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 'Twin Sister', 'Best Friend', 'Lesbian Lover']).GetWord()

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
			'Sharing',
			'Showering With',
			'Smothering',
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
		sTweet = sVerb + " Mr. " + LastNames().GetWord() + ":\n"
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
	Priority = 4
	
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

class Generator40(Generator):
	# I Was Ridden Bareback By A Burly Lumberjack Businessman, And He's Not My Husband!
	ID = 40
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		NotVerbs = ['Tempted', 'Beaten', 'Broken', 'Captured', 'Caught', 'Charmed', 'Cuddled', 'Hotwifed', 'Ruled', 'Seduced', 'Tamed', 'Trained']
		
		Master = MaleChar(iNumMaxCBits = 4, bAllowGang = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False)
		if CoinFlip():
			sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nAnd He's Not Her Husband!"
		else:
			sTweet = "I Was " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nWho Was Not My Husband!"

		return sTweet
		
class Generator41(Generator):
	#Seducing Sheryl: The Virginal Nurse and the Big Titty Dominatrix
	ID = 41
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirl = FemaleChar(Type = GirlType.Good, bAddArticle = True, bAllowClothing = False, bAllowGenMod = False, bAllowPregState = False, bAllowMaritalStatus = False, bAllowSexuality = False, bAllowSpecies = False)
		BadGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = True, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowTitle = False)
		
		sTweet = WordList(["Seducing", "Tempting", "Corrupting", "Degrading", "Debauching", "Perverting"]).GetWord() + " " + self.HerName + ":\n"
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
			Master = MaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["boyfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False)
			Relations = title.misc.RelateMale()
			Prefix = WordList(["Secretly In Love With"])
			sTweet = Prefix.GetWord() + "\nMy " + Master.Desc + " " + Relations.GetWord(NotList = ["Boyfriend", "Husband", "Hubbie", "Widower", "Fiancé"])
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, bAddEndNoun = False, NotList = ["girlfriend"], bAllowRelate = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, bAllowTitle = False)
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
	Priority = 4
	
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
	Priority = 3
	
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
		
		Places = WordList(["Land", "Kingdom", "Planet", "World", "Lost Land", "Lost World", "Forgotten Kingdom", "Island", "Lost Island", "Empire", "Zone", "Forbidden Zone"])
		Beings = WordList(["Penisaurs", "Dong-o-saurs", "Fuck Men", "Ass-Eaters", "Ass Apes", "Cock-o-saurus Rex", "Tri-cock Men", "Sex Robots", "Dildo-Bots", "Uniporns", "Girthy Griffons", "Boner Beasts", "Homo Erectus", "Horny Mermen", "Barewolves", "Lepra-dongs", "Semen Centaurs", "Cum Imps", "Dick Dwarves", "Anal Elves", "Anal Aliens", "Naked Barbarians", "Naked Cowboys", "Massive Martians", "Engorged Energy Beings", "Cum Commandos", "Knob Goblins", "Turgid Trolls"])
		
		if CoinFlip():
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
		else:
			Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Bad, bAddArticle = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowPregState = False)
			
		sTweet = sName + " the " + Girl.Desc + " in:\n"	
		sTweet += "The " + Places.GetWord() + " of the " + Beings.GetWord()

		return sTweet
		
# I hooked up with a strapping leather cowboy
# and now I'm pregnant!
class Generator58(Generator):
	ID = 58
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		HookUpPhrases = WordList(["Hooked Up With", "Had a One Night Stand With", "Slept With", "Banged", "Had a Quickie With", "Fooled Around With"])
		MaleRelatives = WordList(["Step-Dad", "Step-Brother", "Brother", "Brother-in-Law", "Father", "Dad", "Daddy", "Step-Father"])
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, bAllowRelate = True, bAllowSpecies = True, bAllowMaritalStatus = True, bAllowGang = False, bAllowTitle = False)
		sMan = Man.Desc 
		
		if MaleRelatives.FoundIn(sMan, MaleRelatives.List):
			sTweet = "I " + HookUpPhrases.GetWord() +" My " + sMan + "\nAnd Now I'm Pregnant!"
		else:
			sTweet = "I " + HookUpPhrases.GetWord() +" " + AddArticles(sMan) + "\nAnd Now I'm Pregnant!"
		return sTweet
	
# The hot bikini model prom queen
# is secretly a lesbian 	
class Generator59(Generator):
	ID = 59
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		sHotAdjs = WordList(["Dirty", "Hot", "Sexy", "Busty", "Jiggly", "Stacked", "Athletic", "Slender", "Apple-Bottomed", "Curvaceous", "Flexible"])
		sGirlAdjs = WordList(["Blonde", "Redhead", "Asian", "Chocolate", "Giggly", "Flirty", "Curly-Haired", "Tattooed"])
		GirlNouns = WordList(["Schoolgirl", "Bimbo", "Cheerleader", "Bikini Model", "Prom Queen", "Teen", "Coed", "Gymnast",
								"Baby-Sitter", "Fashion Model", "Beach Bunny", "Surfer Girl", "Goth Girl"])
		sNoun1 = GirlNouns.GetWord()
		sNoun2 = GirlNouns.GetWord(NotList = [sNoun1])

		sTweet = "The " + sHotAdjs.GetWord() + " " + sGirlAdjs.GetWord() + " "
		sTweet += sNoun1 + " " + sNoun2 + "\n"
		sTweet += "Is Secretly a Lesbian!" 
		return sTweet		
		
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
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		GoodGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Good, bAddArticle = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = False)
		BadGirl = FemaleChar(iNumMaxCBits = 4, Type = GirlType.Bad, bAddArticle = False, bAllowRelate = False, bAllowSexuality = True, bAllowMaritalStatus = False, bAllowSpecies = True, bAllowNation = False, bAllowTitle = False)
		
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
		VacType = WordList(["Topless", "Nudist", "Fully Nude", "Naked"])
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
						  "And I've Seen Her Tits"])
		Girl = FemaleChar(iNumMaxCBits = 4, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False, bAllowPregState = False)

		sTweet = Exclamations.GetWord() + "\nMy New " + Relatives.GetWord() + " Is\n" + AddArticles(Girl.Desc) + "\nAnd " + Ender.GetWord()
		
		return sTweet	
		
# Anita Gets Serviced 
# By Five Naked Cowboys 
class Generator65(Generator):
	ID = 65
	Priority = 2
	
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
		
# My Hot Redhead Teacher
# Is Secretly
# A Stripper!
# class Generator66(Generator):
	# ID = 66
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# "Go easy on me! I'm a teenage coed nun
# and its my first time
# doing anal!"
class Generator67(Generator):
	ID = 67
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Beginnings = WordList(["Please Go Easy On Me", "Please Be Gentle With Me", "Please Be Gentle", "Please Go Slow", 
							   "Please Be Careful"])
		FirstTimes = WordList(["Doing Anal", "With A Girl", "With Another Woman", "Doing Butt Stuff", 
							   "Wearing a Butt Plug", "In a Gimp Mask", "Being Punished With a Riding Crop",
							   "In a Sex Swing", "Deep Throating", "Being Choked", "Trying Erotic Asphyxiation", 
							   "Wearing Nipple Clamps", "In a Sex Dungeon", "Doing It in Public", "Swallowing",
							   "With One This Big", "Trying Bukkake", "Trying Double Penetration",
							   "With Two Dudes", "With Three Guys At Once", "Trying a Gang Bang",
							   "With an Older Man", "Doing Hardcore Bondage Play", "Wearing a Ball Gag",
							   "Trying Water Sports"])
		Girl = FemaleChar(iNumMaxCBits = 3, Type = GirlType.Good, bAddArticle = False, bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False, bAllowPregState = False)

		sTweet = "\"" + Beginnings.GetWord() + "!\nI'm " + AddArticles(Girl.Desc) + "\nAnd Its My First Time\n" + FirstTimes.GetWord() + "!\""

		return sTweet	
		
# I know I'm married,
# but it can't hurt if I try rimming
# with this Italian Don Juan cowboy 
# just this once!
# class Generator68(Generator):
	# ID = 68
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# The wholesome blonde Christian girl spreads her legs (bends over/drops her panties/puts out)
# for the cocky Italian DILF!
class Generator69(Generator):
	ID = 69
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		Actions = WordList(["Spreads her Legs for","Spreads her Legs for","Bends Over for","Drops Her Panties for","Goes Down On","Lifts her Skirt for","Spreads her Thighs for","Spreads her Cheeks for","Opens Her Legs for","Lubes Herself Up for"])
		Girl = title.misc.NiceGirl()
		sNiceGirl = Girl.Desc
		
		Man = MaleChar(iNumMaxCBits = 3, bAddArticle = False, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = True, bAllowGang = False, bAllowTitle = True)
		
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
		
# Daddy Found Out
# His Sweet Little Step-Daughter 
# Is a Sassy Asian Stripper 
# And Now He's Pissed!
# class Generator72(Generator):
	# ID = 72
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
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
		sTweet = "I Turned My " + sNiceGirl + " into " + BadResult.GetWord() + "!"

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

		if CoinFlip():
			sTweet = "I Made My " + sNiceGirl + " Try " + NaughtyStuff.GetWord() + " And " + Reactions.GetWord() + "!"
		else:
			sTweet = "My " + sNiceGirl + " Tried " + NaughtyStuff.GetWord() + " And " + Reactions.GetWord() + "!"
				
		return sTweet	

class Generator75(Generator):
	ID = 75
	Priority = 2
	
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
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel","Maiden","Fetish","Call-Girl"]
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = WomanNotList, bAddArticle = False, bAllowClothing = True, bAllowRelate = False, bAllowSexuality = True, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = True, bAddEndNoun = True)
		Relations = WordList(["Dad's New Girlfriend","New Next Door Neighbor","New Co-worker","New Boss","New Step-Sister",
								"New Step-Daughter","Daughter's New Best Friend","New Student","New Secretatry",
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
	Priority = 2
	
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
		sManAdj = ManAdjs.GetWord()
		Man = MaleChar(iNumMaxCBits = 3, NotList = [sManAdj], bAddArticle = False, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = True)

		sMate = ""
		if CoinFlip():
			sMate = MateAdjs1.GetWord() + " " + MateAdjs2.GetWord() + " " + MateNouns.GetWord()
		else:
			sMate = MateAdjs1.GetWord() + " " + MateNouns.GetWord()
		
		iRand = randint(1,2)
		if iRand == 1:
			sTweet += "I Was " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc)
		elif iRand == 2:
			sTweet += "I Was " + WordList(["Sold","Gifted","Mated","Bound","Betrothed","Promised","Married","Bred"]).GetWord() + " as " + AddArticles(sMate) + "\nto\n" + AddArticles(sManAdj + " " + Man.Desc)
		# else:
			# sTweet += "I Was " + WordList(["Pledged","Trained"]).GetWord() + " as " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc)

		return sTweet	
	
# His for the Fisting:
# A Submissive Nubile Black Flight-Attendant Story	
class Generator78(Generator):
	ID = 78
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""

		Gerunds = WordList(["69ing","Ass-Eating","Bedding","Binding","Breaking","Breeding","Caning","Claiming","Deflowering",
						    "Defiling","Dominating","Edging","Exposing","Fingering","Fisting","Impregating","Ogling","Milking","Motor-Boating",
							"Paddling","Peeing On","Penetrating","Pleasuring","Porking","Pumping","Rimming","Sharing","Shaving","Spanking","Spraying","Spread-Eagling",
							"Spit-Roasting","Stripping","Stuffing","Taking","Tasting","Tea-Bagging","Touching","Toying","Whipping",
							"Undressing","Using","Video-Taping"])
		SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
		sSubAdj = SubAdjs.GetWord()
		Girl = FemaleChar(iNumMaxCBits = 3, NotList = [sSubAdj], bAddArticle = False, bAllowClothing = True, bAllowRelate = True, bAllowSexuality = True, bAllowSpecies = True, bAllowMaritalStatus = True, bAllowTitle = True)
		
		sTweet = "His For The " + Gerunds.GetWord() + ":\n"
		sTweet += AddArticles(sSubAdj + " " + Girl.Desc) + " Story"
		return sTweet	
		
class Generator79(Generator):
	ID = 79
	Priority = 2
	
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
		
# When the Princess
# Met the Cowboy...
# ...and they had wild interracial sex!
# class Generator80(Generator):
	# ID = 80
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

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
							  "CVS","Target","Chipotle","Burger King","the Mall","IHOP","the Multiplex"])
		
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
# class Generator82(Generator):
	# ID = 82
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# 8" of Steel:
# The Feisty Princess (Nubile Queen / Virginal Priestess)
# Encounters 
# The Strapping Naked Half-Orc Barbarian 
# class Generator83(Generator):
	# ID = 83
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# Forsooth My Lord, I See Thou Art Horny!
# The Nubile Princess 
# and the
# Beefy Well-Hung Marquis
# class Generator84(Generator):
	# ID = 84
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	

class Generator85(Generator):
	ID = 85
	Priority = 2
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
		
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, NotList = ManNotList, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowTrope = False, bAllowGenMod = False)

		if CoinFlip():
			sTweet = "I Lost My Virginity\n"
			sTweet += "to " + AddArticles(Man.Desc) + "\n"
		else:
			sTweet = "I Got My Cherry Popped\n"
			sTweet += "by " + AddArticles(Man.Desc) + "\n"
		
		sTweet += WordList(["Live on Television!","Live on the Internet!","And He Gave Me $100!",
								"And My Dad Was Pissed When He Found Out!","And I Let His Friends Watch!",
								"And " + WordList(["a Cop","My Dad","the Principal","a Teacher","My Step-Brother","a Stranger"]).GetWord() + " Caught Us!",
								"And We Filmed the Whole Thing!",
								"In the Basement of His Parents House!","Upstairs at His Parents House!",
								"And He Didn't Pull Out!","And He Did My Ass Too!","And Then My Parents Came Home!",
								"And His Sexy Wife!","And Now I'm Pregnant!","Who Used To Be A Woman!"]).GetWord()

		return sTweet	
		
# I Shared My Innocent Asian Wife 
# with 
# A Well-Hung Beefy Fighter Pilot!
class Generator86(Generator):
	ID = 86
	Priority = 4
	
	def GenerateTweet(self):
		super().GenerateTweet()
		sTweet = ""
		
		ManNotList = ["Space","Gladiator","Knight","Viking","Warrior","Shape-Shifting","Ghost"]
		WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel"]
		
		Man = MaleChar(iNumMaxCBits = 4, bAddArticle = False, NotList = ManNotList, bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, bAllowTrope = True, bAllowGenMod = False)
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
# class Generator88(Generator):
	# ID = 88
	# Priority = 2
	
	# def GenerateTweet(self):
		# super().GenerateTweet()
		# sTweet = ""

		# return sTweet	
		
# class Generator89(Generator):
	# ID = 89
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
		
	def GetGenerator(self, iGen):
		Generator = None 
		
		if len(self.GeneratorList) > 0:
			for gen in self.GeneratorList :
				if gen[1].ID == iGen:
					Generator = gen[1]
					break
					
		return Generator
		