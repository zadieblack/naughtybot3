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
     
def InitBot(iTweetTimer, bTweet = False, iTweets = 1, bLoop = False, iGeneratorNo = -1, iTweetTxtNo = -1, bRedditPost = False):
     print("=*=*=*= EROTICA_EBOOKS BOT IS RUNNING (@erotica_ebooks) =*=*=*=\n\n")
     print("===InitBot() iTweetTimer=" + str(iTweetTimer) + ", bTweet=" + str(bTweet) + ", iTweets=" + str(iTweets) + ",bLoop=" + str(bLoop) + ",iGeneratorNo=" + str(iGeneratorNo) + "\n")
     
     sTweet = ""
     bTest = False 
     
     titutil.TweetHistoryQ = util.HistoryQWithLog(titutil.HISTORYQ_FILENAME)
     titutil.TweetTxtHistoryQ = util.HistoryQWithLog(titutil.TWEETTXT_HISTORYQ_FILENAME, iQSize = 4)
     
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

               TitleTweet = GeneratedTitleTweet()

               gender = Gender.Neuter
               if CoinFlip():
                   gender = Gender.Female
               else:
                   gender = Gender.Male

               TitleTweet.SetAuthorGender(gender)
               TitleTweet.SetAuthorName(AuthorBuilder(gender))

               ImgTxtGen = GetTweet(bTest, bTweet, iGeneratorNo, bAllowPromo = True, TweetHistoryQ = titutil.TweetHistoryQ, bAllowFavTweets = False)
               if not ImgTxtGen is None:
                    TweetTxtGen = GetTweetText(bTest, 
                                               iGeneratorNo = iGeneratorNo,
                                               TweetTxtHistoryQ = titutil.TweetTxtHistoryQ, 
                                               sAuthorName = TitleTweet.AuthorName(), 
                                               AuthorGender = TitleTweet.AuthorGender())
                    
                    TitleTweet.SetImgTxt(ImgTxtGen.TweetImgTxt())
                    TitleTweet.SetTweetTxt(TweetTxtGen.TweetTxt())

                    print("\n===Here is your " + str(TitleTweet.ImgTxtLen()) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
                    print("[" + TitleTweet.ImgTxt() + "]")
                    if TitleTweet.TweetTxtLen() > 0:
                            print("Tweet text: [" + TitleTweet.TweetTxt() + "]")

                    currentDT = datetime.datetime.now()
                    
                    CreateImg(TitleTweet).save(GenerateFileName(), format = 'PNG')
                    
                    #if bTweet:
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


