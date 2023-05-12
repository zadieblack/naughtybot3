#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from collections import namedtuple
from random import *

from util import *
from excerpt.ex_helpers import *
import names as names

Race = namedtuple("Race", "Name HairColor EyeColor SkinColor NipColor")

RaceCauc  = Race("caucasian",
                 ["black","blonde","brown","dark","gray","red"],
                 ["amber","blue","brown","dark","gray","green","hazel"],
                 ["beige","creamy","freckled","fresh pink","honeyed","light","pale","pink","porcelain","rosy","tanned","sun-bronzed","sun-browned","sun-kissed","white"],
                 ["brown","dark","pink","rosy","tan"]
                )
RacePOC   = Race("poc",
                 ["black","brown","dark",],
                 ["amber","brown","dark",],
                 ["black","beige","bronze","bronzed","brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha","tan"],
                 ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"]
               )
RaceAsian = Race("asian",
                 ["black","brown","dark",],
                 ["brown","dark",],
                 ["almond","beige","brown","creamy","freckled","light","light brown","pale","porcelain","tan","sun-bronzed","sun-browned","sun-kissed","white"],
                 ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"]
                )

class BodyParts(NounPhrase):
    pass

GenPhysTraits = namedtuple("GenPhysTraits",
                           "FirstName LastName Gender Race PubeStyle",
                           defaults = ["","","",None,""]
                          )
class Lover():
    def __init__(self, Gender, NewGenTraits = None):
        self.FirstName = ""
        self.LastName = ""
        self.Gender = ""
        self.Race = None
        self.RaceName = ""
        self.HairColor = ""
        self.EyeColor = ""
        self.SkinColor = ""
        self.NipColor = ""
        self.PubeStyle = ""

        self._TagLists = TagListParams()

        if NewGenTraits is None or not isinstance(NewGenTraits, GenPhysTraits):
            NewGenTraits = GenPhysTraits()
        
        # Set attributes if not blank, otherwise randomize
        self.Gender = Gender

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

        if NewGenTraits.Race and isinstance(Race, NewGenTraits.Race):
            self.Race = NewGenTraits.Race
        else:
            self.Race = choice([RaceCauc,RacePOC,]) # Add RaceAsian

        self.RaceName = self.Race.Name

        TagLists = self._TagLists

        # Handle race
        if self.RaceName == "caucasian":
            TagLists.adj_excl.append("poc")
            TagLists.noun_excl.append("poc")
        elif self.RaceName == "poc":
            TagLists.adj_excl.append("cauc")
            TagLists.noun_excl.append("cauc")

        if NewGenTraits.PubeStyle:
            self.PubeStyle = NewGenTraits.PubeStyle
        else:
            self.PubeStyle = choice(["hairy","shaved","trimmed"])

        if self.PubeStyle == "hairy":
            TagLists.adj_excl.append("shaved")
            TagLists.adj_excl.append("trimmed")
        elif self.PubeStyle == "trimmed":
            TagLists.adj_excl.append("shaved")
            TagLists.adj_excl.append("hairy")
        elif self.PubeStyle == "shaved":
            TagLists.adj_excl.append("trimmed")
            TagLists.adj_excl.append("hairy")

        self.HairColor = choice(self.Race.HairColor)
        self.EyeColor = choice(self.Race.EyeColor)
        self.SkinColor = choice(self.Race.SkinColor)
        self.NipColor = choice(self.Race.NipColor)

MalePhysTraits = namedtuple("MalePhysTraits",
                            "AgeCat Age HeightType BodyType HairStyle HasFacialHair FacialHairStyle DickInches IsCircumcised",
                            defaults = ["",0,"","",False,"","",0,None]
                           )

