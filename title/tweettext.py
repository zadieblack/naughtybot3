#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from util import *
from misc import *
from names import *
from gen import *
from title.people import *
from title.texttoimg import *

def AddHashtag(Tweets):
     # if the last tweet has left over space, append a random hashtag to it: eartg, lprtg, wprtg, ssrtg, imabot, smut, erotica, etc
     if not Tweets is None and type(Tweets) in [list,tuple] and len(Tweets) > 0:
          sHashtag = "\n#" + misc.Hashtags().GetWord()
          if len(Tweets[len(Tweets) - 1]) + len(sHashtag) < MAX_TWITTER_CHARS:
               Tweets[len(Tweets) - 1] += sHashtag

     return Tweets
     
class TweetTxtGen(Generator):
    def __init__(self, ID = -1, 
                 Priority = GenPriority.Normal,
                 Type = GeneratorType.Normal, 
                 Disabled = False,
                 sTxt = False,
                 sAuthorName = "", 
                 AuthorGender = None):
        super().__init__(ID = ID, Priority = Priority, Type = Type, Disabled = Disabled, sTxt = sTxt)

        if AuthorGender is None:
            self._AuthorGender = Gender.Neuter 
        else:
            self._AuthorGender = AuthorGender 

        if sAuthorName != "":
            self._AuthorName = sAuthorName 
        else:
            self._AuthorName = AuthorBuilder(self._AuthorGender)

        self._TweetTxt = ""

    def AuthorName(self):
        return self._AuthorName 

    def AuthorGender(self):
        return self._AuthorGender
     
    def GenerateTweet(self):
        #super().GenerateTweet()

        self.BookSeller = BookSellers()
        self.Hashtag = Hashtags()
        self.SexyAdj = SexyAdjs()
          
        return ""
          
class TweetTxtGen1(TweetTxtGen):
    # The sexy read that was BANNED on Amazon! Now available on Smashwords

    def __init__(self): 
        super().__init__(ID = 1, Priority = GenPriority.Normal)
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sText = ""
          
        sText = "The " + self.SexyAdj.GetWord() + " " 
        sText += WordList(["read", "book", "ebook"]).GetWord() + " "
        sText += "that was " + WordList(["BANNED on", "TOO HOT for", 
                                        "TOO FILTHY for", "too much for"]).GetWord() + " Amazon! "
        sText += "Now available on " + self.BookSeller.GetWord(NotList = ["Amazon", "Kindle Unlimited"]) 
        sText += " (from " + self.AuthorName() + ")"
        #=============================
          
        return sText

