#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Verbs module

from random import *
import title.util

class Verb:
     PastList = []
     PresentList = []
     GerundList = []
     AdverbList = []
     
     def Past(self):
          sPastVerb = ""
          iRandIndex = 0
          
          iRandIndex = randint(0, len(self.PastList) - 1)
          
          sPastVerb = self.PastList[iRandIndex]
          
          return sPastVerb
          
     def Present(self):
          sPresentVerb = ""
          iRandIndex = 0
          
          iRandIndex = randint(0, len(self.PresentList) - 1)
          
          sPresentVerb = self.PresentList[iRandIndex]
          
          return sPresentVerb
          
     def Gerund(self):
          sGerundVerb = ""
          iRandIndex = 0
          
          iRandIndex = randint(0, len(self.GerundList) - 1)
          
          sGerundVerb = self.GerundList[iRandIndex]
          
          return sGerundVerb
          
     def GetAdv(self):
          sAdverb = ""
          
          if not self.AdverbList == None and len(self.AdverbList) > 0:
               iRand = randint(0, len(self.AdverbList) - 1)
               sAdverb = self.AdverbList[iRand]
               
          return sAdverb
          
class VerbThrust(Verb):
     PresentList = ['bang',
          'bore into',
          'burrow into',
          'delve into',
          'desecrate',
          'defile',
          'do',
          'drill',
          'fill',
          'fuck',
          'hammer',
          'impale',
          'jackhammer',
          'nail',
          'penetrate',
          'piston into',
          'plow',
          'pound',
          'probe',
          'pump into',
          'ram',
          'ravage',
          'ravish',
          'ream',
          'rut in',
          'slam',
          'stuff',
          'thrust into',
          'violate']
          
     PastList = ['banged',
          'bored into',
          'burrowed into',
          'delved into',
          'desecrated',
          'defiled',
          'did',
          'drilled',
          'eagerly filled',
          'fucked',
          'hammered',
          'impaled',
          'jackhammered',
          'nailed',
          'penetrated',
          'pistoned into',
          'plowed',
          'pounded',
          'probed',
          'pumped into',
          'rammed relentlessly into',
          'ravaged',
          'ravished',
          'reamed',
          'rutted in',
          'slammed into',
          'stuffed',
          'thrust deep into',
          'violated']
          
     GerundList = ['banging',
          'boring into',
          'burrowing into',
          'delving into',
          'desecrating',
          'defiling',
          'doing',
          'drilling',
          'eagerly filling',
          'fucking',
          'hammering',
          'impaling',
          'jackhammering',
          'nailing',
          'penetrating',
          'pistoning into',
          'plowing',
          'pounding',
          'probing',
          'pumping into',
          'ramming relentlessly into',
          'ravaging',
          'ravishing',
          'reaming',
          'rutting in',
          'slamming into',
          'stuffing',
          'thrusting deep into',
          'violating']
          
class VerbMakeLove(Verb):
     PresentList = []
     PastList = []
     GerundList = []
          
     def __init__(self):
          self.PresentList = ['make love to',
               'ease into',
               'enter',
               'push into',
               'sex']
          
          self.PastList = ['made love to',
               'eased into',
               'entered',
               'pushed into',
               'sexed']
          
          self.GerundList = ['making love to',
               'easing into',
               'entering',
               'pushing into',
               'sexing']
          Harder = VerbThrust()
          
          Prefixes = util.WordList(['gently','lovingly','carefully','tenderly'])
          
          iNumAdd = len(self.PresentList)
          #print("len(self.PresentList) = " + str(iNumAdd))
          for x in sample(range(0, len(Harder.PresentList)), iNumAdd):
               #print("len(Harder.PresentList) = " + str(len(Harder.PresentList)) + ", x = " + str(x))
               self.PresentList.append(Prefixes.GetWord() + " " + Harder.PresentList[x])
               
          iNumAdd = len(self.PastList)
          #print("len(self.PastList) = " + str(iNumAdd))
          for x in sample(range(0, len(Harder.PastList)), iNumAdd):
               #print("len(Harder.PastList) = " + str(len(Harder.PastList)) + ", x = " + str(x))
               self.PastList.append(Prefixes.GetWord() + " " + Harder.PastList[x])
               
          iNumAdd = len(self.GerundList)
          #print("len(self.GerundList) = " + str(iNumAdd))
          for x in sample(range(0, len(Harder.GerundList)), iNumAdd):
               #print("len(Harder.GerundList) = " + str(len(Harder.GerundList)) + ", x = " + str(x))
               self.GerundList.append(Prefixes.GetWord() + " " + Harder.GerundList[x])
          
class VerbEjaculate(Verb):
     PresentList = ['burst',
          'climax',
          'cum',
          'cum hard',
          'ejaculate',
          'erupt',
          'explode',
          'gush',
          'jizz',
          'orgasm',
          'nut',
          'spurt',
          'squirt']
          
     PastList = ['burst',
          'climaxed',
          'came',
          'came hard',
          'ejaculated',
          'erupted',
          'exploded',
          'gushed',
          'jizzed',
          'nutted',
          'orgasmed',
          'spurted',
          'squirted']
          
     GerundList = ['bursting',
          'climaxing',
          'cumming',
          'cumming hard',
          'ejaculating',
          'erupting',
          'exploding',
          'gushing',
          'jizzing',
          'nutting',
          'orgasming',
          'spurting',
          'squirting']
          
