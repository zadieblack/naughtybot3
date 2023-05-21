#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Bodies module

from random import *

from util import *
from excerpt.ex_helpers import *
from excerpt.bodyparts import *
import names as names

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

        # Need to pass colors in like:
        #   EyeColor + ": " + self.Race.TagName + ",color,eyes"
        #   HairColor + ": " + self.Race.TagName + ",color,hair"
        #   NipColor + ": " + self.Race.TagName + ",color"
        #   SkinColor + ": " + self.Race.TagName + ",color"
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

        if self.Race in ["asian","caucasian"] and self.IsTan:
            self.SkinColor = choice(TanColors)
        else:
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

        # Need to pass colors in like:
        #   EyeColor + ": " + self.Race.TagName + ",color,eyes"
        #   HairColor + ": " + self.Race.TagName + ",color,hair"
        #   NipColor + ": " + self.Race.TagName + ",color"
        #   SkinColor + ": " + self.Race.TagName + ",color"
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
        ButtocksParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Anus = AnusFemale(TagLists = LTagLists)
        self.Buttocks = ButtocksFemale(Params = ButtocksParams, TagLists = LTagLists)
        self.Ass = AssFemale(Params = SkinParams, TagLists = LTagLists)
        self.Ass.Anus = self.Anus
        self.Ass.Buttocks = self.Buttocks

        # Back
        BackParams = NPParams(sColor = GetSkinonym(self.SkinColor))

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

        BreastsParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Breasts = Breasts(Params = BreastsParams, TagLists = BreastTagLists)
        self.Breasts.Nipples = self.Nipples

        # Eyes
        self.Eyes = Eyes(Params = EyeParams, TagLists = LTagLists)

        # Face
        FaceParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Face = Face(Params = FaceParams, TagLists = LTagLists)

        # Hair 
        self.Hair = Hair(Params = HairParams, TagLists = LTagLists)

        # Hips
        HipsParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Hips = Hips(Params = HipsParams, TagLists = LTagLists)

        # Legs
        LegsParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Legs = Legs(Params = LegsParams, TagLists = LTagLists)

        # Lips
        self.Lips = Lips(TagLists = LTagLists)

        # Mouth
        self.Mouth = Mouth(TagLists = LTagLists)

        # Skin
        VarSkinParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Skin = Skin(Params = VarSkinParams, TagLists = LTagLists)

        # Thighs
        ThighsParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Thighs = Thighs(Params = ThighsParams, TagLists = LTagLists)

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
        BodyParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Body = BodyFemale(Params = BodyParams, TagLists = LTagLists)
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
        sIsFit = "IsFit: " + str(self.IsFit)
        sIsTan = "IsTan: " + str(self.IsTan)
        sPubeStyle = "PubeStyle: " + self.PubeStyle
        sDesc = "[Gender: Female".ljust(20) + sAge.ljust(20) + sRace.ljust(20) + sBodyType.ljust(20) 
        sDesc += sSkinColor.ljust(20) + sHairColor.ljust(20) + sEyeColor.ljust(20) + sNipColor.ljust(20)
        sDesc += sVirgin.ljust(20) + sBustSize.ljust(20) + sFakeTits.ljust(20) + sPubeStyle.ljust(20) 
        sDesc += sIsFit.ljust(20) + sIsTan.ljust(59) + "]"

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

        AdjList = ['beautiful: super',
                   'bright-eyed: eyes',
                   'cute: super,young',
                   'doe-eyed: eyes',
                   'exotic: super,poc',
                   'little: size,small,short',
                   'lovely: super',
                   'matronly: age,older',
                   'nubile x2: age,young',
                   'pretty: super',
                   'sexy: super',
                   'striking: super',
                   'wide-eyed: eyes',
                  ]

        if self.BustSize in ["large","huge"]:
            AdjList += ['ample-bosomed: bigtits','big-titted: bigtits','bosomy: bigtits,shape','busty: bigtits','buxom: bigtits','full-figured: bigtits,shape','shapely: curvy,bigtits,shape','stacked: bigtits,shape','statuesque: bigtits,shape','voluptuous: bigtits,curvy,shape',]
        elif self.BustSize in ["small"]:
            AdjList += ['flat-chested: smalltits','lithe: slender,flexible','petite: short,small,slender','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]
            
        if self.BodyType in ["plussize"]:
             AdjList += ['chubby: plussize,shape','Rubenesque: plussize,shape','plump: curvy,plussize,shape',]
        elif self.BodyType in ["curvy"]:
            AdjList += ['curvaceous: curvy,shape','round-bottomed: curvy,shape','shapely: curvy,shape']
        elif self.BodyType in ["slender"]:
            AdjList += ['elfin: slender','limber:slender,flexible','lithe: slender,flexible','petite: short,small,slender','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]

        if self.EyeColor in ["blue"]:
            AdjList += ['blue-eyed x3: eyes,cauc',]
        elif self.EyeColor in ["green"]:
            AdjList += ['green-eyed: eyes,cauc',]
        else:
            AdjList += ['brown-eyed x2: eyes','dark-eyed: eyes',]

        if self.Height in ["tall"]:
            AdjList += ['tall: height,tall','willowy: height,tall']
        elif self.Height in ["short"]:
            AdjList += ['petite: short,small,slender','short: height,short',]

        if self.HairStyle in ["bobbed"]:
            AdjList += ['bobbed: hairstyle,bob,shorthair',]
        elif self.HairStyle in ["braids"]:
            AdjList += ['braided: hairstyle,braids',]
        elif self.HairStyle in ["cornrows"]:
            AdjList += ['cornrowed: hairstyle,cornrows,poc',]
        elif self.HairStyle in ["curls"]:
            AdjList += ['curly: hairstyle,curls','curly-haired: hairstyle,curls',]
        elif self.HairStyle in ["fro"]:
            AdjList += ['afro\'d: hairstyle,fro,poc',]
        elif self.HairStyle in ["kinky"]:
            AdjList += ['kinky-haired: hairstyle,kinky,poc',]
        elif self.HairStyle in ["long"]:
            AdjList += ['long-haired: hairstyle,longhair',]
        elif self.HairStyle in ["pigtails"]:
            AdjList += ['pigtailed: hairstyle,pigtails',]
        elif self.HairStyle in ["pixie"]:
            AdjList += ['pixie-cut: hairstyle,pixie,shorthair',]
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

        self.Woman = NounPhrase(NPParams(sColor = GetSkinonym(self.SkinColor)))
        self.Woman.NounList(NounList)
        self.Woman.AdjList(AdjList)
        self.Noun = self.Woman.GetNoun()
        self.Desc = self.Woman.FloweryDesc(TagLists = TagLists(adj_excl = ["color"]))
        self.DescWords = self.Woman.GetDescWordList()

        return True

