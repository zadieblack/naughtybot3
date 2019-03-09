from title.generators import *
import title.misc
import title.util

def CurateFavorites():
	sInput = ""
	
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
				print("Favorited tweet and saved.")
			
		# If [q], quit.
		elif sInput.lower().strip() == "q":
			break
		
		# If [n], do nothing and loop.
		else:
			print("Skipped.")
			
			
CurateFavorites()