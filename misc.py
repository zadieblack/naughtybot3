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
               'cantstopwontstop',
               'classy',
               'cunninglinguist',
               'currentlyreading',
               'dirtyreads',
               'eartg',
               'erotic',
               'erotica','erotica',
               'eroticromance',
               'fiftyshades',
               'hurtmedaddy',
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
               'PleaseRT',
               'relatable',
               'romance','romance',
               'romanceauthor','romanceauthor',
               'romancereaders','romancereader',
               'selfcare',
               'sexybot',
               'smut',
               'sorrynotsorry','sorrynotsorry',
               'ssrtg',
               'steamy',
               'ThanksIHateIt','ThanksIHateIt',
               'twitterbot',
               'vintageromance','vintageromance',
               'wprtg',
               'writingcommunity',
               'writingprompt','writingprompt','writingprompt',
               'yesdaddy'])
               
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

class Colors(WordList):
     def __init__(self):
          super().__init__(['Black','Jet Black',
               'Beige',
               'Blue','Dark Blue','Navy Blue','Sky Blue','Baby Blue',
               'Brown','Chocolate Brown',
               'Chartreuse',
               'Coral',
               'Gold',
               'Green','Bright Green','Dark Green','Lime Green',
               'Indigo',
               'Lavendar',
               'Magenta',
               'Maroon',
               'Mauve',
               'Orange','Neon Orange',
               'Peach',
               'Pink','Hot Pink',
               'Purple',
               'Red','Blood Red','Bright Red','Ruby Red',
               'Silver',
               'Tan',
               'Turquoise',
               'Violet',
               'Yellow','Bright Yellow','Canary Yellow','Lemon Yellow',
               'White','Pure White'])
               
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
               'Boned',
               'Bound',
               'Bred',
               'Broken',
               'Captured',
               'Caught on Tape',
               'Caught on Video',
               'Cavity Searched',
               'Claimed','Claimed',
               'Claimed From Behind',
               'Claimed Hard',
               'Claimed in Public',
               'Chained Up',
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
               'Eaten Out',
               'Enslaved','Enslaved',
               'Exposed in Public',
               'Fisted',
               'Humped',
               'Hunted For Food',
               'Impregnated','Impregnated',
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
               'Ridden Hard',
               'Rimmed',
               'Satisfied',
               'Screwed',
               'Seduced',
               'Sexually Harrassed At My Workplace',
               'Shaved',
               'Sixty-Nined',
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
               'Taken in the Rear',
               'Tea-Bagged',
               'Tied Up',
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
                    'Sold'])
                    
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
     
     
     def __init__(self):
          super().__init__(['Adventure', 
               'Affair','Affair',
               'Encounter',
               'Liaison',
               'Love Story',
               'Romance','Romance','Romance',
               'Rendezvous',
               'Story'])
               
          self.WordHistoryQ = HistoryQ(3)
               
class VaginaSlang(WordList):
     def __init__(self):
          super().__init__(["bacon hole",
                                 "banana basket",
                                 "Bat Cave",
                                 "bearded clam",
                                 "beaver",
                                 "beef",
                                 "beef-flaps",
                                 "beef taco",
                                 "black hole",
                                 "box",
                                 "cherry pie",
                                 "clam",
                                 "clit pit",
                                 "cock-sock",
                                 "cock-garage",
                                 "cock-pocket",
                                 "cock-squeezer",
                                 "cooch",
                                 "coochie",
                                 "cooter",
                                 "cream canal",
                                 "cum dumpster",
                                 "cunny",
                                 "cunt",
                                 "cunt-hole",
                                 "fish lips",
                                 "fish wallet",
                                 "flower",
                                 "frenchfry dip",
                                 "front butt",
                                 "fuck-hole",
                                 "fur burger",
                                 "fur pie",
                                 "furry taco",
                                 "goop chute",
                                 "hair pie",
                                 "honey hole",
                                 "honey pot",
                                 "hot pocket",
                                 "lady bits",
                                 "lady parts",
                                 "love muffin",
                                 "kitty",
                                 "meat flaps",
                                 "meat sleave",
                                 "muff",
                                 "muffin",
                                 "panty hamster",
                                 "penis fly trap",
                                 "pie",
                                 "pink taco",
                                 "piss flaps",
                                 "puss",
                                 "pussy",
                                 "quim",
                                 "Sarlacc pit",
                                 "sausage wallet",
                                 "snatch",
                                 "spunk trunk",
                                 "twat",
                                 "tuna taco",
                                 "U.S.P. Port",
                                 "vag",
                                 "vaj",
                                 "vajayjay",
                                 "vertical bacon sandwich",
                                 "vertical smile",
                                 "whisker biscuit",
                                 "womanhood"
                                 ])
          
