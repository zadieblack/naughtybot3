#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
MAX_SEARCH_LOOPS = 20
TWIT_CONTROLLER = 'zadieblack'

Q_SIZE = 40

TweetHistoryQ = None
     
class Gender(IntEnum):
     Male = 1
     Female = 2
     Neuter = 3
     
class Tense(IntEnum):
     Present = 1
     Past = 2
     Gerund = 3
     
class LocInOutType(IntEnum):
     Indoors = 1
     Outdoors = 2
     Either = 3
     
class LocPubPrivType(IntEnum):
     Public = 1
     Private = 2
     Either = 3
     
class GeneratorType(IntEnum):
     Normal = 1
     Promo = 2
     Test = 3
     BookTitle = 4
     
class GirlType(IntEnum):
     Good = 1
     Bad = 2
     Neutral = 3

class HeaderType(IntEnum):
     Harlequin = 1
     Plain = 2

class LineColorType(IntEnum):
     MainTitle = 1
     SecondTitle = 2
     SmallText = 3
     AuthorName = 4

class GenPriority(IntEnum):
    Lowest = 1          # Unity
    Low = 2             # 2x more likely
    Normal = 2          # 3x more likely
    AboveAverage = 3    # 4x more likely
    High = 4            # 5x
    SuperHigh = 5       # 5.5x

HeartEmoji = ['\U00002764','\U0001F49A','\U0001F499','\U0001F49C','\U0001F49B','\U0001F9E1','\U0001F5A4']

def GetHeartEmoji(iNum = 1):
     sHearts = ""
     
     for i in range(0, iNum):
          sHearts += HeartEmoji[randint(0, len(HeartEmoji) - 1)]
          
     return sHearts
     
Emoji = ['\U0001F346','\U0001F525','\U0001F923','\U0001F916','\U0001F618','\U00002B50','\U0001F601','\U0001F603','\U0001F604','\U0001F609','\U0001F61C','\U0001F643','\U0001F60E','\U0001F607','\U0001F920','\U0001F608','\U0001F31E','\U0001F351',GetHeartEmoji()]

def GetEmoji(iNum = 1):
     sEmoji = ""
     
     for i in range(0, iNum):
          sEmoji += Emoji[randint(0, len(Emoji) - 1)]
          
     return sEmoji
     
#combined version
def AddArticles(sNounPhrase, bMakeUpper = False, cBracket = "", bSplitArticle = False):
     sUpdatedPhrase = sNounPhrase
     sArticle = ""
     sNPNounPhrase = "" #Noun phrase without any 'decoration' characters
     
     if isinstance(sUpdatedPhrase, str) and len(sUpdatedPhrase) > 0:
          # Find first alphanumeric character
          iFirstAlphaPos = 0
          for x in range(0, len(sNounPhrase) - 1):
               iFirstAlphaPos = x 
               if sNounPhrase[x].isalpha():
                    break
                    
          sNPNounPhrase = sNounPhrase[x:]
                    
          bDoArticle = True 
          
          #print(" - sNPNounPhrase is " + sNPNounPhrase + "\n")
          # Make sure we haven't created an empty string
          if len(sNPNounPhrase) == 0:
               bDoArticle = False
          
          # Check for words that look plural but aren't (such as 'ass')
          if sNPNounPhrase[-2:].lower() in ['ss','us']:
               bDoArticle = True 
          elif sNPNounPhrase[-1:].lower() == 's':
               bDoArticle = False 
          else:
               bDoArticle = True 
          
          if bDoArticle:
               # check for words that start with a vowel but actually have a consonant sound
               if sNPNounPhrase[0:2].lower() in ['f.','h.','l.','m.','n.','r.','s.','x.']:
                    sArticle = 'an'
               if sNPNounPhrase[0:3].lower() in ['uni','one','uro']:
                    sArticle = 'a'
               elif sNPNounPhrase[0:4].lower() in ['hour']:
                    sArticle = 'an'
               elif sNPNounPhrase[0:5].lower() in ['honor']:
                    sArticle = 'an'
               elif sNPNounPhrase[0].lower() in ['a','e','i','o','u']:
                    sArticle = 'an'
               else:
                    sArticle = 'a'
                         
          if len(sArticle) > 0 and bMakeUpper:
               if sArticle == 'a':
                    sArticle = 'A'
               else:
                    sArticle = 'An'
            
          sArticleSplitter = " "
          if bSplitArticle:
              sArticleSplitter = "\n"

          if len(sArticle) > 0:
               sUpdatedPhrase = sArticle + sArticleSplitter + cBracket + sNounPhrase + cBracket
          else:
               sUpdatedPhrase = cBracket + sNounPhrase + cBracket
               
     return sUpdatedPhrase

