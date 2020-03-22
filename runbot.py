import sys, argparse
import excerpt.lust_bot
import title.ee_bot

def SetGetArgs():
     Parser = argparse.ArgumentParser(prog='lust_bot',description='Run Flaming Lust Bot for Twitter.')
     Parser.add_argument('-tweet', action='store_true', help='send generated tweets to Twitter? (default is False)')
     Parser.add_argument('-numtweets', type=int, default=1, help='number of tweets to generate before quitting (default is 1)')
     Parser.add_argument('-loop', action='store_true', help='loop infinitely until manually cancelled (default is False)')
     Parser.add_argument('-test', type=int, default=-1, help='type of tweet to generate for testing purposes')
     Parser.add_argument('-tweettimer', type=int, default=1800, help='num of seconds to wait before next tweet')
     Parser.add_argument('-testtweettxt', type=int, default=-1, help='tweet text generator # to test')
     Parser.add_argument('-reddit', action='store_true', help='post generated tweets to reddit? (default is False)')
     Parser.add_argument('-favtweets', action='store_false', help='use curated fav tweets from file? (default is True)')
     Parser.add_argument('-local', action='store_false', help='running from local machine? (default is True)')
     Parser.add_argument('-lustbot', action='store_true', help='run lust_bot only')
     Parser.add_argument('-eebot', action='store_true', help='run ee_bot only')
     return Parser.parse_args()
               
Args = SetGetArgs()     
#print(Args)

if not Args.eebot:
    excerpt.lust_bot.InitBot(Args.tweettimer, 
                             bTweet = Args.tweet, 
                             iTweets = Args.numtweets, 
                             bLoop = Args.loop, 
                             iGeneratorNo = Args.test, 
                             bRedditPost = Args.reddit,
                             bLocal = Args.local)

if not Args.lustbot:
    title.ee_bot.InitBot(Args.tweettimer, 
                         bTweet = Args.tweet, 
                         iTweets = Args.numtweets, 
                         bLoop = Args.loop, 
                         iGeneratorNo = Args.test, 
                         iTweetTxtNo = Args.testtweettxt, 
                         bRedditPost = Args.reddit, 
                         bAllowFavTweets = Args.favtweets,
                         bLocal = Args.local)