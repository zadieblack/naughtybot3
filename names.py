#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Names module

from random import *
from util import *
from gen import *

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
               'Gertrude',
               'Gisele',
               'Gwynneth',
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
               'Luba',
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
               'Diego',
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
          
          self.List = ["Analicker",
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
        super().__init__()

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
          
class InnNameGenerator(Generator):
     def __init__(self, ID = -1, Priority = GenPriority.Normal,Type = GeneratorType.Normal, 
                  AllowedGender = Gender.Neuter):
        super().__init__(ID = ID, Priority = Priority, Type = Type)
          
        self._Default = DefaultLastName.FirstLastName
          
        self._FirstNameFemaleList = WordList()
        self._FirstNameMaleList = WordList()
        self._FirstLastNameList = WordList()
        self._SecondLastNameList = WordList()
        self._LastNameList = WordList()
        self._AllowedGender = AllowedGender

     def GenderAllowed(self, gend):
        bIsAllowed = False

        if self._AllowedGender == Gender.Neuter:
            bIsAllowed = True
        elif self._AllowedGender == gend:
            bIsAllowed = True

        return bIsAllowed
          
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
              if self._AllowedGender == Gender.Female:
                  gend = Gender.Female
              elif self._AllowedGender == Gender.Male:
                  gend = Gender.Male
              else:
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

          iRand = randint(1,10)
          if iRand == 10:
              iRand = randint(1,3)

              if iRand == 1:
                  sName = "Dr. " + sName
              elif iRand == 2:
                  sName = sName + ", M.D."
              elif iRand == 3:
                  sName = sName + ", PhD"
                    
          return sName 
         

# Name: Verb/Adjective - Noun(dick)
class InnNameGen1a(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita','Anita C.']),
                                              InnFirstNameFemale(['Eden']),
                                              InnFirstNameFemale(['Fonda']),
                                              InnFirstNameFemale(['Ivana','Ivana C.']),
                                              InnFirstNameFemale(['Juana','Juana C.']),
                                              InnFirstNameFemale(['Juanita']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['C. Mya','C. Maya']),
                                              InnFirstNameFemale(['Maya C.']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Olive','Olivia','Olive R.']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Onya','P. Onya','I.M. Onya']),
                                              InnFirstNameFemale(['Sia','I. Sia']),
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
                                              InnLastName(['Bone']),
                                              InnLastName(['Cox']),
                                              InnLastName(['Dick','Dicks','Dix','Dickons']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knobb']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Koch','Kochs']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Sachs','Sachs','Sax']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Stiffy']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood'])
                                             ])