def CoinFlip():
     bHeads = True 

     if randint(1,2) == 2:
          bHeads = False
          
     return bHeads 
     
def GenerateFileName():
     # if bot uses same filename every time, twitter might think its spamming. this function randomizes the filename.
     sFileName = ""
     sFileType = "jpg"
     
     #append current time in seconds, remove '.' that seperates miliseconds
     sFileName += str(time.time()).replace(".", "")
     
     #first part of filename is 5-12 alphanumeric chars
     sAlphaNum = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
     
     for i in range(5, randint(7,13)):
          sFileName += sAlphaNum[randint(0, len(sAlphaNum) - 1)]
          
     sFileName += "." + sFileType
     
     return sFileName
     
def IsTweetTooLong(sTweet):
     bTooLong = True
     
     if len(sTweet) <= MAX_TWITTER_CHARS:
          bTooLong = False 
     
     return bTooLong
          
class HistoryQ():
     def __init__(self, iQSize = Q_SIZE):
          self.MaxQSize = iQSize
          self.HistoryQ = []
     
     def PushToHistoryQ(self, item):
          bPushOK = False 

          if not self.IsInQ(item):
               self.HistoryQ.insert(0,item)
               bPushOK = True
               
               while len(self.HistoryQ) > self.MaxQSize:
                    self.HistoryQ.pop()
          
          return bPushOK
          
     def IsInQ(self, item):
          bIsInQ = True 
          
          if len(self.HistoryQ) == 0 or not item in self.HistoryQ:
               bIsInQ = False

          return bIsInQ
               
class HistoryQWithLog(HistoryQ):
    def __init__(self, sLogFileName, iQSize = Q_SIZE):
        super().__init__(iQSize)
        self.LogFileName = sLogFileName
          
        try:
            #print("Opening log file.")
            with open(self.LogFileName, 'rb') as ReadLogFile:
                for item in ReadLogFile.read().splitlines():
                    item = item.decode("utf8")
                    item = item.replace("\\n","\n")
                    #print(item)
                    if type(item) == "int":
                        self.HistoryQ.append(int(item))
                    else:
                        self.HistoryQ.append(item)
        except FileNotFoundError:
            #print("Unable to open log file, creating log file.")
            #open(self.LogFileName, 'wb')
            with open(self.LogFileName, 'rb') as ReadLogFile:
                for item in ReadLogFile.read().splitlines():
                    item = item.decode("utf8")
                    item = item.replace("\\n","\n")
                    #print(item)
                    if type(item) == "int":
                        self.HistoryQ.append(int(item))
                    else:
                        self.HistoryQ.append(item)
        #print("Loaded HistoryQ:")
        #print(self.HistoryQ)
               
    def LogHistoryQ(self):
        #print("Writing log file [" + self.LogFileName + "]")
        with open(self.LogFileName, 'wb+') as WriteHistoryQ:
            for item in self.HistoryQ:
                sLine = str(item)
                sLine = sLine.replace("\n","\\n")
                sLine += "\n"
                UTFLine = sLine.encode("utf8")
                WriteHistoryQ.write(UTFLine)
        #print("Wrote HistoryQ:")
        #print(self.HistoryQ)

     
def FoundIn(sWord, SearchTarget):
     bFound = False 
     
     if isinstance(SearchTarget,str):
          SearchTarget = [SearchTarget]
     
     if isinstance(sWord, str) and isinstance(SearchTarget,list):
          if len(SearchTarget) > 0:
               for s in SearchTarget:
                    if isinstance(s, str):
                         if s.lower() in sWord.lower() or sWord.lower() in s.lower():
                              bFound = True
                              break
               
     return bFound 
          
