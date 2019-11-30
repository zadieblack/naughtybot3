#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from random import *
from util import *

BodyPartHistoryQ = HistoryQ(10)

class BodyParts:
	def __init__(self):
		self._NounList = WordList([])
		self._AdjList = WordList([])
		self._ColorList = WordList([])
		self._DefaultNoun = ""
		self._DefaultAdj = "naked"
		
		self.NounHistoryQ = HistoryQ(3)
		self.AdjHistoryQ = HistoryQ(3)
		
	def NounList(self, NewNounList = None):
		if NewNounList == None:
			SetNounList = []
		else:
			SetNounList = NewNounList 
			
		self._NounList = WordList(SetNounList)
		
	def AdjList(self, NewAdjList = None):
		if NewAdjList == None:
			SetAdjList = []
		else:
			SetAdjList = NewAdjList
			
		self._AdjList = WordList(SetAdjList)
		
	def ColorList(self, NewColorList = None):
		if NewColorList == None:
			SetColorList = []
		else:
			SetColorList = NewColorList
			
		self._ColorList = WordList(SetColorList)
		
	def DefaultNoun(self, NewNoun = None):
		if NewNoun == None:
			NewNoun = ""
			
		self._DefaultNoun = NewNoun 
	
	def DefaultAdj(self, NewAdj = None):
		if NewAdj == None:
			NewAdj = ""
			
		self._DefaultAdj = NewAdj 
		
	def GetDefaultNoun(self, NotList = None):
		sDefaultNoun = ""
		
		if NotList == None:
			NotList = []

		if self._DefaultNoun not in NotList:
			sDefaultNoun = self._DefaultNoun
			
		return sDefaultNoun
		
	def GetDefaultAdj(self, NotList = None):
		sDefaultAdj = ""
		
		if NotList == None:
			NotList = []

		if self._DefaultAdj not in NotList:
			sDefaultAdj = self._DefaultAdj
			
		return sDefaultAdj
	
	def GetNoun(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._NounList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
	
	def GetAdj(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._AdjList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
		
	def GetColor(self, sNot = "", NotList = None):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
				
		return self._ColorList.GetWord(sNot = sNot, NotList = NotList, SomeHistoryQ = BodyPartHistoryQ)
		
	def GetNounList(self):
		return self._NounList.List 
		
	def GetAdjList(self):
		return self._AdjList.List
		
	def GetColorList(self):
		return self._ColorList.List
		
	def HasColors(self):
		bHasColors = False 
		
		if len(self._ColorList.List) > 0:
			bHasColors = True
			
		return bHasColors

	#noun only ("hair")
	def ShortDescription(self, sNot = "", NotList = None):
		#print("ShortDesc sNot = " + str(sNot))
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		return self.GetNoun(sNot = sNot, NotList = NotList)
	
	#adjective noun ("red hair")
	def MediumDescription(self, sNot = "", NotList = None):
		sMediumDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if self.HasColors() and CoinFlip():
			sMediumDesc = self.GetColor(sNot = sNot, NotList = NotList)
		else:
			sMediumDesc = self.GetAdj(sNot = sNot, NotList = NotList)
		sMediumDesc += " " + self.GetNoun(sNot = sNot, NotList = NotList)
			
		return sMediumDesc
	
	#adjective1 adjective2 adjective3 noun ("long, wavy, red hair")
	def FloweryDescription(self, sNot = "", NotList = None):
		sFloweryDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		iNumAdjs = randint(1, 3)
		
		sAdj1 = ""
		sAdj2 = ""
			
		if iNumAdjs == 3:
			sAdj1 = self.GetAdj(sNot = sNot, NotList = NotList)
			sAdj2 = self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1])
			sAdj3 = ""
			if self.HasColors():
				sAdj3 += self.GetColor(sNot = sNot, NotList = NotList + [sAdj1,sAdj2])
			else:
				sAdj3 += self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1,sAdj2])
			sFloweryDesc += sAdj1 + ", " + sAdj2 + ", " + sAdj3
		elif iNumAdjs == 2:
			sAdj1 += self.GetAdj(sNot = sNot, NotList = NotList) 
			if self.HasColors():
				sAdj2 += self.GetColor(sNot = sNot, NotList = NotList + [sAdj1])
			else: 
				sAdj2 += self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1]) 
			sFloweryDesc += sAdj1 + ", " + self.GetAdj(sNot = sNot, NotList = NotList + [sAdj1])
		else:
			if self.HasColors() and CoinFlip():
				sFloweryDesc += self.GetColor(sNot = sNot, NotList = NotList)
			else:
				sFloweryDesc += self.GetAdj(sNot = sNot, NotList = NotList)
				
		sFloweryDesc += " " + self.GetNoun(sNot = sNot, NotList = NotList)
			
		return sFloweryDesc
	
	def RandomDescription(self, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True):
		sRandomDesc = ""
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		iRand = randint(0, 12)
		
		if iRand in range(0, 3):
		#short desc if allowed 
			if bAllowShortDesc:
				#use noun from the list or default noun
				if CoinFlip():
					sRandomDesc = self.ShortDescription(sNot = sNot, NotList = NotList)
				else:
					sRandomDesc = self.GetDefaultNoun(NotList = NotList)
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
		elif iRand in range(3,6):
		#medium desc 
			sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
		else:
		#flowery desc if allowed
			if bAllowLongDesc:
				sRandomDesc = self.FloweryDescription(sNot = sNot, NotList = NotList)
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot, NotList = NotList)
			
		return sRandomDesc

class Face(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['face',
			'face',
			'face',
			'features'])
		
		self.AdjList(['adorable',
			'angelic',
			'beaming',
			'beautiful',
			'cute',
			'delicate',
			'elegant',
			'excited',
			'gentle',
			'gorgeous',
			'flushed',
			'freckled',
			'heart-shaped',
			'innocent',
			'lovely',
			'oval',
			'pale',
			'pretty',
			'radiant',
			'rosy',
			'round',
			# 'sculpted',
			'smiling',
			'startled',
			# 'surprised',
			'sweet',
			'warm',
			'wide-eyed'])
			
		self.DefaultNoun('face')
		
class BackFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['back','back','back','back',
			'spine'])
		
		self.AdjList(['arched','arched',
			'arching',
			'bare',
			'carved',
			'concave',
			'curved','curved',
			'deliate',
			'feminine',
			'flexible',
			'gently curved',
			'graceful','graceful',
			'lissome',
			'lithe','lithe',
			'long',
			'naked',
			'sculpted',
			'sexy',
			'sleek',
			'slender','slender',
			'slim','slim',
			'smooth',
			'tapered','tapered','tapered',
			'tapering','tapering',
			'well-defined',
			'willowy','willowy'])
			
		self.DefaultNoun('back')
		
