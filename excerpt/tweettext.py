from random import *
from util import *
from gen import *
from misc import *
from names import *
from title.generators import GetTweet
import excerpt.bodyparts

MAX_EXCERPT_BOOKTITLE_LEN = 65

TweetTxtHistoryQ = HistoryQ(10)

def LastNameBuilder(NotList = None):
     sLName = ""
     
     Names = []
     
     if NotList == None:
          NotList = []
     
     sName1 = AuthorLastNames().GetWord(NotList = NotList)
     sName2 = AuthorLastNames().GetWord(NotList = [sName1] + NotList)
     
     for _ in range(3):
          Names.append(sName1)
     
     Names.append(sName1 + "-" + sName2)
     
     sLName = Names[randint(0, len(Names) - 1)]
     
     return sLName
          
def AuthorBuilder(gender = Gender.Neuter):
     return GetInnName(gender)

def AddHashtag(Tweets):
     # if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
     if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
          sHashtag = "\n#" + misc.Hashtags().GetWord()
          if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
               Tweets[len(Tweets) - 1] += sHashtag

     return Tweets
     
def BookTitleBuilder(maxlen = None):
     if maxlen is None:
          maxlen = MAX_EXCERPT_BOOKTITLE_LEN
          
     if not isinstance(maxlen, int):
          maxlen = MAX_EXCERPT_BOOKTITLE_LEN
         
     sTitle = ""
     gen = GetTweet(bTest = False, bTweet = False, bAllowPromo = False, bAllowFavTweets = False)
     sTitle = gen.ImgTxt
     while len(sTitle) > maxlen:
          gen = GetTweet(bTest = False, bTweet = False, bAllowPromo = False, bAllowFavTweets = False)
          sTitle = gen.ImgTxt
          
     sTitle = sTitle.replace('\n',' ').replace(':',' - ').replace('\"','')
     sTitle = sTitle.replace('  ',' ') #remove double spaces
     return sTitle
     
class TweetTxtGen(Generator):
     def SetPriority(self, sText, List, iPriority):
          for x in range(iPriority):
               List.append(sText)
     
     def GenerateTweet(self):
          self.BookSellers = BookSellers()
          self.Hashtags = Hashtags()
          self.SexyAdjs = SexyAdjs()
          
          return ""
          
