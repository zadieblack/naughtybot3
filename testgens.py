#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
 
import sys, argparse, datetime, threading, traceback
from io import BytesIO
from random import *
import util as util
import title.util as titutil
import excerpt.generators as excerpt
import excerpt.tweettext as extweettxt
import excerpt.texttoimg as eximg
import title.generators as title 
import title.tweettext as tittweettxt
import title.texttoimg as titimg
import names 


def SetGetArgs():
     Parser = argparse.ArgumentParser(prog='TestGens',description='Run generator tests.')
     Parser.add_argument('-createimages', action='store_true', help='Create images for each generator? (default is False)')
     Parser.add_argument('-excerpts', action='store_true', help='Test excerpt generators')
     Parser.add_argument('-extweettxt', action='store_true', help='Test excerpt tweet text generators')
     Parser.add_argument('-titles', action='store_true', help='Test title generators')
     Parser.add_argument('-tittweettxt', action='store_true', help='Test title tweet text generators')
     Parser.add_argument('-innames', action='store_true', help='Test innuendo names generators')
     Parser.add_argument('-all', action='store_true', help='Test all generators')
     
     return Parser.parse_args()
               
def TestExcerptGens(bCreateImages = False):
     print("==>Testing EXCERPTS<==")
     GeneratorList = []
     
     selector = excerpt.GeneratorSelector()
     GeneratorList = selector.GetGeneratorsSequential()
     
     GeneratorPassList = []
     GeneratorFailList = []
     for gen in GeneratorList:
          try:
               sTweet = gen.GenerateTweet()
                    
               if len(sTweet) > 0:
                    if bCreateImages:
                         eximg.CreateImg(sTweet).save(GenerateFileName(), format = 'jpg')
                    
                    print("* Testing Excerpt Generator ID " + str(gen.ID) + " (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(gen.ID)
               else:
                    print("* ! ERROR: empty tweet (Excerpt Generator ID: " + str(gen.ID) + ") ! *")
                    GeneratorFailList.append(gen.ID)
          except:
               GeneratorFailList.append("* ! Excerpt Generator: " + str(sys.exc_info()[0]) + " ! *")
               
     return [GeneratorPassList,GeneratorFailList]

def TestExcerptTweetTextGens():
     print("==>Testing EXERPT TWEET TEXT<==")
     GeneratorList = []
     
     selector = extweettxt.TweetTxtGenSelector()
     GeneratorList = selector.GetGeneratorsSequential()
     
     GeneratorPassList = []
     GeneratorFailList = []
     for gen in GeneratorList:
          try:     
               sTweet = gen.GenerateTweet()
                         
               if len(sTweet) > 0:
                    print("* Testing Excerpt Text Generator ID " + str(gen.ID) + " (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(gen.ID)
               else:
                    print("* ! ERROR: empty tweet (Excerpt Text Generator ID: " + str(gen.ID) + ") ! *")
                    GeneratorFailList.append(gen.ID)
          except:
               GeneratorFailList.append("* ! Excerpt Text Generator: " + str(sys.exc_info()[0]) + " ! *")
               
     return [GeneratorPassList,GeneratorFailList]

def TestTitleGens(bCreateImages = False):
     print("==>Testing TITLES<==")
     GeneratorList = []
     
     selector = title.GeneratorSelector()
     GeneratorList = selector.GetGeneratorsSequential()
     
     GeneratorPassList = []
     GeneratorFailList = []
     for gen in GeneratorList:
          try:
               sTweet = gen.GenerateTweet()
                    
               if len(sTweet) > 0:
                    if bCreateImages:
                         titimg.CreateImg(sTweet).save(GenerateFileName(), format = 'jpg')
                    
                    print("* Testing Title Generator ID " + str(gen.ID) + " (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(gen.ID)
               else:
                    print("* ! ERROR: empty tweet (Title Generator ID: " + str(gen.ID) + ") ! *")
                    GeneratorFailList.append(gen.ID)
          except:
               GeneratorFailList.append("* ! Title Generator: " + str(sys.exc_info()[0]) + " ! *")
               
     return [GeneratorPassList,GeneratorFailList]

def TestTitleTweetTextGens():
     print("==>Testing TITLE TWEET TEXT<==")
     GeneratorList = []
     
     selector = tittweettxt.TweetTxtGenSelector()
     GeneratorList = selector.GetGeneratorsSequential()
     
     GeneratorPassList = []
     GeneratorFailList = []
     for gen in GeneratorList:
          try:
               sTweet = gen.GenerateTweet()
               
               if len(sTweet) > 0:
                    print("* Testing Title Text Generator ID " + str(gen.ID) + " (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(gen.ID)
               else:
                    print("* ! ERROR: empty tweet (Title Text Generator ID: " + str(gen.ID) + ") ! *")
                    GeneratorFailList.append(gen.ID)
          except:
               GeneratorFailList.append("* ! Title Text Generator: " + str(sys.exc_info()[0]) + " ! *")
               
     return [GeneratorPassList,GeneratorFailList]

def TestInnNameGens():
     print("==>Testing INNUENDO NAMES<==")
     GeneratorList = []
     
     selector = names.InnNameGenSelector()
     GeneratorList = selector.GetGeneratorsSequential()
     
     GeneratorPassList = []
     GeneratorFailList = []
     for gen in GeneratorList:
          try:
               sTweet = gen.GetName(util.Gender.Female)
                    
               if len(sTweet) > 0:
                    print("* Testing Innuendo Name Generator ID " + str(gen.ID) + " FEMALE (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(str(gen.ID) + " FEMALE")
               else:
                    print("* ! ERROR: empty tweet (Innuendo Name Generator ID: " + str(gen.ID) + " FEMALE) ! *")
                    GeneratorFailList.append(str(gen.ID) + " FEMALE")
                    
               sTweet = gen.GetName(util.Gender.Male)
                    
               if len(sTweet) > 0:
                    print("* Testing Innuendo Name Generator ID " + str(gen.ID) + " MALE (" + str(len(sTweet)) + " chars) *")
                    print("[" + sTweet + "]\n")
                    GeneratorPassList.append(str(gen.ID) + " MALE")
               else:
                    print("* ! ERROR: empty tweet (Innuendo Name Generator ID: " + str(gen.ID) + " MALE) ! *")
                    GeneratorFailList.append(str(gen.ID) + " MALE")
          except:
               GeneratorFailList.append("* ! Innuendo Name Generator: " + str(sys.exc_info()[0]) + " ! *")
               
     return [GeneratorPassList,GeneratorFailList]

def TestAllGens(bExcerpts = False, bExcTweetTxts = False, bTitles = False, bTitTweetTxts = False, bInnNames = False, bAll = False, bCreateImages = False):
     print("<=>Calling test functions<=>")
     
     Summaries = []
     
     if bExcerpts or bAll:
          Summaries.append(["Excerpt"] + TestExcerptGens(bCreateImages = bCreateImages))
     if bExcTweetTxts or bAll:
          Summaries.append(["Excerpt tweet text"] + TestExcerptTweetTextGens())
     if bTitles or bAll:
          Summaries.append(["Title"] + TestTitleGens(bCreateImages = bCreateImages))
     if bTitTweetTxts or bAll:
          Summaries.append(["Title tweet text"] + TestTitleTweetTextGens())
     if bInnNames or bAll:
          Summaries.append(["Innuendo name"] + TestInnNameGens())
          
     print("\n<=>SUMMARY<=>")
     for summary in Summaries:
          if not summary is None:
               print("\n" + summary[0] + " generators that passed OK: [" + str(summary[1]) + "]")
               print("\n" + summary[0] + " generators that *!FAILED!*: [" + str(summary[2]) + "]")
          else:
               print("!Empty summary!")
               
     if len(summary[2]) > 0:
          print("\n<=> * ! WARNING ! * " + str(len(summary[2])) + " Errors Found <=>")
     else:
          print("\n<=>SUCCESS! 0 Errors Detected!<=>")
          
# Execute functions!
Args = SetGetArgs()     
print(Args)

TestAllGens(bExcerpts = Args.excerpts, bExcTweetTxts = Args.extweettxt, bTitles = Args.titles, bTitTweetTxts = Args.tittweettxt, bInnNames = Args.innames, bAll = Args.all, bCreateImages = Args.createimages)