class VerbDrip(Verb):
     PresentList = ['dribble',
          'drip',
          'flow',
          'gush',
          'hang',
          'leak',
          'ooze',
          'pour']
          
     PastList = ['dribbled', 
          'dripped', 
          'flowed', 
          'gushed', 
          'hung', 
          'leaked', 
          'oozed', 
          'poured']
          
     GerundList = ['dribbling',
          'dripping',
          'flowing',
          'gushing',
          'hanging',
          'oozing',
          'leaking',
          'pouring']
          
class VerbForeplay(Verb):
     PresentList = ['caress',
          'finger',
          'fondle',
          'kiss',
          'lick',
          'nibble on',
          'play with',
          'rub',
          'rub',
          'squeeze',
          'stroke',
          'suck',
          'tease']
          
     PastList = ['caressed',
          'fingered',
          'fondled',
          'kissed',
          'licked',
          'nibbled on',
          'played with',
          'rubbed',
          'squeezed',
          'stroked',
          'sucked',
          'teased']
          
     GerundList = ['caressing',
          'fingering',
          'fondling',
          'kissing',
          'licking',
          'nibbling on',
          'playing with',
          'rubbing',
          'squeezing',
          'stroking',
          'sucking',
          'teasing']
          
class VerbSex(Verb):
     PresentList = ['bang',
          'boink',
          'fuck',
          'go at it',
          'have sex',
          'hump',
          'make love']
          
     PastList = ['banged',
          'boinked',
          'fucked',
          'went at it',
          'had sex',
          'humped',
          'made love']
          
     GerundList = ['banging',
          'boinking',
          'fucking',
          'going at it',
          'having sex',
          'humping',
          'making love']
          
     AdverbList = ['ardently',
          'enthusiastically',
          'fervently',
          'fervidly',
          'feverishly',
          'heedlessly',
          'intensely',
          'passionately',
          'rapturously',
          'urgently']
          
class VerbSexWith(Verb):
     PresentList = ['bang',
          'boink',
          'fuck',
          'go at it with',
          'have sex with',
          'hump',
          'make love to']
          
     PastList = ['banged',
          'boinked',
          'fucked',
          'went at it with',
          'had sex with',
          'humped',
          'made love to']
          
     GerundList = ['banging',
          'boinking',
          'fucking',
          'going at it with',
          'having sex with',
          'humping',
          'making love to']
          
     AdverbList = ['ardently',
          'enthusiastically',
          'fervently',
          'fervidly',
          'feverishly',
          'heedlessly',
          'intensely',
          'passionately',
          'rapturously']
          
class VerbMoan(Verb):
     PresentList = ['cry',
                         'gasp',
                         'groan',
                         'moan',
                         'murmur',
                         'pant',
                         'purr',
                         'says',
                         'sigh',
                         'wail',
                         'whimper',
                         'whisper']
                    
     PastList = ['cried',
                    'gasped',
                    'groaned',
                    'moaned',
                    'murmured',
                    'panted',
                    'purred',
                    'said',
                    'sighed',
                    'wailed',
                    'whimpered',
                    'whispered']
     
     GerundList = ['crying',
                         'gasping',
                         'groaning',
                         'moaning',
                         'murmuring',
                         'panting',
                         'purring',
                         'saying',
                         'sighing',
                         'wailing',
                         'whimpering',
                         'whispering']
                         
class VerbOralMale(Verb):
     PresentList = ['blow',
          'go down on',
          'fellate',
          'suck',
          'suckle']
     
     PastList = ['blew',
          'went down on',
          'fellated',
          'sucked',
          'suckled']
     
     GerundList = ['blowing'
          'fellating',
          'going down on',
          'sucking',
          'suckling']
          
class VerbSexActsByMale(Verb):
     PresentList = ["ass fuck",
          "cream-pie",
          "dry hump",
          "eat out",
          "facial",
          "finger bang",
          "rim",
          "sixty-nine",
          "tea-bag",
          "titty fuck"]
          
     PastList = ["ass fucked",
          "cream-pied",
          "dry humped",
          "ate out",
          "facialed",
          "finger banged",
          "rim-jobbed",
          "sixty-nined",
          "tea-bagged",
          "titty fucked"]
          
     GerundList = ["ass fucking",
          "cream-pieing",
          "dry humping",
          "eating out",
          "facialing",
          "finger banging",
          "rimming",
          "sixty-nining",
          "tea-bagging",
          "titty fucking"]
          
class VerbSexActsByFemale(Verb):
     PresentList = ["blow",
          "deep throat",
          "dry hump",
          "fellate",
          "give a footjob to",
          "jerk off",
          "peg",
          "rim",
          "sixty-nine",
          "squirt on"]
          
     PastList = ["blew",
          "dry humped",
          "deep-throated",
          "fellated",
          "gave a footjob to",
          "jerked off",
          "pegged",
          "rimmed",
          "sixty-nined",
          "squirted on"]
          
     GerundList = ["blowing",
          "deep throating",
          "dry humping",
          "fellating",
          "giving a footjob to",
          "pegging",
          "rimming",
          "sixty-nining",
          "squriting on"]
     
          
