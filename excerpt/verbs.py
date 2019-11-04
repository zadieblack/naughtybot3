#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Verbs module

from random import *
from util import *

class Verb:
	def __init__(self):
		self._PastList = WordList()
		self._PresentList = WordList()
		self._GerundList = WordList()
		self._AdverbList = WordList()
		
	def SetPast(self, NewList = None):
		if NewList is None:
			NewList = WordList()
			
		self._PastList = WordList(NewList)
	
	def Past(self, NotList = None):
		if NotList is None:
			NotList = []
			
		return self._PastList.GetWord(NotList = NotList)
			
	def GetPastList(self):
		return self._PastList.List
		
	def SetPresent(self, NewList = None):
		if NewList is None:
			NewList = WordList(NewList)
			
		self._PresentList = WordList(NewList)
		
	def Present(self, NotList = None):
		if NotList is None:
			NotList = []
		
		return self._PresentList.GetWord(NotList = NotList)
		
	def GetPresentList(self):
		return self._PresentList.List
		
	def SetGerund(self, NewList = None):
		if NewList is None:
			NewList = WordList()
			
		self._GerundList = WordList(NewList)
		
	def Gerund(self, NotList = None):
		if NotList is None:
			NotList = []
		
		return self._GerundList.GetWord(NotList = NotList)
		
	def GetGerundList(self):
		return self._GerundList.List
		
	def SetAdverb(self, NewList = None):
		if NewList is None:
			NewList = WordList()
			
		self._AdverbList = WordList(NewList)
		
	def GetAdv(self, NotList = None):
		if NotList is None:
			NotList = []
		
		return self._AdverbList.GetWord(NotList = NotList)
		
	def GetAdverbList(self):
		return self._AdverbList.List
		
class VerbThrust(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['bang',
			'bore into',
			'burrow into',
			'delve into',
			'desecrate',
			'defile',
			'do',
			'drill',
			'fill',
			'fuck','fuck','fuck','fuck',
			'hammer',
			'impale',
			'jackhammer',
			'nail','nail',
			'penetrate',
			'piston into',
			'plough',
			'pound','pound',
			'probe',
			'pump into',
			'ram',
			'ravage',
			'ravish',
			'ream','ream',
			'rut in',
			'slam',
			'stuff','stuff',
			'thrust into',
			'violate'])
			
		self.SetPast(['banged',
			'bored into',
			'burrowed into',
			'delved into',
			'desecrated',
			'defiled',
			'did',
			'drilled',
			'eagerly filled',
			'fucked',
			'hammered',
			'impaled',
			'jackhammered',
			'nailed',
			'penetrated',
			'pistoned into',
			'ploughed',
			'pounded',
			'probed',
			'pumped into',
			'rammed relentlessly into',
			'ravaged',
			'ravished',
			'reamed',
			'rutted in',
			'slammed into',
			'stuffed',
			'thrust deep into',
			'violated'])
			
		self.SetGerund(['banging',
			'boring into',
			'burrowing into',
			'delving into',
			'desecrating',
			'defiling',
			'doing',
			'drilling',
			'eagerly filling',
			'fucking',
			'hammering',
			'impaling',
			'jackhammering',
			'nailing',
			'penetrating',
			'pistoning into',
			'ploughing',
			'pounding',
			'probing',
			'pumping into',
			'ramming relentlessly into',
			'ravaging',
			'ravishing',
			'reaming',
			'rutting in',
			'slamming into',
			'stuffing',
			'thrusting deep into',
			'violating'])
		
class VerbMakeLove(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['make love to',
				'ease into',
				'enter',
				'push into',
				'sex'])
			
		self.SetPast(['made love to',
				'eased into',
				'entered',
				'pushed into',
				'sexed'])
			
		self.SetGerund(['making love to',
				'easing into',
				'entering',
				'pushing into',
				'sexing'])
			
		Harder = VerbThrust()
		
		Prefixes = WordList(['gently','lovingly','carefully','tenderly'])
		
		iNumAdd = len(self.GetPresentList())
		#print("len(self.PresentList) = " + str(iNumAdd))
		for x in sample(range(0, len(Harder.GetPresentList())), iNumAdd):
			#print("len(Harder.PresentList) = " + str(len(Harder.PresentList)) + ", x = " + str(x))
			self.GetPresentList().append(Prefixes.GetWord() + " " + Harder.GetPresentList()[x])
			
		iNumAdd = len(self.GetPastList())
		#print("len(self.PastList) = " + str(iNumAdd))
		for x in sample(range(0, len(Harder.GetPastList())), iNumAdd):
			#print("len(Harder.PastList) = " + str(len(Harder.PastList)) + ", x = " + str(x))
			self.GetPastList().append(Prefixes.GetWord() + " " + Harder.GetPastList()[x])
			
		iNumAdd = len(self.GetGerundList())
		#print("len(self.GerundList) = " + str(iNumAdd)) 
		for x in sample(range(0, len(Harder.GetGerundList())), iNumAdd):
			#print("len(Harder.GerundList) = " + str(len(Harder.GerundList)) + ", x = " + str(x))
			self.GetGerundList().append(Prefixes.GetWord() + " " + Harder.GetGerundList()[x])
		
