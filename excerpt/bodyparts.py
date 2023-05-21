#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from collections import namedtuple
from random import *
import re 

from util import *
#from excerpt.ex_helpers import *
from excerpt.ex_helpers import *
import names as names

SkinColors = ["almond: color,asian",
              "beige: color,male",
              "black x4: color,poc",
              "bronze: color,poc",
              "bronzed: color,poc",
              "brown: color,poc",
              "chococlate: color,poc",
              "chocolate-colored: color,poc",
              "coffee-colored: color,poc",
              "copper-skinned: color,poc",
              "creamy: color,cauc,female",
              "cream-colored: color,cauc,female",
              "dark: color,poc",
              "dark brown: color,poc",
              "ebony: color,poc,female",
              "fair: color,cauc,female",
              "freckled: color,cauc",
              "fresh pink: color,cauc,female",
              "honeyed: color",
              "light: color,cauc",
              "light brown",
              "mocha: color,poc",
              "pale: color,cauc",
              "pink: color,cauc",
              "porcelain: color,cauc",
              "rosy: color,cauc,female",
              "tan: color,poc",
              "tanned: color,cauc",
              "sun-bronzed: color,cauc",
              "sun-browned: color,cauc",
              "sun-kissed: color,cauc",
              "well-tanned:color,cauc",
              "white: color,cauc",
              "light brown","mocha","tan",
             ]

#Race = namedtuple("Race", "Name HairColor EyeColor SkinColor NipColor")

@dataclass
class Race:
    Name: str = ""
    EyeColor: list = field(default_factory=list)
    HairColor: list = field(default_factory=list)
    NipColor: list = field(default_factory=list)
    SkinColor: list = field(default_factory=list)
    FemHairStyle: list = field(default_factory=list)

RaceCauc  = Race(Name = "caucasian",
                 EyeColor = ["amber","blue","brown","dark","gray","green","hazel"],
                 HairColor = ["black","blonde","brown","dark","gray","red"],
                 NipColor = ["brown","dark","pink","rosy","tan"],
                 SkinColor = ["beige","creamy","freckled","fresh pink","honeyed","light","pale","pink","porcelain","rosy","tanned","sun-bronzed","sun-browned","sun-kissed","white"],
                 FemHairStyle = ["big","bobbed","braids","curls","long","pigtails","pixie","ponytail","short","updo"]
                )
RacePOC   = Race(Name = "poc",
                 EyeColor = ["amber","brown","dark",],
                 HairColor = ["black","brown","dark",],
                 NipColor = ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"],
                 SkinColor = ["black","beige","bronze","bronzed","brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","ebony","honeyed","light brown","mocha","tan"],
                 FemHairStyle = ["cornrows","curls","fro","kinky","long","pixie","short","updo"]
               )
RaceAsian = Race(Name = "asian",
                 EyeColor = ["brown","dark",],
                 HairColor = ["black","brown","dark",],
                 NipColor = ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"],
                 SkinColor = ["almond","beige","brown","creamy","freckled","light","light brown","pale","porcelain","tan","sun-bronzed","sun-browned","sun-kissed","white"],
                 FemHairStyle = ["braids","long","pigtails","pixie","ponytail","short",]
                )



class BodyParts(NounPhrase):
    def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.AddSkinColors = False 

    def AdjList(self, NewAdjList):
        if self.AddSkinColors:
            for color in SkinColors:
                NewAdjList.append(color)

        NewAdjList.sort()
        super().AdjList(NewAdjList)

@dataclass
class GenPhysTraits:
    FirstName: str = ""
    LastName: str = ""
    Gender: str = ""
    Race: Race = None
    Height: str = ""
    IsFit: bool = False
    PubeStyle: str = ""

#GenPhysTraits = namedtuple("GenPhysTraits",
#                           "FirstName LastName Gender Race PubeStyle",
#                           defaults = ["","","",None,""]
#                          )
class Lover():
    def __init__(self, Gender, NewGenTraits = None):
        self.FirstName = ""
        self.LastName = ""
        self.Gender = ""
        self.Height = ""
        self.IsFit = False
        self.Race = None
        self.RaceName = ""
        self.EyeColor = ""
        self.HairColor = ""
        self.NipColor = ""
        self.SkinColor = ""
        self.IsTan = False
        self.PubeStyle = ""

        self._TagLists = TagLists()

        bRandomize = False

        if NewGenTraits is None or not isinstance(NewGenTraits, GenPhysTraits):
            NewGenTraits = GenPhysTraits()
            bRandomize = True
        
        # Set attributes if not blank, otherwise randomize
        self.Gender = Gender

        if self.Gender == "female":
            self._TagLists.adj_excl.append("male")
        elif self.Gender == "male":
            self._TagLists.adj_excl.append("female")

        if NewGenTraits.FirstName:
            self.FirstName = NewGenTraits.FirstName
        else:
            if self.Gender == "male":
                self.FirstName = names.NamesMale().FirstName()
            else:
                self.FirstName = names.NamesFemale().FirstName()

        if NewGenTraits.LastName:
            self.LastName = NewGenTraits.LastName
        else:
            self.LastName = names.RegularLastNames().GetWord()

        if NewGenTraits.Height:
            self.Height = NewGenTraits.Height
        else:
            self.Height = choice(["tall","medium","medium","short"])

        if not bRandomize:
            self.IsFit = NewGenTraits.IsFit
        else:
            self.IsFit = choice([True,False,False])

        if NewGenTraits.Race and isinstance(Race, NewGenTraits.Race):
            self.Race = NewGenTraits.Race
        else:
            self.Race = choice([RaceCauc,RacePOC,]) # Add RaceAsian

        self.RaceName = self.Race.Name

        self.EyeColor = choice(self.Race.EyeColor)
        self.HairColor = choice(self.Race.HairColor)
        self.NipColor = choice(self.Race.NipColor)
        self.SkinColor = choice(self.Race.SkinColor)

        if not bRandomize:
            self.IsTan = NewGenTraits.IsTan
        else:
            self.IsTan = choice([True,False,False])
        
        LTagLists = self._TagLists

        # Handle race
        if self.RaceName == "caucasian":
            LTagLists.adj_excl.append("poc")
            LTagLists.noun_excl.append("poc")
        elif self.RaceName == "poc":
            LTagLists.adj_excl.append("cauc")
            LTagLists.noun_excl.append("cauc")

        if NewGenTraits.PubeStyle:
            self.PubeStyle = NewGenTraits.PubeStyle
        else:
            self.PubeStyle = choice(["hairy","shaved","trimmed"])

        if self.PubeStyle == "hairy":
            LTagLists.adj_excl.append("shaved")
            LTagLists.adj_excl.append("trimmed")
        elif self.PubeStyle == "trimmed":
            LTagLists.adj_excl.append("shaved")
            LTagLists.adj_excl.append("hairy")
        elif self.PubeStyle == "shaved":
            LTagLists.adj_excl.append("trimmed")
            LTagLists.adj_excl.append("hairy")

        self.HairColor = choice(self.Race.HairColor)
        self.EyeColor = choice(self.Race.EyeColor)
        self.SkinColor = choice(self.Race.SkinColor)
        self.NipColor = choice(self.Race.NipColor)

class Male(NounPhrase):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['athlete: prof,sing',
                         'bachelor: twenties,unmarried,sing',
                         'boy: teen,sing',
                         'brother: poc,sing',
                         'college boy: college,sing',
                         'college guy: college,sing',
                         'cop: prof,sing',
                         'cowboy: prof,sing',
                         'dad: relate,sing',
                         'DILF: relate,sing',
                         'doctor: prof,sing',
                         'gentleman: middleaged,older,wealthy,sing',
                         'husband: relate,married,sing',
                         'father-in-law: father,relate,married,sing',
                         'fighter pilot: prof,sing',
                         'firefighter: prof,sing',
                         'frat boy: college,young,sing',
                         'jock: prof,teen,college,unmarried,sing',
                         'lawyer: prof,sing',
                         'lumberjack: prof,sing',
                         'man x6: std,default,sing',
                         'older man x2: older,sing',
                         'outdoorsman: prof,sing',
                         'single dad: thirties,middleaged,prof,relate,sing',
                         'stay-at-home dad: prof,thirties,middleaged,sing',
                         'stud: strong,handsome,ladiesman,sing',
                         'surfer: prof,sing',
                         'teenage boy: young,sing',
                         'young man x2: std,young,sing',
                        ])
          
          self.AdjList(['athletic: muscular,shape',
                        'authoritative: super',
                        'bald: hair,bald',
                        'balding: hair,bald',
                        'big: size,large',
                        'black x3: color,poc',
                        'blonde x2: hair,cauc',
                        'blue-eyed x3: eyes,cauc',
                        'bearded: facialhair,beard',
                        'bony: slender,',
                        'broad-chested: width,wide',
                        'bronzed: color,tan',
                        'brown-eyed x2: eyes',
                        'brunette x3: hair,cauc',
                        'buff x2: strong,muscular',
                        'dark-eyed: eyes',
                        'clean-cut: facialhair,shaved',
                        'clean-shaven: facialhair,shaved',
                        'chiseled: handsome',
                        'compact: width,narrow,height,short',
                        'copper-skinned: color,poc',
                        'confident: attitude',
                        'dadbod: shape,normal',
                        'dark-skinned: color,poc',
                        'ebony x3: color,poc',
                        'energetic: attitude',
                        'experienced: older',
                        'fatherly: older',
                        'fit: muscular',
                        'goateed: facialhair,goatee',
                        'green-eyed: eyes,cauc',
                        'graying: hair,older',
                        'gruff: attitude,thirties,middleaged,older',
                        'hairy: hairy',
                        'heavily-tattoed: style',
                        'heavy: size,large',
                        'handsome: super',
                        'imposing: super,tall,large',
                        'latino x3: poc',
                        'long-haired: hair',
                        'kinky-haired: hair,poc',
                        'massive: size,large',
                        'mature x3: age,older',
                        'middle-aged: age,middleaged',
                        'moustachioed: facialhair,moustache',
                        'muscular: strong,athletic',
                        'pale: color,cauc',
                        'raven-haired: hair',
                        'redheaded x3: hair,cauc',
                        'shaved: hair, bald',
                        'short-haired: hair',
                        'skinny: slender',
                        'slender: slender',
                        'square-jawed: jawshape,square',
                        'strong: strong',
                        'stubbled: facialhair,stubble',
                        'studly: super',
                        'tall: height,tall',
                        'tanned: color,cauc',
                        'twentysomething: twenties,young,age',
                        'short: height,short',
                        'wealthy: status,rich',
                        'well-built: strong,shape',
                        'white: color,cauc',
                        'young: age,young',
                       ])
               
          self.DefaultNoun('man')
          self.DefaultAdj('bearded')

MalePhysTraits = namedtuple("MalePhysTraits",
                            "AgeCat Age HeightType BodyType HairStyle HasFacialHair FacialHairStyle DickInches IsCircumcised",
                            defaults = ["",0,"","",False,"","",0,None]
                           )

