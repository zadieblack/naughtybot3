#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Body Parts module

from random import *

from util import *
from excerpt.ex_helpers import *

SkinColors = ["almond: color,asian",
              "beige: color,male",
              "black x4: color,poc",
              "bronze: color,poc",
              "bronzed: color,poc,tan",
              "brown: color,poc",
              "chocolate: color,poc",
              "chocolate-colored: color,poc",
              "coffee-colored: color,poc",
              "copper-skinned: color,poc",
              "creamy: color,cauc,female",
              "cream-colored: color,cauc,female",
              "dark: color,poc",
              "dark brown: color,poc",
              "deeply-tanned:color,cauc,tan",
              "ebony: color,poc,female",
              "fair: color,cauc,female",
              "freckled: color,cauc",
              "fresh pink: color,cauc,female",
              "honeyed: color",
              "light: color,cauc",
              "light brown: color,poc",
              "lightly-browned: color,tan",
              "mocha: color,poc",
              "pale: color,cauc",
              "pink: color,cauc",
              "porcelain: color,cauc",
              "rosy: color,cauc,female",
              "tan: color,poc,tan",
              "tanned: color,cauc,tan",
              "sun-bronzed: color,cauc,tan",
              "sun-browned: color,cauc,tan",
              "sun-kissed: color,cauc,tan",
              "white: color,cauc",
              "mocha: color,poc",
              "tan: color,tan",
              "tanned: color,tan",
             ]

TanColors = ["deeply-tanned","honeyed","tan","tanned","sun-bronzed","sun-browned","sun-kissed",]

ColorSkinonyms = {"beige": ["bronze","tan"],
                 "black": ["dark brown"],
                 "bronze": ["coffee-colored","mocha"],
                 "coffee-colored": ["bronze","mocha"],
                 "creamy": ["fair","pale","porcelain","white"],
                 "fair": ["creamy","pale","porcelain","white"],
                 "deeply-tanned": ["honeyed","tan","tanned","sun-bronzed","sun-browned","sun-kissed",],
                 "fresh pink": ["pink","rosy"],
                 "honeyed": ["deeply-tanned","tan","tanned","sun-bronzed","sun-browned","sun-kissed",],
                 "light brown": ["beige","bronze","lightly-browned"],
                 "lightly-brown": ["beige","bronze","light brown"],
                 "mocha": ["bronze","coffee-colored"],
                 "pale": ["white","porcelain"],
                 "pink": ["fresh pink","rosy"],
                 "porcelain": ["creamy","fair","pale","white"],
                 "rosy": ["fresh pink","pink"],
                 "sun-bronzed": ["deeply-tanned","honeyed","tan","tanned","sun-browned","sun-kissed",],
                 "sun-browned": ["deeply-tanned","honeyed","tan","tanned","sun-bronzed","sun-kissed",],
                 "sun-kissed": ["deeply-tanned","honeyed","tan","tanned","sun-bronzed","sun-browned",],
                 "tan": ["beige","honey","light brown","lightly-browned",],
                 "tanned": ["deeply-tanned","honeyed","tan","sun-bronzed","sun-browned","sun-kissed",],
                 "white": ["creamy","fair","pale","porcelain"],
                }

def GetSkinonym(sColor):
    sSkinonym = sColor

    if sColor in ColorSkinonyms:
        sSkinonym = choice([sColor] + ColorSkinonyms[sColor])

    return sSkinonym

#Race = namedtuple("Race", "Name HairColor EyeColor SkinColor NipColor")

@dataclass
class Race:
    Name: str = ""
    TagName: str = ""
    EyeColor: list = field(default_factory=list)
    HairColor: list = field(default_factory=list)
    NipColor: list = field(default_factory=list)
    SkinColor: list = field(default_factory=list)
    FemHairStyle: list = field(default_factory=list)
    MaleHairStyle: list = field(default_factory=list)

RaceCauc    = Race(Name = "caucasian",
                   TagName = "cauc",
                   EyeColor = ["amber","blue","blue","brown","dark","gray","green","hazel"],
                   HairColor = ["black","blonde","brown","dark","gray","red"],
                   NipColor = ["brown","dark","coral","pale","pink","pink","reddish","rosy","rosy","tan"],
                   SkinColor = ["beige","creamy","freckled","fresh pink","honeyed","light","pale","pink","porcelain","rosy","tanned","sun-bronzed","sun-browned","sun-kissed","white"],
                   FemHairStyle = ["big","bobbed","braids","curls","long","pigtails","pixie","ponytail","short","updo"],
                   MaleHairStyle = ["bald","buzz-cut","crew-cut","curly","long-haired","ponytail","mullet","shaved","short-haired","slicked-back"]
                  )
