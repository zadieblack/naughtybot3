#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

import title.people
import title.verbs
import title.names 

from random import *
from title.util import *
		
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
			'amwriting',
			'bookboost','bookboost',
			#'bitcoin',
			#'blockchain',
			'bot',
			'dirtyreads',
			'eartg',
			'erotic',
			'erotica','erotica',
			'eroticromance',
			'fiftyshades',
			'kink',
			#'litecoin',
			'lovestory',
			'lprtg',
			'mrbrtg',
			'naughty',
			'naughtyreads',
			'nsfw','nsfw',
			'PleaseRT','PleaseRT',
			'romance','romance','romance',
			'romanceauthor',
			'romancereaders',
			'sexybot',
			'smut',
			'sorrynotsorry','sorrynotsorry',
			'ssrtg',
			'twitterbot','twitterbot',
			'wprtg'])
		
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
		
class SexyAdjs(WordList):
	def __init__(self):
		super().__init__(['dirty',
		'erotic',
		'filthy',
		'hot',
		'kinky',
		'naughty',
		'raunchy',
		'sexy',
		'sensual',
		'steamy',
		'taboo'])

class BookSellers(WordList):
	def __init__(self):
		super().__init__(['Apple Books',
			'Amazon',
			'B&N',
			'Kindle Unlimited',
			'Kobo',
			'Radish Fiction',
			'Smashwords',
			'WattPad'])
			
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
			'Chaste',
			'Conservative','Conservative',
			'Demure',
			'Flirty',
			'Innocent','Innocent','Innocent',
			'Modest','Modest',
			'Pure',
			'Sassy','Sassy',
			'Sexy',
			'Sheltered',
			'Shy','Shy',
			'Sporty',
			'Sweet','Sweet',
			'Uptight',
			'Virginal',
			'Virtuous',
			'Vivacious',
			'Wholesome','Wholesome'])
		
# kinky, slutty, etc 
class AttitudeBadFemale(WordList):
	def __init__(self):
		super().__init__(['Brazen',
			'Daring',
			'Desperate',
			'Dirty','Dirty',
			'Dirty-Minded',
			'Foxy',
			'Kinky','Kinky',
			'Lewd',
			'Horny',
			'Naughty','Naughty',
			'Nympho','Nympho',
			'Promiscuous',
			'Revealing',
			'Risqué',
			'Salacious',
			'Shameless','Shameless',
			'Slutty','Slutty','Slutty',
			'Wanton','Wanton',
			'Wicked',
			'Wild','Wild',
			'Willing','Willing',
			'X-Rated'])
			
class AttitudeFemale(WordList):
	def __init__(self):
		super().__init__(AttitudeGoodFemale().List + AttitudeBadFemale().List)		
		
class ClothingFemale(WordList):
	def __init__(self):
		super().__init__(['Bikini Wearing',
			'Braless',
			'G-String',
			'High-Heeled',
			'Latex Wearing',
			'Leather-Clad',
			'Scantily-Clad',
			'Topless'])

class GenModFemale(WordList):
	def __init__(self):
		super().__init__(['Anal','Anal',
		'BDSM','BDSM','BDSM',
		'Erotic',
		'Fetish',
		'Horny',
		'Nudist','Nudist','Nudist',
		'Sex',
		'Taboo','Taboo'])
		
# single, single mom, married, engaged
class MaritalStatusFemale(WordList):
	def __init__(self):
		super().__init__(['Recently-Divorced',
			'Concubine',
			'Married','Married','Married',
			'Single','Single','Single','Single'])

# french, italian, etc
class NationFemale(WordList):
	def __init__(self):
		super().__init__(['Amish','Amish','Amish',
			'Asian','Asian',
			'Brazillian',
			'Christian','Christian','Christian',
			'Country',
			'Czech',
			'French',
			'German',
			'Irish',
			'Latina',
			'Polynesian',
			'Russian',
			'Small-Town',
			'Swedish'])
		
# big-titty, etc
class PhysCharFemale(WordList):
	def __init__(self):
		super().__init__(['Apple-Bottomed',
			'Athletic',
			'Attractive',
			'Beautiful',
			'Big Bottomed',
			'Big Titty',
			'Busty',
			'Buxom',
			'Curvy',
			'Curvaceous',
			'Cute',
			'Flexible',
			'Gorgeous',
			'Hot',
			'Jiggling',
			'Juicy','Juicy',
			'Leggy',
			'Little','Little','Little',
			'Naked',
			'Natural',
			'Nubile',
			'Nude',
			'Petite',
			'Plump',
			'Rubenesque',
			'Shapely',
			'Shaved',
			'Skinny',
			'Slender',
			'Sporty',
			'Statuesque',
			'Supple',
			'Top-Heavy',
			'Unshaven',
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
			'Bikini Model',
			'Bridesmaid',
			'Cheerleader',
			'Co-ed',
			'College Girl',
			'Dancer',
			'Fashion Model',
			'Gymnast',
			'House Maid',
			'Housewife',
			'Flight Attendant',
			'Governess',
			'French Maid',
			'Librarian',
			'Life Drawing Model',
			'Lingerie Model',
			'Masseuse',	
			'Maid',
			'Milk Maid',
			'Nanny',
			'Nun',
			'Nurse','Nurse',
			'Secretary','Secretary',
			'Servant',
			'Schoolgirl',
			'Starlet',
			'Supermodel',
			'Teacher',
			'Waitress'])
			
