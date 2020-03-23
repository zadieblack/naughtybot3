import sys, argparse
import util as util
import title.util as titutil
from title.generators import *

Parser = argparse.ArgumentParser(prog='Curate',description='Curate favorite tweets.')
Parser.add_argument('-gen', type=int, default=0, help='tweet text generator # to curate')
Parser.add_argument('-maxlen', type=int, default=0, help='max chars of tweet text to generate')
Args = Parser.parse_args()

if Args.gen != 0:
     print("Curating tweets for Generator #" + str(Args.gen))
else:
     print("Curating random tweets.")

CurateFavorites(iGen = Args.gen, iMaxLen = Args.maxlen)