class Man(Lover):
    def __init__(self, NewGenTraits = None, NewMaleTraits = None):
        super().__init__("male", NewGenTraits = NewGenTraits)
        
        self.Noun = ""
        self.Desc = ""
        self.DescWords = ""
        self.AgeCat = ""
        self.Age = 0
        self.HeightType = ""
        self.BodyType = ""
        self.HairStyle = ""
        self.HasFacialHair = False
        self.FacialHairStyle = ""
        self.DickInches = 0
        self.IsCircumcised = False

        LTagLists = self._TagLists

        if NewMaleTraits is None or not isinstance(NewMaleTraits, MalePhysTraits):
            NewMaleTraits = MalePhysTraits()
        
        # Handle age 
        if NewMaleTraits.AgeCat:
            self.AgeCat = NewMaleTraits.AgeCat
        else:
            self.AgeCat = choice(["teen","college","twenties","thirties","middleaged","older"])
                
        if self.AgeCat in ["teen","college","twenties"]:
            LTagLists.adj_excl.append("older")
        else:
            LTagLists.adj_excl.append("young")

        if NewMaleTraits.Age:
            self.Age = NewMaleTraits.Age
        else:
            if self.AgeCat == "teen":
                self.Age = randint(17,19)
            elif self.AgeCat == "college":
                self.Age = randint(20,24)
            elif self.AgeCat == "twenties":
                self.Age = randint(25,29)
            elif self.AgeCat == "thirties":
                self.Age = randint(30,39)
            elif self.AgeCat == "middleaged":
                self.Age = randint(40,55)
            elif self.AgeCat == "older":
                self.Age = randint(55,65)

        # Handle height
        if NewMaleTraits.HeightType:
            self.HeightType = NewMaleTraits.HeightType
        else:
            self.HeightType = choice(["short","medium","tall"])

        # Handle body type
        # TODO: This lacks consistent tags
        if NewMaleTraits.BodyType:
            self.BodyType = NewMaleTraits.BodyType
        else:
            self.BodyType = choice(["slender","medium","muscular","sturdy"])

        if NewMaleTraits.HairStyle:
            self.HairStyle = NewMaleTraits.HairStyle
        else:
            self.HairStyle = choice(["shaved","bald","normal"])

        self.HasFacialHair = NewMaleTraits.HasFacialHair 

        if NewMaleTraits.FacialHairStyle:
            self.FacialHairStyle = NewMaleTraits.FacialHairStyle
        else:
            self.FacialHairStyle = choice(["beard","goatee","moustache","shaved","stubble"])

        # Handle dick size
        if NewMaleTraits.DickInches:
            self.DickInches = NewMaleTraits.DickInches
        else:
            # Yes, we want to favor ridiculous-sized dicks. That
            # makes it funnier.
            self.DickInches = choice([2,
                                      3,
                                      4,
                                      5, 5,
                                      6, 6, 6, 6,
                                      7, 7, 7, 7, 7, 
                                      8, 8, 8, 8, 8,
                                      9, 9, 9, 9,
                                      10,10,10,10,
                                      11,11,11,
                                      12,12,12,
                                      13,13,
                                      14
                                     ])

        if NewMaleTraits.IsCircumcised is None:
            self.IsCircumcised = CoinFlip()
        else:
            self.IsCircumcised = NewMaleTraits.IsCircumcized

        # ===============
        # Setup bodyparts
        # ===============

        # Arms
        self.Arms = ArmsMale(TagLists = LTagLists)

        # Ass

        self.Anus = AnusFemale(TagLists = LTagLists)
        self.Buttocks = ButtocksMale(TagLists = LTagLists)
        self.Ass = AssMale(TagLists = LTagLists)
        self.Ass.Anus = self.Anus
        self.Ass.Buttocks = self.Buttocks

        # Chest 

        self.Chest = ChestMale(TagLists = LTagLists)

        # Eyes

        self.Eyes = EyesMale(TagLists = LTagLists)

        # Facial Hair

        self.FacialHair = FacialHair(TagLists = LTagLists)

        # Hair

        self.Hair = HairMale(TagLists = LTagLists)

        # Jaw

        self.Jaw = JawMale(TagLists = LTagLists)

        # Legs

        self.Legs = LegsMale(TagLists = LTagLists)

        # Muscles

        self.Muscles = MusclesMale(TagLists = LTagLists)

        # Penis

        self.Head = PenisHead(TagLists = LTagLists)
        self.Testicles = Testicles(TagLists = LTagLists)

        PenisTagLists = None
        if self.DickInches > 8:
            PenisTagLists = TagLists(adj_excl = ["smalldick"] + LTagLists.adj_excl,noun_excl = ["bigdick"])
        elif self.DickInches > 5 and self.DickInches < 8:
            PenisTagLists = TagLists(adj_excl = ["bigdick","smalldick"] + LTagLists.adj_excl,noun_excl = ["bigdick","smalldick"])
        else:
            PenisTagLists = TagLists(adj_excl = ["bigdick"] + LTagLists.adj_excl,noun_excl = ["smalldick"])

        if self.IsCircumcised:
            PenisTagLists.adj_excl.append("cut")
        else:
            PenisTagLists.adj_excl.append("uncut")

        self.Penis = Penis(TagLists = PenisTagLists)
        self.Penis.Head = self.Head
        self.Penis.Testicles = self.Testicles

        # Shoulders

        self.Shoulders = ShouldersMale(TagLists = LTagLists)

        # Skin

        self.Skin = SkinMale(TagLists = LTagLists)

        # Body
        if self.HeightType == "short":
            BodyTagLists = TagLists(adj_excl = ["tall"] + LTagLists.adj_excl)
        elif self.HeightType == "tall":
            BodyTagLists = TagLists(adj_excl = ["short"] + LTagLists.adj_excl)
        else:
            BodyTagLists = TagLists(adj_excl = ["short","tall"] + LTagLists.adj_excl)

        self.Body = BodyMale(TagLists = BodyTagLists)
        self.Body.FacialHair = self.FacialHair
        self.Body.Hair = self.Hair
        self.Body.Eyes = self.Eyes
        self.Body.Jaw = self.Jaw
        self.Body.Legs = self.Legs
        self.Body.Skin = self.Skin
        self.Body.Shoulders = self.Shoulders
        self.Body.Muscles = self.Muscles
        self.Body.Chest = self.Chest
        self.Body.Arms = self.Arms
        self.Body.Ass = self.Ass
        self.Body.Penis = self.Penis

        # Bodypart lists
        self.BodyParts = [self.Arms,self.Ass,self.Ass.Anus,
                          self.Buttocks,self.Body,self.Chest,
                          self.Eyes,self.FacialHair,self.Hair,
                          self.Jaw,self.Legs,self.Muscles,
                          self.Penis,self.Head,self.Testicles,
                          self.Shoulders,self.Skin,
                         ]
        self.HeadParts = [self.Eyes,self.FacialHair,self.Hair,
                          self.Jaw,
                         ]
        self.ClothedParts = [self.Arms,self.Chest,self.Eyes,
                             self.FacialHair,self.Hair,self.Jaw,
                             self.Legs,self.Shoulders,self.Skin,
                            ]
        self.NakedDescParts = [self.Ass,self.Body,self.Chest,self.Legs,
                               self.Penis,self.Shoulders,
                              ]
        self.NakedDescPartsInners = [self.Ass,self.Body,self.Chest,self.Legs,
                                     self.Penis,self.Head,self.Testicles,
                                     self.Shoulders,
                                    ]
        self.NaughtyParts = [self.Ass,self.Penis,self.Penis.Head,self.Penis.Testicles]

        self.Man = Male(TagLists = LTagLists)
        self.Noun = self.Man.GetNoun()
        self.Desc = self.Man.FloweryDesc()
        self.DescWords = self.Man.GetDescWordList()

        sCut = ""
        if self.IsCircumcised:
            sCut = "circumcised"
        else:
            sCut = "uncircumcised"

        sAge = "AgeCat: " + self.AgeCat
        sRace = "Race: " + self.RaceName
        sHeightType = "HeightType: " + self.HeightType
        sBodyType = "BodyType: " + self.BodyType
        sDickInches = "DickInches: " + str(self.DickInches) + "\""
        sCirc = "IsCirc: " + str(self.IsCircumcised)
        sPubeStyle = "PubeStyle: " + self.PubeStyle
        sDesc = "[Gender: Male".ljust(20) + sAge.ljust(20) + sRace.ljust(20) + sHeightType.ljust(20) 
        sDesc += sBodyType.ljust(21) + sDickInches.ljust(20) + sCirc.ljust(20) 
        sDesc += sPubeStyle.ljust(19) + "]"
        #sDesc = "My name is " + self.FirstName + " " + self.LastName + ". "
        #sDesc += "I am a " + str(self.Age) + "-year-old " + self.RaceName + " " + self.Gender + ". "
        #sDesc += "I am a " + self.HeightType + ", " + self.BodyType + " man. "
        #sDesc += "I proudly sport a " + str(self.DickInches) + "-inch cock "
        #sDesc += "and I keep my pubes " + self.PubeStyle + "! "
        #sDesc += "Some of my other notable physical characteristics are "
        #sDesc += "my " + self.Eyes.FloweryDesc() + ", "
        #sDesc += "my " + self.Hair.FloweryDesc() + ", "
        #sDesc += "my " + self.Body.FloweryDesc() + ", "
        #sDesc += "my " + self.Skin.FloweryDesc() + ", "
        #sDesc += "and my " + sCut + " " + self.Penis.FloweryDesc() + "."
        #print(sDesc)

#FemPhysTraits = namedtuple("FemPhysTraits",
#                           "AgeCat Age BodyType BustSize HasFakeTits HairStyle IsVirgin",
#                           defaults = ["",0,"","",None,"", None]
#                          )

@dataclass
class FemPhysTraits:
    AgeCat: str = ""
    Age: int = 0
    BodyType: str = ""
    BustSize: str = ""
    HasFakeTits: bool = False
    HairStyle: str = ""
    IsVirgin: bool = False

class Female(NounPhrase):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['bimbo: std,cauc,sing',
                         'black girl: color,poc,sing',
                         'blonde: hair,cauc,sing',
                         'brunette: hair,cauc,sing',
                         'co-ed: std,college,sing',
                         'college girl: std,college,sing',
                         'divorcee: std,older,milf',
                         'fashion model: prof,young,sing',
                         'girl x4: std,young,sing',
                         'housemaid: prof,sing',
                         'housewife: older,milf,prof,sing',
                         'mature woman x2: older,milf,std,sing',
                         'mom: std,mother,older,sing',
                         'nurse: prof,sing',
                         'redhead: hair,cauc,sing',
                         'schoolgirl: prof,young,teen,sing',
                         'secretary: prof,twenties,sing',
                         'single mom: prof,mother,sing',
                         'teacher: prof,older,sing',
                         'teen girl x2: std,young,teen,sing',
                         'teenage girl x2: std,young,teen,sing',
                         'virgin: std,virginal,young,sing',
                         'wife: std,relate,older,sing',
                         'woman x4: default,std,sing',
                         'young woman: default,young,std,sing',
                        ])
          
          self.AdjList(['ample-bosomed: bigtits',
                        'athletic: muscular,shape',
                        #'black x3: color,poc',
                        #'blonde x2: hair,cauc,color',
                        'blue-eyed x3: eyes,cauc',
                        'big-titted: bigtits',
                        'bosomy: bigtits,shape',
                        'bronzed: color,tan',
                        'brown-eyed x2: eyes',
                        #'brunette x3: hair,cauc',
                        'busty: bigtits',
                        'buxom: bigtits',
                        'chubby: plussize,shape',
                        'curly-haired: hair',
                        'curvaceous: curvy,shape',
                        'dark-eyed: eyes',
                        'doe-eyed: eyes',
                        #'ebony x3: color,poc',
                        'fit: muscular',
                        'flat-chested: smalltits',
                        'full-figured: bigtits,shape',
                        'green-eyed: eyes,cauc',
                        'latina x3: poc,color',
                        'kinky-haired: hair,poc',
                        'leggy: longlegs,shape',
                        'little: size,small,short',
                        'matronly: age,older',
                        #'mature x3: age,older',
                        'nubile x2: age,young',
                        'pale: color,cauc',
                        'plump: curvy,plussize,shape',
                        'pig-tailed: hair',
                        'pony-tailed: hair',
                        'prim: virginal,super',
                        #'raven-haired: hair',
                        #'redheaded x3: hair,cauc',
                        'round-bottomed: curvy,shape',
                        'Rubenesque: plussize,shape',
                        'shapely: curvy,bigtits,shape',
                        'short-haired: hair',
                        'skinny: slender',
                        'slender: slender',
                        'stacked: bigtits,shape',
                        'statuesque: bigtits,shape',
                        'tanned: color,cauc',
                        'tight-bodied: slender',
                        #'twentysomething: twenties,young,age',
                        'voluptuous: bigtits,curvy,shape',
                        'waifish: slender',
                        #'white: color,cauc',
                        'wide-bottomed: curvy,shape,bigbutt'
                        #'young: age,young',
                       ])
               
          self.DefaultNoun('woman')
          self.DefaultAdj('busty')

