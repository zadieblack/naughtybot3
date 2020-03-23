#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
MAX_SEARCH_LOOPS = 8
TWIT_USERNAME = 'bot_lust'

TESTIMAGE_PATH = 'testimages/'

Q_SIZE = 30
HISTORYQ_FILENAME = 'excerpt/history_q.txt'
TWEETTXT_HISTORYQ_FILENAME = 'title/tweettxt_history_q.txt'

TAG_PEN = "sex act with penetration scene"
TAG_NON_PEN = "non-penetrative sex act scene"
TAG_DONE_TO_HER = "done to her scene"
TAG_DONE_TO_HIM = "done to him scene"
TAG_CLIMAX = "orgasm scene"
TAG_POSITION = "sex position scene"
TAG_FOREPLAY = "foreplay scene"
TAG_ABOVE_BELT = "above-the-belt sex act scene"
TAG_BELOW_BELT = "below-the-belt sex act scene"
TAG_ORAL = "oral sex scene"
TAG_CLOTHED = "scene where they still have clothes on"

TweetHistoryQ = None
     
class Tense(IntEnum):
     Present = 1
     Past = 2
     Gerund = 3
     
class LocInOutType(IntEnum):
     Indoors = 1
     Outdoors = 2
     Either = 3
     
class LocPubPrivType(IntEnum):
     Public = 1
     Private = 2
     Either = 3
     
class GeneratorType(IntEnum):
     Normal = 1
     Promo = 2
     Test = 3
     BookTitle = 4

