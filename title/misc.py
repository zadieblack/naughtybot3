#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

import title.people
import title.verbs
import title.names 

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
		
class MaleSO(WordList):
	def __init__(self):
		super().__init__(['boyfriend',
			'fiancé',
			'hubby',
			'husband'])
			
class FemaleSO(WordList):
	def __init__(self):
		super().__init__(['bride',
			'girlfriend',
			'fiancé',
			'wife'])
		
class Hashtags(WordList):
	def __init__(self):
		super().__init__(['50shades',
			'amreading',
			'amwriting',
			'BannedFromAmazon',
			'bookboost',
			'bookideas',
			'bot',
			'botwriter',
			'dirtyreads',
			'eartg',
			'erotic',
			'erotica','erotica',
			'eroticromance',
			'fiftyshades',
			'inspiration',
			'KindleUnlimited',
			'kink',
			'JustABot',
			'lovestory',
			'lprtg',
			'mustread',
			'naughty',
			'naughtybot',
			'naughtyreads',
			'nsfw','nsfw',
			'PleaseRT',
			'romance','romance','romance',
			'romanceauthor',
			'romancereaders',
			'sexybot',
			'smut',
			'sorrynotsorry','sorrynotsorry',
			'ssrtg',
			'steamy',
			'ThanksIHateIt',
			'twitterbot','twitterbot',
			'wprtg',
			'writingcommunity',
			'writingprompt'])
		
class BadGirlNames(NounAdjList):
	DefaultNoun = 'slut'
	DefaultAdj = 'little'
	
	NounList = ['hussy',
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
		'whore']
		
	AdjList = ['brazen',
		'cheeky',
		'filthy',
		'little',
		'nasty',
		'outrageous',
		'saucy',
		'shameless',
		'wanton']
			
# mature, young, teenager, MILF, etc
class AgeFemaleNoun(WordList):
	def __init__(self):
		super().__init__(['College Girl','College Girl',
			'Maiden','Maiden',
			'Mature Woman','Mature Woman',
			'MILF','MILF',
			'Older Woman','Older Woman',
			'Schoolgirl','Schoolgirl',
			'Teen','Teen',
			'Teenager','Teenager',
			'Virgin','Virgin','Virgin'])
			
# mature, young, teenager, MILF, etc
class AgeFemaleAdj(WordList):
	def __init__(self):
		super().__init__(['Co-ed','Co-ed',
			'Maiden','Maiden',
			'Mature','Mature',
			'MILF','MILF',
			'Nubile','Nubile',
			'Older','Older',
			'Schoolgirl','Schoolgirl',
			'Teen','Teen',
			'Teenage','Teenage',
			'Virgin','Virgin',
			'Young','Young'])
		
# bashful, innocent, etc 
class AttitudeGoodFemale(WordList):
	def __init__(self):
		super().__init__(['Anal Virgin',
			'Angelic',
			'Bashful',
			'Bouncy',
			'Bubbly',
			'Chaste',
			'Classy',
			'Conservative','Conservative',
			'Demure',
			'Ditzy',
			'Eager',
			'Elegant',
			'Flirty',
			'Gentle',
			'Innocent','Innocent','Innocent',
			'Kind',
			'Lonely',
			'Modest','Modest',
			'Perky','Perky',
			'Sexy',
			'Sheltered',
			'Shy','Shy',
			'Soft',
			'Soft-hearted',
			'Sparkling',
			'Spirited',
			'Sporty',
			'Spunky',
			'Straight',
			'Straight-laced',
			'Sweet','Sweet',
			'Uptight',
			'Virginal',
			'Virtuous',
			'Vivacious',
			'Wholesome','Wholesome'])
		
# kinky, slutty, etc 
class AttitudeBadFemale(WordList):
	def __init__(self):
		super().__init__(['Anal Virgin',
			'Brazen',
			'Daring',
			'Desperate',
			'Devlish',
			'Dirty','Dirty',
			'Dirty-Minded',
			'Dripping Wet',
			'Foxy',
			'Horny',
			'Kinky','Kinky',
			'Lewd',
			'Moist',
			'Naughty','Naughty',
			'Nasty',
			'Nympho','Nympho',
			'Perverted',
			'Promiscuous',
			'Revealing',
			'Risqué',
			'Sadistic',
			'Salacious',
			'Sassy','Sassy',
			'Saucy',
			'Seductive',
			'Shameless','Shameless',
			'Slutty','Slutty','Slutty',
			'Sultry',
			'Wanton','Wanton',
			'Wet',
			'Wicked',
			'Wild','Wild',
			'Willing','Willing',
			'X-Rated'])
			