class Skin(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['skin','skin','skin','skin',
			'flesh'])
			
		self.ColorList(['almond-colored',
						'brown',
						'bronzed',
						'chocolate',
						'chocolate-colored',
						'coffee-colored',
						'creamy',
						'dark',
						'fresh pink',
						'honeyed',
						'pale',
						'pink',
						'porcelain',
						'rosy',
						'sun-browned',
						'sun-kissed'])
						
		self.AdjList([
			'bare',
			'delicate',
			'exposed',
			'freckled',
			'gentle',
			'gleaming',
			'glistening',
			'glowing',
			'gossamer',
			'luscious',
			'naked',
			'perfect',
			'silken',
			'soft',
			'smooth',
			'supple',
			'sweet',
			'tender',
			'un-blemished',
			'un-sullied',
			'warm',
			'yielding',
			'youthful'])
		
		self.DefaultNoun('skin')
		self.IsPlural = False
		
class Mouth(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['mouth',
						 'mouth',
						 'mouth',
						 'mouth',
						 'mouth-hole'])
			
		self.AdjList(['eager',
			'greedy',
			'hungry',
			'insatiable',
			'insolent',
			'lewd',
			'open',
			'wanting',
			'willing'])
		
		self.DefaultNoun("mouth")
		self.DefaultAdj("insatiable")
		self.IsPlural = False
		
class Lips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['lips'])
			
		self.AdjList(['collagen-injected',
			'full',
			'inviting',
			'insolent',
			'luscious',
			'sensual',
			'sweet'])
			
		self.ColorList(['candy-colored',
						'dark',
						'red','red',
						'rose-colored',
						'rouge',
						'painted black'
					  ])
		
		self.DefaultNoun("lips")
		self.DefaultAdj("full")
		
class Eyes(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['eyes'])
			
		self.AdjList(['alluring',
			'beautiful',
			'bewitching',
			'bright',
			'captivating',
			'clear',
			'dazzling',
			'earnest',
			'electric',
			'electrifying',
			'enchanting',
			'kind',
			'large',
			'mischievous',
			'soulful',
			'sparkling',
			'sweet',
			'wide'])
			
		self.ColorList(['blue','blue',
					  'brown',
					  'gray',
					  'green',
					  'hazel',
					  'pale'])
		
		self.DefaultNoun("eyes")
		self.DefaultAdj("bewitching")
		
class Hips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['hips'])
			
		self.AdjList(['curvy',
			'curvaceous',
			'bare',
			'fertile',
			'rounded',
			'sensual',
			'shapely',
			'slinky',
			'sultry',
			'tantalizing',
			'voluptuous',
			'wanton',
			'wide',
			'womanly'])
		
		self.DefaultNoun("hips")
		
class Hair(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['hair',
			'hair',
			'hair',
			'locks'])
			
		self.AdjList(['curly',
			'braided',
			'glossy',
			'long',
			'luxuriant',
			'pixie cut',
			'silken',
			'short',
			'straight',
			'vibrant',
			'wavy'])
			
		self.ColorList(['black','black',
						'blonde','blonde',
						'blue-dyed',
						'brunette',
						'dark',
						'dyed green',
						'flaming-red',
						'golden',
						'kinky black-girl',
						'platinum blonde',
						'punk blue',
						'sandy',
						'red'])
						
		
		self.DefaultNoun("hair")
		self.DefaultAdj("flowing")
		
class Legs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['legs'])
			
		self.AdjList(['athletic',
			'coltish',
			'elegant',
			'graceful',
			'lithe',
			'limber',
			'lissome',
			'lithesome',
			'long','long',
			'long, sexy',
			'toned',
			'sexy',
			'shapely',
			'shaved',
			'smooth',
			'smooth-shaven'])
		
		self.DefaultNoun("legs")
		
class Thighs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['thighs'])
			
		self.AdjList(['bare',
			'bronzed',
			'chubby',
			'comely',
			'delectable',
			'full',
			'girlish',
			'heavy',
			'inviting',
			'luscious',
			'nubile',
			'pale',
			'powerful',
			'porcelain',
			'ripe',
			'rounded',
			'sensual',
			'sexy',
			'shapely',
			'silken',
			'smooth',
			'soft',
			'tanned',
			'tender',
			'thick','thick',
			'un-sullied',
			'wide',
			'womanly',
			'youthful'])
		
		self.DefaultNoun("thighs")
		
class Nipples(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['nipples',
			'nipples',
			'nipples',
			'nips',
			'teats'])
			
		self.AdjList(['blossoming',
			'budding',
			'dainty',
			'enormous',
			'erect',
			'exposed',
			'inch-long',
			'long',
			'luscious',
			'petite',
			'pert',
			'pokey',
			'puffy',
			'ripe',
			'sensitive',
			'shameless',
			'stiff',
			'succulent',
			'suckable',
			'swollen',
			'tasty',
			'tender',
			'tiny',
			'wide'])
			
		self.ColorList(['chocolate',
						'dark',
						'pink',
						'rosebud',
						'rose-colored'
						])
		
		self.DefaultNoun("nipples")
		self.DefaultAdj("erect")
		
