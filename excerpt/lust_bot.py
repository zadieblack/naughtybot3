#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# launcher code for flaminglustbot. run this.
 
import sys, argparse, datetime, threading, traceback

#import excerpt.bodyparts
#import excerpt.names
#from excerpt.locations import *
#import excerpt.people
#import excerpt.verbs
#import excerpt.misc
#import excerpt.scenes

from io import BytesIO
from random import *
import util as util 
import excerpt.util as exutil
import excerpt.generators as generators 
from excerpt.tweettext import *
from excerpt.twitter_stuff import *
import excerpt.texttoimg 
from excerpt.texttoimg import CreateImg
from reddit import PostToReddit_botlust
     
def InitBot(iTweetTimer, 
            bTweet = False, 
            iTweets = 1, 
            bLoop = False, 
            iGeneratorNo = -1, 
            bRedditPost = False,
            bLocal = False):
    print("=*=*=*= FLAMING LUST BOT IS RUNNING (@bot_lust) =*=*=*=\n\n")
    print("InitBot() arguments:")
    print("  x iTweetTimer         = " + str(iTweetTimer))
    print("  x bTweet              = " + str(bTweet))
    print("  x iTweets             = " + str(iTweets))
    print("  x bLoop               = " + str(bLoop))
    print("  x iGeneratorNo        = " + str(iGeneratorNo))
    print("  x bRedditPost         = " + str(bRedditPost) + "\n")
    print("  x bLocal              = " + str(bLocal)) 
     
    sTweet = ""
    bTest = False 
     
    exutil.TweetHistoryQ = util.HistoryQWithLog(exutil.HISTORYQ_FILENAME)
    exutil.TweetTxtHistoryQ = util.HistoryQWithLog(exutil.TWEETTXT_HISTORYQ_FILENAME, exutil.TWEETTXT_Q_SIZE)
     
    try:
          
        api = InitTweepy()
          
        if iGeneratorNo == -1:
            iGeneratorNo = MAX_GENERATOR_NO
            #print("InitBot() Not in test mode.")
        else:
            bTest = True
            #print("InitBot() In test mode.")
          
        i = 0
        while i in range(0,iTweets) or bLoop:
            #Tweets = [1]
            Gen = None 
            sTweet = ""
            sText = ""
               
            #Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True)
            #print("Generator ID: " + str(Gen.ID))
            Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True, TweetHistoryQ = exutil.TweetHistoryQ)
               
            sTweet = Gen.GenerateTweet()
            if len(sTweet) > 0:
                if Gen.Type != GeneratorType.Promo:
                        sText = GetImgTweetText(bTest = False, TweetTxtHistoryQ = exutil.TweetTxtHistoryQ)
                    
                print("\n===Here is your " + str(len(sTweet)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
                print("[" + sTweet + "]")
                if len(sText) > 0:
                    print("Tweet text: [" + sText + "]")

                currentDT = datetime.datetime.now()

                image = CreateImg(sTweet) 

                if bLocal:
                    image.save(exutil.TESTIMAGE_PATH + "lustbot_" + util.GenerateFileName(), format = 'jpeg', quality = 'high')
                else:        
                    status = None 

                    if bTweet:
                        if Gen.Type == GeneratorType.Promo:
                            status = UpdateStatus(api, sTweet)
                        else:
                            ImgFile = BytesIO() 
                            CreateImg(sTweet).save(ImgFile, format = 'jpeg', quality = 'high')
                                   
                            status = UpdateStatusWithImage(api, sText, ImgFile)    
                                
                            print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
              
                        if bRedditPost == True and not status is None:
                            PostToReddit_botlust(sLinkTitle = sText, sLinkURL = util.ExtractURLFromStatus(status))

                excerpt.util.TweetHistoryQ.LogHistoryQ()
                              
            i += 1
    except IOError as e:
        print("*** ERROR in lust_bot() ***\nFile IO Error: " + str(e))
        excerpt.util.TweetHistoryQ.LogHistoryQ()
    except KeyboardInterrupt:
        print("Ending program ...")
          
    finally:
        # e.set()
        print("\n***Goodbye***\n")