class Woman(Lover):
    def __init__(self, NewGenTraits = None, NewFemTraits = None):
        super().__init__("female", NewGenTraits = NewGenTraits)
        self.Noun = ""
        self.Desc = ""
        self.DescWords = ""
        self.AgeCat = ""
        self.Age = 0
        self.BodyType = ""
        self.HairStyle = ""
        self.BustSize = ""
        self.HasFakeTits = False
        self.IsVirgin = False

        EyeParams = NPParams(sColor = self.EyeColor)
        HairParams = NPParams(sColor = self.HairColor)
        NipParams = NPParams(sColor = self.NipColor)
        SkinParams = NPParams(sColor = self.SkinColor)
        
        LTagLists = self._TagLists

        bRandomize = False

        if NewFemTraits is None or not isinstance(NewFemTraits, FemPhysTraits):
            NewFemTraits = FemPhysTraits()
            bRandomize = True

        if NewFemTraits.AgeCat:
            self.AgeCat = NewFemTraits.AgeCat
        else:
            self.AgeCat = choice(["teen","college","college","twenties","twenties","milf","milf"])
                
        if NewFemTraits.Age > 0 and not bRandomize:
            self.Age = NewFemTraits.Age
        else:
            if self.AgeCat == "teen":
                self.Age = randint(16,17)
            elif self.AgeCat == "college":
                self.Age = randint(18,22)
            elif self.AgeCat == "twenties":
                self.Age = randint(22,29)
            else:
                self.Age = randint(30,50)

        if self.AgeCat in ["teen","college","twenties"]:
            LTagLists.adj_excl.append("older")
            LTagLists.noun_excl.append("older")
        else:
            LTagLists.adj_excl.append("young")
            LTagLists.noun_excl.append("young")

        if NewFemTraits.BodyType:
            self.BodyType = NewFemTraits.BodyType
        else:
            self.BodyType = choice(["slender","avg","curvy","plussize"])

        if self.BodyType in ["slender","avg"]:
            LTagLists.adj_excl.append("plussize")
        elif self.BodyType in ["curvy","plussize"]:
            LTagLists.adj_excl.append("slender")
        
        if NewFemTraits.HairStyle:
            self.HairStyle = NewFemTraits.HairStyle
        else:
            self.HairStyle = choice(self.Race.FemHairStyle)
        
        if NewFemTraits.BustSize:
            self.BustSize = NewFemTraits.BustSize
        else:
            self.BustSize = choice(["small","normal","large","huge"])

        if isinstance(NewFemTraits.HasFakeTits, bool) and not bRandomize:
            self.HasFakeTits = NewFemTraits.HasFakeTits
        else:
            if self.BustSize in ["large","huge"]:
                self.HasFakeTits = choice([False,False,True])
            else:
                self.HasFakeTits = False

        if NewFemTraits.IsVirgin in [True,False] and not bRandomize:
            self.IsVirgin = NewFemTraits.IsVirgin
        else:
            if self.AgeCat in ["college","twenties"]:
                self.IsVirgin = choice([True,False,False,False])
            elif self.AgeCat in ["teen"]:
                self.IsVirgin = CoinFlip()
            else:
                self.IsVirgin = False

        if not self.IsVirgin:
            LTagLists.adj_excl.append("virginal")
            #LTagLists.adj_req.append("tight")
        # ===============
        # Setup bodyparts
        # ===============

        # Ass
        self.Anus = AnusFemale(TagLists = LTagLists)
        self.Buttocks = ButtocksFemale(Params = SkinParams, TagLists = LTagLists)
        self.Ass = AssFemale(Params = SkinParams, TagLists = LTagLists)
        self.Ass.Anus = self.Anus
        self.Ass.Buttocks = self.Buttocks

        # Back
        self.Back = BackFemale(Params = SkinParams, TagLists = LTagLists)

        # Breasts
        self.Nipples = Nipples(Params = NipParams, TagLists = LTagLists)

        BreastTagLists = None
        if self.BustSize == "small":
            BreastTagLists = TagLists(adj_excl = ["bigtits"] + LTagLists.adj_excl, noun_excl = ["bigtits"] + LTagLists.noun_excl)
        elif self.BustSize == "large":
            BreastTagLists = TagLists(adj_excl = ["smalltits"] + LTagLists.adj_excl, noun_excl = ["smalltits"] + LTagLists.noun_excl)
            LTagLists.adj_excl.append("smalltits")
            LTagLists.noun_excl.append("smalltits")
        else:
            BreastTagLists = TagLists(adj_excl = LTagLists.adj_excl, noun_excl = LTagLists.noun_excl)
            LTagLists.adj_excl.append("bigtits")
            LTagLists.noun_excl.append("bigtits")

        if not self.HasFakeTits:
            BreastTagLists.adj_excl.append("fake")
            BreastTagLists.noun_excl.append("fake")

        self.Breasts = Breasts(Params = SkinParams, TagLists = BreastTagLists)
        self.Breasts.Nipples = self.Nipples

        # Eyes
        self.Eyes = Eyes(Params = EyeParams, TagLists = LTagLists)

        # Face
        self.Face = Face(Params = SkinParams, TagLists = LTagLists)

        # Hair 
        self.Hair = Hair(Params = HairParams, TagLists = LTagLists)

        # Hips
        self.Hips = Hips(Params = SkinParams, TagLists = LTagLists)

        # Legs
        self.Legs = Legs(Params = SkinParams, TagLists = LTagLists)

        # Lips
        self.Lips = Lips(TagLists = LTagLists)

        # Mouth
        self.Mouth = Mouth(TagLists = LTagLists)

        # Skin
        self.Skin = Skin(Params = SkinParams, TagLists = LTagLists)

        # Thighs
        self.Thighs = Thighs(Params = SkinParams, TagLists = LTagLists)

        # Vagina
        self.Clitoris = Clitoris(TagLists = LTagLists)
        self.InnerLabia = VaginaInnerLabia(TagLists = LTagLists)
        self.InnerVagina = VaginaInner(TagLists = LTagLists)
        self.OuterLabia = VaginaOuterLabia(TagLists = LTagLists)

        if self.PubeStyle == "shaved":
            VagTagLists = TagLists(adj_excl = ["hairy","trimmed"] + LTagLists.adj_excl, noun_excl = ["hairy","trimmed"])
        elif self.PubeStyle == "hairy":
            VagTagLists = TagLists(adj_excl = ["shaved","trimmed"] + LTagLists.adj_excl, noun_excl = ["shaved","trimmed"])
        elif self.PubeStyle == "trimmed":
            VagTagLists = TagLists(adj_excl = ["shaved","hairy"] + LTagLists.adj_excl, noun_excl = ["shaved","hairy"])

        self.Vagina = Vagina(TagLists = VagTagLists)
        self.Vagina.Clitoris = self.Clitoris
        self.Vagina.InnerVag = self.InnerVagina
        self.Vagina.OuterLabia = self.Vagina.OuterLabia
        self.Vagina.InnerLabia = self.InnerLabia

        # Body
        self.Body = BodyFemale(Params = SkinParams, TagLists = LTagLists)
        self.Body.Hair = self.Hair
        self.Body.Face = self.Face
        self.Body.Eyes = self.Eyes
        self.Body.Lips = self.Lips
        self.Body.Mouth = self.Mouth
        self.Body.Hips = self.Hips
        self.Body.Back = self.Back
        self.Body.Legs = self.Legs
        self.Body.Skin = self.Skin
        self.Body.Thighs = self.Thighs
        self.Body.Breasts = self.Breasts
        self.Body.Vagina = self.Vagina
        self.Body.Ass = self.Ass

        # Bodypart lists
        self.BodyParts = [self.Anus,self.Ass,self.Back,
                          self.Body,self.Breasts,self.Buttocks,
                          self.Eyes,self.Face,self.Hair,
                          self.Hips,self.Legs,self.Lips,
                          self.Mouth,self.Nipples,self.Skin,
                          self.Thighs,self.Vagina,self.Clitoris,
                          self.InnerLabia,self.InnerVagina,
                          self.OuterLabia,
                         ]
        self.HeadParts = [self.Eyes,self.Face,self.Hair,
                          self.Lips,self.Mouth]
        self.ClothedParts = [self.Breasts,self.Body,self.Eyes,
                             self.Face,self.Hair,self.Hips,
                             self.Legs,self.Lips,self.Mouth,
                             self.Skin,
                            ]
        self.IntimateParts = [self.Ass,self.Back,self.Breasts,
                              self.Breasts.Nipples,self.Hips,self.Legs,
                              self.Thighs,self.Vagina,
                             ]
        self.IntimatePartsInners = [self.Ass,self.Anus,self.Back,
                                    self.Breasts,self.Nipples,self.Hips,
                                    self.Legs,self.Thighs,self.Vagina,
                                    self.Clitoris,self.InnerLabia,self.InnerVagina,
                                    self.Vagina.OuterLabia,
                                   ]
        self.NaughtyParts = [self.Ass,self.Anus,self.Breasts,
                             self.Nipples,self.Vagina,self.Clitoris,
                             self.InnerLabia,self.InnerVagina,self.OuterLabia,]

        WomanNotList = []
        if not self.IsVirgin:
            WomanNotList += ["virgin","virginal"]
        #self.Woman = Female(NotList = WomanNotList, TagLists = LTagLists)
        #self.Noun = self.Woman.GetNoun()
        #self.Desc = self.Woman.FloweryDesc()
        #self.DescWords = self.Woman.GetDescWordList()

        self.BuildDesc()

        sAge = "AgeCat: " + self.AgeCat
        sRace = "Race: " + self.RaceName
        sEyeColor = "Eyes: " + self.EyeColor
        sHairColor = "Hair: " + self.HairColor
        sNipColor = "Nips: " + self.NipColor
        sSkinColor = "Skin: " + self.SkinColor
        sBodyType = "BodyType: " + self.BodyType
        sBustSize = "BustSize: " + self.BustSize
        sVirgin = "IsVirgin: " + str(self.IsVirgin)
        sFakeTits = "HasFakeTits: " + str(self.HasFakeTits)
        sPubeStyle = "PubeStyle: " + self.PubeStyle
        sDesc = "[Gender: Female".ljust(20) + sAge.ljust(20) + sRace.ljust(20) + sBodyType.ljust(20) 
        sDesc += sSkinColor.ljust(20) + sHairColor.ljust(20) + sEyeColor.ljust(20) + sNipColor.ljust(20)
        sDesc += sVirgin.ljust(20) + sBustSize.ljust(20) + sFakeTits.ljust(20) + sPubeStyle.ljust(19) + "]"

        print("\n" + sDesc)

    def BuildDesc(self):
        NounList = []

        if self.AgeCat == "teen":
            if self.RaceName == "poc":
                NounList += ["black teen girl: poc,young,teen,sing","black teenage girl: poc,young,teen,sing","young black teen: poc,young,teen,sing","young ebony teen: poc,young,teen,sing","young black woman: poc,young,sing","black girl: poc,young,teen,sing"]
            else:
                NounList += ["teen girl: young,teen,sing","teenage girl: young,teen,sing","young lady: young,sing","young woman: young,sing"]
                if self.HairColor == "blonde":
                    NounList += ["blonde teen girl: hair,cauc,young,teen,sing","blonde teenage girl: hair,cauc,young,teen,sing","young blonde: hair,cauc,young,sing","young blonde woman: hair,cauc,young,sing","blonde girl: hair,cauc,young,sing"]
                elif self.HairColor == "redhead":
                    NounList += ["redhead teen girl: hair,cauc,young,teen,sing","redhead teenage girl: hair,cauc,young,teen,sing","young redhead: hair,cauc,young,sing","young redhead woman: hair,cauc,young,sing","redhead girl: hair,cauc,young,sing"]
                elif self.HairColor == "brown":
                    NounList += ["brunette teen girl: hair,cauc,young,teen,sing","brunette teenage girl: hair,cauc,young,teen,sing","young brunette: hair,cauc,young,sing","young brunette woman: hair,cauc,young,sing","brunette girl: hair,cauc,young,sing","brunette teen: hair,cauc,young,teen,sing"]
                elif self.HairColor == "black":
                    NounList += ["dark-haired teen girl: hair,young,teen,sing","dark-haired girl: hair,young,teen,sing","dark-haired teen: hair,young,teen,sing","raven-haired girl: hair,young,sing","raven-haired teen girl: hair,young,teen,sing","raven-haired young lady: hair,young,sing"] 
        elif self.AgeCat == "college":
            if self.RaceName == "poc":
                NounList += ["black college girl: poc,young,college,sing","ebony college girl: poc,young,college,sing","young black woman: poc,young,sing","black girl: poc,young,sing","young black lady: poc,young,sing","young ebony lady: poc,young,sing","young black college girl: poc,young,college,sing","young ebony college girl: poc,young,college,sing","black co-ed: poc,young,college,sing","ebony co-ed: poc,young,college,sing","young black co-ed: poc,young,college,sing"]
            else:
                NounList += ["college girl: young,college,sing","young lady: young,sing","young woman: young,sing","co-ed: young,college,sing","young co-ed: young,college,sing"]
                if self.HairColor == "blonde":
                    NounList += ["blonde college girl: hair,cauc,young,college,sing","young blonde college girl: hair,cauc,young,college,sing","blonde young woman: hair,cauc,young,sing","blonde girl: hair,cauc,young,sing","blonde young lady: hair,cauc,young,sing","blonde co-ed: hair,cauc,young,college,sing","blonde x3: hair,cauc,sing"]
                elif self.HairColor == "redhead":
                    NounList += ["redheaded college girl: hair,cauc,young,college,sing","young redheaded college girl: hair,cauc,young,college,sing","redheaded young woman: hair,cauc,young,sing","redheaded young lady: hair,cauc,young,sing","redheaded co-ed: hair,cauc,young,college,sing","redhead x3: hair,cauc,sing"]
                elif self.HairColor == "brown":
                    NounList += ["brunette college girl: hair,cauc,young,college,sing","young brunette college girl: hair,cauc,young,college,sing","brunette young woman: hair,cauc,young,sing","brunette girl: hair,cauc,young,sing","brunette young lady: hair,cauc,young,sing","brunette co-ed: hair,cauc,young,college,sing","brunette x3: hair,cauc,sing"]
                elif self.HairColor == "black":
                    NounList += ["dark-haired college girl: hair,young,college,sing","raven-haired college girl: hair,young,college,sing","raven-haired young lady: hair,young,sing","dark-haired co-ed: hair,young,college,sing","raven-haired co-ed: hair,young,college,sing"]
        elif self.AgeCat == "twenties":
            if self.RaceName == "poc":
                NounList += ["young black woman: poc,young,twenties,sing","young ebony woman: poc,young,sing","black woman x3: poc,sing","ebony woman: poc,sing","young black lady: poc,young,sing","young black woman: poc,young,sing"]
            else:
                NounList += ["young lady: young,sing","young woman: young,sing","woman x2: sing"]
                if self.HairColor == "blonde":
                    NounList += ["blonde young woman: hair,cauc,young,sing","blonde girl: hair,cauc,young,sing","blonde young lady: hair,cauc,young,sing","blonde woman x3: hair,cauc,sing","blonde x4: hair,cauc,sing","blonde bombshell: hair,cauc,sing"]
                elif self.HairColor == "redhead":
                    NounList += ["redheaded young woman: hair,cauc,young,sing","redheaded girl: hair,cauc,young,sing","redheaded young lady: hair,cauc,young,sing","redheaded woman: hair,cauc,sing","redhead x4: hair,cauc,sing"]
                elif self.HairColor == "brown":
                    NounList += ["brunette young woman: hair,cauc,young,sing","brunette girl: hair,cauc,young,sing","brunette young lady: hair,cauc,young,sing","brunette woman: hair,cauc,sing","brunette x3: hair,cauc,sing"]
                elif self.HairColor == "black":
                    NounList += ["dark-haired young woman: hair,young,sing","raven-haired young woman: hair,young,sing","dark-haired girl: hair,young,sing","raven-haired girl: hair,young,sing","dark-haired young lady: hair,young,sing","raven-haired young lady: hair,young,sing","dark-haired woman: hair,sing","raven-haired woman: hair,sing"]
        else:
            if self.RaceName == "poc":
                NounList += ["black woman: poc,sing","ebony woman: poc,sing","mature black woman: poc,older,sing","black MILF: poc,older,milf,sing","ebony MILF: poc,older,milf,sing","black lady: poc,sing"]
            else:
                NounList += ["woman x2: sing","mature woman: older, sing","MILF: older,milf,sing","lady: sing"]
                if self.HairColor == "blonde":
                    NounList += ["blonde woman x2: hair,cauc,sing","mature blonde woman: hair,cauc,older,milf,sing","mature blonde: hair,cauc,older,milf,sing","blonde MILF: hair,cauc,older,milf,sing","blonde lady: hair,cauc,sing","blonde x3: hair,cauc,sing","blonde bombshell: hair,cauc,sing"]
                elif self.HairColor == "redhead":
                    NounList += ["redheaded woman x2: hair,cauc,sing","mature redheaded woman: hair,cauc,older,sing","mature redhead: hair,cauc,older,sing","redheaded MILF: hair,cauc,older,milf,sing","redheaded lady: hair,cauc,sing","redhead x3: hair,cauc,sing",]
                elif self.HairColor == "brown":
                    NounList += ["brunette woman x2: hair,cauc,sing","mature brunette woman: hair,cauc,older,sing","mature brunette: hair,cauc,older,sing","brunette MILF: hair,cauc,older,milf,sing","brunette lady: hair,cauc,sing","brunette x3: hair,cauc,sing",]
                elif self.HairColor == "black":
                    NounList += ["dark-haired woman: hair,sing","raven-haired woman: hair,milf,sing","mature dark-haired woman: hair,older,sing","mature raven-haired woman: hair,older,sing","dark-haired MILF: hair,older,milf,sing","raven-haired MILF: hair,older,milf,sing","dark-haired lady: hair,sing","raven-haired lady: hair,sing",]
                else:
                    NounList += ["gray-haired woman: hair,older,sing","silver-haired woman: hair,older,sing","mature gray-haired woman: hair,older,sing","mature silver-haired woman: hair,older,sing","gray-haired lady: hair,older,sing","silver-haired lady: hair,older,sing",]

        self.Noun = choice(NounList)

        AdjList = ['doe-eyed: eyes',
                   'little: size,small,short',
                   'matronly: age,older',
                   'nubile x2: age,young',
                  ]

        if self.BustSize in ["large","huge"]:
            AdjList += ['ample-bosomed: bigtits','big-titted: bigtits','bosomy: bigtits,shape','busty: bigtits','buxom: bigtits','full-figured: bigtits,shape','shapely: curvy,bigtits,shape','stacked: bigtits,shape','statuesque: bigtits,shape','voluptuous: bigtits,curvy,shape',]
        elif self.BustSize in ["small"]:
            AdjList += ['flat-chested: smalltits','lithe: slender,flexible','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]
            
        if self.BodyType in ["plussize"]:
             AdjList += ['chubby: plussize,shape','Rubenesque: plussize,shape','plump: curvy,plussize,shape',]
        elif self.BodyType in ["curvy"]:
            AdjList += ['curvaceous: curvy,shape','round-bottomed: curvy,shape','shapely: curvy,shape']
        elif self.BodyType in ["slender"]:
            AdjList += ['limber:slender,flexible','lithe: slender,flexible','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]

        if self.EyeColor in ["blue"]:
            AdjList += ['blue-eyed x3: eyes,cauc',]
        elif self.EyeColor in ["green"]:
            AdjList += ['green-eyed: eyes,cauc',]
        else:
            AdjList += ['brown-eyed x2: eyes','dark-eyed: eyes',]

        if self.Height in ["tall"]:
            AdjList += ['tall: height,tall','willowy: height,tall']
        elif self.Height in ["short"]:
            AdjList += ['short: height,short',]

        #["big","bobbed","braids","curls","long","pigtails","pixie","ponytail","short","updo"]
        #["cornrows","curls","fro","kinky","long","pixie","short","updo"]
        #["braids","long","pigtails","pixie","ponytail","short",]

        if self.HairStyle in ["bobbed"]:
            AdjList += ['bobbed: hairstyle,bob',]
        elif self.HairStyle in ["braids"]:
            AdjList += ['braided: hairstyle,braids',]
        elif self.HairStyle in ["cornrows"]:
            AdjList += ['cornrowed: hairstyle,cornrows,poc',]
        elif self.HairStyle in ["curls"]:
            AdjList += ['curly: hairstyle,curls',]
        elif self.HairStyle in ["fro"]:
            AdjList += ['afro\'d: hairstyle,fro,poc',]
        elif self.HairStyle in ["kinky"]:
            AdjList += ['kinky-haired: hairstyle,kinky,poc',]
        elif self.HairStyle in ["long"]:
            AdjList += ['long-haired: hairstyle,longhair',]
        elif self.HairStyle in ["pigtails"]:
            AdjList += ['pigtailed: hairstyle,pigtails',]
        elif self.HairStyle in ["pixie"]:
            AdjList += ['pixie-cut: hairstyle,pixie',]
        elif self.HairStyle in ["ponytail"]:
            AdjList += ['pony-tailed: hairstyle,ponytail',]
        elif self.HairStyle in ["short"]:
            AdjList += ['short-haired: hairstyle,shorthair','short-cropped: hairstyle,shorthair',]
        elif self.HairStyle in ["updo"]:
            AdjList += ['big-haired: hairstyle,updo','permed: hairstyle,updo',]

        if self.IsFit:
            AdjList += ['athletic: muscular,shape','fit: muscular','trim: slender,shape']
        else:
            AdjList += ['dainty: small,fragile','delicate: fragile',]

        if self.IsVirgin:
            AdjList += ['virginal: virginal',]

        self.Woman = NounPhrase(NPParams(sColor = self.SkinColor))
        self.Woman.NounList(NounList)
        self.Woman.AdjList(AdjList)
        self.Noun = self.Woman.GetNoun()
        self.Desc = self.Woman.FloweryDesc()
        self.DescWords = self.Woman.GetDescWordList()

        return True


    #'bronzed: color,tan',
    #'curly-haired: hair',
    #'latina x3: poc,color',
    #'kinky-haired: hair,poc',
    #'leggy: longlegs,shape',
    #'pale: color,cauc',
    #'pig-tailed: hair',
    #'pony-tailed: hair',
    #'prim: virginal,super',
    #'short-haired: hair',
    #'tanned: color,cauc',
    #'wide-bottomed: curvy,shape,bigbutt'

class MaleBodyParts(BodyParts):
    def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          self.Gender = "male"

class FemaleBodyParts(BodyParts):
    def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          self.Gender = "female"

class Face(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['face x3: default,std,sing',
                         'features: poetic,plur'
                        ])
          
          self.AdjList(['adorable: super,cute,young,attractive',
                        'angelic: super,cute,attractive',
                        'beaming: emotion,happy',
                        'beautiful: super,attractive',
                        'cute: super,cute,attractive',
                        'delicate: cute',
                        'elegant: older,attractive',
                        'excited: emotion,happy',
                        'expressive: emotion',
                        'gentle: attitude',
                        'gorgeous: super,attractive',
                        'flushed: arousal',
                        'heart-shaped: shape',
                        'innocent: attitude,cute,young,virginal',
                        'lovely: super,attractive',
                        'oval: shape',
                        'pretty: attractive',
                        'radiant: ',
                        'round: shape',
                        'smiling: emotion,happy',
                        'startled: emotion',
                        'sweet: attitude,cute,attractive',
                        'warm: attitude,feel',
                        'wide-eyed: cute,attractive'])
               
          self.DefaultNoun('face')
          
class BackFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['back x4:default,std,sing',
                         'spine:std,clinical,sing'])
          
          self.AdjList(['arched x2: shape',
                         'arching: action',
                         'bare: nude',
                         'carved: shape',
                         'concave: shape',
                         'curved x2: shape',
                         'delicate: super,attractive',
                         'feminine: attractive',
                         'flexible: flexible,attractive',
                         'gently curved: shape, attractive',
                         'graceful x2: fit',
                         'lissome: attractive,slender',
                         'lithe x2: athletic,young,flexible,slender',
                         'long: size,length,long',
                         'naked: nude',
                         'sculpted: attractive',
                         'sexy: attractive',
                         'sleek: slender',
                         'slender x2: slender,shape',
                         'slim x2: slender',
                         'smooth: feel',
                         'tapered x3: shape,slender',
                         'tapering x2: shape,slender',
                         'well-defined: shape',
                         'willowy x2: slender,flexible'
                        ])
               
          self.DefaultNoun('back')
          self.DefaultAdj('curved')
          
class Skin(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True
          self.NounList(['skin x4: default,std,sing',
                         'flesh: sing'
                        ])
                              
          self.AdjList(['bare: nude',
                        'delicate: texture,cute',
                        'exposed: nude',
                        'gentle: feel,texture',
                        'gleaming: texture,shiny',
                        'glistening: wet,texture,shiny',
                        'glowing: texture',
                        'gossamer: feel,texture',
                        'luscious: taste,super',
                        'lustrous x2: texture,shiny',
                        'naked: nude',
                        'perfect: super',
                        'silken: feel,texture',
                        'soft: feel,texture',
                        'smooth: feel,texture',
                        'supple: feel,young,texture',
                        'sweet: super,taste',
                        'tender: feel,cute',
                        'un-blemished: young,virginal,texture',
                        'un-sullied: young,virginal',
                        'warm: feel',
                        'yielding: feel',
                        'youthful: young',
                       ])
          
          self.DefaultNoun('skin')
          self.IsPlural = False
          
class Mouth(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['mouth x4: default,std,sing',
                         'mouth-hole: silly,crude,sing'])
               
          self.AdjList(['eager: attitude',
                        'filthy: attitude,horny,rude',
                        'greedy: horny',
                        'hot: feel',
                        'hungry: horny',
                        'insatiable: horny',
                        'insolent: attitude,rude',
                        'lewd: horny',
                        'open: open',
                        'pretty: attractive',
                        'soft: feel',
                        'sweet: super,attractive',
                        'thirsty: horny',
                        'wanting: horny',
                        'warm: feel',
                        'wet: wet',
                        'willing: attitude,horny'])
          
          self.DefaultNoun("open")
          self.DefaultAdj("insatiable")
          self.IsPlural = False
          
class Lips(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['lips: default,std,plur'])
               
          self.AdjList(['candy-colored: lipstick,color,',
                        'collagen-injected: fake,feel',
                        'curved: shape',
                        'dark: color',
                        'full: thick,desc',
                        'glossy: shiny,texture',
                        'inviting: attitude',
                        'insolent: attitude',
                        'luscious: super,thick,taste',
                        'moist: feel,taste',
                        'painted: lipstick',
                        'pouting: emotion',
                        'pouty: emotion,shape',
                        'red x2: color',
                        'rose-colored: color',
                        'rosy: color',
                        'rouge: color',
                        'sensual: attitude',
                        'shiny: shiny',
                        'smiling: emotion',
                        'soft: feel,texture',
                        'sweet: young,taste'
                        'tender: feel',
                        'warm: feel',
                       ])
          
          self.DefaultNoun("lips")
          self.DefaultAdj("full")
          
class Eyes(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['eyes: std,default,plur'])
               
          self.AdjList(['alluring: attractive',
                        'beautiful: attractive',
                        'bewitching: attractive',
                        'big: size,large',
                        'bright: attractive,young,cauc',
                        'blue x4: color,cauc',
                        'brown x2: color',
                        'captivating: attractive',
                        'clear: attractive,desc',
                        'dazzling: attractive,shiny',
                        'earnest: emotion',
                        'electric: attractive',
                        'electrifying: attractive',
                        'enchanting: attractive',
                        'enormous: size,large',
                        'exotic: attractive',
                        'gray x2: color,cauc',
                        'green x3: color,cauc',
                        'hazel x2: color,cauc',
                        'kind: emotion',
                        'large: size,large,desc',
                        'mischievous: emotion',
                        'pale: color,cauc',
                        'piercing: ',
                        #'slanted: asian',
                        'soulful: attractive',
                        'sparkling: attractive,shiny',
                        'sweet: attractive',
                        'wide x3: size,large'])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("bewitching")
          
class Hips(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['hips: std,default,plur'])
               
          self.AdjList(['curvy: width,wide,shape,desc',
                        'curvaceous: wide,width',
                        'bare: nude',
                        'broad: width,wide',
                        'fertile: width,wide,horny',
                        'girlish: shape,width,narrow,young',
                        'narrow: shape,width,narrow',
                        'rounded: shape',
                        'sensual: attractive',
                        'shapely: shape,attractive',
                        'slender: shape,size,small',
                        'slinky: attitude',
                        'sultry: attitude,attractive',
                        'tantalizing: horny,attractive,',
                        'voluptuous: size,wide,width',
                        'wanton: horny',
                        'wide: size,wide',
                        'womanly: feminine,wide'])
          
          self.DefaultNoun("hips")
          
class Hair(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['braids: style,plur',
                         'hair x4: std,default,sing',
                         'fro: poc,sing'
                         'locks x2: plur',
                         'pig-tails: style,young,plur',
                         ])
               
          self.AdjList(['abundant: volume,thickhair',
                        'auburn: color,cauc',
                        'beautiful: super',
                        'big: volume,thickhair',
                        'black x2:color',
                        'bleached: color',
                        'blonde x4: color,cauc',
                        'brilliant: super,shiny',
                        'brunette x3: color,cauc',
                        'bushy: shape,texture,style,unkempt,volume,thickhair',
                        'coal-black: color',
                        'coppery: color,cauc',
                        'crimped: style,texture',
                        'crinkly: feel,texture',
                        'cropped: length,short',
                        'curly: shape,style',
                        'cute: super',
                        'braided: style,kempt,bound',
                        'dark x2: color',
                        'dyed-blue: color,fake',
                        'dyed-green: color,fake',
                        'dyed-pink: color,fake',
                        'dyed-purple: color,fake',
                        'fair: color,cauc',
                        'fashionable: style',
                        'fine: texture',
                        'flaming-red: color,cauc',
                        'flaxen: color,cauc',
                        'flowing: texture,loose',
                        'fluffy: texture,volume,thickhair',
                        'frizzled: texture',
                        'full-bodied: volume,thickhair',
                        'glossy: feel,texture',
                        'golden: color,cauc',
                        'kinky black-girl: color,poc',
                        'long: length,long',
                        'lovely: super',
                        'lustrous: shiny',
                        'luxuriant: super,volume,thickhair',
                        'natural: super',
                        'permed: style,kempt',
                        'pixie-cut: style',
                        'platinum blonde x2: color,cauc',
                        'pulled-back: style,bound',
                        'punk blue: color,fake,style',
                        'red: color,cauc',
                        'satiny: texture,shiny',
                        'sandy: color,cauc',
                        'scarlet: color,cauc',
                        'severe: style,bound',
                        'short: length,short',
                        'silken: feel',
                        'silvery: color,older',
                        'sleek: texture',
                        'shoulder-length: length,medium',
                        'soft: feel',
                        'straight: shape,style',
                        'stringy: texture,volume,thinhair',
                        'tangled: style,unkempt',
                        'thick: volume,thickhair',
                        'tightly-bound: style,bound',
                        'unbound: style,loose',
                        'unruly: style,unkempt',
                        'vibrant: poetic',
                        'waist-length: length,long',
                        'wavy: shape,style',
                        'white: color,older',
                        'wild: style,unkempt,loose',
                        'wiry: texture',
                        'wispy: texture,volume,thinhair',
                       ])
          
          self.DefaultNoun("hair")
          self.DefaultAdj("flowing")
          
class Legs(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['legs: std,default,plur'])
               
          self.AdjList(['athletic: fit',
                        'bare: nude',
                        'chiseled: fit,attractive',
                        'chubby: curvy',
                        'coltish x2: slender, young',
                        'comely: attractive',
                        'elegant: poetic',
                        'feminine: attractive',
                        'fetching: attractive',
                        'fit: fit',
                        'flexible: flexible',
                        'girlish: young,slender',
                        'graceful: fit',
                        'lithe: flexible',
                        'limber: flexible',
                        'lissome: flexible,fit,slender',
                        'lithesome: flexible,fit,slender',
                        'long x3: length,long',
                        'long, sexy: length,long,attractive',
                        'lovely: attractive,super',
                        'naked: nude',
                        'satiny: feel,shiny',
                        'sinuous: attractive,flexible',
                        'smooth: feel,hairless',
                        'supple: feel,soft,young',
                        #'tan: color',
                        #'tanned: color',
                        'toned: fit',
                        'sexy: attractive',
                        'shapely: fit',
                        'shaved: hairless',
                        'short: length,short',
                        'slender: slender',
                        'smooth: hairless',
                        'smooth-shaven: hairless',
                        'supple: soft,young,feel',
                        'svelte: slender,flexible',
                        'willowy: slender',
                        'womanly: curvy,attractive',
                        'yielding: soft,feel,horny',
                       ])
          
          self.DefaultNoun("legs")
          
class Thighs(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['thighs: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        #'bronzed: color,tan',
                        'chubby: curvy,chubby',
                        'comely: attractive, poetic',
                        'delectable: super,taste',
                        'full: curvy,chubby,large',
                        'girlish: slender,young',
                        'heavy: chubby,large',
                        'inviting: horny',
                        'luscious: super',
                        'nubile: young',
                        #'pale: color,cauc',
                        'plump: curvy,chubby'
                        'powerful: fit,strong',
                        #'porcelain: color,cauc',
                        'ripe: attractive',
                        'rounded: shape',
                        'sensual: attractive',
                        'sexy: attractive',
                        'shapely: shape,attractive',
                        'silken: feel',
                        'smooth: feel,hairless',
                        'soft: feel',
                        #'tanned: color,tan',
                        'tender: feel',
                        'thick x2: large,chubby',
                        'un-sullied: young, virginal',
                        'wide: chubby,large',
                        'womanly: curvy',
                        'youthful: young'])
          
          self.DefaultNoun("thighs")
          
class Nipples(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['nipples x4: std,default,plur',
                         'nips: silly,plur',
                         'teats: silly,plur',
               ])
               
          self.AdjList(['aching: horny',
                        'bare: nude',
                        'bared: nude',
                        'black: color, poc',
                        'blossoming: young',
                        'brown x3: color,',
                        'budding: cute',
                        'chocolate: color',
                        'dainty: size,small,cute',
                        'dark x3: color,',
                        'dusky: color',
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'exquisite: attractive,super',
                        'hard: arousal,',
                        'inch-long: size,large,',
                        'long,: size,large',
                        'luscious: super',
                        'petite: size,small,cute,',
                        'pert: arousal,cute',
                        'pierced: style',
                        'pink x3: color,cauc',
                        'plump: size,large,feel',
                        'pokey: arousal',
                        'prominent: poetic',
                        'puffy: feel,',
                        'ripe: attractive',
                        'rose-colored x2: color,cauc',
                        'rosebud: color,cauc',
                        'sensitive: feel',
                        'shameless: horny',
                        'shy: cute',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'succulent: attractive,taste',
                        'suckable: horny,attractive',
                        'swollen: arousal,size,large,',
                        'tasty: taste,horny,attractive',
                        'tempting: attractive,horny',
                        'tender: feel',
                        'thick: size,large,arousal,',
                        'tiny: size,small,',
                        'wide: size,large'])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")

class Breasts(FemaleBodyParts):
    def __init__(self, Params = None, NotList = None, TagLists = None, bCupSize = False):
        super().__init__(Params, NotList, TagLists)
        self._bCupSize = bCupSize
        self.AddSkinColors = True
          
        self.NounList(['boobies: silly,slang,cute,plur',
                       'boobs x4: std,slang,plur',
                       'bosoms x2: std,plur',
                       'breasticles x2: silly,crude,slang,plur',
                       'breasts x4: std,clinical,default,plur',
                       'buds x2: cute,desc,smalltits,young,plur',
                       'bust: std,sing',
                       'chest: std,sing',
                       'coconuts: silly,slang,bigtits,cute,plur',
                       'dumplings: silly,cute,plur',
                       'fake boobs: std,slang,bigtits,fake,plur',
                       'gazongas: silly,crude,slang,plur',
                       'globes x2: silly,crude,bigtits,desc,plur',
                       'jugs: silly,crude,bigtits,slang,plur',
                       'knockers: silly,crude,bigtits,slang,plur',
                       'orbs x2: silly,bigtits,desc,plur',
                       'mammaries: silly,clinical,plur',
                       'melons: silly,bigtits,crude,desc,plur',
                       'milk-balloons: bigtits,silly,crude,desc,milk,plur',
                       'mommy milkers: silly,crude,bigtits,milk,plur',
                       'mounds x2: smalltits,desc,plur',
                       'tatas: silly,crude,slang,cute,plur',
                       'teats: std,clinical,desc,plur',
                       'tiddies: silly,crude,slang,cute,plur',
                       'titties x2: silly,crude,slang,cute,plur',
                       'tits x3: std,crude,slang,plur',
                       'udders: crude,slang,bigtits,plur',
                    ])
               
        self.AdjList(['big: size,bigtits',
                      'bite-sized: size,smalltits',
                      'bouncy: movement',
                      'bountiful: bigtits',
                      'budding: smalltits,young',
                      'buxom: bigtits',
                      'college girl: age,young',
                      'delicious: super,taste',
                      'enchanting: super,attractive',
                      'fake: fake,bigtits',
                      'fat x3: bigtits,size,feel,plussize,shape',
                      'flouncing: movement',
                      'fuckable: bigtits,horny',
                      'full: bigtits',
                      'fulsome: bigtits',
                      'generous: super,bigtits',
                      'gentle: feel',
                      'girlish: age,smalltits,young',
                      'glistening: wet',
                      'glorious: super',
                      'gorgeous: super',
                      'grapefruit-sized: size,bigtits',
                      'heaving: movement',
                      'heavy: bigtits,feel',
                      'impressive: super,bigtits',
                      'jiggling: movement',
                      'juicy: bigtits,super,feel,taste,horny',
                      'little: smalltits,size',
                      'luscious: taste,super',
                      'lush: super',
                      'luxuriant: bigtits,super',
                      'magnificent: bigtits,super',
                      'maternal: age,older',
                      'mature: age,older',
                      'MILF: age,older',
                      'nubile: age,young',
                      'oiled-up: wet',
                      'pendulous: bigtits,shape,older',
                      'perky: shape,young',
                      'pert: shape,',
                      'petite: size,smalltits,',
                      'plentiful: bigtits,super',
                      'plump: bigtits,feel,shape,',
                      'proud: bigtits,super,',
                      'quivering: movement,',
                      'ripe: feel,shape,young',
                      'round: shape',
                      'sensual: poetic',
                      'shapely: shape',
                      'small: smalltits',
                      'smooth: feel,young',
                      'soft: feel',
                      'statuesque: shape,bigtits,older',
                      'stunning: super',
                      'succulent: super,taste',
                      'suckable: taste,horny',
                      'sumptuous: bigtits,super',
                      'supple: feel,young',
                      'surgically-enhanced: bigtits,shape,fake',
                      'swaying: bigtits,movement',
                      'sweet: super',
                      'swollen: size,bigtits,shape',
                      'teenage: age,young',
                      'tender: feel',
                      'titanic: bigtits',
                      'tiny: smalltits',
                      'voluptuous: size,bigtits',
                      'well-formed: shape',
                      'youthful: age,young',
                     ])
          
        self.DefaultNoun("breasts")

        self.Nipples = Nipples()

    # Override the AdjList creation call so we
    # can manually add the colors from the 
    # ClothesColors list to each adj list.
    def AdjList(self, NewAdjList):
        CupList = ["A-cup x3: small,cupsize,special",
                   "B-cup x2: small,cupsize,special",
                   "D-cup x3: large,cupsize,special",
                   "double-D cup x3: large,cupsize,special",
                   "triple-D cup x4: large,cupsize,special",
                  ]
        
        if self._bCupSize:
            for cupsize in CupList:
                NewAdjList.append(cupsize)

        #print("Amended Breasts NewAdjList is " + str(NewAdjList))
        super().AdjList(NewAdjList)

    def AllowCupSize(self, bCupSize = True):
        self._bCupSize = bCupSize

        self.AdjList(self.GetAdjList())

    def ShortDesc(self, NotList = None, TagLists = None, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)

        return super().ShortDesc(NotList, TagLists)
          
    def MediumDesc(self, NotList = None, TagLists = None, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)
               
        return super().MediumDesc(NotList, TagLists) 
          
    def FloweryDesc(self, NotList = None, TagLists = None, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)
          
        return super().FloweryDesc(NotList, TagLists) 
          
    def RandomDesc(self, bShortDesc = True, bLongDesc = True, NotList = None, TagLists = None, bCupSize = None):
        self._bCupSize = bCupSize

        return super().RandomDesc(NotList, TagLists) 
     
          
class Clitoris(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['bean: desc,silly,slang,sing',
                         'clit x3: std,slang,sing',
                         'clitoris x2: std,default,sing',
                         'love-button: silly,sing',
                         'love-nub: silly,sing',
                         'magic button: silly,sing',
                         'nub: desc,sing',
                         'pearl: desc,sing',
                        ])
               
          self.AdjList(['delicate: small,cute',
                        'engorged x2: arousal,large',
                        'erect: arousal',
                        'exposed: nude',
                        'fevered: horny',
                        'hooded: style',
                        'little: size',
                        'pierced: style',
                        'pink x4: color',
                        'pulsating: horny',
                        'pulsing: horny',
                        'secret: cute',
                        'sensitive: feel',
                        'shy: cute',
                        'swollen: size,large,arousal',
                        'tender: feel,cute',
                        'throbbing: horny',
                        'tingling: feel'])
          
          self.DefaultNoun("clit")
          self.IsPlural = False

class VaginaInner(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['baby-maker: silly,crude,sing',
                         'cherry: crude,desc,slang,sing',
                         'cleft: desc,sing',
                         'chamber: sing',
                         'chasm: sing',
                         'cock-hole: crude,slang,sing',
                         'cock-sock: crude,silly,sing',
                         'fuck-tunnel: crude,slang,horny,sing',
                         'fuckhole: crude,slang,horny,sing',
                         'furrow: desc,sing',
                         'gash: desc,crude,slang,sing',
                         'hole: desc,crude,std,sing',
                         'honey-hole: silly,slang,sing',
                         'keyhole: silly,desc,sing',
                         'lewdness: silly,sing',
                         'love-channel: silly,sing',
                         'love-tunnel: silly,slang,sing',
                         'opening: desc,sing',
                         'passage: desc,sing',
                         'slit: desc,crude,sing',
                         'tunnel: desc,sing',
                         'vagina: std,default,sing',
                         'vaginal canal: std,clinical,sing',
                         'vestibule: sing',
                         'womanhood: sing',
                         'womb: sing',
                        ])
                    
          self.AdjList(['cherry: color',
                        'cherry-red: color',
                        'deep x2: size',
                        'dripping: wet',
                        'fleshy: feel,desc',
                        'gaping: open',
                        'glazed: wet',
                        'gooey: wet',
                        'gushing: wet',
                        'hungry: horny,slutty',
                        'juicy: wet,feel,taste,slutty',
                        'lewd: horny',
                        'little x3: tight,size,small',
                        'lustful: horny',
                        'needful: horny,slutty',
                        'pink x3: color',
                        'secret: taboo,cute,virginal',
                        'silken: feel',
                        'slick x2: wet,feel',
                        'sloppy: wet',
                        'snug: tight',
                        'sopping x2: wet',
                        'spread: open,slutty',
                        'succulent: super,taste',
                        'sweet: cute,taste',
                        'tender: feel,virginal',
                        'tight x3: tight',
                        'velvet x2: feel',
                        'wanton: horny',
                        'warm: feel',
                        'well-used: horny,slutty',
                        'virgin: young,virginal',
                       ])
               
          self.DefaultNoun("vaginal canal")
          self.IsPlural = False
     
class VaginaOuterLabia(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['labia: std,default,plur',
                         'lips: std,desc,plur',
                         'mons pubis: std,clinical,sing',
                         'mound: desc,sing',
                         'nether lips: desc,plur',
                         'outer labia: std,clinical,plur',
                         'outer pussy lips: std,desc,slang,crude,plur',
                         'pussy lips: std,desc,slang,crude,plur',
                         'vulva: std,clinical,sing'
                        ])

          self.AdjList(['bare: nude',
                        'dewy: wet',
                        'downy: hairy,feel',
                        'down-thatched: hairy,feel',
                        'dripping: wet',
                        'fat x2: size,large,shape',
                        'fleshy: feel',
                        'flushed: arousal,color',
                        'fur-lined: hairy',
                        'girlish: young',
                        'gleaming wet: wet,shaved',
                        'glistening: wet,shaved',
                        'hairless: hairless',
                        'honeyed: wet,taste',
                        'juicy: wet,taste,attractive',
                        'lickable: horny',
                        'luscious: taste,attractive',
                        'lush: attractive,superlative',
                        'moist: wet',
                        'naked: nude',
                        'peach-fuzzed: hairy,young',
                        'pink: color,hairless',
                        'plump x3: size,large,shape',
                        'puffy: arousal,shape',
                        'shameless: horny',
                        'shaved: hairless',
                        'shaven: hairless',
                        'silken: feel',
                        'slick: wet,feel',
                        'smooth: feel,hairless',
                        'succulent: taste,super',
                        'suckable: horny',
                        'supple: feel',
                        'sweet: super,cute',
                        'swollen: arousal,shape',
                        'tender: feel',
                        'trim: hairy',
                        'wet: wet'])
               
          self.DefaultNoun("mons pubis")

class VaginaInnerLabia(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['beef-curtains: silly,crude,plur',
                         'butterfly wings:  desc, cute, plur',
                         'cunt-lips: crude,plur',
                         'flaps: desc,crude,plur',
                         'flower petals: desc,cute,plur',
                         'folds: desc,plur',
                         'fringe: desc,plur',
                         'inner labia: std,default,clinical,plur',
                         'labia: std,default,clinical,plur',
                         'lips: desc,plur',
                         'meat-curtains: crude, silly, plur',
                         'meat-flaps: crude, silly, plur',
                         'nether-lips:  plur',
                         'petals: desc,cute,plur',
                         'piss-flaps: crude,plur',
                         'pussy flaps: desc,crude,plur',
                         'pussy lips: std,default,slang,plur',
                         'sex-flaps: silly,crude,plur',
                         'sex-lips: silly,plur',
                         'wizard sleeve: silly,crude,sing',
                        ])

          self.AdjList(['beefy: meaty',
                        'chewy: taste,meaty',
                        'dangling x2: hanging,shape',
                        'dark: color',
                        'delicate: small,attractive,cute',
                        'dewy x2: wet,cute',
                        'drooping: hanging,shape',
                        'fleshy: meaty',
                        'gossamer: attractive,cute',
                        'lengthy: size,long',
                        'lickable: horny',
                        'little: size,small',
                        'long: long',
                        'lush: attractive,cute',
                        'meaty x2: meaty',
                        'moist: wet',
                        'pink: color',
                        'purplish: color',
                        'ruffled: shape',
                        'secret: taboo,virginal',
                        'shameless: horny',
                        'silken: feel,attractive,cute',
                        'shy: virginal,cute',
                        'succulent: taste,super',
                        'suckable: horny',
                        'tasty: taste,horny',
                        'tender: feel,cute',
                        'trim: size, small',
                        'well-used: slutty',
                        'velvet: attractive, feel'])
                              
          self.DefaultNoun("inner labia")
               
class Vagina(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['cherry pie: silly,cute,slang,young,sing',
                         'cock-garage: silly,crude,slang,sing',
                         'cock-sock: silly,crude,slang,sing',
                         'cooch: std,slang,sing',
                         'coochie: std,slang,sing',
                         'cunny: std,slang,cute,sing',
                         'cunt x3: std,slang,crude,sing',
                         'cunt-hole: crude,slang,sing',
                         'flower: desc,sing',
                         'fuckhole: crude,slang,sing',
                         'fur-burger: hairy,crude,silly,slang,sing',
                         'honey-hole: silly,slang,cute,sing',
                         'honeypot: silly,slang,cute,sing',
                         'love-muffin: silly, slang, cute, sing',
                         'muff: hairy,std,slang,sing',
                         'muffin: hairy,std,slang,sing',
                         'peach: desc,cute,sing',
                         'pie: silly,slang,cute,sing',
                         'pussy x4: std,slang,crude,sing',
                         'quim: std,crude,sing',
                         'sex: std,sing',
                         'snatch: std,slang,sing',
                         'twat x2: std,slang,crude,sing',
                         'vagina x4: std,clinical,sing',
                         'womanhood: std,sing',
                        ])
                            
          self.AdjList(['bald: shaved',
                        'bare: nude,hairless',
                        'black: color,poc',
                        'cherry: young,virginal',
                        'chocolate: color,poc',
                        'clenched: tight',
                        'delightful: super',
                        'dewy: wet',
                        'down-thatched: hairy,young',
                        'dripping: wet',
                        'exposed: bare,horny',
                        'fluffy: hairy',
                        'fuckable: horny',
                        'fur-lined: hairy',
                        'girlish: young',
                        'gleaming wet: wet',
                        'glistening: wet',
                        'gushing: wet',
                        'hairless: shaved',
                        'honeyed: taste',
                        'horny: horny,arousal',
                        'hungry: horny',
                        'juicy: taste,super,horny',
                        'leaky: wet,slutty',
                        'lewd: horny',
                        'lickable: taste,horny',
                        'luscious: super,taste',
                        'lush: super',
                        'lustful: horny',
                        'MILF: age,older,horny',
                        'moist: wet',
                        'mouth-watering: horny',
                        'naked: nude',
                        'needful: horny',
                        'pale: color,cauc',
                        'peach-fuzzed: hairy,young',
                        'perfect: super',
                        'puffy: shape,arousal',
                        'shameless: horny',
                        'shaved: shaved',
                        'silken: feel,shaved,texture',
                        'silky: feel,texture',
                        'slick: wet,feel,texture',
                        'slutty: horny',
                        'smooth: feel,shaved',
                        'smooth-shaven: shaved',
                        'sopping: wet',
                        'succulent: super,taste',
                        'suckable: horny,taste',
                        'supple: feel,shaved,young',
                        'sweet: super',
                        'swollen: arousal,shape,feel',
                        'teenage: age,young',
                        'tender: feel,cute',
                        'tight x4: tight',
                        'trim: trimmed,cute',
                        'unsullied: virginal',
                        'velvet: feel',
                        'virgin: virginal,age,young',
                        'wanton: horny',
                        'well-groomed: trimmed',
                        'well-trimmed: trimmed',
                        'well-used: slutty',
                        'willing: horny'
                       ])

          # todo: Add "is wet" parameter
          
          self.DefaultNoun("vagina")
          self.IsPlural = False
          self.InnerVag = VaginaInner()
          self.OuterLabia = VaginaOuterLabia()
          self.InnerLabia = VaginaInnerLabia()
          self.Clitoris = Clitoris()

class AnusFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['anus x4: std,default,clinical,sphincter,sing',
                         'arse-cunt: crude,orifice,sing',
                         'ass: std,orifice,sing',
                         'asshole x4: std,slang,crude,sphincter,sing',
                         'back orifice: desc,clinical,orifice,sing',
                         'back passage: desc,orifice,sing',
                         'back-pussy: silly,crude,slang,orifice,sing',
                         'backdoor: desc,slang,orifice,sing',
                         'bowels: std,plur',
                         'brown hole: desc,slang,crude,sphincter,sing',
                         'bunghole: silly,crude,slang,sphincter,sing',
                         'chocolate starfish: silly,crude,slang,sphincter,sing',
                         'corn hole: silly,crude,slang,sphincter,sing',
                         'dirt-pipe: crude,slang,orifice,sing',
                         'dirt-box: crude,slang,orifice,sing',
                         'fart-blaster: silly,crude,slang,orifice,sing',
                         'fart-box: silly,crude,slang,orifice,sing',
                         'fart-hole: silly,crude,slang,sphincter,sing',
                         'heinie hole: desc,slang,cute,sphincter,sing',
                         'knot: desc,sphincter, sing',
                         'poop-chute: crude,slang,desc,orifice,sing',
                         'poop-trap: crude,slang,sing,sphincter',
                         'rear orifice: desc, clinical, orifice,sing',
                         'rectal cavity: desc, clinical, orifice,sing',
                         'rectum: std,clinical,orifice,sing',
                         'ring: desc,sphincter,sing',
                         'rosebud: desc,slang,cute,crude,sing',
                         'shit-hole: crude,slang,desc,orifice,sing',
                         'shitter: crude,slang,orifice,sing',
                         'sphincter x2: std,clinical,sphincter,sing',
                         'starfish x2: silly,cute,slang,sphincter,sing',
                        ])
       
          self.AdjList(['brown: color',
                        'clenched: small,tight,action',
                        'flexing: action',
                        'forbidden: taboo',
                        'fuckable: horny',
                        'gaping: large,gape,loose',
                        'knotted: small,tight,desc',
                        'lewd: horny',
                        'little x4: small,cute,',
                        'loose: gape,loose',
                        'MILF: age,older,milf',
                        'nasty: taboo',
                        'naughty: horny',
                        'pert: cute,young',
                        'perverted: slutty',
                        'puckered: action',
                        'rusty: desc,color',
                        'shameful: taboo',
                        'shy: horny,taboo',
                        'sinful: taboo',
                        'smooth: feel,desc',
                        'snug x2: small,tight,cute,'
                        'taboo: taboo',
                        'teasing: horny',
                        'tender: feel,desc,cute',
                        'tight x4: small,tight',
                        'wanton: horny',
                        'well-used: gape,older,slutty,loose',
                        'willing: horny',
                        'winking: small,tight,action',
                        'virgin: virginal',
                        'vulgar: taboo',
                       ])
          
          self.DefaultNoun("anus")
          
class ButtocksFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
     
          self.AddSkinColors = True

          self.NounList(['buns: std,plur',
                          'butt-cheeks: std,plur',
                          'buttocks: std,clinical,plur',
                          'cheeks:std,plur',
                         ])
               
          self.AdjList(['ample: large,curvy',
                        'big: size,large',
                        'bubble-butt: shape',
                        'bubble-shaped: shape',
                        'chubby: shape,plussize,curvy',
                        'college-girl: college,age,young',
                        'curvaceous: shape,curvy',
                        'curvy: curvy,shape',
                        'cute: cute',
                        'fat: shape,large,plussize',
                        'jiggling: movement',
                        'juicy: wet,taste,horny',
                        'lickable: taste,horny',
                        'luscious: super,large',
                        'MILF: age,older,milf',
                        'muscular: strong',
                        'petite: size,small',
                        'plump: shape,large,plussize,curvy',
                        'rotund: shape,large,plussize',
                        'round: shape',
                        'rounded: shape',
                        'shapely x3: shape,attractive',
                        'smooth: hairless,feel,texture',
                        'squeezable x2: horny',
                        'succulent: super,attractive,horny',
                        'supple: feel,texture,young',
                        'sweet: attractive',
                        'tender: feel',
                        'teen: age,young,teen',
                        'thick x3: size,large,shape,curvy',
                        'tight: size,small',
                        'trim: size,small',
                        'voluptuous: shape,curvy,attractive',
                        'well-rounded: shape',
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksFemale()
          
          self.NounList(['ass: std,default,sing',
               'backside: std,sing',
               'behind: std,sing',
               'booty: std,cute,slang,sing',
               'bottom: std,desc,sing',
               'bum: std,cute,slang,sing',
               'butt: std,slang,sing',
               'gluteous maximus: std,clinical,sing',
               'heinie: std,cute,slang,sing',
               'rump: desc,sing',
               'tush: cute,slang,sing',
               'tushy: cute,slang,sing'])
               
          self.AdjList(['ample: super,large',
                        'apple-shaped: shape',
                        'bare: nude',
                        'big: size,large',
                        'big, fat: size,large,curvy,plussize',
                        'black: color,poc',
                        'bountiful: super,large',
                        'broad: width,wide,plussize',
                        'brown: color,poc',
                        'bronzed: color',
                        'bubble-shaped: shape,curvy',
                        'chubby: plussize',
                        'coffee-colored: color,poc',
                        'college-girl: age,college',
                        'creamy: color,texture,cauc',
                        'curvaceous: curvy',
                        'curvy: curvy',
                        'cute: cute,size,small',
                        'cute little: cute,size,small',
                        'dark: color,poc',
                        'delightful: super',
                        'fat x4: plussize',
                        'firm: strong,texture',
                        'fuckable: horny',
                        'generous: super,large',
                        'glistening: shiny',
                        'heart-shaped: shape',
                        'huge: size,large,plussize',
                        'honeyed: super,texture,color,poc',
                        'jiggling: movement',
                        'juicy: super,taste',
                        'lush: super',
                        'luscious: super',
                        'MILF: age,older',
                        'muscular: muscular,shape',
                        'naked: nude',
                        'nubile: age,young',
                        'pale: color,cauc',
                        'perfect: super',
                        'pert: shape',
                        'pink: color,cauc',
                        'plump: curvy,plussize',
                        'ripe: super',
                        'rosy: color,cauc',
                        'rotund: shape,size,large',
                        'round: shape',
                        'rounded: shape',
                        'sexy: super',
                        'shameless: horny',
                        'shapely: shape,super',
                        'skinny: width,narrow,slender',
                        'slutty: horny',
                        'smooth: texture,hairless',
                        'squeezable: super',
                        'stately: age,older',
                        'stinky: smelly',
                        'succulent: super,taste',
                        'sultry: super',
                        'sun-bronzed: color',
                        'sun-kissed: color',
                        'supple: texture,young',
                        'sweet: super',
                        'svelte: width,narrow,texture,super',
                        'tempting: horny,super',
                        'tender: feel,super',
                        'tanned: color',
                        'taut: muscular',
                        'teenage: teen,age,young',
                        'thick x2: width,wide,curvy',
                        'tight x2: size,small',
                        'toned: firm,texture',
                        'trim: size,small',
                        'virgin: age,young',
                        'voluptuous: curvy',
                        'well-rounded: super,shape',
                        'white: color,cauc',
                        'wide: width,wide',
                        'womanly: super,curvy',
                        'youthful: age,young',
                        'yummy: super',
                       ])
          
          self.DefaultNoun("ass")
          
class BodyFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['anatomy: std,sing',
                         'body x4: std,default,sing',
                         'curves: plur',
                         'figure: std,sing',
                         'form: std,sing',
                         'physique: std,sing'])
               
          self.AdjList(['beautiful: attractive,super',
                        'breathtaking: super',
                        'busty: bigtits',
                        'buxom: bigtits',
                        'curvaceous: shape,curvy,bigtits,attractive',
                        'curvy: shape,curvy',
                        'feminine: curvy',
                        'gorgeous: super,attractive',
                        'leggy: longlegs',
                        'little: size,small',
                        'lush: super',
                        'luxuriant: super',
                        'model-esque: attractive',
                        'nubile: young,virginal',
                        'plus-size: size,large,plussize',
                        'ravishing: super,attractive,horny',
                        'ripe: attractive',
                        'sensual: attractive,super',
                        'sexy: attractive,super',
                        'shameless: horny',
                        'shapely: attractive,bigtits',
                        'slender: slender',
                        'statuesque: bigtits,older',
                        'stunning: super,attractive',
                        'sultry: attractive',
                        'sun-bronzed: color',
                        'sun-kissed: color',
                        'sweet: super,attractive,taste',
                        'teenage: young',
                        'tight: slender,size,small',
                        'voluptuous: bigtits,curvy',
                        'womanly: curvy',
                        'young: young',
                        'youthful: young',
                       ])
          
          self.DefaultNoun("body")
          self.DefaultAdj("nubile")

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
          
     
     def GetClothedBodyPartDesc(self, part, bLongDesc, sPossessive = None):
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
               sPartDesc = sPossessive + " " + part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
          else:
               sPartDesc = part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
               if bAddArticles:
                    sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bLongDesc = True, sPossessive = None):
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
               sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bLongDesc, sPossessive = sPossessive)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc
          
     def GetNakedBodyPartDesc(self, part, bLongDesc, sPossessive = None, NotList = None):
          sPartDesc = ""

          if NotList is None:
              NotList = []
          
          if sPossessive is None:
               sPossessive = ""
          
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
               sPartDesc = sPossessive + " " + part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = NotList)
          else:
               sPartDesc = part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = NotList)
          
          if bAddArticles:
               sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bExplicit = False, bLongDesc = True, sPossessive = None, NotList = None):
          sBodyDesc = ""

          if NotList is None:
              NotList = []
          
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
               sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bLongDesc, sPossessive = sPossessive)
               NotList += re.split(r',|\w|', sBodyDesc)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc

     def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bShortDesc = False):
          Parts = []
          AllParts = []
          
          if bIncludeInners:
               AllParts.append(self.Hips.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Legs.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Breasts.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Thighs.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Ass.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Ass.Anus.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Vagina.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Vagina.OuterLabia.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Vagina.InnerLabia.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Vagina.InnerVag.RandomDesc(bShortDesc = bShortDesc))
          else:
               AllParts.append(self.Hips.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Legs.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Breasts.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Thighs.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Ass.RandomDesc(bShortDesc = bShortDesc))
               AllParts.append(self.Vagina.RandomDesc(bShortDesc = bShortDesc))
               
          for x in sorted(sample(range(0, len(AllParts)), iNum)):
               Parts.append(AllParts[x])
               
          return Parts
                    
     def GetHoles(self, bIncludeMouth = True):
          Holes = []
          
          if bIncludeMouth:
               Holes = [3]
          
               Holes[0] = self.Mouth.RandomDesc()
               Holes[1] = self.Vagina.RandomDesc()
               Holes[2] = self.Ass.Anus.RandomDesc()
          else:
               Holes = [2]
               
               Holes[0] = self.Vagina.RandomDesc()
               Holes[1] = self.Ass.Anus.RandomDesc()
          
          return Holes
          
     def GetRandomHole(self, bIncludeMouth = True, bShortDesc = True, bLongDesc = True):
          sHole = ""
          Holes = []
          if bIncludeMouth:          
               Holes.append(self.Mouth.RandomDesc(bShortDesc = bShortDesc, bLongDesc = bLongDesc))
               Holes.append(self.Vagina.RandomDesc(bShortDesc = bShortDesc, bLongDesc = bLongDesc))
               Holes.append(self.Ass.Anus.RandomDesc(bShortDesc = bShortDesc, bLongDesc = bLongDesc))
          else:
               Holes.append(self.Vagina.RandomDesc(bShortDesc = bShortDesc, bLongDesc = bLongDesc))
               Holes.append(self.Ass.Anus.RandomDesc(bShortDesc = bShortDesc, bLongDesc = bLongDesc))
          
          iRand = randint(0, len(Holes) - 1)
          sHole = Holes[iRand]
          
          return sHole
          
