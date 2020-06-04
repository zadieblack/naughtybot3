#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Names module

from random import *
from util import *

InnNameHistoryQ = HistoryQ(2)

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
               'Aurelia',
               'Autumn',
               'Ava',
               'Bella',
               'Belle',
               'Bianca',
               'Brielle',
               'Brigitte',
               'Brynn',
               'Calliope',
               'Camille',
               'Candy',
               'Caroline',
               'Carmina',
               'Cecie',
               'Charity',
               'Chelsea',
               'Claire',
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
               'Donatella',
               'Eden',
               'Eleanor',
               'Eliza',
               'Elspeth',
               'Emmeline',
               'Esmerelda',
               'Estelle',
               'Felicia',
               'Felicity',
               'Fiona',
               'Florence',
               'Francesca',
               'Georgina',
               'Gisele',
               'Gwyneth',
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
               'Lana',
               'Laurel',
               'Lauren',
               'Lavinia',
               'Lelani',
               'Leslie',
               'Lilah',
               'Lilli',
               'Lola',
               'Madeline',
               'Marianna',
               'Marilyn',
               'Margaret',
               'Margot',
               'Melina',
               'Molly',
               'Morgan',
               'Natasha',
               'Octavia',
               'Odette',
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
               'Rosalind',
               'Rosaline',
               'Roxanne',
               'Ruby',
               'Sable',
               'Sabrina',
               'Saffron',
               'Satin',
               'Savannah',
               'Scarlett',
               'Serena',
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
               'Violetta',
               'Virginia',
               'Vivienne',
               'Yolanda'])
               
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
          
          self.SetFirstNames(PlainNamesFemale().GetFirstNamesList() + ClassyNamesFemale().GetFirstNamesList())
          
class AuthorNamesFemale(Names):
     def __init__(self):
          super().__init__()
          
          self.SetFirstNames(InnuendoNamesFemale().GetFirstNamesList())