class AttitudeFemale(WordList):
	def __init__(self):
		super().__init__(AttitudeGoodFemale().List + AttitudeBadFemale().List)		
		
class ClothingFemale(WordList):
	def __init__(self):
		super().__init__(['Bikini-Wearing',
			'Braless',
			'Fashionable',
			'G-String',
			'High-Heeled',
			'Latex-Wearing',
			'Leather-Clad',
			'Naked',
			'Nudist','Nudist',
			'Scantily-Clad',
			'Stylish',
			'Thong-Wearing',
			'Topless'])

class GenModFemale(WordList):
	def __init__(self):
		super().__init__(['Anal','Anal',
		'BDSM','BDSM',
		'Erotic',
		'Fetish',
		'Horny',
		'Naughty',
		'Naked',
		'Nude',
		'Oiled Up',
		'Scandalous',
		'Sexy','Sexy',
		'Taboo',
		'Tattooed'])
		
# single, single mom, married, engaged
class MaritalStatusFemale(WordList):
	def __init__(self):
		super().__init__(['Recently-Divorced',
			'Married','Married','Married',
			'Single','Single','Single','Single'])

# french, italian, etc
class NationFemale(WordList):
	def __init__(self):
		super().__init__(['All-American',
			'African',
			'Amish','Amish','Amish',
			'Asian','Asian',
			'Brazillian','Brazillian',
			'Christian','Christian','Christian',
			'Columbian',
			'Country',
			'Czech',
			'Eastern European',
			'Elvish',
			'French',
			'German',
			'Irish',
			'Italian',
			'Japanese',
			'Jewish',
			'Korean',
			'Latina',
			'Mexican',
			'Mormon',
			'Norwegian',
			'Polynesian',
			'Russian',
			'Small-Town',
			'Swedish',
			'Swiss'])
		
# big-titty, etc
class PhysCharFemale(WordList):
	def __init__(self):
		super().__init__(['Apple-Bottomed',
			'Ample-Bosomed',
			'Athletic',
			'Attractive',
			'Bare-Shaven',
			'Beautiful',
			'Big Bottomed',
			'Big-Titty',
			'Bikini-Bod',
			'Boobalicious',
			'Bosomy',
			'Bubble Butt',
			'Busty',
			'Buxom',
			'Chubby',
			'Comely',
			'Curvy',
			'Curvaceous',
			'Cute',
			'Flat-Chested',
			'Flexible',
			'Full-Figured',
			'Gorgeous',
			'Hot',
			'Jiggling',
			'Juicy','Juicy',
			'Large-Breasted',
			'Leggy',
			'Little','Little','Little',
			'Nubile',
			'Petite',
			'Plump',
			'Ripe',
			'Round-Bottomed',
			'Rubenesque',
			'Shapely',
			'Shaved Bare',
			'Skinny',
			'Slender',
			'Soft',
			'Sporty',
			'Stacked',
			'Statuesque',
			'Tender',
			'Thick',
			'Thicc',
			'Tight',
			'Tight-Bodied',
			'Tiny',
			'Top-Heavy',
			'Voluptuous',
			'Wide-Bottomed',
			'Young'])
			
class PregState(WordList):
	def __init__(self):
		super().__init__(['Fertile','Fertile','Fertile','Fertile',
			'Lactating','Lactating',
			'Pregnant','Pregnant','Pregnant',
			'Nursing','Nursing'])

# nurse, flight-attendant, etc
class ProfGoodFemale(WordList):
	def __init__(self):
		super().__init__(ProfNeutralFemale().GetWordList())
			
class ProfFantasyFemale(WordList):
	def __init__(self):
		super().__init__(['Lady',
			'Maid',
			'Milk Maid',
			'Servant',
			'Slave Girl'])
			

# porn star, call girl, escort, etc
class ProfNeutralFemale(WordList):
	def __init__(self):
		super().__init__(['Airline Stewardess',
			'Ballerina',
			'Babysitter',
			'Barista',
			'Bikini Model',
			'Cheerleader',
			'Co-ed',
			'College Girl',
			'Fashion Model',
			'Flight Attendant',
			'French Maid',
			'Gymnast',
			'House Maid',
			'Housewife',
			'Intern',
			'Librarian',
			'Masseuse',	
			'Maid',
			'Mommy Blogger',
			'Nanny',
			'Nun',
			'Nurse','Nurse',
			'Nursing Student',
			'Schoolgirl',
			'School-marm',
			'Secretary','Secretary',
			'Stay-at-Home Mom',
			'Supermodel',
			'Teacher',
			'Waitress',
			'Yoga Instructor'])
			
