#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Clothes module

from random import *
from util import *
from excerpt.bodyparts import *

ClothesColors = WordList(['black x4:',
                          'beige',
                          'blue x2:',
                          'dark blue','navy blue','sky blue','baby blue',
                          'brown','chocolate brown',
                          'chartreuse',
                          'coral',
                          'cream-colored',
                          'gold',
                          'green x2:',
                          'dark green','lime green','sea green',
                          'neon green',
                          'indigo',
                          'lavender x2:',
                          'magenta',
                          'maroon',
                          'mauve',
                          'orange','neon orange',
                          'peach',
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

    # Override the AdjList creation call so we
    # can manually add the colors from the 
    # ClothesColors list to each adj list.
    def AdjList(self, NewAdjList):
        super().AdjList(NewAdjList)

        global ClothesColors 
        
        for color in ClothesColors.GetWordList():
            #def AddUnitToList(self, sUnit, sListName, sType, iPriority = None):
            unit = self.ParseUnit(color)
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
          
          self.AdjList(['crocheted: material,texture',
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

          self.IsTop = True

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
                        'narrow: size,small',
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

          self.IsBottom = True