class PlainNamesMale(Names):
     def __init__(self):
          super().__init__()
          
          self.SetFirstNames(['Allen',
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
               'Anthony',
               'Apollo',
               'Archer',
               'Archibald',
               'Barnaby',
               'Bentley',
               'Blake',
               'Brad',
               'Bradford',
               'Bradley',
               'Bronson',
               'Cal',
               'Chad',
               'Christopher',
               'Clarence',
               'Clint',
               'Clive',
               'Connor',
               'Cullen',
               'Dallas',
               'Dante',
               'Dario',
               'Darius',
               'Deacon',
               'Desmond',
               'Dominic',
               'Drake',
               'Duke',
               'Eduardo',
               'Esteban',
               'Fabian',
               'Ferdinand',
               'Finn',
               'Flint',
               'Gavin',
               'Geoffrey',
               'Gerald',
               'Giorgio',
               'Giovanni',
               'Grant',
               'Granville',
               'Griffin',
               'Grigory',
               'Harrison',
               'Henri',
               'Hudson',
               'Hugo',
               'Hunter',
               'Iain',
               'Ivan',
               'Javier',
               'Jordan',
               'Juan',
               'Julian',
               'Kane',
               'Lawrence',
               'Leo',
               'Leon',
               'Lex',
               'Liam',
               'Lorenzo',
               'Luther',
               'Manuel',
               'Matteo',
               'Marco',
               'Max',
               'Michael',
               'Miles',
               'Milton',
               'Montgomery',
               'Nathaniel',
               'Nicolas',
               'Oliver',
               'Oswald',
               'Pablo',
               'Peter',
               'Pierre',
               'Quentin',
               'Quincy',
               'Quinn',
               'Rafael',
               'Rafe',
               'Raoul',
               'Ramon',
               'Randolph',
               'Reed',
               'Reginald',
               'Remington',
               'Rex',
               'Ricardo',
               'Richard',
               'Rico',
               'Roberto',
               'Roderick',
               'Rodger',
               'Rogan',
               'Roland',
               'Romeo',
               'Ronson',
               'Rowan',
               'Royce',
               'Ruben',
               'Rupert',
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
               "Bone",
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
          
          self.List = ["Ashcroft",
                        "Bardot",
                        "Beaumont",
                        "Beauregard",
                        "Black",
                        "Church",
                        "Cho",
                        "De Boest",
                        "Devlyn",
                        "Featherbottom",
                        "Fox",
                        "Hu",
                        "Johnson",
                        "Jones",
                        "King",
                        "Knight",
                        "Knox",
                        "Lace",
                        "La Vigne",
                        "London",
                        "Mandelay",
                        "Mansfield",
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
          
class AllLastNames(WordList):
     def __init__(self):
          super().__init__()
          
          self.List = PlainLastNames().List + ClassyLastNames().List + InnuendoLastNames().List
          
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
          
def AuthorBuilder(gender = Gender.Neuter):
     return GetInnName(gender)
     
     
class InnName():
     def __init__(self, NewNameVariantsList = None, NewPrefInitList = None, NewSuffInitList = None):
          if NewNameVariantsList is None:
               NewNameVariantsList = []
               
          if NewPrefInitList is None:
               NewPrefInitList = []
     
          if NewSuffInitList is None:
               NewSuffInitList = []     
               
          self._NameVariants = WordList(NewNameVariantsList)
          self._PrefInitList = WordList(NewPrefInitList)
          self._SuffInitList = WordList(NewSuffInitList)
          
          self._Gender = Gender.Neuter 
          
     def GetNameVariant(self):
          return self._NameVariants.GetWord()
          
     def GetPrefInitial(self):
          return self._PrefInitList.GetWord()
          
     def GetSuffInitial(self):
          return self._SuffInitList.GetWord()
     
     def GetNameVariantsList(self):
          return self._NameVariants.List 
          
     def GetPrefInitialList(self):
          return self._PrefInitList.List
          
     def GetSuffInitialList(self):
          return self._SuffInitList.List
          
     def IsNameVariantListEmpty(self):
          return self._NameVariants.IsEmpty()
          
     def IsPrefInitListEmpty(self):
          return self._PrefInitList.IsEmpty()
          
     def IsSuffInitListEmpty(self):
          return self._SuffInitList.IsEmpty()
          
     def SetGender(self, gender):
          if isinstance(gender, Gender):
               self._Gender = gender
          
     def IsMale(self):
          return self._Gender == Gender.Male 
          
     def IsFemale(self):
          return self._Gender == Gender.Female
          
     def IsNeuter(self):
          return self._Gender == Gender.Neuter
          

class InnFirstName(InnName):     
     def GetName(self):
          sFirstName = ""
          
          PossibleNameVariants = WordList() 
          if not self.IsNameVariantListEmpty():
               i = 0
               while i < 3:
                    PossibleNameVariants.AddWord(self.GetNameVariant())
                    i = i + 1
               
               if not self.IsPrefInitListEmpty():
                    PossibleNameVariants.AddWord(self.GetPrefInitial() + ". " + self.GetNameVariant())
               
               if not self.IsSuffInitListEmpty():
                    PossibleNameVariants.AddWord(self.GetNameVariant() + " " + self.GetSuffInitial() + ".")
     
          if not PossibleNameVariants.IsEmpty():
               sFirstName = PossibleNameVariants.GetWord()
               
          return sFirstName
          
class InnFirstNameFemale(InnFirstName):     
     def __init__(self, NewNameVariantsList = None, NewPrefInitList = None, NewSuffInitList = None):
          super().__init__(NewNameVariantsList = NewNameVariantsList, NewPrefInitList = NewPrefInitList, NewSuffInitList = NewSuffInitList)     
               
          self.SetGender(Gender.Female)

class InnFirstNameMale(InnFirstName):     
     def __init__(self, NewNameVariantsList = None, NewPrefInitList = None, NewSuffInitList = None):
          super().__init__(NewNameVariantsList = NewNameVariantsList, NewPrefInitList = NewPrefInitList, NewSuffInitList = NewSuffInitList)     
               
          self.SetGender(Gender.Male)     

class InnLastName(InnName):
     def GetName(self):
          sLastName = ""
          
          PossibleNameVariants = WordList() 
          if not self.IsNameVariantListEmpty():
               i = 0
               while i < 3:
                    PossibleNameVariants.AddWord(self.GetNameVariant())
                    i = i + 1
               
               if not self.IsPrefInitListEmpty():
                    PossibleNameVariants.AddWord(self.GetPrefInitial() + ". " + self.GetNameVariant())
     
          if not PossibleNameVariants.IsEmpty():
               sLastName = PossibleNameVariants.GetWord()
               
          return sLastName
          
class DefaultLastName(Enum):
     FirstLastName = 1
     SecondLastName = 2
          
class InnNameGenerator():
     def __init__(self, id = 0, priority = 1):     
          self.ID = id
          self.Priority = priority
          self.Type = GeneratorType.Normal
          
          self._Default = DefaultLastName.FirstLastName
          
          self._FirstNameFemaleList = WordList()
          self._FirstNameMaleList = WordList()
          self._FirstLastNameList = WordList()
          self._SecondLastNameList = WordList()
          self._LastNameList = WordList()
          
     def FirstNameFemaleList(self, NewList = None):
          if NewList is None:
               NewList = []
               
          self._FirstNameFemaleList = WordList(NewList) 
          
     def FirstNameMaleList(self, NewList = None):
          if NewList is None:
               NewList = []
               
          self._FirstNameMaleList = WordList(NewList) 
          
     def FirstLastNameList(self, NewList = None):
          if NewList is None:
               NewList = []
               
          self._FirstLastNameList = WordList(NewList) 
          
     def SecondLastNameList(self, NewList = None):
          if NewList is None:
               NewList = []
               
          self._SecondLastNameList = WordList(NewList) 
          
     def GetName(self, gend):
          sName = "" 
          
          #print("Gender is class " + str(gend) + ", repr: " + repr(gend) + "\n")
          if not isinstance(gend, Gender):
               gend = Gender.Female 
               
          sLastName = ""
          if self._Default is DefaultLastName.FirstLastName:
               if not self._FirstLastNameList.IsEmpty():
                    if randint(1,3) == 3 and not self._SecondLastNameList.IsEmpty():
                         sLastName = self._FirstLastNameList.GetWord().GetName() + "-" + self._SecondLastNameList.GetWord().GetName()
                    else:
                         sLastName = self._FirstLastNameList.GetWord().GetName()
          else:
               if not self._SecondLastNameList.IsEmpty():
                    if randint(1,3) == 3 and not self._FirstLastNameList.IsEmpty():
                         sLastName = self._FirstLastNameList.GetWord().GetName() + "-" + self._SecondLastNameList.GetWord().GetName()
                    else:
                         sLastName = self._SecondLastNameList.GetWord().GetName()
          
          if gend == Gender.Female and (not self._FirstNameFemaleList.IsEmpty()):
               if sLastName:
                    sName = self._FirstNameFemaleList.GetWord().GetName() + " " + sLastName
               else:
                    sName = self._FirstNameFemaleList.GetWord().GetName()
                    
          elif gend == Gender.Male and (not self._FirstNameMaleList.IsEmpty()):
               if sLastName:
                    sName = self._FirstNameMaleList.GetWord().GetName() + " " + sLastName
               else:
                    sName = self._FirstNameMaleList.GetWord().GetName()
                    
          return sName 
          
     # def FirstNameFemale(self):
          # return self._FirstNameFemaleList.GetWord()
          
     # def FirstNameMale(self):
          # return self._FirstNameMaleList.GetWord()
          
     # def LastName(self):
          # return self._LastNameList.GetWord()
          

# Name: Verb/Adjective - Noun(genitals)
class InnNameGen1(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 1,priority = 1)
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita','Anita C.']),
                                              InnFirstNameFemale(['Eden']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Ivana','Ivana C.']),
                                              InnFirstNameFemale(['Juana','Juana C.']),
                                              InnFirstNameFemale(['Juanita']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Misty']),
                                              InnFirstNameFemale(['C. Mya','C. Maya']),
                                              InnFirstNameFemale(['Maya C.']),
                                              InnFirstNameFemale(['Muffy']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Olive','Olivia','Olive R.']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Satin']),
                                              InnFirstNameFemale(['P. Inya','Inya']),
                                              InnFirstNameFemale(['Onya','P. Onya']),
                                              InnFirstNameFemale(['Tara'])
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Dewey']),
                                              InnFirstNameMale(['Dixon']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['I.C.']),
                                              InnFirstNameMale(['Juan','I. Juan']),
                                              InnFirstNameMale(['Phil','Phil N.','Philmore']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Minnie']),
                                              InnFirstNameMale(['Randy']),
                                              InnFirstNameMale(['Rich']),
                                              InnFirstNameMale(['Ryder']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                              InnFirstNameMale(['Oliver']),
                                              InnFirstNameMale(['Juan A.'])
                                             ])

          self.FirstLastNameList([      InnLastName(['Bare']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Broad']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Hard']),
                                              InnLastName(['Hung']),
                                              InnLastName(['Long']),
                                              InnLastName(['Major']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Strange']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Balls']),
                                              InnLastName(['Beaver']),
                                              InnLastName(['Bone']),
                                              InnLastName(['Brest','Bresst']),
                                              InnLastName(['Broad']),
                                              InnLastName(['Blower']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cooter']),
                                              InnLastName(['Cox']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Dick','Dicks','Dix','Dickons']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Grotch']),
                                              InnLastName(['Hyman']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Lipps']),
                                              InnLastName(['McCreviss']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Moon']),
                                              InnLastName(['Muff','Muffin']),
                                              InnLastName(['Nippel']),
                                              InnLastName(['Peach','Peaches']),
                                              InnLastName(['Pearl']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Puss']),
                                              InnLastName(['Posey']),
                                              InnLastName(['Rack','Racks']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Sachs','Sachs','Sax']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Stiffy']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood'])
                                             ])
                                             
# Name: Adjective Adverb-Verber
class InnNameGen2(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 2,priority = 1)
          
          self.FirstNameFemaleList([      InnFirstNameFemale(['A. Nell']),
                                              InnFirstNameFemale(['Ana L.','Anna L.']),
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']),
                                              InnFirstNameFemale(['Amanda']),
                                              InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Cherry']),
                                              InnFirstNameFemale(['Ima']),
                                              InnFirstNameFemale(['Ivana']),
                                              InnFirstNameFemale(['Juana','I. Juana']),
                                              InnFirstNameFemale(['Kitty']),
                                              InnFirstNameFemale(['Lady']),
                                              InnFirstNameFemale(['May','May I.','Maya','I. May']),
                                              InnFirstNameFemale(['Muffy']),
                                              InnFirstNameFemale(['Sweetie']),
                                              InnFirstNameFemale(['Wanda'])
                                         ])
                                             
          self.FirstNameMaleList([            InnFirstNameMale(['Cooter']),
                                              InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Gunnar','I. Gunnar']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Gaylord']),
                                              InnFirstNameMale(['Howie']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['Kanye']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Otto']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Rod']),
                                              InnFirstNameMale(['Woody','Woody U.']),
                                              InnFirstNameMale(['Will E.','Will I.','Willy','Willie','Will U.'])
                                              
                                             ])

          self.FirstLastNameList([InnLastName(['Bangs','Banger']),
                                              InnLastName(['Bender']),
                                              InnLastName(['Creamer']),
                                              InnLastName(['Cummings']),
                                              InnLastName(['Dicker','Dickens']),
                                              InnLastName(['Djerkov']),
                                              InnLastName(['Faulks']),
                                              InnLastName(['Feltcher']),
                                              InnLastName(['Fokker','Focker']),
                                              InnLastName(['Humper']),
                                              InnLastName(['Jakov','Jackov']),
                                              InnLastName(['Liquor','Licker','Likker'
                                                           ]),
                                              InnLastName(['Gaper']),
                                              InnLastName(['Mounter']),
                                              InnLastName(['Philmore']),
                                              InnLastName(['Polk','Poke','Poker']),
                                              InnLastName(['Porker']),
                                              InnLastName(['Popper']),
                                              InnLastName(['Pu']),
                                              InnLastName(['Rimmer']),
                                              InnLastName(['Rubber']),
                                              InnLastName(['Spreader']),
                                              InnLastName(['Stuffer']),
                                              InnLastName(['Swallower']),
                                              InnLastName(['Stroker']),
                                              InnLastName(['Topper']),
                                              InnLastName(['White'])
                                             ])
          
          #'Daley','Freely','Gayley','Hard','Harder','Knightly','Moore','Shyly','Stiffley','Kootch','Krevises',Kuntz',
          self.SecondLastNameList([InnLastName(['Daley']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley']),
                                              InnLastName(['Beaver']),
                                              InnLastName(['Bodie','Bawdy','Bawdee','Bawdie','Body']),
                                              InnLastName(['Bresst','Brest']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Furrow']),
                                              InnLastName(['Hole', 'Holes']),
                                              InnLastName(['Holston']),
                                              InnLastName(['Hyman']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Kootch','Kooter']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Muffy','Muffin']),
                                              InnLastName(['Peach']),
                                              InnLastName(['Puss']),
                                              InnLastName(['Snatch'])
                                             ])
     
# Name: Amanda Faulk
class InnNameGen3(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 3,priority = 1)
          
          self.FirstNameFemaleList([      InnFirstNameFemale(['Amanda']),
                                              InnFirstNameFemale(['Amanda']),
                                              InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Ivana']),
                                              InnFirstNameFemale(['Juana','I. Juana','Juanita']),
                                              InnFirstNameFemale(['Olive','Olivia']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Wanda']),
                                         ])
                                             
          self.FirstNameMaleList([      InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Gunnar','I. Gunnar']),
                                              InnFirstNameMale(['Gaylord']),
                                              InnFirstNameMale(['Juan A.']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Kanye']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Otto']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Rod']),
                                              InnFirstNameMale(['Woody','Woody U.']),
                                              InnFirstNameMale(['Will E.','Will I.','Willy','Willie','Will U.'])
                                              
                                             ])

          self.FirstLastNameList([      InnLastName(['Blow']),
                                              InnLastName(['Cream']),
                                              InnLastName(['Cummings']),
                                              InnLastName(['Dick','Dickens']),
                                              InnLastName(['Djerkov']),
                                              InnLastName(['Djiz']),
                                              InnLastName(['Faulk']),
                                              InnLastName(['Feltch']),
                                              InnLastName(['Gaylord']),
                                              InnLastName(['Hump']),
                                              InnLastName(['Jakov','Jackov']),
                                              InnLastName(['Gape']),
                                              InnLastName(['Mount']),
                                              InnLastName(['Philmore']),
                                              InnLastName(['Swallow']),
                                              InnLastName(['Stroke']),
                                              InnLastName(['Throat'])
                                             ])
          
          #'Moorehard
          self.SecondLastNameList([      InnLastName(['Bottoms']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Daley']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Moore']),
                                              InnLastName(['Moorehard']),
                                              InnLastName(['Onnum']),
                                              InnLastName(['Stiffley']),
                                             ])
                                             
                                             
# Verb: 'Barry','Bone R.','Buster','Holden','Lance','Pat','Pat N.','Phil','Phil N.','Philip','Philmore','Ryder',
       # 'Seymour','I. Seymour'
# Verb (being): 'Ben','I. Ben'
class InnNameGen4(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 4,priority = 1)
          
          self._Default = DefaultLastName.SecondLastName
          
          #'Carrie','Eden','Kari','Rhoda','Sharon','I'.M. Sharon'
          self.FirstNameFemaleList([      InnFirstNameFemale(['A. Nell']),
                                              InnFirstNameFemale(['Ana L.','Anna L.']),
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']),
                                              InnFirstNameFemale(['Carrie']),
                                              InnFirstNameFemale(['Eden U.']),
                                              InnFirstNameFemale(['C. Cherry','Cherry','Cherry P.']),
                                              InnFirstNameFemale(['Rhoda U.']),
                                              InnFirstNameFemale(['Sharon','I.M. Sharon']),
                                              InnFirstNameFemale(['Yu Mi'])
                                         ])
                                             
          self.FirstNameMaleList([      InnFirstNameMale(['Bone R.','I. Bone','Bone U.']),
                                              InnFirstNameMale(['Buster',]),
                                              InnFirstNameMale(['Craven','I.M. Craven']),
                                              InnFirstNameMale(['C. Dick','Dick','Dick U.']),
                                              InnFirstNameMale(['Holden','Holden P.']),
                                              InnFirstNameMale(['Jack','Jack N.']),
                                              InnFirstNameMale(['Lance','I. Lance','U. Lance']),
                                              InnFirstNameMale(['Pat','Pat N.','Pat U.']),
                                              InnFirstNameMale(['Phil','Phil N.','Philip','I. Philip']),
                                              InnFirstNameMale(['Philmore','I. Philmore']),
                                              InnFirstNameMale(['Ryder','I. Ryder']),
                                              InnFirstNameMale(['Seymour','I. Seymour'])
                                              
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bone','Boner','Bones']),
                                              InnLastName(['Brest','Bresst']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cox']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Dick','Dicks','Dix','Dickons']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Grotch']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Mann']),
                                              InnLastName(['Mannlove']),
                                              InnLastName(['McCreviss']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Moon']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rack','Racks']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Sachs','Sachs','Sax']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Daley']),
                                   InnLastName(['Deeper']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley'])
                                             ])
                                             