class Man(Lover):
    def __init__(self, NewGenTraits = None, NewMaleTraits = None):
        super().__init__("male", NewGenTraits = NewGenTraits)

        self.AgeCat = ""
        self.Age = 0
        self.HeightType = ""
        self.BodyType = ""
        self.HairStyle = ""
        self.HasFacialHair = False
        self.FacialHairStyle = ""
        self.DickInches = 0
        self.IsCircumcised = False

        TagLists = self._TagLists

        if NewMaleTraits is None or not isinstance(NewMaleTraits, MalePhysTraits):
            NewMaleTraits = MalePhysTraits()
        
        # Handle age 
        if NewMaleTraits.AgeCat:
            self.AgeCat = NewMaleTraits.AgeCat
        else:
            self.AgeCat = choice(["teen","college","twenties","thirties","middleaged","older"])
                
        if self.AgeCat in ["teen","college","twenties"]:
            TagLists.adj_excl.append("older")
        else:
            TagLists.adj_excl.append("young")

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

        if self.DickInches < 5:
            TagLists.adj_excl.append("smalldick")
            TagLists.noun_excl.append("smalldick")
        elif self.DickInches >= 7:
            TagLists.adj_excl.append("bigdick")
            TagLists.noun_excl.append("bigdick")
        else:
            TagLists.adj_excl.append("bigdick")
            TagLists.adj_excl.append("smalldick")
            TagLists.noun_excl.append("bigdick")
            TagLists.noun_excl.append("smalldick")

        if NewMaleTraits.IsCircumcised is None:
            self.IsCircumcised = CoinFlip()
        else:
            self.IsCircumcised = NewMaleTraits.IsCircumcized

        # Bodyparts
        self.Arms = ArmsMale(TagLists = TagLists)

        self.Ass = AssMale(TagLists = TagLists)
        self.Anus = AnusFemale(TagLists = TagLists)
        self.Buttocks = ButtocksMale(TagLists = TagLists)

        if self.HeightType == "short":
            BodyTagLists = TagListParams(adj_excl = ["tall"] + TagLists.adj_excl)
        elif self.HeightType == "tall":
            BodyTagLists = TagListParams(adj_excl = ["short"] + TagLists.adj_excl)
        else:
            BodyTagLists = TagListParams(adj_excl = ["short","tall"] + TagLists.adj_excl)

        self.Body = BodyMale(TagLists = BodyTagLists)
        self.Chest = ChestMale(TagLists = TagLists)
        self.Eyes = EyesMale(TagLists = TagLists)
        self.FacialHair = FacialHair(TagLists = TagLists)
        self.Hair = HairMale(TagLists = TagLists)
        self.Jaw = JawMale(TagLists = TagLists)
        self.Legs = LegsMale(TagLists = TagLists)
        self.Muscles = MusclesMale(TagLists = TagLists)

        if self.IsCircumcised:
            PenisTagLists = TagListParams(adj_excl = ["cut"] + TagLists.adj_excl)
        else:
            PenisTagLists = TagListParams(adj_excl = ["uncut"] + TagLists.adj_excl)

        self.Penis = Penis(TagLists = PenisTagLists)
        self.Head = PenisHead(TagLists = TagLists)
        self.Testicles = Testicles(TagLists = TagLists)

        self.Shoulders = ShouldersMale(TagLists = TagLists)
        self.Skin = SkinMale(TagLists = TagLists)

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

        sCut = ""
        if self.IsCircumcised:
            sCut = "circumcised"
        else:
            sCut = "uncircumcised"

        sDesc = "My name is " + self.FirstName + " " + self.LastName + ". "
        sDesc += "I am a " + str(self.Age) + "-year-old " + self.RaceName + " " + self.Gender + ". "
        sDesc += "I am a " + self.HeightType + ", " + self.BodyType + " man. "
        sDesc += "I proudly sport a " + str(self.DickInches) + "-inch cock "
        sDesc += "and I keep my pubes " + self.PubeStyle + "! "
        sDesc += "Some of my other notable physical characteristics are "
        sDesc += "my " + self.Eyes.FloweryDescription() + ", "
        sDesc += "my " + self.Hair.FloweryDescription() + ", "
        sDesc += "my " + self.Body.FloweryDescription() + ", "
        sDesc += "my " + self.Skin.FloweryDescription() + ", "
        sDesc += "and my " + sCut + " " + self.Penis.FloweryDescription() + "."
        print(sDesc + "\n")

FemPhysTraits = namedtuple("FemPhysTraits",
                           "AgeCat Age BodyType BustSize HasFakeTits HairStyle IsVirgin",
                           defaults = ["",0,"","",None,"", None]
                          )

