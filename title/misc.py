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
			'Conservative','Conservative',
			'Demure',
			'Ditzy',
			'Eager',
			'Flirty',
			'Innocent','Innocent','Innocent',
			'Modest','Modest',
			'Perky','Perky',
			'Sexy',
			'Sheltered',
			'Shy','Shy',
			'Sparkling',
			'Spirited',
			'Sporty',
			'Straight',
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
			'Nympho','Nympho',
			'Perverted',
			'Promiscuous',
			'Revealing',
			'Risqué',
			'Sadistic',
			'Salacious',
			'Sassy','Sassy',
			'Saucy',
			'Shameless','Shameless',
			'Slutty','Slutty','Slutty',
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
			'Korean',
			'Latina',
			'Mexican',
			'Mormon',
			'Polynesian',
			'Russian',
			'Small-Town',
			'Swedish'])
		
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
			'Naked',
			'Nubile',
			'Nude',
			'Oiled Up',
			'Petite',
			'Plump',
			'Ripe',
			'Round-Bottomed',
			'Rubenesque',
			'Shapely',
			'Shaved Bare',
			'Skinny',
			'Slender',
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
		super().__init__(['Airline Stewardess',
			'Babysitter',
			'Ballerina',
			'Barista',
			'Cheerleader',
			'Co-ed',
			'College Girl',
			'Fashion Model',
			'Flight Attendant',
			'Gymnast',
			'House Maid',
			'Housewife',
			'Intern',
			'Librarian',
			'Masseuse',	
			'Maid',
			'Milk Maid',
			'Mommy Blogger',
			'Nanny',
			'Nun',
			'Nurse','Nurse',
			'Nursing Student',
			'Secretary','Secretary',
			'Servant',
			'Schoolgirl',
			'School-marm',
			'Stay-at-Home Mom',
			'Supermodel',
			'Teacher',
			'Waitress',
			'Yoga Instructor'])
			
# porn star, call girl, escort, etc
class ProfBadFemale(WordList):
	def __init__(self):
		super().__init__(['Amateur Porn Star',
			'Anal Whore',
			'Bikini Model',
			'Call-Girl','Call-Girl',
			'Club Dancer',
			'Cheerleader',
			'Dominatrix',
			'Escort',
			'Fashion Model',
			'Fetish Model',
			'French Maid',
			'Gymnast',
			'Hooter\'s Waitress',
			'Housewife',
			'Lingerie Model',
			'Masseuse',	
			'Nun',
			'Nurse',
			'Penthouse Pet',
			'Playboy Centerfold',
			'Pole Dancer',
			'Porn Star',
			'Secretary',
			'Stripper','Stripper',
			'Supermodel',
			'Whore'])
			
class ProfFemale(WordList):
	def __init__(self):
		super().__init__(ProfGoodFemale().List + ProfBadFemale().List)
		
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
	
# black, ebony
class SkinHairColorFemale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'Ebony','Ebony',
			'Pale',
			'Blonde','Blonde',
			'Blue-Eyed','Blue-Eyed',
			'Bronzed','Bronzed',
			'Brunette','Brunette',
			'Dark-Eyed',
			'Dark-Haired',
			'Dark-Skinned',
			'Green-Eyed',
			'Redhead','Redhead',
			'Tanned','Tanned'])

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
			'Butch','Butch','Butch',
			'Closeted','Closeted',
			'Femme','Femme','Femme',
			'Flannel-Wearing',
			'Freaky',
			'Gold Star',
			'High Femme',
			'Manly',
			'Masculine',
			'Out',
			'Pillow Princess',
			'S&M',
			'Switch'])
			
class LesFemaleNoun(WordList):
	def __init__(self):
		super().__init__(['Bean Flicker',
			'Bull Dyke','Bull Dyke',
			'Celesbian',
			'Diesel Dyke',
			'Dyke','Dyke','Dyke',
			'Lesbo','Lesbo',
			'Lezzie','Lezzie',
			'Lipstick Lesbian',
			'Muff Diver','Muff Diver',
			'Pillow Princess',
			'Rug Muncher',
			'Stud',
			'U-Haul Lesbian'])
			
	
class AgeMaleAdj(WordList):
	def __init__(self):
		super().__init__(['College',
			'Older','Older','Older',
			'Mature',
			'Middle-Aged',
			'Teenage',
			'Young'])
		
class AttitudeMale(WordList):
	def __init__(self):
		super().__init__(['Brash',
			'Brazen',
			'Brooding',
			'Charming',
			'Cocky','Cocky',
			'Clever',
			'Devil-May-Care',
			'Dominant',
			'Eager',
			'Experienced','Experienced',
			'Fashionable',
			'Foxy',
			'Frisky',
			'Gentlemanly',
			'Gruff',
			'Hard-Drinking',
			'Hardened',
			'Highly Eligible',
			'Horny',
			'Kinky',
			'Lustful',
			'Naughty',
			'Powerful',
			'Rakish',
			'Randy',
			'Raunchy',
			'Rebel',
			'Renegade',
			'Roguish',
			'Savage',
			'Seductive',
			'Sensitive',
			'Sensual',
			'Shameless',
			'Slick',
			'Sly',
			'Smooth',
			'Suave','Suave',
			'Thrill-Seeking',
			'Wanton',
			'Wicked',
			'Virile'])
		
class GenModMale(WordList):
	def __init__(self):
		super().__init__(['Barbarian',
			'BDSM',
			'Dapper',
			'Heart-Throb',
			'Heavily Tattooed',
			'Manly',
			'Masked',
			'Massive',
			'Mysterious',
			'Naked',
			'Nudist',
			'Pantsless',
			'Tattooed',
			'Secret',
			'Sex Addict',
			'Shirtless',
			'Stay-at-Home',	
			'Studly',
			'Stylish',
			'Taboo',
			'S.W.A.T. Team',
			'Vegan',
			'Virile',
			'Wealthy'])
		
