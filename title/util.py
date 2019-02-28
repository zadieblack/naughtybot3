#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
MAX_SEARCH_LOOPS = 8
TWIT_USERNAME = 'erotica_ebooks'

Q_SIZE = 12
HISTORYQ_FILENAME = 'history_q.txt'
TWEETTXT_HISTORYQ_FILENAME = 'tweettxt_history_q.txt'

TAG_PEN = "sex act with penetration scene"
TAG_NON_PEN = "non-penetrative sex act scene"
TAG_DONE_TO_HER = "done to her scene"
TAG_DONE_TO_HIM = "done to him scene"
TAG_CLIMAX = "orgasm scene"
TAG_POSITION = "sex position scene"
TAG_FOREPLAY = "foreplay scene"
TAG_ABOVE_BELT = "above-the-belt sex act scene"
TAG_BELOW_BELT = "below-the-belt sex act scene"
TAG_ORAL = "oral sex scene"
TAG_CLOTHED = "scene where they still have clothes on"

TweetHistoryQ = None
	
class Gender(Enum):
	Male = 1
	Female = 2
	Neuter = 3
	
class Tense(Enum):
	Present = 1
	Past = 2
	Gerund = 3
	
class LocInOutType(Enum):
	Indoors = 1
	Outdoors = 2
	Either = 3
	
class LocPubPrivType(Enum):
	Public = 1
	Private = 2
	Either = 3
	
class GeneratorType(Enum):
	Normal = 1
	Promo = 2
	Test = 3
	BookTitle = 4
	
class GirlType(Enum):
	Good = 1
	Bad = 2
	Neutral = 3

def AddArticles(sNounPhrase):
	sUpdatedPhrase = ""
	
	if len(sNounPhrase) > 0:
		if sNounPhrase[0].lower() in ['a','e','i','o','u']:
			sUpdatedPhrase = 'An ' + sNounPhrase
		else:
			sUpdatedPhrase = 'A ' + sNounPhrase
			
	return sUpdatedPhrase
	
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

def CoinFlip():
	bHeads = True 
	iRand = randint(1,2)
	if iRand == 2:
		bHeads = False
		
	return bHeads 
	
def GenerateFileName():
	# if bot uses same filename every time, twitter might think its spamming. this function randomizes the filename.
	sFileName = ""
	sFileType = "png"
	
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
		#print("LogFileName is " + self.LogFileName)
		
		try:
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		except FileNotFoundError:
			open(self.LogFileName, 'w')
			with open(self.LogFileName, 'r') as ReadLogFile:
				for item in ReadLogFile.read().splitlines():
					#print(item)
					self.HistoryQ.append(int(item))
		#print("Loaded HistoryQ:")
		#print(self.HistoryQ)
			
	def LogHistoryQ(self):
		with open(self.LogFileName, 'w') as WriteHistoryQ:
			for item in self.HistoryQ:
				WriteHistoryQ.write(str(item) + "\n")
		#print("Wrote HistoryQ:")
		#print(self.HistoryQ)
			
class WordList:
	def __init__(self, NewList = None):
		if NewList == None:
			self.List = []
		else:
			self.List = NewList
			
		self.DefaultWord = ""
		
	def FoundIn(self, sWord, ListStrings):
		bFound = False 
		
		if not ListStrings is None and len(ListStrings) > 0:
			for str in ListStrings:
				if str.lower() in sWord.lower() or sWord.lower() in str.lower():
					bFound = True
					break
				
		return bFound 
	
	def GetWord(self, NotList = None, SomeHistoryQ = None):
		sWord = ""
		
		if NotList is None:
			NotList = []
			
		if not self.List == None and len(self.List) > 0:
			sWord = self.List[randint(0, len(self.List) - 1)]
			
			if SomeHistoryQ is None:
				i = 0
				while self.FoundIn(sWord, NotList) and i < MAX_SEARCH_LOOPS:
					#print("Collision! '" + sWord + "' in NotList, trying again.")
					sWord = self.List[randint(0, len(self.List) - 1)]
					i += 1
			else:
				i = 0
				while (not SomeHistoryQ.PushToHistoryQ(sWord) or self.FoundIn(sWord, NotList)) and i < MAX_SEARCH_LOOPS:
					#print("Collision! '" + sWord + "' in NotList, trying again.")
					sWord = self.List[randint(0, len(self.List) - 1)]
					i += 1
				
		return sWord
		
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
		
		iRandNounIndex = 0
		
		if not self.NounList == None and len(self.NounList) > 0:
			sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
			while not self.NounHistoryQ.PushToHistoryQ(sNoun) or sNoun in NotList:
				sNoun = self.NounList[randint(0, len(self.NounList) - 1)]
			
		return sNoun
		
	def GetAdj(self, NotList = None):
		sAdj = ""
		
		if NotList is None:
			NotList = []
		
		iRandAdjIndex = 0
		
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