class Woman(Lover):
    def __init__(self, NewGenTraits = None, NewFemTraits = None):
        super().__init__("female", NewGenTraits = NewGenTraits)

        self.AgeCat = ""
        self.Age = 0
        self.BodyType = ""
        self.HairStyle = ""
        self.BustSize = ""
        self.HasFakeTits = False
        self.IsVirgin = False

        TagLists = self._TagLists

        if NewFemTraits is None or not isinstance(NewFemTraits, FemPhysTraits):
            NewFemTraits = FemPhysTraits()

        if NewFemTraits.AgeCat:
            self.AgeCat = NewFemTraits.AgeCat
        else:
            self.AgeCat = choice(["teen","college","college","twenties","twenties","milf","milf"])
                
        if NewFemTraits.Age:
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
            TagLists.adj_excl.append("older")
        else:
            TagLists.adj_excl.append("young")

        if NewFemTraits.BodyType:
            self.BodyType = NewFemTraits.BodyType
        else:
            self.BodyType = choice(["slender","avg","curvy","plussize"])

        if self.BodyType in ["slender","avg"]:
            TagLists.adj_excl.append("plussize")
        elif self.BodyType in ["curvy","plussize"]:
            TagLists.adj_excl.append("slender")
        
        if NewFemTraits.HairStyle:
            self.HairStyle = NewFemTraits.HairStyle
        else:
            self.HairStyle = choice(["long","short","curly"])
        
        if NewFemTraits.BustSize:
            self.BustSize = NewFemTraits.BustSize
        else:
            self.BustSize = choice(["small","normal","large","huge"])

        if isinstance(NewFemTraits.HasFakeTits, bool):
            self.HasFakeTits = NewFemTraits.HasFakeTits
        else:
            if self.BustSize in ["large","huge"]:
                self.HasFakeTits = choice([False,False,True])
            else:
                self.HasFakeTits = False

        if isinstance(NewFemTraits.IsVirgin, bool):
            self.IsVirgin = NewFemTraits.IsVirgin
        else:
            if self.AgeCat in ["college","twenties"]:
                self.IsVirgin = choice([True,False,False,False])
            elif self.AgeCat in ["teen"]:
                self.IsVirgin = CoinFlip()
            else:
                self.IsVirgin = False

        if not self.IsVirgin:
            TagLists.adj_excl.append("virginal")
            TagLists.adj_excl.append("tight")

        self.Ass = AssFemale(TagLists = TagLists)
        self.Anus = AnusFemale(TagLists = TagLists)
        self.Buttocks = ButtocksFemale(TagLists = TagLists)
        self.Back = BackFemale(TagLists = TagLists)
        self.Body = BodyFemale(TagLists = TagLists)

        BreastTagLists = None
        if self.BustSize == "small":
            BreastTagLists = TagListParams(adj_excl = ["bigtits"] + TagLists.adj_excl, noun_excl = ["bigtits"] + TagLists.noun_excl)
        elif self.BustSize == "large":
            BreastTagLists = TagListParams(adj_excl = ["smalltits"] + TagLists.adj_excl, noun_excl = ["smalltits"] + TagLists.noun_excl)
        else:
            BreastTagLists = TagListParams(adj_excl = TagLists.adj_excl, noun_excl = TagLists.noun_excl)

        if not self.HasFakeTits:
            BreastTagLists.adj_excl.append("fake")
            BreastTagLists.noun_excl.append("fake")

        self.Breasts = Breasts(TagLists = BreastTagLists)
        self.Nipples = Nipples(TagLists = TagLists)
        self.Eyes = Eyes(TagLists = TagLists)
        self.Face = Face(TagLists = TagLists)
        self.Hair = Hair(TagLists = TagLists)
        self.Hips = Hips(TagLists = TagLists)
        self.Legs = Legs(TagLists = TagLists)
        self.Lips = Lips(TagLists = TagLists)
        self.Mouth = Mouth(TagLists = TagLists)
        self.Skin = Skin(TagLists = TagLists)
        self.Thighs = Thighs(TagLists = TagLists)

        if self.PubeStyle == "shaved":
            VagTagLists = TagListParams(adj_excl = ["hairy","trimmed"] + TagLists.adj_excl, noun_excl = ["hairy","trimmed"])
        elif self.PubeStyle == "hairy":
            VagTagLists = TagListParams(adj_excl = ["shaved","trimmed"] + TagLists.adj_excl, noun_excl = ["shaved","trimmed"])
        elif self.PubeStyle == "trimmed":
            VagTagLists = TagListParams(adj_excl = ["shaved","hairy"] + TagLists.adj_excl, noun_excl = ["shaved","hairy"])

        self.Vagina = Vagina(TagLists = VagTagLists)
        self.Clitoris = Clitoris(TagLists = TagLists)
        self.InnerLabia = VaginaInnerLabia(TagLists = TagLists)
        self.InnerVagina = VaginaInner(TagLists = TagLists)
        self.OuterLabia = VaginaOuterLabia(TagLists = TagLists)

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

        sAge = "AgeCat: " + self.AgeCat
        sRace = "Race: " + self.RaceName
        sBodyType = "BodyType: " + self.BodyType
        sBustSize = "BustSize: " + self.BustSize
        sVirgin = "IsVirgin: " + str(self.IsVirgin)
        sFakeTits = "HasFakeTits: " + str(self.HasFakeTits)
        sPubeStyle = "PubeStyle: " + self.PubeStyle
        sDesc = "[" + sAge.ljust(20) + sRace.ljust(20) + sBodyType.ljust(20) + sVirgin.ljust(20)  
        sDesc += sBustSize.ljust(20) + sFakeTits.ljust(20) + sPubeStyle.ljust(19) + "]\n"
        sDesc += "My name is " + self.FirstName + " " + self.LastName + ". "
        sDesc += "I am a " + str(self.Age) + "-year-old woman. "
        sDesc += "Some of my notable physical characteristics are "
        sDesc += "my " + self.Eyes.FloweryDescription() + ", "
        sDesc += "my " + self.Hair.FloweryDescription() + ", "
        sDesc += "my " + self.Skin.FloweryDescription() + ", "
        sDesc += "my " + self.Breasts.FloweryDescription() + " "
        sDesc += "with " + self.Nipples.FloweryDescription() + ", "
        sDesc += "and my " + self.Vagina.FloweryDescription() + ". "
        print(sDesc + "\n")

#A lover() object is a collection of attributes and body parts.
#	- Attributes like:
#		- Gender 
#		- Race 
#		- Age
#			- General categories but also pick a specific year 
#		- Hair color 
#       - Eye color
#       - Skin color
#		- Bust size
#       - Nipple color
#		- Whether pubes are shaved or trimmed
#   - Body parts are stored in a list. 
#       - Example: [Hair,Eyes,Breasts,Back,Thighs,Vagina,Ass,Legs]
#       - Or possibly sub-lists such as Chest, Genitalia and Backside
#   - All body parts are automatically intialized with tag restrictions to make sure they are consistent 
#   - Initialized body parts properties don't change when Reset is called 
#   - Could have other attributes, such as a profession.