class TweetTxtGen1(TweetTxtGen):
     # "Punished by the handsome Swedish prime minister" is the sexy read 
     # that was BANNED on Amazon!
     # Now available on Wattpad from Dick Spunk
     def __init__(self):          
          super().__init__(ID = 1, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "\"" + BookTitleBuilder() + "\" is the "
          sText += self.SexyAdjs.GetWord() + " " + WordList(["read", "book", "ebook"]).GetWord() + " "
          sText += "that was " + WordList(["BANNED on", "TOO HOT for", "TOO FILTHY for", "too much for"]).GetWord() + " "
          sText += "Amazon! Now available on " + self.BookSellers.GetWord(NotList = ["Amazon", "Kindle Unlimited"]) 
          if CoinFlip():
               sText += " (from " + AuthorBuilder() + ")"
          #=============================
          
          return sText
          
class TweetTxtGen2(TweetTxtGen):
     # "Punished by the handsome Swedish prime minister" is now available 
     # on Kindle. By Ben Dover
     def __init__(self):     
          super().__init__(ID = 2, Priority = GenPriority.Low)     
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sBookSeller = self.BookSellers.GetWord()
          
          sText = "\"" + BookTitleBuilder() + "\" is "
          sText += WordList(["coming soon on", "now available on", "available to download from", "out soon on", 
                                "available to download on", "out now on",
                               ]).GetWord() 
          sText += " " + sBookSeller 
          sText += ". By " + AuthorBuilder()
          
          return sText
          
class TweetTxtGen3(TweetTxtGen):
     # "Punished by the handsome Swedish prime minister" is coming soon 
     # to discerning readers on Amazon. By Ben Dover
     def __init__(self):          
          super().__init__(ID = 3, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sBookSeller = self.BookSellers.GetWord()
          
          sText = "\"" + BookTitleBuilder() + "\" is "
          sText += WordList(["now available", "coming soon", "available now"]).GetWord() + " to " 
          sText += WordList(["discerning", "discrete", "discriminating"]).GetWord() + " readers on " + sBookSeller 
          sText += "! By " + AuthorBuilder()
          
          return sText
                    
class TweetTxtGen4(TweetTxtGen):
     # Get excited! The wait is over for Ben Dover's latest sexy release, 
     # "Punished by the handsome Swedish prime minister"!
     def __init__(self):          
          super().__init__(ID = 4, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["At last!","At last!","At last!", "Finally!","Finally!", "Get excited!", "It's here!"]).GetWord() + " "
          sText += "The wait is over for " + AuthorBuilder() + "'s " + WordList(["newest", "latest"]).GetWord() + ", " 
          sText += "\"" + BookTitleBuilder() + "\"!"
          
          return sText
          
class TweetTxtGen5(TweetTxtGen):
     # Out soon from Ben Dover
     def __init__(self):
          super().__init__(ID = 5, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Check out this " + self.SexyAdjs.GetWord() + " excerpt from "
          sText += "\"" + BookTitleBuilder() + ",\" available soon on " + self.BookSellers.GetWord() + "!"
          
          return sText
          
#class TweetTxtGen6(TweetTxtGen):
#     # You have to retweet this if it turned you on.
#     def __init__(self):
#          super().__init__(ID = 6)
     
#     def GenerateTweet(self):
#          super().GenerateTweet()
#          sText = ""
          
#          sText = "\U0001F525"
#          sText += "I know " + WordList(["you like reading these", "you're into this", "you freaky", 
#                                                "you're into this bot", "you love these", "these kinda get you off"
#                                               ]).GetWord() + "."
#          sText += "\U0001F525 " 
#          sText += WordList(["Don't worry, I won't tell", "Don't worry, your secret is safe with me", 
#                                 "It's cool, it will be our little secret", "No one has to know", 
#                                 "Don't worry, it can stay between you and me"]).GetWord() + ". " 
#          sText += GetEmoji()
          
#          return sText
          
class TweetTxtGen7(TweetTxtGen):
     # The sexual positions depicted are algorithmically generated and have not been approved by 
     # a licensed medical practicitioner. Do not attempt.
     def __init__(self):
          super().__init__(ID = 7)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["The sex acts", "The sexual positions", "The " + SexyAdjs().GetWord() + " scenarios"]).GetWord() + " " 
          sText += "depicted are " + WordList(["computer-generated", "algorithmically generated", "entirely fictional", 
                                                        "bot-generated", "extremely hot"]).GetWord() + " "
          sText += "and have not been approved by " + WordList(["a doctor","a physician", "a licensed medical practicitioner", 
                                                                             "the AMA", "a licensed physician", "a licensed professional"]).GetWord() + ". "
          sText += "Do not attempt."
          
          return sText
          
class TweetTxtGen8(TweetTxtGen):
     # You have to retweet this if it made you laugh
     def __init__(self):
          super().__init__(ID = 8, Priority = GenPriority.Lowest)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["You have to retweet this", "Please retweet this", "Favorite this", "Fave this", 
                                "You have to favorite this"]).GetWord() + " "
          sText += "if it " + WordList(["made you giggle", "made you laugh", "made you smile", "got you hot", 
                                             "made you blush", "made you grin", "made your privates all tingly", 
                                             "made your naughty bits all tingly", "turned you on", "made you feel hot", 
                                             "got you going", "did it for you", "made your naughty bits feel good"]).GetWord() + ". " 

          return sText
     
# Follow @erotica_ebooks for more #botlaughs 
class TweetTxtGen9(TweetTxtGen):
     # Out soon from Ben Dover
     def __init__(self):
          super().__init__(ID = 9, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "from \"" + BookTitleBuilder() + "\"\n\n" 
          sText += WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + " "
          sText += "@erotica_ebooks for more " + self.SexyAdjs.GetWord() + " "
          sText += WordList(["made-up","bot-generated","machine-generated","algorithmically-generated",
                                 "randomly generated"]).GetWord() + " "
          sText += WordList(["ebook titles", "book titles","#EroticaBookTitles"]).GetWord() + "!"
          
          return sText
          
# The password is 'scrotal'
class TweetTxtGen10(TweetTxtGen):
     # Out soon from Ben Dover
     def __init__(self):
          super().__init__(ID = 10, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          FavWord = WordList()
          FavWord.List += excerpt.bodyparts.AnusFemale().GetNounList()
          FavWord.List += excerpt.bodyparts.Penis().GetNounList()
          FavWord.List += excerpt.bodyparts.Vagina().GetAdjList()
          FavWord.List += excerpt.bodyparts.Testicles().GetNounList ()
          FavWord.List += ['bunghole','crevice','fissure','pendulous','beefy','ravish','ample','nubile', 
                               'panties','lust','throbbing','turgid','tumescent','meat','gooey','juicy', 
                               'moist','taint','labia','pubes','scrotal']

          if CoinFlip():
               sText = "My favorite word is '" + FavWord.GetWord() + "'"
          else:
               sText = "The password is '" + FavWord.GetWord() + "'"
          
          return sText
          
class TweetTxtGen11(TweetTxtGen):
     # If you only read one book this year about clown bukkake, make 
     # sure it is 'Black T-Rex for the Bisexual Princess'!
     def __init__(self):
          super().__init__(ID = 11, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Creatures = WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat man", 
                                     "dwarf", "futanari", "alien", "tentacle monster", "pirate", "lumberjack", "trapeze artist", 
                                     "clown", "sumo wrestler", "were-horse", "gorilla", "dinosaur", "dinosaur", "zombie",
                                     "pro wrestler", "vampire", "velociraptor", "goblin", "elf", "reality TV star",
                                     "shape-shifter"])
          SexActs = WordList(["nipple play", "incest", "threesomes", "fisting", "foursomes", "fivesomes", "bukkake", "bukkake", 
                                   "forced feminization", "spanking", "rope play", "water-sports", "wife swapping", 
                                   "choking play", "orgies", "gangbangs", "reverse gangbangs", "harems", "lactation",
                                   "fem-dom", "race play", "cuckolding", "cuck-queaning", "raw dogging", "sixty-nining",
                                   "erotic asphyxiation", "pee drinking", "cream pies", "anal play", "butt stuff",
                                   "voyeurism", "wife swapping", "domination", "double penetration", "triple penetration",
                                   "handjobs", "nipple play"])
          
          sText = "If you only read one book this " + WordList(["year", "year", "year", "month", "month", "decade", "week", "week", "century"]).GetWord() + " about "
          sText += Creatures.GetWord() + " "
          sText += SexActs.GetWord() + ", " 
          sText += WordList(["it should be", "make sure it is", "I heartily recommend"]).GetWord() + " "
          sText += "'" + BookTitleBuilder() + "'!" 
          
          return sText
          
class TweetTxtGen12(TweetTxtGen):
     # Write one little sumo wrestler fisting scene and they ban you 
     # from Amazon for life!
     def __init__(self):
          super().__init__(ID = 12)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Write one little " + WordList(['non-consensual','interracial','pseudo-incest']).GetWord() + " "
          sText += WordList(["unicorn", "centaur", "werewolf", "mermaid", "merman", "mer-MILF", "dragon", "orc", "goat-man", 
                                 "dwarf", "futanari", "space alien", "tentacle monster", "clown", "sumo wrestler", "were-horse", 
                                 "gorilla", "dinosaur", "dinosaur", "velociraptor", "zombie", "bodybuilder",
                                 "pro-wrestler"]).GetWord() + " "
          sText += WordList(["anal", "double anal", "nipple play", "fisting", "incest", "twincest", "threesome", 
                                   "foursome", "fivesome", "bukkake", "feminization", "paddling", "rope play", 
                                   "water-sports", "wife swapping", "69", "erotic asphyxiation", "orgy", "gangbang", 
                                   "reverse gangbang", "milking", "double penetration", "triple penetration", 
                                   "pee-drinking", "Dirty Sanchez", "sodomy", "age play", "BDSM", "fisting",
                                   "anal fisting", "fem-dom"]).GetWord() + " scene, " 
          sText += "and they ban you from Amazon" 
          if CoinFlip():
               sText += " for life"
          sText += "!"
          
          return sText
          
class TweetTxtGen13(TweetTxtGen):
     # Author Ben Dover is truly the Hemmingway of triple penetration!
     def __init__(self):
          super().__init__(ID = 13)

     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText += WordList(["Author","Writer"]).GetWord() + " "
          sText += AuthorBuilder() + " is truly the " + WordList(["Stephen King", "J.K. Rowling", "Jane Austen", 
                                                                                "William Shakespeare", "Shia Lebouf", "Charles Dickens", 
                                                                                "Hemmingway", "Agatha Christie", "Maya Angelou", 
                                                                                "Tolstoy", "Melville", "Harper Lee", "Proust", 
                                                                                "Emily Dickinson", "Truman Capote"]).GetWord() + " of "
          sText += WordList(["gay", "lesbian", "MILF", "unicorn", "centaur", "werewolf", "mermaid", "merman", 
                                 "mer-MILF", "dwarf", "dragon", "orc", "goat man", "futanari", "alien", "tentacle monster", 
                                 "pirate", "lumberjack", "trapeze artist", "clown", "sumo wrestler", "were-horse", 
                                 "gorilla", "dinosaur", "dinosaur"]).GetWord() + " "
          sText += WordList(["anal", "nipple play", "incest", "fisting", "twincest", "threesomes", "foursomes", 
                                 "fivesomes", "bukkake", "bukkake", "forced feminization", "spanking", "rope play", 
                                 "water-sports", "wife swapping", "69", "erotic asphyxiation", "orgy", "gangbang", 
                                 "reverse gangbangs", "lactation", "double penetration", "triple penetration", "porn", 
                                 "erotica", "edging", "BDSM", "bondage", "cuckolding"]).GetWord() + "!" 

          
          return sText
          
class TweetTxtGen14(TweetTxtGen):
     # "Double-Penetrated by the Filthy Centaur Bikers," page 312
     def __init__(self):
          super().__init__(ID = 14)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          sText = "\"" + BookTitleBuilder() + "\" by " + AuthorBuilder() + ", "
          
          if CoinFlip():
               sText += "page " + str(randint(6,349))
          else:
               sText += "chapter " + str(randint(2,46))
          return sText

class TweetTxtGen15(TweetTxtGen):
     # "Teen mom for the Well-Hung Viking" is 'Delightful & provactive!' 
     # raves Dwarf Fisting Magazine 
     def __init__(self):
          super().__init__(ID = 15, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Praises = WordList(["delightful & provactive", "thoughtful & heart-warming", "heart-warming & transcendant", 
                                   "complex yet satisfying", "a real rollercoaster ride", "an emotional rollercoaster", 
                                   "an edge-of-your-seat, stand-up-and-cheer page-turner", 
                                   "un-put-downable", "a grand slam", "a home-run", "a modern classic"])
          PraiseVerbs = WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", 
                                        "salutes", "extols"])
          Creatures = WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", 
                                     "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", 
                                     "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur","MILF"])
          Fetishes = WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", 
                                    "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", 
                                    "Erotic Asphyxiation", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", 
                                    "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"])
          
          sText = "\"*" + BookTitleBuilder() + "* is " + Praises.GetWord() + "!\" "
          sText += PraiseVerbs.GetWord() + " " + Creatures.GetWord() + " "+ Fetishes.GetWord() + " Magazine" 
          
          return sText
          
