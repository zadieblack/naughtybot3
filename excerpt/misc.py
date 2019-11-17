#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

import excerpt.people
import excerpt.verbs
import excerpt.names 

from random import *
from util import *
		
class Events(WordList):
	def __init__(self):
		super().__init__(['Ash Wednesday',
		'Christmas Eve',
		'Easter Sunday',
		'Friday',
		'Halloween',
		'Highschool Graduation',
		'Homecoming',
		'Hump Day',
		'Independence Day',
		'International Women\'s Day',
		'Junior Prom',
		'Mardis Gras',
		'Mother\'s Day',
		'my anniversary',
		'my birthday',
		'my wedding day',
		'New Year\'s Eve',
		'Spring Break',
		'St. Patrick\'s Day',
		'Superbowl Sunday',
		'teacher planning day',
		'Valentine\'s Day'])
		
	def RemoveMy(self, sWord):
		return sWord.replace('my ','')
		
	def GetWord(self, bRemoveMy = False):
		sEvent = ""
		
		sEvent = super().GetWord()
			
		if bRemoveMy:
			sEvent = self.RemoveMy(sEvent)
			
		return sEvent
		
class Hashtags(WordList):
	def __init__(self):
		super().__init__(['50shades',
			'amreading',
			'amwriting',
			'BDSM',
			'bookboost',
			'bookblast',
			'bot',
			'botALLY'
			'botlove',
			'dirtybooks',
			'dirtyreads',
			'erotica',
			'erotica',
			'eroticromance',
			'fantasy',
			'fiftyshades',
			'filthy',
			'kink',
			'lovestory',
			'naughty',
			'naughtybooks',
			'naughtyreads',
			'naughtybot',
			'nsfw',
			'PleaseRT',
			'romance',
			'smut',
			'sorrynotsorry',
			'ssrtg',
			'ssrtg',
			'taboo',
			'toosexy',
			'truelove',
			'ThanksIHateIt',
			'twitterbot','twitterbot',
			'writingcommunity',
			'writingprompt'])
		
class BadGirlNouns(WordList):
	def __init__(self):
		super().__init__(['hussy',
						'minx',
						'nympho',
						'skank',
						'slut',
						'slut',
						'slut',
						'tart',
						'tramp',
						'trollop',
						'whore',
						'whore'])
						
class BadGirlAdjs(WordList):
	def __init__(self):
		super().__init__(['brazen',
						'cheeky',
						'filthy',
						'little',
						'nasty',
						'outrageous',
						'saucy',
						'shameless',
						'wanton'])
		
class Exclamations(WordList):
	def __init__(self):
		super().__init__(['baby','oh baby',
		'damn',
		'fuck','fuck','fuck','fuck',
		'oh fuck','oh fuck',
		'fuck me','fuck me',
		'hell','hell',
		'oh hell',
		'holy fuck','holy fuck',
		'oh holy fuck',
		'holy shit','holy shit',
		'oh holy shit',
		'god','god',
		'oh god','oh god',
		'gosh',
		'oh gosh',
		'holy motherfucking shit',
		'holy tits','holy tits',
		'holy fucking tits',
		'lord',
		'oh lord',
		'oh my',
		'oh my god',
		'shit',
		'shit',
		'oh shit',
		'tits',
		'oh tits',
		'you\'ve got to be kidding me'
		'you\'re fucking kidding me'])
		
	def GetWord(self, bHappy = False, bSad = False, bExMk = True):
		sExclamation = ""
		iRand = 1
		
		sExclamation = ""
		if bSad:
			sExclamation = super().GetWord(NotList = ['baby'])
		else:
			sExclamation = super().GetWord(NotList = ['kidding'])
			
		iRand = randint(1, 3)
		if iRand == 1 and bHappy:
			if CoinFlip():
				sExclamation += ", yes"
			else:
				sExclamation += ", yeah"
			
		if bExMk:
			sExclamation += "!"
			
		return sExclamation
		