class MaleBodyParts(BodyParts):
    def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          self.Gender = "male"

class FemaleBodyParts(BodyParts):
    def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          self.Gender = "female"

class Face(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['face x3: default,std,sing',
                         'features: poetic,plur'
                        ])
          
          self.AdjList(['adorable: super,cute,young,attractive',
                        'angelic: super,cute,attractive',
                        'beaming: emotion,happy',
                        'beautiful: super,attractive',
                        'cute: super,cute,attractive',
                        'delicate: cute',
                        'dark: color',
                        'elegant: older,attractive',
                        'excited: emotion,happy',
                        'expressive: emotion',
                        'gentle: attitude',
                        'gorgeous: super,attractive',
                        'flushed: arousal',
                        'freckled: color,cauc',
                        'heart-shaped: shape',
                        'innocent: attitude,cute,young,virginal',
                        'lovely: super,attractive',
                        'oval: shape',
                        'pale: color,cauc',
                        'pretty: attractive',
                        'radiant: ',
                        'rosy: color,young',
                        'round: shape',
                        'smiling: emotion,happy',
                        'startled: emotion',
                        'sweet: attitude,cute,attractive',
                        'warm: attitude,feel',
                        'wide-eyed: cute,attractive'])
               
          self.DefaultNoun('face')
          
