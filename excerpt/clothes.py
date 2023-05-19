#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Clothes module

from random import *
from util import *
from excerpt.ex_helpers import *

ClothesColors = WordList(['amber: color,fem',
                          'black x5: color',
                          'beige: color',
                          # ------ Blues ------
                          'blue x2: color',
                          'dark blue: color',
                          'navy blue: color',
                          'sky blue: color',
                          'baby blue: color,fem',
                          'pastel blue: color,fem',
                          # -------------------

                          # ------ Browns -----
                          'brown: color',
                          'chocolate brown: color',
                          # -------------------

                          'chartreuse: color,fem',
                          'cream-colored: color',
                          'gold: color',
                          # ----- Greens ------
                          'green x2: color',
                          'dark green: color',
                          'lime green: color',
                          'sea green: color',
                          'neon green: color',
                          'pastel green: color',
                          # -------------------

                          'indigo: color',
                          'lavender x2: color,fem',
                          'lilac: color,fem',
                          'magenta: color,fem',
                          'maroon: color',
                          'mauve: color,fem',
                          # ----- Oranges -----
                          'orange: color',
                          'neon orange: color',
                          # -------------------

                          'peach: color,fem',
                          'periwinkle: color,fem',
                          # ------ Pinks ------
                          'pink x4: color',
                          'hot pink x2: color',
                          # -------------------

                          'purple x3: color,fem',
                          # ------ Reds -------
                          'red x5: color',
                          'blood red: color',
                          'bright red: color',
                          'ruby red: color,fem',
                          # -------------------

                          'silver: color',
                          'turquoise: color,fem',
                          'violet x3: color,fem',
                          # ----- Yellows -----
                          'yellow: color',
                          'bright yellow: color',
                          'canary yellow: color',
                          'dayglow yellow: color',
                          'lemon yellow: color',
                          # -------------------

                          # ----- Whites ------
                          'white x2: color',
                          'pure white: color',
                          # -------------------
                         ])

class Clothes(NounPhrase):
    def __init__(self):
        super().__init__()

        self.IsTop = False
        self.IsBottom = False 
        self.IsDress = False
        self.IsUnderwear = False
        self.AddColors = True

        self.ColorsNotList = []

    # Override the AdjList creation call so we
    # can manually add the colors from the 
    # ClothesColors list to each adj list.
    def AdjList(self, NewAdjList):
        global ClothesColors 
        
        if self.AddColors:
            for color in ClothesColors.GetWordList():
                unit = self.ParseUnit(color)
                
                if not FoundIn(unit.sUnit, self.ColorsNotList):
                    if not self.Gender is None:
                       if self.Gender == "male" and not "fem" in unit.TagList:
                           NewAdjList.append(color)
                       elif self.Gender == "female":
                           NewAdjList.append(color)

        super().AdjList(NewAdjList)

# ***********************
# *** Female Clothing ***
# ***********************

class FemWardrobe():
    def __init__(self):
        # Tops

        self.BikiniTop = BikiniTop()
        self.Blouse = Blouse()
        self.Bra = Bra()
        self.CropTop = CropTop()
        self.Dress = Dress()
        self.EveningDress = EveningDress()
        self.Nightgown = Nightgown()
        self.PencilDress = PencilDress()
        self.Robe = RobeFemale()
        self.SportsBra = SportsBra()
        self.Tshirt = TshirtFemale()
        
        # Bottoms

        self.BikiniBottoms = BikiniBottoms()
        self.DaisyDukes = DaisyDukes()
        self.Jeans = JeansFemale()
        self.Panties = Panties()
        self.Pantyhose = Pantyhose()
        self.Shorts = ShortsFemale()
        self.ShortSkirt = ShortSkirt()
        self.YogaPants = YogaPants()

        # Combos & Dresses

        self.Bikini = Bikini()
        self.Underwear = UnderwearFemale()
        self.Workout = WorkoutFemale()

        # Other

        self.Heels = Heels()

        # Clothing pools

        self.Bottoms = [self.BikiniBottoms,self.DaisyDukes,self.Jeans,
                        self.Panties,self.Pantyhose,self.Shorts,
                        self.ShortSkirt,self.YogaPants
                       ]

        self.Dresses = [self.Dress,self.EveningDress,self.PencilDress]

        self.Tops = [self.BikiniTop, self.Blouse,self.Bra,self.CropTop,
                     self.Nightgown,self.Robe,self.SportsBra,self.Tshirt
                    ]

        self.Underwear = [self.Bra,self.Nightgown,self.Panties,
                          self.Robe,self.Tshirt,self.Underwear,]

    def GetBottom(self, NotList = None):
        if NotList is None:
            NotList = []

        Bottoms = self.Bottoms.copy()

        if len(NotList) > 0:
            Bottoms = self.ExclNotList(Bottoms, NotList)

        return choice(Bottoms)

    def GetTop(self, NotList = None, bDresses = False):
        if NotList is None:
            NotList = []

        Tops = self.Tops.copy()

        if bDresses:
            Tops = Tops + self.Dresses.copy()

        if len(NotList) > 0:
            Tops = self.ExclNotList(Tops, NotList)

        return choice(Tops)

    def ExclNotList(self, List, NotList):
        CleanList = []

        for litem in List:
            bInNL = False
            for nlitem in NotList:
                if litem == nlitem:
                    bInNL = True
                    break
            if not bInNL:
                CleanList.append(litem)

        return CleanList

class FemaleClothes(Clothes):
     def __init__(self):
          self.Gender = "female"
          super().__init__()

# --- Tops ---

class BikiniTop(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['bikini x4: default,std,sing',
                         'bikini top x2: default,std,sing',
                         'crocheted bikini: variant,material,sing',
                         'crocheted bikini top: variant,material,sing',
                         'spandex bikini: variant,material,sing',
                         'spandex bikini top: variant,material,sing',
                         'strapless bikini x3: variant,sing',
                        ])
          
          self.AdjList(['daring x2: skimpy',
                        'flimsy: skimpy',
                        'floral: pattern',
                        'hot: super',
                        'immodest: skimpy',
                        'leopard print: pattern',
                        'little: size,small',
                        'metallic: texture',
                        'microscopic: size,small',
                        'plaid: pattern',
                        'provocative: skimpy',
                        'polka-dot: pattern',
                        'racy: super,skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'scant: skimpy',
                        'sexy: super',
                        'sheer: seethru,texture,pattern,material,fetish',
                        'shocking: super',
                        'skimpy x2: skimpy',
                        'slender: size,small,skimpy',
                        'stringy: skimpy',
                        'stunning: super',
                        'teeny-tiny: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'translucent: texture,material',
                        'V-shaped x3: shape',
                        'vivid: super',
                       ])
               
          self.DefaultNoun('bikini top')
          self.DefaultAdj('skimpy')

          self.IsTop = True