# Name: Noun - Adjective
class InnNameGen5(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 5,priority = 1)
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Ima']),
                                              InnFirstNameFemale(['Ophelia'])
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Ben','I. Ben']),
                                              InnFirstNameMale(['Dick']),
                                              InnFirstNameMale(['Gaylord']),
                                              InnFirstNameMale(['Juan U.']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Rod']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                              InnFirstNameMale(['Seymour','I. Seymour']),
                                              InnFirstNameMale(['Willie','Willy'])
                                             ])

          #'Bear','Blush','Biggs','Clozov','Cummer','Fatt','Goode','Hancock','Hancocke','Hard',
             # 'Humper','Hung','Hunter','Inya','Long','Manlove','Moorehard','Oxhard','Pink','Stiffy',
             # 'Stiffington'
          self.FirstLastNameList([InnLastName(['Bare', 'S. Bare']),
                                              InnLastName(['Blushing', 'S. Blushing']),
                                              InnLastName(['Biggs', 'S. Biggs']),
                                              InnLastName(['Clozov']),
                                              InnLastName(['Cumming', 'S. Cumming']),
                                              InnLastName(['Fatt', 'S. Fatt']),
                                              InnLastName(['Goode', 'S. Goode']),
                                              InnLastName(['Hancock', 'S. Hancock']),
                                              InnLastName(['Hard','Harder', 'S. Hard']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Hung', 'S. Hung']),
                                              InnLastName(['Inya', 'S. Inya']),
                                              InnLastName(['Long', 'S. Long']),
                                              InnLastName(['Manlove', 'S. Manlove']),
                                              InnLastName(['Moorehard', 'S. Moorehard']),
                                              InnLastName(['Onya', 'S. Onya']),
                                              InnLastName(['Oxhard', 'S. Oxhard']),
                                              InnLastName(['Pink', 'S. Pink']),
                                              InnLastName(['Stiffy']),
                                              InnLastName(['Stiffington', 'S. Stiffington'])
                                             ])
                                             
# Name: Ima Ho
class InnNameGen6(InnNameGenerator):
     def __init__(self):
          super().__init__(id = 6,priority = 1)
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Ima']),
                                              InnFirstNameFemale(['Issa']),
                                              InnFirstNameFemale(['Juana','I. Juana','U. Juana']),
                                              InnFirstNameFemale(['Rhoda','I. Rhoda','U. Rhoda']),
                                              InnFirstNameFemale(['Wanda','I. Wanda'])
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Ben A.','I. Ben']),
                                              InnFirstNameMale(['Craven','I.M. Craven']),
                                              InnFirstNameMale(['Dick','Dick A.','I. Dick']),
                                              InnFirstNameMale(['Juan A.']),
                                              InnFirstNameMale(['Major','U. Major','I. Major']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer'])
                                             ])

          self.FirstLastNameList([      InnLastName(['Bigg']),
                                              InnLastName(['Butt']),
                                              InnLastName(['Cheap']),
                                              InnLastName(['Daley']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Free']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Hard']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Rear']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['White']) 
 
                                             ])
                                             
          self.SecondLastNameList([      InnLastName(['Analicker']),
                                              InnLastName(['Djerkov']),
                                              InnLastName(['Ho']),
                                              InnLastName(['Hoar']),
                                              InnLastName(['Jackov','Jakov']),
                                              InnLastName(['Liquor','Likker','Licker']),
                                              InnLastName(['Mann','Mannlova'])
                                             ])
                                             