class VerbEjaculate(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['burst',
			'climax',
			'cum',
			'cum hard',
			'ejaculate',
			'erupt',
			'explode',
			'gush',
			'jizz',
			'orgasm',
			'nut',
			'spurt',
			'squirt'])
			
		self.SetPast(['burst',
			'climaxed',
			'came',
			'came hard',
			'ejaculated',
			'erupted',
			'exploded',
			'gushed',
			'jizzed',
			'nutted',
			'orgasmed',
			'spurted',
			'squirted'])
			
		self.SetGerund(['bursting',
			'climaxing',
			'cumming',
			'cumming hard',
			'ejaculating',
			'erupting',
			'exploding',
			'gushing',
			'jizzing',
			'nutting',
			'orgasming',
			'spurting',
			'squirting'])
		
class VerbDrip(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['dribble',
			'drip',
			'flow',
			'gush',
			'hang',
			'leak',
			'ooze',
			'pour'])
			
		self.SetPast(['dribbled', 
			'dripped', 
			'flowed', 
			'gushed', 
			'hung', 
			'leaked', 
			'oozed', 
			'poured'])
			
		self.SetGerund(['dribbling',
			'dripping',
			'flowing',
			'gushing',
			'hanging',
			'oozing',
			'leaking',
			'pouring'])
		
class VerbForeplay(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['caress',
			'finger',
			'fondle',
			'kiss',
			'lick',
			'nibble on',
			'play with',
			'rub',
			'rub',
			'squeeze',
			'stroke',
			'suck',
			'tease'])
			
		self.SetPast(['caressed',
			'fingered',
			'fondled',
			'kissed',
			'licked',
			'nibbled on',
			'played with',
			'rubbed',
			'squeezed',
			'stroked',
			'sucked',
			'teased'])
			
		self.SetGerund(['caressing',
			'fingering',
			'fondling',
			'kissing',
			'licking',
			'nibbling on',
			'playing with',
			'rubbing',
			'squeezing',
			'stroking',
			'sucking',
			'teasing'])
		
class VerbSex(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['bang',
			'boink',
			'fuck',
			'go at it',
			'have sex',
			'hump',
			'make love'])
			
		self.SetPast(['banged',
			'boinked',
			'fucked',
			'went at it',
			'had sex',
			'humped',
			'made love'])
			
		self.SetGerund(['banging',
			'boinking',
			'fucking',
			'going at it',
			'having sex',
			'humping',
			'making love'])
			
		self.SetAdverb(['ardently',
			'enthusiastically',
			'fervently',
			'fervidly',
			'feverishly',
			'heedlessly',
			'intensely',
			'passionately',
			'rapturously',
			'urgently'])
		
class VerbSexWith(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['bang',
			'boink',
			'fuck',
			'go at it with',
			'have sex with',
			'hump',
			'make love to'])
			
		self.SetPast(['banged',
			'boinked',
			'fucked',
			'went at it with',
			'had sex with',
			'humped',
			'made love to'])
			
		self.SetGerund(['banging',
			'boinking',
			'fucking',
			'going at it with',
			'having sex with',
			'humping',
			'making love to'])
			
		self.SetAdverb(['ardently',
			'enthusiastically',
			'fervently',
			'fervidly',
			'feverishly',
			'heedlessly',
			'intensely',
			'passionately',
			'rapturously'])
		
class VerbMoan(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['cry',
						'gasp',
						'groan',
						'moan',
						'murmur',
						'pant',
						'purr',
						'says',
						'sigh',
						'wail',
						'whimper',
						'whisper'])
					
		self.SetPast(['cried',
					'gasped',
					'groaned',
					'moaned',
					'panted',
					'purred',
					'said',
					'sighed',
					'wailed',
					'whimpered',
					'whispered'])
		
		self.SetGerund(['crying',
						'gasping',
						'groaning',
						'moaning',
						'murmuring',
						'panting',
						'purring',
						'saying',
						'sighing',
						'wailing',
						'whimpering',
						'whispering'])
					
class VerbOralMale(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(['blow',
			'go down on',
			'fellate',
			'suck',
			'suck off',
			'suckle'])
		
		self.SetPast(['blew',
			'went down on',
			'fellated',
			'sucked',
			'sucked off',
			'suckled'])
		
		self.SetGerund(['blowing'
			'fellating',
			'going down on',
			'sucking',
			'sucking off',
			'suckling'])
		
class VerbSexActsByMale(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(["ass fuck",
			"cream-pie",
			"dry hump",
			"eat out",
			"facial",
			"finger bang",
			"fist",
			"rim",
			"sixty-nine",
			"tea-bag",
			"titty fuck",
			"throat fuck"])
			
		self.SetPast(["ass fucked",
			"cream-pied",
			"dry humped",
			"ate out",
			"facialed",
			"fisted",
			"finger banged",
			"rim-jobbed",
			"sixty-nined",
			"tea-bagged",
			"titty fucked",
			"throat fucked"])
			
		self.SetGerund(["ass fucking",
			"cream-pieing",
			"dry humping",
			"eating out",
			"facialing",
			"finger banging",
			"fisting",
			"rimming",
			"sixty-nining",
			"tea-bagging",
			"throat fucking",
			"titty fucking"])
		
class VerbSexActsByFemale(Verb):
	def __init__(self):
		super().__init__()
		self.SetPresent(["blow",
			"deep throat",
			"dry hump",
			"fellate",
			"give a footjob to",
			"jerk off",
			"peg",
			"rim",
			"sixty-nine",
			"squirt on"])
			
		self.SetPast(["blew",
			"dry humped",
			"deep-throated",
			"fellated",
			"gave a footjob to",
			"jerked off",
			"pegged",
			"rimmed",
			"sixty-nined",
			"squirted on"])
			
		self.SetGerund(["blowing",
			"deep throating",
			"dry humping",
			"fellating",
			"giving a footjob to",
			"pegging",
			"rimming",
			"sixty-nining",
			"squriting on"])
	
		