class TweetTxtGen2(TweetTxtGen):
     # Available soon on Amazon and Smashwords. By Ben Dover
     def __init__(self): 
         super().__init__(ID = 2, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sBookSeller = self.BookSeller.GetWord()
          
          sText = WordList(["Coming soon on", "Available soon on", "Look for this soon on", "Get it now on", "Download it today on"]).GetWord() + " " + sBookSeller 
          if CoinFlip():
               sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
          if CoinFlip():
               sText += ". By " + self.AuthorName()
          
          return sText
          
class TweetTxtGen3(TweetTxtGen):
     # Watch for this naughty ebook on Wattpad and Kobo. By Ben Dover 
     def __init__(self): 
         super().__init__(ID = 3, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sBookSeller = self.BookSeller.GetWord()
          
          sText = WordList(["Watch for this", "Look for this", "Keep an eye out for this"]).GetWord() + " " + self.SexyAdj.GetWord() + " ebook on " + sBookSeller
          if CoinFlip():
               sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
          if CoinFlip():
               sText += ". By " + self.AuthorName()
          #=============================
          
          return sText
          
class TweetTxtGen4(TweetTxtGen):
     # Coming soon to discerning readers on Amazon and Smashwords. By Ben Dover 
     def __init__(self): 
         super().__init__(ID = 4, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sBookSeller = self.BookSeller.GetWord()
          
          sText = WordList(["Available soon", "Coming soon", "On its way soon"]).GetWord() + " to " + WordList(["discerning", "discrete", "discriminating"]).GetWord() + " readers on " + sBookSeller 
          if CoinFlip():
               sText += " and " + self.BookSeller.GetWord(NotList = [sBookSeller])
          if CoinFlip():
               sText += ". By " + self.AuthorName()
          
          return sText
          
class TweetTxtGen5(TweetTxtGen):
     # Ben Dover's Patreon supporters get instant access to all his filthy reads!
     def __init__(self): 
         super().__init__(ID = 5, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Supporters = WordList(["Patreon supporters", "supporters on Patreon"])
          Access = WordList(["instant access", "free access", "access"])
          Reads = WordList(["reads", "books", "stories"])
          
          if self.AuthorGender() is Gender.Male:
               # male
               sText = self.AuthorName() + "'s "
               sText += Supporters.GetWord() + " get " 
               sText += Access.GetWord() + " to all his " 
               sText += self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"
          else:
               # female
               sText =self.AuthorName() + "'s "
               sText += Supporters.GetWord() + " get " 
               sText += Access.GetWord() + " to all her " 
               sText += self.SexyAdj.GetWord() + " " + Reads.GetWord() + "!"

          
          return sText
          
class TweetTxtGen6(TweetTxtGen):
     # Get excited! The wait is over for Ben Dover's latest sexy release!
     def __init__(self): 
         super().__init__(ID = 6, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText += WordList(["At last!","At last!","At last!", "Finally!",
                            "Finally!", "Get excited!", "It's here!"]).GetWord() + " "
          sText += "The wait is over for " + self.AuthorName() + "'s " 
          sText += WordList(["newest", "latest"]).GetWord() + " " 
          sText += self.SexyAdj.GetWord() + " " 
          sText += WordList(["book","book","book","release","novel","ebook", 
                             "release"]).GetWord() + "!"
          
          return sText
          
class TweetTxtGen7(TweetTxtGen):
     # Out soon from Ben Dover
     def __init__(self): 
         super().__init__(ID = 7, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["Available soon", "Coming soon", "On its way soon", 
                            "Out soon", "Arriving soon"]).GetWord() + " "
          sText += "from " + self.AuthorName()
          
          return sText
          
class TweetTxtGen8(TweetTxtGen):
     # The fisting scene is really surprisingly tasteful!
     def __init__(self): 
         super().__init__(ID = 8, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          SexActs = WordList(["anal", "orgy", "gangbang", "fisting", "reverse gangbang", "double gangbang", 
                                   "triple penetration", "deep throat", "incest", "foursome", "fivesome", 
                                   "MILF orgy", "lesbian orgy", "bukkake", "forced feminization", "choking", 
                                   "twincest", "Dirty Sanchez", "pee drinking", "wife swapping",
                                   "erotic asphyxiation", "cum swapping", "forced feminization",
                                   "anal hook", "leather bondage", "steel dildo", "ball punishment"])
          
          sText = "The " + SexActs.GetWord() + " scene is " 
          sText += WordList(["surprisingly", "actually surprisingly", "really surprisingly", "actually very", "really quite", "actually unexpectedly", "unexpectedly"]).GetWord() + " " 
          sText += WordList(["tasteful", "tasteful", "loving", "affectionate", "sweet", "heartfelt", "classy", "subdued", "discrete", "charming", "endearing", "thoughtful", "tactful", "wistful"]).GetWord() 
          
          return sText
          
class TweetTxtGen9(TweetTxtGen):
     # If you only read one book this year about clown bukkake, make sure it is this one!
     def __init__(self): 
         super().__init__(ID = 9, Priority = GenPriority.AboveAverage)
     
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
          sText += WordList(["it should be", "make sure it is", "I heartily recommend"]).GetWord() + " this one!" 

          
          return sText
          
class TweetTxtGen10(TweetTxtGen):
     # Who will Emily choose, the rodeo clown or her step-dad? I was on 
     # the edge of my seat! #teamstepdad
     def __init__(self): 
         super().__init__(ID = 10, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sSuitor1 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True, bAllowGang = False).Desc
          sSuitor2 = Master = MaleChar(iNumMaxCBits = 1, bAddArticle = True, bAllowGang = False).Desc
          sText = "Who will " + NamesFemale().FirstName() + " choose, " + NamesMale().FirstName() + " " + SmartLower(sSuitor1) + " or " + NamesMale().FirstName() + " " + SmartLower(sSuitor2) + "? I was on the edge of my seat! " 
          if CoinFlip():
               if CoinFlip():
                    sText += "#Team" + sSuitor1.replace(" ", "").replace("The", "").replace("Her", "").replace("-", "")
               else:
                    sText += "#Team" + sSuitor2.replace(" ", "").replace("The", "").replace("Her", "").replace("-", "")
          
          return sText
          
class TweetTxtGen11(TweetTxtGen):
     # Include one little sumo wrestler fisting scene and they ban you from Amazon for life!
     def __init__(self): 
         super().__init__(ID = 11, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Include one little " + WordList(['non-consensual','interracial','pseudo-incest']).GetWord() + " "
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
          
class TweetTxtGen12(TweetTxtGen):
     # Ben Dover is truly the Hemmingway of triple penetration!
     def __init__(self): 
         super().__init__(ID = 12, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = self.AuthorName() + " is truly "
          sText += "the " + WordList(["Stephen King", "J.K. Rowling", "Jane Austen", 
                                      "William Shakespeare", "Shia Lebouf", 
                                      "Charles Dickens", "Hemmingway", 
                                      "Agatha Christie", "Maya Angelou", "Tolstoy", 
                                      "Melville", "Harper Lee", "John Grisham", 
                                      "Proust", "Emily Dickinson", "Truman Capote", 
                                      "James Patterson", "Dean Koontz"]).GetWord() + " of "
          sText += WordList(["gay", "lesbian", "MILF", "unicorn", "centaur", 
                             "werewolf", "mermaid", "merman", "mer-MILF", 
                             "dwarf", "dragon", "orc", "goat man", "futanari", 
                             "alien", "tentacle monster", "pirate", 
                             "lumberjack", "trapeze artist", "clown", 
                             "sumo wrestler", "were-horse", "gorilla", 
                             "dinosaur", "dinosaur"]).GetWord() + " "
          sText += WordList(["anal", "nipple play", "incest", "fisting", 
                             "twincest", "threesomes", "foursomes", 
                             "fivesomes", "bukkake", "bukkake", 
                             "forced feminization", "spanking", 
                             "rope play", "water-sports", "wife swapping", 
                             "69", "erotic asphyxiation", "orgy", 
                             "gangbang", "reverse gangbangs", "lactation", 
                             "double penetration", "triple penetration", 
                             "porn", "erotica", "edging", "BDSM", 
                             "bondage", "cuckolding"]).GetWord() + "!" 

          return sText
          
class TweetTxtGen13(TweetTxtGen):
     # Honestly, these books don't really get going until the 16th book 
     # in the series.
     def __init__(self): 
         super().__init__(ID = 13, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["You know,", "Honestly,", "To tell the truth", 
                            "In my opinion", "They say that"]).GetWord() + " "
          sText += "these books " + WordList(["really get going after", 
                                              "really hit their stride after", 
                                              "don't really get good until", 
                                              "really take off after", 
                                              "don't really take off until", 
                                              "really get good after"]).GetWord() + " "
          sText += "the " + str(randint(4, 29)) + "th book in the series"
          
          return sText
          
class TweetTxtGen14(TweetTxtGen):
     # CONTENT WARNING: book contains graphic depictions of veganism.
     def __init__(self): 
         super().__init__(ID = 14, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["WARNING", "CONTENT WARNING", "READER WARNING", 
                            "ALERT", "READER ALERT"]).GetWord() + ": "
          sText += "book contains " + WordList(["explicit", "explicit", "explicit", 
                                                "graphic", "graphic", "vivid"]).GetWord() + " " 
          sText += WordList(["depictions", "descriptions", "scenes"]).GetWord() + " of " 
          sText += WordList(["male comb-overs","vaping", "80's perms", 
                             "mullet haircuts", "people with facial tattoos",
                             "sports talk radio", "the 1970's", "trips to IKEA", 
                             "Bronies", "ferret grooming", "juice cleanses", 
                             "large animal husbandry", "dubstep", "tech bros",
                             "ham-and-pineapple pizza", "crossfit", "cat memes",
                             "kale smoothies", "veganism", "angry Game of Thrones fans"
                             "crossword puzzle solving", "sporks", "Cats: The Musical",
                             "fish being reheated in the microwave", "Justin Bieber's music",
                             "people listening to Nickleback", "Bernie Bros",
                             "tax preparation", "Twilight fan fiction",
                             "people promoting their podcast", "Cats: The Movie",
                             "older women discussing their colonoscopies", 
                             "Bitcoin investing", "Jazzercize", "the 90's",
                             "essential oil use", "Gwyneth Patlrow's vagina",
                             "hipster beard hygene", "bitchy soccer moms", 
                             "the music of Ariana Grande"]).GetWord() + "!"
          
          return sText
          
class TweetTxtGen15(TweetTxtGen):
     # I honestly had no idea that I was into bald centaurs until I read this book.
     def __init__(self): 
         super().__init__(ID = 15, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Fetishes = WordList(["kinky", "well-hung", "well-endowed", "naughty", "gay", "bisexual", "bearded", "bald", 
                                    "short", "mustachioed", "constantly-aroused", "repressed", "stay-at-home", 
                                    "blue-collar", "Asian", "cuckolded", "lactating", "submissive", "dominant", 
                                    "well-dressed", "flannel-wearing", "vegan", "dad bod", "pansexual", "hairless",
                                    "chubby", "black", "redheaded", "freckled", "lumber-sexual", "hipster",
                                    "husky", "mature", "retiree"])
          Creatures = WordList(["unicorns", "centaurs", "werewolves", "mermen", "dwarves", "dragons", "orcs", "popes", 
                                     "trolls", "goat-men", "futanari", "aliens", "tentacle monsters", "pirates", 
                                     "lumberjacks", "trapeze artists", "clowns", "sumo wrestlers", "were-horses", 
                                     "gorillas", "dinosaurs", "dinosaurs", "blacksmiths", "Japanese businessmen", 
                                     "guys named Steve", "zombies", "rodeo clowns", "elves", "Italians",
                                     "porn stars", "furries", "male nurses", "space aliens", "dads", "step-dads"])
          sText = "I honestly had no idea that I was into " + Fetishes.GetWord() + " "
          sText += Creatures.GetWord() + " "
          sText += "until I read this book." 
          
          return sText
          
class TweetTxtGen16(TweetTxtGen):
     # SPOILER ALERT: Amber winds up deep-throating a biker
     def __init__(self): 
         super().__init__(ID = 16, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "SPOILER ALERT: at the end, " + NamesFemale().FirstName() + " " 
          sText += WordList(["has anal sex with", "gets fisted by", "has her toes sucked by", "tries nipple play with", 
                                   "tries rope play with", "gets peed on by", "becomes a cuck-quean for", 
                                   "sixty-nines", "gets erotically asphyxiated by", "rims", "joins an orgy with", 
                                   "gets gangbanged by", "tries a reverse gangbang with", 
                                   "tries a double gangbang with", "gets double penetrated by", 
                                   "gets triple penetrated by", "films a porno with", "tries BDSM with", 
                                   "gets tied up by", "gets dominated by", "gets a Dirty Sanchez from", 
                                   "gets hot-wifed to", "lets the guys in the gym watch her with", 
                                   "gets her ass eaten by", "gives a foot-job to", "pegs",
                                   "spreads her legs for", "spreads her cheeks for", "bends over for", 
                                   "deep-throats", "gets tea-bagged by", "gets fisted by"]).GetWord() + " "
          sText += WordList(["a lumberjack", "a fireman", "a policeman", "a lifeguard", "a stunt man", "a bull rider",  
                                   "a fighter pilot", "a Chippendales dancer", "an astronaut", "a Navy SEAL", 
                                   "a Green Beret", "a cowboy", "a guitar player", "an olympic gold medalist", 
                                   "a pro surfer", "a private eye", "a paramedic", "a mechanic", "a biker", 
                                   "a pirate captain", "a highwayman", "a troubador", "a Viking warrior",
                                   "a jockey", "a sumo wrestler", "a bodybuilder", "a contortionist",
                                   "a Brony", "a reality TV star", "a taxidermist", "a pro wrestler"]).GetWord() 
          if CoinFlip():
               sText += " from " + DullPlaces().GetWord()
          
          return sText
          
class TweetTxtGen17(TweetTxtGen):
     # This was a good read, but was the lesbian anal scene really necessary?
     def __init__(self): 
         super().__init__(ID = 17, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["Delightful and provcative", "Good book", "I enjoyed this", "This was a good read", "Pretty good read", "Fun book", "A real page-turner"]).GetWord() + ", but was the "
          sText += WordList(["tentacle", "unicorn", "centaur", "man-o-taur", "gargoyle", "werewolf", "merman", "dwarf", "dragon", "orc", "troll", "goat-man", "futa", "alien", "tentacle monster", "clown", "sumo wrestler", "were-horse", "t-rex", "velociraptor", "dinosaur", "reverse merman", "cyborg", "were-shark", "gay", "lesbian", "dinosaur", "gargoyle", "lumberjack", "SWAT team", "construction worker", "male stripper", "cowboy", "MMA fighter"]).GetWord() + " "
          sText += WordList(["anal", "fisting", "toe-sucking", "nipple play", "incest", "twincest", "threesome", "foursome", "fivesome", "bukkake", "rope play", "water-sports", "cuck-queaning", "69", "orgy", "gangbang", "reverse gangbang", "double gangbang", "double penetration", "triple penetration", "porn", "BDSM", "bondage", "Dirty Sanchez", "hot-wifing", "water-sports", "enema", "rimming", "analingus", "glory hole", "fellatio", "deep throat", "cuckolding"]).GetWord() + " "
          sText += "scene really necessary?"
          
          return sText
          
class TweetTxtGen18(TweetTxtGen):
     # 'Delightful & provactive!' raves Dwarf Fisting Magazine 
     def __init__(self): 
         super().__init__(ID = 18, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "'" + WordList(["Delightful & provactive", "Thoughtful & heart-warming", "Heart-warming & transcendant", "Complex yet satisfying", "A real rollercoaster ride", "An emotional rollercoaster", "An edge-of-your-seat, stand-up-and-cheer page-turner", "Kept me literally glued to my Kindle", "Kept me literally nailed to my seat", "Un-put-downable", "A grand slam", "A home-run", "A modern classic"]).GetWord() + "!' "
          sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
          sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
          sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Erotic Asphyxiation", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 
               
          return sText
          
class TweetTxtGen19(TweetTxtGen):
     # 'Ben Dover's latest is a triumph!' applauds Goat-man Foursome Magazine 
     def __init__(self): 
         super().__init__(ID = 19, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "'" + self.AuthorName() + "'s latest is " + WordList(['a triumph', 'a triumph', 'a massive success', 'a masterpiece', 'an erotic masterpiece', 'a modern classic', 'a sexual classic', 'brilliant', 'a work of genius', 'an unmatched success', 'the next Harry Potter', 'the next 50 Shades of Gray', 'the next Hunger Games', 'un-put-downable', 'heart-warming and satisfying', 'very readable']).GetWord() + "!' "
          sText += WordList(["raves", "raves", "enthuses", "gushes", "applauds", "cheers", "celebrates", "salutes", "extols"]).GetWord() + " " 
          sText += WordList(["Unicorn", "Centaur", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Pirate", "Lumberjack", "Clown", "Sumo Wrestler", "Were-horse", "Dinosaur", "Dinosaur"]).GetWord() + " "
          sText += WordList(["Anal", "Fisting", "Nipple Play", "Incest", "Twincest", "Threesome", "Foursome", "Fivesome", "Bukkake", "Rope Play", "Water-sports", "Cuckolding", "69", "Erotic Asphyxiation", "Orgy", "Gangbang", "Double Gangbang", "Double Penetration", "Triple Penetration", "BDSM", "Bondage", "Wife-swapping", "Voyeurism", "Water-sports"]).GetWord() + " Magazine" 

          
          return sText
          
# class TweetTxtGen20(TweetTxtGen):
     # # Reply to this tweet and I'll tweet a randomly-generated naughty ebook title @ you!
     # ID = 20
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # sText = "Reply to this tweet and " 
          # if CoinFlip():
               # sText += "I'll tweet a " + WordList(["randomly", "computer", "bot", "algorithmically"]).GetWord () + "-generated " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title @ you!"
          # else:
               # sText += "get a custom " + WordList(["erotica", "smutty", "naughty", "erotic", "adult"]).GetWord() + " ebook title of your very own in reply! " + GetEmoji()
          # sText += " " + GetEmoji()

          
          # return sText
          
class TweetTxtGen21(TweetTxtGen):
     # Follow my sister bot @bot_lust to read naughty excerpts from this book (warning: NSFW!) ;-)
     def __init__(self): 
         super().__init__(ID = 21, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["Check out", "Follow", "Visit", "Take a look at"]).GetWord() + WordList([" my sister bot", " my bot-sibbling", ""]).GetWord() + " @bot_lust " + WordList(["to read what's inside", "to read " + self.SexyAdj.GetWord() + " excerpts from", "to see what's inside", "to read " + SexyAdjs().GetWord() + " bot-generated love scenes from"]).GetWord() + " this book (warning: NSFW!) " + GetEmoji()
          
          return sText
          
class TweetTxtGen22(TweetTxtGen):
     # Features a beautiful interracial relationship between a stegosaur and a reverse merman
     def __init__(self): 
         super().__init__(ID = 22, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Creatures = WordList(["Unicorn", "Centaur", "Man-o-taur", "Gargoyle", "Werewolf", "Merman", "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", "Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-horse", "T-Rex", "Velociraptor", "Stegosaur", "Plesiosaur", "Pterodactyl", "Reverse Merman", "Cyborg", "Vampire", "Zombie", "Were-shark", "Demon", "Incubus"])
          sSpecies1 = SmartLower(Creatures.GetWord())
          sSpecies2 = SmartLower(Creatures.GetWord(NotList = [sSpecies1]))
          
          sText = "Features a " + WordList(['beautiful', 'tender', 'loving', 'sweet', 'touching', 'heartfelt', 'heart-warming']).GetWord() + " interracial relationship between a " + sSpecies1 + " and a " + sSpecies2 
          
          return sText
          
class TweetTxtGen23(TweetTxtGen):
     # The edging scene goes on for 97 pages
     def __init__(self): 
         super().__init__(ID = 23, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "The " + WordList(["anal", "double anal", "lesbian orgy", "reverse gangbang", "Dirty Sanchez", 
                                           "fisting", "nipple play", "incest", "twincest", "threesome", "foursome", 
                                           "fivesome", "bukkake", "rope play", "pee-drinking", "cuckolding", "69", 
                                           "choking", "orgy", "gangbang", "double gangbang", "double penetration", 
                                           "triple penetration", "BDSM", "bondage", "wife-swapping", "voyeurism", 
                                           "water-sports", "public humiliation", "lactation", "age play", 
                                           "mutual masturbation", "edging", "forced orgasm", "domination", 
                                           "submission"]).GetWord() + " scene goes on for " + str(randint(20,119)) + " pages"
          
          return sText
          
class TweetTxtGen24(TweetTxtGen):
     # I had some trouble keeping the characters straight. Is Gary the blonde fireman with the 7" schlong or the brunette fireman with the 8" schlong?
     def __init__(self): 
         super().__init__(ID = 24, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "I had " + WordList(["a hard time", "some trouble", "a bit of a problem", "some difficulty"]).GetWord() + " keeping the characters straight. "
          if CoinFlip():
               sName = NamesFemale().FirstName()
               Lady = SmartLower(WordList(title.misc.TropesBadFemale().List + title.misc.TropesGoodFemale().List + title.misc.ProfFemale().List).GetWord())
               iLength = WordList([32,34,36]).GetWord()
               sCupSize = WordList(['D', 'DD']).GetWord()
               BoobNames = WordList(['boobs', 'tits', 'gazongas', 'coconuts', 'melons', 'bazookas', 'hooters', 'tatas', 'jugs', 'rack', 'titties', 'cantalopes', 'grapefruits', 'pom-poms'])
               sBoobName = BoobNames.GetWord()
               
               sText += "Was " + sName + " the blonde " + Lady + " with the " + str(iLength) + sCupSize + " " + sBoobName + " or the brunette " + Lady + " with the " + str(iLength + 2) + sCupSize + "D " + sBoobName + "?"
          else:
               sName = NamesMale().FirstName()
               Dude = SmartLower(WordList(title.misc.SpeciesMale().List + title.misc.ProfMale().List + title.misc.TropesMale().List).GetWord())
               iLength = randint (6, 12)
               PenisNames = WordList(['schlong', 'dick', 'bagpipe', 'rod', 'pole', 'willy', 'johnson', 'dingus', 'dong', 'package', 'prick', 'sausage', 'slim jim', 'stiffy', 'swizzle stick', 'tool', 'trouser snake', 'wiener'])
               sPenisName = PenisNames.GetWord()
               
               sText += "Was " + sName + " the blonde " + Dude + " with the " + str(iLength) + "\" " + sPenisName + " or the brunette " + Dude + " with the " + str(iLength + 1) + "\" " + sPenisName + "?"
          return sText
          
class TweetTxtGen25(TweetTxtGen):
     # Why don't I ever meet any horny, well-hung lumberjacks in real life?
     def __init__(self): 
         super().__init__(ID = 25, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Why don't I ever meet any " + WordList(["horny", "desperate", "lonely", "steamy", "single", "sensual", "bereft", "tragically widowed", "lustful", "sexually repressed", "loner", "bachelor", "naked"]).GetWord() + ", "
          sText += WordList(["sexy", "hot", "hunky", "handsome", "shirtless", "brawny", "virile", "clean-cut", 
                                 "stylish", "suave", "alluring", "gruff", "chiseled", "strapping", "attractive", 
                                 "erotic", "stunning", "well-hung", "well-endowed", "girthy", "hugely erect"]).GetWord() + " "
          sText += WordList(["lumberjacks", "firemen", "cops", "lifeguards", "stunt men", "bull riders", 
                                 "park rangers", "pilots", "Chippendales dancers", "astronauts", "attorneys", 
                                 "Navy SEALs", "Green Berets", "heart surgeons", "cowboys", "guitar players", 
                                 "olympic gold medalists", "private eyes", "professional surfers"]).GetWord() + " in real life?"
          return sText
          
class TweetTxtGen26(TweetTxtGen):
     # Experts recommend wearing a condom while you read this book
     def __init__(self): 
         super().__init__(ID = 26, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["Experts", "Doctors", "Medical professionals", "Scientists", "Studies"]).GetWord() + " recommend " 
          sText += WordList(["wearing a condom", "using birth control", "using protection", "avoiding pregnancy", "that women remain on the pill", "not operating heavy machinery", "that men discontinue the use of Viagra or Cialis"]).GetWord() + " "
          sText += "while reading this book"
          
          return sText
          
class TweetTxtGen27(TweetTxtGen):
     # I mean, who among us hasn't had a secret affair with our curvaceous cheerleader step-daughter?
     def __init__(self): 
         super().__init__(ID = 27, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = WordList(["Really", "I mean", "Honestly", "Let's get real", "Seriously", "For real though"]).GetWord() + ", "
          sText += "who among us hasn't " + WordList(["had a secret affair with", "secretly impregnated", "started a secret family with", "had a secret baby with", "accidentally showered with", "mistaken our girlfriend for", "gotten drunk and gotten a handjob from", "gotten drunk and eaten the ass of", "masturbated in the dressing room with", "played doctor with", "helped fertilize the eggs of", "spooned naked with", "watched a porno with"]).GetWord() + " "
          sText += "our " + SmartLower(title.misc.PhysCharFemale().GetWord()) + " " + SmartLower(title.misc.ProfGoodFemale().GetWord()) + " "
          sText += WordList(["step-daughter", "step-mom", "step-sister", "cousin", "sister-in-law", "daughter-in-law", "aunt", "niece", "neighbor", "MILF", "teacher"]).GetWord() + "?"
          
          return sText

class TweetTxtGen28(TweetTxtGen):
     # Of course in real life you should never attempt centaur bukkake without strict medical supervision.
     def __init__(self): 
         super().__init__(ID = 28, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sText = "Of course in real life you should never attempt " 
          sText += WordList(["tentacle", "unicorn", "centaur", "man-o-taur", "gargoyle", "werewolf", "merman", "dwarf", "dragon", "orc", "troll", "goat-man", "futanari", "alien", "tentacle monster", "clown", "sumo wrestler", "were-horse", "t-rex", "velociraptor", "dinosaur", "reverse merman", "cyborg", "were-shark"]).GetWord() + " "
          sText += WordList(["anal", "double anal", "fisting", "nipple play", "incest", "twincest", "cum-swapping", 
                                   "bukkake", "rope play", "pee-drinking", "cuckolding", "69", "erotic asphyxiation", 
                                   "double gangbang", "double penetration", "triple penetration", "BDSM", "bondage", 
                                   "water-sports", "public humiliation", "lactation", "age play", "edging", 
                                   "forced orgasm", "domination", "submission"]).GetWord() + " "
          sText += "without " + WordList(["strict medical supervision", "a note from your doctor", "waiting at least two hours after eating", "guidance from a trained professional", "help from a licensed dominatrix", "the buddy system", "regular checkups", "notifying the police", "an ambulance standing by", "a certified SCUBA instructor", "a friend that you can trust", "telling someone where you are", "paramedics on hand", "medical training", "power of attorney"]).GetWord()
          
          return sText

class TweetTxtGen29(TweetTxtGen):
     # I was hoping that Emily would hook up with Brad, but then SURPRISE! anal threesome with Jack!
     def __init__(self): 
         super().__init__(ID = 29, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sHerName = NamesFemale().FirstName()
          sHisName = NamesMale().FirstName()
          sTheirName = ""
          
          if CoinFlip():
               sTheirName = NamesFemale().FirstName()
          else:
               sTheirName = NamesMale().FirstName()
               
          sText = "I was rooting for " + sHerName + " " 
          sText += WordList(["to hook up with", "to get with", "to get together with", "to wind up with"]).GetWord() + " "
          sText += sHisName + ", but then " 
          sText += WordList(["SURPISE!", "nope, boom!", "watch out!", "*WOW!*", "nuh uh!", "guess what?", "*oh snap!!*", "PLOT TWIST!", "what the fuck??", "*SHOCKER!*"]).GetWord() + " "
          sText += WordList(["she does anal", "she does lesbian anal", "anal threesome", "fisting", "toe sucking", 
                                 "she tries nipple play", "it's a threesome", "it's a foursome", 
                                 "it's a fucking fivesome", "bukkake", "rope play", "she tries water-sports", 
                                 "she becomes a cuck-quean", "she sixty-nines", "she gets choked", "she does rimming", 
                                 "she joins an orgy", "gangbang", "reverse gangbang", "she does a double gangbang", 
                                 "double penetration", "triple penetration", "she films a porno", "she does bondage", 
                                 "a Dirty Sanchez", "hot-wifing", "she lets the guys in the gym watch her", 
                                 "she walks naked through Times Square", "she gets her ass eaten", "analingus", 
                                 "she spreads her legs", "a footjob"]).GetWord() + " with "
          if CoinFlip():
               sText += sTheirName + "!!"
          else:
               sText += "a " + SmartLower(WordList(["Unicorn", "Centaur", "Man-o-taur", "Gargoyle", "Werewolf", "Merman", 
                                               "Dwarf", "Dragon", "Orc", "Pope", "Troll", "Goat-man", "Futanari", 
                                               "Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-horse", 
                                               "T-Rex", "Velociraptor", "Stegosaur", "Plesiosaur", "Pterodactyl", 
                                               "Reverse Merman", "Cyborg", "Vampire", "Zombie", "Were-shark", 
                                               "Demon", "Incubus"]).GetWord()) + "!!"
          
          return sText

class TweetTxtGen30(TweetTxtGen):
     # I was stunned when it was revealed that Jack the handsome Cowboy 
     # was actually a gazillionaire!
     def __init__(self): 
         super().__init__(ID = 30, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sHisName = NamesMale().FirstName()
          
          sText = "I was " + WordList(["stunned", "shocked", "flabbergasted", "floored", "blown away", "so surprised"]).GetWord() + " when it was revealed that "
          sText += sHisName + " the " + WordList(["sexy", "hot", "hunky", "handsome", "shirtless", "brawny", "virile", "clean-cut", "stylish", "suave", "smooth-talking", "gruff", "chiseled", "strapping", "attractive", "erotic", "stunning", "well-hung", "well-endowed", "girthy", "gentlemanly", "charming", "blonde", "brunette", "redheaded", "taciturn", "rakish", "heart-throb", "beefcake", "tattooed", "bearded"]).GetWord() + " " 
          sText += WordList(["lumberjack", "fireman", "policeman", "lifeguard", "stunt man", "bull rider", 
                                 "park ranger", "pilot", "Chippendales dancer", "astronaut", "Navy SEAL", 
                                 "Green Beret", "cowboy", "guitar player", "olympic gold medalist", 
                                 "pro surfer", "private eye", "paramedic", "mechanic", "biker", 
                                 "nude model", "pirate captain", "highwayman", "troubador", 
                                 "Viking warrior", "family man"]).GetWord() + " "
          sText += "was " + WordList(["really", "actually", "in fact"]).GetWord() + " a " + WordList(["millionaire", "multi-millionaire", "billionaire", "trillionaire", "gazillionaire", "king", "prince", "duke", "marquis", "manor lord", "sheikh", "pope", "crown prince", "CEO"]).GetWord() + "!"
          
          return sText

class TweetTxtGen31(TweetTxtGen):
     # ME YELLING AT THE MAIN CHARACTER: No Emily! You can't sleep with Jack! 
     # He's your long-lost twin brother!
     def __init__(self): 
         super().__init__(ID = 31, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sHerName = NamesFemale().FirstName()
          sHisName = NamesMale().FirstName()
          
          sHerName2 = NamesFemale().FirstName()
          sHisName2 = PlainNamesMale().FirstName()
          
          sText = "ME, " + WordList(["YELLING", "YELLING", "SCREAMING"]).GetWord() + " AT THE " + WordList(["BOOK", "BOOK", "PAGE", "MAIN CHARACTER"]).GetWord() + ": No " + sHerName + "! Don't " + WordList(["sleep with", "sleep with", "have sex with", "hook up with"]).GetWord () + " " + sHisName + "! "
          sText += "He " + WordList(["is your long lost twin brother", 
                                             "is secretly married to " + sHerName2, 
                                             "is the serial killer that's been terrorizing " + DullPlaces().GetWord(),
                                             "just wants you for your " + WordList(["millions", "billions", "bitcoin", "successful fondue restaurant", "enormous titties"]).GetWord(), 
                                             "is the mysterious " + WordList(["man in black","masked man","drifter","hit man","assassin","vigilante"]).GetWord() + " that shot your father",
                                             "is an imposter named " + sHisName2 + " and he's really from " + DullPlaces().GetWord(),
                                             "is secretly a " + WordList(["werewolf", "were-horse", "were-shark", "were-gorilla", "were-dinosaur","vampire","zombie","ghost"]).GetWord(),
                                             "is being mind-controlled by Dr. " + InnuendoLastNames().GetWord(),
                                             "is an evil clone",
                                             "is the father you've never met",
                                             "is your " + WordList(["father","long lost father","real dad","biological father"]).GetWord(),
                                             "is a hitman for the " + WordList(["Italian", "Irish", "Russian", "French", "Canadian", "French-Canadian", "Sicilian", "Japanese", "Hawaiian", "Belgian"]).GetWord() + " mafia",
                                             "has a prosthetic " + WordList(["nose", "nose", "ear", "nipple", "ass", "penis", "dick", "cock"]).GetWord(),
                                             "is secretly from " + DullPlaces().GetWord(),
                                             "is in love with " + sHerName2,
                                             "is a spy for " + WordList(["your wicked step-mother","your evil step-brother","your evil clone","the Russians","the Chinese","your scheming boss","the Nazis", "the alien invaders"]).GetWord(),
                                             "is sleeping with your " + WordList(["sister","half-sister","mom","step mom","friend","best friend","daughter","mother-in-law","sister-in-law","twin sister"]).GetWord(),
                                             "is blackmailing your " + WordList(["brother","dad","mom","step-brother","sister","sister-in-law","step-dad"]).GetWord(),
                                             "has no sense of smell"]).GetWord() + "!"
          
          return sText

class TweetTxtGen32(TweetTxtGen):
     # Ben Dover is definitely the best erotica author working in Tuscaloosa!
     def __init__(self): 
         super().__init__(ID = 32, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sAuthor = self.AuthorName()
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

class TweetTxtGen33(TweetTxtGen):
     # "A wild fuckfest!" -Abraham Lincoln
     def __init__(self): 
         super().__init__(ID = 33, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adjs = WordList(["thrilling", "wild", "sensual", "perverted", "raunchy", "tasteless", "lascivious", "erotic", "horny", 
                                   "delightful", "sinful", "arousing", "naughty", "depraved", "lustful", "wicked", "outrageous", "delicious", 
                                   "stimulating", "sexy", "provocative", "lewd", "wicked", "shameless", "stimulating", "kinky", "juicy",
                                   "wanton"])
          Celebs = WordList(["Abraham Lincoln", "Winston Churchill", "Barak Obama", "Mother Theresa", 
                                   "Salman Rushdie", "Albert Einstein", "Hillary Clinton", "Isaac Asimov", "Jonathan Franzen", 
                                   "Cormac McCarthy", "Ghandi", "Boutros Boutros-Ghali", "Bob Dylan", "The Dalai Lama", "Elon Musk", 
                                   "Warren Buffett", "Stephen King", "Bill Gates", "Billy Graham", "Jimmy Carter", "Oprah Winfrey",
                                   "Neil Armstrong", "Stephen Hawking", "Al Gore", "Bernie Sanders"])
          
          if CoinFlip():
               sAdj1 = Adjs.GetWord()
               sAdj2 = Adjs.GetWord(NotList = [sAdj1])
               sText = "\"" + sAdj1.title() + " and " + sAdj2 + "!\"\n"
          elif CoinFlip():
               sAdj = Adjs.GetWord()
               if sAdj[0] in ('a','e','i','o','u'):
                    sText = "\"An " + sAdj + " fuckfest!\"\n"
               else: 
                    sText = "\"A " + sAdj + " fuckfest!\"\n"
          elif CoinFlip():
               sAdj = Adjs.GetWord()
               sText = "\"" + sAdj.title() + " AF!\"\n"
          elif CoinFlip():
               sText = "\"I'm so horny for this!\"\n" 
          elif CoinFlip():
               sText = "\"I got off on this!\"\n" 
          elif CoinFlip():
               sText = "\"This is some kinky shit, but I'm into it!\"\n" 
          else:
               sText = "\"What the fuck did I just read??\"\n" 
               
          sText += " ~" + Celebs.GetWord()
          
          return sText

class TweetTxtGen34(TweetTxtGen):
     # This is widely considered to be the Lord of the Rings of anal fisting books.
     def __init__(self): 
         super().__init__(ID = 34, Priority = GenPriority.AboveAverage)
     
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
                                          
          sText = "This is " + WordList(["widely regarded","widely considered","broadly regarded","broadly considered"]).GetWord() + " "
          sText += "to be the '" + Books.GetWord() + "' of " + EroticaNiches.GetWord() + " books."
          
          return sText

class TweetTxtGen35(TweetTxtGen):
     # I really identified with the protagonist. I too would like to be spooned 
     # by a naked lumberjack.
     def __init__(self): 
         super().__init__(ID = 35, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sJobGuy = SmartLower(title.misc.ProfMale().GetWord())
          sText = "I really identified with the " + WordList(["protagonist","main character","lead character","mc"]).GetWord() + ". "
          
          iRand = randint(1,6)
          if iRand == 1:
               sText += "I too would like to be spooned by a naked " + sJobGuy + "."
          elif iRand == 2:
               sText += "I too want to lick " + WordList(["syrup","whipped cream","honey","melted chocolate"]).GetWord() + " "
               sText += "off a " + sJobGuy + "'s naked body."
          elif iRand == 3:
               sText += "I would also like to soap up a handsome, rugged " + sJobGuy + " in the shower."
          elif iRand == 4:
               sText += "I too would like to cover a naked " + sJobGuy + " with flavored lube."
          elif iRand == 5:
               sText += "I too would like to rub baby oil all over a naked " + sJobGuy + "."
          else:
               sText += "I too would like to meet " + AddArticles(sJobGuy) + " who looks good naked and likes to eat ass."
          
          return sText

class TweetTxtGen36(TweetTxtGen):
     # Extremely educational. I learned so much about clit clamps and lactation.
     def __init__(self): 
         super().__init__(ID = 36, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          SexToys = WordList(["clit clamps","Ben Wa balls","nipple clamps","cock rings","anal hooks","spreader bars",
                                   "ball gags","butt plugs","dental dams","clothes pins","sex swings","riding crops",
                                   "nose hooks","chastity belts","erotic furniture","clit pumps","sybians","nylons",
                                   "anal beads"])
                              
          Fetishes = WordList(["lactation","bukkake","age play","tea bagging","fem-dom","butt play",
                                    "fisting","caning","edging","erotic asphyxiation","smothering","enemas",
                                    "frottage","cuckolding","cuckqueaning","cock and ball torture","electrostimulation",
                                    "impact play","Shibari","water sports","race play"])
                                    
          sText = WordList(["An extremely","A very","A highly"]).GetWord() + " educational book. I learned so much about " 
          sText += SexToys.GetWord() + " and " + Fetishes.GetWord() + "."
          
          return sText          
          
class TweetTxtGen37(TweetTxtGen):
     # This was Ben Dover's last book before he was banned from Amazon for 
     # writing a scene involving a goat man and bukkake.
     def __init__(self): 
         super().__init__(ID = 37, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adjs = WordList(['filthy','shocking','provactive','outrageous','disgusting',
                           'taboo','naughty','tasteless','completely gratuitous'])
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
          
          if self.AuthorGender() == Gender.Male:
               # male
               sText = "This was " + self.AuthorName() + "'s last book before "
               sText += "he was banned from Amazon for " + SmartLower(AddArticles(Adjs.GetWord())) + " scene involving "
               
          else:
               # female
               sText = "This was " + self.AuthorName() + "'s final book before "
               sText += "she was banned from Amazon for " + SmartLower(AddArticles(Adjs.GetWord())) + " scene involving "
               
          iRand = randint(1,5)
          if iRand == 1:
               sText += SexToys.GetWord() + " and "
               if CoinFlip():
                    sText += SmartLower(AddArticles("underage " + Species.GetWord()))
               else:
                    sText += SmartLower(AddArticles(Species.GetWord()))
          elif iRand == 2:
               sText += SexToys.GetWord() + " and "
               if CoinFlip():
                    sText += "underage "
               sText += SexActs.GetWord() 
          elif iRand == 3:
               if CoinFlip():
                    sText += SmartLower(AddArticles("underage " + Species.GetWord()))
               else:
                    sText += SmartLower(AddArticles(Species.GetWord()))
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
          
class TweetTxtGen38(TweetTxtGen):
     # By day, erotica author Ben Dover is a Wedding Photographer from Scranton.
     def __init__(self): 
         super().__init__(ID = 38, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sMaleJob = DullJobsMale().GetWord()
          sFemaleJob = DullJobsFemale().GetWord()
          sPlace = DullPlaces().GetWord()
          
          if self.AuthorGender() == Gender.Male:
               # male
               sText = "By day, erotica author " + self.AuthorName() + " is " + SmartLower(AddArticles(sMaleJob)) + " from " + sPlace + "."     
          else:
               # female
               sText = "By day, erotica author " + self.AuthorName() + " is " + SmartLower(AddArticles(sFemaleJob)) + " from " + sPlace + "."
          
          return sText     

# I have to tell you, I did not expect the ~SPOILER ALERT~ velociraptor attack!          
class TweetTxtGen39(TweetTxtGen):
     def __init__(self): 
         super().__init__(ID = 39, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Surprises = WordList(['velociraptor attack','space alien invasion','Martian invasion','T-Rex attack',
                                        'man-eating tiger attack','zombie invasion','polar bear attack',
                                        'Great White Shark attack','giant spider attack','venemous snake attack',
                                        'shape-shifting alien invasion','spitting cobra attack',
                                        'boa constrictor attack','water buffalo stampede','Viking invasion'])
          Alerts = WordList(['~SPOILER ALERT~','**SPOILER ALERT**','~*SPOILER ALERT*~','[SPOILER ALERT]',
                                   '~SPOILER WARNING~','**SPOILER WARNING**','~*SPOILER WARNING*~','[SPOILER WARNING]',
                                   '~SPOILERS~','**SPOILERS**','~*SPOILERS*~','[SPOILERS]'])
                                   
          iRand = randint(1,5)
          if iRand == 1:
               sText = "I have to tell you, I did not expect the " + Alerts.GetWord() + " " + Surprises.GetWord() + "!"
          elif iRand == 2:
               sText = "The part with the " + Alerts.GetWord() + " " + Surprises.GetWord() + " was very unexpected!"
          elif iRand == 3:
               sText = "I did not see the part with the " + Alerts.GetWord() + " " + Surprises.GetWord() + " coming!"
          elif iRand == 4:
               sText = "I was definitely caught off guard when the " + Alerts.GetWord() + " " + Surprises.GetWord() + " happened!"
          else:
               sText = "I was certainly surprised by the unexpected twist with the " + Alerts.GetWord() + " " + Surprises.GetWord() + "!"

          
          return sText     
          
class TweetTxtGen40(TweetTxtGen):
     # More steamy lesbian vampire wife-swapping erotica from author 
     # Ivana Schaft-Hyman!
     def __init__(self): 
         super().__init__(ID = 40, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          Adjs = WordList(['steamy','hot','naughty','dirty','ground-breaking','filthy','raunchy',
                               'exciting','thrilling'])
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
                                          
          sText = "Get the latest " + Adjs.GetWord() + " ebook "
          sText += "from " + WordList(['noted','celebrated','leading',
                                       'best-selling']).GetWord() + " " 
          sText += EroticaNiches.GetWord() + " author " + self.AuthorName() + "!"
          
          return sText     
          
class TweetTxtGen41(TweetTxtGen):
     # The sex scenes in this book were so grounded and realistic!
     def __init__(self): 
         super().__init__(ID = 41, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          RealAdjs = WordList(['grounded','realistic','plausible','earthy',
                                    'down-to-earth','believable','authentic',
                                    'emotional','touching','gritty','genuine',
                                    'tasteful','heartfelt','tender','sweet',
                                    'heart-warming'])
          sRealAdj1 = RealAdjs.GetWord()
          sRealAdj2 = RealAdjs.GetWord(NotList = [sRealAdj1])
          
          sText = WordList(["The sex scenes in this book were so " + sRealAdj1 + " and " + sRealAdj2 + "!"
                               ,"The love scenes in this book were so " + sRealAdj1 + " and " + sRealAdj2 + "!"
                               ,"The sex in this book was surprisingly " + sRealAdj1 + " and " + sRealAdj2 + "!"
                               ,"The love-making in this story is really quite " + sRealAdj1 + "!"
                               ,"I was surprised by how " + sRealAdj1 + " and " + sRealAdj2 + " the sex scenes were!"
                               ]).GetWord()
          
          return sText     
          
class TweetTxtGen42(TweetTxtGen):
     # LEGAL DISCLAIMER: Wal-Mart does not condone cum-swapping or genital piercings.
     def __init__(self): 
         super().__init__(ID = 42, Priority = GenPriority.AboveAverage)
     
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
                                   "Tesco","Best Buy"
                                ]).GetWord() + " "
          sText += "does not condone " + sAct1 + " or " + sAct2 + "."
          
          return sText     
          
class TweetTxtGen43(TweetTxtGen):
     # I was so surprised when it turned out that Vaughn the dumpy plumber 
     # had a 12-inch schlong!
     def __init__(self): 
         super().__init__(ID = 43, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          BlueCollarNotList = ['serf','peasant','farm','paige']
          sHisName = DiverseNamesMale().FirstName()
          
          BadAdj = WordList(['awkward','bald','dumpy','fat','nerdy','pimply','short','ugly'])
          Dick = WordList(['boner','dick','erection','hot-rod','joystick','package','penis',
                               'popsicle','prick','rod','schlong','thing','tool','woody',
                               'pocket-rocket','johnson','weiner'])
          DickSize = WordList(['a twelve-inch','a foot-long','a thirteen-inch','a fourteen-inch','a ten-inch',
                                    'a nine-inch','a giant','an eleven-inch','a super-size','a massive',
                                    'a jumbo'])
                                    
          sText = "I was so surprised when it turned out that " + sHisName + " "
          sText += "the " + BadAdj.GetWord() + " " + JobBlueCollar().GetWord(NotList = BlueCollarNotList) + " "
          sText += "had " + DickSize.GetWord() + " " + Dick.GetWord() + "!"
          
          return sText     
          
class TweetTxtGen44(TweetTxtGen):
     # I *knew* that Viola shouldn't trust Jack! Not after he called her 
     # vagina a 'fish taco'!
     def __init__(self): 
         super().__init__(ID = 44, Priority = GenPriority.High)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sHisName = NamesMale().FirstName()
          sHerName = NamesFemale().FirstName()
          
          VagNotList = ['box','cooch','flower','honey','lady','kitty','muff','pie','puss',
                           'quim','vag','womanhood']
          sVagName = VaginaSlang().GetWord(NotList = VagNotList)

          sText = "I *knew* that " + sHerName + " shouldn't trust " + sHisName + "! "
          if randint(1,10) == 10:
               sText += "Not after he refused to eat her ass!"
          else:
               sText += "Not after he referred to her vagina as a \"" + sVagName + "\"!"
          
          return sText     

class TweetTxtGen45(TweetTxtGen):
     # I was rooting for Vance to get together with Vanessa, so it was quite 
     # a shock when he ran off with Pedro!
     def __init__(self): 
         super().__init__(ID = 45, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sText = ""
          
          sHerName = NamesFemale().FirstName()
          sHisName1 = NamesMale().FirstName()
          sHisName2 = PlainNamesMale().FirstName()
          
          sText = "I was " + WordList(["rooting for", "hoping for"]).GetWord() + " "
          sText += sHisName1 + " to get together with " + sHerName + ", "
          sText += "so " + WordList(["it was quite a shock when","I was stunned when"]).GetWord() + " "
          sText += "he had sex with " 
          sText += sHisName2 + " instead!"
          
          return sText
          
class TweetTxtGen46(TweetTxtGen):
    # This book taught me the tantric sex technique called the "Mexican Gorilla"
    def __init__(self): 
         super().__init__(ID = 46, Priority = GenPriority.AboveAverage)
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sText = ""

        sSexTechnique = WordList(["the tantric sex technique","the sex technique",
                                   "the sexual position","the sex position",
                                   "the tantric sex position","the sex move"]).GetWord()
        sDirtyPhrase = TantricTechniques().GetWord()

        iRand = randint(1,9)
        if iRand == 1:
             sText = "Before I read this book I had never even heard of " + sSexTechnique + " called \"The " + sDirtyPhrase + ".\""
        elif iRand == 2:
             sText = "Before I read this I didn't even know what " + AddArticles(sDirtyPhrase, cBracket = "\"") + " was."
        elif iRand == 3:
             sText = "I had never even heard of " + AddArticles(sDirtyPhrase, cBracket = "\"") + " before but now I want to try it in real life!"
        elif iRand == 4:
             sText = "I've read about the \"" + sDirtyPhrase + "\" technique before in Cosmo but you need at least three people to try it."
        elif iRand == 5:
             sText = "I would love to try " + AddArticles(sDirtyPhrase, cBracket = "\"") + " with my boyfriend but I don't think I'm flexible enough."
        elif iRand == 6:
             sText = "The part where he gives her " + AddArticles(sDirtyPhrase, cBracket = "\"") + " is the filthiest thing I've ever read in my life."
        elif iRand == 7:
             sText = "I want to try " + AddArticles(sDirtyPhrase, cBracket = "\"") + " but my boyfriend thinks its disgusting."
        elif iRand == 8:
             sText = "If you haven't heard of " + AddArticles(sDirtyPhrase, cBracket = "\"") + " before, do NOT google it."
        elif iRand == 9:
             sProtection = WordList(["a dental dam","protection","condoms","surgical gloves"]).GetWord()
             sText = "If you're going to try " + AddArticles(sDirtyPhrase, cBracket = "\"") + ", both you and your partner need to wear " + sProtection + "."
        else:
             sText = "This book introduced me to " + sSexTechnique + " known as \"The " + sDirtyPhrase + ".\""


        return sText     

class TweetTxtGen47(TweetTxtGen):
    # Yes, this book does contain some man-on-horse frottage scenes, but it's all consensual!
    def __init__(self): 
         super().__init__(ID = 47, Priority = GenPriority.High)
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sText = ""

        Numbers = WordList(["double","triple","quaduple","quintuple"])
        MaleJobs = WordList(["biker",
                                "body builder",
                                "carnie",
                                "circus clown",
                                "construction worker",
                                "cowboy",
                                "coal miner",
                                "oil rigger",
                                "long-haul trucker",
                                "luchador",
                                "lumberjack",
                                "mime",
                                "MMA fighter",
                                "pirate",
                                "rodeo clown",
                                "sailor",
                                "SCUBA diver",
                                "sumo wrestler"])

        sText = WordList(["Yes","Sure","It's true"]).GetWord() + ", "
        sText += "this book DOES contain "

        iRand = randint(1,10)
        if iRand == 1:
            sText += "a scene where " + WordList(["a baguette",
                                                  "a can of Mountain Dew",
                                                  "a cantaloupe",
                                                  "a jar of chunky peanut butter",
                                                  "an eggplant",
                                                  "a jar of quarters",
                                                  "a large McDonald's french fries",
                                                  "a pack of hotdogs",
                                                  "a live octopus",
                                                  "a pineapple"]).GetWord() + " "
            sText += "is inserted into someone's " + WordList(["anus","colon","rectum"]).GetWord()
        elif iRand == 2:
            sText += "a scene of man-on-" + WordList(["basilisk",
                                                      "bee hive",
                                                      "boa constrictor",
                                                      "centaur",
                                                      "dinosaur",
                                                      "donkey",
                                                      "falcon",
                                                      "firetruck",
                                                      "gargoyle",
                                                      "goat",
                                                      "helicopter",
                                                      "hippogriff",
                                                      "kraken",
                                                      "leprechaun",
                                                      "orca",
                                                      "robot",
                                                      "salad",
                                                      "sea serpent",
                                                      "swamp creature",
                                                      "vending machine",
                                                      "walrus",
                                                      "wookie",
                                                      "werebear"
                                                      ]).GetWord() + " "
            sText += "sexual " + WordList(["intercourse", "relations"]).GetWord()
        elif iRand == 3:
            sText += "an erotic " + MaleJobs.GetWord() + " "
            sText += WordList(["gangbang","orgy","foursome","bukkake scene"]).GetWord()
        elif iRand == 4:
            sText += WordList(["quadruplet","quintuplet","sextuplet","septuplet","octuplet"]).GetWord() + " twincest"
        elif iRand == 5:
            sText += "a public " + str(randint(20,100)) + "-" + MaleJobs.GetWord() + " "
            sText += WordList(["anal gangbang","prison gangbang","orgy","bukkake scene"]).GetWord()
        elif iRand == 6:
            sText += AddArticles(MaleJobs.GetWord(),bMakeUpper = False) + " "
            sText += WordList(["gangbang","orgy","bukkake scene"]).GetWord() + " "
            sText += WordList(["in a library","in a church","in a synagogue","in a Starbucks",
                               "at the circus","at an ice-skating rink","in a yoga studio",
                               "on roller skates","on ice skates","at a Subway Sandwiches",
                               "at a Burger King", "on a trampoline","in a food court"]).GetWord()
        elif iRand == 7:
            sText += "a scene with a " + WordList(["guy","dude","man"]).GetWord() + " strapped into "
            sText += AddArticles(Colors().GetWord(), bMakeUpper = False).lower() + " "
            sText += WordList(["corduroy","denim","flannel","fur",
                               "leather","nylon","pleather",
                               "polyester","PVC","spandex",
                               "vulcanized rubber"]).GetWord() + " gimp suit"
        elif iRand == 8:
            sText += "a scene with "
            sText += WordList(["a chunky peanut butter",
                               "a Diet Coke",
                               "a micro-brewed craft beer",
                               "a pickle juice",
                               "a soy milk",
                               "a venti iced latte", 
                               "a whale semen",
                               "a greek yogurt",
                               ]).GetWord() + " enema"
        elif iRand == 9:
            Celebs = WordList(["The Dalai Lama","Ryan Reynolds","The Pope","German Chancellor Angela Merkel",
                               "Elvis Presley", "Beyoncé", "the Harlem Globetrotters", "Post Malone",
                               "Arnold Schwarznegger","Miss America","Martha Stewart", "Vladamir Putin",
                               "Bruce Lee", "Batman", "Hugh Jackman", "JFK", "the Spice Girls",
                               "The cast of Glee", "Drake", "Ed Sheeran", "Lady Gaga", "Ariana Grande",
                               "Kim Kardashian", "Tom Hanks", "Vin Diesel", "Nicholas Cage","The Hulk",
                               "The Simpsons","Elmo from Sesame Street","Elon Musk","Taylor Swift",
                               "One Direction", "John Cena", "Henry Kissinger", "Val Kilmer", "Bananorama",
                               "Donald Duck","Elsa from 'Frozen'","Mr. T","Dr. Phil","Oprah",
                               "Spiderman","Ice Cube","the cast of Hamilton","the Power Rangers",
                               "BTS","Johnny Depp","Harry Potter","Hermione from Harry Potter",
                               "Kanye West"])
            sCeleb1 = Celebs.GetWord()
            sCeleb2 = Celebs.GetWord(NotList = [sCeleb1])
            sText += WordList(["a gangbang", "an orgy", "a prison gangbang", "a bukkake gangbang"]).GetWord() + " "
            sText += "involving " + sCeleb1 + " and " + sCeleb2
        elif iRand == 10:
            sText += "a scene of " + MaleJobs.GetWord() + " pee-drinking"
        sText += ", but it's all consensual!"

        return sText

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText          
          
# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText
          
# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     

# class TweetTxtGen44(TweetTxtGen):
     # The sexy read that was BANNED on Amazon! Now available on Smashwords
     # ID = 44
     # Priority = 2
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sText = ""
          
          # return sText     
                                   
def GetTweetText(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None, 
                 TweetTxtHistoryQ = None,
                 sAuthorName = "", AuthorGender = Gender.Neuter):
    #the bot's images are the random parts but we need to be careful that this isn't constantly generating static duplicate text. twitter won't like that.
    sTxt = ""
    Gen = None
     
    GenType = None 
    HistoryQ = None 
     
    if not Type is None:
        GenType = Type 
    else:
        GenType = None 
     
    if not TweetTxtHistoryQ is None:
        HistoryQ = TweetTxtHistoryQ
     
    GenSel = GeneratorContainer(TweetTxtGen, 1, HistoryQ) #sAuthorName = sAuthorName, AuthorGender = AuthorGender)
    if bTest:
        Gen = GenSel.GetGenerator(iGeneratorNo)
    else:
        Gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
     
    if not Gen is None:
        Gen._AuthorName = sAuthorName
        Gen._AuthorGender = AuthorGender
        sTxt = Gen.GenerateTweet()

        # bots using hashtags can lead to shadowbans. so we have to use sparingly.
        if randint(1,5) == 5:
            sTxt += " #" + Hashtags().GetWord()
    else:
        sTxt = ""
     
    return sTxt  
     
