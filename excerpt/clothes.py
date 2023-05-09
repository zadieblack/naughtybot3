#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Clothes module

from random import *
from util import *
from excerpt.bodyparts import *

ClothesColors = WordList(['black x4:',
                          'beige',
                          'blue x2:',
                          'dark blue','navy blue','sky blue','baby blue','pastel blue',
                          'brown','chocolate brown',
                          'chartreuse',
                          'coral',
                          'cream-colored',
                          'gold',
                          'green x2:',
                          'dark green','lime green','sea green',
                          'neon green','pastel green',
                          'indigo',
                          'lavender x2:',
                          'lilac',
                          'magenta',
                          'maroon',
                          'mauve',
                          'orange','neon orange',
                          'peach',
                          'periwinkle',
                          'pink x4:',
                          'hot pink x2:',
                          'purple x3:',
                          'red x4:',
                          'blood red','bright red','ruby red',
                          'silver',
                          'tan',
                          'turquoise',
                          'violet x3:',
                          'yellow',
                          'bright yellow','canary yellow','dayglow yellow','lemon yellow',
                          'white x2:',
                          'pure white',
                         ])

class Clothes(BodyParts):
    def __init__(self):
        super().__init__()

        self.IsTop = False
        self.IsBottom = False 
        self.AddColors = True

        self.ColorsNotList = []

    # Override the AdjList creation call so we
    # can manually add the colors from the 
    # ClothesColors list to each adj list.
    def AdjList(self, NewAdjList):
        super().AdjList(NewAdjList)

        global ClothesColors 
        
        if self.AddColors:
            for color in ClothesColors.GetWordList():
                unit = self.ParseUnit(color)
                
                if unit.sUnit not in self.ColorsNotList:
                    self.AddUnitToList(unit.sUnit, "master", "adj", unit.iPriority)
                    self.AddUnitToList(unit.sUnit, "color", "adj", unit.iPriority)

class Bikini(Clothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['bikini x4: default,std,sing',
                         'Brazilian bikini: variant,sing',
                         'French bikini: variant,sing',
                         'sling bikini: variant,sing',
                         'strapless bikini: variant,sing',
                         'string bikini: std,sing',
                         'two-piece bathing suit: std,sing',
                        ])
          
          self.AdjList(['crocheted: material,texture',
                        'daring x2: skimpy',
                        'eye-watering: super',
                        'flimsy: skimpy',
                        'floral: pattern',
                        'heart-shaped: shape',
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
                        'sheer: seethru,texture,pattern,material',
                        'skimpy x2: skimpy',
                        'snug: skimpy',
                        'spandex: material',
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
          
          self.NounList(['bikini bottoms x3: default,std,plur',
                         'Brazilian bikini bottoms: std,plur',
                         'G-string x2: variant,sing',
                         'string bikini bottoms: variant,plur',
                         'thong x4: std,sing',
                        ])
          
          self.AdjList(['cheeky: super',
                        'crocheted: material,texture',
                        'crotchless: style,fetish',
                        'daring x2: skimpy',
                        'flimsy: skimpy',
                        'floral: pattern',
                        'hot: super',
                        'immodest: skimpy',
                        'leopard print: pattern',
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
                        'spandex: material',
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
          
          self.NounList(['bikini top x3: default,std,sing',
                         'strapless bikini top: variant,sing',
                        ])
          
          self.AdjList(['cheeky: super',
                        'crocheted: material,texture',
                        'crotchless: style,fetish',
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
                        'spandex: material',
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
          
          self.NounList(['bra x3: default,std,sing',
                         'brassiere: std,sing',
                         'cupless bra: variant,fetish,sing',
                         'pushup bra: variant,sing',
                         'strapless bra: variant,sing',
                        ])
          
          self.AdjList(['cute: super',
                        'daring: super',
                        'delicate: super',
                        'elegant: super',
                        'fancy: super',
                        'flowered: pattern',
                        'full: size,large',
                        'full-cup: size,large',
                        'flimsy: material',
                        'frilly: pattern,style',
                        'Italian: style',
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
                        'Victoria\'s Secret: style',
                        'wispy: small',
                       ])
               
          self.DefaultNoun('bra')
          self.DefaultAdj('skimpy')

          self.IsTop = True

class Panties(Clothes):
     def __init__(self):
          super().__init__()
          
          self.NounList(['G-string panties: variant,plur',
                         'panties x4: default,std,plur',
                         'thong: variant,sing',
                         'thong underwear: variant,sing',
                         'underwear x2: std,sing',
                        ])
          
          self.AdjList(['brief: size,small',
                        'cheeky: skimpy',
                        'cotton x2: material',
                        'cute: super',
                        'dainty: super',
                        'delicate: super',
                        'diaphanous: seethru',
                        'fancy: super',
                        'flimsy: super',
                        'flowered: pattern',
                        'French: style',
                        'frilly: style',
                        'Japanese: style',
                        'lace x2: pattern,material',
                        'lacey x2: pattern,material',
                        'leopard print: pattern',
                        'little x4: size,small',
                        'naughty: super',
                        'nylon: material',
                        'plain: style,pattern',
                        'polka-dotted: pattern',
                        'pretty: super',
                        'provocative: skimpy',
                        'revealing: skimpy',
                        'ruffled: style',
                        'satin x2: material,texture',
                        'scant: skimpy',
                        'see-thru: pattern,texture,seethru',
                        'sexy x2: super',
                        'sheer: seethru,texture,pattern,material',
                        'silk x2: material',
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

          self.ColorsNotList = ["gold","silver"]

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
          
          self.NounList(['leggings: std,plur',
                         'yoga pants x3: std,default,plur',
                        ])
          
          self.AdjList(['athletic: style',
                        'body-hugging: tight',
                        'clingy: tight',
                        'cute: super',
                        'daring: super',
                        'figure-hugging: tight',
                        'form-fitting: tight',
                        'hip-hugging: tight',
                        'Lululemon: style',
                        'lycra: material',
                        'microfiber: material',
                        'sexy: super',
                        'sheath-like: tight',
                        'sleek: texture',
                        'slender: slender',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'spandex: material',
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
          
          self.NounList(['sports bra x4: default,std,sing',
                        ])
          
          self.AdjList(['athletic: style',
                        'cute: super',
                        'daring: super',
                        'flimsy: material',
                        'high-impact: super',
                        'large: size,large',
                        'lycra: material',
                        'microfiber: material',
                        'petite: size,small',
                        'provocative: super,skimpy',
                        'racerback: style',
                        'revealing: skimpy',
                        'sexy: super',
                        'sleek: texture',
                        'skimpy: skimpy',
                        'small: size,small',
                        'soft: texture',
                        'snug x2: tight',
                        'spandex: material',
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
          
          self.NounList(['ball gown: std,sing',
                         'cocktail dress x2: std,sing',
                         'cocktail gown: std,sing',
                         'evening gown x2: std,default,sing',
                         'evening dress x2: std,sing',
                         'mini dress: std,sing',
                         'sheath dress: variant,sing',
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
                        'French: style',
                        'frilly: style',
                        'glamorous: super',
                        'gold: color,material',
                        'gorgeous: super',
                        'jet-black: color',
                        'knee-length: length,medium',
                        'lacey x2: pattern,material',
                        'long: length,long',
                        'luxurious: style',
                        'mini: short,skimpy',
                        'Parisian: style',
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

