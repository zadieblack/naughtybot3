#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Utilities module

import os, time, sys, random

from random import *
from enum import * 

MAX_TWITTER_CHARS = 280
MAX_GENERATOR_NO = 44
MAX_SEARCH_LOOPS = 8
TWIT_USERNAME = 'erotica_ebooks'
TWIT_CONTROLLER = 'zadieblack'

Q_SIZE = 40
HISTORYQ_FILENAME = 'title/history_q.txt'
TWEETTXT_HISTORYQ_FILENAME = 'title/tweettxt_history_q.txt'
FAVTITLE_FILENAME = 'title/fav_titles.txt'
FAVTITLE_DIVIDER = "~~~"

TESTIMAGE_PATH = 'testimages/'

TweetHistoryQ = None

class TempType(Enum):
     Short = 1
     Medium = 2
     Flowery = 3
     
class Tense(Enum):
     Present = 1
     Past = 2
     Gerund = 3
     
class LocInOutType(Enum):
     Indoors = 1
     Outdoors = 2
     Either = 3
     
class LocPubPrivType(Enum):
     Public = 1
     Private = 2
     Either = 3
     
class GeneratorType(Enum):
     Normal = 1
     Promo = 2
     Test = 3
     BookTitle = 4
     
class GirlType(Enum):
     Good = 1
     Bad = 2
     Neutral = 3
     
class MaleCharType(Enum):
     Straight = 1
     GangAny = 2
     GangSingular = 3
     GangPlural = 4
     Gay = 5
                    
          
     