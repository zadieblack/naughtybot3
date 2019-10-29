#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from random import *
from excerpt.util import *


class BodyParts:
	def __init__(self):
		self.NounList = []
		self.AdjList = []
		self.DefaultNoun = ""
		self.DefaultAdj = "naked"
		
		self.NounHistoryQ = HistoryQ(3)
		self.AdjHistoryQ = HistoryQ(3)
	
	def GetNoun(self, sNot = ""):
		sNoun = ""

		if len(self.NounList) > 0:
			sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
			while not self.NounHistoryQ.PushToHistoryQ(sNoun) and (len(sNot) > 0 and sNot in sNoun):
				sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
				
		return sNoun
	
	def GetAdj(self, sNot = ""):
		sAdj = ""

		if len(self.AdjList) > 0:
			sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
			
			while not self.AdjHistoryQ.PushToHistoryQ(sAdj) or (len(sNot) > 0 and sNot in sAdj):
				sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
			
		return sAdj

	def ShortDescription(self, sNot = ""):
		#print("ShortDesc sNot = " + str(sNot))
		return self.GetNoun(sNot = sNot)
	
	def MediumDescription(self, sNot = ""):
		sMediumDesc = ""
		#print("MediumDesc sNot = " + str(sNot))
		
		sMediumDesc = self.GetAdj(sNot = sNot) + " " + self.GetNoun(sNot = sNot)
			
		return sMediumDesc
	
	def FloweryDescription(self, sNot = ""):
		sFloweryDesc = ""
		#print("FloweryDesc sNot = " + str(sNot))
		
		iNumAdjs = randint(1, 3)
		x = randint(1, 6)
		
		if x == 6 and iNumAdjs < 3 and not sNot in self.DefaultAdj:
			sFloweryDesc += self.DefaultAdj + " "
		else:
			for i in range(0, iNumAdjs):
				sAdj = self.GetAdj(sNot = sNot)
				
				while sAdj in sFloweryDesc:
					sAdj = self.GetAdj(sNot = sNot)
				
				sFloweryDesc += self.GetAdj(sNot = sNot)
								
				if i < iNumAdjs - 1:
					sFloweryDesc += ", "
				elif i == iNumAdjs - 1:
					sFloweryDesc += " "
				
		sFloweryDesc += self.GetNoun(sNot = sNot)
			
		return sFloweryDesc
	
	def RandomDescription(self, sNot = "", bAllowShortDesc = True, bAllowLongDesc = True):
		sRandomDesc = ""
		
		iRand = randint(0, 9)
		
		if iRand in range(0, 3):
			if bAllowShortDesc:
				if CoinFlip():
					sRandomDesc = self.ShortDescription(sNot = sNot)
				else:
					sRandomDesc = self.DefaultNoun
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot)
		elif iRand in range(3, 5):
			if bAllowLongDesc:
				sRandomDesc = self.FloweryDescription(sNot = sNot)
			else:
				sRandomDesc = self.MediumDescription(sNot = sNot)
		elif iRand in range(5, 10):
			sRandomDesc = self.MediumDescription(sNot = sNot)
		else:
			sRandomDesc = self.MediumDescription(sNot = sNot)
			
		return sRandomDesc

