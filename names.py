#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Names module

from random import *
from util import *

class Names:
	def __init__(self):
		self._FirstNamesList = WordList()
		self._LastNamesList = WordList()
		
	def FirstName(self, NotList = None):
		if NotList is None:
			NotList = []
			
		return self._FirstNamesList.GetWord(NotList = NotList)
		
	def SetFirstNames(self, NewList = None):
		if NewList is None:
			NewList = []
			
		self._FirstNamesList = WordList(NewList)
		
	def GetFirstNamesList(self):
		return self._FirstNamesList.List 
	
	def LastName(self, NotList = None):
		if NotList is None:
			NotList = []
	
		return self._LastNamesList.GetWord(NotList = NotList)
		
	def SetLastNames(self, NewList = None):
		if NewList is None:
			NewList = []
			
		self._LastNamesList = WordList(NewList)
		
	def GetLastNamesList(self):
		return self._LastNamesList.List 
		
class ClassyNamesFemale(Names):
	def __init__(self):
		super().__init__()
		self.SetFirstNames(['Alana',
			'Alexis',
			'Amelia',
			'Anastasia',
			'Angela',
			'Angelica',
			'Anita',
			'Annabel',
			'Aria',
			'Autumn',
			'Ava',
			'Bella',
			'Belle',
			'Bianca',
			'Brielle',
			'Brigitte',
			'Brynn',
			'Calliope',
			'Candy',
			'Caroline',
			'Carmina',
			'Cecie',
			'Charity',
			'Chelsea',
			'Clarissa',
			'Colette',
			'Constance',
			'Cordelia',
			'Daisy',
			'Dalia',
			'Dani',
			'Dannielle',
			'Daphne',
			'Deanna',
			'Delilah',
			'Delores',
			'Eden',
			'Eliza',
			'Elspeth',
			'Esmerelda',
			'Estelle',
			'Felicia',
			'Felicity',
			'Fiona',
			'Florence',
			'Francesca',
			'Georgina',
			'Gisele',
			'Harmony',
			'Heidi',
			'Heaven',
			'Honey',
			'Indigo',
			'Isabelle',
			'Jacinda',
			'Jaqueline',
			'Jasmine',
			'Josephine',
			'Juliana',
			'Juliette',
			'Juniper',
			'Jynx',
			'Kaitlyn',
			'Katrina',
			'Lacey',
			'Laurel',
			'Lauren',
			'Lavinia',
			'Lelani',
			'Leslie',
			'Lilah',
			'Lilli',
			'Lola',
			'Marianna',
			'Marilyn',
			'Melina',
			'Molly',
			'Morgan',
			'Natasha',
			'Olive',
			'Olivia',
			'Ophelia',
			'Paris',
			'Penelope',
			'Phoebe',
			'Piper',
			'Raven',
			'Regina',
			'Rhonda',
			'Roanna',
			'Rosaline',
			'Roxanne',
			'Ruby',
			'Sable',
			'Sabrina',
			'Saffron',
			'Satin',
			'Savannah',
			'Scarlett',
			'Simone',
			'Sophie',
			'Summer',
			'Svetlana',
			'Sydney',
			'Sylvia',
			'Tonya',
			'Tori',
			'Valentina',
			'Vanessa',
			'Veronica',
			'Viola',
			'Violet',
			'Virginia',
			'Vivienne'])
			
class PlainNamesFemale(Names):
	def __init__(self):
		super().__init__()
		self.SetFirstNames(['Amber',
							   'Anne',
							   'Annie',
							   'Cindy',
							   'Beatrice',
							   'Betty',
							   'Dianne',
							   'Donna',
							   'Doris',
							   'Elizabeth',
							   'Emma',
							   'Ericka',
							   'Ginger',
							   'Harriet',
							   'Holly',
							   'Jane',
							   'June',
							   'Lucy',
							   'Kim',
							   'Kitty',
							   'Lilly',
							   'Marsha',
							   'Mary',
							   'Mary Jane',
							   'May',
							   'Mel',
							   'Melissa',
							   'Misty',
							   'Rachael',
							   'Sally',
							   'Tasha',
							   'Tess',
							   'Tiffany',
							   'Vicky',
							   ])
							   
