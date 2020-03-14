#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
 
import sys, argparse, datetime, threading, traceback
import util as util
import title.util as titutil

from io import BytesIO
from random import *
from title.generators import *
from title.tweettext import *
from title.twitter_stuff import *
from title.texttoimg2 import *
from names import AuthorBuilder
from reddit import PostToReddit_eebot
     
def InitBot(iTweetTimer, 
            bTweet = False, 
            iTweets = 1, 
            bLoop = False, 
            iGeneratorNo = -1, 
            iTweetTxtNo = -1, 
            bRedditPost = False,
            bAllowFavTweets = True):
     print("=*=*=*= EROTICA_EBOOKS BOT IS RUNNING (@erotica_ebooks) =*=*=*=\n\n")
     print("===InitBot() iTweetTimer=" + str(iTweetTimer) + ", bTweet=" + str(bTweet) + ", iTweets=" + str(iTweets) + ",bLoop=" + str(bLoop) + ",iGeneratorNo=" + str(iGeneratorNo) + "\n")
     
     sTweet = ""
     bTest = False 
     
     titutil.TweetHistoryQ = util.HistoryQWithLog(titutil.HISTORYQ_FILENAME)
     titutil.TweetTxtHistoryQ = util.HistoryQWithLog(titutil.TWEETTXT_HISTORYQ_FILENAME, iQSize = 20)
     
     try:
          api = InitTweepy()
          
          if iGeneratorNo == -1:
               iGeneratorNo = MAX_GENERATOR_NO
          else:
               bTest = True
          i = 0
          while i in range(0,iTweets) or bLoop:
               # Tweets = [1]
               ImgTxtGen = None 
               TweetTxtGen = None

               ImgTxtGen = GetTweet(bTest, 
                                    bTweet, 
                                    iGeneratorNo, 
                                    bAllowPromo = True, 
                                    TweetHistoryQ = titutil.TweetHistoryQ, 
                                    bAllowFavTweets = bAllowFavTweets)
               
               #ImgTxtGen.SetImgText("I Secretly Impregnated\nMy Naked Slutty Italian Elf Step-Mom!")
               #ImgTxtGen.ImgTxt = "I Secretly Impregnated\nMy Naked Slutty Italian Elf Step-Mom"

               if not ImgTxtGen.ImgTxt is None:
                    TweetTxtGen = GetTweetText(bTest = bTest, 
                                               iGeneratorNo = iTweetTxtNo,
                                               TweetTxtHistoryQ = titutil.TweetTxtHistoryQ, 
                                               sAuthorName = ImgTxtGen.AuthorName, 
                                               AuthorGender = ImgTxtGen.AuthorGender)
                    #ImgTxtGen.SetImgText("Hunted for Food\nby the\nWanton Sex God")
                    ImgTxtGen.TweetTxt = TweetTxtGen.TweetTxt()

                    print("\n===Here is your " + str(len(ImgTxtGen.ImgTxt)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
                    print("[" + ImgTxtGen.ImgTxt + "]")
                    if len(ImgTxtGen.ImgTxt) > 0:
                            print("Tweet text: [" + ImgTxtGen.TweetTxt + "]")

                    currentDT = datetime.datetime.now()
                    
                    CreateImg(ImgTxtGen).save(titutil.TESTIMAGE_PATH + GenerateFileName(), format = 'PNG')
                    
                    #if bTweet:  <-- uncomment before deploying
                    if False:
                            status = None
                         
                            ImgFile = BytesIO() 
                            #CreateImg(sTweet).save(ImgFile, format = 'PNG')
                            CreateImg(TitleTweet).save(ImgFile, format = 'PNG')
                              
                            if status == None:
                                pass
                                status = UpdateStatusWithImage(api, TweetTxtGen.TweetTxt(), ImgFile)          
                            else:
                                #pass
                                ImgFile = BytesIO() 
                                CreateImg(sTweet).save(ImgFile, format = 'PNG')
                              
                                #status = UpdateStatusWithImage(api, TweetTxtGen.TweetTxt(), ImgFile, status.id)  
                              
                            #if bRedditPost and not status is None:
                            #    PostToReddit_eebot(sLinkTitle = TweetTxtGen.TweetTxt(), sLinkURL = util.ExtractURLFromStatus(status))

                            print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
                         
                            titutil.TweetHistoryQ.LogHistoryQ()
                            titutil.TweetTxtHistoryQ.LogHistoryQ()
                            
               
     
                    # else:
                         # with open(GenerateFileName(), 'wb') as file:
                              # file.write(ImgFile.getvalue())
               i += 1

     except KeyboardInterrupt:
          print("Ending program ...")
     finally:
          # e.set()
          
          print("***Goodbye***")


