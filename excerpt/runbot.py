import sys, argparse
import lust_bot

def SetGetArgs():
	Parser = argparse.ArgumentParser(prog='lust_bot',description='Run Flaming Lust Bot for Twitter.')
	Parser.add_argument('-tweet', action='store_true', help='send generated tweets to Twitter? (default is False)')
	Parser.add_argument('-numtweets', type=int, default=1, help='number of tweets to generate before quitting (default is 1)')
	Parser.add_argument('-loop', action='store_true', help='loop infinitely until manually cancelled')
	Parser.add_argument('-test', type=int, default=-1, help='type of tweet to generate for testing purposes')
	Parser.add_argument('-tweettimer', type=int, default=1800, help='num of seconds to wait before next tweet')
	Parser.add_argument('-replytimer', type=int, default=300, help='num of seconds to wait before running reply routine')
	
	return Parser.parse_args()
			
Args = SetGetArgs()	
print(Args)

lust_bot.InitBot(Args.tweettimer, Args.replytimer, bTweet = Args.tweet, iTweets = Args.numtweets, bLoop = Args.loop, iGeneratorNo = Args.test)