class TermsOfEndearment(WordList):
	def __init__(self):
		super().__init__(['babe',
		'baby',
		'darling',
		'dear',
		'honey',
		'love',
		'my love',
		'sweetie',
		'sweetheart'])
		
class Gobs(WordList):
	def __init__(self):
		super().__init__(['beads', 
		'drops', 
		'globules', 
		'gobs', 
		'pearls', 
		'ropes', 
		'strings', 
		'trails'])
		
class SexyAdjs(WordList):
	def __init__(self):
		super().__init__(['dirty',
		'filthy',
		'hot',
		'naughty',
		'sexy',
		'steamy'])
		
class WomanAdjs(WordList):
	def __init__(self):
		super().__init__(['beautiful',
			'busty',
			'buxom',
			'comely',
			'curvaceous',
			'curvy',
			'elegant',
			'gorgeous',
			'leggy',
			'lewd',
			'model-esque',
			'MILF-esque',
			'nubile',
			'petite',
			'ravishing',
			'saucy',
			'sensual',
			'sexy',
			'shameless',
			'shapely',
			'slender',
			'statuesque',
			'stunning',
			'sultry',
			'teenage',
			'voluptuous',
			'young',
			'youthful'])

class BookSellers(WordList):
	def __init__(self):
		super().__init__(['Apple Books',
			'Amazon',
			'B&N',
			'Kobo',
			'Radish Fiction',
			'Smashwords',
			'WattPad'])
			
class BookGirls(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Airline Stewardess',
			'Amish Maiden',
			'Babysitter',
			'Bikini Model',
			'Bimbo',
			'Blonde',
			'Brat',
			'Bride',
			'Bridesmaid',
			'BBW',
			'Call-Girl',
			'Co-ed',
			'Concubine',
			'Flight Attendant',
			'Futa',
			'Girlfriend',
			'Governess',
			'Handmaiden',
			'Harem Girl',
			'Hotwife',
			'Housewife',
			'House Maid',
			'Flight Attendant',
			'French Maid',
			'Intern',
			'Lady',
			'Librarian',
			'Maid',
			'Maiden',
			'Masseuse',
			'Mature Woman',
			'Milk Maid',
			'Momma',
			'Nanny',
			'Nurse',
			'Older Woman',
			'Princess',
			'Princess',
			'Redhead',
			'Sex Surrogate',
			'Secretary',
			'Secretary',
			'Single Mom',
			'Step-Daughter',
			'Submissive',
			'Teacher',
			'Virgin',
			'Wallflower',
			'Waitress',
			'Wife',
			'Woman'])
			
class BookGirlAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Amish',
		'BBW',
		'Bimbo',
		'Black',
		'Blonde',
		'Call-Girl',
		'Chaste',
		'Co-ed',
		'Concubine',
		'Curvy',
		'Divorced',
		'Dominatrix',
		'Ebony',
		'Fertile',
		'Futa',
		'Harem',
		'Hotwife',
		'High-Heeled',
		'Innocent',
		'Innocent',
		'Intern',
		'Kept',
		'Lesbian',
		'Married',
		'MILF',
		'Naked',
		'Naked',
		'Naughty',
		'Nubile',
		'Nude',
		'Nudist',
		'Nursing',
		'Pregnant',
		'Redhead',
		'Servant',
		'Sex',
		'Shy',
		'Single',
		'Single Mom',
		'Small-Town',
		'Submissive',
		'Taboo',
		'Teen',
		'Teenage',
		'Virgin',
		'Virgin',
		'Virgin',
		'Virgin',
		'Young'])

