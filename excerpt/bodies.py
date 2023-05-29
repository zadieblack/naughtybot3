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
    IsTan: bool = False
    PubeStyle: str = ""

#GenPhysTraits = namedtuple("GenPhysTraits",
#                           "FirstName LastName Gender Race PubeStyle",
#                           defaults = ["","","",None,""]
#                          )
class Body():
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

        if NewGenTraits.Race and isinstance(NewGenTraits.Race,Race):
            self.Race = NewGenTraits.Race
        else:
            self.Race = choice([RaceCauc,RaceCauc,RaceGinger,RacePOC,RacePOC,RaceAsian,RaceLatin]) # Add RaceAsian

        self.RaceName = self.Race.Name.lower()

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
        #print("Selected " + self.Gender + " who is " + self.RaceName)
        RaceTags = ["asian","cauc","poc","latin","redhead"]
        if self.RaceName == "asian":
            RaceTags.remove("asian")
        elif self.RaceName == "caucasian":
            RaceTags.remove("cauc")
        elif self.RaceName == "latin":
            RaceTags.remove("latin")
        elif self.RaceName == "poc":
            RaceTags.remove("poc")
        elif self.RaceName == "redhead":
            RaceTags.remove("redhead")
        else:
            RaceTags = []

        #print("Excluding RaceTags: " + str(RaceTags))
        LTagLists.adj_excl += RaceTags

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

        if self.Race in ["asian","caucasian"] and not self.HairColor in ["red"] and self.IsTan:
            self.SkinColor = choice(TanColors)
        else:
            self.SkinColor = choice(self.Race.SkinColor)
        self.NipColor = choice(self.Race.NipColor)

@dataclass
class MalePhysTraits:
    AgeCat: str = ""
    Age: int = 0
    HeightType: str = ""
    BodyType: str = ""
    HairStyle: str = ""
    HasFacialHair: bool = False
    FacialHairStyle: str = ""
    DickInches: int = 0
    IsCircumcised: bool = False 