class WordList:
     def __init__(self, NewList = None):
          if NewList == None:
               self.List = []
          else:
               self.List = NewList
               
          self.DefaultWord = ""
          
     def AddWord(self, word):
          self.List.append(word)
     
     def GetWord(self, sNot = "", NotList = None, SomeHistoryQ = None):
          sWord = ""
          
          if NotList is None:
               NotList = []
               
          if sNot != "":
               NotList.append(sNot)
               
          if not self.List == None and len(self.List) > 0:
               sWord = self.List[randint(0, len(self.List) - 1)]
               
               if SomeHistoryQ is None:
                    i = 0
                    while FoundIn(sWord, NotList) and i < MAX_SEARCH_LOOPS:
                         #print("Collision! '" + sWord + "' in NotList, trying again.")
                         sWord = self.List[randint(0, len(self.List) - 1)]
                         i += 1
               else:
                    i = 0
                    while (not SomeHistoryQ.PushToHistoryQ(sWord) or FoundIn(sWord, NotList)) and i < MAX_SEARCH_LOOPS:
                         #print("Collision! '" + sWord + "' in NotList, trying again.")
                         sWord = self.List[randint(0, len(self.List) - 1)]
                         i += 1
                    
          return sWord
          
     def Length(self):
          iLen = 0
          
          if isinstance(self.List, list):
               iLen = len(self.List)
               
          return iLen
          
     def IsEmpty(self):
          bIsEmpty = True 
          
          if self.Length() > 0:
               bIsEmpty = False 
          
          return bIsEmpty
          
     def GetWordList(self):
          return self.List
          
class NounAdjList:
     def __init__(self, NewNounList = None, NewAdjList = None):
          if NewNounList == None:
               self.NounList = []
          else:
               self.NounList = NewNounList
               
          if NewAdjList == None:
               self.AdjList = []
          else:
               self.AdjList = NewAdjList
               
          self.NounHistoryQ = HistoryQ(3)
          self.AdjHistoryQ = HistoryQ(3)
               
          self.DefaultNoun = ""
          self.DefaultAdj = ""
     
     def GetNoun(self, NotList = None):
          sNoun = ""
          
          if NotList is None:
               NotList = []
          
          if not self.NounList == None and len(self.NounList) > 0:
               sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
               while not self.NounHistoryQ.PushToHistoryQ(sNoun) or sNoun in NotList:
                    sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
               
          return sNoun
          
     def GetAdj(self, NotList = None):
          sAdj = ""
          
          if NotList is None:
               NotList = []
          
          if not self.AdjList == None and len(self.AdjList) > 0:
               sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
               while not self.AdjHistoryQ.PushToHistoryQ(sAdj) or sAdj in NotList:
                    sAdj = self.AdjList[randint(0, len(self.AdjList) - 1)]
               
          return sAdj
     
     def GetWord(self, NotList = None):
          sWord = ""
          
          if NotList is None:
               NotList = []
                         
          sWord = self.GetAdj(NotList) + " " + self.GetNoun(NotList)
          
          return sWord
          
def SmartLower(phrase):
     sResult = phrase
     if isinstance(sResult,str):
          aOldPhrase = sResult.split()
          aNewPhrase = []
          for item in aOldPhrase:
               if len(item) > 1 and not item[1].isupper():
                    aNewPhrase.append(item.lower())
               else:
                    aNewPhrase.append(item)
          sResult = ' '.join(aNewPhrase)
          
     return sResult

# https://twitter.com/{status.user.screen_name}/status/{status.id} 
def ExtractURLFromStatus(status):
    sURL = ""

    if not status is None:
        sScreenName = status.user.screen_name 
        sTweetID = str(status.id)

        sURL = "https://twitter.com/" + sScreenName + "/status/" + sTweetID

    return sURL

def len_alpha_key(str):
     return -len(str), str.lower()
     
class Sound():
     def __init__(self, newlist):
          self._SoundList = sorted(newlist,key=len_alpha_key)
          if len(self._SoundList) > 0:
               self.Length = len(self._SoundList[0])
          else:
               self.Length = 0
          
     def SoundsLike(self, word):
          bSoundsLike = False 
          
          if isinstance(self._SoundList, list) and isinstance(word,str):
               for item in self._SoundList:
                    iSoundLen = len(item)
                    if item.lower()[0:iSoundLen] == word.lower()[0:iSoundLen]:
                         bSoundsLike = True 
                         break
     
          return bSoundsLike
          
     
     