class BookMasters(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alpha',
			'Alpha Wolf',
			'Assassin',
			'Barbarian',
			'BBC',
			'BDSM',
			'Biker',
			'Billionaire',
			'Bitcoin Billionaire',
			'Boss',
			'Breeding Stud',
			'CEO',
			'Count',
			'Cop',
			'Cowboy',
			'Dad',
			'Daddy',
			'Dildo Designer',
			'Dinosaur',
			'Doctor',
			'Dom',
			'Duke',
			'Duke',
			'Futanari',
			'Goat Man',
			'Goat Men',
			'Hitman',
			'Incubus',
			'Fire Fighter',
			'Jet Fighter Pilot',
			'King',
			'Knight',
			'Lesbian Cheerleader',
			'Lesbian Dominatrix',
			'Lipstick Lesbian',
			'Older Man',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Stripper',
			'Man-o-taur',
			'Manor Lord',
			'Man-telope',
			'Man-ticore',
			'Marquis',
			'Mer-man',
			'MMA Fighter',
			'Millionaire',
			'Mountain Man',
			'Multi-Millionaire',
			'Navy Seal',
			'Navy Seals',
			'Pirate Captain',
			'Pirates',
			'Playboy Billionaire',
			'Pope',
			'Porn Star',
			'President',
			'Prince',
			'Professor',
			'Quarterback',
			'Rock Star',
			'Roommate',
			'Sex Addict',
			'Sex Warlock',
			'Sheriff',
			'Sorcerer',
			'Spy',
			'Surfer',
			'Trillionaire',
			'Viking',
			'Uniporn',
			'Vampire',
			'Voyeur',
			'Werewolf',
			'Widower'])
			
class BookMasterAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Alien',
			'Alpha',
			'Bad Boy',
			'Bitcoin Billionaire',
			'Biker',
			'Billionaire',
			'Black',
			'Cowboy',
			'Dinosaur',
			'Ebony',
			'Fire Fighter',
			'French',
			'Futanari',
			'Goat Man',
			'Highlander',
			'Hitman',
			'Horny',
			'Irish',
			'Italian',
			'Mer-man',
			'Millionaire',
			'MMA Fighter',
			'Mountain Man',
			'Multi-Millionaire',
			'Naked',
			'Navy Seal',
			'Nudist',
			'Older Man',
			'Outlaw',
			'Pirate',
			'Playboy',
			'Porn Star',
			'Rebel',
			'Renegade',
			'Savage',
			'Scottish',
			'Secret',
			'Sex Addict',
			'Single Dad',
			'Space',
			'Spanish',
			'Stay-at-Home',
			'Stripper',
			'Superstar',
			'Surfer',
			'Viking',
			'Well-hung',
			'Werewolf',
			'Wicked',
			'Widowed'])
			
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Beaten',
			'Blackmailed',
			'Bound',
			'Captured',
			'Claimed',
			'Conquered',
			'Charmed',
			'Deflowered',
			'Dominated',
			'Enslaved',
			'Exposed in Public',
			'Forced',
			'Hotwifed',
			'Humiliated',
			'Impregnated',
			'Kept',
			'Knocked Up',
			'Mastered',
			'Owned',
			'Pleasured',
			'Punished',
			'Ravished',
			'Seduced',
			'Sold',
			'Sold',
			'Spanked',
			'Shaved',
			'Stripped',
			'Taken',
			'Taken',
			'Tempted',
			'Trained'])
			
class BookVerbsTo(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Bound',
				'Cuckquean',
				'Engaged',
				'Hotwife',
				'Hotwifed',
				'Married',
				'Mated',
				'Sold',
				'Submissive',
				'Submitting'])
			