class PenisHead(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['cock-head: silly,slang,sing',
                         'dick-tip: silly,crude,slang,sing',
                         'head x3: std,default,sing',
                         'helmet: desc,sing',
                         'knob x2: crude,silly,desc,slang,sing',
                         'mushroom: desc,sing',
                         'tip x3: std, default,sing',
                        ])
               
          self.AdjList(['broad: width,thick',
                        'brown: color,poc',
                        'bulging: shape',
                        'dripping: wet',
                        'engorged: aroused',
                        'fat: shape',
                        'glistening: shiny',
                        'pulsating: motion',
                        'purple: color',
                        'red: color',
                        'smooth: texture,feel',
                        'swollen: thick, aroused',
                        'thick: width,thick',
                        'throbbing: motion',
                        'tumescent: aroused'
                       ])
          
          self.DefaultNoun("head")
          self.IsPlural = False
          
class Testicles(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['balls x3: std,default,plur', 
                         'ballsack x2: silly,crude,slang,plur',
                         'bollocks: silly,crude,plur',
                         'gonads: std, clinical, plur',
                         'nuts: silly,slang,plur',
                         'nutsack: silly,slang,crude,sing',
                         'sack: desc,sing',
                         'scrotum x2: std,clinical,sing',
                         'silk purse: desc,sing',
                         'testicles x2: std,clinical,plur',
                        ])
               
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