class InnuendoNamesFemale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(['Amanda','Amanda','Amanda',
							'Anita','Anita','Anita','Anita',
							'Anna',
							'Anna L.','Anna L.','Ana L.',
							'Candy',
							'Carrie',
							'Chastity',
							'Cherry','Cherry',
							'Deepa',
							'Dixie',
							'Eden','Eden','Eden',
							'Fonda','Fonda','I.M. Fonda',
							'Hilda',
							'Honey',
							'Ida',
							'Ima',
							'Inya','Inya',
							'Issa','Issa',
							'Ivana','Ivana','Ivana','Ivana',
							'Jackie',
							'Jill','Jill N.','Jill N.',
							'Juanita',
							'Kari',
							'Maya','Maya P.','Maya C.',
							'Misty',
							'Muffy',
							'Nastya',
							#'Nell',
							'Olive',
							'Olive R.','Olive R.',
							'Olivia','Olivia',
							'Ophelia','Ophelia','Ophelia',
							'Rhoda','Rhoda','Rhoda','I. Rhoda',
							'Rosie',
							'Sandy',
							'Satin',
							'Sharon','Sharon','Sharon','I.M. Sharon',
							'Tara',
							'Tina',
							'Tonya',
							'Wilma'])
			
class NamesFemale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(ClassyNamesFemale().GetFirstNamesList())
		
class AuthorNamesFemale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(InnuendoNamesFemale().GetFirstNamesList())

class PlainNamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(['Al',
							'Allen',
							   'Ben',
							   'Bob',
							   'Chuck',
							   'Dan',
							   'Dave',
							   'Dick',
							   'Doug',
							   'Duane',
							   'Earl',
							   'Ed',
							   'Frank',
							   'Greg',
							   'Hank',
							   'Harry',
							   'Isaac',
							   'Ivan',
							   'James',
							   'Jeff',
							   'Jim',
							   'Jimmy',
							   'Joe',
							   'John',
							   'Josh',
							   'Kenny',
							   'Lenny',
							   'Lou',
							   'Mike',
							   'Nick',
							   'Phil',
							   'Philip',
							   'Rob',
							   'Rusty',
							   'Steve',
							   'Steven',
							   'Ted',
							   'Tim',
							   'Tom',
							   'Will',
							   'Zach',
							   'Zeke'])

class ClassyNamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(['Adam',
			'Alistair',
			'Ambrose',
			'Andre',
			'Angel',
			'Apollo',
			'Archer',
			'Blake',
			'Brad',
			'Bradford',
			'Bradley',
			'Cal',
			'Chad',
			'Christopher',
			'Clint',
			'Clive',
			'Connor',
			'Cullen',
			'Dallas',
			'Dante',
			'Darius',
			'Deacon',
			'Desmond',
			'Dominic',
			'Drake',
			'Duke',
			'Eduardo',
			'Esteban',
			'Ferdinand',
			'Finn',
			'Flint',
			'Gavin',
			'Geoffrey',
			'Grant',
			'Griffin',
			'Grigory',
			'Hudson',
			'Hunter',
			'Iain',
			'Ivan',
			'Javier',
			'Jordan',
			'Juan',
			'Julian',
			'Kane',
			'Leo',
			'Leon',
			'Lex',
			'Liam',
			'Lorenzo',
			'Manuel',
			'Marco',
			'Max',
			'Michael',
			'Miles',
			'Nicolas',
			'Pablo',
			'Peter',
			'Quentin',
			'Quinn',
			'Rafael',
			'Rafe',
			'Ramon',
			'Raoul',
			'Reed',
			'Reginald',
			'Remington',
			'Rex',
			'Ricardo',
			'Richard',
			'Rico',
			'Roberto',
			'Rogan',
			'Roland',
			'Romeo',
			'Ronson',
			'Rowan',
			'Royce',
			'Ruben',
			'Russell',
			'Ryder',
			'Sean',
			'Sebastian',
			'Sergei',
			'Shane',
			'Stefan',
			'Sterling',
			'Tremaine',
			'Trey',
			'Tristan',
			'Tristan',
			'Tucker',
			'Ty',
			'Vance',
			'Vaughan',
			'Vicenzo',
			'Vincent',
			'Xavier'])
	   
class InnuendoNamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(['Barry',
			'Ben','Ben',
			'Bone R.',
			'Buster',
			'Dewey','Dewey',
			'Dick','Dick','Dick',
			'Dirk',
			'Dixon',
			'Gaylord',
			'Hans',
			'Harry','Harry','Harry',
			'Holden','Holden',
			'Howie',
			'Hugh','Hugh',
			'Jack','Jack','Jack N.','Jack N.',
			'Juan','I. Juan','I. Juan','Juan A.',
			'Kanye',
			'Lance','Lance',
			'Major',
			'Max',
			#'Mike','Mike',
			'Neil',
			'Oliver','Oliver',
			'Otto',
			'Pat','Pat','I. Pat','Pat N.',
			'Penn S.',
			'Peter','Peter',
			'Phil','Phil M.'
			'Philip',
			'Philmore',
			'Randy',
			'Rich','Rich',
			'Rod',
			'Ryder',
			'Sawyer','Sawyer','Sawyer P.','I. Sawyer',
			'Seymour','Seymour','Seymour','I. Seymour',
			'Willie','Willie','Will E.','Will I.',
			'Woody','Woody','Woody U.'
			])
			
class AuthorNamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(InnuendoNamesMale().GetFirstNamesList())
		
class DiverseNamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(ClassyNamesMale().GetFirstNamesList() + PlainNamesMale().GetFirstNamesList())		
		
class NamesMale(Names):
	def __init__(self):
		super().__init__()
		
		self.SetFirstNames(ClassyNamesMale().GetFirstNamesList())
			
class InnuendoLastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = ["Amalova",
			"Analiquor",
			"Anlicker",
			"Bangs","Bangs",
			"Bear",
			"Beaver","Beaver","Beaver",
			"Beeter",
			"Bendz",
			"Biggs",
			"Blower",
			"Blush",
			"Bodie",
			"Brest","Bresst",
			"Broad",
			"Brownie",
			"Bottoms",
			"Buhnz",
			"Butts",
			"Cherry",
			"Clam",
			"Clams",
			"Clozov",
			"Cox",
			"Cracks",
			"Cream",
			"Creamer",
			"Creams",
			"Cummer",
			"Cummings","Cummings",
			"Daley",
			"Dick",
			"Dickens",
			"Dicker",
			"Dicter",
			"Dix",
			"Djerkov",
			"Djiz",
			"Fatone",
			"Fatt",
			"Faulks",
			"Felch",
			"Feltcher",
			"Fuchs",
			"Furrows",
			"Galey",
			"Gaylord",
			"Goodebody",
			"Goodhead",
			"Gozinya",
			"Grotch",
			"Hancock",
			"Handler",
			"Hard",
			"Harder",
			"Hardin",
			"Head",
			"Hiscock",
			"Ho","Ho","Ho",
			"Hoar",
			"Holden",
			"Holston",
			"Hump",
			"Humper",
			"Hung","Hung",
			#"Hunt",
			"Hyman",
			"Hunter",
			"Inya",
			"Janus",
			"Jacov",
			"Jiggles",
			"Johnson","Johnson",
			"Knightly",
			"Knockers",
			"Knott",
			"Knuttz",
			"Koch",
			"Kootch",
			"Krevises",
			"Kuntz",
			"Lipps",
			"Liquor",
			"Lode",
			"Long",
			"Lust",
			"Mann",
			"Mannlove",
			"McCreviss",
			"Mehoff",
			"Mellck",
			"Melons",
			"Milfinger",
			"Minx",
			"Moon",
			"Moore",
			"Moorecox",
			"Moorehard",
			"Moorehead",
			"Mortits",
			"Mount",
			"Mountcox",
			"Mountford",
			"Muncher",
			"Muff",
			"Muffin",
			"Nippell",
			"Oxhard",
			"Peach",
			"Peaches",
			"Pearl",
			"Pecker",
			"Peckwood",
			"Peters","Peters",
			"Philmore",
			"Pink",
			"Pohl",
			"Polk",
			"Poppa",
			"Puss",
			"Popper",
			"Posey",
			"Pu",
			"Rack",
			"Racks",
			"Rohdd",
			"Rimmer",
			"Rubber",
			"Sachs",
			"Sacks",
			"Sax",
			"Schaft",
			"Schlong",
			"Snatch",
			"Spreader",
			"Spunck",
			"Stiffington",
			"Stiffly",
			"Stiffy",
			"Stinker",
			"Stroker",
			"Stuffers",
			"Swallower",
			"Swallows",
			"Throat",
			"Topper",
			"Wang",
			"Weiner",
			"Wood",
			"Zemen"]
			
class ClassyLastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = ["Bardot",
					"Black",
					"Church",
					"Cho",
					"De Boest",
					"Devlyn",
					"Fox",
					"Hu",
					"Johnson",
					"Jones",
					"King",
					"Knight",
					"Knox",
					"Lace",
					"La Vigne",
					"Mandelay",
					"Morgan",
					"Prince",
					"Quinn",
					"Red",
					"Rose",
					"St. Claire",
					"St. Thomas",
					"Steele",
					"Strange",
					"Sweet",
					"Vale",
					"Valentine",
					"White",
					"Wilde",
					"Winters",
					"Zahara"]
			
class PlainLastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = ['Beaver',
					  'Bell',
					  'Bottoms',
					  'Brown',
					  'Butts',
					  'Chang',
					  'Chin',
					  'Church',
					  'Clark',
					  'Cox',
					  'Cummings',
					  'Davis',
					  'Goodbody',
					  'Gonzalez',
					  'Gray',
					  'Green',
					  'Hancock',
					  'Hill',
					  'Jefferson',
					  'Johnson',
					  'Jones',
					  'King',
					  'Lee',
					  'Long',
					  'Lopez',
					  'Moore',
					  'Moorecox',
					  'Pearl',
					  'Peters',
					  'Philmore',
					  'Robinson',
					  'Rogers',
					  'Ross',
					  'Sanderson',
					  'Smith',
					  'Taylor',
					  'Wang',
					  'White',
					  'Williams',
					  'Wilson',
					  'Wood'
					]
					
class AuthorLastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = InnuendoLastNames().List + ClassyLastNames().List
		
class RegularLastNames(WordList):
	def __init__(self):
		super().__init__()
		
		self.List = PlainLastNames().List + ClassyLastNames().List
		
def LastNameBuilder(NotList = None):
	sLName = ""
	
	Names = []
	
	if NotList == None:
		NotList = []
	
	sName1 = AuthorLastNames().GetWord(NotList = NotList)
	sName2 = AuthorLastNames().GetWord(NotList = [sName1] + NotList)
	
	for _ in range(3):
		Names.append(sName1)
	
	Names.append(sName1 + "-" + sName2)
	
	sLName = Names[randint(0, len(Names) - 1)]
	
	return sLName
		
def AuthorBuilder(Gender = Gender.Neuter):
	sAName = ""
	
	Alphabet = "AAAABBBCCDDDEEEEFFFGGGGHHHIIJJJJKKLLLMNOOPPPQRRRRSSSSTTTTUVVWWWXYZ"
	
	FirstNames = []
	MaleNames = AuthorNamesMale()
	FemNames = AuthorNamesFemale()
	
	sName = ""
	for _ in range(2):
		sName += Alphabet[randint(0, len(Alphabet) - 1)] + "."
	FirstNames.append(sName)
	
	if Gender == Gender.Male or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(MaleNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(4):
			sName1 = MaleNames.FirstName()
			FirstNames.append(sName1)
			
		for _ in range(2):
			sMaleFirstName = MaleNames.FirstName()
			if not '.' in sMaleFirstName:
				FirstNames.append(sMaleFirstName + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
			
		for _ in range(2):
			sMaleFirstName = MaleNames.FirstName()
			if not '.' in sMaleFirstName:
				FirstNames.append("AAEIIUBCP"[randint(0, 8)] + ". " + sMaleFirstName)
		
	if Gender == Gender.Female or Gender == Gender.Neuter:
		for _ in range(5):
			FirstNames.append(FemNames.FirstName())
			
		sName1 = ""
		sName2 = ""
		for _ in range(4):
			sName1 = FemNames.FirstName()
			FirstNames.append(sName1)
			
		for _ in range(2):
			sFemFirstName = FemNames.FirstName()
			if '.' not in sFemFirstName:
				FirstNames.append(sFemFirstName + " " + Alphabet[randint(0, len(Alphabet) - 1)] + ".")
			
		for _ in range(2):
			sFemFirstName = FemNames.FirstName()
			if '.' not in sFemFirstName:
				FirstNames.append("AAEIIUBCP"[randint(0, 8)] + ". " + sFemFirstName)
		
	sAName = FirstNames[randint(0, len(FirstNames) - 1)]
	
	sAName += " " + LastNameBuilder(NotList = [sAName])
	
	return sAName