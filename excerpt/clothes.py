#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Clothes module

from random import *
from util import *
from excerpt.bodyparts import *

ClothesColors = WordList(['black x5: color',
                          'beige: color',
                          # ------ Blues ------
                          'blue x2: color',
                          'dark blue: color',
                          'navy blue: color',
                          'sky blue: color',
                          'baby blue: color',
                          'pastel blue: color',
                          # -------------------

                          # ------ Browns -----
                          'brown: color',
                          'chocolate brown: color',
                          # -------------------

                          'chartreuse: color',
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
                          'lavender x2: color',
                          'lilac: color',
                          'magenta: color',
                          'maroon: color',
                          'mauve: color',
                          # ----- Oranges -----
                          'orang: colore',
                          'neon orange: color',
                          # -------------------

                          'peach: color',
                          'periwinkle: color',
                          # ------ Pinks ------
                          'pink x4: color',
                          'hot pink x2: color',
                          # -------------------

                          'purple x3: color',
                          # ------ Reds -------
                          'red x5: color',
                          'blood red: color',
                          'bright red: color',
                          'ruby red: color',
                          # -------------------

                          'silver: color',
                          'turquoise: color',
                          'violet x3: color',
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

class FemWardrobe():
    def GetBottom(self):
        Bottoms = [BikiniBottoms(),
                   BikiniBottoms(),
                   BikiniBottoms(),
                   BikiniBottoms(),
                   DaisyDukes(),
                   DaisyDukes(),
                   Panties(),
                   Panties(),
                   Panties(),
                   ShortsFemale(),
                   ShortsFemale(),
                   YogaPants(),
                   YogaPants(),
                  ]

        return choice(Bottoms)

    def GetTop(self, bDresses = False ):
        Tops = [BikiniTop(),
                BikiniTop(),
                BikiniTop(),
                Bra(),
                Bra(),
                Bra(),
                Bra(),
                SportsBra(),
                SportsBra(),
                TshirtFemale(),
               ]

        if bDresses:
            Dresses = [EveningDress(),
                       EveningDress(),
                       RobeFemale(),
                      ]

            Tops = Tops + Dresses

        return choice(Tops)

class Clothes(BodyParts):
    def __init__(self):
        super().__init__()

        self.IsTop = False
        self.IsBottom = False 
        self.IsDress = False
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
                    NewAdjList.append(color)
                    #self.AddUnitToList(unit.sUnit, "master", "adj", unit.iPriority)
                    #self.AddUnitToList(unit.sUnit, "color", "adj", unit.iPriority)

        super().AdjList(NewAdjList)

class Bikini(Clothes):
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
          
          self.AdjList([#'crocheted: material,texture',
                        'daring x2: skimpy',
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
                        #'spandex: material',
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

class BikiniBottoms(Clothes):
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
                        #'crocheted: material,texture',
                        #'crotchless: style,fetish',
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
                        #'spandex: material',
                        'stretchy: stretchy',
                        'stunning: super',
                        'teeny-tiny: size,small',
                        'thin: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'triangular: shape',
                        'V-shaped x3: shape',
                        'vivid: super',
                       ])
               
          self.DefaultNoun('bikini top')
          self.DefaultAdj('skimpy')

          self.IsBottom = True

class BikiniTop(Clothes):
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
          
          self.AdjList([#'crocheted: material,texture',
                        'daring x2: skimpy',
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
                        #'spandex: material',
                        'stringy: skimpy',
                        'stunning: super',
                        'teeny-tiny: size,small',
                        'tight x2: size,small',
                        'tiny x3: size,small',
                        'translucent: texture,material',
                        'triangular: shape',
                        'V-shaped x3: shape',
                        'vivid: super',
                       ])
               
          self.DefaultNoun('bikini top')
          self.DefaultAdj('skimpy')

          self.IsTop = True

class UnderwearFemale(Clothes):
     def __init__(self):
          super().__init__()
          
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

class Bra(Clothes):
     def __init__(self):
          super().__init__()
          
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
                        #'full-cup: size,large',
                        'flimsy: material',
                        'frilly: pattern,style',
                        #'Italian: style',
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
                        #'Victoria\'s Secret: style',
                        'wispy: small',
                       ])
               
          self.DefaultNoun('bra')
          self.DefaultAdj('skimpy')

          self.IsTop = True

class Panties(Clothes):
     def __init__(self):
          super().__init__()

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
                        #'cotton x2: material',
                        'cute: super',
                        'dainty: super',
                        'delicate: super',
                        'diaphanous: seethru',
                        'fancy: super',
                        'flimsy: super',
                        'flowered: pattern',
                        #'French: style',
                        'frilly x3: style',
                        #'Japanese: style',
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

class WorkoutFemale(Clothes):
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

class YogaPants(Clothes):
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
                        #'Lululemon: style',
                        #'lycra: material',
                        #'microfiber: material',
                        'sexy: super',
                        'sleek: texture',
                        'slender: slender',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        #'spandex: material',
                        'stretchy: stretchy',
                        'svelte: super',
                        'tight x2: size,small,tight',
                        'tightly-fitted: tight',
                       ])
               
          self.DefaultNoun('yoga pants')
          self.DefaultAdj('form-fitting')

          self.IsBottom = True

class SportsBra(Clothes):
     def __init__(self):
          super().__init__()
          
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
                        #'lycra: material',
                        #'microfiber: material',
                        'petite: size,small',
                        'provocative: super,skimpy',
                        #'racerback: style',
                        'revealing: skimpy',
                        'sexy: super',
                        'sleek: texture',
                        'skimpy: skimpy',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        #'spandex: material',
                        'tight x2: size,small,tight',
                        'tightly-fitted: tight',
                        'tiny x3: size,small',
                        'zip-up: style',
                       ])
               
          self.DefaultNoun('sports bra')
          self.DefaultAdj('black')

          self.IsTop = True

class EveningDress(Clothes):
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
                        #'French: style',
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
                        #'Parisian: style',
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

class ShortsFemale(Clothes):
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
                        'snug x2: tight',
                        'teeny: size,small',
                        'teeny-tiny: tight',
                        'thigh-length: medium',
                        'tight x2: tight',
                        'tiny x3: tight',
                       ])
               
          self.DefaultNoun('short shorts')
          self.DefaultAdj('snug')

          self.IsBottom = True

class DaisyDukes(Clothes):
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

class TshirtFemale(Clothes):
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
                        #'cotton: material',
                        #'cut-off: style,shape',
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
                        #'v-neck: shape',
                        'white x3: color',
                        'plain white: color',
                        'yellow: color',
                       ])
               
          self.DefaultNoun('t-shirt')
          self.DefaultAdj('white')

          self.IsTop = True

class RobeFemale(Clothes):
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

class Nightgown(Clothes):
     def __init__(self):
          super().__init__()

          #self.ColorsNotList = ["black"]

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

class Heels(Clothes):
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

# TODO:
#   x high heels
#   - blouse
#   - skirt
#   - robe/nightgown/negligee/shift(/kimono?)