class ConsonantSounds():
     def sound_key(self,sound):
          return -sound.Length,sound._SoundList[0].lower()
     
     def __init__(self):
          self.sounds = []
     
          self.sounds.append(Sound(['b']))
          self.sounds.append(Sound(['bl']))
          self.sounds.append(Sound(['br']))
          self.sounds.append(Sound(['bw']))
          self.sounds.append(Sound(['c','k']))
          self.sounds.append(Sound(['ch']))
          self.sounds.append(Sound(['cl','kl']))
          self.sounds.append(Sound(['cr','kr','chr']))
          self.sounds.append(Sound(['cw','kw','qu']))
          self.sounds.append(Sound(['d']))
          self.sounds.append(Sound(['dr']))
          self.sounds.append(Sound(['dw']))
          self.sounds.append(Sound(['f']))
          self.sounds.append(Sound(['fl']))
          self.sounds.append(Sound(['fr']))
          self.sounds.append(Sound(['g','gh']))
          self.sounds.append(Sound(['gl']))
          self.sounds.append(Sound(['gn','kn','n']))
          self.sounds.append(Sound(['gr']))
          self.sounds.append(Sound(['gw']))
          self.sounds.append(Sound(['gy','ji']))
          self.sounds.append(Sound(['h','wh']))
          self.sounds.append(Sound(['j']))
          self.sounds.append(Sound(['l',]))
          self.sounds.append(Sound(['m']))
          self.sounds.append(Sound(['n']))
          self.sounds.append(Sound(['p']))
          self.sounds.append(Sound(['pl']))
          self.sounds.append(Sound(['pr']))
          self.sounds.append(Sound(['ps','s']))
          self.sounds.append(Sound(['r','wr','rh']))
          self.sounds.append(Sound(['sc','sch','sk']))
          self.sounds.append(Sound(['scr','schr']))
          self.sounds.append(Sound(['sl']))
          self.sounds.append(Sound(['sm']))
          self.sounds.append(Sound(['sn']))
          self.sounds.append(Sound(['sp']))
          self.sounds.append(Sound(['squ','scw','skw']))
          self.sounds.append(Sound(['st']))
          self.sounds.append(Sound(['str']))
          self.sounds.append(Sound(['sw']))
          self.sounds.append(Sound(['t']))
          self.sounds.append(Sound(['th']))
          self.sounds.append(Sound(['tw']))
          self.sounds.append(Sound(['v']))
          self.sounds.append(Sound(['w','jua']))
          self.sounds.append(Sound(['x','z']))
          
          
          self.sounds.append(Sound(['am']))
          self.sounds.append(Sound(['an']))
          self.sounds.append(Sound(['au','ah']))
          self.sounds.append(Sound(['ath']))
          self.sounds.append(Sound(['at','att']))
          self.sounds.append(Sound(['air','aer','are']))
          self.sounds.append(Sound(['ar']))
          self.sounds.append(Sound(['in','inn']))
          self.sounds.append(Sound(['er','ear']))
          self.sounds.append(Sound(['ex']))
          self.sounds.append(Sound(['oi']))
          self.sounds.append(Sound(['ol']))
          self.sounds.append(Sound(['out']))
          self.sounds.append(Sound(['u']))
          self.sounds.append(Sound(['uni']))
          self.sounds.append(Sound(['un','unn']))
          
          self.sounds.append(Sound(['ur']))
          
          self.sounds = sorted(self.sounds,key=self.sound_key)
          
          
     def __iter__(self):
          return iter(self.sounds)

Sounds = ConsonantSounds()

def GradeSoundMatch(word1,word2):
     iMatchGrade = 0
     
     sounds = Sounds
     
     word1sound = Sound([])

     # find a matching sound for the first word 
     for sound in sounds:
          if sound.SoundsLike(word1):     
               word1sound = sound 
               break
               
     # compare the matched sound to the second word 
     if word1sound.SoundsLike(word2):
          iMatchGrade = word1sound.Length
          
     return iMatchGrade

def GetRhymingWord(word, list):
     shuffle(list)
     
     bestmatchlen = 0
     bestmatch = ""

     for item in list:
          itemgrade = GradeSoundMatch(item,word)
          if itemgrade > bestmatchlen:
               bestmatchlen = itemgrade
               bestmatch = item
                    
     return bestmatch
     
def GetRhymingPair(list1, list2):
     rhymingpair = ["",""]
     shuffle(list1)
     
     srhyme = ""
     for item in list1:
          srhyme = GetRhymingWord(item, list2)
          if len(srhyme) > 0 and not srhyme == item[0:len(srhyme)] and not srhyme[0:len(item)] == item:
               rhymingpair = [item,srhyme]
               break

                    
     return rhymingpair