# porn star, call girl, escort, etc
class ProfVeryBadFemale(WordList):
	def __init__(self):
		super().__init__(['Amateur Porn Star',
			'Anal Whore',		
			'Call-Girl','Call-Girl',
			'Club Dancer',		
			'Dominatrix',
			'Escort',		
			'Fetish Model',
			'Hooter\'s Waitress',		
			'Lingerie Model',
			'Penthouse Pet',
			'Playboy Centerfold',
			'Pole Dancer',
			'Porn Star',
			'Stripper','Stripper',
			'Whore'])
			
# porn star, call girl, escort, etc
class ProfBadFemale(WordList):
	def __init__(self):
		super().__init__(ProfNeutralFemale().GetWordList() + ProfVeryBadFemale().GetWordList())
			
class ProfFemale(WordList):
	def __init__(self):
		super().__init__(ProfGoodFemale().List + ProfBadFemale().List)

class NiceGirlNouns(WordList):
	def __init__(self):
		super().__init__(["Babysitter",
						  "Bride",
						  "Fiancé",
						  "Girlfriend",
						  "Governess",
						  "House Maid",
						  "Housewife",
						  "Librarian",
						  "Maid",
						  "Piano Teacher",
						  "Teacher",
						  "Secretary",
						  "Schoolgirl",
						  "Small-Town Girl",
						  "Stay-at-Home Wife",
						  "Step-Daughter",
						  "Step-Mom",
						  "Step-Sister",
						  "Wife"])
						  
class ProfLesbian(WordList):
	def __init__(self):
		super().__init__(['Artist',
			'Athlete',
			'Basketball Player',
			'Bodyguard',
			'Boxer',
			'Bull Rider',
			'Cheerleader',
			'Coal Miner',
			'Construction Worker',
			'Cop',
			'Cowgirl',
			'Deputy',
			'Dominatrix',
			'Escort',
			'Fetish Model',
			'Fitness Model',
			'Fire Fighter','Fire Fighter',
			'Green Beret',
			'Gym Coach',
			'Killer-for-Hire',
			'Lumberjane','Lumberjane','Lumberjane',
			'Matador',
			'Mechanic','Mechanic',
			'MMA Fighter',
			'Nun',
			'Private Eye',
			'Rodeo Clown',
			'Sailor','Sailor',
			'Schoolgirl',
			'Secret Service Agent',
			'Secretary','Secretary',
			'Snowboarder',
			'Stuntwoman',
			'Tattoo Artist',
			'Tri-Athlete',
			'Trucker','Trucker','Trucker'])

# step-daughter, mom
class RelateFemale(WordList):
	def __init__(self):
		super().__init__(['Concubine',
			'Cousin',
			'Daughter','Daughter',
			'Daughter\'s Best Friend',
			'Girlfriend','Girlfriend','Girlfriend',
			'Mistress',
			'Mommy','Mommy',
			'Sister',
			'Step-Daughter','Step-Daughter',
			'Step-Mom','Step-Mom','Step-Mom',
			'Step-Sister','Step-Sister',
			'Wife','Wife'])

class SexualityFemale(WordList):
	def __init__(self):
		super().__init__(['Bi-Curious',
			'Bisexual',
			'Lesbian','Lesbian','Lesbian',
			'Pansexual',
			'Trans'])
			
class SexualityNounFemale(WordList):
	def __init__(self):
		super().__init__(['Bi-Curious Girl','Bi-Curious Woman',
			'Bisexual','Bisexual',
			'Lesbian','Lesbian','Lesbian','Lesbo',
			'Pansexual',
			'Queer Girl','Queer Woman',
			'Trans Girl','Trans Woman'])

class SkinColorPOCFemale(WordList):
	def __init__(self):
		super().__init__(['Almond-Skinned',
			'Black','Black','Black',
			'Brown-skinned',
			'Ebony','Ebony',
			'Bronzed','Bronzed',
			'Dark-Skinned',
			'Mocha-Skinned',
			'Tanned','Tanned'])
			
class SkinColorWhiteFemale(WordList):
	def __init__(self):
		super().__init__(['Almond-Skinned',
			'Bronzed','Bronzed',
			'Pale','Pale',
			'Tanned','Tanned',
			'White'])
			
class SkinColorFemale(WordList):
	def __init__(self):
		super().__init__(SkinColorPOCFemale().GetWordList() + SkinColorWhiteFemale().GetWordList())

class HairColorWhiteFemale(WordList):
	def __init__(self):
		super().__init__(['Blonde','Blonde',
			'Blue-Eyed','Blue-Eyed',
			'Brunette','Brunette',
			'Dark-Eyed',
			'Dark-Haired',
			'Green-Eyed',
			'Platinum Blonde',
			'Raven-Haired',
			'Redhead','Redhead'])
			
