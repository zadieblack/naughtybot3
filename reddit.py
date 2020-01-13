#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import praw

SUBREDDIT_NAME = 'erotica_ebooks'

def PostToReddit(sLinkTitle, sLinkURL, iFlairID):
    try:
        reddit = praw.Reddit('bot1')

        subreddit = reddit.subreddit(SUBREDDIT_NAME)

        subreddit.submit(title = sLinkTitle, 
                            url = sLinkURL, 
                            flair_id = iFlairID, 
                            nsfw = True,
                            resubmit = False)
    except praw.exceptions.PRAWException as e:
        print("* ! PRAW Error: " + e.reason + " ! *")

def PostToReddit_eebot(sLinkTitle, sLinkURL):
    iFlairID = "0968a470-362f-11ea-a7cd-0e19e0d6966d"

    PostToReddit(sLinkTitle, sLinkURL, iFlairID)

def PostToReddit_botlust(sLinkTitle, sLinkURL):
    iFlairID = "12906c9a-362f-11ea-ad00-0e251d7edbcb"

    PostToReddit(sLinkTitle, sLinkURL, iFlairID)