# Name: Verb/Adjective - Noun(pussy)
class InnNameGen1b(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita','Anita C.']),
                                              InnFirstNameFemale(['Eden']),
                                              InnFirstNameFemale(['Fonda']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Ivana','Ivana C.']),
                                              InnFirstNameFemale(['Juana','Juana C.']),
                                              InnFirstNameFemale(['Juanita']),
                                              InnFirstNameFemale(['Lucy']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['Minnie']),
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
                                              InnFirstNameFemale(['Yu Mi'])
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Dewey']),
                                              InnFirstNameMale(['Dixon']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['I.C.']),
                                              InnFirstNameMale(['Juan','I. Juan']),
                                              InnFirstNameMale(['Phil','Phil N.','Philmore','Phillip']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Randy']),
                                              InnFirstNameMale(['Rex','I. Rex']),
                                              InnFirstNameMale(['Ryder']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                              InnFirstNameMale(['Oliver']),
                                              InnFirstNameMale(['Juan A.'])
                                             ])

          self.FirstLastNameList([      InnLastName(['Bare']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Deeper']),
                                              InnLastName(['Dicker']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Fish']),
                                              InnLastName(['Furry','Fuzzie']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Horny']),
                                              InnLastName(['Knotty']),
                                              InnLastName(['Knuttin']),
                                              InnLastName(['Lady']),
                                              InnLastName(['Likker']),
                                              InnLastName(['Loose']),
                                              InnLastName(['Love']),
                                              InnLastName(['Major']),
                                              InnLastName(['Misty']),
                                              InnLastName(['Moist','Moister']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Rubber']),
                                              InnLastName(['Shy']),
                                              InnLastName(['Strange']),
                                              InnLastName(['Sweet']),
                                              InnLastName(['Wet']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Beaver']),
                                              InnLastName(['Button']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cooter']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Flaps']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Grotch']),
                                              InnLastName(['Hyman']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Lipps']),
                                              InnLastName(['McCreviss']),
                                              InnLastName(['Muff','Muffin']),
                                              InnLastName(['Peach','Peaches']),
                                              InnLastName(['Pearl']),
                                              InnLastName(['Pie']),
                                              InnLastName(['Puss']),
                                              InnLastName(['Posey']),
                                              InnLastName(['Snatch']),
                                             ])
                                         
# Name: Verb/Adjective - Noun(butts)
class InnNameGen1c(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita','Anita C.']),
                                              InnFirstNameFemale(['Eden']),
                                              InnFirstNameFemale(['Fonda']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Ivana','Ivana C.']),
                                              InnFirstNameFemale(['Juana','Juana C.']),
                                              InnFirstNameFemale(['Juanita']),
                                              InnFirstNameFemale(['C. Mya','C. Maya']),
                                              InnFirstNameFemale(['Maya C.']),
                                              InnFirstNameFemale(['Olive','Olivia','Olive R.']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Satin']),
                                              InnFirstNameFemale(['P. Inya','Inya']),
                                              InnFirstNameFemale(['Onya','P. Onya'])
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Dixon']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['I.C.']),
                                              InnFirstNameMale(['Juan','I. Juan']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Ryder','Rider']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                              InnFirstNameMale(['Oliver']),
                                             ])

          self.FirstLastNameList([      InnLastName(['Apple']),
                                              InnLastName(['Bare']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Broad']),
                                              InnLastName(['Brown']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Major']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['Twerking']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Bootay','Bootie','Buty']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Bum','Bumm']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Caboose']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Crack']),
                                              InnLastName(['Donk']),
                                              InnLastName(['Duff']),
                                              InnLastName(['Fanny']),
                                              InnLastName(['Hump','Humps']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['McCreviss']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Moon']),
                                              InnLastName(['Patootie']),
                                              InnLastName(['Pooper','Puhper']),
                                              InnLastName(['Pooter']),
                                              InnLastName(['Rack','Racks']),
                                              InnLastName(['Rump']),
                                              InnLastName(['Schitter']),
                                              InnLastName(['Tail']),
                                              InnLastName(['Tush','Tushie','Tushy']),
                                             ])

# Name: Verb/Adjective - Noun(tits)
class InnNameGen1d(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita C.']),
                                              InnFirstNameFemale(['Fonda']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Ivana C.']),
                                              InnFirstNameFemale(['Juana','Juana C.']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['C. Mya','C. Maya']),
                                              InnFirstNameFemale(['Maya C.']),
                                              InnFirstNameFemale(['Olive','Olivia','Olive R.']),
                                              InnFirstNameFemale(['Onya','P. Onya']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Satin']),
                                              InnFirstNameFemale(['Sia', 'I. Sia']),
                                              
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Chester']),
                                              InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Creamer']),
                                              InnFirstNameMale(['Dixon']),
                                              InnFirstNameMale(['Holden']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['I.C.']),
                                              InnFirstNameMale(['Juan','I. Juan']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Ryder']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                              InnFirstNameMale(['Oliver'])
                                             ])

          self.FirstLastNameList([      InnLastName(['Bare']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Bouncy']),
                                              InnLastName(['Busty']),
                                              InnLastName(['Chubby']),
                                              InnLastName(['Deedee']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Jumbo']),
                                              InnLastName(['Large']),
                                              InnLastName(['Major']),
                                              InnLastName(['Milky','Milk']),
                                              InnLastName(['Plump']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Blimps']),
                                              InnLastName(['Bongos']),
                                              InnLastName(['Bewbs','Boobs','Boobies','Bewbees']),
                                              InnLastName(['Brest','Bresst']),
                                              InnLastName(['Canns']),
                                              InnLastName(['Hangers']),
                                              InnLastName(['Hooters']),
                                              InnLastName(['Jubblies']),
                                              InnLastName(['Juggs']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Mounds']),
                                              InnLastName(['Nippel']),
                                              InnLastName(['Pillows']),
                                              InnLastName(['Rack','Racks']),
                                              InnLastName(['Tatas']),
                                              InnLastName(['Titts','Tiddies']),
                                              InnLastName(['Udders']),
                                             ])

# Name: Adjective Adverb-Verber
class InnNameGen2(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
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
                                              InnLastName(['Fister']),
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
     
# Name: Amanda Faulk, Kanye Kuhmm-Galey
class InnNameGen3(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
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
                                              InnLastName(['Kuhmm','Khumm']),
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
                                              InnLastName(['Moorehard'])
                                             ])
                                             
                                             
class InnNameGen4Dick(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._AllowedGender = Gender.Male
          self._Default = DefaultLastName.FirstLastName
                                             
          self.FirstNameMaleList([      InnFirstNameMale(['Bone','I. Bone']),
                                              InnFirstNameMale(['Dick']),
                                              InnFirstNameMale(['Lance','I. Lance']),
                                              InnFirstNameMale(['Phil','Phil N.','Philip','I. Philip']),
                                              InnFirstNameMale(['Philmore','I. Philmore']),
                                              
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bottom','Bottoms','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Butt','Butte','Butts']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Hose']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Menn']),
                                              InnLastName(['Mommes']),
                                              InnLastName(['Pie','Pies','Pye']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Twatt','Twatts']),
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Daley']),
                                   InnLastName(['Deeper']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley'])
                                             ])

class InnNameGen4Eden(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._AllowedGender = Gender.Female
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([
                                              InnFirstNameFemale(['Eden','Eden','Eden','Eden A.','Eden R.']),
                                         ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Boner']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Crack']),
                                              InnLastName(['Dick']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Hole']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner'])
                                             ])
                                             
          self.SecondLastNameList([           InnLastName(['Daley']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gladly']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Sweetly']),
                                             ])

class InnNameGen4FondaCraven(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']), 
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Craven','I.M. Craven']),
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bone','Boner','Bones']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Come','Kuhm','Kumm']),
                                              InnLastName(['Cox']),
                                              InnLastName(['Crack']),
                                              InnLastName(['Dick']),
                                              InnLastName(['Djizz']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Mannlove']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood']),
                                             ])
                                             
          self.SecondLastNameList([           InnLastName(['Daley']),
                                              InnLastName(['Knightly']),
                                             ])
   
class InnNameGen4Rex(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._AllowedGender = Gender.Male
          self._Default = DefaultLastName.FirstLastName
                                             
          self.FirstNameMaleList([      InnFirstNameMale(['Rex','I. Rex']),                                       
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Ho','Hose']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Menn']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Starfish']),
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Daley']),
                                   InnLastName(['Deeper']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley'])
                                             ])


class InnNameGen4Rhoda(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([      InnFirstNameFemale(['Rhoda']),
                                              InnFirstNameFemale(['Sharon','I.M. Sharon']),
                                              InnFirstNameFemale(['Yu Mi'])
                                         ])
                                             
          self.FirstNameMaleList([      InnFirstNameMale(['Holden','Holden']),
                                              InnFirstNameMale(['Jack','Jack N.']),
                                              InnFirstNameMale(['Pat','Pat N.']),
                                              
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bone','Boner','Bones']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cox','Koch']),
                                              InnLastName(['Dick','Dicks','Dix']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Ho','Hose']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knuttz']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Kuhnt']),
                                              InnLastName(['Mann']),
                                              InnLastName(['McGrotch']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Peter','Peters']),
                                              InnLastName(['Pohl']),
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

class InnNameGen4Ryder(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._AllowedGender = Gender.Male
          self._Default = DefaultLastName.FirstLastName
                                             
          self.FirstNameMaleList([InnFirstNameMale(['Ryder','I. Ryder']),])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Boottay']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Clam','Clamm',]),
                                              InnLastName(['Flower']),
                                              InnLastName(['Furrow']),
                                              InnLastName(['Hole','Holes']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Kreviss']),
                                              InnLastName(['Kuhnt','K. Hunt']),
                                              InnLastName(['Mann']),
                                              InnLastName(['Snatch']),
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Daley']),
                                   InnLastName(['Deeper']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Hard','Harder']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley'])
                                             ])

class InnNameGen4Sia(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._AllowedGender = Gender.Female
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([      InnFirstNameFemale(['Sia','Sia','Sia','I. Sia']),
                                         ])
                                             
          self.FirstLastNameList([      InnLastName(['Beaver']),
                                              InnLastName(['Bone','Boner',]),
                                              InnLastName(['Brest','Bresst']),
                                              InnLastName(['Bottom',]),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Butt',]),
                                              InnLastName(['Clam','Clamm',]),
                                              InnLastName(['Cox']),
                                              InnLastName(['Crack']),
                                              InnLastName(['Dick']),
                                              InnLastName(['Fatone']),
                                              InnLastName(['Furrow',]),
                                              InnLastName(['Grotch']),
                                              InnLastName(['Ho',]),
                                              InnLastName(['Hole',]),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Nutt']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Kuhnt']),
                                              InnLastName(['Moon']),
                                              InnLastName(['Pecker',]),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rack',]),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Snatch']),
                                              InnLastName(['Stiffy']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood'])
                                             ])
                                             
          self.SecondLastNameList([           InnLastName(['Daley']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Gladly']),
                                              InnLastName(['Knightly']),
                                             ])

class InnNameGen4Seymour(InnNameGenerator):
     def __init__(self):
          super().__init__()
         
          self._AllowedGender = Gender.Male
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameMaleList([        InnFirstNameMale(['Seymour','Seymour','Seymour','I. Seymour'])
                                              
                                             ])
                                             
          self.FirstLastNameList([      InnLastName(['Beavers']),
                                              InnLastName(['Bones','Boners']),
                                              InnLastName(['Titts']),
                                              InnLastName(['Bottoms']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Butts']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Clams','Clamms',]),
                                              InnLastName(['Cox']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Dick','Dicks','Dix']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Hose']),
                                              InnLastName(['Holes']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Johnsons']),
                                              InnLastName(['Knuttz','Nutts']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Melons']),
                                              InnLastName(['Peckers']),
                                              InnLastName(['Peters']),
                                              InnLastName(['Racks']),
                                              InnLastName(['Sachs','Sachs','Sax']),
                                              InnLastName(['Woods'])
                                             ])
                                             
          self.SecondLastNameList([           InnLastName(['Daley']),
                                              InnLastName(['Freely']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Gladly']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Stiffley'])
                                             ])

# Name: Noun (Dick) - Adjective
class InnNameGen5(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Ima']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['I.M.']),
                                              InnFirstNameFemale(['Sia', 'I. Sia'])
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Ben','I. Ben']),
                                              InnFirstNameMale(['Dick','C. Dick']),
                                              InnFirstNameMale(['Gaylord']),
                                              InnFirstNameMale(['Juan U.']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter','Pete R.']),
                                              InnFirstNameMale(['Rod']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
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
class InnNameGen6Ho(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Ima']),
                                              InnFirstNameFemale(['Issa']),
                                              InnFirstNameFemale(['Ivana',]),
                                              InnFirstNameFemale(['Juana','I. Juana']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Rhoda','I. Rhoda']),
                                              InnFirstNameFemale(['Wanda','I. Wanda'])
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Ben A.',]),
                                              InnFirstNameMale(['Craven A.','I.M. Craven A.']),
                                              InnFirstNameMale(['Dick','Dick A.','I. Dick A.']),
                                              InnFirstNameMale(['Juan A.']),
                                              InnFirstNameMale(['Major','U. Major']),
                                              InnFirstNameMale(['Penn S.']),
                                              InnFirstNameMale(['Peter']),
                                              InnFirstNameMale(['Randy']),
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
                                             
          self.SecondLastNameList([      InnLastName(['Ho','Ho','Ho','Hoar']),
                                             ])


# Name: Juan A. Nell
class InnNameGen7Anal(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']),
                                              InnFirstNameFemale(['Ivana']),
                                              InnFirstNameFemale(['Juana','I. Juana',]),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['Olive']),
                                              InnFirstNameFemale(['Sia','I. Sia']),
                                              InnFirstNameFemale(['Sharon','I.M. Sharon']),
                                         ])

          self.FirstNameMaleList([      InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Dew N.']),
                                              InnFirstNameMale(['I.C.']),
                                              InnFirstNameMale(['I. Juan','Juan']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer'])
                                             ])

          self.FirstLastNameList([      InnLastName(['A. Nell']),
                                             ])
                                             
          self.SecondLastNameList([      InnLastName(['Cherry']),
                                              InnLastName(['Daily']),
                                              InnLastName(['Deeper']),
                                              InnLastName(['Dickens']),
                                              InnLastName(['Djiz']),
                                              InnLastName(['Faulk']),
                                              InnLastName(['Fisting']),
                                              InnLastName(['Gape','Gaper']),
                                              InnLastName(['Gayley']),
                                              InnLastName(['Harder']),
                                              InnLastName(['Hoar']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Rimming']),
                                              InnLastName(['Sachs']),
                                              InnLastName(['Sexton']),
                                              InnLastName(['Topping']),
                                             ])

# Verb Noun-Verb(ing)
# Seymour Titt-Likking
class InnNameGen8(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']),
                                              InnFirstNameFemale(['Ivana']),
                                              InnFirstNameFemale(['Juana','I. Juana','U. Juana']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['C. Mya','C. Maya']),
                                              InnFirstNameFemale(['Maya C.']),
                                              InnFirstNameFemale(['Olive']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Sharon','I.M. Sharon']),
                                              InnFirstNameFemale(['Wanda','I. Wanda']) 
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Craven']),
                                              InnFirstNameMale(['Dew N.']),
                                              InnFirstNameMale(['Gaylord']),
                                              InnFirstNameMale(['Juan', 'Juan A.','I. Juan','I. Juan A.']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                             ])

          self.FirstLastNameList([      InnLastName(['A. Nell']),
                                              InnLastName(['Butte','Butt']),
                                              InnLastName(['Cox','Koch','Kochs']),
                                              InnLastName(['Daley']),
                                              InnLastName(['Dick']),
                                              InnLastName(['Duff']),
                                              InnLastName(['Fanny']),
                                              InnLastName(['Gay']),
                                              InnLastName(['Hard']),
                                              InnLastName(['Hump']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Knobb','Nobb']),
                                              InnLastName(['Knockers']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Knutt','Nutt']),
                                              InnLastName(['Krevice','Crevice','Creviss','Kreviss']),
                                              InnLastName(['Kuhm','Khum']),
                                              InnLastName(['Lady']),
                                              InnLastName(['Mann']),
                                              InnLastName(['Melon']),
                                              InnLastName(['Mouth']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Peter']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Reckdle']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Throat']),
                                              InnLastName(['Titt']),
                                              InnLastName(['Toe']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Whett']),
                                              InnLastName(['Wood'])
                                              
                                             ])
                                             
          self.SecondLastNameList([      InnLastName(['Balling']),
                                              InnLastName(['Boning']),
                                              InnLastName(['Creaming']),
                                              InnLastName(['Cumming']),
                                              InnLastName(['Djizzing']),
                                              InnLastName(['Faulking']),
                                              InnLastName(['Feltching']),
                                              InnLastName(['Fisting']),
                                              InnLastName(['Gaping']),
                                              InnLastName(['Humping']),
                                              InnLastName(['Jacking']),
                                              InnLastName(['Jerking']),
                                              InnLastName(['Knightly']),
                                              InnLastName(['Likking']),
                                              InnLastName(['Loving']),
                                              InnLastName(['Mounting']),
                                              InnLastName(['Popping']),
                                              InnLastName(['Riding']),
                                              InnLastName(['Rimming']),
                                              InnLastName(['Rubbing']),
                                              InnLastName(['Schtupping']),
                                              InnLastName(['Spanking']),
                                              InnLastName(['Stroking']),  
                                              InnLastName(['Stuffing']),
                                              InnLastName(['Sucking']),
                                             ])
   
# Anita Blow-Jobb, Hadda Rimm-Jobb, Ivana Buub-Jobb, I.M. Craven Hand-Jobb
class InnNameGen9(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.FirstLastName
          
          self.FirstNameFemaleList([   InnFirstNameFemale(['Anita']),
                                              InnFirstNameFemale(['Fonda','I.M. Fonda']),
                                              InnFirstNameFemale(['Hatta','Hadda']),
                                              InnFirstNameFemale(['Ivana']),
                                              InnFirstNameFemale(['Juana','I. Juana','U. Juana']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Olive']),
                                              InnFirstNameFemale(['Ophelia']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Sharon','I.M. Sharon']),
                                              InnFirstNameFemale(['Wanda','I. Wanda']) 
                                         ])
          #'Dick','Gaylord','Hans','Penn S.','Peter','Rod','Willie','Willy'
          self.FirstNameMaleList([      InnFirstNameMale(['Craven','I.M. Craven']),
                                              InnFirstNameMale(['Dew N.']),
                                              InnFirstNameMale(['Earl E.']),
                                              InnFirstNameMale(['Juan', 'Juan A.','I. Juan','I. Juan A.']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameFemale(['Randy']),
                                              InnFirstNameMale(['Sawyer','I. Sawyer']),
                                             ])

          self.FirstLastNameList([      InnLastName(['Asse-Jobb']),
                                              InnLastName(['Blow-Jobb']),
                                              InnLastName(['Buub-Jobb','Boob-Jobb','Bewb-Jobb']),
                                              InnLastName(['Butt-Jobb','Butte-Jobb']),
                                              InnLastName(['Foot-Jobb']),
                                              InnLastName(['Gumm-Jobb']),
                                              InnLastName(['Hand-Jobb']),
                                              InnLastName(['Panty-Jobb']),
                                              InnLastName(['Rimm-Jobb','Rim-Jobb']),
                                              InnLastName(['Stroke-Jobb']),
                                              InnLastName(['Titt-Jobb']),
                                              
                                             ])

# Name: Adjective - Dick (noun)
class InnNameGenAdjDick(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([          InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['Minnie']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Ruby']),
                                              InnFirstNameFemale(['Sable']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Scarlett']),
                                              
                                         ])

          self.FirstNameMaleList([            
                                              InnFirstNameMale(['Beef E.']),
                                              InnFirstNameMale(['Dewey']),
                                              InnFirstNameMale(['Harder','Hardy','Hardy']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['Long']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              InnFirstNameMale(['Randy']),
                                              InnFirstNameMale(['Rich']),
                                              
                                             ])

          self.FirstLastNameList([            InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Dark']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Hard']),
                                              InnLastName(['Hung']),
                                              InnLastName(['Long']),
                                              InnLastName(['Major']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Power']),
                                              InnLastName(['Stiff']),
                                              InnLastName(['Tall']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['Whett']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([
                                              InnLastName(['Bone']),
                                              InnLastName(['Cox']),
                                              InnLastName(['Dick']),
                                              InnLastName(['Johnson']),
                                              InnLastName(['Koch']),
                                              InnLastName(['Pecker']),
                                              InnLastName(['Peter','Peters']),
                                              InnLastName(['Pohl']),
                                              InnLastName(['Rodd','Rohdd']),
                                              InnLastName(['Schaft','Shaft']),
                                              InnLastName(['Schlong']),
                                              InnLastName(['Stiffy']),
                                              InnLastName(['Wang']),
                                              InnLastName(['Weiner']),
                                              InnLastName(['Wood'])
                                             ])

# Name: Adjective - Balls (noun)
class InnNameGenAdjBalls(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([          InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Love']),
                                              InnFirstNameFemale(['Minnie']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Puffy']),
                                              
                                         ])

          self.FirstNameMaleList([            
                                              InnFirstNameMale(['Beef E.']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['Long']),
                                              InnFirstNameMale(['Lowe']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              
                                             ])

          self.FirstLastNameList([            InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Dangle']),
                                              InnLastName(['Dark']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Hung']),
                                              InnLastName(['Lo']),
                                              InnLastName(['Major']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Round']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['White']),
                                             ])
                                             
          self.SecondLastNameList([
                                              InnLastName(['Balls','Bawls']),
                                              InnLastName(['Sachs','Sachs','Sacks','Sax']),
                                              InnLastName(['Scrowtum','Skrotum']),
                                             ])

# Name: Adjective - Pussy (noun)
class InnNameGenAdjPussy(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([          InnFirstNameFemale(['Cherry']),
                                              InnFirstNameFemale(['Dusty']),
                                              InnFirstNameFemale(['Ginger']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Lucy']),
                                              InnFirstNameFemale(['Minnie']),
                                              InnFirstNameFemale(['Misty']),
                                              InnFirstNameFemale(['Nastya']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Ruby']),
                                              InnFirstNameFemale(['Sable']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Satin']),
                                              InnFirstNameFemale(['Yu Mi'])
                                              
                                         ])

          self.FirstNameMaleList([            
                                              InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Fuzzy']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              
                                             ])

          self.FirstLastNameList([      InnLastName(['Bare']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Deeper']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Fish']),
                                              InnLastName(['Furry','Fuzzie']),
                                              InnLastName(['Goode']),
                                              InnLastName(['Horny']),
                                              InnLastName(['Knotty']),
                                              InnLastName(['Lady']),
                                              InnLastName(['Loose']),
                                              InnLastName(['Major']),
                                              InnLastName(['Misty']),
                                              InnLastName(['Moist','Moister']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Shy']),
                                              InnLastName(['Sweet']),
                                              InnLastName(['Tight','Tite']),
                                              InnLastName(['Wet','Whett']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Beaver']),
                                              InnLastName(['Button']),
                                              InnLastName(['Cherry']),
                                              InnLastName(['Clam','Clamm','Clams','Clamms','Clamz','Clammz']),
                                              InnLastName(['Cooter','Kooter']),
                                              InnLastName(['Cracks']),
                                              InnLastName(['Bush']),
                                              InnLastName(['Flaps']),
                                              InnLastName(['Furrows']),
                                              InnLastName(['Grotch']),
                                              InnLastName(['Hole']),
                                              InnLastName(['Hyman']),
                                              InnLastName(['Kootch']),
                                              InnLastName(['Krevises']),
                                              InnLastName(['Kuntz']),
                                              InnLastName(['Lipps']),
                                              InnLastName(['McCreviss']),
                                              InnLastName(['Muff','Muffin']),
                                              InnLastName(['Peach','Peaches']),
                                              InnLastName(['Pearl']),
                                              InnLastName(['Pie','Pye']),
                                              InnLastName(['Puss']),
                                              InnLastName(['Posey']),
                                              InnLastName(['Slitt']),
                                              InnLastName(['Snatch']),
                                             ])

# Name: Adjective - Ass (noun)
class InnNameGenAdjAss(InnNameGenerator):
     def __init__(self):
          super().__init__()
          
          self._Default = DefaultLastName.SecondLastName
          
          self.FirstNameFemaleList([          InnFirstNameFemale(['Apple']),
                                              InnFirstNameFemale(['Bubble']),
                                              InnFirstNameFemale(['Honey']),
                                              InnFirstNameFemale(['Lotta']),
                                              InnFirstNameFemale(['Lucy']),
                                              InnFirstNameFemale(['Peach']),
                                              InnFirstNameFemale(['Rosie']),
                                              InnFirstNameFemale(['Sandy']),
                                              InnFirstNameFemale(['Satin']),
                                              InnFirstNameFemale(['Yu Mi'])
                                              
                                         ])

          self.FirstNameMaleList([            
                                              InnFirstNameMale(['Deepa']),
                                              InnFirstNameMale(['Harry']),
                                              InnFirstNameMale(['Hugh']),
                                              InnFirstNameMale(['Joose E.']),
                                              InnFirstNameMale(['Lucious']),
                                              InnFirstNameMale(['Major']),
                                              InnFirstNameMale(['Max']),
                                              
                                             ])

          self.FirstLastNameList([      InnLastName(['Apple']),
                                              InnLastName(['Bigg']),
                                              InnLastName(['Black']),
                                              InnLastName(['Broad']),
                                              InnLastName(['Brown']),
                                              InnLastName(['Fatt']),
                                              InnLastName(['Lucious']),
                                              InnLastName(['Pink']),
                                              InnLastName(['Sweet']),
                                              InnLastName(['Thicke']),
                                              InnLastName(['White'])
                                             ])
                                             
          self.SecondLastNameList([InnLastName(['Bootay','Bootie','Buty']),
                                              InnLastName(['Bottom','Bottoms']),
                                              InnLastName(['Brownie']),
                                              InnLastName(['Bum','Bumm']),
                                              InnLastName(['Buhnz']),
                                              InnLastName(['Butts','Butt','Butte']),
                                              InnLastName(['Caboose']),
                                              InnLastName(['Cheeks']),
                                              InnLastName(['Crack']),
                                              InnLastName(['Donk']),
                                              InnLastName(['Duff']),
                                              InnLastName(['Fanny']),
                                              InnLastName(['Janus']),
                                              InnLastName(['Knott']),
                                              InnLastName(['Moon']),
                                              InnLastName(['Patootie']),
                                              InnLastName(['Pooper','Puhper']),
                                              InnLastName(['Pooter']),
                                              InnLastName(['Rump']),
                                              InnLastName(['Schitter']),
                                              InnLastName(['Tail']),
                                              InnLastName(['Tush','Tushie','Tushy']),
                                             ])

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
     
     GenSel = GeneratorContainer(InnNameGenerator, HistoryQ = HistoryQ)
     if iGeneratorNo != 0:
          gen = GenSel.GetGenerator(iGeneratorNo)
     else:
         gen = GenSel.RandomGenerator()

         iLoops = 0
         while not gen.GenderAllowed(gender) and iLoops < MAX_SEARCH_LOOPS:
             gen = GenSel.RandomGenerator()
             iLoops += 1
     
     if not gen is None:
          #print("Innuendo name generator #" + str(gen.ID) + " selected for " + str(gender))
          sName = gen.GetName(gender)

     
     return sName 