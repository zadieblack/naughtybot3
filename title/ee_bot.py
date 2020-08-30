#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
 
import sys, argparse, time, datetime, threading, traceback
from pytz import timezone
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
            bAllowFavTweets = True,
            bLocal = False):
    print("=*=*=*= EROTICA_EBOOKS BOT IS RUNNING (@erotica_ebooks) =*=*=*=\n\n")
    print("InitBot() arguments:")
    print("  x iTweetTimer      = " + str(iTweetTimer))
    print("  x bTweet           = " + str(bTweet))
    print("  x iTweets          = " + str(iTweets))
    print("  x bLoop            = " + str(bLoop))
    print("  x iGeneratorNo     = " + str(iGeneratorNo))
    print("  x iTweetTxtNo      = " + str(iTweetTxtNo))
    print("  x bRedditPost      = " + str(bRedditPost))
    print("  x bAllowFavTweets  = " + str(bAllowFavTweets))
    print("  x bLocal           = " + str(bLocal))
    print("")
     
    sTweet = ""
    bTest = False 
     
    titutil.TweetHistoryQ = util.HistoryQWithLog(titutil.HISTORYQ_FILENAME)
    titutil.TweetTxtHistoryQ = util.HistoryQWithLog(titutil.TWEETTXT_HISTORYQ_FILENAME, iQSize = 20)
     
    try:
        api = InitTweepy()
          
        if iGeneratorNo != -1:
            bTest = True

        i = 0
        while i in range(0,iTweets) or bLoop:
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

                ImgTxtGen.TweetTxt = TweetTxtGen.TweetTxt()

                print("\n===Here is your " + str(len(ImgTxtGen.ImgTxt)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
                print("[" + ImgTxtGen.ImgTxt + "]")
                if len(ImgTxtGen.ImgTxt) > 0:
                        print("Tweet text: [" + ImgTxtGen.TweetTxt + "]")

                currentDT = datetime.datetime.utcnow()
                thisTZ = timezone("US/Eastern")
                currentDTaware = thisTZ.localize(currentDT)
                    
                image = CreateImg(ImgTxtGen)

                if bLocal:
                    image.save(titutil.TESTIMAGE_PATH + "eebot_" + GenerateFileName(), format = 'jpeg', quality = 'high')
                else:
                    status = None
                         
                    ImgFile = BytesIO() 
                    image.save(ImgFile, format = 'jpeg', quality = 'high')
                              
                if bTweet:
                    status = UpdateStatusWithImage(api, TweetTxtGen.TweetTxt(), ImgFile)          

                if bRedditPost and not status is None:
                    PostToReddit_eebot(sLinkTitle = TweetTxtGen.TweetTxt(), sLinkURL = util.ExtractURLFromStatus(status))

                print("* Tweeted at " + currentDTaware.strftime("%I:%M %p"))
                         
                titutil.TweetHistoryQ.LogHistoryQ()
                titutil.TweetTxtHistoryQ.LogHistoryQ()

            i += 1

    except IOError as e:
        print("*** ERROR in ee_bot() ***\nFile IO Error: " + str(e))
    except KeyboardInterrupt:
        print("Ending program ...")
    #except:
    #    print("*** ERROR in ee_bot() ***\n" + str(sys.exc_info()[0]))
     
    print("\n***Goodbye***\n")


