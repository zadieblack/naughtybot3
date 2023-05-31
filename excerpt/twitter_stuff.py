#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Twitter-related functions (Tweepy-based)

# FYI I have learned something about twitter and bot 
# automation that I want to share. I was having a lot 
# of trouble with this bot's replies to people 
# disappearing into the ether. They were being sent. 
# If I logged in as the bot I could see them. But 
# the recipient was not notified and sometimes 
# the replies didnt show up even when I searched for 
# them.
# I googled everything I could think of and finally 
# found a dev who was saying that the name you 
# registered your app with at app.twitter.com had to 
# match your bot's twitter handle. I updated my name 
# to match, and within about 30 minutes the problem 
# was solved! So be sure that the name of your bot 
# matches the twitter handle it will be using. 

from io import BytesIO
from excerpt.generators import *
import excerpt.misc
import tweepy
import excerpt.twitterauth

from random import *
from util import *

REPLIES_FILE_NAME = "excerpt/reply_ids.txt"
HASHTAG_LOVESCENE = "#lovescene"
HASHTAG_BOOKTITLE = "#book"

def InitTweepy():
     api = None
     
     # These twitter access codes are stored in a seperate file not included in the github repo. You must create your own. simply name it twitterauth.py and include the four variables below: ConsumerKey, ConsumerSecret, AccessKey, AccessSecret. you get these codes from https://apps.twitter.com/
     CONSUMER_KEY = excerpt.twitterauth.ConsumerKey
     CONSUMER_SECRET = excerpt.twitterauth.ConsumerSecret
     ACCESS_KEY = excerpt.twitterauth.AccessKey
     ACCESS_SECRET = excerpt.twitterauth.AccessSecret
     BEARER_TOKEN = excerpt.twitterauth.BearerToken

     #auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
     auth = tweepy.OAuth1UserHandler(consumer_key = CONSUMER_KEY, 
                                     consumer_secret = CONSUMER_SECRET,
                                     access_token = ACCESS_KEY,
                                     access_token_secret = ACCESS_SECRET)
     auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


     #auth = tweepy.OAuth1UserHandler(consumer_key = CONSUMER_KEY, 
     #                                consumer_secret = CONSUMER_SECRET,
     #                                callback="oob")
     #print(auth.get_authorization_url())
     #verifier = input("Input PIN: ")
     #access_token, access_token_secret = auth.get_access_token(verifier)
     #auth.set_access_token(access_token, access_token_secret)

     #api = tweepy.API(auth, wait_on_rate_limit = True)
     
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

# # Upload media to Twitter APIv1.1
# ret = api.media_upload(filename="dummy_string", file=b)

# # Attach media to tweet
# api.update_status(media_ids=[ret.media_id_string], status="hello world")

def UpdateStatusWithImage(api, Tweet, ImgFile, in_reply_to_status_id = ""):
     status = None 
     bTryToTweet = True 
     while bTryToTweet:
          try:
               #status = api.update_status(status = "Pest tost")
               #print("Made a test post")
               #ret = api.media_upload(filename = GenerateFileName(), file = ImgFile)
               #print("Media uploaded")
               #status = api.update_status(status = Tweet, media_ids=[ret.media_id_string])
               status = api.update_status_with_media(status = Tweet, 
                                                     filename = GenerateFileName(), 
                                                     file = ImgFile)
               bTryToTweet = False 
          except tweepy.TweepyException as e:    
               print("\n***TWITTER ERROR***\n" + str(e))
               # if twitter throws certain over capacity errors, wait a few seconds and try again
               if not e.api_codes is None:
                   code = e.api_codes
                   if code in [88, 130, 131]:
                        bTryToTweet = True
                        time.sleep(30)
                   else:
                        bTryToTweet = False

     return status 

def RespondToReplies(api):
     my_userid = '973202601545273344'
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
          
     try:          
          replies = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

          for reply in replies:
               if not reply.user.id_str == my_userid:
                    if len(HistoricReplies) == 0 or not reply.id_str in HistoricReplies:
                         print("Reply found (ID# " + reply.id_str + "): " + reply.text)

                         sPrefix = "@" + reply.user.screen_name + " thanks for replying to me! Here is your love scene:"

                         Gen = GetTweet(False, bAllowPromo = False)
                         sTweet = Gen.GenerateTweet()

                         status = None
                         print("===Here is your " + str(len(sTweet)) + " char tweet reply===")
                         print("[" + sTweet + "]")
                         print("Tweet text: [" + sPrefix + "]")
                         
                         if sTweet != "" and sPrefix != "":
                              ImgFile = BytesIO() 
                              CreateImg(sTweet).save(ImgFile, format = 'PNG')
                              
                              status = UpdateStatusWithImage(api, sPrefix, ImgFile, reply.id_str)     
                         
                         with open(REPLIES_FILE_NAME, 'a') as WriteReplyFile:
                              WriteReplyFile.write(str(reply.id_str) + "\n")
          
     except tweepy.TweepError as e:
          print("***ERROR*** [" + e.reason + "]")

