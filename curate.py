from decimal import Decimal
import sys, argparse
from title.generators import *
import title.misc
import title.util

def CurateFavorites(iGen = 0):
     sInput = ""
     iSkipCount = 0
     iAddCount = 0
     
     while True:
          # Create Title and output.
          sTweet = ""
          if iGen != 0:
               sTweet = GetTweet(True, False, iGeneratorNo = iGen, bAllowPromo = False, bAllowFavTweets = False)
          else:
               sTweet = GetTweet(False, False, iGeneratorNo = iGen, bAllowPromo = False, bAllowFavTweets = False)
          print("\nGenerated tweet:\n[" + sTweet + "]")
          
          # Prompt user.
          sInput = input("\nKeep suggested title? [y]es, [n]o, or [q]uit: ")
          
          # If [y], save tweet.
          if sInput.lower().strip() == "y":
               with open(FAVTITLE_FILENAME, 'a') as WriteReplyFile:
                    WriteReplyFile.write(str(sTweet) + "\n///\n")
                    iAddCount += 1
                    print("Favorited tweet and saved.")
               
          # If [q], quit.
          elif sInput.lower().strip() == "q":
               dPerRejects = 100
               if (iAddCount + iSkipCount) != 0:
                    dPerRejects = round((Decimal(iSkipCount)/Decimal(iAddCount + iSkipCount))*100,2)
                    
               print("\nFavorited " + str(iAddCount) + ", rejected " + str(iSkipCount) + ". " + str(dPerRejects) + "% rejection rate.")
               break
          
          # If [n], do nothing and loop.
          else:
               iSkipCount += 1
               print("Skipped.")
               
Parser = argparse.ArgumentParser(prog='Curate',description='Curate favorite tweets.')
Parser.add_argument('-gen', type=int, default=0, help='tweet text generator # to curate')
Args = Parser.parse_args()

if Args.gen != 0:
     print("Curating tweets for Generator #" + str(Args.gen))
else:
     print("Curating random tweets.")

CurateFavorites(iGen = Args.gen)