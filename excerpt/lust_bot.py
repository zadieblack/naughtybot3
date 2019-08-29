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
#from excerpt.util import *
#import excerpt.util
import excerpt.util as exutil
#from excerpt.generators import *
import excerpt.generators as generators 
from excerpt.twitter_stuff import *
	
def InitBot(iTweetTimer, bTweet = False, iTweets = 1, bLoop = False, iGeneratorNo = -1):
	print("=*=*=*= FLAMING LUST BOT IS RUNNING (@bot_lust) =*=*=*=\n\n")
	print("===InitBot() iTweetTimer=" + str(iTweetTimer) + ", bTweet=" + str(bTweet) + ", iTweets=" + str(iTweets) + ",bLoop=" + str(bLoop) + ",iGeneratorNo=" + str(iGeneratorNo) + "\n") 
	
	sTweet = ""
	bTest = False 
	
	exutil.TweetHistoryQ = exutil.HistoryQWithLog(exutil.HISTORYQ_FILENAME)
	
	try:
		
		api = InitTweepy()
		
		if iGeneratorNo == -1:
			iGeneratorNo = MAX_GENERATOR_NO
			print("InitBot() Not in test mode.")
		else:
			bTest = True
			print("InitBot() In test mode.")
		
		i = 0
		while i in range(0,iTweets) or bLoop:
			#Tweets = [1]
			Gen = None 
			sTweet = ""
			sText = ""
			
			Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True)
			#print("Generator ID: " + str(Gen.ID))
			while bTweet and not excerpt.util.TweetHistoryQ.PushToHistoryQ(Gen.ID):
				Gen = GetTweet(bTest, iGeneratorNo, bAllowPromo = True)
			
			sTweet = Gen.GenerateTweet()
			if len(sTweet) > 0:
				if Gen.Type != GeneratorType.Promo:
					sText = GetImgTweetText(Gen)
				
				print("\n===Here is your " + str(len(sTweet)) + " char tweet (" + str(i + 1) + " of " + str(iTweets) + ")===")
				print("[" + sTweet + "]")
				if len(sText) > 0:
					print("Tweet text: [" + sText + "]")
					
				currentDT = datetime.datetime.now()
				if bTweet:
					print("* Tweeted at " + currentDT.strftime("%H:%M:%S"))
						
					status = None
						
					if status == None:
						#pass
						#status = UpdateStatus(api, tweet)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet)
						else:
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sText, ImgFile)		
					else:
						#pass
						#status = UpdateStatus(api, tweet, status.id)
						if Gen.Type == GeneratorType.Promo:
							status = UpdateStatus(api, sTweet, status.id)
						else:
							ImgFile = BytesIO() 
							CreateImg(sTweet).save(ImgFile, format = 'PNG')
							
							status = UpdateStatusWithImage(api, sText, ImgFile, status.id)	
					
					excerpt.util.TweetHistoryQ.LogHistoryQ()
						
			i += 1
	except KeyboardInterrupt:
		print("Ending program ...")
		
	finally:
		# e.set()
		print("***Goodbye***")