class Breasts(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Nipples = []
		
		self.NounList(['boobies',
			'boobs',
			'bosoms',
			'bosoms',
			'breasts',
			'breasts',
			'breasts',
			'breasts',
			'buds',
			'bust',
			'coconuts',
			'dumplings',
			'gazongas',
			'globes',
			'jugs',
			'knockers',
			'mammaries',
			'melons',
			'orbs',
			'teats',
			'tits',
			'tits',
			'titties'])
			
		self.AdjList(['bouncy',
			'bountiful',
			'budding',
			'buxom',
			'delicious',
			'double-D',
			'full',
			'fulsome',
			'generous',
			'gentle',
			'girlish',
			'glorious',
			'gorgeous',
			'heaving',
			'heavy',
			'impressive',
			'jiggling',
			'juicy',
			'luscious',
			'lush',
			'luxuriant',
			'magnificent',
			'nubile',
			'pale',
			'pendulous',
			'perky',
			'pert',
			'petite',
			'plump',
			'proud',
			'quivering',
			'ripe',
			'round',
			'sensual',
			'shapely',
			'smooth',
			'soft',
			'statuesque',
			'stunning',
			'succulent',
			'sumptuous',
			'supple',
			'surgically-enhanced',
			'swaying',
			'sweet',
			'swollen',
			'tender',
			'voluptuous'])
		
		self.DefaultNoun("breasts")
		self.Nipples = Nipples() 
		
class Clitoris(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['clit',
			'clit',
			'clitoris',
			'clitoris',
			'love-button',
			'love-nub',
			'magic button',
			'nub',
			'pearl'])
			
		self.AdjList(['delicate',
			'engorged',
			'engorged',
			'erect',
			'exposed',
			'fevered',
			'pink',
			'pulsating',
			'pulsing',
			'secret',
			'sensitive',
			'shy little',
			'swollen',
			'tender',
			'throbbing',
			'tingling'])
		
		self.DefaultNoun("clit")
		self.IsPlural = False

class VaginaInner(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['cherry',
				'cleft',
				'chamber',
				'chasm',
				'cock-sock',
				'cunt-hole',
				'fuck-tunnel',
				'fuckhole',
				'furrow',
				'gash',
				'hole',
				'honey hole',
				'honeypot',
				'keyhole',
				'love-channel',
				'love-tunnel',
				'passage',
				'slit',
				'tunnel',
				'vagina',
				'vaginal canal',
				'vestibule',
				'womanhood'])
				
		self.AdjList(['cherry',
				'cherry red',
				'deep',
				'deep',
				'dripping',
				'glazed',
				'gushing',
				'hungry',
				'juicy',
				'lewd',
				'lustful',
				'pink',
				'pink',
				'pink',
				'secret',
				'silken',
				'slick',
				'slick',
				'snug',
				'sopping',
				'spread',
				'succulent',
				'sweet',
				'tender',
				'tight',
				'velvet',
				'velvet',
				'wanton',
				'well-used'])
			
		self.DefaultNoun("vaginal canal")
		self.IsPlural = False
	
class VaginaOuterLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['labia',
							 'lips',
							 'mons pubis',
							 'mound',
							 'nether lips',
							 'outer labia',
							 'outer pussy lips',
							 'pussy lips',
							 'vulva'])
		self.AdjList(['bare',
							'dewy',
							'downy',
							'down-thatched',
							'dripping',
							'fat',
							'fat',
							'fleshy',
							'flushed',
							'fur-lined',
							'girlish',
							'gleaming wet',
							'glistening',
							'hairless',
							'honeyed',
							'juicy',
							'lickable',
							'luscious',
							'lush',
							'moist',
							'naked',
							'peach-fuzzed',
							'pink',
							'plump',
							'puffy',
							'shameless',
							'shaved',
							'shaven',
							'silken',
							'slick',
							'smooth',
							'succulent',
							'suckable',
							'supple',
							'sweet',
							'swollen',
							'tender',
							'trim',
							'wet'])
							
			
		self.DefaultNoun("mons pubis")

class VaginaInnerLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList(['beef-curtains',
							 'butterfly wings',
							 'cunt-lips',
							 'cunt-flaps',
							 'flaps',
							 'flower petals',
							 'folds',
							 'fringe',
							 'inner labia',
							 'labia',
							 'lips',
							 'meat curtains',
							 'meat-flaps',
							 'nether-lips',
							 'petals',
							 'piss-flaps',
							 'pussy-flaps',
							 'pussy lips',
							 'sex flaps',
							 'sex-lips',
							 'wizard sleeve'])
		self.AdjList(['beefy',
							'chewy',
							'dangling',
							'delicate',
							'dewy',
							'dewy',
							'dripping',
							'gleaming wet',
							'glistening',
							'gossamer',
							'honeyed',
							'juicy',
							'lickable',
							'lush',
							'meaty',
							'moist',
							'ruffled',
							'secret',
							'shameless',
							'silken',
							'shy',
							'sticky',
							'sticky',
							'succulent',
							'suckable',
							'trim'])
							
		self.ColorList(['dark',
						'drooping',
						'droopy',
						'little',
						'lengthy',
						'long',
						'meaty',
						'pink',
						'purple',
						'tender',
						'velvet'])
						
		self.DefaultNoun("inner labia")
			
class Vagina(BodyParts):
	InnerVag = []
	InnerLabia = []
	OuterLabia = []
	Clitoris = []
	
	def __init__(self):
		super().__init__()
		
		self.NounList(['cherry pie',
					'cock-garage',
					'cock-sock','cock-sock',
					'cooch',
					'coochie',
					'cunny',
					'cunt','cunt',
					'cunt-hole',
					'flower',
					'fuckhole',
					'fur-burger',
					'honey-hole',
					'honeypot',
					'love-muffin',
					'muff',
					'muffin',
					'peach',
					'pie',
					'pussy','pussy','pussy',
					'quim',
					'sex',
					'snatch','snatch',
					'twat','twat',
					'vagina','vagina',
					'womanhood'])
					   
		self.AdjList(['bare',
					'cherry',
					'clenched',
					'delightful',
					'dewy',
					'down-thatched',
					'dripping',
					'exposed',
					'fuckable',
					'fur-lined',
					'girlish',
					'gleaming wet',
					'glistening',
					'gushing',
					'hairless',
					'honeyed',
					'horny',
					'hungry',
					'juicy',
					'leaky',
					'lewd',
					'lickable',
					'luscious',
					'lush',
					'lustful',
					'moist',
					'naked',
					'peach-fuzzed',
					'puffy',
					'shameless',
					'silken',
					'slick',
					'slutty',
					'smooth',
					'sopping',
					'succulent',
					'suckable',
					'supple',
					'sweet',
					'swollen',
					'tender',
					'tight',
					'trim',
					'unsullied',
					'velvet',
					'wanton',
					'well-used',
					'willing'])
		
		self.DefaultNoun("vagina")
		self.IsPlural = False
		self.InnerVag = VaginaInner()
		self.OuterLabia = VaginaOuterLabia()
		self.InnerLabia = VaginaInnerLabia()
		self.Clitoris = Clitoris()


class AnusFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['anus',
			'anus',
			'anus',
			'arse-cunt',
			'asshole',
			'back orifice',
			'back passage',
			'backdoor',
			'bowels',
			'bunghole',
			'butthole',
			'butt hole',
			'corn hole',
			'dirt-pipe',
			'fart blaster',
			'heinie hole',
			'knot',
			'poop-chute',
			'poop-trap',
			'pooper',
			'rear orifice',
			'rectum',
			'rosebud',
			'sphincter',
			'sphincter',
			'starfish',
			'starfish'])
			
		self.AdjList(['clenched',
			'forbidden',
			'fuckable',
			'gaping',
			'knotted',
			'lewd',
			'little',
			'loose',
			'nasty',
			'naughty',
			'pert',
			'puckered',
			'shy',
			'smooth',
			'snug',
			'taboo',
			'tender',
			'tight',
			'wanton',
			'well-used',
			'willing',
			'winking'])
		
		self.DefaultNoun("anus")
		self.IsPlural = False
		