class HairColorPOCFemale(WordList):
	def __init__(self):
		super().__init__(['Dark-Haired','Dark-Haired','Dark-Haired',
			'Kinky-Haired'])
		
class HairColorFemale(WordList):
	def __init__(self):
		super().__init__(HairColorWhiteFemale().GetWordList() + HairColorPOCFemale().GetWordList())
		
class SkinHairColorFemale(WordList):
	def __init__(self):
		super().__init__(SkinColorFemale().GetWordList() + HairColorFemale().GetWordList())

# futa			
class SpeciesFemale(WordList):
	def __init__(self):
		super().__init__(['Elf',
			'Fairy',
			'Futa','Futa',
			'Green-Skinned Alien',
			'Mermaid','Mermaid','Mermaid',
			'Nymph',
			'Succubus','Succubus',
			'Vampire',
			'Vampire Queen'])
						
class RaceFemale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'White','White',
			'Asian','Asian',
			'Latina','Latina'])
	
# princess	
class TitlesFemale(WordList):
	def __init__(self):
		super().__init__(['Heiress',
			'Princess','Princess','Princess','Princess','Princess',
			'Queen','Queen'])
		
# Amish maiden, BBW, Farmer's Daughter
class TropesGoodFemale(WordList):
	def __init__(self):
		super().__init__(['All-American Blonde',
			'Amish Maiden','Amish Maiden',
			'Bathing Beauty',
			'BBW','BBW',
			'Beauty',
			'Beauty Queen',
			'Bride',
			'Catholic School Girl',
			'Chaste Nun',
			'Cheer Squad Captain',
			'Damsel',
			'Farmer\'s Daughter',
			'Hippy Chick',
			'HuCow',
			'Kitten',
			'Pastor\'s Wife',
			'Pixie',
			'Princess',
			'Prom Queen',
			'Schoolgirl',
			'Single Mom',
			'Slave Girl',
			'Small-Town Girl',
			'Snow Bunny',
			'Soccer Mom',
			'Southern Belle',
			'Tomboy',
			'Virgin','Virgin','Virgin'])
		
# bad girl, bimbo, brat
class TropesBadFemale(WordList):
	def __init__(self):
		super().__init__(['Bad Girl',
			'Bad Girl',
			'Beach Bunny',
			'Bitch',
			'Brat',
			'Anal Bimbo',
			'Bimbo','Bimbo',
			'Cougar',
			'Naughty Brat',
			'Femme Fatale',
			'Goth Girl',
			'Harem Princess',
			'Hotwife','Hotwife',
			'HuCow',
			'Sex Kitten',
			'Lesbian',
			'MILF','MILF','MILF',
			'Nymphomaniac','Nymphomaniac',
			'Party Girl',
			'Pregnant Stripper',
			'Rebellious Teen',
			'Rich Bitch',
			'Single Mom Stripper',
			'Slut',
			'Sorority Girl',
			'Spoiled Bitch',
			'Stripper',
			'Submissive',
			'Tease',
			'Valley Girl',
			'Witch'])
			
class TropesFemale(WordList):
	def __init__(self):
		super().__init__(TropesGoodFemale().List + TropesBadFemale().List)	
		
class LesFemaleAdj(WordList):
	def __init__(self):
		super().__init__(['Androgynous','Androgynous',
			'Bicurious',
			'Butch','Butch','Butch',
			'Closeted','Closeted',
			'Femme','Femme','Femme',
			'Flannel-Wearing',
			'Freaky',
			'Gold Star',
			'High Femme',
			'Masculine',
			'Out-of-the-Closet',
			'Pillow Princess',
			'S&M',
			'Switch'])
			
class LesFemaleNoun(WordList):
	def __init__(self):
		super().__init__(['Baby Dyke',
			'Bean Flicker',
			'Boi',
			'Bull Dyke','Bull Dyke',
			'Celesbian',
			'Chapstick Lesbian',
			'Diesel Dyke',
			'Dyke','Dyke','Dyke',
			'Lesbo','Lesbo',
			'Lezzie','Lezzie',
			'Lipstick Lesbian',
			'Muff Diver','Muff Diver',
			'Pillow Princess',
			'Rug Muncher',
			'Stud'])			


class GenModMale(WordList):
	def __init__(self):
		super().__init__(['Experienced',
			'Heavily-Tattooed',
			'Highly-Eligible',
			'Horny',
			'Masked',
			'Mysterious',
			'Naked',
			'Nude',
			'Oiled-Up',
			'Tattooed',
			'Sexy',	
			'Shameless',
			'Studly',
			'Wanton'])
		
