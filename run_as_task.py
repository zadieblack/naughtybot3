#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import argparse, datetime, logging, socket, sys, time
from pytz import timezone
from random import *

lock_socket = None  # we want to keep the socket open until the very end of
                    # our script so we use a global variable to avoid going
                    # out of scope and being garbage-collected

def is_lock_free():
    global lock_socket
    lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        lock_id = "zadieblack.twitterbot3"   # this should be unique. using your username as a prefix is a convention
        lock_socket.bind('\0' + lock_id)
        logging.debug("Acquired lock %r" % (lock_id,))
        return True
    except socket.error:
        # socket already locked, task must already be running
        logging.info("Failed to acquire lock %r" % (lock_id,))
        return False

if not is_lock_free():
    logging.info("Bot already running.")
    sys.exit()
     
def SetGetArgs():
    Parser = argparse.ArgumentParser(prog='naughtybots',description='Run Flaming Lust Bot & erotica_ebooks for Twitter.')
    Parser.add_argument('-tweettimer', type=int, default=9000, help='num of seconds to wait before next tweet')
     
    return Parser.parse_args()

# then, either include the rest of your script below,
# or import it, if it's in a separate file:
import excerpt.lust_bot 
import title.ee_bot

Args = SetGetArgs()     
print(Args)

iTweetTimer = Args.tweettimer 
currentDT = datetime.datetime.utcnow()
thisTZ = timezone("US/Eastern")
currentDTaware = thisTZ.localize(currentDT)

while True:
    iRand = randint(2,3)
    print("+ randint(2,3) = " + str(iRand))
    if iRand != 1:
        #pass
        print("+ running bot lust")
        excerpt.lust_bot.InitBot(180, bTweet = True, bLoop = False, bRedditPost = False)
    else:
        print("+ skipping bot lust")

    title.ee_bot.InitBot(180, bTweet = True, bLoop = False, bRedditPost = False)
    currentDTaware = thisTZ.localize(datetime.datetime.utcnow())
    
    print("* Tweeted at " + currentDTaware.strftime("%I:%M %P"))

    if iTweetTimer > 180:
        iRandSecs = iTweetTimer
               
        iRandSecs = randint(int(iRandSecs - (iRandSecs * (1/3))), int(iRandSecs + (iRandSecs * (1/3))))
        dtNext = currentDTaware + datetime.timedelta(seconds = iRandSecs)
        print("* Next tweets in " + str(datetime.timedelta(seconds = iRandSecs)) + " (" + dtNext.strftime("%I:%M %P") + ")...")
        time.sleep(iRandSecs)
    else:
        dtNext = currentDTaware + datetime.timedelta(seconds = iTweetTimer)
        print("* Next tweets in " + str(datetime.timedelta(seconds = iTweetTimer)) + " minutes (" + dtNext.strftime("%I:%M %P") + ")...")
        time.sleep(iTweetTimer)