class BackFemale(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['skin x4: default,std,sing',
                         'flesh: sing'
                        ])
                              
          self.AdjList(['almond-colored: asian,color',
                        'bare: nude',
                        'brown: color,poc',
                        'chocolate: color,taste,poc,',
                        'chocolate-colored: color,poc,',
                        'coffee-colored: color,poc',
                        'creamy: texture,color,taste,cauc',
                        'dark: color,poc',
                        'delicate: texture,cute',
                        'exposed: nude',
                        'freckled: texture,cauc',
                        'fresh pink: color,cauc',
                        'gentle: feel,texture',
                        'gleaming: texture,shiny',
                        'glistening: wet,texture,shiny',
                        'glowing: texture',
                        'gossamer: feel,texture',
                        'honeyed: color, taste,texture',
                        'luscious: taste,super',
                        'lustrous x2: texture,shiny',
                        'naked: nude',
                        'pale: color,cauc',
                        'perfect: super',
                        'pink: color,cauc,young',
                        'porcelain: color,texture,cauc',
                        'rosy: color,texture,cauc,young',
                        'silken: feel,texture',
                        'soft: feel,texture',
                        'smooth: feel,texture',
                        'sun-browned: color',
                        'sun-kissed: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['eyes: std,default,plur'])
               
          self.AdjList(['alluring: attractive',
                        'beautiful: attractive',
                        'bewitching: attractive',
                        'bright: attractive,young,cauc',
                        'blue x4: color,cauc',
                        'brown x3: color',
                        'captivating: attractive',
                        'clear: attractive,desc',
                        'dazzling: attractive,shiny',
                        'earnest: emotion',
                        'electric: attractive',
                        'electrifying: attractive',
                        'enchanting: attractive',
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
                        'wide: size,large'])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("bewitching")
          
class Hips(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['hips: std,default,plur'])
               
          self.AdjList(['curvy: width,wide,shape,desc',
                        'curvaceous: wide,width',
                        'bare: nude',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['braids: style,plur',
                         'hair x4: std,default,sing',
                         'fro: poc,sing'
                         'locks x2: plur',
                         'pig-tails: style,young,plur',
                         ])
               
          self.AdjList(['auburn: color,cauc',
                        'black x2:color',
                        'blonde x4: color,cauc',
                        'brunette x3: color,cauc',
                        'curly: shape,style',
                        'braided: style',
                        'dark x2: color',
                        'dyed-blue: color,fake',
                        'dyed-green: color,fake',
                        'dyed-pink: color,fake',
                        'dyed-purple: color,fake',
                        'fashionable: style',
                        'flaming-red: color,cauc',
                        'flowing: poetic'
                        'glossy: feel',
                        'golden: color,cauc',
                        'kinky black-girl: color,poc',
                        'long: length',
                        'luxuriant: feel',
                        'pixie cut: style',
                        'platinum blonde x2: color,cauc',
                        'punk blue: color,fake,style',
                        'red: color,cauc',
                        'sandy: color,cauc',
                        'silken: feel',
                        'short: length',
                        'straight: shape,style',
                        'vibrant: poetic',
                        'wavy: shape,style'])
          
          self.DefaultNoun("hair")
          self.DefaultAdj("flowing")
          
class Legs(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
                        'tall: length,long',
                        'tan: color',
                        'tanned: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['thighs: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'bronzed: color,tan',
                        'chubby: curvy,chubby',
                        'comely: attractive, poetic',
                        'delectable: super,taste',
                        'full: curvy,chubby,large',
                        'girlish: slender,young',
                        'heavy: chubby,large',
                        'inviting: horny',
                        'luscious: super',
                        'nubile: young',
                        'pale: color,cauc',
                        'plump: curvy,chubby'
                        'powerful: fit,strong',
                        'porcelain: color,cauc',
                        'ripe: attractive',
                        'rounded: shape',
                        'sensual: attractive',
                        'sexy: attractive',
                        'shapely: shape,attractive',
                        'silken: feel',
                        'smooth: feel,hairless',
                        'soft: feel',
                        'tanned: color,tan',
                        'tender: feel',
                        'thick x2: large,chubby',
                        'un-sullied: young, virginal',
                        'wide: chubby,large',
                        'womanly: curvy',
                        'youthful: young'])
          
          self.DefaultNoun("thighs")
          
class Nipples(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['nipples x4: std,default,plur',
                         'nips: silly,plur',
                         'teats: silly,plur',
               ])
               
          self.AdjList(['aching: horny',
                        'bare: nude',
                        'bared: nude',
                        'black: color, poc',
                        'blossoming: young',
                        'brown: color,',
                        'budding: cute',
                        'chocolate: color',
                        'dainty: size,small,cute',
                        'dark: color,',
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
                        'pink: color,cauc',
                        'plump: size,large,feel',
                        'pokey: arousal',
                        'prominent: poetic',
                        'puffy: feel,',
                        'ripe: attractive',
                        'rose-colored: color,cauc',
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
    def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None, bCupSize = False):
        super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials = bCupSize, NotList = NotList, TagLists = TagLists)

        self._bCupSize = bCupSize
          
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
               
        self.AdjList(['black: color,poc',
                      'big: size,bigtits',
                      'bite-sized: size,smalltits',
                      'bouncy: movement',
                      'bountiful: bigtits',
                      'bronzed: color',
                      'brown: color,poc',
                      'budding: smalltits,young',
                      'buxom: bigtits',
                      'chocolate: color,poc,taste',
                      'college girl: age,young',
                      'creamy: color,cauc,taste',
                      'dark: color,poc',
                      'delicious: super,taste',
                      'enchanting: super,attractive',
                      'fair: color,cauc',
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
                      'pale: color,cauc,young',
                      'pendulous: bigtits,shape,older',
                      'perky: shape,young',
                      'pert: shape,',
                      'petite: size,smalltits,',
                      'plentiful: bigtits,super',
                      'plump: bigtits,feel,shape,',
                      'proud: bigtits,super,',
                      'quivering: movement,',
                      'ripe: feel,shape,young',
                      'rosy: color,cauc,young',
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

    #def CupBuilder(self, NotList = None):
    #    if NotList == None:
    #        NotList = []

    #    CupList = ["A-cup: small,cupsize",
    #               "B-cup: small,cupsize",
    #               "D-cup: large,cupsize",
    #               "double-D cup: large,cupsize",
    #               "triple-D cup: large,cupsize",
    #              ]

    #    return WordList(CupList).GetWord(NotList = NotList)

    def AllowCupSize(self, bCupSize = True):
        self._bCupSize = bCupSize

        self.AdjList(self.GetAdjList())

    def ShortDescription(self, ExtraAdjList = None, NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)

        #if bCupSize:
        #    if ExtraAdjList is None:
        #        ExtraAdjList = []

        #    ExtraAdjList.append(self.CupBuilder(NotList = NotList))
            #print("  Selected cup size is " + ExtraAdjList[0])

        return super().ShortDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
          
    def MediumDescription(self, ExtraAdjList = None, NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)

        #if bCupSize:
        #    if ExtraAdjList is None:
        #        ExtraAdjList = []

        #    ExtraAdjList.append(self.CupBuilder(NotList = NotList))
        #    #print("  Selected cup size is " + ExtraAdjList[0])
               
        return super().MediumDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
    def FloweryDescription(self, ExtraAdjList = None, NotList = None, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)

        #if bCupSize:
        #    if ExtraAdjList is None:
        #        ExtraAdjList = []

        #    ExtraAdjList.append(self.CupBuilder(NotList = NotList))
        #    #print("  Selected cup size is " + ExtraAdjList[0])
          
        return super().FloweryDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
    def RandomDescription(self, ExtraAdjList = None, NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bCupSize = None, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
        self._bCupSize = bCupSize

        return super().RandomDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
     
          
class Clitoris(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
     InnerVag = []
     InnerLabia = []
     OuterLabia = []
     Clitoris = []
     
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
                        'cherry: young,virginal',
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
                        'peach-fuzzed: hairy,young',
                        'puffy: shape,arousal',
                        'shameless: horny',
                        'shaved: shaved',
                        'silken: feel,shaved,texture',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
                        'gaping: large,gape',
                        'knotted: small,tight,desc',
                        'lewd: horny',
                        'little x4: small,cute,',
                        'loose: gape',
                        'nasty: taboo',
                        'naughty: horny',
                        'pert: cute,young',
                        'puckered: action',
                        'rusty: desc,color',
                        'shy: horny,taboo',
                        'smooth: feel,desc',
                        'snug x2: small,tight,cute,'
                        'taboo: taboo',
                        'tender: feel,desc,cute',
                        'tight x4: small,tight',
                        'wanton: horny',
                        'well-used: gape,old',
                        'willing: horny',
                        'winking: small,tight,action',
                       ])
          
          self.DefaultNoun("anus")
          
class ButtocksFemale(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
     
          self.NounList(['buns: std,plur',
                          'butt-cheeks: std,plur',
                          'buttocks: std,clinical,plur',
                          'cheeks:std,plur',
                         ])
               
          self.AdjList(['ample: large,curvy',
                        'big: size,large',
                        'black: color,poc',
                        'bronzed: color',
                        'brown: color,poc',
                        'bubble-butt: shape',
                        'bubble-shaped: shape',
                        'chubby: shape,plussize,curvy',
                        'coffee-colored: color,poc',
                        'creamy: color,cauc',
                        'curvaceous: shape,curvy',
                        'curvy: curvy,shape',
                        'cute: cute',
                        'dark: color,poc',
                        'fat: large,plussize',
                        'honeyed: taste',
                        'jiggling: movement',
                        'juicy: wet,taste,horny',
                        'lickable: taste,horny',
                        'luscious: super,large',
                        'muscular: strong',
                        'pale: color,cauc',
                        'petite: size,small',
                        'pink: color,cauc',
                        'plump: large,plussize,curvy',
                        'rosy: color,cauc',
                        'rotund: large,plussize',
                        'round: shape',
                        'rounded: shape',
                        'shapely x3: shape,attractive',
                        'smooth: hairless,feel,texture',
                        'squeezable x2: horny',
                        'succulent: super,attractive,horny',
                        'sun-browned: color',
                        'sun-kissed: color',
                        'supple: feel,texture,young',
                        'sweet: attractive',
                        'tender: feel',
                        'tanned: color',
                        'thick x3: size,large,shape,curvy',
                        'tight: size,small',
                        'trim: size,small',
                        'voluptuous: shape,curvy,attractive',
                        'well-rounded: shape',
                        'well-tanned: color',
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssFemale(FemaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['anatomy: std,sing',
                         'body x4: std,default,sing',
                         'curves: plur',
                         'figure: std,sing',
                         'form: std,sing',
                         'physique: std,sing'])
               
          self.AdjList(['beautiful: attractive,super',
                        'black: color,poc',
                        'breathtaking: super',
                        'bronzed: color',
                        'brown: color,poc',
                        'busty: bigtits',
                        'buxom: bigtits',
                        'coffee-colored: color,poc',
                        'curvaceous: shape,curvy,bigtits,attractive',
                        'curvy: shape,curvy',
                        'feminine: curvy',
                        'gorgeous: super,attractive',
                        'leggy: longlegs',
                        'little: size,small',
                        'lush: super',
                        'luxuriant: super',
                        'mocha: color,poc',
                        'model-esque: attractive',
                        'nubile: young,virginal',
                        'pale: color,cauc',
                        'pink: color,cauc,young',
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
                        'tanned: color',
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
          
     
     def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
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
               sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          else:
               sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
               if bAddArticles:
                    sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
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
               sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc
          
     def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None, NotList = None):
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
               sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = NotList)
          else:
               sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = NotList)
          
          if bAddArticles:
               sPartDesc = AddArticles(sPartDesc)
          
          return sPartDesc
     
     def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bExplicit = False, bAllowLongDesc = True, sPossessive = None, NotList = None):
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
               sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               NotList += re.split(r',|\w|', sBodyDesc)
               if iLoops == iNum - 2:  
                    sBodyDesc += sDivideChar + " and "
               elif iLoops < iNum - 2:
                    sBodyDesc += sDivideChar + " "
               iLoops = iLoops + 1
               
          return sBodyDesc

     def GetRandomIntimateParts(self, iNum, bIncludeInners = False, bAllowShortDesc = False):
          Parts = []
          AllParts = []
          
          if bIncludeInners:
               AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.OuterLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.InnerLabia.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.InnerVag.RandomDescription(bAllowShortDesc = bAllowShortDesc))
          else:
               AllParts.append(self.Hips.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Breasts.Nipples.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Thighs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               AllParts.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               
          for x in sorted(sample(range(0, len(AllParts)), iNum)):
               Parts.append(AllParts[x])
               
          return Parts
                    
     def GetHoles(self, bIncludeMouth = True):
          Holes = []
          
          if bIncludeMouth:
               Holes = [3]
          
               Holes[0] = self.Mouth.RandomDescription()
               Holes[1] = self.Vagina.RandomDescription()
               Holes[2] = self.Ass.Anus.RandomDescription()
          else:
               Holes = [2]
               
               Holes[0] = self.Vagina.RandomDescription()
               Holes[1] = self.Ass.Anus.RandomDescription()
          
          return Holes
          
     def GetRandomHole(self, bIncludeMouth = True, bAllowShortDesc = True, bAllowLongDesc = True):
          sHole = ""
          Holes = []
          if bIncludeMouth:          
               Holes.append(self.Mouth.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
          else:
               Holes.append(self.Vagina.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
               Holes.append(self.Ass.Anus.RandomDescription(bAllowShortDesc = bAllowShortDesc, bAllowLongDesc = bAllowLongDesc))
          
          iRand = randint(0, len(Holes) - 1)
          sHole = Holes[iRand]
          
          return sHole
          
class PenisHead(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['cock-head: silly,slang,sing',
                         'dick-tip: silly,crude,slang,sing',
                         'head x3: std,default,sing',
                         'helmet: desc,sing',
                         'knob x2: crude,silly,desc,slang,sing',
                         'mushroom: desc,sing',
                         'tip x3: std, default,sing',
                        ])
               
          self.AdjList(['broad',
                        'brown',
                        'bulging',
                        'dripping',
                        'engorged',
                        'fat',
                        'glistening',
                        'pulsating',
                        'purple',
                        'red',
                        'smooth',
                        'swollen',
                        'thick',
                        'throbbing',
                        'tumescent'])
          
          self.DefaultNoun("head")
          self.IsPlural = False
          
class Testicles(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
          
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None, bAllowBAP = True):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
                        'black: color,poc',
                        'beautiful: super',
                        'beefy: bigdick,taste',
                        'bent: shape',
                        'big x4: size,bigdick',
                        'broad x2: width,wide',
                        'bulbous: shape',
                        'bulging x2: hard,bigdick,shape'
                        'burning: feel,warm',
                        'carefully man-scaped: style,trimmed',
                        'circumcized: cut',
                        'crooked: shape',
                        'curved: shape',
                        'delicious: taste,horny,super',
                        'dripping: wet',
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
                        'gorgeous: super,attractive',
                        'greasy x4: feel,wet',
                        'hairy: hairy',
                        'hairless: hairless',
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
                        'pierced: style',
                        'pink: color,cauc',
                        'powerful: horny,super',
                        'pretty: attractive',
                        'proud: poetic',
                        'pulsating: feel,throb',
                        'purple: color',
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
                        'uncircumcized: style, cut',
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
     
     def GetRandomPenisPart(self, NotList = None, bAllowShortDesc = False):
          if NotList == None:
               NotList = []
               
          iRand = randint(1,3)
          
          if iRand == 1:
               return self.Head.RandomDescription(NotList = NotList, bAllowShortDesc = bAllowShortDesc)
          elif iRand == 2: 
               return self.Testicles.RandomDescription(NotList = NotList, bAllowShortDesc = bAllowShortDesc)
          else:
               return self.RandomDescription(NotList = NotList, bAllowShortDesc = bAllowShortDesc)
               
     def GenerateLength(self):
          sLength = ""
          
          sLength = str(randint(6, 13))
          if CoinFlip():
               sLength += " 1/2"
          sLength += "-inch"
          
          return sLength
               
     def ShortDescription(self, ExtraAdjList = None, NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if bAddLen:
               if ExtraAdjList is None:
                   ExtraAdjList = []
                   
               ExtraAdjList.append(self.GenerateLength())
          
          return super().ShortDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList)
          
     def MediumDescription(self, ExtraAdjList = None, NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if bAddLen:
               if ExtraAdjList is None:
                   ExtraAdjList = []
                   
               ExtraAdjList.append(self.GenerateLength())
               
          return super().MediumDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
     def FloweryDescription(self, ExtraAdjList = None, NotList = None, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if bAddLen:
               if ExtraAdjList is None:
                   ExtraAdjList = []
                   
               ExtraAdjList.append(self.GenerateLength())
          
          return super().FloweryDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
          
     def RandomDescription(self, ExtraAdjList = None, NotList = None, bAllowShortDesc = True, bAllowLongDesc = True, bAddLen = False, NounReqTagList = None, NounExclTagList = None, AdjReqTagList = None, AdjExclTagList = None):
          if bAddLen:
               if ExtraAdjList is None:
                   ExtraAdjList = []
                   
               ExtraAdjList.append(self.GenerateLength())
          
          return super().RandomDescription(ExtraAdjList = ExtraAdjList, NotList = NotList, NounReqTagList = NounReqTagList, NounExclTagList = NounExclTagList, AdjReqTagList = AdjReqTagList, AdjExclTagList = AdjExclTagList) 
     
class Semen(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)

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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['buns: std,cute,desc,plur',
                         'butt cheeks: std,slang,plur',
                         'buttocks: std,default,clinical,plur',
                         'glutes: std,strong,plur',
                         ])
               
          self.AdjList(['beefy: large',
                        'broad: size,wide',
                        'bronzed: color',
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
                        'tan: color',
                        'tight x2: size,small,shape',
                        'trim: size,narrow,shape',
                        'virile: attractive',
                        'well-defined: shape'
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssMale(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksMale()
          
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
                        'bronzed: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['skin x4: default,std,sing',
                         'flesh x2: std,sing',
                         'hide: std,sing',
                        ])
               
          self.AdjList(['bare: nude',
                        'bronzed: color',
                        'brown: color,poc',
                        'coffee-colored: color,poc',
                        'dark: color,poc',
                        'ebony: color,poc',
                        'exposed: bare',
                        'freckled: color,cauc',
                        'glistening: shiny,wet,texture',
                        'hairy: hairy',
                        'leathery: feel,texture,older',
                        'naked: nude',
                        'pale: color,cauc',
                        'rough: texture',
                        'rugged: texture',
                        'smooth: texture',
                        'sun-browned: color',
                        'supple: feel,young,texture',
                        'tanned: color',
                        'tough: texture',
                        'warm: feel',
                        'weathered: texture,older',
                        'youthful: young'])
          
          self.DefaultNoun("skin")
          self.DefaultAdj("rugged")
          
class ShouldersMale(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['shoulders'])
               
          self.AdjList(['bare: nude',
                        'brawny: strong,large',
                        'broad: size,wide',
                        'bronzed: color',
                        'brown: color,poc',
                        'coffee-colored: color,poc',
                        'dark: color,poc',
                        'ebony: color,poc',
                        'freckled: color,cauc',
                        'mighty: strong',
                        'muscular: shape,strong',
                        'naked: nude',
                        'powerful: super',
                        'rugged: shape',
                        'square: shape,wide',
                        'strong: strong',
                        'sturdy: strong',
                        'sun-browned: color',
                        'tanned: color',
                        'well-built: shape',
                        'wide: size,wide'])

          self.DefaultNoun("shoulders")
          self.DefaultAdj("broad")
          
class MusclesMale(MaleBodyParts):
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['muscles: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: large,strong',
                        'broad: size,large,wide',
                        'bronzed: color',
                        'bulging: shape',
                        'burly: strong',
                        'chiseled: shape',
                        'dark: color',
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
                        'tanned: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['chest x4: std,default,sing',
                         'pectorals: std,plur'])
               
          self.AdjList(['bare: nude',
                        'brawny: muscular',
                        'broad: size,large,wide',
                        'bronzed: color',
                        'brown: color,poc',
                        'burly: muscular,size,large,shape',
                        'coffee-colored: color,poc',
                        'compact: size,small',
                        'dark: color,poc',
                        'dark-thatched: hairy',
                        'ebony: color,poc',
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
                        'sun-browned: color',
                        'tanned: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['arms x4: std,default,plur',
                         'limbs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong',
                        'bronzed: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
          self.NounList(['legs x3: std,default,plur',
                         'calves: std,plur',
                         'limbs: std,plur',
                         'thighs: std,plur'])
               
          self.AdjList(['athletic: shape',
                        'bare: nude',
                        'brawny: strong,large,shape',
                        'bronzed: color',
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
     def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
          super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
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
    def __init__(self, iNumAdjs = 4, ExtraAdjList = None, bVaryAdjTags = None, bEnableSpecials = False, NotList = None, TagLists = None):
        super().__init__(iNumAdjs, ExtraAdjList, bVaryAdjTags, bEnableSpecials, NotList, TagLists)
          
        self.NounList(['body x4: std,default,sing',
                       'build: std,sing',
                       'bulk: std,large,heavy,sing',
                       'form: std,sing',
                       'physique x2: std,sing',
                      ])
               
        self.AdjList(['beefy: large',
                      'brawny: strong,shape',
                      'broad: size,wide',
                      'bronzed: color',
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
     
    def GetClothedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
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
            sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomClothedBodyParts(self, iNum = 3, sDivideChar = ',', bAllowLongDesc = True, sPossessive = None):
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
            sBodyDesc += self.GetClothedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1
               
        return sBodyDesc
          
    def GetNakedBodyPartDesc(self, part, bAllowLongDesc, sPossessive = None):
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
            sPartDesc = sPossessive + " " + part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
        else:
            sPartDesc = part.RandomDescription(bAllowShortDesc = False, bAllowLongDesc = bAllowLongDesc, NotList = PartNotList)
          
            if bAddArticles:
                sPartDesc = AddArticles(sPartDesc)
          
        return sPartDesc
     
    def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bPenis = True, bAss = True, bExplicit = False, bAllowLongDesc = True, sPossessive = None):
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
            sBodyDesc += self.GetNakedBodyPartDesc(SelectedParts[iLoops], bAllowLongDesc, sPossessive = sPossessive)
               
            if iLoops == iNum - 2:  
                sBodyDesc += sDivideChar + " and "
            elif iLoops < iNum - 2:
                sBodyDesc += sDivideChar + " "
            iLoops = iLoops + 1

        return sBodyDesc
          
 
    def GetRandomIntimateParts(self, iNum, bIncludeInners, bAllowShortDesc = False):
        Parts = []
        AllParts = []
          
        if bIncludeInners:
            AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.Head.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.Testicles.RandomDescription(bAllowShortDesc = bAllowShortDesc))
        else:
            AllParts.append(self.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Shoulders.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Chest.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Legs.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Ass.RandomDescription(bAllowShortDesc = bAllowShortDesc))
            AllParts.append(self.Penis.RandomDescription(bAllowShortDesc = bAllowShortDesc))
               
        for x in sorted(sample(range(0, len(AllParts)), iNum)):
            Parts.append(AllParts[x])
               
        return Parts


#for i in range(6):
#    TestMale = Man()

for i in range(6):
    TestFem = Woman()