class Penis(MaleBodyParts):
     def BuildAPenis(self, NotList = []):
          sPenis = ""
          
          iRandFront = 0
          iRandBack = 0
          
          iRandFront = randint(0,len(self.PenisFrontPart) - 1)
          iRandBack = randint(0,len(self.PenisBackPart) - 1)
          sFrontPart = self.PenisFrontPart[iRandFront]
          sBackPart = self.PenisBackPart[iRandBack]
          
          while FoundIn(sFrontPart, sBackPart) or FoundIn(sFrontPart, NotList) or FoundIn(sBackPart, NotList):
               iRandFront = randint(0,len(self.PenisFrontPart) - 1)
               iRandBack = randint(0,len(self.PenisBackPart) - 1)
               sFrontPart = self.PenisFrontPart[iRandFront]
               sBackPart = self.PenisBackPart[iRandBack]
               
          sPenis = sFrontPart + "-" + sBackPart
          
          while sPenis in self.GetNounList("silly"):
               iRandFront = randint(0,len(self.PenisFrontPart) - 1)
               iRandBack = randint(0,len(self.PenisBackPart) - 1)
               sFrontPart = self.PenisFrontPart[iRandFront]
               sBackPart = self.PenisBackPart[iRandBack]
               
               while FoundIn(sFrontPart, sBackPart) or FoundIn(sFrontPart, NotList) or FoundIn(sBackPart, NotList):
                    iRandFront = randint(0,len(self.PenisFrontPart) - 1)
                    iRandBack = randint(0,len(self.PenisBackPart) - 1)
                    sFrontPart = self.PenisFrontPart[iRandFront]
                    sBackPart = self.PenisBackPart[iRandBack]
                    
               sPenis = sFrontPart + "-" + sBackPart
               
          return sPenis
          
     def __init__(self, Params = None, NotList = None, TagLists = None, bAllowBAP = True):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['boner: silly,crude,hard,sing',
                         'choad: crude,slang,smalldick,sing',
                         'cock x3: std,default,slang,crude,sing',
                         'cock-meat: crude,sing',
                         'cocksicle: silly,crude,slang,sing',
                         'dick x3: std,slang,sing',
                         'erection x2: std,clinical,hard,sing',
                         'girth: desc,sing',
                         'goo-gun: silly,crude,semen,sing',
                         'hard-on: std,slang,hard,sing',
                         'hardness: desc,hard,sing',
                         'hot-rod: silly,crude,slang,sing',
                         'joystick: silly,slang,sing',
                         'lady-dagger: silly,slang,sing',
                         'love-gun: silly,slang,sing',
                         'meat: crude,slang,sing',
                         'member: std,clinical,sing',
                         'monster: silly,hard,bigdick,sing',
                         'organ: std,clinical,sing,',
                         'pecker: std,slang,smalldick',
                         'penis x4: std,clinical,sing',
                         'phallus: std,sing',
                         'pole: desc,hard,sing',
                         'popsicle: silly,slang,sing',
                         'prick: std,slang,crude,sing',
                         'ramrod: crude,desc,sing',
                         'rod: desc,sing',
                         'sausage: desc,silly,slang,crude,sing',
                         'schlong: silly,slang,sing',
                         'serpent: desc,sing',
                         'shaft: desc,sing',
                         'snake: desc,sing',
                         'stalk: desc,sing',
                         'stem: desc,sing',
                         'thing: std,silly,sing',
                         'tool: std, slang,sing',
                         'wood: crude,slang,sing'
                        ])

          # large, wide, 
          self.AdjList(['bald: hairless',
                        'black x4: color,poc',
                        'beautiful: super',
                        'beefy: bigdick,taste',
                        'bent: shape',
                        'big x4: size,bigdick',
                        'broad x2: width,wide',
                        'bulbous: shape',
                        'bulging x2: hard,bigdick,shape'
                        'burning: feel,warm',
                        'carefully man-scaped: style,trimmed',
                        'chocolate x2: color,poc',
                        'circumcised: cut',
                        'crooked: shape',
                        'curved: shape',
                        'dark: color,poc',
                        'delicious: taste,horny,super',
                        'dripping: wet',
                        'dusky: color',
                        'engorged x2: hard',
                        'enormous: size,bigdick',
                        'enormously erect: size,bigdick,hard',
                        'erect x2: hard',
                        'fat x4: size,width,wide',
                        'fevered: feel,warm',
                        'feverish: feel,warm',
                        'firm x3: hard,feel',
                        'fully engorged: hard',
                        'fully erect: hard',
                        'girthy x2: width,wide',
                        'glistening: wet,shiny',
                        'god-like: super',
                        'gnarled: shape',
                        'gorgeous: super,attractive',
                        'greasy x4: feel,wet',
                        'hairy x4: hairy',
                        'hairless x2: hairless',
                        'hard x3: hard',
                        'hardened: hard',
                        'heavy: bigdick,feel',
                        'hefty: bigdick',
                        'hooked: shape',
                        'hot x2: feel,attractive,super',
                        'huge: size,bigdick',
                        'hugely erect: size,bigdick,hard',
                        'impressive: super',
                        'knobby: shape',
                        'legendary: super',
                        'lengthy: length,long,bigdick',
                        'long: length,long,bigdick',
                        'lovingly man-scaped: style,trimmed',
                        'lustful x2: horny',
                        'magnificient: super',
                        'massive: size,bigdick',
                        'massively erect: size,bigdick,hard',
                        'meaty x3: feel,taste',
                        'monstrous: super,bigdick',
                        'mouth-watering: horny',
                        'oily: wet,shiny',
                        'pale: color,cauc',
                        'pierced: style',
                        'pink x3: color,cauc',
                        'powerful: horny,super',
                        'pretty: attractive',
                        'proud: poetic',
                        'pulsating: feel,throb',
                        'purple x2: color',
                        'raging: hard',
                        'rampant: hard',
                        'red: color',
                        'ribbed: feel,shape',
                        'rigid: hard',
                        'rock-hard: hard',
                        'serpentine: shape',
                        'short: smalldick,length,short',
                        'silken: feel',
                        'skinny: width,narrow,smalldick',
                        'smooth x3: hairless,feel',
                        'stiff x2: hard',
                        'strong x3: super,horny',
                        'stubby x5: smalldick,short',
                        'swollen x2: hard',
                        'tall: length,long,bigdick',
                        'tasty x3: taste,horny',
                        'thick x3: width,wide',
                        'throbbing x2: feel,throb',
                        'towering: length,long,size,bigdick',
                        'tumescent: hard',
                        'turgid x2:hard',
                        'two-toned: color',
                        'uncircumcised: style, cut',
                        'uncut: style, cut',
                        'veiny x4: texture',
                        'virile: attractive',
                        'warm: feel,warm',
                        'wrinkled: texture,older'
                        'well-oiled: shiny,wet',
                        'youthful: young',
                       ])
               
          self.PenisFrontPart = ['beef',
                                 'daddy',
                                 'flesh',
                                 'fuck',
                                 'love',
                                 'man',
                                 'meat',
                                 'rape',
                                 'splooge',
                                ]
               
          self.PenisBackPart = ['bayonette',
                               'bone',
                               'burrito',
                               'hammer',
                               'lance',
                               'meat',
                               'missile',
                               'monster',
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
                               'torpedo',
                               'tube',
                               'weapon',
                               'weasel',
                               'worm']
          
          self.DefaultNoun("cock")
          self.IsPlural = False
          self.Head = PenisHead()
          self.Testicles = Testicles()
          
          if bAllowBAP:
               for i in range(0, int(self.NounListLen() * (2/3))):
                    sBAP = self.BuildAPenis()
                    self.AddNounToList(sBAP,"silly")
                    self.AddNounToList(sBAP,"crude")
     
     def GetRandomPenisPart(self, NotList = None, bShortDesc = False):
          if NotList == None:
               NotList = []
               
          iRand = randint(1,3)
          
          if iRand == 1:
               return self.Head.RandomDesc(NotList = NotList, bShortDesc = bShortDesc)
          elif iRand == 2: 
               return self.Testicles.RandomDesc(NotList = NotList, bShortDesc = bShortDesc)
          else:
               return self.RandomDesc(NotList = NotList, bShortDesc = bShortDesc)
               
     def GenerateLength(self):
          sLength = ""
          
          iInch = randint(5, 15)
          sLength = str(iInch)
          if randint(1,3) == 2:
               sLength += " 1/2"
          sLength += "-inch: size"

          if iInch > 7:
              sLength += ",bigdick"
          
          return sLength

     def GetTLClass(self):
         return TagLists()
               
     def ShortDesc(self, NotList = None, TagLists = None, bAddLen = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().ShortDesc(NotList, TagLists)
          
     def MediumDesc(self, NotList = None, TagLists = None, bAddLen = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
               
          return super().MediumDesc(NotList, TagLists) 
          
     def FloweryDesc(self, NotList = None, TagLists = None, bAddLen = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().FloweryDesc(NotList, TagLists) 
          
     def RandomDesc(self, NotList = None, TagLists = None, bShortDesc = True, bLongDesc = True, bAddLen = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().RandomDesc(NotList, TagLists) 
     
class Semen(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['baby batter: silly,slang,sing',
                         'baby gravy: silly,crude,slang,sing',
                         'cock-milk: crude,slang,sing',
                         'cock-snot: crude,silly,slang,sing',
                         'cream: desc,sing',
                         'cum x4: std,slang,sing',
                         'daddy-sauce: silly,crude,slang,sing',
                         'gravy: desc,crude,sing',
                         'jizm: crude,slang,sing',
                         'jizz x2: crude,slang,sing',
                         'load x2: slang,sing',
                         'lotion: desc,sing',
                         'love juice: silly,slang,sing',
                         'man-custard: desc,silly,slang,sing',
                         'man-o-naise: silly,sing',
                         'man-milk: desc,silly,sing',
                         'man-seed: desc,sing',
                         'nut-butter: silly,slang,sing',
                         'penis pudding: silly,crude,slang,sing',
                         'sauce: desc,sing',
                         'seed x2: std,sing',
                         'semen x3: std,clinical,default,sing',
                         'sperm x2: std,clinical,plur',
                         'splooge: std,slang,sing',
                         'spunk: std,slang,sing',
                         'throat yogurt: silly,crude,slang,sing',
                         'trouser gravy: silly,crude,slang,sing',
                         'weiner sauce: silly,crude,slang,sing',
                        ])
               
          self.AdjList(['creamy x3: taste,color',
                        'delicious: taste,super',
                        'glossy: shiny',
                        'gooey x3: sticky',
                        'hot x3: feel,warm',
                        'nasty: gross,horny',
                        'nourishing: taste,horny',
                        'oozing: sticky',
                        'ropy: shape',
                        'salty x2: taste',
                        'silken: feel',
                        'silky: feel',
                        'sloppy x2: sticky,gross',
                        'sticky x4: sticky',
                        'tasty: taste,horny',
                        'thick x4: thick',
                        'warm x3: feel,warm',
                        'white-hot x2: warm',
                        'yummy: taste,horny',
                        'cream-colored: color',
                        'milky: color',
                        'pearly: color,shiny',
                        'pearlescent: color,shiny'])
          
          self.DefaultNoun("semen")
          self.DefaultAdj("gooey")
          
class ButtocksMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['buns: std,cute,desc,plur',
                         'butt cheeks: std,slang,plur',
                         'buttocks: std,default,clinical,plur',
                         'glutes: std,strong,plur',
                         ])
               
          self.AdjList(['beefy: large',
                        'broad: size,wide',
                        #'bronzed: color',
                        'chiseled: shape',
                        'compact: size,small,shape',
                        'hairy: hairy',
                        'lean: shape',
                        'manly: attractive',
                        'masculine: attractive',
                        'muscular: strong',
                        'rock-hard: feel,strong',
                        'sexy: attractive',
                        'smooth: hairless',
                        'strapping: strong',
                        'swole: size,large,shape',
                        'taut: strong',
                        #'tan: color',
                        'tight x2: size,small,shape',
                        'trim: size,narrow,shape',
                        'virile: attractive',
                        'well-defined: shape'
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksMale()
          
          self.AddSkinColors = True

          self.NounList(['ass x3: std,slang,default,sing',
                         'backside: std,sing',
                         'behind: std,sing',
                         'bottom: std,sing',
                         'bum: std,cute,sing',
                         'buns: desc,cute,plur',
                         'butt x3: std,sing',
                         'gluteous maximus: std,clinical,sing',
                         'rump: std,sing',
                         'tush: silly,slang,sing',
                        ])
               
          self.AdjList(['beefy: large',
                        'broad: size,wide',
                        #'bronzed: color',
                        'chiseled: shape',
                        'compact: size,small',
                        'hairy: hairy',
                        'lean: size,small',
                        'manly: attractive',
                        'masculine: attractive',
                        'muscular: strong',
                        'naked: nude',
                        'powerful: strong,super',
                        'rippling: shape',
                        'rock-hard: feel',
                        'smooth: hairless',
                        'strapping:  strong',
                        'supple: feel',
                        'taut: shape,strong',
                        'tight: shape,small',
                        'trim: shape,small',
                        'virile: attractive',
                        'well-defined: shape',
                       ])
          
          self.DefaultNoun("buttocks")
          
class SkinMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['skin x4: default,std,sing',
                         'flesh x2: std,sing',
                         'hide: std,sing',
                        ])
               
          self.AdjList(['bare: nude',
                        'exposed: bare',
                        'glistening: shiny,wet,texture',
                        'hairy: hairy',
                        'leathery: feel,texture,older',
                        'naked: nude',
                        'rough: texture',
                        'rugged: texture',
                        'smooth: texture',
                        'supple: feel,young,texture',
                        'tough: texture',
                        'warm: feel',
                        'weathered: texture,older',
                        'youthful: young'])
          
          self.DefaultNoun("skin")
          self.DefaultAdj("rugged")
          
class ShouldersMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True 

          self.NounList(['shoulders'])
               
          self.AdjList(['bare: nude',
                        'brawny: strong,large',
                        'broad: size,wide',
                        'mighty: strong',
                        'muscular: shape,strong',
                        'naked: nude',
                        'powerful: super',
                        'rugged: shape',
                        'square: shape,wide',
                        'strong: strong',
                        'sturdy: strong',
                        'well-built: shape',
                        'wide: size,wide'])

          self.DefaultNoun("shoulders")
          self.DefaultAdj("broad")
          
class MusclesMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['muscles: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: large,strong',
                        'broad: size,large,wide',
                        'bulging: shape',
                        'burly: strong',
                        'chiseled: shape',
                        'hard: feel',
                        'hulking: size,large',
                        'impressive: super',
                        'lean: size,small',
                        'magnificent: super',
                        'massive: size,large',
                        'mighty: strong',
                        'powerful: strong',
                        'robust: strong',
                        'rugged: shape',
                        'sinewy: poetic',
                        'strapping x2: poetic',
                        'strong: strong',
                        'sturdy: strong',
                        'supple: feel,young',
                        'taut: shape',
                        'toned: shape',
                        'tight: feel',
                        'well-built: size,large',
                        'well-defined: shape',
                        'whip-cord: shape',
                        'wood-carved: shape'])
          
          self.DefaultNoun("muscles")
          self.DefaultAdj("strapping")

class NipplesMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['nipples: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'bared: nude',
                        'black: color, poc',
                        'bold: hard',
                        'broad: size,large',
                        'brown: color,',
                        'chocolate: color',
                        'dark: color,',
                        'dusky: color',
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'firm: arousal',
                        'handsome: super,attractive',
                        'hard: arousal,',
                        'perfect: super,attractive',
                        'pert: arousal,cute',
                        'pierced: style',
                        'pink: color,cauc',
                        'prominent: poetic',
                        'reddish: color',
                        'small: size,small',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'sun-kissed: color',
                        'tanned: color',
                        'thick: size,large,arousal,',
                        'tiny: size,small,',
                        'turgid: arousal',
                        'wide: size,large'])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")
          
class ChestMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['chest x4: std,default,sing',
                         'pectorals: std,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: muscular',
                        'broad: size,large,wide',
                        'burly: muscular,size,large,shape',
                        'compact: size,small',
                        'dark-thatched: hairy',
                        'expansive: size,large,wide',
                        'hairy: hairy',
                        'lusty: horny',
                        'mighty: strong',
                        'muscular: muscular',
                        'naked: nude',
                        'oiled: wet,shiny',
                        'powerful: strong',
                        'rippling: super,shape',
                        'ripped: muscular',
                        'rugged: attractive',
                        'strapping: muscular,strong',
                        'strong: strong',
                        'sturdy: size,large',
                        'toned: muscular',
                        'wide: size,wide',
                        'uncovered: nude',
                        'virile: attractive',
                        'well-built: muscular',
                        'well-defined: muscular,shape',
                        'well-oiled: wet,shiny'])

          self.Nipples = NipplesMale()
          self.DefaultNoun("chest")
          self.DefaultAdj("broad")
          
class ArmsMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors = True

          self.NounList(['arms x4: std,default,plur',
                         'limbs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong',
                        'burly: shape,strong',
                        'long: size,length,long',
                        'mighty: strong',
                        'muscular: shape',
                        'naked: bare',
                        'powerful: super',
                        'protective: friendly',
                        'rippling: shape',
                        'ripped: strong,shape',
                        'short: size,short',
                        'sinewy: shape',
                        'strapping: strong',
                        'strong: strong',
                        'sturdy: size,large,wide',
                        'thick: size,wide',
                        'toned: shape',
                        'trunk-like: size,wide',
                        'well-built: shape',
                        'wiry: shape'])
          
          self.DefaultNoun("arms")
          self.DefaultAdj("muscular")
          
class EyesMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['eyes'])
               
          self.AdjList(['alluring: attractive',
                        'beautiful: super',
                        'blue: color,cauc',
                        'bright: shiny',
                        'brown: color',
                        'brooding: emotion',
                        'captivating: attractive',
                        'clear: ',
                        'dark: color',
                        'dazzling: shiny',
                        'deep: ',
                        'earnest: emotion',
                        'electric: attractive',
                        'electrifying: attractive',
                        'gray: color, cauc',
                        'green: color, cauc',
                        'hazel: color, cauc',
                        'icy-blue: color, cauc',
                        'kind: emotion',
                        'large: size,large',
                        'mischievous: emotion',
                        'narrow: size,narrow',
                        'penetrating: emotion',
                        'small: size,small',
                        'soulful: emotion',
                        'sparkling: shiny',
                        'steely: emotion',
                        'steely-blue: color, cauc',
                        'stern: emotion',
                        'sweet: young,attractive',
                        'youthful: young',
                        'wide: size,wide,large',
                       ])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("penetrating")