class Man(Body):
    def __init__(self, NewGenTraits = None, NewMaleTraits = None):
        super().__init__("male", NewGenTraits = NewGenTraits)
        
        self.Noun = ""
        self.Desc = ""
        self.DescWords = ""
        self.AgeCat = ""
        self.Age = 0
        self.HeightType = ""
        self.BodySize = ""
        self.IsFit = False
        self.HairStyle = ""
        self.HasFacialHair = False
        self.FacialHairStyle = ""
        self.DickInches = 0
        self.IsCircumcised = False

        self.Man = None
        self.Noun = ""
        self.Desc = ""
        self.DescWords = ""

        EyeParams = NPParams(sColor = self.EyeColor)
        HairParams = NPParams(sColor = self.HairColor)
        NipParams = NPParams(sColor = self.NipColor)
        SkinParams = NPParams(sColor = self.SkinColor)

        LTagLists = self._TagLists

        bRandomize = False

        if NewMaleTraits is None or not isinstance(NewMaleTraits, MalePhysTraits):
            NewMaleTraits = MalePhysTraits()
            bRandomize = True

        # Handle age 
        if NewMaleTraits.AgeCat:
            self.AgeCat = NewMaleTraits.AgeCat
        else:
            self.AgeCat = choice(["teen","college","twenties","thirties","middleaged","older"])
                
        if self.AgeCat in ["teen","college","twenties"]:
            LTagLists.adj_excl.append("older")
        else:
            LTagLists.adj_excl.append("young")

        if NewMaleTraits.Age > 0 and not bRandomize:
            self.Age = NewMaleTraits.Age
        else:
            # ["teen","college","twenties","thirties","middleaged","older"]
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
            self.HeightType = choice(["short","medium","medium","tall","tall","tall"])

        # Handle body type
        if NewMaleTraits.BodyType:
            self.BodyType = NewMaleTraits.BodyType
        else:
            self.BodyType = choice(["slender","medium","large",])

        if bRandomize:
            self.IsFit = choice([True,True,False])

        if NewMaleTraits.HairStyle:
            self.HairStyle = NewMaleTraits.HairStyle
        else:
            if self.AgeCat in ["twenties","thirties",]:
                self.HairStyle = choice(["shaved","bald","normal","normal"])
            elif self.AgeCat in ["middleaged","older"]:
                self.HairStyle = choice(["bald","bald","normal"])
            else:
                self.HairStyle = choice(["shaved","normal","normal"])

        self.HasFacialHair = NewMaleTraits.HasFacialHair 

        if NewMaleTraits.FacialHairStyle:
            self.FacialHairStyle = NewMaleTraits.FacialHairStyle
        else:
            if self.AgeCat in ["teen"]:
                self.FacialHairStyle = choice(["goatee","moustache","shaved","shaved","shaved","shaved","shaved","stubble"])
            else:
                self.FacialHairStyle = choice(["beard","beard","goatee","moustache","shaved","shaved","shaved","stubble"])

        # Handle dick size
        if NewMaleTraits.DickInches > 0 and not bRandomize:
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

        if bRandomize:
            self.IsCircumcised = CoinFlip()
        else:
            self.IsCircumcised = NewMaleTraits.IsCircumcised

        # ===============
        # Setup bodyparts
        # ===============

        # Arms
        self.Arms = ArmsMale(TagLists = LTagLists)

        # Ass
        ButtocksParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Anus = AnusFemale(TagLists = LTagLists)
        self.Buttocks = ButtocksMale(Params = ButtocksParams,TagLists = LTagLists)
        self.Ass = AssMale(Params = SkinParams, TagLists = LTagLists)
        self.Ass.Anus = self.Anus
        self.Ass.Buttocks = self.Buttocks

        # Chest 
        ChestParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Chest = ChestMale(Params = ChestParams, TagLists = LTagLists)

        # Eyes
        self.Eyes = EyesMale(Params = EyeParams, TagLists = LTagLists)

        # Facial Hair

        self.FacialHair = FacialHair(TagLists = LTagLists)

        # Hair

        self.Hair = HairMale(Params = HairParams, TagLists = LTagLists)

        # Jaw

        self.Jaw = JawMale(TagLists = LTagLists)

        # Legs
        LegsParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Legs = LegsMale(Params = LegsParams, TagLists = LTagLists)

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
        ShoulderParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Shoulders = ShouldersMale(Params = ShoulderParams, TagLists = LTagLists)

        # Skin
        VarSkinParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        self.Skin = SkinMale(Params = VarSkinParams, TagLists = LTagLists)

        # Body
        BodyParams = NPParams(sColor = GetSkinonym(self.SkinColor))

        if self.HeightType == "short":
            BodyTagLists = TagLists(adj_excl = ["tall"] + LTagLists.adj_excl)
        elif self.HeightType == "tall":
            BodyTagLists = TagLists(adj_excl = ["short"] + LTagLists.adj_excl)
        else:
            BodyTagLists = TagLists(adj_excl = ["short","tall"] + LTagLists.adj_excl)

        self.Body = BodyMale(Params = BodyParams, TagLists = BodyTagLists)
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

        self.BuildDesc(LTagLists)

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

        return

    def BuildDesc(self, TLParams):
        # ["teen","college","twenties","thirties","middleaged","older"]

        AdjList = ['confident: attitude',
                   'gruff: attitude,thirties,middleaged,older',
                   'handsome x4: super',
                   'hairy: hairy',
                   'heavily-tattoed: style',
                   'sexy x2: super',
                   'striking: super',
                  ]

        ColorList = []

        NounList = ['guy x2: sing',
                    'man x4: adult,sing',
                   ]

        if self.RaceName == "asian":
            AdjList += ['Asian x20: race,asian',]
        elif self.RaceName == "caucasian":
            if self.HairStyle in ["normal"]:
                if self.HairColor in ["blonde"]:
                    AdjList += ['blonde x8: blonde,haircolor,cauc','fair: blonde,haircolor,cauc',]
                elif self.HairColor in ["brown"]:
                    AdjList += ['brunette x6: haircolor,brunette,cauc','brown-haired x6: haircolor,brunette,cauc']
                elif self.HairColor in ["gray"]:
                    AdjList += ['gray-haired: haircolor,grayhair,older,age','silver-haired: haircolor,grayhair,older,age']
                else:
                    AdjList += ['dark-haired: haircolor,dark,brunette','raven-haired x3: haircolor,darkhair',]
            else:
                    AdjList += ["bald-shaven: hair,shaved,bald,",]
        elif self.RaceName == "latin":
            AdjList += ['latino x20: race,latin,sing',]
            NounList += ['latino x3: race,latin,sing',]
        elif self.RaceName == "poc":
            AdjList += ['black x20: color,race,poc','ebony x6: color,race,poc',]
        elif self.RaceName == "redhead":
            AdjList += ['redheaded x20: haircolor,race,redhead,redhair',]

        
        if self.AgeCat not in ["middleaged","older"]:
            AdjList += ['young x12: age,young',]
            NounList += ['boy x3: age,young,sing',]
        else:
            AdjList += ['fatherly: age,older',
                        'grand-fatherly: age,older',
                        'mature x8: age,older',
                        'middle-aged x8: age,middleage',]
        if self.AgeCat not in ["twenties","thirties","middleaged","older"]:
            NounList += ['young man x3: adult,age,young,sing',]
        if self.AgeCat in ["teen"]:
            AdjList += ['teen x8: age,teen,young',
                        'teenage x6: age,teen,young',]
            NounList += ['teen x3: age,young,teen,sing',]
            
        if self.AgeCat in ["college"]:
            NounList += ['college boy x3: age,young,college,sing',
                         'college guy x4: age,young,college,sing']

        if self.RaceName in ["asian","caucasian","latin"]:
            if self.IsTan:
                AdjList += TanColors
        if self.RaceName in ["caucasian","redhead"]:
            if not self.IsTan:
                AdjList += ['fair-skinned: color','freckled: color','pale: color',]

        if self.HairStyle in ["shaved"]:
            AdjList += ["bald-shaven x5: hair,shaved","smooth-shaven x5: hair,shaved"]
        elif self.HairStyle in ["bald"]:
            AdjList += ["bald x10: hairless,bald"]
        elif self.HairColor == "gray":
            AdjList += ['gray-haired: haircolor,grayhair,older,age','silver-haired: haircolor,grayhair,older,age']

        # Old stuff ===========================================
        #if self.AgeCat == "teen":
        #    if self.RaceName == "poc":
        #        NounList += ["black teen boy: poc,young,teen,sing","black teenage boy: poc,young,teen,sing","young black man: poc,young,sing","young black guy: poc,young,sing","black boy: poc,young,teen,sing"]
        #    elif self.RaceName == "asian":
        #        NounList += ["Asian teen boy: asian,young,teen,sing","Asian teenage boy: asian,young,teen,sing","young Asian man: asian,young,sing","young Asian guy: asian,young,sing","Asian boy: asian,young,teen,sing"]
        #    elif self.RaceName == "latin":
        #        NounList += ["latino teen boy: latino,young,teen,sing","latino teenage boy: latino,young,teen,sing","young latino man: latino,young,sing","young latino guy: latino,young,sing","latino boy: latino,young,teen,sing"]
        #    else:
        #        NounList += ["teen boy: young,teen,sing","teenage boy: young,teen,sing","young man x3: young,sing",]
        #        if self.HairStyle in ["normal"]:
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde teen boy: hair,cauc,young,teen,sing","blonde teenage boy: hair,cauc,young,teen,sing","young blonde man: hair,cauc,young,sing","blonde boy: hair,cauc,young,sing"]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redhead teen boy: hair,cauc,young,teen,sing","redhead teenage boy: hair,cauc,young,teen,sing","young redhead man: hair,cauc,young,sing","redhead boy: hair,cauc,young,sing"]
        #            elif self.HairColor == "brown":
        #                NounList += ["brown-haired teen boy: hair,cauc,young,teen,sing","brown-haired teenage boy: hair,cauc,young,teen,sing","young brown-haired man: hair,cauc,young,sing","brown-haired boy: hair,cauc,young,sing",]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired teen boy: hair,young,teen,sing","dark-haired boy: hair,young,teen,sing","dark-haired teen: hair,young,teen,sing","raven-haired boy: hair,young,sing","raven-haired teen boy: hair,young,teen,sing","dark-haired young man: hair,young,sing","raven-haired young man: hair,young,sing"]
        #        else:
        #            NounList += ["skin-headed teen boy: hair,shaved,young,teen,sing","skin-headed teenage boy: hair,shaved,young,teen,sing","skin-headed young man x3: hair,shaved,young,sing",
        #                         "bald-shaven teen boy: hair,shaved,young,teen,sing","bald-shaven teenage boy: hair,shaved,young,teen,sing","bald-shaven young man x3: hair,shaved,young,sing",]
        
        #elif self.AgeCat == "college":
        #    if self.RaceName == "poc":
        #        NounList += ["black college boy: poc,young,college,sing","black college guy: poc,young,college,sing","ebony college boy: poc,young,college,sing","young black man: poc,young,sing","young ebony man: poc,young,sing","young ebony guy: poc,young,sing","young black guy: poc,young,sing","young black college boy: poc,young,college,sing","young ebony college boy: poc,young,college,sing","black man x4: poc,young,college,sing","ebony man: poc,young,college,sing"]
        #    elif self.RaceName == "asian":
        #        NounList += ["Asian college boy: asian,young,college,sing","Asian college guy: asian,young,college,sing","young Asian man: asian,young,sing","young Asian guy: asian,young,sing","young Asian college boy: asian,young,college,sing","Asian man x4: asian,young,college,sing",]
        #    elif self.RaceName == "latin":
        #        NounList += ["latino college boy: latino,young,college,sing","latino college guy: latino,young,college,sing","young latino man: latino,young,sing","young latino guy: latino,young,sing","young latino college boy: latino,young,college,sing","latino man x4: latino,young,college,sing",]
        #    else:
        #        NounList += ["college boy: young,college,sing","college guy: young,college,sing","young guy: young,sing","young man: young,sing",]
        #        if self.HairStyle in ["normal"]:
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde college boy: hair,cauc,young,college,sing","blonde college guy: hair,cauc,young,college,sing","young blonde college boy: hair,cauc,young,college,sing","blonde young man: hair,cauc,young,sing","blonde boy: hair,cauc,young,sing","blonde guy: hair,cauc,sing","blonde young man: hair,young,cauc,sing"]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redheaded college boy: hair,cauc,young,college,sing","redheaded college guy: hair,cauc,young,college,sing","young redheaded college boy: hair,cauc,young,college,sing","redheaded young man: hair,cauc,young,sing","redheaded young guy: hair,cauc,young,sing","redheaded young man: hair,cauc,young,sing"]
        #            elif self.HairColor == "brown":
        #                NounList += ["brown-haired college boy: hair,cauc,young,college,sing","brunette college guy: hair,cauc,young,college,sing","young brown-haired college boy: hair,cauc,young,college,sing","brown-haired young man: hair,cauc,young,sing","brown-haired boy: hair,cauc,young,sing","brown-haired guy: hair,cauc,young,sing","brunette guy: hair,cauc,young,sing","brown-haired young man: hair,cauc,young,sing",]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired college boy: hair,young,college,sing","dark-haired college guy: hair,young,college,sing","dark-haired young man: hair,young,sing"]
        #        else:
        #            NounList += ["skin-headed college boy: hair,shaved,young,college,sing","skin-headed college guy: hair,shaved,young,college,sing","skin-headed young man x3: hair,shaved,young,sing",
        #                         "bald-shaven college boy: hair,shaved,young,college,sing","bald-shaven college guy: hair,shaved,young,college,sing","bald-shaven young man x3: hair,shaved,young,sing",]

        #elif self.AgeCat == "twenties":
        #    if self.RaceName == "poc":
        #        NounList += ["young black man: poc,young,twenties,sing","young ebony man: poc,young,sing","black man x3: poc,sing","ebony man: poc,sing","young black guy: poc,young,sing","black guy: poc,sing"]
        #    elif self.RaceName == "asian":
        #        NounList += ["young Asian man: asian,young,twenties,sing","Asian man x3: asian,sing","young Asian guy: asian,young,sing","Asian guy: asian,sing"]
        #    elif self.RaceName == "latin":
        #        NounList += ["young latino man: latino,young,twenties,sing","latino man x3: latino,sing","young latino guy: latino,young,sing","latino guy: latino,sing"]
        #    else:
        #        NounList += ["young guy: young,sing","young man: young,sing","man x3: sing"]
        #        if self.HairStyle in ["normal"]:
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde young man: hair,cauc,young,sing","blonde guy: hair,cauc,sing","blonde man x3: hair,cauc,sing"]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redheaded young man: hair,cauc,young,sing","redheaded guy: hair,cauc,sing","redheaded man x3: hair,cauc,sing",]
        #            elif self.HairColor == "brown":
        #                NounList += ["brunette young man: hair,cauc,young,sing","brunette guy: hair,cauc,sing","brunette man x3: hair,cauc,sing"]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired young man: hair,young,sing","dark-haired guy: hair,young,sing","dark-haired man x3: hair,young,sing","dark-haired young man: hair,young,sing"]
        #        elif self.HairStyle in ["shaved"]:
        #            NounList += ["skin-headed young man: hair,shaved,young,sing","skin-headed young guy: hair,shaved,young,sing","skin-headed man: hair,shaved,sing",
        #                         "bald-shaven young man: hair,shaved,young,sing","bald-shaven young guy: hair,shaved,young,sing","bald-shaven man x3: hair,shaved,sing",]
        #        elif self.HairStyle in ["bald"]:
        #            NounList += ["bald young man: hair,bald,young,sing","bald guy: hair,bald,sing","bald man x3: hair,bald,sing"]
        #elif self.AgeCat == "thirties":
        #    if self.RaceName == "poc":
        #        NounList += ["black man x3: poc,sing","ebony man: poc,sing","black guy: poc,sing"]
        #    elif self.RaceName == "asian":
        #        NounList += ["Asian man x3: asian,sing","Asian guy: asian,sing"]
        #    elif self.RaceName == "latin":
        #        NounList += ["latino man x3: latino,sing","latino guy: latino,sing"]
        #    else:
        #        NounList += ["man x3: sing"]
        #        if self.HairStyle in ["normal"]:
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde man x3: hair,cauc,sing","blonde guy: hair,cauc,sing",]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redheaded man x3: hair,cauc,sing","redheaded guy: hair,cauc,sing"]
        #            elif self.HairColor == "brown":
        #                NounList += ["brunette man: hair,cauc,sing","brown-haired man x3: hair,cauc,sing","brown-haired guy: hair,cauc,sing","brunette guy: hair,cauc,sing"]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired man x3: hair,sing","raven-haired man: hair,sing","dark-haired guy: hair,sing",]
        #        elif self.HairStyle in ["shaved"]:
        #            NounList += ["skin-headed man: hair,shaved,sing","skin-headed guy: hair,shaved,sing",
        #                         "bald-shaven man: hair,shaved,sing","bald-shaven guy: hair,shaved,sing",]
        #        elif self.HairStyle in ["bald"]:
        #            NounList += ["bald young man: hair,bald,young,sing","bald guy: hair,bald,sing","bald man x3: hair,bald,sing"]
        #elif self.AgeCat in ["middleaged"]:
        #    if self.RaceName == "poc":
        #        NounList += ["black man: poc,sing","ebony man: poc,sing","middle-aged black man: poc,middleaged,sing","middle-aged black guy: poc,middleaged,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald black man: hair,bald,poc,sing","bald middle-aged black man: hair,bald,poc,middleaged,sing","bald middle-aged black guy: hair,bald,poc,middleaged,sing",]
        #    elif self.RaceName == "asian":
        #        NounList += ["Asian man: asian,sing","middle-aged Asian man: asian,middleaged,sing","middle-aged Asian guy: asian,middleaged,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald Asian man: hair,bald,asian,sing","bald middle-aged Asian man: hair,bald,asian,middleaged,sing","bald middle-aged Asian guy: hair,bald,asian,middleaged,sing",]
        #    elif self.RaceName == "latin":
        #        NounList += ["latino man: latino,sing","middle-aged latino man: latino,middleaged,sing","middle-aged latino guy: latino,middleaged,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald latino man: hair,bald,latino,sing","bald middle-aged latino man: hair,bald,latino,middleaged,sing","bald middle-aged latino guy: hair,bald,latino,middleaged,sing",]
        #    else:
        #        if self.HairStyle in ["normal"]:
        #            NounList += ["man x2: sing","middle-aged man: middleaged, sing","guy: middleaged,guy,sing"]
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde man x2: hair,cauc,sing","middle-aged blonde man: hair,cauc,middleaged,sing","middle-aged blonde guy: hair,cauc,middleaged,sing","blonde guy: hair,cauc,middleaged,guy,sing",]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redheaded man x2: hair,cauc,sing","middle-aged redheaded man: hair,cauc,middleaged,sing","middle-aged redheaded guy: hair,cauc,middleaged,sing","redheaded guy: hair,cauc,middleaged,guy,sing",]
        #            elif self.HairColor == "brown":
        #                NounList += ["brunette man x2: hair,cauc,sing","middle-aged brown-haired man: hair,cauc,middleaged,sing","middle-aged brown-haired guy: hair,cauc,middleaged,sing","brunette guy: hair,cauc,sing",]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired man: hair,sing","raven-haired man: hair,guy,sing","middle-aged dark-haired man: hair,middleaged,sing","middle-aged dark-haired guy: hair,middleaged,sing",]
        #            else:
        #                NounList += ["graying man x2: hair,middleaged,sing","graying middle-aged man: hair,middleaged,sing"]
        #        elif self.HairStyle in ["bald"]:
        #            NounList += ["bald man: hair,bald,sing","balding man: hair,bald,sing","bald guy: hair,bald,sing","bald middle-aged man x3: hair,bald,middleaged,sing","balding middle-aged man: hair,bald,middleaged,sing","bald middle-aged guy: hair,bald,middleaged,sing"]

        #else:
        #    if self.RaceName == "poc":
        #        NounList += ["black man: poc,sing","ebony man: poc,sing","older black man: poc,older,sing","older black guy: poc,older,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald black man: hair,bald,poc,sing","bald older black man: hair,bald,poc,older,sing","bald older black guy: hair,bald,poc,older,sing",]
        #    elif self.RaceName == "asian":
        #        NounList += ["Asian man: asian,sing","older Asian man: asian,older,sing","older Asian guy: asian,older,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald Asian man: hair,bald,asian,sing","bald older Asian man: hair,bald,asian,older,sing","bald older Asian guy: hair,bald,asian,older,sing",]
        #    elif self.RaceName == "latin":
        #        NounList += ["latino man: latino,sing","older latino man: latino,older,sing","older latino guy: latino,older,sing",]
        #        if self.HairStyle in ["bald"]:
        #            NounList += ["bald latino man: hair,bald,latino,sing","bald older latino man: hair,bald,latino,older,sing","bald older latino guy: hair,bald,latino,older,sing",]
        #    else:
        #        if self.HairStyle in ["normal"]:
        #            NounList += ["man x2: sing","older man: older, sing","guy: older,guy,sing"]
        #            if self.HairColor == "blonde":
        #                NounList += ["blonde man x2: hair,cauc,sing","older blonde man: hair,cauc,older,sing","older blonde guy: hair,cauc,older,sing","blonde guy: hair,cauc,older,guy,sing","older man: older,sing"]
        #            elif self.HairColor == "redhead":
        #                NounList += ["redheaded man x2: hair,cauc,sing","older redheaded man: hair,cauc,older,sing","older redheaded guy: hair,cauc,older,sing","redheaded guy: hair,cauc,older,guy,sing","older guy: sing",]
        #            elif self.HairColor == "brown":
        #                NounList += ["brunette man x2: hair,cauc,sing","older brown-haired man: hair,cauc,older,sing","older brown-haired guy: hair,cauc,older,sing","brunette guy: hair,cauc,sing","older guy: older,sing","older man: hair,older,sing",]
        #            elif self.HairColor == "black":
        #                NounList += ["dark-haired man: hair,sing","raven-haired man: hair,guy,sing","older dark-haired man: hair,older,sing","older dark-haired guy: hair,older,sing","older man: older,sing","older guy: older,sing",]
        #            else:
        #                NounList += ["gray-haired man: hair,older,sing","silver-haired man: hair,older,sing","older gray-haired man: hair,older,sing","older silver-haired man: hair,older,sing","graying older man x2: hair,older,sing","older man: older,sing","older guy: older,sing",]
        #        elif self.HairStyle in ["bald"]:
        #            NounList += ["bald man: hair,bald,sing","balding man: hair,bald,sing","bald guy: hair,bald,sing","bald older man x3: hair,bald,older,sing","balding older man: hair,bald,older,sing","bald older guy: hair,bald,older,sing"]

        #if self.HeightType in ["tall"]:
        #    AdjList += ['tall x3: height,tall','lanky: height,tall','towering: height,tall','imposing: super',]
        #elif self.HeightType in ["short"]:
        #    AdjList += ['short x2: height,short','compact: width,narrow,height,short',]

        if self.BodyType in ["slender"]:
            AdjList += ['slender: slender','skinny: slender','bony: slender,',]
        elif self.BodyType in ["large"]:
            AdjList += ['big: size,large','heavy: size,large,chubby','massive: size,large','large: size,large','broad-chested: width,wide','broad-shouldered: width,wide','imposing: super']

        if self.IsFit:
            AdjList += ['muscular: strong,athletic','buff: strong,muscular','strong: strong','well-built: strong,shape','athletic: muscular,shape','fit: muscular','tough: muscular','broad-chested: width,wide','broad-shouldered: width,wide',]
        else:
            AdjList += ['dadbod: shape,chubby','pudgy: shape,chubby','sturdy: size,large,chubby','stocky: size,large,stocky',]

        if self.EyeColor in ["blue"]:
            AdjList += ['blue-eyed x3: eyes,cauc',]
        elif self.EyeColor in ["green"]:
            AdjList += ['green-eyed: eyes,cauc',]
        elif self.EyeColor in ["brown","dark"]:
            AdjList += ['brown-eyed x2: eyes','dark-eyed: eyes',]

        if self.RaceName in ["asian","caucasian","latino"]:
            if self.IsTan:
                AdjList += TanColors
            else:
                AdjList += ['fair: color,cauc','freckled: color,cauc','pale: color,cauc']

        # ["bald","buzz-cut","crew-cut","long-haired","ponytail","mullet","shaved","short-haired","slicked-back"]
        # ["afro","buzz-cut","cornrows","crew-cut","curly","dreadlocks","kinky",]
        #if self.HairStyle in ["afro"]:
        #    AdjList += ['afro\'d: hairstyle,afro,poc,bighair',]
        #elif self.HairStyle in ["buzz-cut"]:
        #    AdjList += ['buzz-cut: hairstyle,buzz,shorthair',]
        #elif self.HairStyle in ["braids"]:
        #    AdjList += ['crew-cut: hairstyle,crew,shorthair',]
        #elif self.HairStyle in ["cornrows"]:
        #    AdjList += ['cornrowed: hairstyle,cornrows,poc',]
        #elif self.HairStyle in ["curls"]:
        #    AdjList += ['curly: hairstyle,curls','curly-haired: hairstyle,curls',]
        #elif self.HairStyle in ["dreadlocks"]:
        #    AdjList += ['dreadlocked: hairstyle,dreads,poc',]
        #elif self.HairStyle in ["kinky"]:
        #    AdjList += ['kinky-haired: hairstyle,kinky,poc',]
        #elif self.HairStyle in ["long-haired"]:
        #    AdjList += ['long-haired: hairstyle,longhair',]
        #elif self.HairStyle in ["mullet"]:
        #    AdjList += ['mulletted: hairstyle,mullet',]
        #elif self.HairStyle in ["ponytail"]:
        #    AdjList += ['pony-tailed: hairstyle,ponytail',]
        #elif self.HairStyle in ["short"]:
        #    AdjList += ['short-haired: hairstyle,shorthair','short-cropped: hairstyle,shorthair',]
        #elif self.HairStyle in ["slicked-back"]:
        #    AdjList += ['slick: hairstyle,slick',]

        # ["beard","goatee","moustache","shaved","stubble"]
        if self.FacialHairStyle in ["beard"]:
            AdjList += ['authoritative: super','bearded x4: facialhair,beard',]
        elif self.FacialHairStyle in ["goatee"]:
            AdjList += ['goateed: facialhair,goatee',]
        elif self.FacialHairStyle in ["moustache"]:
            AdjList += ['moustachioed: facialhair,moustache',]
        elif self.FacialHairStyle in ["stubble"]:
            AdjList += ['stubbled: facialhair,stubble']
        else:
            AdjList += ['clean-cut: facialhair,shaved','clean-shaven: facialhair,shaved','chiseled: super','square-jawed: jawshape,square',]

        ManParams = NPParams(iNumAdjs = randint(3,4),
                               AdjList = AdjList,
                               ColorList = ColorList,
                               NounList = NounList)
        ManDesc = NounPhrase(Params = ManParams, TLParams = TagLists)

        self.ManDesc = ManDesc
        self.Noun = self.ManDesc.GetNoun()
        self.Desc = self.ManDesc.GetFullDesc(iNumAdjs = 4, bCommas = False)
        self.DescWords = self.ManDesc.GetDescWordList()

        #self.Man = NounPhrase()
        #self.Man.NounList(NounList)
        #self.Man.AdjList(AdjList)
        #self.Noun = self.Man.GetNoun()
        #self.Desc = self.Man.FloweryDesc(TagLists = TagLists(adj_excl = ["color"]))
        #self.DescWords = self.Man.GetDescWordList()

        return

