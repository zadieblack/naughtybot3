from decimal import Decimal
import sys, argparse
from title.generators import *
import util as util 
import title.misc as titmisc
import title.util as titutil
from names import AuthorBuilder

def CurateFavorites(iGen = 0):
        sInput = ""
        iSkipCount = 0
        iAddCount = 0

        ImgTxtGen = None
     
        while True:
        # Create Title 
            sDetailsLine = ""
            sTxtLine = ""
            sOutput = ""
          
            if iGen != 0:
        # Create Titles for specific generator
                ImgTxtGen = GetTweet(bTest = True, bTweet = False, iGeneratorNo = iGen, bAllowPromo = False, bAllowFavTweets = False)
            else:
        # Create Titles from random generators
                ImgTxtGen = GetTweet(bTest = False, bTweet = False, iGeneratorNo = 0, bAllowPromo = False, bAllowFavTweets = False)

        # Get author 
            ImgTxtGen.AuthorName = AuthorBuilder(ImgTxtGen.AuthorGender)

        # Create output string for writing 
            sDetailsLine += "[" + str(ImgTxtGen.ID) + "]"
            sDetailsLine += "[" + str(ImgTxtGen.Template.ID) + "]"
            sDetailsLine += "[" + ImgTxtGen.AuthorName + "]"
            sDetailsLine += "[" + str(ImgTxtGen.AuthorGender).split(".")[1] + "]" 
            sTxtLine += ImgTxtGen.ImgTxt.strip()
            sOutput = "{{" + sDetailsLine + "}}\n" + sTxtLine  + "\n" + FAVTITLE_DIVIDER + "\n"

        # Print generated title and info
            print(sOutput)

        # Prompt user.
            sInput = input("\nKeep suggested title? [y]es, [n]o, or [q]uit: ")
          
        # If [y], save tweet.
            if sInput.lower().strip() == "y":
                with open(FAVTITLE_FILENAME, 'a+') as WriteReplyFile:

                    WriteReplyFile.write(sOutput)

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