class Face(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['face',
			'face',
			'face',
			'features']
		
		self.AdjList = ['adorable',
			'angelic',
			'beaming',
			'beautiful',
			'cute',
			'delicate',
			'elegant',
			'excited',
			'gorgeous',
			'flushed',
			'freckled',
			'heart-shaped',
			'innocent',
			'lovely',
			'oval',
			'pale',
			'pretty',
			'rosy',
			'round',
			'sculpted',
			'smiling',
			'startled',
			'surprised',
			'sweet',
			'wide-eyed']
			
		self.DefaultNoun = 'face'
		
class Skin(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['skin','skin','skin',
			'flesh']
			
		self.AdjList = ['almond-colored',
			'bare',
			'bronzed',
			'chocolate',
			'coffee-colored',
			'dark',
			'delicate',
			'exposed',
			'freckled',
			'gentle',
			'gleaming',
			'glistening',
			'glowing',
			'gossamer',
			'honeyed',
			'luscious',
			'naked',
			'pale',
			'perfect',
			'porcelain',
			'silken',
			'soft',
			'smooth',
			'sun-browned',
			'sun-kissed',
			'supple',
			'sweet',
			'tender',
			'un-blemished',
			'un-sullied',
			'warm',
			'yielding',
			'youthful']
		
		self.DefaultNoun = "skin"
		self.IsPlural = False
		
class Mouth(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['mouth',
						 'mouth',
						 'mouth',
						 'mouth',
						 'mouth-hole']
			
		self.AdjList = ['eager',
			'greedy',
			'hungry',
			'insatiable',
			'insolent',
			'lewd',
			'open',
			'wanting',
			'willing']
		
		self.DefaultNoun = "mouth"
		self.DefaultAdj = "insatiable"
		self.IsPlural = False
		
class Lips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['lips']
			
		self.AdjList = ['candy-colored',
			'red',
			'collagen-injected',
			'full',
			'inviting',
			'insolent',
			'luscious',
			'red',
			'sensual',
			'sweet']
		
		self.DefaultNoun = "lips"
		self.DefaultAdj = "red"
		
class Eyes(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['eyes']
			
		self.AdjList = ['alluring',
			'beautiful',
			'bewitching',
			'blue',
			'brown',
			'captivating',
			'dark',
			'dazzling',
			'enchanting',
			'green',
			'gray',
			'mischievous',
			'soulful',
			'sweet']
		
		self.DefaultNoun = "eyes"
		self.DefaultAdj = "bewitching"
		
class Hips(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['hips']
			
		self.AdjList = ['curvy',
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
			'womanly']
		
		self.DefaultNoun = "hips"
		
class Hair(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['hair',
			'hair',
			'hair',
			'locks']
			
		self.AdjList = ['black',
			'blue-dyed',
			'punk blue',
			'blonde',
			'brunette',
			'curly',
			'dark',
			'flaming-red',
			'glossy blonde',
			'glossy red',
			'glossy brown',
			'golden',
			'kinky black-girl',
			'long, luxuriant',
			'red',
			'silken blonde',
			'short blonde',
			'vibrant red',
			'wavy blonde']
		
		self.DefaultNoun = "hair"
		self.DefaultAdj = "flowing"
		
class Legs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['legs',
			'legs',
			'legs',
			'limbs']
			
		self.AdjList = ['athletic',
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
			'smooth-shaven']
		
		self.DefaultNoun = "legs"
		
class Thighs(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['thighs']
			
		self.AdjList = ['bare',
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
			'youthful']
		
		self.DefaultNoun = "thighs"
		
class Nipples(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['nipples',
			'nipples',
			'nipples',
			'nips',
			'teats']
			
		self.AdjList = ['blossoming',
			'budding',
			'chocolate',
			'dainty',
			'dark',
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
			'rosebud',
			'rose-colored',
			'ripe',
			'sensitive',
			'shameless',
			'stiff',
			'succulent',
			'swollen',
			'tasty',
			'tender',
			'tiny',
			'wide']
		
		self.DefaultNoun = "nipples"
		self.DefaultAdj = "erect"
		
class Breasts(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Nipples = []
		
		self.NounList = ['boobies',
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
			'titties']
			
		self.AdjList = ['bouncy',
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
			'voluptuous']
		
		self.DefaultNoun = "breasts"
		self.Nipples = Nipples() 
		
class Clitoris(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['clit',
			'clit',
			'clitoris',
			'clitoris',
			'love-button',
			'love-nub',
			'magic button',
			'nub',
			'pearl']
			
		self.AdjList = ['delicate',
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
			'tingling']
		
		self.DefaultNoun = "clit"
		self.IsPlural = False

class VaginaInner(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList = ['cherry',
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
				'trench',
				'tunnel',
				'vagina',
				'vaginal canal',
				'vestibule',
				'womanhood']
		self.AdjList = ['cherry',
				'cherry red',
				'clenched',
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
				'virginal',
				'wanton',
				'well-used']
			
		self.DefaultNoun = "vaginal canal"
		self.IsPlural = False
	
class VaginaOuterLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList = ['labia',
							 'lips',
							 'mons pubis',
							 'mound',
							 'nether lips',
							 'outer labia',
							 'outer pussy lips',
							 'pussy lips',
							 'vulva']
		self.AdjList = ['bare',
							'dewy',
							'downy',
							'down-thatched',
							'dripping',
							'fat',
							'fat',
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
							'wet']
			
		self.DefaultNoun = "mons pubis"

class VaginaInnerLabia(BodyParts):

	def __init__(self):
		super().__init__()
		
		self.NounList = ['beef-curtains',
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
							 'pussy lips',
							 'sex-lips',
							 'wizard sleeve']
		self.AdjList = ['beefy',
							'chewy',
							'dangling',
							'dark',
							'delicate',
							'dewy',
							'dewy',
							'dripping',
							'drooping',
							'droopy',
							'gleaming wet',
							'glistening',
							'gossamer',
							'honeyed',
							'juicy',
							'lickable',
							'little',
							'long',
							'lush',
							'meaty',
							'moist',
							'pink',
							'purple',
							'ruffled',
							'secret',
							'shameless',
							'silken',
							'shy',
							'sticky',
							'sticky',
							'succulent',
							'suckable',
							'tender',
							'trim',
							'velvet']
		self.DefaultNoun = "inner labia"
			
class Vagina(BodyParts):
	InnerVag = []
	InnerLabia = []
	OuterLabia = []
	Clitoris = []
	
	def __init__(self):
		super().__init__()
		
		self.NounList = ['cherry pie',
					'cooch',
					'coochie',
					'cunny',
					'cunt',
					'flower',
					'fuckhole',
					'fur-burger',
					'hole',
					'honeypot',
					'love-muffin',
					'muff',
					'muffin',
					'peach',
					'pie',
					'pussy',
					'quim',
					'sex',
					'snatch',
					'twat',
					'vagina',
					'womanhood']
					   
		self.AdjList =  ['bare',
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
					'pink',
					'pink',
					'puffy',
					'shameless',
					'silken',
					'slick',
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
					'virginal',
					'wanton',
					'well-used',
					'willing']
		
		self.DefaultNoun = "vagina"
		self.IsPlural = False
		self.InnerVag = VaginaInner()
		self.OuterLabia = VaginaOuterLabia()
		self.InnerLabia = VaginaInnerLabia()
		self.Clitoris = Clitoris()


class AnusFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['anus',
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
			'hole',
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
			'starfish']
			
		self.AdjList = ['clenched',
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
			'virginal',
			'wanton',
			'well-used',
			'willing',
			'winking']
		
		self.DefaultNoun = "anus"
		self.IsPlural = False
		
class AssFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.Anus = AnusFemale()
		
		self.NounList = ['ass',
			'backside',
			'behind',
			'booty',
			'bottom',
			'bum',
			'buns',
			'butt',
			'buttocks',
			'cheeks',
			'heinie',
			'rump',
			'tush',
			'tushy']
			
		self.AdjList = ['ample',
			'bountiful',
			'broad',
			'bubble-shaped',
			'chubby',
			'curvaceous',
			'curvy',
			'fuckable',
			'generous',
			'glistening',
			'honeyed',
			'juicy',
			'lush',
			'luscious',
			'nubile',
			'pert',
			'plump',
			'ripe',
			'rosy',
			'rotund',
			'round',
			'shameless',
			'shapely',
			'smooth',
			'succulent',
			'supple',
			'sweet',
			'tender',
			'thick',
			'trim',
			'virginal',
			'voluptuous',
			'womanly']
		
		self.DefaultNoun = "ass"
		
class BodyFemale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['anatomy',
			'body',
			'body',
			'body',
			'body',
			'curves',
			'figure',
			'flesh',
			'form',
			'physique']
			
		self.AdjList = ['beautiful',
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
			'youthful']
		
		self.DefaultNoun = "body"
		self.DefaultAdj = "nubile"
		self.IsPlural = False
		self.Hair = Hair()
		self.Face = Face()
		self.Eyes = Eyes()
		self.Lips = Lips()
		self.Mouth = Mouth()
		self.Hips = Hips()
		self.Legs = Legs()
		self.Skin = Skin()
		self.Thighs = Thighs()
		self.Breasts = Breasts()
		self.Vagina = Vagina()
		self.Ass = AssFemale()
		
	def GetRandomBodyParts(self, iNum, bIncludeInners = False, bIncludeIntimate = True, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
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
		elif bIncludeIntimate:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Face.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Lips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		#print(AllParts)
		return Parts
		
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

	DefaultAdj = "voluptuous"
		
class PenisHead(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['cock-head',
			'head',
			'head',
			'head',
			'helmet',
			'knob',
			'knob',
			'mushroom',
			'tip',
			'tip']
			
		self.AdjList = ['bulging',
			'dripping',
			'engorged',
			'glistening',
			'pulsating',
			'purple',
			'smooth',
			'swollen',
			'throbbing',
			'tumescent']
		
		self.DefaultNoun = "head"
		self.IsPlural = False
		
class Testicles(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['balls',
			'ballsack',
			'bollocks',
			'gonads',
			'nutsack',
			'sack',
			'silk purse',
			'scrotum',
			'testicles']
			
		self.AdjList = ['dangling',
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
			'wrinkled']
		
		self.DefaultNoun = "testicles"

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
		
		while sPenis in self.NounList:
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
		
	def __init__(self):
		super().__init__()
		
		self.NounList = ['boner',
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
			'wood']
			
		self.AdjList = ['beautiful',
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
			'virile']
			
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
		
		self.DefaultNoun = "cock"
		self.IsPlural = False
		self.Head = PenisHead()
		self.Testicles = Testicles()
		
		for i in range(0, int(len(self.NounList) * (2/3))):
			self.NounList.append(self.BuildAPenis())
	
	def GetRandomPenisPart(self, bAllowShortDesc = False):
		iRand = randint(1,3)
		
		if iRand == 1:
			return self.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc)
		elif iRand == 2: 
			return self.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc)
		else:
			return self.RandomDescription(bAllowShortDesc = bAllowShortDesc)
			
	def GenerateLength(self):
		sLength = ""
		
		sLength = str(randint(6, 13))
		if CoinFlip():
			sLength += " 1/2"
		sLength += "\""
		
		return sLength
			
	def ShortDescription(self, sNot = "", bAddLen = False):
		sDesc = super().ShortDescription(sNot = sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc
		
	def MediumDescription(self, sNot = "", bAddLen = False):
		sDesc = super().MediumDescription(sNot = sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
			
		return sDesc 
		
	def FloweryDescription(self, sNot = "", bAddLen = False):
		sDesc = super().FloweryDescription(sNot = sNot)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
		
	def RandomDescription(self, sNot = "", bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False):
		sDesc = super().RandomDescription(sNot = sNot, bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc)
		
		if bAddLen:
			Words = sDesc.split()
			Words.insert(len(sDesc.split()) - 1, self.GenerateLength())
			sDesc = " ".join(Words)
		
		return sDesc 
	
class Semen(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['cock milk',
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
			'spunk']
			
		self.AdjList = ['creamy',
			'delicious',
			'glossy',
			'gooey',
			'milky',
			'nasty',
			'nourishing',
			'oozing',
			'pearlescent',
			'pearly',
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
			'yummy']
		
		self.DefaultNoun = "semen"
		self.DefaultAdj = "gooey"
		
class AssMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['ass',
			'backside',
			'behind',
			'bottom',
			'bum',
			'buns',
			'butt',
			'butt cheeks',
			'buttocks',
			'glutes',
			'gluteous maximus',
			'rump',
			'tush']
			
		self.AdjList = ['beefy',
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
			'well-defined']
		
		self.DefaultNoun = "buttocks"
		
class SkinMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['skin',
			'skin',
			'skin',
			'flesh',
			'hide']
			
		self.AdjList = ['bare',
			'bronzed',
			'coffee-colored',
			'dark',
			'ebony',
			'exposed',
			'freckled',
			'glistening',
			'hairy',
			'naked',
			'rough',
			'rugged',
			'smooth',
			'sun-browned',
			'supple',
			'tough',
			'warm',
			'youthful']
		
		self.DefaultNoun = "skin"
		self.DefaultAdj = "rugged"
		
class ShouldersMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['shoulders']
			
		self.AdjList = ['bare',
			'brawny',
			'broad',
			'bronzed',
			'freckled',
			'mighty',
			'muscular',
			'naked',
			'powerful',
			'rugged',
			'strong',
			'sturdy',
			'sun-browned',
			'well-built',
			'wide']
		
		self.DefaultNoun = "shoulders"
		self.DefaultAdj = "broad"
		
class ChestMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['chest',
			'chest',
			'chest',
			'chest',
			'pectorals']
			
		self.AdjList = ['bare',
			'brawny',
			'broad',
			'bronzed',
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
			'well-oiled']
		
		self.DefaultNoun = "chest"
		self.DefaultAdj = "broad"
		
class ArmsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['arms',
			'arms',
			'arms',
			'arms',
			'limbs']
			
		self.AdjList = ['athletic',
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
			'wiry']
		
		self.DefaultNoun = "arms"
		self.DefaultAdj = "muscular"
		
class EyesMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['eyes']
			
		self.AdjList = ['beautiful',
			'blue',
			'brooding',
			'brown',
			'captivating',
			'dark',
			'dazzling',
			'green',
			'gray',
			'icy blue',
			'kind',
			'mischievous',
			'penetrating',
			'soulful',
			'steely-blue',
			'stern',
			'youthful']
		
		self.DefaultNoun = "eyes"
		self.DefaultAdj = "penetrating"
		
class LegsMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['legs',
			'legs',
			'legs',
			'calves',
			'limbs',
			'thighs']
			
		self.AdjList = ['athletic',
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
			'wiry']
		
		self.DefaultNoun = "legs"
		self.DefaultAdj = "sinewy"
		
class JawMale(BodyParts):
	def __init__(self):
		super().__init__()
		
		self.NounList = ['jaw']
			
		self.AdjList = ['bearded',
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
			'striking']
		
		self.DefaultNoun = "jaw"
		self.DefaultAdj = "chiseled"
		
class BodyMale(BodyParts):	
	def __init__(self):
		super().__init__()
		
		self.NounList = ['body',
			'form',
			'physique',
			'anatomy',
			'bulk',
			'build',
			'body',
			'physique',
			'build',
			'form',
			'body']
			
		self.AdjList = ['beefy',
			'brawny',
			'broad',
			'bronzed',
			'burly',
			'commanding',
			'compact',
			'dark-thatched',
			'handsome',
			'hung',
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
			'virile',
			'well-built',
			'well-hung',
			'well-oiled',
			'wiry',
			'youthful']
		
		self.DefaultNoun = "body"
		self.IsPlural = False
		#self.Hair = Hair()
		self.Eyes = EyesMale()
		self.Jaw = JawMale()
		self.Legs = LegsMale()
		self.Skin = SkinMale()
		self.Shoulders = ShouldersMale()
		self.Chest = ChestMale()
		self.Arms = ArmsMale()
		self.Ass = AssMale()
		self.Penis = Penis()
		
	def GetRandomBodyParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
		Parts = []
		AllParts = []
		
		if bIncludeInners:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
		else:
			AllParts.append(self.Eyes.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Jaw.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			#AllParts.append(self.Hair.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Skin.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Arms.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
			
		for x in sorted(sample(range(0, len(AllParts)), iNum)):
			Parts.append(AllParts[x])
			
		return Parts
				
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