class InnNameGenSelector():
     GeneratorList = []
     
     def __init__(self):
          for subclass in InnNameGenerator.__subclasses__():
               item = subclass()
               for x in range(0, item.Priority):
                    self.GeneratorList.append([item.ID, item])
               
     def RandomGenerator(self,):
          Generator = None
          
          Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
                              
          return Generator 
          
     def GetGeneratorsSequential(self, bAllowPromo = True, Type = None):
          GeneratorList = []
          AllowedTypes = []
          
          if not Type is None:
               AllowedTypes = [Type] 
          else:
               AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
          if bAllowPromo:
               AllowedTypes.append(GeneratorType.Promo)

          for subclass in InnNameGenerator.__subclasses__():
               gen = subclass()

               if gen.Type in AllowedTypes:
                    GeneratorList.append(gen)
               
          return GeneratorList  
          
     def GetGenerator(self, iGen):
          Generator = None 
          
          if len(self.GeneratorList) > 0:
               for gen in self.GeneratorList :
                    if gen[1].ID == iGen:
                         Generator = gen[1]
                         break
                         
          return Generator 
                         

          
def GetInnName(gender, iGeneratorNo = 0):
     sName = ""
     
     Generator = None
     GenType = None 
     HistoryQ = None 
     
     if gender == Gender.Neuter:
          if CoinFlip():
               gender = Gender.Female
          else:
               gender = Gender.Male
     
     if not InnNameHistoryQ is None:
          HistoryQ = InnNameHistoryQ
     
     GenSel = InnNameGenSelector()
     if iGeneratorNo != 0:
          gen = GenSel.GetGenerator(iGeneratorNo)
     else:
          gen = GenSel.RandomGenerator()
          while not HistoryQ.PushToHistoryQ(gen.ID):
               gen = GenSel.RandomGenerator()
     
     if not gen is None:
          #print("Innuendo name generator #" + str(gen.ID) + " selected for " + str(gender))
          sName = gen.GetName(gender)

     
     return sName 