class ButtocksFemale(BodyParts):
	def __init__(self):
		super().__init__()
	
		self.NounList(['buns',
			'butt-cheeks',
			'buttocks',
			'cheeks'])
			
		self.AdjList(['ample',
			'chubby',
			'curvaceous',
			'curvy',
			'cute',
			'fat',
			'honeyed',
			'jiggling',
			'juicy',
			'luscious',
			'muscular',
			'plump',
			'rotund',
			'round',
			'rounded',
			'shapely','shapely','shapely',
			'smooth',
			'squeezable','squeezable',
			'succulent',
			'supple',
			'sweet',
			'tender',
			'thick','thick','thick',
			'tight',
			'trim',
			'voluptuous',
			'well-rounded'])
			
		self.ColorList(['bronzed',
						'black',
						'brown',
						'coffee-colored',
						'creamy',
						'dark',
						'pale',
						'pink',
						'rosy',
						'sun-kissed',
						'tanned'
					   ])
		
		self.DefaultNoun("buttocks")
		
class AssFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Anus = AnusFemale()
		self.Buttocks = ButtocksFemale()
		
		self.NounList(['ass',
			'backside',
			'behind',
			'booty',
			'bottom',
			'bum',
			'butt',
			'gluteous maximus',
			'heinie',
			'rump',
			'tush',
			'tushy'])
			
		self.AdjList(['ample',
			'bountiful',
			'broad',
			'bubble-shaped',
			'chubby',
			'curvaceous',
			'curvy',
			'cute little',
			'fat',
			'fuckable',
			'generous',
			'glistening',
			'huge',
			'honeyed',
			'jiggling',
			'juicy',
			'lush',
			'luscious',
			'muscular',
			'nubile',
			'pert',
			'plump',
			'ripe',
			'rotund',
			'round',
			'rounded',
			'shameless',
			'shapely',
			'succulent',
			'supple',
			'sweet',
			'tender',
			'thick','thick',
			'tight',
			'trim',
			'voluptuous',
			'womanly',
			'well-rounded'])
			
		self.ColorList(['bronzed',
						'black',
						'brown',
						'coffee-colored',
						'creamy',
						'dark',
						'pale',
						'pink',
						'rosy',
						'sun-kissed',
						'tanned'
					   ])
		
		self.DefaultNoun("ass")
		
	def ShortDescription(self, sNot = "", NotList = None, bAllowButtocks = False):
		sDesc = super().ShortDescription(sNot = "", NotList = NotList)
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)

		if bAllowButtocks:
			if randint(1,15) > 11:
				self.Buttocks.ShortDescription(sNot = sNot, NotList = NotList)
		
		return sDesc
		
	def MediumDescription(self, sNot = "",  NotList = None, bAllowButtocks = False):
		sDesc = super().MediumDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAllowButtocks:
			if randint(1,15) > 11:
				self.Buttocks.MediumDescription(sNot = sNot, NotList = NotList)
			
		return sDesc 
		
	def FloweryDescription(self, sNot = "", NotList = None, bAllowButtocks = False):
		sDesc = super().FloweryDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAllowButtocks:
			if randint(1,15) > 11:
				self.Buttocks.FloweryDescription(sNot = sNot, NotList = NotList)
		
		return sDesc 
		
	def RandomDescription(self, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAllowButtocks = False):
		sDesc = super().RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		if bAllowButtocks:
			if randint(1,15) > 11:
				self.Buttocks.RandomDescription(sNot = sNot, NotList = NotList, 
												bAllowShortDesc = bAllowShortDesc, 
												bAllowLongDesc = bAllowLongDesc)
		
		return sDesc 
		
class BodyFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['anatomy',
			'body',
			'body',
			'body',
			'body',
			'curves',
			'figure',
			'form',
			'physique'])
			
		self.AdjList(['beautiful',
			'busty',
			'buxom',
			'curvaceous',
			'curvy',
			'feminine',
			'gorgeous',
			'leggy',
			'little',
			'lush',
			'luxuriant',
			'model-esque',
			'nubile',
			'pale',
			'ravishing',
			'ripe',
			'sensual',
			'sexy',
			'shameless',
			'shapely',
			'slender',
			'statuesque',
			'stunning',
			'sultry',
			'sweet',
			'teenage',
			'tight',
			'voluptuous',
			'womanly',
			'young',
			'youthful'])
			
		self.ColorList(['black',
						'brown',
						'coffee-colored',
						'mocha',
						'pale',
						'pink',
						'tanned'
					   ])
		
		self.DefaultNoun("body")
		self.DefaultAdj("nubile")
		self.IsPlural = False
		self.Hair = Hair()
		self.Face = Face()
		self.Eyes = Eyes()
		self.Lips = Lips()
		self.Mouth = Mouth()
		self.Hips = Hips()
		self.Back = BackFemale()
		self.Legs = Legs()
		self.Skin = Skin()
		self.Thighs = Thighs()
		self.Breasts = Breasts()
		self.Vagina = Vagina()
		self.Ass = AssFemale()
		
	
	def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
		sPartDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		PartNotList = ['naked','nude','bare','exposed']
		bAddArticles = True
		
		if isinstance(part, Skin):
			PartNotList += ['warm','tender']
			bAddArticles = False 
		elif isinstance(part, Hair): 
			bAddArticles = False 
		elif isinstance(part, Eyes):
			bAddArticles = False 
		elif isinstance(part, Mouth):
			bAddArticles = True 
			PartNotList += ['open','mouth-hole','lewd','insatiable','willing']
		elif isinstance(part, Lips):
			bAddArticles = False 
		elif isinstance(part, Hips):
			bAddArticles = False 
		elif isinstance(part, Legs):
			bAddArticles = False 
		elif isinstance(part, Breasts):
			PartNotList += ['boobies','boobs','buds','coconuts','dumplings','gazongas',
								'globes','jugs','knockers','mammaries','melons','teats','titties',
								'delicious','gentle','girlish','jiggling','lus','nubile',
								'pendulous','pert','quivering','ripe','sensual','surgic',
								'sweet','swollen','tender']
			bAddArticles = False 
			
		#print(" - PartNotList is [" + str(PartNotList) + "]\n")
		if not sPossessive == "":
			bAddArticles = False 
			sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		else:
			sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
			if bAddArticles:
				sPartDesc = AddArticles(sPartDesc)
		
		return sPartDesc
	
	def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
		sBodyDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		if iNum < 3:
			iNum = 3
		if iNum > 5:
			iNum = 5
			
		hair = self.Hair
		face = self.Face 
		eyes = self.Eyes 
		if CoinFlip():
			mouth = self.Lips 
		else:
			mouth = self.Mouth 
		hips = self.Hips 
		back = self.Back
		legs = self.Legs 
		skin = self.Skin
		boobs = self.Breasts 
		body = self
		
		PartPriorities = [[hair,1],
						  [eyes,1],
						  [face,2],
						  [mouth,3],
						  [legs,4],
						  [hips,4],
						  [back,5],
						  [skin,6],
						  [body,6],
						  [boobs,7]]
		
		PartGroups = []
		
		if iNum == 3:
			for part1 in PartPriorities: #skin 6
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] == part1[1] and not part2[0] == part1[0]:
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								PartGroups.append([part1[0],part2[0],part3[0]])
					
		elif iNum == 4:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
	
		else:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
											if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
												PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
		
		SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
		
		iLoops = 0
		while iLoops < iNum:
			sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
			if iLoops == iNum - 2:  
				sBodyDesc += sDivideChar + " and "
			elif iLoops < iNum - 2:
				sBodyDesc += sDivideChar + " "
			iLoops = iLoops + 1
			
		return sBodyDesc
		
	def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
		sPartDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		PartNotList = []
		bAddArticles = True
		
		if isinstance(part, Hips):
			bAddArticles = False 
		elif isinstance(part, Skin):
			bAddArticles = False 
		elif isinstance(part, Legs):
			bAddArticles = False 
		elif isinstance(part, Thighs):
			bAddArticles = False 
		elif isinstance(part, Breasts):
			bAddArticles = False 
		
		if not sPossessive == "":
			bAddArticles = False 
			sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		else:
			sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		
		if bAddArticles:
			sPartDesc = AddArticles(sPartDesc)
		
		return sPartDesc
	
	def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bExplicit = False, bAllowLongDesc = True, sPossessive = None):
		sBodyDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
			sPossessive = ""
		
		if iNum < 3:
			iNum = 3
		if iNum > 5:
			iNum = 5
			
		hair = self.Hair
		face = self.Face 
		eyes = self.Eyes 
		if CoinFlip():
			mouth = self.Lips 
		else:
			mouth = self.Mouth 
		hips = self.Hips 
		back = self.Back
		legs = self.Legs 
		skin = self.Skin
		thighs = self.Thighs 
		nipples = self.Breasts.Nipples
		boobs = self.Breasts 
		pussy = self.Vagina 
		innerlabia = self.Vagina.InnerLabia
		outerlabia = self.Vagina.OuterLabia
		cunthole = self.Vagina.InnerVag 
		ass = self.Ass 
		asshole = self.Ass.Anus 
		body = self
		
		PartPriorities = [[legs,1],
						  [hips,1],
						  [thighs,2],
						  [back,3],
						  [skin,4],
						  [body,4]]
		
		if bBoobs:
			PartPriorities.append([boobs,5])
			PartPriorities.append([nipples,6])
		if bAss:
			PartPriorities.append([ass,7])
		if bPussy:
			PartPriorities.append([pussy,7])
		if bExplicit:
			PartPriorities.append([innerlabia,8])
			PartPriorities.append([outerlabia,8])
			PartPriorities.append([cunthole,8])
			PartPriorities.append([asshole,9])
		
		PartGroups = []
		
		if iNum == 3:
			for part1 in PartPriorities: #skin 6
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] == part1[1] and not part2[0] == part1[0]:
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								PartGroups.append([part1[0],part2[0],part3[0]])
					
		elif iNum == 4:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
	
		else:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
											if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
												PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
		
		SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
		
		iLoops = 0
		while iLoops < iNum:
			sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
			if iLoops == iNum - 2:  
				sBodyDesc += sDivideChar + " and "
			elif iLoops < iNum - 2:
				sBodyDesc += sDivideChar + " "
			iLoops = iLoops + 1
			
		return sBodyDesc
		
	
	
		
	def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
	def GetHoles(self, bIncludeMouth = True):
		Holes = []
		
		if bIncludeMouth:
			Holes = [3]
		
			Holes[0] = self.Mouth.RandomDescription()
			Holes[1] = self.Vagina.RandomDescription()
			Holes[2] = self.Ass.Anus.RandomDescription()
		else:
			Holes = [2]
			
			Holes[0] = self.Vagina.RandomDescription()
			Holes[1] = self.Ass.Anus.RandomDescription()
		
		return Holes
		
	def GetRandomHole(self, bIncludeMouth = True, bAllowShortDesc = True, bAllowLongDesc = True):
		sHole = ""
		Holes = []
		if bIncludeMouth:		
			Holes.append(self.Mouth.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
		else:
			Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
			Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
		
		iRand = randint(0, len(Holes) - 1)
		sHole = Holes[iRand]
		
		return sHole
		
class PenisHead(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['cock-head',
			'head',
			'head',
			'head',
			'helmet',
			'knob',
			'knob',
			'mushroom',
			'tip',
			'tip'])
			
		self.AdjList(['bulging',
			'dripping',
			'engorged',
			'glistening',
			'pulsating',
			'purple',
			'smooth',
			'swollen',
			'throbbing',
			'tumescent'])
			
		self.ColorList(['black',
			'brown',
			'purple',
			'red'])
		
		self.DefaultNoun("head")
		self.IsPlural = False
		
class Testicles(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['balls',
			'ballsack',
			'bollocks',
			'gonads',
			'nutsack',
			'sack',
			'silk purse',
			'scrotum',
			'testicles'])
			
		self.AdjList(['dangling',
			'downy',
			'down-covered',
			'fleshy',
			'hairy',
			'heavy',
			'hefty',
			'pendulous',
			'round',
			'satin',
			'silken',
			'soft',
			'smooth',
			'swaying',
			'swinging',
			'tender',
			'wrinkled'])
		
		self.DefaultNoun("testicles")

class Penis(BodyParts):
	def BuildAPenis(self):
		sPenis = ""
		
		iRandFront = 0
		iRandBack = 0
		
		iRandFront = randint(0,len(self.PenisFrontPart) - 1)
		iRandBack = randint(0,len(self.PenisBackPart) - 1)
		sFrontPart = self.PenisFrontPart[iRandFront]
		sBackPart = self.PenisBackPart[iRandBack]
		
		while sFrontPart in sBackPart:
			iRandFront = randint(0,len(self.PenisFrontPart) - 1)
			iRandBack = randint(0,len(self.PenisBackPart) - 1)
			sFrontPart = self.PenisFrontPart[iRandFront]
			sBackPart = self.PenisBackPart[iRandBack]
			
		sPenis = sFrontPart + "-" + sBackPart
		
		while sPenis in self.GetNounList():
			iRandFront = randint(0,len(self.PenisFrontPart) - 1)
			iRandBack = randint(0,len(self.PenisBackPart) - 1)
			sFrontPart = self.PenisFrontPart[iRandFront]
			sBackPart = self.PenisBackPart[iRandBack]
			
			while sFrontPart in sBackPart:
				iRandFront = randint(0,len(self.PenisFrontPart) - 1)
				iRandBack = randint(0,len(self.PenisBackPart) - 1)
				sFrontPart = self.PenisFrontPart[iRandFront]
				sBackPart = self.PenisBackPart[iRandBack]
				
			sPenis = sFrontPart + "-" + sBackPart
			
		return sPenis
		
	def __init__(self, bAllowBAP = True):
		super().__init__()
		
		self.NounList(['boner',
			'cock',
			'cock',
			'cock',
			'cock meat',
			'cocksicle',
			'dick',
			'erection',
			'girth',
			'goo-gun',
			'hardness',
			'hard-on',
			'hot-rod',
			'joystick',
			'lady-dagger',
			'love-gun',
			'meat',
			'member',
			'organ',
			'package',
			'penis',
			'penis',
			'penis',
			'phallus',
			'pole',
			'popsicle',
			'prick',
			'ramrod',
			'rod',
			'schlong',
			'serpent',
			'shaft',
			'snake',
			'stalk',
			'stem',
			'thing',
			'tool',
			'wood'])
			
		self.AdjList(['beautiful',
			'beefy',
			'bulging',
			'burning',
			'carefully man-scaped',
			'engorged',
			'enormous',
			'enormously erect',
			'erect',
			'erect',
			'fat',
			'fat',
			'fevered',
			'fully erect',
			'hairy',
			'hairless',
			'hard',
			'hardening',
			'hardened',
			'huge',
			'hugely erect',
			'impressive',
			'lengthy',
			'long',
			'lovingly man-scaped',
			'magnificient',
			'massive',
			'massively erect',
			'meaty',
			'pulsating',
			'raging',
			'rampant',
			'rigid',
			'rock-hard',
			'silken',
			'smooth',
			'stiff',
			'swollen',
			'tall',
			'tasty',
			'thick',
			'throbbing',
			'towering',
			'tumescent',
			'turgid',
			'unfurled',
			'veiny',
			'virile'])
			
		self.PenisFrontPart = ['beef',
			'flesh',
			'fuck',
			'love',
			'man',
			'meat']
			
		self.PenisBackPart = ['bayonette',
			'bone',
			'hammer',
			'lance',
			'meat',
			'missile',
			'pipe',
			'pistol',
			'pole',
			'popsicle',
			'python',
			'rocket',
			'rod',
			'rifle',
			'sausage',
			'serpent',
			'shaft',
			'snake',
			'stack',
			'stalk',
			'stick',
			'sword',
			'tool',
			'tube',
			'weapon',
			'worm']
		
		self.DefaultNoun("cock")
		self.IsPlural = False
		self.Head = PenisHead()
		self.Testicles = Testicles()
		
		if bAllowBAP:
			for i in range(0, int(len(self.GetNounList()) * (2/3))):
				self.GetNounList().append(self.BuildAPenis())
	
	def GetRandomPenisPart(self, sNot = None, NotList = None, bAllowShortDesc = False):
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		iRand = randint(1,3)
		
		if iRand == 1:
			return self.Head.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
		elif iRand == 2: 
			return self.Testicles.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
		else:
			return self.RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc)
			
	def GenerateLength(self):
		sLength = ""
		
		sLength = str(randint(6, 13))
		if CoinFlip():
			sLength += " 1/2"
		sLength += "-inch"
		
		return sLength
			
	def ShortDescription(self, sNot = "", NotList = None, bAddLen = False):
		sDesc = super().ShortDescription(sNot = "", NotList = NotList)
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)

		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc
		
	def MediumDescription(self, sNot = "",  NotList = None, bAddLen = False):
		sDesc = super().MediumDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
			
		return sDesc 
		
	def FloweryDescription(self, sNot = "", NotList = None, bAddLen = False):
		sDesc = super().FloweryDescription(sNot = sNot, NotList = NotList)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
		
	def RandomDescription(self, sNot = "", NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False):
		sDesc = super().RandomDescription(sNot = sNot, NotList = NotList, bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc)
		
		if NotList == None:
			NotList = []
		
		if sNot != "":
			NotList.append(sNot)
			
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
	