class MaritalStatusMale(WordList):
	def __init__(self):
		super().__init__(['Divorced',
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
		
class PhysCharMale(WordList):
	def __init__(self):
		super().__init__(['Athletic',
			'Bald','Bald',
			'Balding',
			'Bare-Chested',
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
			'Muscled',
			'Muscular','Muscular',
			'Mustachioed',
			'Sexy',			
			'Shape-Shifting',
			'Strapping',
			'Strong',
			'Tall',
			'Tattooed',
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
		
class ProfMale(WordList):
	def __init__(self):
		super().__init__(['Airline Pilot',
			'Artist',
			'Astronaut',
			'Assassin',
			'Athlete',
			'Attorney',
			'Blacksmith',
			'Body Builder',
			'Bodyguard',
			'Boxer',
			'Brain Surgeon',
			'Bull Rider',
			'Business Man', 'Business Man',
			'Camp Counselor',
			'Chippendales Dancer',
			'CIA Agent',
			'Coal Miner',
			'Construction Worker',
			'Cop',
			'Cowboy',
			'Defensive Lineman',
			'Doctor',
			'Dom',
			'Fashion Photographer',
			'FBI Agent',
			'Fighter Pilot','Fighter Pilot',
			'Fire Fighter',
			'Frat Boy',
			'Gladiator',
			'Green Beret',
			'Gunslinger',
			'Gym Coach',
			'Heart Surgeon',
			'Hitman',
			'Investment Banker',
			'Killer-for-Hire',
			'Lawyer',
			'Long Haul Trucker',
			'Luchador',
			'Lumberjack',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Model',
			'Male Nurse',
			'Male Stripper',
			'Matador',
			'MI5 Agent',
			'Minister',
			'Mossad Agent',
			'MMA Fighter',
			'Naval Officer',
			'Navy Seal',
			'Personal Trainer',
			'Pirate',
			'Pirate Captain',
			'Preacher',
			'Priest',
			'Private Eye',
			'Professor',
			'Quarterback',
			'Rock Guitarist',
			'Rodeo Clown',
			'Sailor',
			'Secret Agent',
			'Secret Service Agent',
			'Sheriff',
			'Snowboarder',
			'Spy',
			'Stockbroker',
			'Stuntman',
			'Sumo Wrestler',
			'Surfer',
			'Surgeon',
			'Tattoo Artist',
			'Trucker',
			'Undercover Cop'])
		
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
		
class SkinHairColorMale(WordList):
	def __init__(self):
		super().__init__(['Black','Black','Black',
			'Black-Bearded',
			'Blonde','Blonde',
			'Bronzed',
			'Copper-Skinned',
			'Curly-Haired',
			'Ebony',
			'Red-Headed','Red-Headed',
			'Tanned','Tanned'])
		
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
			
class TropesMale(WordList):
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
			
class GangsMale(WordList):
	def __init__(self):
		super().__init__(['Baby Daddies',
			'Bandits',
			'Barbarian Horde',
			'Barbarians',
			'Basketball Team',
			'Biker Gang',
			'Billionaires Club',
			'Men\'s Locker Room',
			'Boy\'s School',
			'Brothers',
			'Businessmen',
			'Carnies',
			'Chain Gang',
			'Chippendales Dancers',
			'Coal Miners',
			'Construction Workers',
			'Cops',
			'Cowboys',
			'DILFs',
			'Dwarves',
			'Firemen',
			'Football Team',
			'Gangstas',
			'Goat Men',
			'Goblin Horde',
			'Herd of Centaurs',
			'Hockey Team',
			'Identical Twin Brothers',
			'Knights of the Round Table',
			'Lesbian Harem',
			'Long Haul Truckers',
			'Luchadors',
			'Men at the Gym',
			'Men of Kappa Omega Kappa',
			'Men\'s Volleyball Team',
			'Mer-men',
			'Mongol Horde',
			'Mountain Men',
			'Navy Seals',
			'Orc Horde',
			'Pirates',
			'Police Force',
			'Pro Wrestlers',
			'Roadies',
			'Rock Band',
			'Rugby Team',
			'Men of Seal Team Six',
			'S.W.A.T. Team',
			'Scottsmen',
			'Sperm Donors',
			'Street Gang',
			'Sumo Wrestlers',
			'Truckers',
			'Viking Horde',
			'Vampire Coven',
			'Varsity Athletes',
			'Werewolf Pack'])
			
class GayMaleAdj(WordList):
	def __init__(self):
		super().__init__(['Bent',
			'Camp',
			'Closeted',
			'Drag Queen',
			'Discrete',
			'Effeminate',
			'Feminine',
			'Flamboyant',
			'Flaming',
			'Gay','Gay','Gay',
			'Gay-for-Pay',
			'Gaysian',
			'HIV Postive',
			'Macho',
			'Out',
			'S&M',])
			
class GayMaleNoun(WordList):
	def __init__(self):
		super().__init__(['Anal Astronaut',
			'Auntie',
			'Back-Door Bandit',
			'Bear','Bear','Bear',
			'Bottom',
			'Boy Toy',
			'Butt Pirate',
			'Cub',
			'Daddy','Daddy',
			'Drag Queen','Drag Queen',
			'Flamer',
			'Gaysian',
			'Gym Bunny',
			'Knob Jockey',
			'Leather Daddy',
			'Muscle Mary',
			'Power Bottom',
			'Princess',
			'Queen','Queen','Queen','Queen',
			'Queer',
			'Sailor',
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
			
			