class FacialHair(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['beard x3: beard,std,default,sing',
                         'fuzz: stubble,std,sing',
                         'goatee: goatee,std,sing',
                         'moustache: moustache,std,sing',
                         'stubble: stubble,std,sing',
                        ])
               
          self.AdjList(['black x2: color',
                        'blonde x2: color,cauc',
                        'bristling: style',
                        'brown: color',
                        'bushy: shape',
                        'coifed: style',
                        'curly: shape',
                        'dark: color',
                        'full: size,large',
                        'glossy: shiny',
                        'gray: color, older',
                        'long: size,large',
                        'luxuriant: super',
                        'magnificent: super',
                        'manly: attractive',
                        'messy: style',
                        'red: color, cauc',
                        'sandy: color,cauc',
                        'silken: feel',
                        'short: size,small,style',
                        'thick: size,large',
                        'trimmed: style',
                        'unkempt: style',
                        'untamed: style',
                        'well-trimmed: style',
                        'wild: style',
                        'wiry: style'])
          
          self.DefaultNoun("beard")
          self.DefaultAdj("glossy")
          
class HairMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['afro: std,poc,sing',
                         'bouffant: std,sing',
                         'coif: std,sing',
                         'dreads: std,plur',
                         'fro: std,poc,sing',
                         'hair x4: std,default,sing',
                         'locks x3: std,plur'
                        ])
               
          self.AdjList(['black x2: color',
                        'blonde x2: color,cauc',
                        'brunette: color',
                        'coifed: style',
                        'curly: shape',
                        'dark: color',
                        'dyed-green: color,fake',
                        'flaming-red: color,cauc',
                        'glossy: shiny',
                        'golden: color,young,cauc',
                        'graying: color,older',
                        'long: size,length,long',
                        'luxuriant: super',
                        'messy: style',
                        'platinum blonde: color',
                        'punk blue: color,fake',
                        'red: color,cauc',
                        'sandy: color,cauc',
                        'silken: feel',
                        'shaggy: style',
                        'short: size,length,short,small',
                        'spiky: style',
                        'untamed: style',
                        'vibrant: super',
                        'wavy: shape',
                        'wild: style'])
          
          self.DefaultNoun("hair")
          self.DefaultAdj("glossy")
          
class LegsMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          self.AddSkinColors = True

          self.NounList(['legs x3: std,default,plur',
                         'calves: std,plur',
                         'limbs: std,plur',
                         'thighs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong,large,shape',
                        #'bronzed: color',
                        'burly: strong,large,shape',
                        'long: length,long',
                        'mighty: strong',
                        'muscular: strong,shape',
                        'naked: bare',
                        'powerful: super',
                        'rangy: length,long,width,narrow',
                        'rippling: shape',
                        'sinewy: shape',
                        'short: length,short',
                        'slender: width,narrow',
                        'slim: width,narrow',
                        'strapping: strong',
                        'strong: strong',
                        'sturdy: width,wide',
                        'thick: width,wide',
                        'toned: shape',
                        'trunk-like: shape,width,wide',
                        'well-built: shape',
                        'wiry: width,narrow'
                       ])
          
          self.DefaultNoun("legs")
          self.DefaultAdj("sinewy")
          
class JawMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.NounList(['jaw'])
               
          self.AdjList(['angular: shape',
                        'bearded: beard,hairy',
                        'chiseled: shape',
                        'commanding: attitude',
                        'decisive: attitude',
                        'dominant: attitude',
                        'forceful: attitude',
                        'handsome: attractive',
                        'powerful: attitude',
                        'rugged: shape',
                        'scruffy: stubble,hairy',
                        'sharp: shape',
                        'smooth-shaven: hairless',
                        'square: shape',
                        'striking: attractive',
                        'stubbled: stubble,hairy',
                        'unshaven: stubble,hairy',
                       ])
          
          self.DefaultNoun("jaw")
          self.DefaultAdj("chiseled")
          