@dataclass
class FemPhysTraits:
    AgeCat: str = ""
    Age: int = 0
    BodyType: str = ""
    BustSize: str = ""
    HasFakeTits: bool = False
    HairStyle: str = ""
    IsVirgin: bool = False

class Woman(Body):
    def __init__(self, NewGenTraits = None, NewFemTraits = None):
        super().__init__("female", NewGenTraits = NewGenTraits)
        self.Noun = ""
        self.Desc = ""
        self.DescWords = []
        self.WomanDesc = None
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

        self.BuildDesc(LTagLists)

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

        #print("\n" + sDesc)

    def BuildDesc(self, TagLists):
        
        AdjList = ['beautiful: super',
                   'bright-eyed: eyes',
                   'cute: super',
                   'doe-eyed: eyes',
                   'lovely: super',
                   'pretty: super',
                   'sexy: super',
                   'striking: super',
                  ]

        ColorList = []

        NounList = ['woman x4: adult,sing',
                   ]

        if self.RaceName == "asian":
            AdjList += ['Asian x12: race,asian',]
        elif self.RaceName == "caucasian":
            if self.HairColor in ["blonde"]:
                NounList += ['blonde x3: haircolor,blonde,cauc,sing','blonde bombshell: haircolor,blonde,cauc,sing',]
                AdjList += ['blonde x8: blonde,haircolor,cauc','fair: blonde,haircolor,cauc','platinum blonde: blonde,haircolor,cauc',]
            elif self.HairColor in ["brown"]:
                NounList += ['brunette x3: haircolor,brunette,cauc,sing',]
                AdjList += ['brunette x8: haircolor,brunette,cauc',]
            elif self.HairColor in ["gray"]:
                AdjList += ['gray-haired: haircolor,grayhair,older,age','silver-haired: haircolor,grayhair,older,age']
            else:
                AdjList += ['dark-haired: haircolor,dark,brunette','raven-haired x3: haircolor,darkhair',]
        elif self.RaceName == "latin":
            AdjList += ['latina x12: race,latina,sing',]
            NounList += ['latina x3: race,latina,sing',]
        elif self.RaceName == "poc":
            AdjList += ['black x12: color,race,poc','ebony x6: color,race,poc',]
        elif self.RaceName == "redhead":
            AdjList += ['redheaded x12: haircolor,race,redhead,redhair',]
            NounList += ['redhead x3: haircolor,redhead,race,ginger,sing',]

        if self.AgeCat not in ["milf",]:
            AdjList += ['young x8: age,young',]
            NounList += ['girl x3: age,young,sing',]
        else:
            AdjList += ['matronly: age,older,bigtits',
                        'mature x4: age,older',]
            NounList += ['MILF x2: age,older,milf,sing',]
        if self.AgeCat not in ["twenties","milf"]:
            AdjList += ['nubile x2: super,young',]
            NounList += ['young lady x3: adult,age,young,sing',
                         'young woman x3: adult,age,young,sing',]
        if self.AgeCat in ["teen"]:
            AdjList += ['teen x8: age,teen,young',
                        'teenage x6: age,teen,young',]
            NounList += ['teen x3: age,young,teen,sing',]
        else:
            NounList += ['lady x2: adult,sing',]
            
        if self.AgeCat in ["college"]:
            NounList += ['coed x3: age,young,college,sing',
                         'college girl x3: age,young,college,sing',]

        if self.BustSize in ["large","huge"]:
            AdjList += ['ample-bosomed: bigtits','big-titted: bigtits','bosomy: bigtits,shape','busty: bigtits','buxom: bigtits','full-figured: bigtits,shape','shapely: curvy,bigtits,shape','stacked: bigtits,shape','statuesque: bigtits,shape','voluptuous: bigtits,curvy,shape',]
        elif self.BustSize in ["small"]:
            AdjList += ['flat-chested: smalltits','lithe: slender,flexible','petite: short,small,slender','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]
            
        if self.BodyType in ["plussize"]:
            AdjList += ['chubby: plussize,shape','Rubenesque: plussize,shape','plump: curvy,plussize,shape',]
        elif self.BodyType in ["curvy"]:
            AdjList += ['curvaceous: curvy,shape','round-bottomed: curvy,shape','shapely: curvy,shape']
        elif self.BodyType in ["slender"]:
            AdjList += ['elfin: slender','limber:slender,flexible','lithe: slender,flexible','little: size,small,slender','petite: short,small,slender','skinny: slender','slender: slender','tight-bodied: slender','waifish: slender',]
            
        if self.RaceName in ["asian","caucasian","latin"]:
            if self.IsTan:
                AdjList += TanColors
        if self.RaceName in ["caucasian","redhead"]:
            if not self.IsTan:
                AdjList += ['fair-skinned: color','freckled: color','pale: color',]

                if self.EyeColor in ["blue"]:
                    AdjList += ['blue-eyed x3: eyes,eyecolor',]
                elif self.EyeColor in ["green"]:
                    AdjList += ['green-eyed: eyes,eyecolor',]
                elif self.EyeColor in ["brown","dark"]:
                    AdjList += ['brown-eyed x2: eyes,eyecolor','dark-eyed: eyes,eyecolor',]

                
        if self.Height in ["tall"]:
            AdjList += ['tall: height,tall','willowy: height,tall']
        elif self.Height in ["short"]:
            AdjList += ['little: height,short','petite: short,small,slender','short: height,short',]
        else:
            AdjList += ['little: height,short',]

        #if self.HairStyle in ["bobbed"]:
        #    AdjList += ['bobbed: hairstyle,bob,shorthair',]
        #elif self.HairStyle in ["braids"]:
        #    AdjList += ['braided: hairstyle,braids',]
        #elif self.HairStyle in ["cornrows"]:
        #    AdjList += ['cornrowed: hairstyle,cornrows,poc',]
        #elif self.HairStyle in ["curls"]:
        #    AdjList += ['curly: hairstyle,curls','curly-haired: hairstyle,curls',]
        #elif self.HairStyle in ["fro"]:
        #    AdjList += ['afro\'d: hairstyle,fro,poc',]
        #elif self.HairStyle in ["kinky"]:
        #    AdjList += ['kinky-haired: hairstyle,kinky,poc',]
        #elif self.HairStyle in ["long"]:
        #    AdjList += ['long-haired: hairstyle,longhair',]
        #elif self.HairStyle in ["pigtails"]:
        #    AdjList += ['pigtailed: hairstyle,pigtails',]
        #elif self.HairStyle in ["pixie"]:
        #    AdjList += ['pixie-cut: hairstyle,pixie,shorthair',]
        #elif self.HairStyle in ["ponytail"]:
        #    AdjList += ['pony-tailed: hairstyle,ponytail',]
        #elif self.HairStyle in ["short"]:
        #    AdjList += ['short-haired: hairstyle,shorthair',]
        #elif self.HairStyle in ["updo"]:
        #    AdjList += ['big-haired: hairstyle,updo','permed: hairstyle,updo',]

        if self.IsFit:
            AdjList += ['athletic: muscular,shape','fit: muscular','trim: slender,shape']
        else:
            AdjList += ['dainty: small,fragile','delicate: fragile',]
            
        if self.IsVirgin:
            AdjList += ['virginal: virginal',]

        WomanParams = NPParams(iNumAdjs = randint(3,4),
                               AdjList = AdjList,
                               ColorList = ColorList,
                               NounList = NounList)
        WomanDesc = NounPhrase(Params = WomanParams, TLParams = TagLists)

        self.WomanDesc = WomanDesc
        self.Noun = self.WomanDesc.GetNoun()
        self.Desc = self.WomanDesc.GetFullDesc(iNumAdjs = 4, bCommas = False)
        self.DescWords = self.WomanDesc.GetDescWordList()

        return True