class TittySlang(WordList):
    def __init__(self):
          super().__init__(['Bazooms',
                            'Bongos',
                            'Breasticles',
                            'Cantaloups',
                            'Coconuts',
                            'Fun-Bags',
                            'Gazongas',
                            'Grand Tetons',
                            'Grapefruits',
                            'Hangers',
                            'Hooters',
                            'Jugs',
                            'Juice-Bags',
                            'Jubblies',
                            'Knockers',
                            'Love-Pillows',
                            'Mammaries',
                            'Melons',
                            'Meat-Melons',
                            'Milk Balloons',
                            'Pumpkins',
                            'Sweater-Zeppelins',
                            'Tatas',
                            'Tiddies',
                            'Titties',
                            'Udders'   
                           ])

class TantricTechniques(NounAdjList):
    def __init__(self):
          super().__init__(["Baloney",
                            "Banana",
                            "Beaver",
                            "Bronco",
                            "Bulldog",
                            "Bunghole",
                            "Burrito",
                            "Butterfly",                                                        
                            "Camel",
                            "Cherry",
                            "Coat-Hanger",
                            "Corn-Dog",
                            "Corn-Hole",
                            "Chimichanga",
                            "Cowgirl",
                            "Delight",
                            "Donkey",
                            "Dwarf",
                            "Enema",
                            "Fanny",
                            "Goat",
                            "Ham",
                            "Hamster",
                            "Hot-Dog",
                            "Kumquat",
                            "Lizard",
                            "Lotus",
                            "Manhole",
                            "Mermaid",
                            "Milk Maid",
                            "Milkshake",
                            "Monk",
                            "Monkey",
                            "Moustache",
                            "Noodle",
                            "Nun",
                            "Panini",
                            "Peter",
                            "Pickle",
                            "Pillow",
                            "Pony",
                            "Pork",
                            "Potato",
                            "Pudding",
                            "Rodeo",
                            "Row Boat",
                            "Sailor",
                            "Sandwich",
                            "Sausage",
                            "Stallion",
                            "Starfish",
                            "Stripper",
                            "Susan",
                            "Taco",
                            "Taint",
                            "Teabag",
                            "Thong",
                            "Tornado",
                            "Trombone",
                            "Tuna",
                            "Weasel",
                            "Whoopsie"
                            ],
                            ["Anal",
                            "Bald",
                            "Bangkok",
                            "Beef",
                            "Bloody",
                            "Brown",
                            "Burning",
                            "Buttered",
                            "Chinese",
                            "Chocolate",
                            "Choirboy",
                            "Chunky",
                            "Creamy",
                            "Crusty",
                            "Dental",
                            "Dentist's",
                            "Devil's",
                            "Dirty",
                            "Disco",
                            "Donkey",
                            "Drunken",
                            "Egyptian",
                            "Eskimo",
                            "Farmer's",
                            "Farting",
                            "Forbidden",
                            "French",
                            "Fruity",
                            "Fudge",
                            "German",
                            "Greasy",
                            "Gutter",
                            "Hairy",
                            "Hooker's",
                            "Italian",
                            "Jailhouse",
                            "Juicy",
                            "Las Vegas",
                            "Lazy",
                            "Magic",
                            "Mayonnaise",
                            "Mexican",
                            "Midnight",
                            "Mongolian",
                            "Mustard",
                            "Penile",
                            "Penis",
                            "Pink",
                            "Polish",
                            "Pony",
                            "Puckered",
                            "Rectal",
                            "Reverse",
                            "Russian",
                            "Rusty",
                            "Salty",
                            "Schoolgirl",
                            "Silky",
                            "Slippery",
                            "Sloppy",
                            "Spaghetti",
                            "Spicy",
                            "Spread-Eagle",
                            "Sticky",
                            "Stripper's",
                            "Texas",
                            "Three-Legged",
                            "Thirsty",
                            "Thong",
                            "Tijuana",
                            "Turkish",
                            "Upside-Down",
                            "Velvet",
                            "Whipped",
                            "Yellow"
                            ])
              
