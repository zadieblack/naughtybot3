from random import shuffle
import title.util as util

def ShuffleFavs(sFileName = ""):
	if sFileName == "":
		sFileName = util.FAVTITLE_FILENAME
		
	sFavTitle = ""
	
	Titles = [""]
	iTitleCount = 0
		
	with open(sFileName, 'r') as infile:
		for line in infile:
			if line.strip() != util.FAVTITLE_DIVIDER:
				Titles[iTitleCount] += line 
			else:
				Titles.append("")
				iTitleCount += 1
	
	shuffle(Titles)
	
	with open(sFileName, 'w') as outfile:	
		for x in range(0, len(Titles)):
			outfile.write(Titles[x] + util.FAVTITLE_DIVIDER + "\n")

	
ShuffleFavs()