#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Twitter-related functions (Tweepy-based)

# FYI I have learned something about twitter and bot automation that I want to share. 
# I was having a lot of trouble with this bot's replies to people disappearing into 
# the ether. They were being sent. If I logged in as the bot I could see them. But 
# the recipient was not notified and sometimes the replies didnt show up even when I 
# searched for them. I googled everything I could think of and finally found a dev 
# who was saying that the name you registered your app with at app.twitter.com had 
# to match your bot's twitter handle. I updated my name to match, and within about 
# 30 minutes the problem was solved! So be sure that the name of your bot matches the 
# twitter handle it will be using. 

from io import BytesIO
from title.generators import *
import title.misc
import tweepy
import title.twitterauth

from random import *
from util import *

NUM_MORE_REPLIES = 7
REPLIES_FILE_NAME = "title/reply_ids.txt"
HASHTAG_LOVESCENE = "#lovescene"
HASHTAG_BOOKTITLE = "#book"

def InitTweepy():
     api = None
     
     # These twitter access codes are stored in a seperate file not included in the github repo. 
     # You must create your own. simply name it twitterauth.py and include the four variables below: 
     # ConsumerKey, ConsumerSecret, AccessKey, AccessSecret. Get these codes from https://apps.twitter.com/
     CONSUMER_KEY = title.twitterauth.ConsumerKey
     CONSUMER_SECRET = title.twitterauth.ConsumerSecret
     ACCESS_KEY = title.twitterauth.AccessKey
     ACCESS_SECRET = title.twitterauth.AccessSecret
     
     auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
     auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
     
     api = tweepy.API(auth, wait_on_rate_limit = True)
     
     return api
     
def UpdateStatus(api, Tweet, in_reply_to_status_id = ""):
     status = None 
     bTryToTweet = True 
     
     while bTryToTweet:
          try:
               status = api.update_status(Tweet, in_reply_to_status_id)
               bTryToTweet = False 
          except tweepy.TweepError as e:
               print("***TWITTER ERROR*** " + e.reason)     
               # if twitter throws certain over capacity errors, wait a few seconds and try again
               print(e.api_code)
               code = e.api_code
               if code in [88, 130, 131]:
                    bTryToTweet = True
                    time.sleep(30)
               else:
                    bTryToTweet = False

     return status 

def UpdateStatusWithImage(api, Tweet, ImgFile, in_reply_to_status_id = 0):
     status = None 
     bTryToTweet = True 
     
     while bTryToTweet:
          try:
               status = api.update_with_media(GenerateFileName(), Tweet, in_reply_to_status_id, file = ImgFile)
               bTryToTweet = False 
          except tweepy.TweepError as e:
               print("***TWITTER ERROR*** " + e.reason)     
               # if twitter throws certain over capacity errors, wait a few seconds and try again
               print(e.api_code)
               code = e.api_code
               if code in [88, 130, 131]:
                    bTryToTweet = True
                    time.sleep(30)
               else:
                    bTryToTweet = False

     return status 

def RespondToReplies(api, sFrom = ""):
     my_userid = '983078341241704448'
     max_id = None
     max_tweets = 60
     
     sTweet = ""
     sPrefix = ""
     
     HistoricReplies = []
     with open(REPLIES_FILE_NAME) as ReadReplyFile:
          HistoricReplies = ReadReplyFile.read().splitlines()
          
     #print("Historic reply IDs:")
     #print(HistoricReplies)
          
     query = "to:" + TWIT_USERNAME
     if sFrom != "":
          query += " from:" + sFrom
          
     try:          
          replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

          for reply in replies:
               if not reply.user.id_str == my_userid:
                    if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
                         print("Reply found (ID# " + reply.id_str + "): " + reply.text)
                         
                         sPrefix = "@" + reply.user.screen_name + " thanks for replying to me! Here is your " + misc.SexyAdjs().GetWord() + " ebook title! " + GetEmoji()
                         Gen = GetTweet(False, bAllowPromo = False)
                         sTweet = Gen.GenerateTweet()

                         status = None
                         print("===Here is your " + str(len(sTweet)) + " char tweet reply===")
                         print("[" + sTweet + "]")
                         print("Tweet text: [" + sPrefix + "]")
                         
                         if sTweet != "" and sPrefix != "":
                              ImgFile = BytesIO() 
                              CreateImg(sTweet).save(ImgFile, format = 'jpg')
                              
                              status = UpdateStatusWithImage(api, sPrefix, ImgFile, reply.id)     
                    
                         with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
                              WriteReplyFile.write(str(reply.id_str) + "\n")
          
     except tweepy.TweepError as e:
          print("***ERROR*** [" + e.reason + "]")
          