class Semen(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['cock milk',
			'cock-snot',
			'cream',
			'cum',
			'jizm',
			'jizz',
			'load',
			'lotion',
			'man-custard',
			'man-jam',
			'man-milk',
			'man-seed',
			'sauce',
			'seed',
			'semen',
			'sperm',
			'splooge',
			'spunk'])
			
		self.AdjList(['creamy',
			'delicious',
			'glossy',
			'gooey',
			'nasty',
			'nourishing',
			'oozing',
			'ropy',
			'salty',
			'silken',
			'silky',
			'sloppy',
			'sticky',
			'tasty',
			'thick',
			'warm',
			'white-hot',
			'yummy',
			'cream-colored',
			'milky',
			'pearly',
			'pearlescent'])
		
		self.DefaultNoun("semen")
		self.DefaultAdj("gooey")
		
class ButtocksMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['buns',
			'butt cheeks',
			'buttocks',
			'glutes'])
			
		self.AdjList(['beefy',
			'broad',
			'bronzed',
			'chiseled',
			'compact',
			'hairy',
			'lean',
			'manly',
			'masculine',
			'muscular',
			'rock-hard',
			'sexy',
			'smooth',
			'strapping',
			'swole',
			'taut',
			'tan',
			'tight','tight',
			'trim',
			'virile',
			'well-defined'])
		
		self.DefaultNoun("buttocks")
		
class AssMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Anus = AnusFemale()
		self.Buttocks = ButtocksMale()
		
		self.NounList(['ass',
			'backside',
			'behind',
			'bottom',
			'bum',
			'buns',
			'butt',
			'gluteous maximus',
			'rump',
			'tush'])
			
		self.AdjList(['beefy',
			'broad',
			'bronzed',
			'chiseled',
			'compact',
			'hairy',
			'lean',
			'manly',
			'masculine',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'rock-hard',
			'smooth',
			'strapping',
			'supple',
			'taut',
			'tight',
			'trim',
			'virile',
			'well-defined'])
		
		self.DefaultNoun("buttocks")
		
class SkinMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['skin',
			'skin',
			'skin',
			'flesh',
			'hide'])
			
		self.AdjList(['bare',
			'exposed',
			'glistening',
			'hairy',
			'leathery',
			'naked',
			'rough',
			'rugged',
			'smooth',
			'supple',
			'tough',
			'warm',
			'youthful'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'freckled',
						'light-colored',
						'pale',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("skin")
		self.DefaultAdj("rugged")
		
class ShouldersMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['shoulders'])
			
		self.AdjList(['bare',
			'brawny',
			'broad',
			'freckled',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rugged',
			'strong',
			'sturdy',
			'well-built',
			'wide'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("shoulders")
		self.DefaultAdj("broad")
		
class MusclesMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['muscles'])
			
		self.AdjList(['bare',
			'brawny',
			'broad',
			'bulging',
			'burly',
			'chiseled',
			'hard',
			'hulking',
			'impressive',
			'lean',
			'magnificent',
			'massive',
			'mighty',
			'powerful',
			'robust',
			'rugged',
			'sinewy',
			'strapping','strapping',
			'strong',
			'sturdy',
			'supple',
			'taut',
			'toned',
			'tight',
			'well-built',
			'well-defined',
			'whip-cord',
			'wood-carved'])
			
		self.ColorList(['bronzed',
						'dark',
						'tanned'
					   ])
		
		self.DefaultNoun("shoulders")
		self.DefaultAdj("broad")
		
class ChestMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['chest',
			'chest',
			'chest',
			'chest',
			'pectorals'])
			
		self.AdjList(['bare',
			'brawny',
			'broad',
			'burly',
			'compact',
			'dark-thatched',
			'expansive',
			'hairy',
			'lusty',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rippling',
			'ripped',
			'rugged',
			'strapping',
			'strong',
			'sturdy',
			'toned',
			'wide',
			'uncovered',
			'virile',
			'well-built',
			'well-defined',
			'well-oiled'])
			
		self.ColorList(['bronzed',
						'brown',
						'coffee-colored',
						'dark',
						'ebony',
						'sun-browned',
						'tanned'
					   ])
		
		self.DefaultNoun("chest")
		self.DefaultAdj = "broad"
		
class ArmsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['arms',
			'arms',
			'arms',
			'arms',
			'limbs'])
			
		self.AdjList(['athletic',
			'bare',
			'brawny',
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'protective',
			'rippling',
			'ripped',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry'])
		
		self.DefaultNoun("arms")
		self.DefaultAdj("muscular")
		
class EyesMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['eyes'])
			
		self.AdjList(['alluring',
			'beautiful',
			'bright',
			'brooding',
			'captivating',
			'clear',
			'dazzling',
			'deep',
			'earnest',
			'electric',
			'electrifying',
			'kind',
			'mischievous',
			'penetrating',
			'soulful',
			'sparkling',
			'steely',
			'stern',
			'sweet',
			'youthful',
			'wide'])
			
		self.ColorList(['blue',
						'brown',
						'dark',
						'gray',
						'green',
						'hazel',
						'icy-blue',
						'steely-blue'
					   ])
		
		self.DefaultNoun("eyes")
		self.DefaultAdj("penetrating")

class FacialHair(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['beard','beard','beard',
			'fuzz',
			'goatee',
			'moustache',
			'stubble',
			'fro'])
			
		self.AdjList(['bristling',
			'bushy',
			'curly',
			'full',
			'glossy',
			'long',
			'luxuriant',
			'magnificent',
			'manly',
			'measy',
			'silken',
			'short',
			'thick',
			'trimmed',
			'unkempt',
			'untamed',
			'well-trimmed',
			'wild',
			'wiry'])
			
		self.ColorList(['black','black',
						'blonde','blonde',
						'brown',
						'coifed',
						'dark',
						'graying',
						'sandy',
						'red'])
						
		
		self.DefaultNoun("hair")
		self.DefaultAdj("glossy")
		
class HairMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['afro',
			'bouffant',
			'coif',
			'dreads',
			'fro',
			'hair',
			'hair',
			'hair',
			'locks'])
			
		self.AdjList(['curly',
			'glossy',
			'long',
			'luxuriant',
			'measy',
			'silken',
			'shaggy',
			'short',
			'spiky',
			'untamed',
			'vibrant',
			'wavy',
			'wild'])
			
		self.ColorList(['black','black',
						'blonde','blonde',
						'brunette',
						'coifed',
						'dark',
						'dyed green',
						'flaming-red',
						'golden',
						'graying',
						'platinum blonde',
						'punk blue',
						'sandy',
						'red'])
						
		
		self.DefaultNoun("hair")
		self.DefaultAdj("glossy")
		
class LegsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['legs',
			'legs',
			'legs',
			'calves',
			'limbs',
			'thighs'])
			
		self.AdjList(['athletic',
			'bare',
			'brawny',
			'bronzed',
			'burly',
			'long',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rangy',
			'rippling',
			'sinewy',
			'strapping',
			'strong',
			'sturdy',
			'thick',
			'toned',
			'trunk-like',
			'well-built',
			'wiry'])
		
		self.DefaultNoun("legs")
		self.DefaultAdj("sinewy")
		
class JawMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList(['jaw'])
			
		self.AdjList(['bearded',
			'chiseled',
			'commanding',
			'decisive',
			'dominant',
			'forceful',
			'handsome',
			'powerful',
			'rugged',
			'scruffy',
			'sharp',
			'striking'])
		
		self.DefaultNoun("jaw")
		self.DefaultAdj("chiseled")
		
