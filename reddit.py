#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import pkg_resources
pkg_resources.require("praw==6.5.1")
import praw

SUBREDDIT_NAME = 'erotica_ebooks'

def PostToReddit(sLinkTitle, sLinkURL, sFlairID):
    try:
        reddit = praw.Reddit('bot1')

        subreddit = reddit.subreddit(SUBREDDIT_NAME)

        print("subreddit: {" + str(subreddit) + "}\n")
        print("subreddit.title: " + sLinkTitle)
        print("subreddit.url: " + sLinkURL)
        print("subreddit.flair_id: " + sFlairID)
        print("subreddit.nsfw: " + str(True))
        print("subreddit.resubmit: " + str(False))

        subreddit.submit(title = sLinkTitle, 
                            url = sLinkURL, 
                            flair_id = sFlairID, 
                            nsfw = True,
                            resubmit = False)
    except praw.exceptions.PRAWException as e:
        print("* ! PRAW Error: " + e.reason + " ! *")

def PostToReddit_eebot(sLinkTitle, sLinkURL):
    sFlairID = "0968a470-362f-11ea-a7cd-0e19e0d6966d"

    PostToReddit(sLinkTitle, sLinkURL, sFlairID)

def PostToReddit_botlust(sLinkTitle, sLinkURL):
    sFlairID = "12906c9a-362f-11ea-ad00-0e251d7edbcb"

    PostToReddit(sLinkTitle, sLinkURL, sFlairID)