class AttitudeMale(WordList):
	def __init__(self):
		super().__init__(['Brash',
			'Brazen',
			'Brooding',
			'Charming',
			'Cocky','Cocky',
			'Dapper',
			'Devil-May-Care',
			'Dominant',
			'Disciplined',
			'Eager',
			'Fashionable',
			'Foxy',
			'Frisky',
			'Gentlemanly',
			'Graying',
			'Gruff',
			'Hard-Drinking',
			'Hardened',
			'Kinky',
			'Lustful',
			'Naughty',
			'Powerful',
			'Rakish',
			'Randy',
			'Raunchy',
			'Rebellious',
			'Renegade',
			'Roguish',
			'Savage',
			'Seductive',
			'Sensitive',
			'Sensual',
			'Slick',
			'Sly',
			'Smooth',
			'Stern',
			'Stylish',
			'Suave','Suave',
			'Thrill-Seeking',
			'Urbane',
			'Wicked'])
						
class ClothesMale(WordList):
	def __init__(self):
		super().__init__(['Black Leather-Wearing',
			'Business Casual',
			'Dark-Suited',
			'Naked',
			'Oiled-Up',
			'Leather-Jacketed',
			'Pantsless',
			'Shirtless',
			'Thong-Wearing',
			'Tuxedoed',
			'Uniformed',
			'Well-Dressed'])
		
class PhysCharMale(WordList):
	def __init__(self):
		super().__init__(['Athletic',
			'Bald','Bald',
			'Balding',
			'Bearded',
			'Beefcake',
			'Beefy','Beefy',
			'Big','Big',
			'Brawny',
			'Buff',
			'Burly',
			'Chiseled',
			'Clean-Cut',
			'Clean-Shaven',
			'Craggy',
			'Dad-Bod',
			'Fit',
			'Giant',
			'Hairy','Hairy',
			'Handsome','Handsome',
			'Hulking',
			'Hunky',
			'Husky',
			'Lanky',
			'Muscular','Muscular',
			'Mustachioed',
			'Rangy',
			'Sexy',			
			'Shape-Shifting',
			'Strapping',
			'Strong',
			'Tall',
			'Ugly'])
			
class DickCharMale(WordList):
	def __init__(self):
		super().__init__(['Donkey-Dicked',
			'Engorged',
			'Erect',
			'Fully Erect',
			'Girthy',
			'Hard',
			'Horse-Cock',
			'Hugely Erect',
			'Hung','Hung',
			'Massively Erect',
			'Rock-Hard',
			'Throbbing',
			'Visibly Aroused',
			'Visibly Erect',
			'Well-Hung','Well-Hung',
			'Well-Endowed','Well-Endowed',
			'Virile'])

class TypeModMale(WordList):
	def __init__(self):
		super().__init__(['Barbarian',
			'BDSM',
			'Heart-Throb',
			'Hipster',
			'Manly',
			'Millennial',
			'Mysterious',
			'Naked',
			'Nudist',
			'Playboy',
			'Rebel',
			'Sex Addict',
			'Shirtless',
			'Stay-at-Home',	
			'Studly',
			'Taboo',
			'S.W.A.T. Team',
			'Vegan','Vegan',
			'Veteran',
			'Wealthy','Wealthy','Wealthy'])

class HairColorMale(WordList):
	def __init__(self):
		super().__init__(['Black-Bearded',
			'Blonde','Blonde',
			'Curly-Haired',
			'Graying',
			'Red-Headed','Red-Headed',
			'Brown-Haired'])
			
class SkinColorPOCMale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'Copper-Skinned',
			'Dark-Skinned',
			'Ebony'])
			
class SkinColorWhiteMale(WordList):
	def __init__(self):
		super().__init__(['Bronzed','Bronzed',
			'Copper-Skinned',
			'Pale',
			'Tanned','Tanned','Tanned'])

class SkinColorMale(WordList):
	def __init__(self):
		super().__init__(SkinColorPOCMale().GetWordList() + SkinColorWhiteMale().GetWordList())
			
class SkinHairColorMale(WordList):
	def __init__(self):
		super().__init__(SkinColorMale().GetWordList() + HairColorMale().GetWordList())
			
class AgeMaleAdj(WordList):
	def __init__(self):
		super().__init__(['College',
			'Older','Older','Older','Older',
			'Mature','Mature',
			'Middle-Aged','Middle-Aged',
			'Teenage',
			'Young','Young'])

class MaritalStatusMale(WordList):
	def __init__(self):
		super().__init__(['Bachelor',
			'Divorced',
			'Married','Married','Married','Married',
			'Single','Single','Single',
			'Widowed','Widowed'])
		