class TweetTxtGen16(TweetTxtGen):
     # 'Ben Dover's latest is a triumph!' applauds Goat-man Foursome Magazine 
     def __init__(self):
          super().__init__(ID = 16, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sAuthor = AuthorBuilder() 
          if sAuthor[len(sAuthor) - 1] == "s":
               sAuthor += "'"
          else:
               sAuthor += "'s"
          sText = "'" + sAuthor + " latest is " 
          sText += WordList(['a triumph', 'a triumph', 'a massive success', 'a masterpiece', 'an erotic masterpiece', 
                                 'a modern classic', 'a sexual classic', 'brilliant', 'a work of genius', 
                                 'an unmatched success', 'the next Harry Potter', 'the next 50 Shades of Gray', 
                                 'the next Hunger Games', 'un-put-downable', 'heart-warming and satisfying', 
                                 'very readable']).GetWord() + "!' "
          sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", 
                                 "extols"]).GetWord() + " " 
          sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", 
                                 "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", 
                                 "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
          sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", 
                                 "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", 
                                 "Erotic Asphyxiation", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", 
                                 "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", 
                                 "Water-sports"]).GetWord() + " Magazine" 
          
          return sText
          
class TweetTxtGen17(TweetTxtGen):
     # Why don't I ever meet any horny, well-hung lumberjacks in real life?
     def __init__(self):
          super().__init__(ID = 17, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adj1 = WordList(["horny", "desperate", "lonely", "steamy", "single", "sensual", "bereft", 
                               "tragically widowed", "lustful", "sexually repressed", "loner", "bachelor", 
                               "naked"])
          Adj2 = WordList(["sexy", "hot", "hunky", "handsome", "shirtless", "brawny", "virile", "clean-cut", 
                                 "stylish", "suave", "alluring", "gruff", "chiseled", "strapping", "attractive", 
                                 "erotic", "stunning", "well-hung", "well-endowed", "girthy", "hugely erect"])
          Professions = WordList(["lumberjacks", "firemen", "cops", "lifeguards", "stunt men", "bull riders", 
                                 "park rangers", "pilots", "Chippendales dancers", "astronauts", "attorneys", 
                                 "Navy SEALs", "Green Berets", "heart surgeons", "cowboys", "guitar players", 
                                 "olympic gold medalists", "private eyes", "professional surfers"])
                                 
          sText = "Why don't I ever meet any " + Adj1.GetWord() + ", "+ Adj2.GetWord() + " "
          sText += Professions.GetWord() + " in real life?"
          
          return sText
          
class TweetTxtGen18(TweetTxtGen):
     # Of course in real life you should never attempt centaur bukkake 
     # without strict medical supervision.
     def __init__(self):
          super().__init__(ID = 18, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Of course in real life you should never attempt " 
          sText += WordList(["tentacle", "unicorn", "centaur", "man-o-taur", "gargoyle", "werewolf", "merman", "dwarf", 
                                 "dragon", "orc", "troll", "goat-man", "futanari", "alien", "tentacle monster", "clown", 
                                 "sumo wrestler", "were-horse", "t-rex", "velociraptor", "dinosaur", "reverse merman", 
                                 "cyborg", "were-shark"]).GetWord() + " "
          sText += WordList(["anal", "double anal", "fisting", "nipple play", "incest", "twincest", "cum-swapping", 
                                   "bukkake", "rope play", "pee-drinking", "cuckolding", "69", "erotic asphyxiation", 
                                   "double gangbang", "double penetration", "triple penetration", "BDSM", "bondage", 
                                   "water-sports", "public humiliation", "lactation", "age play", "edging", 
                                   "forced orgasm", "domination", "submission"]).GetWord() + " "
          sText += "without " + WordList(["strict medical supervision", "a note from your doctor", 
                                                  "waiting at least two hours after eating", 
                                                  "guidance from a trained professional", "protection",
                                                  "help from a licensed dominatrix", "using the buddy system", 
                                                  "regular checkups", "notifying the police", 
                                                  "a medical team on hand", "a licensed professional",
                                                  "an ambulance standing by", "a certified SCUBA instructor", 
                                                  "a friend that you can trust", "telling someone where you are", 
                                                  "paramedics on hand", "medical training", "power of attorney"]).GetWord() + "."
          
          
          return sText
          
class TweetTxtGen19(TweetTxtGen):
     # Ben Dover is definitely the best erotica author working in Tuscaloosa!
     def __init__(self):
          super().__init__(ID = 19,Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sAuthor = AuthorBuilder()
          sSuper = WordList(["best", "premier", "finest", "top ten"]).GetWord()
          EroticaNiches = WordList(["anal fisting","dwarf lactation","wife-swapping","lesbian fisting",
                                          "lesbian lactation","lesbian anal","trans age-play","cuckquean lactation",
                                          "werewolf fisting","vampire age-play","vampire lactation",
                                          "anal exhibitionism","vampire knotting","BDSM lactation","vampire menage",
                                          "anal menage","lactation menage","cuckquean psuedo-incest",
                                          "pseudo-incest lactation","pseudo-incest fisting","vampire fisting",
                                          "pseudo-incest age-play","BDSM cuckolding","interracial fisting",
                                          "interracial vampire menage","vampire exhibitionism",
                                          "interracial pseudo-incest","trans pseudo-incest","interracial cuckqueaning",
                                          "interracial age-play","pseudo-incest anal fisting","interracial anal fisting",
                                          "interracial gangbang","interracial anal gangbang",
                                          "interracial pseudo-incest anal gangbang","interracial lesbian voyeurism",
                                          "interracial pseudo-incest BDSM","non-consensual vampire fisting",
                                          "interracial lesbian anal menage","trans mer-man age-play",
                                          "trans mer-man BDSM","pseudo-incest gangbang voyeurism",
                                          "trans cuckquean BDSM", "interracial trans lactation",
                                          "interracial anal cuckolding","non-consensual nipple play",
                                          "pseudo-incest lesbian nipple play","interracial anal fem-dom",
                                          "interracial vampire fem-dom","trans pseudo-incest fem-dom",
                                          "non-consensual fem-dom lactation", "male lactation",
                                          "interracial futanari pseudo-incest","interracial futanari gangbang",
                                          "interracial futanari anal","interracial futanari lactation",
                                          "interracial futa wife-swapping", "interracial lesbian wife-swapping",
                                          "anal mer-man exhibitionism", "interracial MILF nipple-play",
                                          "psuedo-incest anal cuck-quean", "non-consensual foot fetish",
                                          "pseudo-incest vampire menage", "lesbian vampire fisting",
                                          "werewolf foot-fetish fem-dom", "reverse gangbang anal fisting",
                                          "anal vampire reverse gangbang", "trans anal foot-fetish",
                                          "pseudo-incest werewolf foot-fetish", "trans vampire anal wife-swapping"])
          sType = EroticaNiches.GetWord()
          
          Places = DullPlaces()
          sPlace = ""
          if CoinFlip():
               sPlace += "in " 
               if CoinFlip():
                    sPlace += WordList(["North", "South", "East", "West"]).GetWord() + " "
               sPlace += Places.GetWord()
          else:
               sPlace += "from " 
               if CoinFlip():
                    sPlace += WordList(["North", "South", "East", "West"]).GetWord() + " "
               sPlace += Places.GetWord()
               
          sText = WordList(["There's no question that " + sAuthor + " is one of the ",
                                sAuthor + " is absolutely one of the ",
                                "There's no doubt in my mind that " + sAuthor + " is one of the ",
                                "There can be no debate that " + sAuthor + " is one of the ",
                                "No one can deny that " + sAuthor + " is one of the "]).GetWord()
          sText += sSuper + " " + sType + " writers " + sPlace
          
          return sText
          
class TweetTxtGen20(TweetTxtGen):
     # "*Spit-Roasting My Busty Centaur MILF* is a wild fuck-fest!" 
     # -Abraham Lincoln
     def __init__(self):
          super().__init__(ID = 20, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adjs = WordList(["thrilling", "wild", "sensual", "perverted", "raunchy", "tasteless", "lascivious", "erotic", "horny", 
                                   "delightful", "sinful", "arousing", "naughty", "depraved", "lustful", "wicked", "outrageous", "delicious", 
                                   "stimulating", "sexy", "provocative", "lewd", "wicked", "shameless", "stimulating", "kinky", "juicy",
                                   "wanton"])
          Celebs = WordList(["Abraham Lincoln", "Winston Churchill", "Barak Obama", "Michelle Obama", 
                             "Mother Theresa", "Salman Rushdie", "Albert Einstein", "Hillary Clinton", 
                             "Isaac Asimov", "Jonathan Franzen", "Cormac McCarthy", "Ghandi", 
                             "Boutros Boutros-Ghali", "Bob Dylan", "The Dalai Lama", "Elon Musk", 
                             "Warren Buffett", "Stephen King", "Bill Gates", "Billy Graham", 
                             "Jimmy Carter", "Oprah Winfrey","Neil Armstrong", "Stephen Hawking", 
                             "Al Gore"])
          sAdj1 = Adjs.GetWord()
          sAdj2 = Adjs.GetWord(NotList = [sAdj1])
          
          iRand = randint(1,6)
          if iRand == 1:
               sAdj1 = Adjs.GetWord()
               sAdj2 = Adjs.GetWord(NotList = [sAdj1])
               sText += "\"*" + BookTitleBuilder() + "* is " + sAdj1 + " and " + sAdj2 + "!\"\n"
          elif iRand == 2:
               sAdj = Adjs.GetWord()
               sText = "\"*" + BookTitleBuilder() + "* is "
               sText += AddArticles(sAdj1 + " fuckfest!") + "\"\n"
          elif iRand == 3:
               sAdj = Adjs.GetWord()
               sText += "\"*" + BookTitleBuilder() + "* is " + sAdj1 + " AF!\"\n"
          elif iRand == 4:
               sText += "\"I'm so horny for this!\"\n" 
          elif iRand == 5:
               sText += "\"I got off on this!\"\n" 
          else:
               sText = "\"What the fuck did I just read??\"\n" 
               
          sText += " ~" + Celebs.GetWord()
          
          return sText
          
class TweetTxtGen21(TweetTxtGen):
     # "Fisted by the Alpha Male Goat-Men on Uranus" is widely considered to 
     # be the 'Lord of the Rings' of anal fisting books.
     def __init__(self):
          super().__init__(ID = 21, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Books = WordList(["Lord of the Rings","War and Peace","Finnegan's Wake","Harry Potter","1984",
                                "Jane Eyre","Moby Dick","Romeo & Juliet","Hamlet","Lord of the Flies",
                                "To Kill a Mockingbird","Don Quixote","Brave New World","Catch-22","Bell Jar",
                                "One Hundred Years of Solitude","Grapes of Wrath","Ulysses","Brothers Karamazov",
                                "Atlas Shrugged","Heart of Darkness","Handmaid's Tale","Madame Bovary",
                                "Great Expectations","Paradise Lost","Old Man and the Sea","Scarlet Letter",
                                "Gone With the Wind","Waiting for Godot","Fahrenheit 451"])
          EroticaNiches = WordList(["anal fisting","dwarf lactation","wife-swapping","lesbian fisting",
                                          "lesbian lactation","lesbian anal","trans age-play","cuckquean lactation",
                                          "werewolf fisting","vampire age-play","vampire lactation",
                                          "anal exhibitionism","vampire Knotting","BDSM lactation","vampire menage",
                                          "anal menage","lactation menage","cuckquean Psuedo-incest",
                                          "pseudo-incest lactation","pseudo-incest fisting","vampire fisting",
                                          "pseudo-incest age-play","BDSM cuckolding","interracial fisting",
                                          "interracial vampire menage","vampire exhibitionism",
                                          "interracial pseudo-incest","trans pseudo-incest","interracial cuckqueaning",
                                          "interracial age-play","pseudo-incest anal fisting","interracial anal fisting",
                                          "interracial gangbang","interracial anal gangbang",
                                          "interracial pseudo-incest anal gangbang","interracial lesbian voyeurism",
                                          "interracial pseudo-incest BDSM","non-consensual vampire fisting",
                                          "interracial lesbian anal menage","trans Merman age-play",
                                          "trans Merman BDSM","pseudo-incest Gangbang Voyeurism",
                                          "trans cuckquean BDSM", "interracial trans lactation",
                                          "interracial anal cuckolding","Non-consensual nipple play",
                                          "pseudo-incest lesbian nipple play","interracial anal fem-dom",
                                          "interracial vampire fem-dom","trans pseudo-incest fem-dom",
                                          "non-consensual fem-dom lactation", "male lactation",
                                          "interracial futanari pseudo-incest","interracial futanari gangbang",
                                          "interracial futanari anal","interracial futanari lactation"])
                                          
          sText = "\"" + BookTitleBuilder() + "\" "
          sText += "is " + WordList(["widely regarded","widely considered","broadly regarded","broadly considered"]).GetWord() + " "
          sText += "to be the '" + Books.GetWord() + "' of " + EroticaNiches.GetWord() + " books."
          
          
          return sText
          
class TweetTxtGen22(TweetTxtGen):
     # This was Ben Dover's last book before he was banned from Amazon 
     # for writing a scene involving a goat man and bukkake.
     def __init__(self):
          super().__init__(ID = 22)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adjs = WordList(['a filthy','a shocking','a provactive','an outrageous','a disgusting','a taboo',
                               'a naughty','a tasteless','an extremely gratuitous','a highly unnecessary'])
          Species = WordList(["unicorn","centaur","werewolf","merman","goat man","dwarf","demon","clown",
                                   "space alien","tentacle monster","were-horse","manticore","sea monster",
                                   "werewolf","dinosaur", "dinosaur","vampire","martian","lizard man","mime",
                                   "minotaur","reverse centaur","giant","unicorn","pegasus","ghost",
                                   "zombie"])
          SexToys = WordList(["clit clamps","Ben Wa balls","nipple clamps","cock rings","anal hooks","spreader bars",
                                   "ball gags","butt plugs","dental dams","clothes pins","sex swings","riding crops",
                                   "nose hooks","chastity belts","erotic furniture","clit pumps","sybians","nylons",
                                   "anal beads","fur suits","steel dildos","wooden dildos","anal vibrators",
                                   "strap-ons","assless chaps","glory holes"])
          SexActs = WordList(["anal", "double anal", "fisting","anal fisting","nipple play", "incest", "twincest",
                                   "cum-swapping","bukkake","rope play","pee-drinking","cuckolding","sixty-nine",
                                   "erotic asphyxiation","double penetration","triple penetration",
                                   "BDSM","water-sports","lactation","age play","edging","forced orgasm", 
                                   "forced feminization","deep-throating","swinging","leather bondage","tea-bagging",
                                   "full-frontal massage","cuck-queaning","enemas","pegging","butt stuff","sodomy",
                                   "premarital sex","spanking","paddling"])
          
          if CoinFlip():
               # male
               sText = "This was " + AuthorBuilder(Gender.Male) + "'s last book before "
               sText += "he was banned from Amazon for " + Adjs.GetWord() + " scene involving "
               
          else:
               # female
               sText = "This was " + AuthorBuilder(Gender.Female) + "'s final book before "
               sText += "she was banned from Amazon for " + Adjs.GetWord() + " scene involving "
               
          iRand = randint(1,5)
          if iRand == 1:
               sText += SexToys.GetWord() + " and "
               if CoinFlip():
                    sText += AddArticles("underage " + Species.GetWord()).lower()
               else:
                    sText += AddArticles(Species.GetWord()).lower()
          elif iRand == 2:
               sText += SexToys.GetWord() + " and "
               if CoinFlip():
                    sText += "underage "
               sText += SexActs.GetWord() 
          elif iRand == 3:
               if CoinFlip():
                    sText += AddArticles("underage " + Species.GetWord()).lower()
               else:
                    sText += AddArticles(Species.GetWord()).lower()
               sText += " and " 
               if CoinFlip():
                    sText += WordList(['underage','non-consensual','extreme']).GetWord() + " "
               sText += SexActs.GetWord()
          elif iRand == 4:
               sText += SexToys.GetWord() + " and "
               if CoinFlip():
                    sText += WordList(['underage','non-consensual','extreme']).GetWord() + " "
               sText += Species.GetWord() + " sex"
          else:
               sText += Species.GetWord() + " " + SexActs.GetWord() + " and "
               if CoinFlip():
                    sText +=  WordList(['underage','non-consensual','extreme']).GetWord() + " "
               sText += SexToys.GetWord() 

          sText += "!"
          
          return sText
          
class TweetTxtGen23(TweetTxtGen):
     # By day, erotica author Ben Dover is a Wedding Photographer from Scranton.
     def __init__(self):
          super().__init__(ID = 23, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sMaleJob = DullJobsMale().GetWord()
          sFemaleJob = DullJobsFemale().GetWord()
          sPlace = DullPlaces().GetWord()
          
          if CoinFlip():
               # male
               sText = "By day, erotica author " + AuthorBuilder(Gender.Male) + " is " + AddArticles(sMaleJob).lower() + " from " + sPlace + "."     
          else:
               # female
               sText = "By day, erotica author " + AuthorBuilder(Gender.Female) + " is " + AddArticles(sFemaleJob).lower() + " from " + sPlace + "."
          
          return sText     
          
class TweetTxtGen24(TweetTxtGen):
     # LEGAL DISCLAIMER: Wal-Mart does not condone cum-swapping or genital 
     # piercings.
     def __init__(self):
          super().__init__(ID = 24, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          SexActs = WordList(["unprotected anal sex","double anal penetration","fisting",
                                   "anal fisting","twincest","tribbing","pee drinking",
                                   "cum-swapping","bukkake","public gang bangs",
                                   "anal gangbangs","urinating in the mouth of another person",
                                   "pee-drinking","erotic asphyxiation","double penetration",
                                   "triple penetration","forced orgasm","public nudity",
                                   "ball torture","forced feminization","wife-swapping",
                                   "leather bondage","tea-bagging","full-frontal massage",
                                   "enemas","pegging","butt stuff","sodomy","premarital sex",
                                   "spanking","paddling","adult diapers","choke play",
                                   "genital piercings","extreme vaginal insertion",
                                   "cum drinking","extreme anal insertion",
                                   "interracial gang-bangs"])
          sAct1 = SexActs.GetWord()
          sAct2 = SexActs.GetWord(NotList = [sAct1])
          
          sText = "LEGAL DISCLAIMER: " 
          sText += WordList(["Wal-Mart","Outback Steakhouse","Bank of America",
                                   "Whole Foods","CVS Pharmacy","Applebee's",
                                   "Pizza Hut","Starbucks","Chipotle","Barnes & Noble",
                                   "The International House of Pancakes",
                                   "The Walt Disney Corporation","The Apple Store",
                                   "Famous Footwear","Men's Wearhouse",
                                   "The Cheesecake Factory","Subway Sandwiches",
                                   "Olive Garden","Cracker Barrel","Red Lobster",
                                   "Tesco","Best Buy","Costco"
                                ]).GetWord() + " "
          sText += "does not condone " + sAct1 + " or " + sAct2 + "."
          
          return sText               
          
class TweetTxtGen25(TweetTxtGen):
     # from Part 3 of Ben Dover's 12-book "Baby For the Ugly Werewolf" series
     def __init__(self):
          super().__init__(ID = 25)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Series = WordList([[3,"three"],
                                 [4,"four"],
                                 [5,"five"],
                                 [6,"six"],
                                 [7,"seven"],
                                 [8,"eight"],
                                 [10,"ten"],
                                 [12,"twelve"],
                                 [13,"thirteen"],
                                 [16,"sixteen"],
                                 [20,"twenty"],
                                 [69,"sixty-nine"]]).GetWord()
          
          sText = "from Part " + str(randint(2,Series[0] - 1)) + " "
          sText += "of " + AuthorBuilder(Gender.Neuter) + "'s "
          sText += WordList(["epic","epic","ambitious","momentous","seminal","classic","critically-acclaimed"]).GetWord() + " "
          sText += Series[1] + "-book "
          sText += "\"" + BookTitleBuilder(maxlen = 60) + "\" "
          sText += WordList(['series','saga','cycle','trilogy']).GetWord()
          
          return sText     

class TweetTxtGen26(TweetTxtGen):
     # From page 307 of One Hundred Years of Solitude by Gabriel Garcia Marquez
     def __init__(self):
          super().__init__(ID = 26)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Literature = WordList([["Lord of the Rings","J.R.R. Tolkien"],
                                        ["Pride and Predjuice","Jane Austin"],
                                        ["Wuthering Heights","Emily Brontë"],
                                        ["Sense and Sensibility","Jane Austin"],
                                        ["One Hundred Years of Solitude","Gabriel García Márquez"],
                                        ["The Bell Jar","Sylvia Plath"],
                                        ["The Great Gatsby","F. Scott Fitzgerald"],
                                        ["The Grapes of Wrath","John Steinbeck"],
                                        ["War and Peace", "Leo Tolstoy"],
                                        ["Anna Karenina","Leo Tolstoy"],
                                        ["The Sun Also Rises","Earnest Hemmingway"],
                                        ["Jane Eyre","Charlotte Brontë"],
                                        ["Heart of Darkness","Joseph Conrad"],
                                        ["Finnegan's Wake","James Joyce"],
                                        ["Ulysses","James Joyce"],
                                        ["Moby Dick","Herman Melville"],
                                        ["To Kill A Mockingbird","Harper Lee"],
                                        ["1984","George Orwell"],
                                        ["The Catcher in the Rye", "J.D. Salinger"],
                                        ["The Brothers Karamazov","Fyodor Dostoyevsky"],
                                        ["The Scarlet Letter","Nathaniel Hawthorne"],
                                        ["Don Quixote","Miguel de Cervantes"],
                                        ["Les Misérables","Victor Hugo"],
                                        ["Of Mice and Men","John Steinbeck"],
                                        ["A Tale of Two Cities","Charles Dickens"],
                                        ["Charlotte's Web","E.B. White"],
                                        ["The Wind in the Willows","Kenneth Grahame"],
                                        ["All Quiet on the Western Front","Erich Maria Remarque"],
                                        ["Rememberance of Things Past","Marcel Proust"],
                                        ["The Call of the Wild","Jack London"],
                                        ["Portnoy's Complaint","Philip Roth"],
                                        ["The Sound & The Fury","William Faulkner"],
                                        ["Madame Bovary","Gustave Flaubert"],
                                        ["Harry Potter and the Deathly Hallows","J.K. Rowling"],
                                        ["Are You There God? It's Me, Margaret","Judy Bloom"],
                                        ["The Unbearable Lightness of Being","Milan Kundera"],]).GetWord()
                                        
          sText = "From \"" + Literature[0] + ",\" by " + Literature[1] + ". "
          if CoinFlip():
               sText += "Chapter " + str(randint(4,69)) 
          else:
               sText += "Page " + str(randint(101,950))
          sText += "."
          
          return sText     

class TweetTxtGen27(TweetTxtGen):
     # From the demented imagination of author Ben Dover
     def __init__(self):
          super().__init__(ID = 27, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText += "From the " + WordList(["fertile","kinky","deranged","horny","unique","dirty","filthy",
                                                   "demented","creative","extraordinary"]).GetWord() + " "
          sText += WordList(["mind","mind","brain","imagination","imaginings"]).GetWord() + " "
          sText += "of " + WordList(["writer","author"]).GetWord() + " " +  AuthorBuilder(Gender.Neuter) + ":"
          
          return sText     

class TweetTxtGen29(TweetTxtGen):
    # The part where he gives her a "Mexican Donkey" is the filthiest thing I've ever read in my life
    def __init__(self):
        super().__init__(ID = 29, Priority = GenPriority.High)
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sText = ""

        sSexTechnique = WordList(["the trantric sex technique","the sex technique",
                                   "the sexual position","the sex position",
                                   "the tantric sex position","the sex move"]).GetWord()
        sDirtyPhrase = TantricTechniques().GetWord()

        iRand = randint(1,5)
        if iRand == 1:
             sText = "Before I read this book I had never even heard of " + sSexTechnique + " called \"The " + sDirtyPhrase + ".\""
        elif iRand == 2:
             sText = "Before I read this I didn't even know what " + AddArticles(sDirtyPhrase, cBracket = "\"") + " was."
        elif iRand == 3:
             sText = "I had never even heard of " + AddArticles(sDirtyPhrase, cBracket = "\"") + " before I read this book!"
        elif iRand == 4:
             sText = "The part where he gives her " + AddArticles(sDirtyPhrase, cBracket = "\"") + " is the filthiest thing I've ever read in my life."
        else:
             sText = "If you haven't heard of " + AddArticles(sDirtyPhrase, cBracket = "\"") + " before, do NOT google it."

        return sText     

# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     


# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     


# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     


# class TweetTxtGen24(TweetTxtGen):
     # # Out soon from Ben Dover
     # def __init__(self):
          # super().__init__()
          # self.ID = 24
          # self.Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText               
          
def GetImgTweetText(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetTxtHistoryQ = None):
     #the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
     sText = ""
     
     Generator = None
     GenType = None 
     HistoryQ = None 
     
     if not Type is None:
          GenType = Type 
     else:
          GenType = None 
     
     if not TweetTxtHistoryQ is None:
          HistoryQ = TweetTxtHistoryQ
     
     GenSel = GeneratorContainer(TweetTxtGen, HistoryQ = TweetTxtHistoryQ)
     if bTest:
          gen = GenSel.GetGenerator(iGeneratorNo)
     else:
          gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
          while not HistoryQ.PushToHistoryQ(gen.ID):
               gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
     
     if not gen is None:
          sText = gen.GenerateTweet()
     else:
          sText = ""

     # bots using hashtags can lead to shadowbans. so we have to use sparingly.
     if randint(1,5) == 5:
          sText += " #" + Hashtags().GetWord()
     
     return sText 