class Blouse(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.NounList(['blouse x3: std,default,sing',
                         'shirt: std,sing',
                        ])
          
          self.AdjList(['ample: super',
                        'breezy: super',
                        'cropped: shape',
                        'cute: super',
                        'dainty: super',
                        'daring: super,skimpy',
                        'delicate: super',
                        'denim: material,color,texture',
                        'flimsy: thickness,thin',
                        'floral: pattern',
                        'flowered: pattern',
                        'frilly: style',
                        'lacy: material,pattern,texture',
                        'little x4: size,small',
                        'loose: shape',
                        'midriff-baring: shape,skimpy',
                        'modest: modest,skimpy,seethru,tight',
                        'open: shape',
                        'open-necked: shape',
                        'plaid: pattern,color',
                        'pleated: texture',
                        'polka-dot: pattern',
                        'pretty: super',
                        'prim: super,style',
                        'ruffled: style',
                        'scoop-neck: shape',
                        'see-thru: seethru',
                        'severe: style',
                        'sheer: seethru,texture,pattern,material',
                        'shiny: shiny,texture',
                        'short: length,short',
                        'silken: texture',
                        'sleeved: shape',
                        'sleeveless: shape',
                        'smooth: texture',
                        'snug: tight',
                        'soft: texture',
                        'strict: super,style',
                        'stunning: super',
                        'suggestive: super',
                        'tantalizing: super',
                        'thin: thickness,thin',
                        'tight: tight',
                        'unbuttoned: skimpy',
                        'V-necked: style',
                       ])
               
          self.DefaultNoun('blouse')
          self.DefaultAdj('prim')

          self.IsTop = True

class Bra(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.IsUnderwear = True
          
          self.NounList(['bra x5: default,std,sing',
                         'brassiere x3: std,sing',
                         'cupless bra: variant,fetish,sing',
                         'full-cup bra: variant,large,sing',
                         'full-cup brassiere: std,large,sing',
                         'Italian bra: variant,style,sing',
                         'pushup bra x2: variant,sing',
                         'strapless bra x2: variant,sing',
                         'Victoria\'s Secret bra: variant,style,sing',
                        ])
          
          self.AdjList(['ample: size,large,super',
                        'cute: super',
                        'daring: super',
                        'delicate: super',
                        'elegant: super',
                        'fancy: super',
                        'flowered: pattern',
                        'full: size,large',
                        'flimsy: material',
                        'frilly: pattern,style',
                        'lace: material,pattern',
                        'lacy: material,pattern',
                        'large: size,large',
                        'little: size,small',
                        'meager: size,small',
                        'miniscule: size,small',
                        'modest: style,large',
                        'padded: style',
                        'petite: size,small',
                        'provocative: super,skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'satin: material',
                        'seductive: super',
                        'sequined: style,pattern',
                        'sensuous: super',
                        'sexy: super',
                        'sheer: texture,seethru',
                        'silk: material,texture',
                        'silken: material,texture',
                        'skimpy: skimpy',
                        'soft: texture',
                        'stunning: super',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'wispy: small',
                       ])
               
          self.DefaultNoun('bra')
          self.DefaultAdj('skimpy')

          self.IsTop = True

class CropTop(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.NounList(['crop-top x3: std,default,sing',
                         'tube-top: variant,sing',
                        ])
          
          self.AdjList(['ample: super',
                        'belly-baring: shape',
                        'body-hugging: super,skimpy,tight',
                        'brazen: super',
                        'breezy: super',
                        'cleavage-baring: shape',
                        'crocheted: material,texture',
                        'cute: super',
                        'dainty: super',
                        'daring: super,skimpy',
                        'denim: material,color',
                        'exciting: super',
                        'eye-catching: super',
                        'flimsy: thickness,thin',
                        'frilly: style',
                        'hot: super',
                        'knitted: pattern,texture',
                        'lacy: material,pattern,texture',
                        'leopard-print: pattern,color',
                        'little x2: size,small',
                        'midriff-baring: shape',
                        'metallic: texture',
                        'off-shoulder: style,shape',
                        'petite: size,small',
                        'revealing: skimpy',
                        'sassy: super',
                        'sexy: super',
                        'sheer: seethru,texture,pattern,material',
                        'shiny: shiny',
                        'short: length,short',
                        'short-sleeved: shape',
                        'skimpy: skimpy',
                        'sleeveless: shape',
                        'snug: tight',
                        'strappy: style',
                        'stunning: super',
                        'tantalizing: super',
                        'thin: thickness,thin',
                        'tight: tight',
                        'tight-fitting: tight',
                        'tiny: tight,skimpy',
                       ])
               
          self.DefaultNoun('crop-top')
          self.DefaultAdj('midriff-baring')

          self.IsTop = True

class Dress(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True
          self.IsDress = True
          
          self.NounList(['dress x3: std,default,sing',
                         'minidress: variant,short,skimpy,sing',
                         'sleeveless dress: variant,shape,sing',
                         'strapless dress: variant,shape,sing',
                         'sundress: variant,sing',
                         'tropical dress: variant,sing',
                        ])
          
          self.AdjList(['ample: bigtits',
                        'backless: style',
                        'breezy: super',
                        'brief: size,small',
                        'brocaded: pattern,material',
                        'beautiful: super',
                        'cute: super',
                        'dainty: super',
                        'calico: pattern,color',
                        'clingy x2: tight',
                        'demure: modest,skimpy,seethru,tight',
                        'elegant: super',
                        'enchanting: super',
                        'fancy: super',
                        'fashionable: super',
                        'flared: shape',
                        'flimsy: super',
                        'flirty: super',
                        'floor-length: length,long',
                        'floral: pattern',
                        'flowered: pattern',
                        'flowing: long,shape',
                        'form-fitting: tight',
                        'frilly: style',
                        'girlish: super,style,young',
                        'gorgeous: super',
                        'high-waisted: style',
                        'knee-length: length,medium',
                        'lacy: pattern,material,texture',
                        'long: length,long',
                        'lovely: super',
                        'low-cut: shape,skimpy',
                        'modest: modest,skimpy,seethru,tight',
                        'plaid: pattern,color',
                        'pleated: texture',
                        'polka-dot: pattern',
                        'pretty: super',
                        'plunging: neckline',
                        'revealing: skimpy',
                        'ruffled: style',
                        'sassy: super',
                        'satin x2: material,texture',
                        'scandalous: super',
                        'scant: skimpy',
                        'scoop-neck: shape',
                        'see-thru: pattern,texture,seethru',
                        'sexy x4: super',
                        'sheer: seethru,texture,pattern,material',
                        'short: length,short',
                        'short-skirted: shape,skirt,length,short',
                        'silk x2: material',
                        'silken x2: material',
                        'simple: style',
                        'sizzling: super',
                        'skimpy x2: skimpy',
                        'sleazy: super,skimpy',
                        'slender x2: shape',
                        'soft: texture',
                        'striped: pattern',
                        'stunning: super',
                        'stylish: super',
                        'swirly: shape',
                        'tawdry: super,skimpy',
                        'thigh-length: length,short',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'V-necked: shape,',
                        'velvety: material,texture',
                        'vintage: style',
                        'wispy: pattern,texture,material',
                       ])
               
          self.DefaultNoun('dress')
          self.DefaultAdj('cute')

class EveningDress(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False
          self.IsDress = True
          
          self.NounList(['cocktail dress x2: std,sing',
                         'cocktail gown x2: std,sing',
                         'evening gown x2: std,default,sing',
                         'evening dress x2: std,sing',
                         'French evening dress: variant,style,sing',
                         'French mini dress: variant,style,sing',
                         'mini dress: variant,shape,sing',
                         'Parisian evening gown: variant,style,sing',
                         'sheath dress: variant,shape,sing',
                        ])
          
          self.AdjList(['alluring: super',
                        'audacious: super',
                        'backless: style',
                        'brief: size,small',
                        'black x4: color',
                        'chiffon: material',
                        'clingy x2: tight',
                        'crimson: color',
                        'diaphanous: seethru',
                        'elegant: super',
                        'fancy: super',
                        'fashionable: super',
                        'flared: shape',
                        'flimsy: super',
                        'floor-length: length,long',
                        'form-fitting: tight',
                        'frilly: style',
                        'glamorous: super',
                        'gold: color,material',
                        'gorgeous: super',
                        'jet-black: color',
                        'knee-length: length,medium',
                        'lacy x2: pattern,material',
                        'long: length,long',
                        'luxurious: style',
                        'mini: short,skimpy',
                        'plunging: neckline',
                        'provocative: super',
                        'red x3: color',
                        'revealing: skimpy',
                        'ruffled: style',
                        'satin x2: material,texture',
                        'scandalous: super',
                        'scant: skimpy',
                        'scarlet: color',
                        'seductive: super',
                        'see-thru: pattern,texture,seethru',
                        'sexy x4: super',
                        'sheer: seethru,texture,pattern,material',
                        'shimmering: shiny',
                        'short: length,short',
                        'short-skirted: shape,skirt,length,short',
                        'silk x2: material',
                        'silken x2: material',
                        'silver: color,material',
                        'skimpy x2: skimpy',
                        'slender x2: shape',
                        'slinky x4: super',
                        'slit: shape',
                        'sequined: material',
                        'sparkling: shiny',
                        'stunning: super',
                        'thigh-length: length,short',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'translucent: seethru,texture',
                        'V-necked: shape,',
                        'velvet: material',
                        'voluptuous: shape,bust',
                       ])
               
          self.DefaultNoun('evening gown')
          self.DefaultAdj('sexy')

class Nightgown(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.IsUnderwear = True

          self.NounList(['babydoll x2: variant,lingerie,sing',
                         'chemise x2: variant,sing',
                         'negligee x4: variant,lingerie,sing',
                         'nightgown x4: std,default,sing',
                         'satin babydoll: variant,lingerie,material,sing',
                         'satin chemise: variant,material,sing',
                         'satin negligee: variant,lingerie,material,sing',
                         'satin nightgown: std,material,sing',
                         'satin shift: variant,material,sing',
                         'silk babydoll: variant,lingerie,material,silk,sing',
                         'silk chemise: variant,material,silk,sing',
                         'silk negligee: variant,lingerie,material,silk,sing',
                         'silk nightgown: std,material,silk,sing',
                         'silk shift: variant,material,silk,sing',
                         'shift: variant,sing',
                        ])
          
          self.AdjList(['brief: size,small',
                        'beautiful: super',
                        'cute: super',
                        'dainty: super',
                        'delicate: super',
                        'diaphanous: seethru,thickness,thin',
                        'embroidered: style',
                        'exquisite: super',
                        'flimsy: thickness,thin',
                        'frilly x3: style',
                        'gauzy: thickness,thin',
                        'gossamer: texture,thin,shiny,seethru',
                        'intimate: super,skimpy',
                        'lace: texture,material',
                        'lacy: texture',
                        'little: size,small',
                        'loose: style',
                        'naughty: super',
                        'old-fashioned: style',
                        'paper-thin: thickness,thin',
                        'pretty: super',
                        'provocative: skimpy',
                        'racy: super,skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'scant: skimpy',
                        'seductive: super',
                        'see-thru: pattern,texture,seethru',
                        'sexy x2: super',
                        'sheer: seethru,texture,pattern,material',
                        'short: length,short',
                        'silken: texture,silk',
                        'silky: texture,silk',
                        'simple: style,super',
                        'slinky: super,skimpy',
                        'skimpy: skimpy',
                        'suggestive: super,skimpy',
                        'thigh-length: length,medium',
                        'thin x4: thickness,thin',
                        'wispy: super,small',
                       ])
               
          self.DefaultNoun('nightgown')
          self.DefaultAdj('lacy')

          self.IsTop = True

class PencilDress(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False
          self.IsDress = True
          
          self.NounList(['pencil dress: variant,tight,slender,sing',
                        ])
          
          self.AdjList(['black x3: color',
                        'beige: color',
                        'businesslike x3: super',
                        'cream-colored: color',
                        'dark gray: color',
                        'demure: modest,skimpy,seethru,tight',
                        'elegant: super',
                        'fashionable: super',
                        'form-fitting x2: tight',
                        'gorgeous: super',
                        'gray x2: color',
                        'high-waisted: style',
                        'hip-hugging: tight',
                        'knee-length: length,medium',
                        'low-cut: shape,skimpy',
                        'modest: modest,skimpy,seethru,tight',
                        'pleated: texture',
                        'ruffled: style',
                        'sassy: super',
                        'satin x2: material,texture',
                        'severe: super',
                        'sexy x2: super',
                        'sharp: super',
                        'short: length,short',
                        'short-skirted: shape,skirt,length,short',
                        'silk x2: material',
                        'silken x2: material',
                        'sizzling: super',
                        'slender x2: shape',
                        'sleek: super',
                        'soft: texture',
                        'striped: pattern',
                        'stunning: super',
                        'stylish: super',
                        'tan: color',
                        'thigh-length: length,short',
                        'tight x2: size,small',
                        'white: color',
                       ])
               
          self.DefaultNoun('pencil dress')
          self.DefaultAdj('businesslike')

class RobeFemale(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.ColorsNotList = ["black"]

          self.NounList(['bathrobe x3: variant,sing',
                         'kimono: variant,sing',
                         'robe x4: std,default,sing',
                         'satin bathrobe: std,material,sing',
                         'satin robe x2: std,material,sing',
                         'silk robe x2: std,material,silk,sing',
                        ])
          
          self.AdjList(['beautiful: super',
                        'clingy: skimpy',
                        'comfortable: texture',
                        'cozy: texture,thick',
                        'diaphanous: seethru,thickness,thin',
                        'embroidered: style',
                        'flimsy: thickness',
                        'flowered: style',
                        'gauzy: thickness,thin',
                        'glossy: texture,shiny',
                        'gossamer: texture,thin,shiny,seethru',
                        'light: thickness,thin',
                        'long: length,long',
                        'loose: style',
                        'paper-thin: thickness,thin',
                        'plush: texture,material,thick',
                        'silken: texture,silk',
                        'silky: texture,silk',
                        'simple: style,super',
                        'short: length,short',
                        'soft: texture',
                        'thick: thickness,thick'
                        'thin x4: thickness,thin',
                        'tightly-wrapped: style',
                        'warm: feel,thick',
                       ])
               
          self.DefaultNoun('robe')
          self.DefaultAdj('loose robe')

          self.IsTop = True

class SportsBra(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.IsUnderwear = True
          
          self.NounList(['lycra sports bra: variant,material,sing',
                         'microfiber sports bra: variant,material,sing',
                         'racerback sports bra: variant,style,shape,sing',
                         'spandex sports bra: variant,material,sing',
                         'sports bra x4: default,std,sing',
                        ])
          
          self.AdjList(['athletic: style',
                        'cute: super',
                        'daring: super',
                        'flimsy: material',
                        'high-impact: super',
                        'large: size,large',
                        'petite: size,small',
                        'provocative: super,skimpy',
                        'revealing: skimpy',
                        'sexy: super',
                        'sleek: texture',
                        'skimpy: skimpy',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'tight x2: size,small,tight',
                        'tightly-fitted: tight',
                        'tiny x3: size,small',
                        'zip-up: style',
                       ])
               
          self.DefaultNoun('sports bra')
          self.DefaultAdj('black')

          self.IsTop = True

class TshirtFemale(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False

          self.NounList(['t-shirt x4: default,std,sing',
                         'cotton t-shirt: std,material,sing',
                         'cotton tee: std,material,sing',
                         'cut-off t-shirt: variant,style,shape',
                         'cut-off tee: variant,style,shape',
                         'v-neck t-shirt: variant,style,shape',
                         'v-neck tee: variant,style,shape',
                         'white cotton t-shirt: std,material,color,sing',
                         'white cotton tee: std,material,color,sing',
                        ])
          
          self.AdjList(['baby blue: color',
                        'casual: style',
                        'clingy: skimpy',
                        'comfortable: texture',
                        'diaphanous: seethru',
                        'faded: color',
                        'flimsy: thickness',
                        'large: size,large',
                        'loose: size,large,thin',
                        'midriff-baring: style,shape',
                        'old: distressed',
                        'oversized: size,large',
                        'paper-thin: thickness',
                        'pink: color',
                        'see-thru: seethru',
                        'sexy: super',
                        'simple: style',
                        'skimpy: skimpy',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'thin x4: thickness',
                        'tight x3: size,small,tight',
                        'tiny x3: size,small',
                        'white x3: color',
                        'plain white: color',
                        'yellow: color',
                       ])
               
          self.DefaultNoun('t-shirt')
          self.DefaultAdj('white')

          self.IsTop = True


# --- Bottoms ---

class BikiniBottoms(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['bikini bottoms x4: default,std,plur',
                         'Brazilian bikini bottoms: std,plur',
                         'crocheted bikini bottoms: variant,material,plur',
                         'crotchless bikini bottoms: variant,seethru,fetish,plur',
                         'G-string x3: variant,sing',
                         'spandex bikini bottoms: variant,material,plur',
                         'string bikini bottoms: variant,plur',
                         'thong x4: std,sing',
                        ])
          
          self.AdjList(['cheeky: super',
                        'daring x2: skimpy',
                        'flimsy: skimpy',
                        'floral: pattern',
                        'hot: super',
                        'immodest: skimpy',
                        'leopard print: pattern,color',
                        'little: size,small',
                        'metallic: texture',
                        'microscopic: size,small',
                        'narrow: size,small',
                        'plaid: pattern',
                        'provocative: skimpy',
                        'polka-dot: pattern',
                        'racy: super,skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'scant: skimpy',
                        'sexy: super',
                        'sheer: seethru,texture,pattern,material',
                        'shocking: super',
                        'skimpy x2: skimpy',
                        'slender: size,small,skimpy',
                        'stretchy: stretchy',
                        'stunning: super',
                        'teeny-tiny: size,small',
                        'thin: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'V-shaped x3: shape',
                        'vivid: super',
                       ])
               
          self.DefaultNoun('bikini top')
          self.DefaultAdj('skimpy')

          self.IsBottom = True

class DaisyDukes(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 

          self.NounList(['cutoff shorts: std,default,plur',
                         'Daisy Dukes: std,plur',
                         'denim cutoff shorts: std,material,plur',
                         'bluejean shorts: std,color,plur',
                         'jean shorts: std,plur',
                        ])
          
          self.AdjList(['brief: size,small',
                        'cheeky: skimpy',
                        'clingy: tight',
                        'crotch-length: length,short',
                        'cute: super',
                        'dainty: super',
                        #'denim x2: material',
                        'faded x2: color',
                        'flimsy: super',
                        'frayed: distressed',
                        'hip-hugging: tight',
                        'hot: super',
                        'little x4: size,small',
                        'microscopic: size,small,tight',
                        'provocative: skimpy',
                        'revealing: skimpy',
                        'ripped: distressed',
                        'sexy x2: super',
                        'skimpy x2: skimpy',
                        'snug x2: tight',
                        'teeny: size,small',
                        'teeny-tiny: tight',
                        'thigh-length: length,medium',
                        'tight x2: tight',
                        'tiny x3: tight',
                        'torn: distressed',
                       ])
               
          self.DefaultNoun('cutoff shorts')
          self.DefaultAdj('denim')

          self.IsBottom = True

class JeansFemale(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 

          self.NounList(['bluejeans x3: std,color,default,plur',
                         'jeans x3: std,plur',
                         'denim jeans: std,material,plur',
                         'denim bluejeans: std,material,color,plur',
                        ])
          
          self.AdjList(['bell-bottomed: style,shape',
                        'clingy: tight,fit',
                        'faded x2: color',
                        'flared: shape,style',
                        'form-fitting: tight,fit',
                        'frayed: distressed',
                        'hip-hugging: tight,fit',
                        'leggy: super',
                        'low-slung: fit',
                        'ripped: distressed',
                        'skinny: slender,shape',
                        'skintight: tight,fit',
                        'snug x2: tight,fit',
                        'tight x2: tight,fit',
                        'tight-fitted: tight,fit',
                        'torn: distressed',
                        'unbuttoned: style',
                        'unzipped: style',
                       ])
               
          self.DefaultNoun('bluejeans')
          self.DefaultAdj('tight')

          self.IsBottom = True

class Panties(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.IsUnderwear = True

          self.ColorsNotList = ["gold","silver"]
          
          self.NounList(['cotton panties: std,material,plur',
                         'French panties: variant,style,plur',
                         'G-string panties: variant,plur',
                         'Japanese panties: variant,style,plur',
                         'panties x4: default,std,plur',
                         'silk panties x2: variant,material,plur',
                         'thong: variant,sing',
                         'thong underwear: variant,sing',
                         'white cotton panties: std,material,color,plur',
                         'underwear x2: std,sing',
                        ])
          
          self.AdjList(['brief: size,small',
                        'cheeky: skimpy',
                        'cute: super',
                        'dainty: super',
                        'delicate: super',
                        'diaphanous: seethru',
                        'fancy: super',
                        'flimsy: super',
                        'flowered: pattern',
                        'frilly x3: style',
                        'gossamer: texture,material',
                        'lace x2: pattern,material',
                        'lacey x4: pattern,material',
                        'leopard print: pattern,color',
                        'little x4: size,small',
                        'naughty: super',
                        'nylon: material',
                        'plain: style,pattern',
                        'polka-dotted: pattern',
                        'pretty: super',
                        'provocative: skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'satin x3: material,texture',
                        'scant: skimpy',
                        'see-thru: pattern,texture,seethru',
                        'sexy x2: super',
                        'sheer: seethru,texture,pattern,material',
                        #'silk x3: material',
                        'silken x2: material',
                        'skimpy x2: skimpy',
                        'soft: feel,texture',
                        'teeny-tiny: size,small',
                        'thin: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'wispy: super,small',
                       ])
               
          self.DefaultNoun('panties')
          self.DefaultAdj('little')

          self.IsBottom = True

class Pantyhose(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.AddColors = False
          self.IsBottom = True
          self.IsUnderwear = True
          
          self.NounList(['fishnets: variant,plur',
                         'French nylons: variant,plur',
                         'French pantyhose: variant,sing',
                         'French stockings: variant,plur',
                         'lace pantyhose: variant,material,texture,lace,sing',
                         'lace tights: variant,material,texture,lace,plur',
                         'nylons x3: std,material,plur',
                         'pantyhose x4: std,default,sing',
                         'silk pantyhose: std,material,silk,sing',
                         'sheer tights: std,seethru,plur',
                         'silk stockings: variant,material,silk,plur',
                         'stockings: variant,plur',
                        ])
          
          self.AdjList(['beige x3: color',
                        'black x3: color',
                        'brief: length,shape',
                        'creamy: color',
                        'dark: color',
                        'flawless: super',
                        'flimsy: thickness,thin',
                        'form-fitting: tight',
                        'glossy x4: shiny,texture',
                        'gray: color',
                        'hip-hugging: tight',
                        'long: length,long',
                        'pink: color',
                        'scarlet: color',
                        'seamless: style',
                        'sexy: super',
                        'sheer x4: seethru',
                        'shiny: shiny',
                        'silken: texture,silk',
                        'silky: texture,silk',
                        'skintight: tight',
                        'sleek: texture',
                        'slender: slender',
                        'smooth: texture',
                        'snug: tight',
                        'soft: texture',
                        'stretchy: stretchy',
                        'svelte x2: super',
                        'taut: tight',
                        'thin: thickness,thin',
                        'tight x2: size,small,tight',
                        'tightly-fitted: tight',
                        'transparent: seethru',
                        'waist-high: length,shape',
                        'white: color',
                       ])
               
          self.DefaultNoun('pantyhose')
          self.DefaultAdj('glossy')

class ShortsFemale(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.ColorsNotList = ["gold","silver"]
          
          self.NounList(['booty shorts: variant,plur',
                         'hotpants: variant,plur',
                         'running shorts: variant,plur',
                         'short shorts: std,default,plur',
                         'spandex shorts: variant,plur',
                        ])
          
          self.AdjList(['brief: size,small',
                        'cheeky: skimpy',
                        'clingy: tight',
                        'crotch-length: length,short',
                        'cute: super',
                        'dainty: super',
                        'flimsy: super',
                        'hip-hugging: tight',
                        'hot: super',
                        'little x4: size,small',
                        'microscopic: size,small,tight',
                        'petite: size,small',
                        'provocative: skimpy',
                        'revealing: skimpy',
                        'sexy x2: super',
                        'skimpy x2: skimpy',
                        'skintight: tight',
                        'snug x2: tight',
                        'sporty: super',
                        'striped: pattern',
                        'teeny: size,small',
                        'teeny-tiny: tight',
                        'thigh-length: medium',
                        'tight x2: tight',
                        'tiny x3: tight',
                       ])
               
          self.DefaultNoun('short shorts')
          self.DefaultAdj('snug')

          self.IsBottom = True

class ShortSkirt(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True
          self.IsBottom = True
          
          self.NounList(['bubble skirt: variant,sing',
                         'denim skirt: variant,denim,material,sing',
                         'leather skirt: variant,leather,material,sing',
                         'microskirt: variant,short,sing',
                         'miniskirt x2: variant,short,sing',
                         'short skirt x2: std,short,sing',
                         'skirt x4: std,default,sing',
                        ])
          
          self.AdjList(['abbreviated: skimpy',
                        'breezy: super',
                        'brief: skimpy',
                        'crisp: super',
                        'cute: super',
                        'clingy: tight',
                        'cute: super',
                        'dainty: super',
                        'delightful: super',
                        'denim: material,color,texture',
                        'flirtatious: super',
                        'floral: pattern',
                        'flowered x2: pattern',
                        'form-fitting: tight',
                        'frilly: style',
                        'girly: super,young',
                        'high-waisted: style',
                        'hip-hugging: tight',
                        'hot: super',
                        'linen: material',
                        'little x4: size,small',
                        'metallic: texture,material',
                        'narrow: width,narrow,tight',
                        'petite: size,small',
                        'plaid: pattern,color',
                        'pleated x3: texture,style',
                        'polka-dot: pattern',
                        'pretty: super',
                        'prim: super',
                        'ruffled: style',
                        'sexy x2: super',
                        'silken: texture,material',
                        'slim: width,narrow,tight',
                        'slinky: super,skimpy',
                        'slitted: stle',
                        'snug x2: tight',
                        'striped: pattern',
                        'suggestive: super',
                        'tantalizing: super',
                        'tasteful: super,modest',
                        'thigh-length: length,short',
                        'thin: thickness,thin',
                        'teeny: size,small',
                        'teeny-tiny: tight',
                        'thigh-length: medium',
                        'tight x2: tight',
                        'tiny x3: tight',
                        'wool: material',
                       ])
               
          self.DefaultNoun('skirt')
          self.DefaultAdj('snug')

class YogaPants(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.ColorsNotList = ['white','cream']
          
          self.NounList(['leggings x3: std,plur',
                         'Lululemon yoga pants: variant,style,plur',
                         'lycra yoga pants: variant,material,plur',
                         'microfiber yoga pants: variant,material,plur',
                         'spandex leggings: variant,material,plur',
                         'spandex yoga pants: variant,material,plur',
                         'yoga pants x4: std,default,plur',
                        ])
          
          self.AdjList(['athletic: style',
                        'body-hugging: tight',
                        'clingy: tight',
                        'cute: super',
                        'daring: super',
                        'figure-hugging: tight',
                        'form-fitting: tight',
                        'hip-hugging: tight',
                        'sexy: super',
                        'skintight: tight',
                        'sleek: texture',
                        'slender: slender',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'stretchy: stretchy',
                        'svelte: super',
                        'tight x2: size,small,tight',
                        'tightly-fitted: tight',
                       ])
               
          self.DefaultNoun('yoga pants')
          self.DefaultAdj('form-fitting')

          self.IsBottom = True


# --- Combos and Dresses ---

class Bikini(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['bikini x4: default,std,sing',
                         'crocheted bikini: variant,material,sing',
                         'Brazilian bikini: variant,sing',
                         'French bikini: variant,sing',
                         'sling bikini: variant,sing',
                         'spandex bikini: variant,material,sing',
                         'strapless bikini: variant,sing',
                         'string bikini: std,sing',
                         'two-piece bathing suit: std,sing',
                        ])
          
          self.AdjList(['daring x2: skimpy',
                        'eye-watering: super',
                        'flimsy: skimpy',
                        'floral: pattern',
                        'heart-shaped: shape',
                        'hot: super',
                        'immodest: skimpy',
                        'leopard print: pattern, color',
                        'little: size,small',
                        'metallic: texture',
                        'microscopic: size,small',
                        'plaid: pattern',
                        'provocative: skimpy,super',
                        'polka-dot: pattern',
                        'racy: super,skimpy',
                        'revealing: skimpy,super',
                        'risqué: skimpy,super',
                        'ruffled: style',
                        'scant: skimpy',
                        'sexy: super',
                        'sheer: seethru,texture,pattern,material',
                        'skimpy x2: skimpy',
                        'striped: pattern',
                        'stunning: super',
                        'teeny-tiny: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'vivid: super',
                       ])
               
          self.DefaultNoun('bikini')
          self.DefaultAdj('tiny')

          self.Bottoms = BikiniBottoms()
          self.Top = BikiniTop()

class UnderwearFemale(FemaleClothes):
     def __init__(self):
          super().__init__()

          self.IsUnderwear = True
          
          self.NounList(['bra and panties: std,plur',
                         'lingerie x2: std,sing',
                         'underclothes: std,plur',
                         'underwear x4: std,default,sing',
                         'undies: slang,plur',
                        ])
          
          self.AdjList(['alluring: super',
                        'brief: size,small',
                        'cheeky: skimpy',
                        'cotton x2: material',
                        'cute: super',
                        'dainty: super',
                        'delicate: super',
                        'diaphanous: seethru',
                        'elaborate: super',
                        'elegant: super',
                        'erotic: super,fetish',
                        'fancy: super',
                        'flimsy: super',
                        'flowered: pattern',
                        'French: style',
                        'frilly: style',
                        'glamorous: super',
                        'intimate: super',
                        'Italian: style',
                        'Japanese: style',
                        'lace x2: pattern,material',
                        'lacey x2: pattern,material',
                        'leopard print: pattern',
                        'luxurious: style',
                        'naughty: super',
                        'nylon: material',
                        'Parisian: style',
                        'plain: style,pattern',
                        'polka-dotted: pattern',
                        'pretty: super',
                        'provocative: skimpy',
                        'racy: skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'satin x2: material,texture',
                        'scant: skimpy',
                        'seductive: super',
                        'see-thru: pattern,texture,seethru',
                        'sexy x4: super',
                        'sheer: seethru,texture,pattern,material',
                        'silk x2: material',
                        'silken x2: material',
                        'skimpy x2: skimpy',
                        'slinky: super',
                        'soft: feel,texture',
                        'teeny-tiny: size,small',
                        'thin: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                       ])
               
          self.DefaultNoun('underwear')
          self.DefaultAdj('sexy')

          self.Bra = Bra()
          self.Panties = Panties()

class WorkoutFemale(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['activewear',
                         'gym clothes: std,plur',
                         'Lululemons: style,brand,plur',
                         'workout clothes: std,default,plur',
                         'workout wear: std,sing',
                        ])
          
          self.AdjList(['body-hugging: tight',
                        'figure-hugging: tight',
                        'form-fitting: tight',
                        'sexy: super',
                        'skin-tight: tight',
                        'spandex: material',
                        'tight: tight,small',
                       ])
               
          self.DefaultNoun('workout clothes')
          self.DefaultAdj('skin-tight')

          self.Top = SportsBra()
          self.Bottom = YogaPants()


# --- Other ---

class Heels(FemaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True

          self.NounList(['French heels: variant,style,plur',
                         'four-inch heels: variant,length,plur',
                         'heels x2: std,plur',
                         'high heels x3: std,default,plur',
                         'pumps: variant,plur',
                         'six-inch heels: variant,length,plur',
                         'stiletto heels: variant,plur',
                        ])
          
          self.AdjList(['dainty: super',
                        'fashionable: super',
                        'French: style',
                        'lethal: super',
                        'outrageous: super',
                        'sequined: material',
                        'sexy x4: super',
                        'sleek: super,slender,shape',
                        'slender: slender,shape',
                        'slim: slender,shape',
                        'sparkling: shiny',
                        'spiked: shape',
                        'strappy: style',
                        'stylish: super',
                        'tall: tall',
                        'towering: tall,super',
                       ])
               
          self.DefaultNoun('high heels')
          self.DefaultAdj('red')

          self.IsTop = True

# ***********************
# *** Male Clothing ***
# ***********************

class MaleWardrobe():
    def __init__(self):
        # Tops

        self.Tshirt = TshirtMale()
        
        # Bottoms

        self.Boxers = Boxers()
        self.Briefs = Briefs()
        self.Jeans = JeansMale()
        self.Khakis = Khakis()
        self.Slacks = Slacks()
        self.Speedo = Speedo()
        self.Thong = ThongMale()
        self.Trunks = SwimTrunks()

        # Clothing pools

        self.Bottoms = [self.Boxers,
                        self.Briefs,
                        self.Jeans,
                        self.Khakis,
                        self.Slacks,
                        self.Speedo,
                        self.Thong,
                        self.Trunks,
                       ]

        self.Tops = [self.Tshirt,
                    ]

        self.Trousers = [self.Jeans,self.Khakis,self.Slacks]

        self.Underwear = [self.Boxers,
                          self.Briefs,
                          self.Thong,
                         ]

    def GetBottom(self, NotList = None):
        if NotList is None:
            NotList = []

        Bottoms = self.Bottoms.copy()

        if len(NotList) > 0:
            Bottoms = self.ExclNotList(Bottoms, NotList)

        return choice(Bottoms)

    def GetTop(self, NotList = None, bDresses = False):
        if NotList is None:
            NotList = []

        Tops = self.Tops.copy()

        if len(NotList) > 0:
            Tops = self.ExclNotList(Tops, NotList)

        return choice(Tops)

    def GetTrousers(self, NotList = None):
        if NotList is None:
            NotList = []

        Trousers = self.Trousers.copy()

        if len(NotList) > 0:
            Trousers = self.ExclNotList(Trousers, NotList)

        return choice(Trousers)

    def GetUnderwear(self, NotList = None):
        if NotList is None:
            NotList = []

        Underwears = self.Underwear.copy()

        if len(NotList) > 0:
            Underwears = self.ExclNotList(Underwears, NotList)

        return choice(Underwears)

    def ExclNotList(self, List, NotList):
        CleanList = []

        for litem in List:
            bInNL = False
            for nlitem in NotList:
                if litem == nlitem:
                    bInNL = True
                    break
            if not bInNL:
                CleanList.append(litem)

        return CleanList

# --- Tops ---

class MaleClothes(Clothes):
     def __init__(self):
          self.Gender = "male"
          super().__init__()

class TshirtMale(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True

          self.NounList(['athletic tee: variant,sing',
                         'band shirt: variant,style,sing',
                         'cotton t-shirt: std,material,sing',
                         'cotton tee: std,material,sing',
                         'cut-off t-shirt: variant,style,shape',
                         'cut-off tee: variant,style,shape',
                         'heavy metal t-shirt: variant,style,sing',
                         't-shirt x4: default,std,sing',
                         'v-neck t-shirt: variant,style,shape',
                         'v-neck tee: variant,style,shape',
                         'white cotton t-shirt: std,material,color,sing',
                         'white cotton tee: std,material,color,sing',
                        ])
          
          self.AdjList(['casual: style',
                        'clingy: skimpy',
                        'comfortable: texture',
                        'damp: dirty',
                        'faded: distressed',
                        'large: size,large',
                        'loose: size,large,thin',
                        'midriff-baring: style,shape',
                        'old: distressed',
                        'oversized: size,large',
                        'pristine: dirty',
                        'sexy: super',
                        'simple: style',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'sweaty: dirty,wet',
                        'thin x4: thickness',
                        'tight x3: size,small,tight',
                        'torn: distressed',
                        'plain white x4: color,style',
                       ])
               
          self.DefaultNoun('t-shirt')
          self.DefaultAdj('plain white')

          self.IsTop = True

# --- Bottoms ---

class Boxers(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True 
          self.IsBottom = True
          self.IsUnderwear = True

          self.NounList(['boxers: std,default,plur',
                        ])
          
          self.AdjList(['baggy: loose, shape',
                        'brief: skimpy,tight',
                        'bulging: bigdick,shape',
                        'cotton: material',
                        'flimsy: skimpy',
                        'gingham: pattern',
                        'loose: fit',
                        'paper-thin: thickness,thin',
                        'plaid: pattern',
                        'polka-dotted: pattern',
                        'see-thru: see-thru,skimpy',
                        'sexy: super',
                        'short: length,short',
                        'silk: material,silk',
                        'snug: tight',
                        'soft: feel',
                        'soggy: wet',
                        'striped: pattern',
                        'taut: tight',
                        'thin: thickness,thin',
                        'tight x2: tight',
                        'woven: texture',
                       ])
               
          self.DefaultNoun('boxers')
          self.DefaultAdj('snug')

class Briefs(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 
          self.IsUnderwear = True
          self.IsBottom = True

          self.NounList(['boxer briefs: variant,plur',
                         'briefs x3: std,default,plur',
                         'underwear x2: std,sing',
                        ])
          
          self.AdjList(['black x2: color',
                        'brief: skimpy,tight',
                        'bulging: bigdick,shape',
                        'clingy: tight',
                        'cotton: material',
                        'flimsy: skimpy',
                        'little: size,small',
                        'meager: skimpy',
                        'mesh: texture,material',
                        'microscopic: size,small',
                        'plain white: style,color',
                        'red: color',
                        'seductive: super',
                        'see-thru: seethru,skimpy',
                        'sexy: super',
                        'skimpy: skimpy',
                        'slender: width,narrow',
                        'snug: tight',
                        'spandex: material',
                        'taut: tight',
                        'thin: thickness,thin',
                        'tight x2: tight',
                        'tiny: size,small,skimpy',
                        'V-shaped: shape',
                        'white x4: color',
                       ])
               
          self.DefaultNoun('briefs')
          self.DefaultAdj('plain white')

          self.IsBottom = True

class JeansMale(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 

          self.NounList(['bluejeans x3: std,color,default,plur',
                         'jeans x3: std,plur',
                         'denim jeans: std,material,plur',
                         'denim bluejeans: std,material,color,plur',
                        ])
          
          self.AdjList(['baggy: loose, shape',
                        'crisp: style',
                        'dusty: dirty',
                        'faded x2: color',
                        'frayed: distressed',
                        'loose: fit',
                        'low-slung: style',
                        'ragged: distressed',
                        'ripped: distressed',
                        'skinny: slender,shape',
                        'snug x2: tight',
                        'tight x2: tight',
                        'tight-fitted: tight',
                        'torn: distressed',
                        'unbuttoned: style',
                        'unzipped: style',
                        'well-worn: distressed',
                        'worn: distressed',
                       ])
               
          self.DefaultNoun('bluejeans')
          self.DefaultAdj('faded')

          self.IsBottom = True

class Khakis(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 

          self.NounList(['khakis: std,default,plur',
                        ])
          
          self.AdjList(['baggy: fit,loose,shape',
                        'beige x2: color',
                        'business-like: super,style',
                        'casual: super,style',
                        'comfortable: super',
                        'confident: super',
                        'crisp: style',
                        'fitted: style',
                        'gray x3: color',
                        'long: length,long',
                        'loose: fit,loose,shape',
                        'navy blue x2: color',
                        'neat: super',
                        'pleated: style',
                        'pressed: style',
                        'sharp: super',
                        'silver x2: color',
                        'skinny: slender,shape',
                        'slim: slender,shape',
                        'snug x2: tight',
                        'stylish: super',
                        'tailored: super',
                        'tall: super',
                        'tan: color',
                        'tapered: style',
                        'tight x2: tight',
                        'tight-fitted: tight',
                        'trim: slender',
                        'unbuttoned: style',
                        'unzipped: style',
                       ])
               
          self.DefaultNoun('bluejeans')
          self.DefaultAdj('faded')

          self.IsBottom = True

class Slacks(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = False 

          self.NounList(['chinos: variant,plur',
                         'dress pants: std,plur',
                         'slacks x2: std,default,plur',
                         'suit pants: variant,plur',
                         'trousers: std,plur',
                        ])
          
          self.AdjList(['beige x2: color',
                        'black x2: color',
                        'brown: color',
                        'business-like: super',
                        'confident: super',
                        'crisp: style',
                        'dark gray x3: color',
                        'fitted: style',
                        'fine: super',
                        'gray x3: color',
                        'long: length,long',
                        'navy blue x2: color',
                        'pleated: style',
                        'pressed: style',
                        'sharp: super',
                        'silver x2: color',
                        'skinny: slender,shape',
                        'slim: slender,shape',
                        'snug x2: tight',
                        'tailored: super',
                        'tall: super',
                        'tan x2: color',
                        'tapered: style',
                        'tight x2: tight',
                        'tight-fitted: tight',
                        'trim: slender',
                        'unbuttoned: style',
                        'unzipped: style',
                        'white: color',
                       ])
               
          self.DefaultNoun('bluejeans')
          self.DefaultAdj('faded')

          self.IsBottom = True

class Speedo(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True 

          self.NounList(['speedo: std,default,sing',
                         'speedos: std,plur',
                         'swim briefs: std,plur',
                         'thong: std,sing',
                        ])
          
          self.AdjList(['brief: skimpy,tight',
                        'bulging: bigdick,shape',
                        'clingy: tight',
                        'damp: wet',
                        'flashy: super',
                        'flimsy: skimpy',
                        'little: size,small',
                        'nylon: material',
                        'sexy: super',
                        'sleek: super',
                        'slender: width,narrow',
                        'slick: super',
                        'snug: tight',
                        'spandex: material',
                        'taut: tight',
                        'thin: thickness,thin',
                        'tight x2: tight',
                        'tiny: size,small,skimpy',
                       ])
               
          self.DefaultNoun('speedo')
          self.DefaultAdj('tight')

          self.IsBottom = True

class SwimTrunks(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True 

          self.NounList(['bathing suit: std,sing',
                         'boardshorts x2: variant,plur',
                         'swim shorts: std,plur',
                         'swimsuit: std,sing',
                         'swim trunks x3: std,default,plur',
                        ])
          
          self.AdjList(['baggy: loose, shape',
                        'brief: skimpy,tight',
                        'bulging: bigdick,shape',
                        'clingy: tight',
                        'damp: wet',
                        'flashy: super',
                        'flimsy: skimpy',
                        'knee-length: length,long',
                        'loose: fit',
                        'nylon: material',
                        'polyester: material',
                        'see-thru: see-thru,skimpy',
                        'sleek: super',
                        'slick: super',
                        'short: length,short',
                        'snug: tight',
                        'soggy: wet',
                        'square-cut: style,shape',
                        'thin: thickness,thin',
                        'tight x2: tight',
                        'tropical: style',
                       ])
               
          self.DefaultNoun('swim trunks')
          self.DefaultAdj('snug')

          self.IsBottom = True

class ThongMale(MaleClothes):
     def __init__(self):
          super().__init__()
          
          self.AddColors = True 
          self.IsBottom = True
          self.IsUnderwear = True

          self.NounList(['G-string: std,sing',
                         'man-thong: std,sing',
                         'thong x3: std,default,sing',
                        ])
          
          self.AdjList(['brief: skimpy,tight',
                        'bulging: bigdick,shape',
                        'cheeky: skimpy',
                        'clingy: tight',
                        'cotton: material',
                        'flashy: super',
                        'flimsy: skimpy',
                        'leopard print: pattern,color',
                        'little x3: size,small',
                        'nylon: material',
                        'sexy: super',
                        'sheer: seethru,texture,pattern,material',
                        'silk: material',
                        'sleek: super',
                        'slender: width,narrow',
                        'slick: super',
                        'snug: tight',
                        'spandex: material',
                        'T-backed: shape',
                        'taut: tight',
                        'thin: thickness,thin',
                        'tight x4: tight',
                        'tiny: size,small,skimpy',
                       ])
               
          self.DefaultNoun('thong')
          self.DefaultAdj('tight')

          

# TODO:
#   x high heels
#   X blouse
#   X skirt
#   X robe/nightgown/negligee/shift(/kimono?)
#   X Male blue jeans
#   X Male boxers
#   X Male briefs
#   - Male suit
#   X Male swimsuit
#   X Trousers/Slacks
#   - Button-down shirt
#   X Khakis
#   - Tank top
#   - Leather pants