def RespondToMoreRequests(api, sFrom = ""):
     my_userid = '983078341241704448'
     max_id = None
     max_tweets = 60
     
     sTweet = ""
     sPrefix = ""
     
     HistoricReplies = []
     with open(REPLIES_FILE_NAME) as ReadReplyFile:
          HistoricReplies = ReadReplyFile.read().splitlines()
          
     #print("Historic reply IDs:")
     #print(HistoricReplies)
          
     query = "to:" + TWIT_USERNAME
     if sFrom != "":
          query += " from:" + sFrom
          
     try:          
          replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

          for reply in replies:
               if not reply.user.id_str == my_userid:
                    if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
                         sTweetText = reply.text
                         #print("Reply found (ID# " + reply.id_str + "): " + sTweetText)
                         
                         # find tweets from the controller that contain #more. 
                         istart = sTweetText.lower().find("#more")
                         if istart > -1:
                              istart += 5
                              
                              #print("Found '#more'. Remaining tweet: [" + sTweetText[istart:] + "]")
                              
                              sMoreNum = ""
                              while not sTweetText[istart].isdigit() and istart < len(sTweetText):
                                   istart += 1
                                   
                              #print("Skipped non-digits. Remaining tweet: [" + sTweetText[istart:] + "]")
                                   
                              while istart < len(sTweetText) and sTweetText[istart].isdigit():
                                   #print("character #" + str(istart) + " [" + sTweetText[istart] + "] is a digit.")
                                   sMoreNum += str(sTweetText[istart])
                                   istart += 1
                                   
                              #print("sMoreNum from [" + sTweetText + "] is " + sMoreNum)
                              xMore = 0
                              if sMoreNum != "":
                                   xMore = int(sMoreNum) 
                                   
                              for x in range(0, xMore):

                                   sPrefix = "@" + reply.user.screen_name + " "
                                   
                                   sTweet = GetTweet(False, False, bAllowPromo = False, bAllowFavTweets = False)

                                   status = None
                                   print("===Here is " + str(len(sPrefix + sTweet)) + " char tweet reply #" + str(x+1) + " of " + str(xMore) + "===")
                                   print("[" + sPrefix + sTweet + "]")
                                   
                                   if sTweet != "" and sPrefix != "":
                                        status = UpdateStatus(api, Tweet = sPrefix + sTweet, in_reply_to_status_id = reply.id)     
                         
                                   with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
                                        WriteReplyFile.write(str(reply.id_str) + "\n")
                                        
                                   time.sleep(.85)
                              time.sleep(3)
          
     except tweepy.TweepError as e:
          print("***ERROR*** [" + e.reason + "]")
          
def SaveFavorites(api, sFrom = ""):
     my_userid = '983078341241704448'
     max_id = None
     max_tweets = 60
     
     sTweet = ""
     sPrefix = ""
     
     HistoricReplies = []
     with open(REPLIES_FILE_NAME) as ReadReplyFile:
          HistoricReplies = ReadReplyFile.read().splitlines()
          
     #print("Historic reply IDs:")
     #print(HistoricReplies)
          
     query = "to:" + TWIT_USERNAME
     if sFrom != "":
          query += " from:" + sFrom
          
     try:          
          replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

          for reply in replies:
               if not reply.user.id_str == my_userid:
                    if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
                         sTweetText = reply.text

                         print("Reply found (ID# " + reply.id_str + "): " + sTweetText)
                         
                         # find tweets from the controller that contain #yes. 
                         if sTweetText.lower().find("#yes") > -1:     
                              if reply.in_reply_to_status_id is not None:
                                   root_tweet = api.get_status(reply.in_reply_to_status_id)
                                   
                                   sRootText = root_tweet.text
                                   sSkip = '@' + TWIT_CONTROLLER
                                   istart = sRootText.lower().find(sSkip)
                                   if istart > -1:
                                        istart += len(sSkip) + 1
                                   
                                   print("Original tweet is [" + sRootText[istart:] + "]")
                         
                                   with open(FAVTITLE_FILENAME, 'a') as WriteReplyFile:
                                        WriteReplyFile.write(str(sRootText[istart:]) + "\n///\n")
                                   
                                   with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
                                        WriteReplyFile.write(str(reply.id_str) + "\n")
          
     except tweepy.TweepError as e:
          print("***ERROR*** [" + e.reason + "]")


    