class NationMale(WordList):
	def __init__(self):
		super().__init__(['All-American',
			'Australian',
			'British',
			'French','French',
			'Greek',
			'Highlander','Highlander',
			'Irish',
			'Italian','Italian',
			'Japanese',
			'Latino','Latino',
			'Norwegian',
			'Scottish','Scottish',
			'Space',
			'Spanish'])
			
class NationNounMale(WordList):
	def __init__(self):
		super().__init__(['All-American Guy',
			'African Man',
			'Arabic Man',
			'Australian',
			'Brit',
			'Frenchman','Frenchman',
			'Greek',
			'Highlander','Highlander',
			'Irishman',
			'Italian','Italian',
			'Japanese Man',
			'Latino','Latino',
			'Norwegian',
			'Scotsman','Scotsman',
			'Space Man',
			'Spanish Lothario'])
		
class ProfBlueCollarMale(WordList):
	def __init__(self):
		super().__init__(['Baggage Handler',
			'Carnie',
			'Cattle Wrangler',
			'Coal Miner',
			'Construction Worker',
			'Cop',
			'Cowboy',
			'Farmer',
			'Fire Fighter',
			'Garbage Man',
			'Gym Coach',
			'Long Haul Trucker',
			'Lumberjack',
			'Mailman',
			'Male Nurse',
			'Mechanic',
			'Pizza Delivery Guy',
			'Plumber',
			'Postman',
			'Roadie',
			'Sailor',
			'Tattoo Artist',
			'Trucker'])

class ProfWhiteCollarMale(WordList):
	def __init__(self):
		super().__init__(['Airline Pilot',
			'Architect',
			'Artist',
			'Attorney',
			'Brain Surgeon',
			'Business Man', 'Business Man',
			'Chef',
			'Classical Violinist',
			'Doctor','Doctor',
			'Engineer',
			'Fashion Photographer',
			'FBI Agent',
			'Fifth-grade Teacher',
			'Frat Boy',
			'Gynecologist',
			'Heart Surgeon',
			'High-School Teacher',
			'Investment Banker',
			'Lawyer',
			'Musician',
			'Minister',
			'Neurosurgeon',
			'Personal Trainer',
			'Plastic Surgeon',
			'Preacher',
			'Priest',
			'Professor',
			'Psychiatrist',
			'Rocket Scientist',
			'Surgeon',
			'Stockbroker',
			'Writer'])
			
class ProfFantasyMale(WordList):
	def __init__(self):
		super().__init__(['Assassin',	
			'Baker',
			'Blacksmith',
			'Butler',
			'Farmer',
			'Gladiator',
			'Huntsman',
			'Knight',
			'Ninja',
			'Peasant',
			'Pirate',
			'Pirate Captain',
			'Samurai',
			'Stable Boy'])
			
class ProfAthleteMale(WordList):
	def __init__(self):
		super().__init__(['Athlete',	
			'Body Builder',
			'Bodyguard',
			'Bouncer',
			'Boxer',
			'Bull Rider',
			'Defensive Lineman',
			'Dive Instructor',
			'Olympic Gold Medalist',
			'Male Gymnast',
			'MMA Fighter',
			'Pro Basketball Player',
			'Pro Footballer',
			'Pro Soccer Player',
			'Quarterback',
			'Rodeo Clown',
			'Sumo Wrestler',
			'Tennis Coach'])

class ProfRockstarMale(WordList):
	def __init__(self):
		super().__init__(['Astronaut',
			'Author',
			'Chippendales Dancer',
			'CIA Agent',
			'Detective',
			'DJ',
			'Dom',
			'Fighter Pilot','Fighter Pilot',
			'Green Beret',
			'Gunslinger',
			'Hitman',
			'Killer-for-Hire',
			'Lifeguard',
			'Luchador',
			'Outlaw',
			'Male Escort',
			'Male Masseuse',
			'Male Model',
			'Male Stripper',
			'Matador',
			'MI5 Agent',
			'Mossad Agent',
			'Naval Officer',
			'Navy Seal',
			'N.Y.P.D. Officer',
			'Photographer',
			'Private Eye',
			'Rancher',
			'Rock Guitarist',
			'Secret Agent',
			'Secret Service Agent',
			'Sheriff',
			'Snowboarder',
			'Spy',
			'Stand-up Comedian',
			'Stuntman',
			'Surfer',
			'Undercover Cop'])
	
class ProfMale(WordList):
	def __init__(self):
		super().__init__(ProfBlueCollarMale().GetWordList() + 
						 ProfWhiteCollarMale().GetWordList() +
						 ProfAthleteMale().GetWordList() +
						 ProfFantasyMale().GetWordList() +
						 ProfRockstarMale().GetWordList())
						 