RaceGinger  = Race(Name = "redhead",
                   TagName = "redhead",
                   EyeColor = ["amber","blue","brown","gray","green","green","hazel"],
                   HairColor = ["auburn","copper","fiery red","flaming red","ginger","red","strawberry blonde"],
                   NipColor = ["coral","pale","pale","pale pink","pink","pink","reddish","rosy",],
                   SkinColor = ["creamy","freckled","freckled","fresh pink","pale","pale","pink","porcelain","rosy","white"],
                   FemHairStyle = ["big","bobbed","braids","curls","long","pigtails","pixie","ponytail","short","updo"],
                   MaleHairStyle = ["bald","buzz-cut","crew-cut","curly","long-haired","ponytail","mullet","shaved","short-haired"]
                  )
RacePOC     = Race(Name = "poc",
                   TagName = "poc",
                   EyeColor = ["amber","brown","dark",],
                   HairColor = ["black","brown","dark",],
                   NipColor = ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"],
                   SkinColor = ["black","beige","bronze","bronzed","brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","ebony","honeyed","light brown","mocha","tan"],
                   FemHairStyle = ["cornrows","curls","fro","kinky","long","pixie","short","updo"],
                   MaleHairStyle = ["afro","buzz-cut","cornrows","crew-cut","curly","dreadlocks","kinky",]
                  )
RaceAsian   = Race(Name = "asian",
                   TagName = "asian",
                   EyeColor = ["brown","dark",],
                   HairColor = ["black","brown","dark",],
                   NipColor = ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha"],
                   SkinColor = ["almond","beige","brown","creamy","freckled","light","light brown","pale","porcelain","tan","sun-bronzed","sun-browned","sun-kissed","white"],
                   FemHairStyle = ["braids","long","pigtails","pixie","ponytail","short",],
                   MaleHairStyle = ["bald","buzz-cut","crew-cut","long-haired","ponytail","shaved","short-haired","slicked-back"]
                  )
RaceLatin   = Race(Name = "latin",
                   TagName = "latin",
                   EyeColor = ["amber","brown","dark","hazel"],
                   HairColor = ["black","brown","dark",],
                   NipColor = ["brown","chocolate","chocolate-colored","coffee-colored","dark","dark brown","honeyed","light brown","mocha","reddish","tan"],
                   SkinColor = ["beige","bronze","brown","copper","creamy","dark","freckled","light","light brown",],
                   FemHairStyle = ["braids","curls","kinky","long","pigtails","pixie","ponytail","short","updo"],
                   MaleHairStyle = ["buzz-cut","cornrows","crew-cut","curly","dreadlocks","kinky","ponytail","shaved","short-haired","slicked-back"]
                  )

RaceList = [RaceCauc,RaceGinger,RacePOC,RaceAsian,RaceLatin]

class BodyParts(NounPhrase):
    def AddSkinColors(self):
        super().ColorList(SkinColors)

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
          
          self.AddSkinColors()

          self.NounList(['face x3: default,std,sing'
                        ])
          
          self.AdjList(['adorable: super,cute,young',
                        'angelic: super,cute',
                        'beaming: emotion,happy',
                        'beautiful: super',
                        'cute: super,cute',
                        'delicate: cute',
                        'elegant: older',
                        'excited: emotion,happy',
                        'expressive: emotion',
                        'gentle: attitude',
                        'gorgeous: super',
                        'flushed: arousal',
                        'heart-shaped: shape',
                        'innocent: attitude,cute,young,virginal',
                        'lovely: super',
                        'oval: shape',
                        'pretty: super',
                        'radiant: ',
                        'round: shape',
                        'smiling: emotion,happy',
                        'startled: emotion',
                        'sweet: attitude,cute',
                        'warm: attitude,feel',
                        'wide-eyed: cute'])
               
          self.DefaultNoun('face')
          
class BackFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

          self.NounList(['back x4:default,std,sing',
                         'spine:std,clinical,sing'])
          
          self.AdjList(['arched x2: shape',
                         'arching: action',
                         'bare: nude',
                         'carved: shape',
                         'concave: shape',
                         'curved x2: shape',
                         'delicate: super',
                         'feminine: super',
                         'flexible: flexible',
                         'gently curved: shape',
                         'graceful x2: fit',
                         'lissome: slender',
                         'lithe x2: athletic,young,flexible,slender',
                         'long: size,length,long',
                         'naked: nude',
                         'sculpted: shape',
                         'sexy: super',
                         'sleek: slender',
                         'slender x2: slender',
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
          
          self.AddSkinColors()
          self.NounList(['skin x4: default,std,sing',
                         'flesh: sing'
                        ])
                              
          self.AdjList(['bare: nude',
                        'delicate: super,cute',
                        'exposed: nude',
                        'gentle: feel',
                        'gleaming: shiny',
                        'glistening: wet,shiny',
                        'glowing: shiny',
                        'gossamer: shiny',
                        'luscious: horny,super',
                        'lustrous x2: texture,shiny',
                        'naked: nude',
                        'perfect: super',
                        'silken: texture',
                        'soft: feel,',
                        'smooth: feel,',
                        'supple: feel,young,',
                        'sweet: super,',
                        'tender: feel,',
                        'un-blemished: young,virginal,',
                        'un-sullied: young,virginal',
                        'warm: feel',
                        'yielding: feel',
                        'youthful: young',
                       ])
          
          self.DefaultNoun('skin')
          
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
                        'pretty: super',
                        'soft: feel',
                        'sweet: super',
                        'thirsty: horny',
                        'wanting: horny',
                        'warm: feel',
                        'wet: wet',
                        'willing: attitude,horny'])
          
          self.DefaultNoun("open")
          self.DefaultAdj("insatiable")
          
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
               
          self.AdjList(['alluring: super',
                        'beautiful: super',
                        'bewitching: super',
                        'big: size,large',
                        'bright: super,young,cauc',
                        #'blue x4: color,cauc',
                        #'brown x2: color',
                        'captivating: super',
                        'clear: super,desc',
                        'dazzling: super,shiny',
                        'deep: size',
                        'earnest: emotion',
                        'electric: super',
                        'electrifying: super',
                        'enchanting: super',
                        'enormous: size,large',
                        'exotic: super',
                        #'gray x2: color,cauc',
                        #'green x3: color,cauc',
                        #'hazel x2: color,cauc',
                        'kind: emotion',
                        'large: size,large,desc',
                        'innocent: young,virginal',
                        'mischievous: emotion',
                        'pale: color,cauc',
                        'piercing: ',
                        'slanted: asian',
                        'soulful: super',
                        'sparkling: super,shiny',
                        'sweet: super',
                        'wide x3: size,large'])

          self.ColorList(['amber: color',
                          'blue x3: color,cauc',
                          'brown x4: color',
                          'dark: color',
                          'gray: color,cauc',
                          'green: color,cauc',
                          'hazel: color,cauc',
                          'pale: color,cauc',
                         ])
          
          self.DefaultNoun("eyes")
          self.DefaultAdj("bewitching")
          