# I really really like the random book titles. See if you can tell! ;-P
class BookTitleBuilder():
	def __init__(self):
		self.Girls = BookGirls()
		self.GirlAdjs = BookGirlAdjs()
		self.Masters = BookMasters()
		self.MasterAdjs = BookMasterAdjs()
		self.VerbsBy = BookVerbsBy()
		self.VerbsTo = BookVerbsTo()

	
	def GetMaster(self, bLong = False):
		sMaster = ""
		
		sMaster = self.Masters.GetWord()
		
		sMasterAdj = self.MasterAdjs.GetWord()
		while sMasterAdj != "" and sMasterAdj in sMaster:
			sMasterAdj = self.MasterAdjs.GetWord()
		
		if CoinFlip():
			if bLong:
				sMaster = sMasterAdj + " " + sMaster
		else:
			sMaster = sMasterAdj + " " + sMaster
			
		return sMaster
		
	def GetGirl(self, bLong = False):
		sGirl = ""
		
		iRand = randint(1,7)
		sGirl = self.Girls.GetWord()
		sGirlAdj = self.GirlAdjs.GetWord()
		while sGirlAdj != "" and sGirlAdj in sGirl:
			sGirlAdj = self.GirlAdjs.GetWord()
			
		if iRand <= 3:
			if bLong:
				sGirl = sGirlAdj + " " + sGirl
		elif iRand > 3 and iRand < 7:
			sGirl = sGirlAdj + " " + sGirl
		elif iRand == 7:
			sGirl = sGirlAdj + " " + sGirl
			
			sGirlAdj = self.GirlAdjs.GetWord()
			while sGirlAdj != "" and sGirlAdj in sGirl:
				sGirlAdj = self.GirlAdjs.GetWord()
				
			sGirl = sGirlAdj + " " + sGirl
			
		return sGirl
		
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
		
	def GetTitle(self):
		sTitle = ""

		sVerbBy = self.VerbsBy.GetWord()
		sVerbTo = self.VerbsTo.GetWord()
		
		sHerName = excerpt.names.NamesFemale().FirstName()
		
		Titles = []
		
		sGirl = self.GetGirl()
		sMaster = self.GetMaster()
		# make sure that both the girl and the master arent just one word b/c thats usually boring
		while len(sGirl.split(" ")) < 2 and len(sMaster.split(" ")) < 2:
			sGirl = self.GetGirl()
			sMaster = self.GetMaster()
		
		# Blackmailed by the Billionaire Mountain Man 
		sTitle = sVerbBy + " by the " + sMaster
		Titles.append(sTitle)
		# =========================

		# Married to the Alpha Wolf
		sTitle = sVerbTo + " to the " + self.GetMaster(bLong = True)
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A " + self._getFMs_() + " Romance"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
		
		# The President's Girl
		sTitle = "The " + self.GetMaster(bLong = True) + "'s " + sGirl
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A BDSM Romance"
			else:
				sTitle += ": A Hot Ménage"
		Titles.append(sTitle)
		# =========================
				
		# The Secretary and the Space Werewolf 
		sTitle = "The " + sGirl + " & the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A BDSM Romance"
			else:
				sTitle += ": A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# Baby for the Stay-at-Home Manticore
		sTitle = "Baby for the " + self.GetMaster(bLong = True) 
		if CoinFlip():
			sTitle += ": A " + self._getFMs_() + " Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Millionaire Sherrif's Virgin
		sTitle = "The " + sMaster + "'s " + sGirl
		Titles.append(sTitle)
		# =========================
				
		# Babysitter to the Billionaire Uniporn
		sTitle = sGirl + " to the " + sMaster
		Titles.append(sTitle)
		# =========================
				
		# Babysitter for the Billionaire Uniporn
		sTitle = sGirl + " for the " + sMaster
		if CoinFlip():
			if CoinFlip():
				sTitle += ": An " + self._getFMs_() + " Adventure"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Small-Town Virgin's First Time
		sTitle = "The " + self.GetGirl(bLong = True) + "'s First Time"
		if CoinFlip():
			if CoinFlip():
				sTitle += ": A " + self._getFMs_() + " Romance"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# Full Frontal for the Shy Amish Virgin: A BDSM Romance
		if CoinFlip():
			sTitle = "Full Frontal Nudity for the "
			if CoinFlip():
				sTitle += self.GetMaster(bLong = True)
			else:
				sTitle += self.GetGirl(bLong = True)
		else:
			sTitle = "Naked for the " + self.GetMaster(bLong = True)
		if CoinFlip():
			if CoinFlip():
				sTitle += ": An " + self._getFMs_() + " Adventure"
			else:
				sTitle += ": A BDSM Romance"
		Titles.append(sTitle)
		# =========================
				
		# The Amish Virgin and the Taboo MILF: A Lesbian Love Story 
		sTitle = "The " + sGirl + " and the " + self.GetGirl()
		if CoinFlip():
			sTitle += ": A Lesbian Love Story"
		else:
			sTitle += ": A Secret Lesbian Affair"
		Titles.append(sTitle)
		# =========================
		
		#print(Titles)
		sTitle = Titles[randint(0, len(Titles) - 1)]
		
		return sTitle