class ProfNormalMale(WordList):
	def __init__(self):
		super().__init__(ProfBlueCollarMale().GetWordList() + 
						 ProfWhiteCollarMale().GetWordList())

class ProfAspirationalMale(WordList):
	def __init__(self):
		super().__init__(ProfAthleteMale().GetWordList() + 
						 ProfRockstarMale().GetWordList())

class RaceMale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'White','White',
			'Asian','Asian',
			'Latino','Latino'])
			
class RelateMale(WordList):
	def __init__(self):
		super().__init__(['Adopted Brother',
			'Brother','Brother',
			'Boyfriend','Boyfriend',
			'Dad','Dad',
			'Father',
			'Father-in-Law',
			'Fiancé',
			'Husband','Husband',
			'Step-Brother',
			'Step-Dad',
			'Widower'])

class SpeciesMale(WordList):
	def __init__(self):
		super().__init__(['Alien',
			'Alpha Wolf',
			'Centaur','Centaur',
			'Cyborg',
			'Demon',
			'Dinosaur','Dinosaur',
			'Dwarf',
			'Gargoyle',
			'Goat-Man',
			'Incubus',
			'Man-o-taur',
			'MANtelope',
			'MANticore',
			'Mer-man','Mer-man',
			'Swamp Creature',
			'Tentacle Monster',
			'Undead',
			'Uniporn',
			'Vampire','Vampire',
			'Were-Horse',
			'Were-Shark',
			'Werewolf','Werewolf',
			'Zombie'])
		
class TitlesMale(WordList):
	def __init__(self):
		super().__init__(['CEO',
			'Count','Count',
			'Duke','Duke',
			'King',
			'Manor Lord', 'Manor Lord',
			'Marquis',
			'Pope',
			'President',
			'Prime Minister',
			'Prince','Prince','Prince',
			'Shah',
			'Sheikh','Sheikh',
			'Sultan',
			])
		
class TropesMale(WordList):
	def __init__(self):
		super().__init__(['Alpha',
			'Alpha Male',
			'Bachelor',
			'Bad Boy',
			'Barbarian',
			'BBC',
			'Biker',
			'Billionaire',
			'Boss',
			'Breeding Stud',
			'Casanova',
			'Criminal',
			'Daddy',
			'Daddy Dom',
			'DILF',
			'Dirty Old Man',
			'Don Juan',
			'Ex-Con',
			'Family Man',
			'Gangsta',
			'Gay-for-Pay Porn Star',
			'Gazillionaire',
			'Gentleman',
			'Ghost',
			'Heart-Breaker',
			'Hipster',
			'Hunk',
			'Jock',
			'Knight',
			'Ladies Man',
			'Ladykiller',
			'Millionaire',
			'Mob Boss',
			'Mountain Man',
			'Multi-Millionaire',
			'Older Man',
			'Playboy',
			'Playboy Billionaire',
			'Porn Star',
			'Prince Charming',
			'Rock Star',
			'Scoundrel',
			'Serial Killer',
			'Sex God',
			'Single Dad',
			'Silver Fox',
			'Smooth Operator',
			'Stallion',
			'Stalker',
			'Stud',
			'Sugar Daddy',
			'Trillionaire',
			'Viking',
			'Voyeur',
			'Warrior'])
			
class TropesWealthyMale(WordList):
	def __init__(self):
		super().__init__(['Billionaire',
			'Gazillionaire',
			'Millionaire',
			'Multi-Billionaire',
			'Multi-Millionaire',
			'Playboy',
			'Playboy Billionaire',
			'Trillionaire'
			])

class GangsMaleSingular(WordList):
	def __init__(self):
		super().__init__(['Barbarian Horde',
			'Basketball Team',
			'Biker Gang',
			'Billionaires Club',
			'Men\'s Locker Room',
			'Boy\'s School',
			'Chain Gang',
			'Football Team',
			'Goblin Horde',
			'Herd of Centaurs',
			'Hockey Team',
			'Identical Twin Brothers',
			'Men\'s Volleyball Team',
			'Mongol Horde',
			'Orc Horde',
			'Police Force',
			'Rock Band',
			'Rugby Team',
			'S.W.A.T. Team',
			'Street Gang',
			'Viking Horde',
			'Vampire Coven',
			'Werewolf Pack'])
			