class Hips(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

          self.NounList(['hips: std,default,plur'])
               
          self.AdjList(['curvy: width,wide,shape,desc',
                        'curvaceous: wide,width',
                        'bare: nude',
                        'broad: width,wide',
                        'fertile: width,wide,horny',
                        'girlish: shape,width,narrow,young',
                        'narrow: shape,width,narrow',
                        'rounded: shape',
                        'sensual: super',
                        'shapely: shape',
                        'slender: shape,size,small',
                        'slinky: attitude',
                        'sultry: attitude',
                        'tantalizing: horny,',
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
                        'vibrant: super',
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
          
          self.AddSkinColors()

          self.NounList(['legs: std,default,plur'])
               
          self.AdjList(['athletic: fit',
                        'bare: nude',
                        'chiseled: fit',
                        'chubby: curvy',
                        'coltish x2: slender, young',
                        'comely: super',
                        'elegant: super',
                        'feminine: super',
                        'fetching: super',
                        'fit: fit',
                        'flexible: flexible',
                        'girlish: young,slender',
                        'graceful: fit',
                        'lithe: flexible',
                        'limber: flexible',
                        'lissome: flexible,fit,slender',
                        'lithesome: flexible,fit,slender',
                        'long x3: length,long',
                        'long, sexy: length,long',
                        'lovely: super',
                        'naked: nude',
                        'satiny: feel,shiny',
                        'sinuous: flexible',
                        'smooth: feel,hairless',
                        'supple: feel,soft,young',
                        #'tan: color',
                        #'tanned: color',
                        'toned: fit',
                        'sexy: super',
                        'shapely: fit',
                        'shaved: hairless',
                        'short: length,short',
                        'slender: slender',
                        'smooth: hairless',
                        'smooth-shaven: hairless',
                        'supple: soft,young,feel',
                        'svelte: slender,flexible',
                        'willowy: slender',
                        'womanly: curvy',
                        'yielding: soft,feel,horny',
                       ])
          
          self.DefaultNoun("legs")
          
class Thighs(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

          self.NounList(['thighs: std,default,plur'])
               
          self.AdjList(['bare: nude',
                        #'bronzed: color,tan',
                        'chubby: curvy,chubby',
                        'comely: super',
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
                        'ripe: super',
                        'rounded: shape',
                        'sensual: super',
                        'sexy: super',
                        'shapely: shape',
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
                        'big: size,large',
                        'bite-sized: size,small',
                        'blossoming: young',
                        'budding: cute,young',
                        'cone-shaped: shape',
                        'conical: shape',
                        'dainty: size,small,cute',
                        'delicate: super',
                        'elfin: size,small,delicate,cute',
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'exquisite: super',
                        'fat: large',
                        'feminine: super',
                        'firm: feel,texture',
                        'fleshy: texture',
                        'flushed: color',
                        'hard: arousal,',
                        'huge: size,large',
                        'impudent: super',
                        'inch-long: length,long,',
                        'inviting: horny',
                        'large: size,large',
                        'long: length,long',
                        'lush: size,large,',
                        'luscious: super',
                        'oval: shape',
                        'perfect: super',
                        'perky: arousal',
                        'petite: size,small,cute,',
                        'pert: arousal,cute',
                        'pierced: style',
                        'plump: size,large',
                        'pointy: shape,long',
                        'pokey: arousal',
                        'prominent: size,large',
                        'proud: super',
                        'puffy: feel,',
                        'rigid: arousal',
                        'ripe: super',
                        'rock-hard: arousal',
                        'rosebud: color,cauc',
                        'round: shape',
                        'saucer-like: shape,size,large',
                        'saucy: horny',
                        'sensitive: feel',
                        'shameless: nude',
                        'shy: small,cute',
                        'soft: feel',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'succulent: super,taste',
                        'suckable: horny',
                        'sweet: super,cute',
                        'swollen: arousal,size,large,',
                        'taut: arousal',
                        'tasty: taste,horny',
                        'tempting: horny',
                        'tender: feel',
                        'thick: size,large,arousal,',
                        'tight: size,small',
                        'tiny: size,small,',
                        'turgid: arousal',
                        'two-inch: length',
                        'velvety: feel',
                        'wee: size,small,cute',
                        'wide: size,large',
                        'young: young',
                        'youthful: youthful',
                       ])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")

class Breasts(FemaleBodyParts):
    def __init__(self, Params = None, NotList = None, TagLists = None, bCupSize = False):
        super().__init__(Params, NotList, TagLists)
        self._bCupSize = bCupSize
        self.AddSkinColors()
          
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
                      'enchanting: super',
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
                      'sensual: super',
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

    def ShortDesc(self, NotList = None, TagLists = None, bSilly = False, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)

        return super().ShortDesc(NotList, TagLists, bSilly)
          
    def MediumDesc(self, NotList = None, TagLists = None, bSilly = False, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)
               
        return super().MediumDesc(NotList, TagLists, bSilly) 
          
    def FloweryDesc(self, NotList = None, TagLists = None, bSilly = False, bCupSize = None):
        if bCupSize is None:
            bCupSize = self._bCupSize

        if bCupSize and not self._bCupSize:
            self.AllowCupSize(bCupSize = bCupSize)
          
        return super().FloweryDesc(NotList, TagLists, bSilly) 
          
    def RandomDesc(self, bShortDesc = True, bLongDesc = True, NotList = None, TagLists = None, bSilly = False, bCupSize = None):
        self._bCupSize = bCupSize

        return super().RandomDesc(bShortDesc, bLongDesc, NotList, TagLists, bSilly) 
     
          
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
                        'little x3: size,small',
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
                        'juicy: wet,taste',
                        'lickable: horny',
                        'luscious: taste',
                        'lush: super',
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
                        'delicate: small,cute',
                        'dewy x2: wet,cute',
                        'drooping: hanging,shape',
                        'fleshy: meaty',
                        'gossamer: super,cute',
                        'lengthy: size,long',
                        'lickable: horny',
                        'little: size,small',
                        'long: long',
                        'lush: super,cute',
                        'meaty x2: meaty',
                        'moist: wet',
                        'pink: color',
                        'purplish: color',
                        'ruffled: shape',
                        'secret: taboo,virginal',
                        'shameless: horny',
                        'silken: feel,cute',
                        'shy: virginal,cute',
                        'succulent: taste,super',
                        'suckable: horny',
                        'tasty: taste,horny',
                        'tender: feel,cute',
                        'trim: size, small',
                        'well-used: slutty',
                        'velvet: super, feel'])
                              
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
          self.InnerVag = VaginaInner()
          self.OuterLabia = VaginaOuterLabia()
          self.InnerLabia = VaginaInnerLabia()
          self.Clitoris = Clitoris()

class AnusFemale(FemaleBodyParts):
    def __init__(self, Params = None, NotList = None, TagLists = None, bGape = False):
        super().__init__(Params, NotList, TagLists)

        self.Gape = bGape

        self.GapeCheck(self.Gape)

        self.NounList(['anus x4: std,default,clinical,sphincter,orifice,sing',
                        'arse-cunt: crude,orifice,sing',
                        'ass: std,orifice,sing',
                        'asshole x4: std,slang,crude,sphincter,orifice,sing',
                        'back orifice: desc,clinical,orifice,sing',
                        'back passage: desc,orifice,sing',
                        'back-pussy: silly,crude,slang,orifice,sing',
                        'backdoor: desc,slang,orifice,sing',
                        'bowels: std,orifice,plur',
                        'brown hole: desc,slang,crude,sphincter,orifice,sing',
                        'bunghole: silly,crude,slang,sphincter,orifice,sing',
                        'chocolate starfish: silly,crude,slang,sphincter,sing',
                        'corn hole: silly,crude,slang,sphincter,orifice,sing',
                        'dirt-pipe: crude,slang,orifice,sing',
                        'dirt-box: crude,slang,orifice,sing',
                        'fart-blaster: silly,crude,slang,orifice,sing',
                        'fart-box: silly,crude,slang,orifice,sing',
                        'fart-hole: silly,crude,slang,sphincter,orifice,sing',
                        'heinie hole: desc,slang,cute,sphincter,orifice,sing',
                        'knot: desc,sphincter, sing',
                        'poop-chute: crude,slang,desc,orifice,sing',
                        'poop-trap: silly,crude,slang,sing,orifice,sphincter',
                        'rear orifice: desc, clinical, orifice,sing',
                        'rectal cavity: desc, clinical, orifice,sing',
                        'rectum: std,clinical,orifice,sing',
                        'ring: desc,sphincter,sing',
                        'rosebud: desc,slang,cute,crude,sphincter,orifice,sing',
                        'shit-hole: crude,slang,desc,orifice,sing',
                        'shitter: crude,slang,orifice,sing',
                        'sphincter x2: std,clinical,sphincter,sing',
                        'starfish x2: silly,cute,slang,sphincter,orifice,sing',
                    ])
       
        self.AdjList(['brown: color',
                    'clenched: small,tight,action',
                    'flexing: action',
                    'forbidden: super',
                    'fuckable: horny',
                    'gaping: large,gape,loose',
                    'knotted: small,tight,desc',
                    'lewd: horny',
                    'little x4: small,cute,',
                    'loose: gape,loose',
                    'MILF: age,older,milf',
                    'nasty: super',
                    'naughty: horny',
                    'pert: cute,young',
                    'perverted: super',
                    'puckered: action',
                    'rusty: desc,color',
                    'shameful: super',
                    'shy: cute,super',
                    'sinful: super',
                    'smooth: feel,desc',
                    'snug x2: small,tight,cute,'
                    'taboo: super',
                    'teasing: horny',
                    'tender: feel,desc,cute',
                    'tight x4: small,tight',
                    'wanton: horny',
                    'well-used: gape,older,loose',
                    'willing: horny',
                    'winking: small,action',
                    'virgin: virginal',
                    'vulgar: super',
                    ])
          
        self.DefaultNoun("anus")

    def GapeCheck(self, bGape = False):
        if not bGape:
            if not "gape" in self._ExclTagList:
                self.ExclTagList(self._ExclTagList + ["gape"])
        else:
            if "gape" in self._ExclTagList:
                self.ExclTagList(self._ExclTagList.copy.remove("gape"))
        return

    def ShortDesc(self, NotList = None, TagLists = None, bSilly = False, bGape = False):
        self.GapeCheck(bGape)

        return super().ShortDesc(NotList, TagLists, bSilly)
          
    def MediumDesc(self, NotList = None, TagLists = None, bSilly = False, bGape = False):
        self.GapeCheck(bGape)
               
        return super().MediumDesc(NotList, TagLists, bSilly) 
          
    def FloweryDesc(self, NotList = None, TagLists = None, bSilly = False, bGape = False):
        self.GapeCheck(bGape)
          
        return super().FloweryDesc(NotList, TagLists, bSilly) 
          
    def RandomDesc(self, bShortDesc = True, bLongDesc = True, NotList = None, TagLists = None, bSilly = False, bGape = False):
        self.GapeCheck(bGape)

        return super().RandomDesc(bShortDesc, bLongDesc, NotList, TagLists, bSilly) 
     
          
class ButtocksFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
     
          self.AddSkinColors()

          self.NounList(['ass-cheeks: std,plur',
                         'buns: std,plur',
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
                        'shapely x3: shape',
                        'smooth: hairless,feel,texture',
                        'squeezable x2: horny',
                        'succulent: super,horny',
                        'supple: feel,texture,young',
                        'sweet: super',
                        'tender: feel',
                        'teen: age,young,teen',
                        'thick x3: size,large,shape,curvy',
                        'tight: size,small',
                        'trim: size,small',
                        'voluptuous: shape,curvy',
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
                        #'black: color,poc',
                        'bountiful: super,large',
                        'broad: width,wide,plussize',
                        #'brown: color,poc',
                        #'bronzed: color',
                        'bubble-shaped: shape,curvy',
                        'chubby: plussize',
                        #'coffee-colored: color,poc',
                        'college-girl: age,college',
                        #'creamy: color,texture,cauc',
                        'curvaceous: curvy',
                        'curvy: curvy',
                        'cute: cute,size,small',
                        'cute little: cute,size,small',
                        #'dark: color,poc',
                        'delightful: super',
                        'fat x4: plussize',
                        'firm: strong,texture',
                        'fuckable: horny',
                        'generous: super,large',
                        'glistening: shiny',
                        'heart-shaped: shape',
                        'huge: size,large,plussize',
                        #'honeyed: super,texture,color,poc',
                        'jiggling: movement',
                        'juicy: super,taste',
                        'lush: super',
                        'luscious: super',
                        'MILF: age,older',
                        'muscular: muscular,shape',
                        'naked: nude',
                        'nubile: age,young',
                        #'pale: color,cauc',
                        'perfect: super',
                        'pert: shape',
                        #'pink: color,cauc',
                        'plump: curvy,plussize',
                        'ripe: super',
                        #'rosy: color,cauc',
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
                        #'sun-bronzed: color',
                        #'sun-kissed: color',
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
                        'virgin: age,young,virginal',
                        'voluptuous: curvy',
                        'well-rounded: super,shape',
                        #'white: color,cauc',
                        'wide: width,wide',
                        'womanly: super,curvy',
                        'youthful: age,young',
                        'yummy: super',
                       ])
          
          self.DefaultNoun("ass")
          
class BodyFemale(FemaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

          self.NounList(['anatomy: std,sing',
                         'body x4: std,default,sing',
                         'curves: plur',
                         'figure: std,sing',
                         'form: std,sing',
                         'physique: std,sing'])
               
          self.AdjList(['agile: flexible',
                        'athletic: muscular',
                        'bare: nude',
                        'beautiful: super',
                        'big-hipped: curvy,plussize',
                        'breathtaking: super',
                        'busty: bigtits',
                        'buxom: bigtits',
                        'chubby: plussize',
                        'curvaceous: shape,curvy,bigtits',
                        'curvy: shape,curvy',
                        'dainty: small,delicate',
                        'delicate: delicate',
                        'feminine: super',
                        'firm: muscular',
                        'fit: muscular',
                        'flexible: flexible',
                        'full: curvy',
                        'gorgeous: super',
                        'graceful: super,slender',
                        'healthy: super',
                        'leggy: longlegs,tall',
                        'lithe: slender,flexible',
                        'little: size,small',
                        'luscious: super',
                        'lush: super',
                        'luxuriant: super',
                        'matronly: older',
                        'model-esque: super',
                        'narrow-waisted: shape',
                        'nubile: young',
                        'plump: size,large,plussize',
                        'plus-size: size,large,plussize',
                        'ravishing: super',
                        'ripe: super',
                        'Rubenesque: plussize',
                        'sensual: super',
                        'sensuous: super',
                        'sexy: super',
                        'shameless: nude',
                        'shapely: shape',
                        'slender: slender',
                        'slight: delicate,slender,small',
                        'slim: slender',
                        'small: small',
                        'smooth: hairless,feel',
                        'statuesque: bigtits',
                        'strong: muscular',
                        'stunning: super',
                        'sultry: super',
                        'svelte: slender',
                        'sweet: super',
                        'taut: slender,muscular',
                        'teenage: young,teen,age',
                        'tight: slender,smalltits',
                        'tiny: small,short',
                        'toned: muscular',
                        'trim: slender',
                        'twentysomething: young,twenties,age',
                        'voluptuous: bigtits,curvy',
                        'willowy: slender,tall',
                        'womanly: super',
                        'wonderful: super',
                        'wondrous: super',
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
     
     def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bBoobs = True, bPussy = False, bAss = False, bBody = True, bExplicit = False, bLongDesc = True, sPossessive = None, NotList = None):
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
                           ]

          if bBody:
              PartPriorities.append([body,4])
          
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
          
class Testicles(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)

          self.NounList(['balls x3: std,default,plur', 
                         'ballsack x2: silly,crude,slang,sing',
                         'bollocks: silly,crude,plur',
                         'gonads: std, clinical, plur',
                         'nuts: silly,slang,plur',
                         'nutsack: silly,slang,crude,sing',
                         'sack: desc,sing',
                         'scrotum x2: std,clinical,sing',
                         'silk purse: desc,sing',
                         'testicles x2: std,clinical,plur',
                        ])
               
          self.AdjList(['black: color,poc',
                        'bare: nude,hairless',
                        'brown: color,poc,latin',
                        'bull-like: super,large',
                        'dangling: hanging',
                        'dark: color',
                        'delicious: super,horny',
                        'downy: hairy',
                        'down-covered: hairy',
                        'enormous: large',
                        'fat: size,large',
                        'fleshy: texture,feel',
                        'fuzzy: hairy,texture',
                        'hairless: hairless',
                        'hairy: hairy',
                        'heavy: size,large',
                        'hefty: size,large',
                        'large: size,large',
                        'leathery: texture',
                        'low-hanging: hanging',
                        'low-swinging: movement,hanging',
                        'magnificent: super',
                        'mammoth: size,large',
                        'monstrous: super,size,large',
                        'pale: color,cauc,asian',
                        'pendulous: shape',
                        'plump: shape,large',
                        'ripe: super',
                        'round: shape',
                        'satin: texture',
                        'silken: texture',
                        'soft: feel',
                        'small: size,small',
                        'smooth: hairless',
                        'smooth-shaven: hairless',
                        'swaying: movement',
                        'swinging: movement',
                        'taut: shape',
                        'tender: super',
                        'tight: shape',
                        'virile: super',
                        'wee: size,small,cute',
                        'wrinkled: texture',
                       ])
          
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
                        'gorgeous: super',
                        'greasy x4: feel,wet',
                        'hairy x4: hairy',
                        'hairless x2: hairless',
                        'hard x3: hard',
                        'hardened: hard',
                        'heavy: bigdick,feel',
                        'hefty: bigdick',
                        'hooked: shape',
                        'hot x2: feel,super',
                        'huge: size,bigdick',
                        'hugely erect: size,bigdick,hard',
                        'impressive: super',
                        'knobby: shape',
                        'legendary: super',
                        'lengthy: length,long,bigdick',
                        'long: length,long,bigdick',
                        'lovingly man-scaped: style,trimmed',
                        'lustful x2: horny',
                        'magnificent: super',
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
                        'pretty: super',
                        'proud: super',
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
                        'virile: super',
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
               
     def ShortDesc(self, NotList = None, TagLists = None, bAddLen = False, bSilly = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().ShortDesc(NotList, TagLists, bSilly)
          
     def MediumDesc(self, NotList = None, TagLists = None, bAddLen = False, bSilly = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
               
          return super().MediumDesc(NotList, TagLists, bSilly) 
          
     def FloweryDesc(self, NotList = None, TagLists = None, bAddLen = False, bSilly = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().FloweryDesc(NotList, TagLists, bSilly) 
          
     def RandomDesc(self, NotList = None, TagLists = None, bShortDesc = True, bLongDesc = True, bAddLen = False, bSilly = False):
          if bAddLen:
               if TagLists is None:
                   TagLists = self.GetTLClass()
                   TagLists.adj_extra.append(self.GenerateLength())
          
          return super().RandomDesc(bShortDesc, bLongDesc, NotList, TagLists, bSilly) 
     
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
                        'delicious: taste,super,horny',
                        'glossy: shiny',
                        'gooey x3: sticky',
                        'hot x3: feel,warm',
                        'nasty: gross,horny',
                        'nourishing: taste,horny',
                        'oozing: sticky',
                        'potent: super',
                        'ropy: shape',
                        'salty x2: taste',
                        'silken: feel',
                        'silky: feel',
                        'sloppy x2: sticky,gross',
                        'sticky x4: sticky',
                        'tasty: taste,horny',
                        'thick x4: thick',
                        'virile x3: super',
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
          
          self.AddSkinColors()

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
                        'manly: super',
                        'masculine: super',
                        'muscular: strong',
                        'rock-hard: feel,strong',
                        'sexy: super',
                        'smooth: hairless',
                        'strapping: strong',
                        'swole: size,large,shape',
                        'taut: strong',
                        #'tan: color',
                        'tight x2: size,narrow,shape',
                        'trim: size,narrow,shape',
                        'virile: super',
                        'well-defined: shape',
                       ])
          
          self.DefaultNoun("buttocks")
          
class AssMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.Anus = AnusFemale()
          self.Buttocks = ButtocksMale()
          
          self.AddSkinColors()

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
                        'chiseled: shape',
                        'compact: size,small',
                        'hairy: hairy',
                        'lean: size,small',
                        'manly: super',
                        'masculine: super',
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
                        'virile: super',
                        'well-defined: shape',
                       ])
          
          self.DefaultNoun("buttocks")
          
class SkinMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

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
          
          self.AddSkinColors() 

          self.NounList(['shoulders: plur'])
               
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
          
          self.AddSkinColors()

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
                        'sinewy: texture',
                        'strapping x2: super',
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
                        'enormous: size,large',
                        'erect: arousal,',
                        'exposed: nude',
                        'firm: arousal',
                        'handsome: super',
                        'hard: arousal,',
                        'perfect: super',
                        'pert: arousal,cute',
                        'pierced: style',
                        'prominent: length,long',
                        'small: size,small',
                        'stiff: arousal,',
                        'stiffly erect: arousal',
                        'tanned: color',
                        'thick: size,large,arousal,',
                        'tiny: size,small,',
                        'turgid: arousal',
                        'wide: size,large',
                       ])
               
          self.DefaultNoun("nipples")
          self.DefaultAdj("erect")
          
class ChestMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

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
                        'rugged: super,muscular',
                        'strapping: muscular,strong',
                        'strong: strong',
                        'sturdy: size,large',
                        'toned: muscular',
                        'wide: size,wide',
                        'uncovered: nude',
                        'virile: super',
                        'well-built: muscular',
                        'well-defined: muscular,shape',
                        'well-oiled: wet,shiny'])

          self.Nipples = NipplesMale()
          self.DefaultNoun("chest")
          self.DefaultAdj("broad")
          
class ArmsMale(MaleBodyParts):
     def __init__(self, Params = None, NotList = None, TagLists = None):
          super().__init__(Params, NotList, TagLists)
          
          self.AddSkinColors()

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
               
          self.AdjList(['alluring: super',
                        'beautiful: super',
                        'blue: color,cauc',
                        'bright: shiny',
                        'brown: color',
                        'brooding: emotion',
                        'captivating: super',
                        'clear: ',
                        'dark: color',
                        'dazzling: shiny',
                        'deep: ',
                        'earnest: emotion',
                        'electric: super',
                        'electrifying: super',
                        'gray: color, cauc',
                        'green: color, cauc',
                        'hazel: color, cauc',
                        'icy-blue: color, cauc',
                        'kind: emotion',
                        'large: size,large',
                        'magnetic: super',
                        'mischievous: emotion',
                        'narrow: size,narrow',
                        'penetrating: emotion',
                        'small: size,small',
                        'soulful: emotion',
                        'sparkling: shiny',
                        'steely: emotion',
                        'steely-blue: color, cauc',
                        'stern: emotion',
                        'sweet: young',
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
                        'manly: super',
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
          self.AddSkinColors()

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
          
          self.NounList(['jaw x3: std,default,sing',
                         'chin: variant,sing',
                        ])
               
          self.AdjList(['angular: shape',
                        'assertive: assertive',
                        'bearded: beard,hairy',
                        'chiseled: shape',
                        'commanding: assertive',
                        'decisive: assertive',
                        'dominant: assertive',
                        'forceful: assertive',
                        'handsome: super',
                        'powerful: assertive',
                        'rugged: shape',
                        'scruffy: stubble,hairy',
                        'sharp: shape',
                        'smooth-shaven: hairless',
                        'square: shape',
                        'striking: super',
                        'stubbled: stubble,hairy',
                        'unshaven: stubble,hairy',
                       ])
          
          self.DefaultNoun("jaw")
          self.DefaultAdj("chiseled")
          
class BodyMale(MaleBodyParts):     
    def __init__(self, Params = None, NotList = None, TagLists = None):
        super().__init__(Params, NotList, TagLists)
          
        self.AddSkinColors()

        self.NounList(['body x4: std,default,sing',
                       'build: std,sing',
                       'bulk: std,large,heavy,sing',
                       'form: std,sing',
                       'physique x2: std,sing',
                      ])
               
        self.AdjList(['beefy: large',
                      'brawny: strong,shape',
                      'broad: size,wide',
                      'burly: strong,shape,size,wide',
                      'commanding: attitude',
                      'compact: size,small',
                      'dad-bod: plussize',
                      'dark-thatched: hairy',
                      'godlike: super',
                      'handsome: super',
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
                      'sexy: super',
                      'short: length,short',
                      'sinewy: shape',
                      'smooth: hairless',
                      'strapping: strong',
                      'striking: super',
                      'strong: strong',
                      'sturdy: size,large',
                      'supple: flexible,young',
                      'tall: height,tall',
                      'taut: shape',
                      'thin: width,narrow',
                      'tight: size,small',
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
     
    def DescRandomNakedParts(self, iNum = 3, sDivideChar = ',', bPenis = True, bAss = True, bBody = True, bExplicit = False, bLongDesc = True, sPossessive = None):
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
                         ]

        if bBody:
            PartPriorities.append([body,6])
          
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