class Punchline():
	Location = None
	MalePunchlines = []
	FemalePunchlines = []
	NeuterPunchlines = []
	
	BigEvent = None
	Exclamation = None 
	JobBlueCollar = None 
	JobWhiteCollar = None 
	JobWealthyMale = None 
	JobWealthyFemale = None 
	MaleFWB = None 
	FemaleFWB = None 
	MaleSO = None 
	FemaleSO = None 
	VerbSex = None 
	
	def __init__(self, Location = None):
		if not Location is None:
			self.Location = Location 
		else:
			self.Location = None
			
		self.BigEvent = Events()
		self.Exclamation = Exclamations()
		self.JobBlueCollar = excerpt.people.JobBlueCollar()
		self.JobWhiteCollar = excerpt.people.JobWhiteCollar()
		self.JobWealthyMale = excerpt.people.JobWealthyMale()
		self.JobWealthyFemale = excerpt.people.JobWealthyFemale()
		self.MaleFWB = excerpt.people.MaleFWB()
		self.FemaleFWB = excerpt.people.FemaleFWB()
		self.MaleSO = excerpt.people.MaleSO()
		self.FemaleSO = excerpt.people.FemaleSO()
		self.VerbSex = excerpt.verbs.VerbSex()
		
		sHappyExclamation = ""
		sSadExclamation = ""
		sExclamation = ""
		
		if CoinFlip():
			sHappyExclamation = self.Exclamation.GetWord(bHappy = True).capitalize() + " "
			sSadExclamation = self.Exclamation.GetWord(bSad = True).capitalize() + " "
			sExclamation = self.Exclamation.GetWord().capitalize() + " "
		
		if not self.Location == None:
			#Female location-specific exclamations
			self.FemalePunchlines.append("'I've never done it " + Location.NamePrep + " before', she said.")
			self.FemalePunchlines.append("'Do you always take your girls " + Location.NamePrep + "?', she asked.")
			self.FemalePunchlines.append("'I'll bet you brought the last " + FemaleFWB.GetPerson() + " here too,' she said teasingly.")
			self.FemalePunchlines.append("'Well, cross that off my bucket list,' she said.")
			
			#Male location-specific exclamations
		
		#Female exclamations 
		self.FemalePunchlines.append("'This is not how I imagined spending " + self.BigEvent.GetWord() + "!' she said.")
		self.FemalePunchlines.append("'This has been the best " + self.BigEvent.GetWord(bRemoveMy = True) + " ever!' she said.")
		self.FemalePunchlines.append("'That was the best " + self.BigEvent.GetWord(bRemoveMy = True) + " gift ever!' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're the best " + self.JobWhiteCollar.GetPerson() +" ever!' she said.")
		self.FemalePunchlines.append("'You should know I'm married,' she said.")
		self.FemalePunchlines.append("'Don't you dare tell mother about this,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I love you,' she said.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "I think I'm in love with you,' she said.")
		self.FemalePunchlines.append("'You can't tell anyone that I'm a " + self.JobWealthyFemale.GetPerson() + ",' she said seriously.")
		self.FemalePunchlines.append("'We can't tell my " + self.MaleSO.GetWord() + " about this,' she said.")
		self.FemalePunchlines.append("'" + sSadExclamation + "My dress is completely ruined!' she said.")
		self.FemalePunchlines.append("'Before you ask, I already have a boyfriend,' she said, 'And he's not a " + self.JobBlueCollar.GetPerson() + " like you.'")
		self.FemalePunchlines.append("'It doesn't count as cheating on your " + self.MaleSO.GetWord() + " if you " + self.VerbSex.Present() + " a " + self.JobWealthyMale.GetPerson() + ", right?' she asked.")
		self.FemalePunchlines.append("'I can't let my " + self.MaleSO.GetWord() + " know that I'm screwing my " + self.JobBlueCollar.GetPerson() + "!' she said.")
		self.FemalePunchlines.append("'Hang on,' she said, 'I need to Snap Chat this.'")
		self.FemalePunchlines.append("'I usually only do this for money,' she said.")
		self.FemalePunchlines.append("'I can't wait to tell my husband all about this,' she said.")
		
		
		#Male exclamations
		self.MalePunchlines.append("'Happy " + self.BigEvent.GetWord(bRemoveMy = True) + "!' he said.")
		self.MalePunchlines.append("'We can't tell my " + self.FemaleSO.GetWord() + " about this,' he said.")
		self.MalePunchlines.append("'You should know I'm married,' he said.")
		self.MalePunchlines.append("'You can't tell anyone that I'm a " + self.JobWealthyMale.GetPerson() + ",' he said, seriously.")
		self.MalePunchlines.append("'Same time next Tuesday?' he asked.")
		self.MalePunchlines.append("'You remind me so much of my ex-wife,' he said.")
		self.MalePunchlines.append("'I can't wait to tell my " + self.FemaleSO.GetWord() + " about this,' he said.")
		self.MalePunchlines.append("'Fuck, interracial sex really IS hot!' he said.")
		self.MalePunchlines.append("'Here's my business card,' he said. 'Call me.'")
		
		
	def GetPunchline(self, gender):
		sPunchline = ""
		iRand = 0
		if gender == Gender.Male and not self.MalePunchlines is None and len(self.MalePunchlines) > 0:
			iRand = randint(0, len(self.MalePunchlines) - 1)
			sPunchline = self.MalePunchlines[iRand]
		elif gender == Gender.Female and not self.FemalePunchlines is None and len(self.FemalePunchlines) > 0:
			iRand = randint(0, len(self.FemalePunchlines) - 1)
			sPunchline = self.FemalePunchlines[iRand]
		elif gender == Gender.Neuter and not self.NeuterPunchlines is None and len(self.NeuterPunchlines) > 0:
			iRand = randint(0, len(self.NeuterPunchlines) - 1)
			sPunchline == self.NeuterPunchlines[iRand]
		else:
			pass
			
		return sPunchline
		
class PunchlineAfterSex(Punchline):
	def __init__(self, Location = None):
		if not Location is None:
			self.Location = Location 
		else:
			self.Location = None
			
		super().__init__(Location)
		
		sHappyExclamation = ""
		sSadExclamation = ""
		sExclamation = ""
		
		if CoinFlip():		
			sHappyExclamation = self.Exclamation.GetWord(bHappy = True).capitalize() + " "
			sSadExclamation = self.Exclamation.GetWord(bSad = True).capitalize() + " "
			sExclamation = self.Exclamation.GetWord().capitalize() + " "
		
		if not self.Location == None:
			#Female location-specific exclamations
			
			#Male location-specific exclamations
			self.MalePunchlines.append("'I can't believe I just did it with my " + self.FemaleFWB.GetPerson() + " " + Location.NamePrep + "!' he said.")
	
		#Female exclamations 
		self.FemalePunchlines.append("'" + sHappyExclamation + "That was amazing! What did you say your name was again?' she asked.")
		self.FemalePunchlines.append("'" + sHappyExclamation + "You're so good, baby,' she said to her " + self.MaleFWB.GetPerson() + ".")	
		self.FemalePunchlines.append("'" + sHappyExclamation + "I can't believe I'm not a virgin anymore,' she said.")	
		self.FemalePunchlines.append("'Was this your first time " + self.VerbSex.Gerund() + " a " + self.JobWealthyFemale.GetPerson() + "?' she asked him.")	
		self.FemalePunchlines.append("'" + sExclamation + "What would my mother say if she knew that I was " + self.VerbSex.Gerund () + " a " + self.JobBlueCollar.GetPerson() + "?'. she asked.")
		self.FemalePunchlines.append("'Same time next Thursday?' she asked.")
		
		#Male exclamations 
		self.MalePunchlines.append("'You're even better than your sister,' he said.")
		self.MalePunchlines.append("'So is this a date?' he asked.")
	
		
		