class GangsMalePlural(WordList):
	def __init__(self):
		super().__init__(['Barbarians',
			'Baby Daddies',
			'Bandits',
			'Brothers',
			'Businessmen',
			'Carnies',
			'Chippendales Dancers',
			'Coal Miners',
			'Construction Workers',
			'Cops',
			'Cowboys',
			'DILFs',
			'Dwarves',
			'Firemen',
			'Gangstas',
			'Goat Men',
			'Knights of the Round Table',
			'Long Haul Truckers',
			'Luchadors',
			'Men at the Gym',
			'Men of Kappa Omega Kappa',
			'Mer-men',
			'Mountain Men',
			'Navy Seals',
			'Pirates',
			'Pro Wrestlers',
			'Roadies',
			'Men of Seal Team Six',
			'Scottsmen',
			'Sperm Donors',
			'Sumo Wrestlers',
			'Truckers',
			'Varsity Athletes'])
		
class GangsMale(WordList):
	def __init__(self):
		super().__init__(GangsMaleSingular().GetWordList() + GangsMalePlural().GetWordList())
			
class GayMaleAdj(WordList):
	def __init__(self):
		super().__init__(['Androgynous',
			'Bareback',
			'Bent',
			'Bicurious',
			'Bisexual',
			'Butch',
			'Camp',
			'Closeted',
			'Cross-Dressing',
			'Drag',
			'Discrete',
			'Dominant',
			'Effeminate',
			'Feminine',
			'Flamboyant','Flamboyant','Flamboyant',
			'Flaming',
			'Fruity',
			'Gay','Gay','Gay',
			'Gay-for-Pay',
			'Gaysian',
			'Gender-fluid',
			'Gender-queer',
			'HIV Postive',
			'Macho','Macho',
			'Out-of-the-Closet',
			'Rough Trade',
			'S&M',
			'Submissive',
			'Trans'
			])
			
class GayMaleNoun(WordList):
	def __init__(self):
		super().__init__(['Anal Astronaut',
			'Auntie',
			'Back-Door Bandit',
			'Bear','Bear','Bear',
			'Beefcake',
			'Bottom',
			'Boy Toy',
			'Bronco',
			'Butt Pirate',
			'Cub',
			'Daddy','Daddy',
			'DILF',
			'Drag Queen','Drag Queen',
			'Fairy',
			'Flamer',
			'Gay',
			'Gaysian',
			'Gym Bunny',
			'Knob Jockey',
			'Leather Daddy',
			'Muscle Mary',
			'Nancy',
			'Power Bottom',
			'Pillow Princess',
			'Queen','Queen','Queen','Queen',
			'Queer',
			'Stud',
			'Top',
			'Twink','Twink','Twink',
			'Wolf'])

class SubtitleCoda(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Adventure', 
			'Affair','Affair',
			'Encounter',
			'Liaison',
			'Love Story',
			'Romance','Romance','Romance',
			'Rendezvous',
			'Story'])
			
class NiceGirlGoodAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(["Amish",
						  "Bashful",
						  "Chaste",
						  "Conservative",
						  "Christian","Christian",
						  "Demure",
						  "Innocent",
						  "Modest",
						  "Mormon",
						  "Sheltered",
						  "Shy",
						  "Tender",
						  "Wholesome",
						  "Uptight",
						  "Virgin"])

class NiceGirlAdjs(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(["All-American",
						  "Asian",
						  "Athletic",
						  "BBW",
						  "Blonde",
						  "British",
						  "Brunette",
						  "Cheerleader",
						  "Dark-Skinned",
						  "Curvy",
						  "Ebony",
						  "Fashionable",
						  "Geeky",
						  "Gymnast",
						  "Introverted",
						  "Irish",
						  "Lactating",
						  "Mature",
						  "Nerdy",
						  "Pale",
						  "Petite",
						  "Pregnant",
						  "Redheaded",
						  "Spanish"])

class NiceGirlNouns(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(["Babysitter",
						  "Bride",
						  "Fiancé",
						  "Girlfriend",
						  "Governess",
						  "House Maid",
						  "Housewife",
						  "Librarian",
						  "Maid",
						  "Piano Teacher",
						  "Teacher",
						  "Secretary",
						  "Schoolgirl",
						  "Small-Town Girl",
						  "Stay-at-Home Wife",
						  "Step-Daughter",
						  "Step-Mom",
						  "Step-Sister",
						  "Wife"])

class NiceGirl():
	def __init__(self, NotList = None):
		if NotList == None:
			NotList = []
			
		sNiceAdj1 = NiceGirlGoodAdjs().GetWord(NotList = NotList)
		sNiceGirl = sNiceAdj1 + " "
		if CoinFlip():
			sNiceGirl += NiceGirlGoodAdjs().GetWord(NotList = [sNiceAdj1] + NotList) + " "
		if CoinFlip():
			sNiceGirl += NiceGirlAdjs().GetWord(NotList = NotList) + " "
		sNiceGirl += NiceGirlNouns().GetWord(NotList = NotList)
		
		self.Desc = sNiceGirl 
			
			