class BodyMale(BodyParts):	
	def __init__(self):
		super().__init__()
		
		self.NounList(['body','body','body','body',
			'form',
			'physique',
			'bulk',
			'build',
			'body',
			'physique'])
			
		self.AdjList(['beefy',
			'brawny',
			'broad',
			'bronzed',
			'burly',
			'commanding',
			'compact',
			'dark-thatched',
			'handsome',
			'hardened',
			'hearty',
			'hung',
			'husky',
			'lanky',
			'lean',
			'limber',
			'manly',
			'masculine',
			'massive',
			'muscular',
			'powerful',
			'rugged',
			'sinewy',
			'smooth',
			'strapping',
			'striking',
			'strong',
			'sturdy',
			'supple',
			'tall',
			'taut',
			'tight',
			'toned',
			'towering',
			'trim',
			'virile','virile',
			'well-built',
			'well-hung',
			'wiry',
			'youthful'])
		
		self.DefaultNoun("body")
		self.IsPlural = False
		self.FacialHair = FacialHair()
		self.Hair = HairMale()
		self.Eyes = EyesMale()
		self.Jaw = JawMale()
		self.Legs = LegsMale()
		self.Skin = SkinMale()
		self.Shoulders = ShouldersMale()
		self.Muscles = MusclesMale()
		self.Chest = ChestMale()
		self.Arms = ArmsMale()
		self.Ass = AssMale()
		self.Penis = Penis()
		
	# woman random body parts used by gen 8 (one instance), 18,21,31,38,60,72
	# man random body parts used by gen 19, 20, 22,38
	
	def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
		sPartDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		PartNotList = ['naked','nude','bare','exposed']
		bAddArticles = True
		
		if isinstance(part, SkinMale):
			PartNotList += ['warm','tender']
			bAddArticles = False 
		elif isinstance(part, HairMale): 
			bAddArticles = False
		elif isinstance(part, FacialHair): 
			bAddArticles = True 
		elif isinstance(part, EyesMale):
			bAddArticles = False 
		elif isinstance(part, ShouldersMale):
			bAddArticles = False 
		elif isinstance(part, ChestMale):
			bAddArticles = True 
		elif isinstance(part, LegsMale):
			bAddArticles = False 
		elif isinstance(part, AssMale):
			bAddArticles = True 
		elif isinstance(part, PenisHead):
			bAddArticles = True 
		elif isinstance(part, Testicles):
			bAddArticles = True 
		elif isinstance(part, Head):
			bAddArticles = True 
		elif isinstance(part, JawMale):
			bAddArticles = True 
		elif isinstance(part, MusclesMale):
			bAddArticles = False 
		elif isinstance(part, ArmsMale):
			PartNotList += ['boobies']
			bAddArticles = False 
			
		if not sPossessive == "":
			bAddArticles = False 
			sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		else:
			sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
			if bAddArticles:
				sPartDesc = AddArticles(sPartDesc)
		
		return sPartDesc
	
	def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
		sBodyDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		if iNum < 3:
			iNum = 3
		if iNum > 5:
			iNum = 5
			
		hair = self.Hair
		beard = self.FacialHair
		jaw = self.Jaw 
		eyes = self.Eyes 
		chest = self.Chest
		legs = self.Legs 
		skin = self.Skin
		shoulders = self.Shoulders
		arms = self.Arms
		
		PartPriorities = [[hair,1],
						  [eyes,1],
						  [beard,2]
						  [jaw,2]
						  [chest,3],
						  [shoulders,4],
						  [legs,4],
						  [body,5],
						  [skin,6]]
						  
		
		PartGroups = []
		
		if iNum == 3:
			for part1 in PartPriorities: 
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] == part1[1] and not part2[0] == part1[0]:
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								PartGroups.append([part1[0],part2[0],part3[0]])
					
		elif iNum == 4:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
	
		else:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
											if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
												PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
		
		SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
		
		iLoops = 0
		while iLoops < iNum:
			sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
			if iLoops == iNum - 2:  
				sBodyDesc += sDivideChar + " and "
			elif iLoops < iNum - 2:
				sBodyDesc += sDivideChar + " "
			iLoops = iLoops + 1
			
		return sBodyDesc
		
	def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
		sPartDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
		
		PartNotList = []
		bAddArticles = True
		
		if isinstance(part, SkinMale):
			PartNotList += ['warm','tender']
			bAddArticles = False 
		elif isinstance(part, HairMale): 
			bAddArticles = False
		elif isinstance(part, FacialHair): 
			bAddArticles = True 
		elif isinstance(part, EyesMale):
			bAddArticles = False 
		elif isinstance(part, ShouldersMale):
			bAddArticles = False 
		elif isinstance(part, ChestMale):
			bAddArticles = True 
		elif isinstance(part, LegsMale):
			bAddArticles = False 
		elif isinstance(part, AssMale):
			bAddArticles = True 
		elif isinstance(part, PenisHead):
			bAddArticles = True 
		elif isinstance(part, Testicles):
			bAddArticles = True 
		elif isinstance(part, PenisHead):
			bAddArticles = True 
		elif isinstance(part, JawMale):
			bAddArticles = True 
		elif isinstance(part, ArmsMale):
			bAddArticles = False 
		elif isinstance(part, MusclesMale):
			bAddArticles = False 
			
		if not sPossessive == "":
			sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		else:
			sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
		
			if bAddArticles:
				sPartDesc = AddArticles(sPartDesc)
		
		return sPartDesc
	
	def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bPenis = True, bAss = True, bExplicit = False, bAllowLongDesc = True, sPossessive = None):
		sBodyDesc = ""
		
		if sPossessive is None:
			sPossessive = ""
			sPossessive = ""
		
		if iNum < 3:
			iNum = 3
		if iNum > 5:
			iNum = 5
			
		hair = self.Hair
		beard = self.FacialHair
		jaw = self.Jaw 
		eyes = self.Eyes 
		chest = self.Chest
		muscles = self.Muscles
		legs = self.Legs 
		skin = self.Skin
		shoulders = self.Shoulders
		arms = self.Arms
		penis = self.Penis
		balls = self.Penis.Testicles
		head = self.Penis.Head 
		ass = self.Ass 
		asshole = self.Ass.Anus 
		body = self
		
		PartPriorities = [[chest,1],
						  [shoulders,2],
						  [muscles,3],
						  [legs,4],
						  [skin,5],
						  [body,6]]
		
		if bAss:
			PartPriorities.append([ass,4])
		if bPenis:
			PartPriorities.append([penis,8])
		
		if bExplicit:
			PartPriorities.append([testicles,9])
			PartPriorities.append([head,10])
			PartPriorities.append([asshole,11])
		
		PartGroups = []
		
		if iNum == 3:
			for part1 in PartPriorities: #skin 6
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] == part1[1] and not part2[0] == part1[0]:
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								PartGroups.append([part1[0],part2[0],part3[0]])
					
		elif iNum == 4:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										PartGroups.append([part1[0],part2[0],part3[0],part4[0]])
	
		else:
			for part1 in PartPriorities:
				for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
					if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
						for part3 in PartPriorities[PartPriorities.index(part2) + 1:]:
							if part3[1] > part2[1] or (part3[1] == part2[1] and not part3[0] == part2[0]):
								for part4 in PartPriorities[PartPriorities.index(part3) + 1:]:
									if part4[1] > part3[1] or (part4[1] == part3[1] and not part4[0] == part3[0]):
										for part5 in PartPriorities[PartPriorities.index(part4) + 1:]:
											if part5[1] > part4[1] or (part5[1] == part4[1] and not part5[0] == part4[0]):
												PartGroups.append([part1[0],part2[0],part3[0],part4[0],part5[0]])
		
		SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]

		iLoops = 0
		while iLoops < iNum:
			sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
			
			if iLoops == iNum - 2:  
				sBodyDesc += sDivideChar + " and "
			elif iLoops < iNum - 2:
				sBodyDesc += sDivideChar + " "
			iLoops = iLoops + 1

		return sBodyDesc
		
	
				
	def GetRandomIntimateParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts