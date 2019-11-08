#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Misc module

from util import *

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
			'NaNoWriMo','NaNoWriMo',
			'naughty',
			'naughtynovember','naughtynovember','naughtynovember',
			'naughtyreads',
			'nnn','nnn','nnn',
			'nofapnovember','nofapnovember',
			'nonutnovember','nonutnovember','nonutnovember',
			'nsfw','nsfw',
			'PleaseRT',
			'romance',
			'romanceauthor',
			'romancereaders',
			'sexybot',
			'smut',
			'sorrynotsorry','sorrynotsorry',
			'ssrtg',
			'steamy',
			'ThanksIHateIt','ThanksIHateIt',
			'twitterbot','twitterbot',
			'wprtg',
			'writingcommunity',
			'writingprompt'])
			
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
			
class DullPlaces(WordList):
	def __init__(self):
		super().__init__(['Albuquerque',
			'Ann Arbor',
			'Billings',
			'Blackpool',
			'Calgary',
			'Cardiff',
			'Cedar Rapids',
			'Dayton',
			'Deltona',
			'Derby',
			'Des Moines',
			'Doncaster',
			'Duluth',
			'East Lansing',
			'El Paso',
			'Elk Grove',
			'Essex',
			'Fargo',
			'Flagstaff',
			'Fort Wayne',
			'Fresno',
			'Hull',
			'Ithaca',
			'Modesto',
			'Norwich',
			'Pensacola',
			'Peoria',
			'Plano',
			'Poole',
			'Portsmouth',
			'Provo',
			'Reno',
			'Santa Fe',
			'Scranton',
			'Shreveport',
			'Sioux Falls',
			'South Bend',
			'Southampton',
			'Spokane',
			'Sunnyvale',
			'Sussex',
			'Syracuse',
			'Toledo',
			'Tulsa',
			'Tuscaloosa',
			'West Bromwich',
			'Wichita',
			'Wolverhampton'])
			
class DullJobsMale(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(["Accountant",
						  "Amazon delivery guy",
						  "Graphic Designer",
						  "Bank Manager",
						  "Fry Cook",
						  "Golf Caddy",
						  "Drywall Installer",
						  "Physical Therapist",
						  "Dentist",
						  "Building Inspector",
						  "Used Car Salesman",
						  "Mortician",
						  "Drummer",
						  "Opthamologist",
						  "IT Technician",
						  "Male Nurse",
						  "Cat Sitter",
						  "Dog Walker",
						  "Wedding Photographer",
						  "Warehouse Manager",
						  "SCUBA Supplier",
						  "8th Grade Teacher",
						  "College Adjunct",
						  "Business Analyst",
						  "Call Center Employee",
						  "Grad Student",
						  "Beekeeper",
						  "Piano Tuner",
						  "9th Grade Teacher",
						  "Zoology Professor",
						  "Retiree",
						  "US Army Ranger",
						  "Auto Mechanic",
						  "HVAC Technician",
						  "Zoomba Instructor",
						  "Life Coach",
						  "Vice Principal",
						  "Truck Driver",
						  "Materials Engineer",
						  "Uber Driver",
						  "Cable Installer",
						  "Bouncer",
						  "Zamboni Driver",
						  "Windshield Installer",
						  "Tiler Grouter",
						  "Forklift Operator",
						  "Air Traffic Controller",
						  "Manhole inspector"])
			
class DullJobsFemale(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(["Bank Teller",
						  "Gourmet Chef",
						  "Physical Therapist",
						  "Nurse",
						  "Dental Hygenist",
						  "Receptionist",
						  "English Teacher",
						  "Spanish Teacher",
						  "Lexicographer",
						  "Dermatologist",
						  "Graphic Designer",
						  "Church Pianist",
						  "3rd Grade Teacher",
						  "Tax Accountant",
						  "Cat Sitter",
						  "Dog Walker",
						  "Pigeon Trainer",
						  "Intern",
						  "Grad Student",
						  "Beekeeper",
						  "Produce Buyer",
						  "Electrical Engineer",
						  "Mommy Blogger",
						  "Stay-at-Home Mom",
						  "Guidance Counselor",
						  "Yoga Instructor",
						  "Lyft Driver",
						  "Librarian",
						  "Podcast Host",
						  "Meter Maid",
						  "Speech Therapist",
						  "Beautician",
						  "Manicurist",
						  "Wedding Planner",
						  "Hostess",
						  "Kindergarten Teacher",
						  "Tutor",
						  "House Maid",
						  "Funeral Planner",
						  "Professional Hand Model",
						  "Sculptor",
						  "Car Wash Manager",
						  "Loan Officer"])
		
class BookVerbsBy(WordList):
	WordHistoryQ = HistoryQ(3)
	
	def __init__(self):
		super().__init__(['Anally Deflowered',
			'Anally Deflowered in Public',
			'Banged',
			'Bared',
			'Beaten',
			'Beaten with a Belt',
			'Boned',
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
			'Cream-Pied',
			'Cuddled',
			'Cuddled Hard',
			'Deflowered','Deflowered',
			'Deflowered in Public',
			'Dominated',
			'Dominated in the Dungeon',
			'Drilled',
			'Dry-Humped',
			'Enslaved','Enslaved',
			'Exposed in Public',
			'Fisted',
			'Humped',
			'Hunted For Food',
			'Impregnated','Impregnated',
			'Imprisoned in the Sex Dungeon',
			'Knocked Up','Knocked Up',
			'Milked',
			'Mind-Controlled',
			'Motor-Boated',
			'Mounted',
			'Mounted Bareback',
			'Nailed',
			'Paddled',
			'Pleasured',
			'Pleasured in Public',
			'Plowed',
			'Porked',
			'Punished',
			'Punished in Public',
			'Ravished','Ravished',
			'Reamed',
			'Ridden',
			'Ridden Bareback',
			'Rimmed',
			'Satisfied',
			'Screwed',
			'Seduced',
			'Sexually Harrassed At My Workplace',
			'Shaved',
			'Sixty-Nined',
			'Sold',
			'Sold',
			'Spanked',
			'Spanked in Public',
			'Spanked with a Belt',
			'Shagged',
			'Shaved',
			'Stripped',
			'Stripped in Public',
			'Stuffed',
			'Taken','Taken',
			'Taken From Behind',
			'Taken Hard',
			'Taken Hard in Public',
			'Taken in Public',
			'Tea-Bagged',
			'Tied to the Bed',
			'Tied Up',
			'Tied Up in the Basement',
			'Tempted',
			'Secretly Watched',
			'Used as a Sex Doll',
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
			'Claiming','Claiming',
			'Controlling',
			'Deflowering', 
			'Dominating',
			'Dry Humping',
			'Eating Out',
			'Enslaving',
			'Feeling Up',
			'Fingering',
			'Fisting',
			'Hooking Up With',
			'Hot-Dogging',
			'Hypnotizing',
			'Going Down On',
			'Impregnating',
			'Knocking Up',
			'Licking',
			'Massaging',
			'Milking',
			'Mind Controlling',
			'Motor-Boating','Motor-Boating',
			'Mounting',
			'Paddling',
			'Playing With',
			'Pleasuring',
			'Ravishing','Ravishing',
			'Raw Dogging',
			'Riding',
			'Rimming',
			'Sixty-nining',
			'Sleeping With','Sleeping With',
			'Shaving',
			'Showering With','Showering With','Showering With',
			'Spanking',
			'Spooning','Spooning With',
			'Stripping',
			'Taking',
			'Tasting',
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
			
