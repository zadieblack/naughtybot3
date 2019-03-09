from decimal import Decimal
from title.generators import *
import title.misc
import title.util

def CurateFavorites():
	sInput = ""
	iSkipCount = 0
	iAddCount = 0
	
	while True:
		# Create Title and output.
		sTweet = ""
		sTweet = GetTweet(False, False, bAllowPromo = False, bAllowFavTweets = False)
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
			print("\nFavorited " + str(iAddCount) + ", rejected " + str(iSkipCount) + ". " + str(round((Decimal(iSkipCount)/Decimal(iAddCount + iSkipCount))*100,2)) + "% rejection rate.")
			break
		
		# If [n], do nothing and loop.
		else:
			iSkipCount += 1
			print("Skipped.")
			
			
CurateFavorites()