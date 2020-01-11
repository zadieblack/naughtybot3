from random import shuffle
import title.util as util

def ShuffleFavs(sFileName = ""):
     if sFileName == "":
          sFileName = util.FAVTITLE_FILENAME
          
     sFavTitle = ""
     
     Titles = []
     Titles.append("")
     iTitleCount = 0
          
     with open(sFileName, 'r') as infile:
          for line in infile:
               #print(str(iTitleCount) + "     [" + line + "]")
               if line.strip() == util.FAVTITLE_DIVIDER:
                    #print("Divider Found.")
                    Titles.append("")
                    iTitleCount += 1
               elif not line.strip():
                    # do nothing
                    pass
               else:
                    Titles[iTitleCount] += line 
     
     print("***BEFORE SHUFFLE***")
     print("There are " + str(len(Titles)) + " favorited titles.")
     shuffle(Titles)
     print("***AFTER SHUFFLE***")
     print("There are " + str(len(Titles)) + " favorited titles.")
     
     CleanTitles = []
     for x in range(0, len(Titles)):
          if Titles[x].strip():
               CleanTitles.append(Titles[x])
     
     print("***AFTER CLEANING***")
     print("There are " + str(len(CleanTitles)) + " favorited titles.")
     with open(sFileName, 'w') as outfile:     
          for x in range(0, len(CleanTitles)):
               if CleanTitles[x].endswith('\n'):
                    outfile.write(CleanTitles[x] + util.FAVTITLE_DIVIDER + "\n")
               else:
                    outfile.write(CleanTitles[x] + "\n" + util.FAVTITLE_DIVIDER + "\n")

     
ShuffleFavs()