class BodyMale(MaleBodyParts):     
    def __init__(self, Params = None, NotList = None, TagLists = None):
        super().__init__(Params, NotList, TagLists)
          
        self.AddSkinColors = True

        self.NounList(['body x4: std,default,sing',
                       'build: std,sing',
                       'bulk: std,large,heavy,sing',
                       'form: std,sing',
                       'physique x2: std,sing',
                      ])
               
        self.AdjList(['beefy: large',
                      'brawny: strong,shape',
                      'broad: size,wide',
                      #'bronzed: color',
                      'burly: strong,shape,size,wide',
                      'commanding: attitude',
                      'compact: size,small',
                      'dad-bod: plussize',
                      'dark-thatched: hairy',
                      'godlike: super',
                      'handsome: attractive',
                      'hardened: strong',
                      'hearty: size,large',
                      'hung: bigdick',
                      'husky: size,large,plussize',
                      'lanky: width,narrow',
                      'lean: width,narrow',
                      'limber: flexible',
                      'manly: manly',
                      'masculine: manly',
                      'massive: size,large',
                      'muscular: shape',
                      'powerful: strong',
                      'rugged: shape',
                      'sexy: attractive',
                      'short: length,short',
                      'sinewy: shape',
                      'smooth: hairless',
                      'strapping: strong',
                      'striking: attractive',
                      'strong: strong',
                      'sturdy: size,large',
                      'supple: flexible,young',
                      'tall: height,tall',
                      'taut: shape',
                      'thin: width,narrow',
                      'tight: shape,strong',
                      'toned: shape,strong',
                      'towering: size,large,height,tall',
                      'trim: width,narrow',
                      'virile x2: manly',
                      'well-built: shape',
                      'well-hung: bigdick',
                      'wiry: width,narrow',
                      'youthful: young',
                     ])
          
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
     
    def GetClothedBodyPartDesc(self, part, bLongDesc, sPossessive = None):
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
            sPartDesc = sPossessive + " " + part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bLongDesc = True, sPossessive = None):
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
            sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bLongDesc, sPossessive = sPossessive)
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1
               
        return sBodyDesc
          
    def GetNakedBodyPartDesc(self, part, bLongDesc, sPossessive = None):
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
            sPartDesc = sPossessive + " " + part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDesc(bShortDesc = False, bLongDesc = bLongDesc, NotList = PartNotList)
          
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bPenis = True, bAss = True, bExplicit = False, bLongDesc = True, sPossessive = None):
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
            PartPriorities.append([balls,9])
            PartPriorities.append([head,10])
            #PartPriorities.append([asshole,11])
          
        PartGroups = []
          
        if iNum == 3:
            for part1 in PartPriorities: #skin 6
                for part2 in PartPriorities[PartPriorities.index(part1) + 1:]:
                    if part2[1] > part1[1] or (part2[1] == part1[1] and not part2[0] == part1[0]):
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
        
        SelectedParts = None
        
        if len(PartGroups) > 1:
            SelectedParts = PartGroups[randint(0,len(PartGroups) - 1)]
        elif len(PartGroups) == 1:
            SelectedParts = PartGroups[0]

        iLoops = 0
        while iLoops < iNum:
            sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bLongDesc, sPossessive = sPossessive)
               
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1

        return sBodyDesc
          
 
    def GetRandomIntimateParts(self, iNum, bIncludeInners, bShortDesc = False):
        Parts = []
        AllParts = []
          
        if bIncludeInners:
            AllParts.append(self.Shoulders.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Chest.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Legs.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Ass.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Penis.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Penis.Head.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Penis.Testicles.RandomDesc(bShortDesc = bShortDesc))
        else:
            AllParts.append(self.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Shoulders.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Chest.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Legs.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Ass.RandomDesc(bShortDesc = bShortDesc))
            AllParts.append(self.Penis.RandomDesc(bShortDesc = bShortDesc))
               
        for x in sorted(sample(range(0, len(AllParts)), iNum)):
            Parts.append(AllParts[x])
               
        return Parts


#for i in range(6):
#    TestMale = Man()

#for i in range(6):
#    TestFem = Woman()