# porn star, call girl, escort, etc
class ProfBadFemale(WordList):
	def __init__(self):
		super().__init__(['Amateur Porn Star',
			'Anal Whore',
			'Call-Girl','Call-Girl','Call-Girl',
			'Dominatrix',
			'Escort',
			'Fashion Model',
			'Fetish Model',
			'Gymnast',
			'Housewife',
			'Nun',
			'Playboy Centerfold',
			'Porn Star',
			'Slave','Slave','Slave',
			'Stripper','Stripper',
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
		super().__init__(['Cat-Girl', 
			'Green-Skinned Alien',
			'Fairy',
			'Futa','Futa',
			'Mermaid','Mermaid','Mermaid',
			'Nymph',
			'Succubus','Succubus',
			'Vampire Queen','Vampire Queen'])
	
# princess	
class TitlesFemale(WordList):
	def __init__(self):
		super().__init__(['Baroness','Baroness',
			'Duchess','Duchess',
			'Princess','Princess','Princess','Princess','Princess',
			'Queen','Queen','Queen'])
		
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
			'Ice Queen',
			'Innocent Cutie',
			'Damsel',
			'Daddy\'s Girl',
			'Farmer\'s Daughter',
			'Good Christian Girl',
			'Harem Princess',
			'Hippy Chick',
			'HuCow',
			'Kitten',
			'Pastor\'s Wife',
			'Pixie',
			'Princess',
			'Prom Queen','Prom Queen',
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
			'Brat',
			'Anal Bimbo',
			'Bimbo','Bimbo',
			'Cougar',
			'Naughty Brat',
			'Femme Fatale',
			'Goth Girl',
			'Hotwife','Hotwife',
			'Sex Kitten',
			'Lesbian',
			'MILF','MILF','MILF',
			'Nymphomaniac','Nymphomaniac',
			'Party Girl',
			'Pregnant Stripper',
			'Rebellious Teen',
			'Rich Bitch',
			'Single Mom Stripper',
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
			'Bareback',
			'BDSM',
			'Dapper',
			'Gang-Bang',
			'Heart-Throb',
			'Manly',
			'Masked',
			'Mysterious',
			'Nudist',
			'Secret',
			'Sex Addict',
			'Sorcerer',
			'Stay-at-Home',	
			'Studly',
			'Stylish',
			'Taboo',
			'Throbbing',
			'S.W.A.T. Team',
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
			'Bald',
			'Bare-Chested','Bare-Chested',
			'Bearded','Bearded',
			'Beefcake',
			'Beefy','Beefy',
			'Big','Big',
			'Brawny',
			'Buff',
			'Burly',
			'Chiseled',
			'Clean-Cut',
			'Clean-Shaven','Clean-Shaven',
			'Dad-Bod',
			'Fine',
			'Fit',
			'Giant',
			'Girthy',
			'Hairy','Hairy',
			'Handsome','Handsome',
			'Hulking',
			'Hung','Hung',
			'Hunky',
			'Husky',
			'Muscled',
			'Muscular','Muscular',
			'Mustachioed',
			'Naked',
			'Pantsless',
			'Rock-Hard',
			'Sexy',			
			'Shape-Shifting',
			'Strapping',
			'Strong',
			'Tall','Tall',
			'Tattooed',
			'Tough',
			'Visibly Erect',
			'Well-Built',
			'Well-Hung','Well-Hung',
			'Well-Endowed','Well-Endowed'])
		
class ProfMale(WordList):
	def __init__(self):
		super().__init__(['Airline Pilot',
			'Artist',
			'Astronaut',
			'Assassin',
			'Athlete',
			'Attorney',
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
			'Lumberjack',
			'Olympic Gold Medalist',
			'Outlaw',
			'Male Escort',
			'Male Model',
			'Male Stripper',
			'Matador',
			'MI5 Agent',
			'Minister',
			'Mossad Agent',
			'MMA Fighter',
			'Navy Seal',
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
			'Tattoo Artist',
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
			'Dinosaur',
			'Dwarf',
			'Futanari',
			'Gargoyle',
			'Giant',
			'Goat-Man',
			'Incubus',
			'Man-o-taur',
			'MANtelope',
			'MANticore',
			'Mer-man',
			'Swamp Creature',
			'Tentacle Monster',
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
			'Bitcoin Billionaire',
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
			'Hot Professor',
			'Hunk',
			'Jock',
			'Kingpin',
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
			'Sex Warlock',
			'Single Dad',
			'Silver Fox',
			'Smooth Operator',
			'Stallion',
			'Stalker',
			'Stud',
			'Sugar Daddy',
			'Suave Bachelor',
			'Trillionaire',
			'Viking',
			'Voyeur',
			'Warrior'])
			
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
			'Rock Band',
			'Rugby Team',
			'Men of Seal Team Six',
			'S.W.A.T. Team',
			'Scottsmen',
			'Sperm Donors',
			'Street Gang',
			'Sumo Wrestlers',
			'Viking Horde',
			'Vampire Coven',
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

			
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowered',
			'Anally Deflowered in Public',
			'Bared',
			'Beaten',
			'Beaten with a Belt',
			'Bound',
			'Bound in the Dungeon',
			'Bred',
			'Broken',
			'Captured',
			'Caught on Tape',
			'Caught on Video',
			'Claimed','Claimed',
			'Claimed From Behind',
			'Claimed Hard',
			'Claimed in Public',
			'Chained Up',
			'Chained Up in the Sex Dungeon',
			'Chained Up in the Basement',
			'Charmed',
			'Cuddled',
			'Cuddled Hard',
			'Deflowered','Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Dominated in the Dungeon',
			'Enslaved','Enslaved',
			'Exposed in Public',
			'Fisted',
			'Humiliated',
			'Hunted For Food',
			'Hypnotized',
			'Impregnated','Impregnated',
			'Imprisoned in the Sex Dungeon',
			'Knocked Up','Knocked Up',
			'Massaged',
			'Milked',
			'Mind-Controlled',
			'Motor-Boated',
			'Mounted',
			'Mounted Bareback',
			'Paddled',
			'Pleasured','Pleasured',
			'Pleasured in Public',
			'Publically Humiliated',
			'Punished',
			'Punished in Public',
			'Ravished','Ravished',
			'Ridden',
			'Ridden Bareback',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Shaved',
			'Sold',
			'Sold',
			'Spanked',
			'Spanked in Public',
			'Spanked with a Belt',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Taken','Taken',
			'Taken From Behind',
			'Taken Hard',
			'Taken Hard in Public',
			'Taken in Public',
			'Tied to the Bed',
			'Tied Up',
			'Tied Up in the Basement',
			'Tempted',
			'Secretly Watched',
			'Whipped',
			'Whipped in Public'])
			
class BookVerbsTo(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Bared',
				'Bound',
				'Bred',
				'Chained',
				'Enslaved',
				'Gifted',
				'Mated',
				'Sold',
				'Surrendered'])
				
class BookGerunds(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowering',
			'Bedding',
			'Blackmailing',
			'Binding',
			'Breaking',
			'Claiming','Claiming','Claiming',
			'Controlling',
			'Deflowering', 
			'Dominating',
			'Enslaving',
			'Feeling Up',
			'Fingering',
			'Fisting',
			'Hooking Up With',
			'Humiliating',
			'Hypnotizing',
			'Gagging',
			'Going Down On',
			'Impregnating',
			'Knocking Up',
			'Licking',
			'Lusting For',
			'Massaging',
			'Milking',
			'Mind Controlling',
			'Motor-Boating',
			'Mounting',
			'Paddling',
			'Playing With',
			'Pleasuring',
			'Publically Humiliating',
			'Punishing',
			'Ravishing','Ravishing',
			'Raw Dogging',
			'Riding',
			'Rimming',
			'Secretly Watching',
			'Seducing',
			'Sleeping With','Sleeping With',
			'Spanking',
			'Shaving',
			'Showering With',
			'Spooning',
			'Spying On',
			'Stripping',
			'Taking','Taking','Taking',
			'Taming',
			'Tasting',
			'Tempting',
			'Tying Up',
			'Teaching',
			'Undressing',
			'Using',
			'Videoing',
			'Whipping'])
			
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
						  "Pure",
						  "Sheltered",
						  "Shy",
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
	def __init__(self):
		sNiceAdj1 = NiceGirlGoodAdjs().GetWord()
		sNiceGirl = sNiceAdj1 + " "
		if CoinFlip():
			sNiceGirl += NiceGirlGoodAdjs().GetWord(NotList = [sNiceAdj1]) + " "
		if CoinFlip():
			sNiceGirl += NiceGirlAdjs().GetWord() + " "
		sNiceGirl += NiceGirlNouns().GetWord()
		
		self.Desc = sNiceGirl 
			
			
