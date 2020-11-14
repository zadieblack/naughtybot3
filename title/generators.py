#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import re, sys
from decimal import Decimal
from random import *
from util import *
from names import *
from gen import *
import misc
from title.characters import *
import title.chargenerator as char
import title.misc as titmisc
import title.titletemplates as templates
from title.util import *

PromoHistoryQ = HistoryQ(2)

class TitleGen(Generator):          
    def _getFMs_(self):
        FMs = ""
          
        iRandLen = randint(4,10)
        for x in range(1, iRandLen):
            iRandChoice = randint(1,3)
            if iRandChoice == 1:
                FMs += "F"
            else:
                FMs += "M"
                    
        if "M" not in FMs:
            FMs += "M"
        elif "F" not in FMs:
            FMs += "F"
          
        return FMs
    
    def __init__(self, ID = -1, 
                 Priority = GenPriority.Normal, 
                 Type = GeneratorType.Normal, 
                 Disabled = False, 
                 sTxt = "", 
                 Template = templates.TitleTemplateHHDefault()):
        super().__init__(ID = ID, Priority = Priority, Disabled = Disabled, sTxt = sTxt)

        self.Template = Template
        self.ExclTemplateTags = []
        self.ReqTemplateTags = []

        self.ImgTxt = ""
        self.SetImgText("")
        self.TweetTxt = ""
        self.AuthorName = ""

        if CoinFlip():
            self.AuthorGender = Gender.Male 
        else:
            self.AuthorGender = Gender.Female

    def Generate(self):
        sTweet = self.GenerateTweet()
        self.ImgTxt = sTweet
        self.SetImgText(sTweet)

    def GenerateTweet(self):
        self.VerbsBy = misc.BookVerbsBy()
        self.VerbsTo = misc.BookVerbsTo()
        self.Gerunds = misc.BookGerunds()
        self.HerName = NamesFemale().FirstName()
        self.HisName = NamesMale().FirstName()
        self.SubtitleCoda = titmisc.SubtitleCoda()

        return ""

    def SetImgText(self,stxt = ""):
        if self.Template is None:
            self.Template = templates.TitleTemplateHHDefault()

        if not stxt is None:
            self.Template.ClearLineText()
            self.Template.AddLineText(stxt)

    def GetTitleFromFile(self, sFileName = ""):
        bSuccess = True 
        if sFileName == "":
            sFileName = FAVTITLE_FILENAME
     
        Titles = [""]
        iTitleCount = 0

        Details = [] 
        Lines = []
        sImgTxt = ""
          
        try:
            with open(sFileName, 'r') as infile:
                for line in infile:
                    Lines.append(line.strip())
                         
        except OSError as err:
            print("**File IO ERROR READING " + sFileName + ": " + str(err) + "**\n")
            bSuccess = False

        if len(Lines) > 0:
            iLineNo = 0
            # ignore lines until we find our first detail line
            for iLineNo, line in enumerate(Lines):
                if len(line) > 4 and line[:2] == "{{" and line[-2:] == "}}":
                    break
            Lines = Lines[iLineNo:]

            if Lines[0][:2] == "{{" and Lines[0][-2:] == "}}":
            # This is a new entry 
                Details = Lines[0][3:-3].split("][")
                Lines = Lines[1:]

            # Next lines should be the imgtxt. append it until we
            # hit a divider
                for iLineNo, line in enumerate(Lines):
                    if line == titutil.FAVTITLE_DIVIDER:
                        break
                    if not sImgTxt == "":
                        sImgTxt += "\n"
                    sImgTxt += line
                Lines = Lines[iLineNo + 1:] # skip next divider

                #print("sImgTxt from " + sFileName + " for gen # " + str(Details[0]) + " is [" + sImgTxt + "]")
            else: 
                bSuccess = False
                print("ERROR: Did not find a details line.")

            # We've got our generator info. Now read in the rest of 
            # the file and spit it back out minus the gen we just read
            #print("Writing rest of lines back to file")
            try:
                with open(sFileName, 'w') as outfile:     
                    for iLineNo, line in enumerate(Lines, start  = iLineNo):
                        outfile.write(line + "\n")
          
            except OSError as err:
                print("**File IO ERROR WRITING " + sFileName + ": " + str(err) + "**\n")
                bSuccess = False
            # Now that's done lets put our info into this generator!

            if len(Details) > 3:
            #    print("Populating generator with file data")

            # 1st item is ID #
                self.ID = int(Details[0])

            # 2nd item is template #
                sTemplateID = Details[1]
                TemplateSelector = GeneratorContainer(templates.TitleTemplate)
                self.Template = TemplateSelector.GetGenerator(sTemplateID)

            # 3rd item is author name
                self.AuthorName = Details[2]

            # 4th item is author gender
                if Details[3].lower() == "male":
                    self.AuthorGender = Gender.Male
                elif Details[3].lower() == "female":
                    self.AuthorGender = Gender.Female
                else:
                    self.AuthorGender = Gender.Neuter

            # 5th item is required template tags (optional)
                if len(Details) > 4:
                    tags = []
                    for tag in Details[4].split(","):
                        if len(tag) > 0:
                            self.ReqTemplateTags.append(tag)

            # 6th item is excluded template tags (optional)
                if len(Details) > 5:
                    tags = []                    
                    for tag in Details[5].split(","):
                        if len(tag) > 0:
                            self.ExclTemplateTags.append(tag)
            else: 
                bSuccess = False
                print("ERROR: Did not have data so could not populate generator.")

            # Finally dont forget about the image text!!
            self.ImgTxt = sImgTxt
            self.SetImgText(sImgTxt)
        else: 
            bSuccess = False 

        #print("Pulled image text from file.\nRequired tag list is " + str(self.ReqTemplateTags) + "\nExcluded tag list is " + str(self.ExclTemplateTags))
        return bSuccess

def GetTweetGenerator(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetHistoryQ = None):
     gen = None
     GenType = None 
     
     if not Type is None:
          GenType = Type 
     else:
          GenType = None 

     GC = GeneratorContainer(TitleGen, HistoryQ = TweetHistoryQ)
     
     iSwitch = 999
     
     if bTest:
          gen = GC.GetGenerator(iGeneratorNo)
          if gen == None:
               gen = Generator()
     else:
          gen = GC.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
          
     return gen
     
def GetRandomTweetGenerator(bTest, bTweet, iGeneratorNo = 0, bAllowPromo = True, TweetHistoryQ = None):
    Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = bAllowPromo, TweetHistoryQ = TweetHistoryQ)

    Gen.Generate()

    Gen.AuthorName = AuthorBuilder()

    return Gen

def GetTweet(bTest, bTweet, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetHistoryQ = None, bAllowFavTweets = True, iMaxLen = 0):
    Gen = None
    sTweet = ""

    iLocMaxLen = 9999
    if iMaxLen > 0:
        iLocMaxLen = iMaxLen 

    #TGC = GeneratorContainer(TitleGen)
    
    while Gen is None or (len(Gen.ImgTxt) > iLocMaxLen):
        if not bTest and bAllowFavTweets:
            Gen = TitleGen()
            if not Gen.GetTitleFromFile(FAVTITLE_FILENAME):
                Gen = GetRandomTweetGenerator(bTest, bTweet, iGeneratorNo, bAllowPromo = bAllowPromo, TweetHistoryQ = TweetHistoryQ)
        else:
            Gen = GetRandomTweetGenerator(bTest, bTweet, iGeneratorNo, bAllowPromo = bAllowPromo, TweetHistoryQ = TweetHistoryQ)

    return Gen
     
class GeneratorPromo(TitleGen):
     def __init__(self):
        super().__init__(ID = 0, Priority = GenPriority.Lowest, Disabled = True, Type = GeneratorType.Promo)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          #sTweet = "Blue Diamond: \U0001F539 Eggplant: \U0001F346 Fire: \U0001F525 Laughing: \U0001F923 Robot: \U0001F916 Green Heart: \U0001F49A Blue Heart: \U0001F499 Purple Heart: \U0001F49C No one under 18: \U0001F51E Winking kiss face: \U0001F618 Star: \U00002B50"

          iRand = randint(1,7)
          while not PromoHistoryQ.PushToHistoryQ(iRand):
               iRand = randint(1,7)

          if iRand == 1:
               sTweet = "Reply to " + WordList(["one of my tweets", "an @bot_lust tweet", "a Flaming Lust Bot tweet"]).GetWord() + " for a fun surprise! " + GetEmoji()
               sTweet += "\n\n\U0001F539Reply \"#book\" and I'll respond with a made-up smutty book title."
               sTweet += "\n\U0001F539Reply \"#lovescene\" to get your own custom love scene!"
          elif iRand == 2:
               sTweet = "Tell your family, friends and lovers to follow " + WordList(["@bot_lust", "Flaming Lust Bot", "me", "this bot"]).GetWord() + " for all the steamy, sweaty, silly action!\n" + GetEmoji(randint(1,3))
          elif iRand == 3:
               sTweet = WordList(["@bot_lust", "Flaming Lust Bot", "this bot"]).GetWord() + " is very naughty, and NOT appropriate for anyone under 18! \U0001F51E\n\nThat includes you, " + WordList(["kid who is hiding their phone behind their math book while they check twitter", str(randint(6,11)) + "th grader who is supposed to be doing homework", str(randint(6,11)) + "th grader who is supposed to be reading"]).GetWord() + "!"
               if CoinFlip(): 
                    sTweet += " \U0001F928"
          elif iRand == 4:
               sTweet = "I am a twitter bot\U0001F916 designed to automatically generate " + WordList(["hot", "sexy", "naughty", "steamy"]).GetWord() + "\U0001F525, " + WordList(["filthy", "dirty"]).GetWord() + "\U0001F346, and " + WordList(["funny", "hilarious", "ridiculous", "silly"]).GetWord() + "\U0001F923 scenes from the world's worst smutty romance novel!\n\nReply to one of my tweets " + WordList(["and get a surprise!", "if you want more.", "if you're impatient for my next terrible love scene!"]).GetWord()
          elif iRand == 5:
               if CoinFlip():
                    sTweet = "Full disclosure: "
               sTweet += "I am a bot\U0001F916!\n\nBut not the Russian kind of bot, the " + WordList(["funny", "sexy", "naughty", "silly", "dirty"]).GetWord() + " kind of bot!" 
               if CoinFlip():
                    sTweet += " " + GetEmoji()
               if CoinFlip():
                    sTweet += "\n#botlife #twitterbot"
          elif iRand == 6:
               sTweet = "Look what " + WordList(["my followers are", "people are ", "other twitter users are", "the internet is"]).GetWord() + " saying:\n\n\U00002B50'I am hooked on this ridiculous account!'\n\U00002B50'The stuff this bot comes up with is hysterical. XD'\n\U00002B50'[S]imultaneously hilarious, nauseating, and inspiring'\n\n" + WordList(["Thank you!", "Thanks!", "Thank you all!", "Big bot love to everyone!"]).GetWord() 
               sTweet += " " + GetEmoji(randint(1,3))
          else:
               sTweet = WordList(["I love you", "You're the best", "Big Bot Love", "I \U00002764 you"]).GetWord() + ", followers!"
               if CoinFlip():
                    sTweet = "*" + sTweet + "*"
               sTweet += "\n\n" + GetHeartEmoji(randint(1,5))
               
          return sTweet
          
class Generator1(TitleGen):
     # Blackmailed by the Billionaire Mountain Man 
     def __init__(self):
         super().__init__(ID = 1, Priority = GenPriority.High)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian"]
          self.ReqTemplateTags = ["woman","man"]
          
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, MaxChars = 32,
                                 bSplitArticle = True, bAllowGang = True)
          
          sTweet = self.VerbsBy.GetWord() + "\nBy " + Master.Desc

          return sTweet
          
class Generator2(TitleGen):
    # Bedded
    # by the
    # Busty Trans Japanese Schoolgirl
    def __init__(self):
        super().__init__(ID = 2, Priority = GenPriority.High)
        self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
          
        self.ExclTemplateTags = ["gay","couple","women","lesbian"]
        #self.ReqTemplateTags = ["woman"]

        Verbs = WordList(["Ball-Gagged","Bedded","Blown","Cavity Searched","Chained to the Bed","Collared",
                        "Deep-Throated","Disciplined","Dominated","Dry-Humped",
                        "Fellated","Feminized","Gone Down On","Hand-cuffed","Horse-Whipped",
                        "Jerked Off","Licked","Smothered","Peed On","Pegged",
                        "Pegged with a Strap-on","Ridden","Rimmed","Seduced",
                        "Sixty-Nined","Straddled","Stroked","Spanked",
                        "Sucked Off","Swallowed","Teased","Tempted",
                        "Tied Up","Urinated On","Whipped"])

        Woman = char.FemaleChar(bAllowRelate = True, bAllowSexuality = False)

        sTweet = Verbs.GetWord() + "\n"
        if FoundIn(Woman.Desc, ["sister","brother","mom","dad","mother",
                                "father","fiancé","wife","girlfriend",
                                "teacher","secretary","daughter",
                                "babysitter","governess","tutor",
                                "bride","house maid","french maid"]):
            sTweet += "By\nMy " + Woman.Desc
        else:
            sTweet += "By\n" + AddArticles(Woman.Desc, bMakeUpper = True)
          
        return sTweet

class Generator3(TitleGen):
     # Married to the Alpha Wolf
     def __init__(self):
         super().__init__(ID = 3, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate1()
       
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian"]
          self.ReqTemplateTags = ["woman","man"]
          
          Master = char.MaleChar(TempType = TempType.Flowery, 
                                 bAddTheArticle = True, 
                                 sPosArticle = "Her", 
                                 bSplitArticle = True,
                                 bAllowGang = True, 
                                 bAllowRelate = True, 
                                 bAllowTrope = True)
               
          sTweet = self.VerbsTo.GetWord() + "\nTo " + Master.Desc

          #self.SetImgText(sTweet)

          return sTweet

class Generator4(TitleGen):
     # Veronica Gets Married to the Alpha Wolf     
     def __init__(self):
        super().__init__(ID = 4, Priority = GenPriority.Low, Disabled = True)

     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          #Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
          #Girl = char.FemaleChar(TempType = TempType.Flowery, bAddArticle = False, bAllowTrope = True)
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowGang = True, bAllowRelate = True, bAllowTrope = True)
          
          sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
          
          return sTweet
          
class Generator5(TitleGen):
    # Jackie Shows a Horny French Alpha Wolf her Cunning Stunt
    def __init__(self):
        super().__init__(ID = 5, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate3()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
        GenNotList = ["BDSM"]
        Girl = None
        Master = None

        self.ExclTemplateTags = ["gay","lesbian"]
        self.ReqTemplateTags = ["woman","man"]
               
        iMaxMasterChar = 50
        Master = char.MaleChar(TempType = TempType.Flowery, bAddAnArticle = True, 
                                sPosArticle = "Her",
                                bAllowRelate = True, bSplitArticle = False, 
                                NotList = GenNotList, MaxChars = iMaxMasterChar)

        sTweet = self.HerName + "\nShows\n" + Master.Desc + "\nHer\nCunning Stunt" 
          
        return sTweet
          
class Generator6(TitleGen):
     # Seduced in the Bed of the Billionaire     
     def __init__(self):
        super().__init__(ID = 6, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["bed","woman"]
          self.ExclTemplateTags = ["gay","lesbian"]
          
          NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", 
                     "Harrassed", "Sold", "Gifted", "Pledged", "Bed", 
                     "Sex Dungeon","Basement","Dungeon","Surrendered"]
          
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True,
                                 bAllowRelate = True, bAllowTrope = True)

          sTweet += self.VerbsBy.GetWord(NotList = NotList) + "\nIn the Bed of\n" + Master.Desc 
          
          return sTweet
          
class Generator7(TitleGen):
    # A Buff Tuxedoed Italian Dinosaur Took My Wife Hard From Behind!
    def __init__(self):
        super().__init__(ID = 7, Priority = GenPriority.AboveAverage)
        self.Template = templates.TitleTemplate4()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["gay","lesbian"]
        self.ReqTemplateTags = ["woman","man"]
        
        iMaxChars = 22
        sTag = "!"
        if CoinFlip():
            sTag = "\n"
            sTag += WordList(["And they let me watch", "And I watched",
                             "And I got to watch",
                             "And I video-taped the whole thing"]).GetWord()
            sTag += "!"
            #iMaxChars = 32

        Master = char.MaleChar(TempType = TempType.Flowery, MaxChars = iMaxChars,
                                    bAllowRelate = True, 
                                    bAllowTrope = True,
                                    bAddAnArticle = True, 
                                    bSplitArticle = False,
                                    sPosArticle = "My")

        Verbs = WordList(["Took","Claimed","Ravished","Mounted", "Plowed"])
          
        sTweet = Master.Desc  + "\n"
        sTweet += Verbs.GetWord() + " My Wife From Behind"
        sTweet += sTag

        return sTweet

class Generator8(TitleGen):
     # My Blind Date is A Uniformed Australian Mer-man Fighter Pilot! 
     def __init__(self):
         super().__init__(ID = 8, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian"]
          self.ReqTemplateTags = ["man"]
          
          NotList = ["Boyfriend", "Hot Date", "Fiancé", "Husband", "Single", "Ugly", "BDSM", "Comedian"]
          Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True,NotList = NotList,bAddAnArticle = True,
                                        ReqList = [ProfRockstarMale],
                                        ExclList = [DickCharMale,ProfBlueCollarMale,ProfAthleteMale,ProfWhiteCollarMale,MaritalStatusMale,AttitudeMale])

          sTweet = "My " + WordList(["New Boyfriend", "Hot Date", "New Fiancé", "Blind Date", "Kidnapper", "New Hubby", 
                                             "New Husband", "New Man","New Daddy", "New Boss", "New Teacher"]).GetWord() + " "
          sTweet += "is " + Master.Desc
          if CoinFlip():
               DickWords = WordList(["Boner","Cock","Dick","Penis","Schlong","Tool","Package","Erection"])
          
               sTweet += "\nand " + WordList(["He's Hung Like a Horse",
                                              "He Has a Massive " + DickWords.GetWord(),
                                              "He has a " + WordList(["Beautiful","Gorgeous"]).GetWord() + " " + DickWords.GetWord(),
                                              "His " + DickWords.GetWord() + " is ENORMOUS"]).GetWord()
          sTweet += "!"

          return sTweet
          
# Idea: a rhyming version of this generator
class Generator9(TitleGen):
     # The Secretary and the Space Werewolf  
     def __init__(self):
         super().__init__(ID = 9, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man", "woman"]
          
          NotList = ["BDSM"]
          Girl = char.FemaleChar(TempType = TempType.Medium, bAllowRelate = True, bAllowTrope = True, bAllowSpecies = False, bAllowTitle = False, NotList = NotList)
          Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True, bAddTheArticle = True, sPosArticle = "Her", bSplitArticle = True, NotList = NotList)
          
          sTweet = "The " + Girl.Desc + "\nAnd " + Master.Desc 
          if len(sTweet) > 60:
              sTweet += "\n" + AddArticles(WordList([self._getFMs_(), 
                                                                "BDSM", 
                                                                misc.SexyAdjs().GetWord().lower()]).GetWord(),
                                           bSplitArticle = True) + " " 
              sTweet += self.SubtitleCoda.GetWord().lower()
          
          return sTweet
          
class Generator10(TitleGen):
     # I'm Having a Baby for a Stay-at-Home Manticore!
     def __init__(self):
         super().__init__(ID = 10, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate15()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["couple", "straight"]

          ManNotList = ["naked","nude","hung","shirtless","bdsm",
                        "erect","pantsless","hard","masked","sex addict",
                        "girthy","bald","millennial","graying","eager",
                        "rebel","savage","wicked","husky","rangy",
                        "shape","stay-at-home","tabboo","college","teen",
                        "widowed","divorced","husband","family man"]
          Master = char.MaleChar(bAddAnArticle = True, sPosArticle = "My", 
                                 NotList = ManNotList,
                                 ExclList = [ProfBlueCollarMale,DickCharMale,
                                             ClothesMale,GenModMale])

          sTweet = "I'm Having A Baby For\n" + Master.Desc + "!"

          return sTweet
          
class Generator11(TitleGen):
     # Shaving
     # My Cute Black Cheerleader Step-Sister
     def __init__(self):
         super().__init__(ID = 11, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]

          Gerunds = self.Gerunds

          iTempNo = 0
          if CoinFlip():
          # Good female relation template
             iTempNo = 8
          else:
          # Bad female relation template
             iTempNo = 9

          FemNotList = ['Girlfriend', 'Wife', 'Mistress','Concubine']
          FemChar = char.FemaleChar(MaxChars = 28, SelectTemplateID = iTempNo,
                                    NotList = FemNotList)
          
          sTweet = Gerunds.GetWord() + "\nMy " + FemChar.Desc

          return sTweet
          
class Generator12(TitleGen):
     # Fingering Felicity
     # A Mommy Encounter
     def __init__(self):
         super().__init__(ID = 12, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay"]
          
          RelNotList = ["Wife","Girlfriend","Mistress","Concubine","Daughter's Best Friend"]
          Relations = titmisc.RelateFemale()
          Gerunds = self.Gerunds
          Names = NamesFemale()

          RhymingPair = GetRhymingPair(Gerunds.GetWordList(), Names.GetFirstNamesList())

          sTweet = RhymingPair[0] + " " + RhymingPair[1] + "\n" 
          sTweet += AddArticles(Relations.GetWord(NotList = RelNotList), bMakeUpper = True) + " " 
          sTweet += self.SubtitleCoda.GetWord()

          return sTweet
          
class Generator13(TitleGen):     
     # I Was a Bra-less Escort for a French Billionaire Uniporn
     def __init__(self):
         super().__init__(ID = 13, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay"]
          self.ReqTemplateTags = ["man"]
          
          GirlNotList = ["college girl","co-ed","mommy blogger","school-marm"]
          Girl = char.FemaleChar(TempType = TempType.Medium, Type = GirlType.Bad, 
                                 sPosArticle = "My", SelectTemplateID = 21,
                                 NotList = GirlNotList, bAllowNation = False)
          Master = char.MaleChar(bAddAnArticle = True, MaxChars = 28)
          
          sTweet = "I was " + AddArticles(Girl.Desc) + "\nfor\n" + Master.Desc

          return sTweet
     
# Note: this 'gang bang' generator has been split in two. See also
# gen 40
class Generator14(TitleGen):
    # The Virgin French Cheerleader
    # Has a Gang-Bang with
    # 30
    # Giant Well-Hung Sumo Wrestlers
    def __init__(self):
        super().__init__(ID = 14, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate16()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["lesbian","women","gay"]
          
        GangNot = ["Dapper","Gang-Bang","Brothers"]
          
        GirlShort = char.FemaleChar(Type = GirlType.Good, 
                                    TempType = TempType.Medium,
                                    bAddTheArticle = True, 
                                    bAllowSpecies = False)
        GirlLong = char.FemaleChar(Type = GirlType.Good, 
                                   TempType = TempType.Flowery, 
                                   bAddTheArticle = True, MaxChars = 24,
                                   bAllowSpecies = False)
        GangShort = char.GangMaleChar(TempType = TempType.Medium,
                                      bAllowClothing = False,
                                      NotList = GangNot)
        GangLong = char.GangMaleChar(TempType = TempType.Flowery,
                                         NotList = GangNot, MaxChars = 24,
                                         bAllowClothing = False)

        if CoinFlip():
            # short girl, long gang
            sTweet = GirlShort.Desc + "\n"
            if sTweet[0:2].lower() == "my":
                sTweet += "Had " 
            else:
                sTweet += "Has "
            sTweet += "a Gang-Bang with\n"
            sTweet += "The " + GangLong.Desc
        else:
            # long girl, short gang
            sTweet = GirlLong.Desc + "\n"
            if sTweet[0:2].lower() == "my":
                sTweet += "Had " 
            else:
                sTweet += "Has "
            sTweet += "a Gang-Bang with\n"
            sTweet += "The " + GangShort.Desc
          
        return sTweet
          
class Generator15(TitleGen):
    # The Small-Town Virgin's First Porno
    def __init__(self):
        super().__init__(ID = 15, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate7()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["gay","couple"]

        GirlNotList = ["little"]
          
        Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, 
                               MaxChars = 26, NotList = GirlNotList,
                               bAllowTitle = False)
          
        sTweet = Girl.Desc + "\n" + WordList(["Makes a Porno","Does Anal Porn!","Does Lesbian Porn!",
                                              "Does Gangbang Porn!","Does Inter-Racial Gangbang Porn!",
                                              "Becomes an Anal Porn Star!","Does Inter-Racial Porn!",
                                              "Does Animal Porn!", "Does Lesbian Anal Porn!",
                                              "Makes a Porno With Her Dad!"]).GetWord() 
        if "lesbian" in sTweet.lower():
            self.ExclTemplateTags.append("man")
            self.ExclTemplateTags.append("men")
        if "animal" in sTweet.lower():
            self.ReqTemplateTags = ["kinky"]

        return sTweet
          
class Generator16(TitleGen):
# "Oh No! I Went to an Orgy
# And I Accidentally
# Finger-Banged My Asian Step-Sister!"
     def __init__(self):
         super().__init__(ID = 16, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate8()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay"]
          
          Tweets = []
          
          RelNotList = ['Wife', 'Girlfriend', 'Fiancé','Concubine','Mistress',
                        'BDSM','little']

          Verbs = WordList(["Boned","Banged","Humped","Had Sex With","Went Down On","Sixty-Nined","Ate Out",
                            "Had Anal Sex With","Boinked","Jizzed On","Finger-Banged","Fisted","Did"])

          StepMom = char.FemaleChar(TempType = TempType.Medium, SelectTemplateID = 7, 
                                    NotList = RelNotList, 
                                    ExclList = [SpeciesFemale])
          
          sTweet += "\"Oh No! I Went to " + WordList(["an Orgy","a Swinger's Party","a Wild Sex Party"]).GetWord() + " "
          if randint(1,8) == 1:
               sTweet += "And I Accidentally Ate My " + StepMom.Desc + "'s Ass!\""
          else:
               sTweet += "And I Accidentally " + Verbs.GetWord() + " " 
               sTweet += "My " + StepMom.Desc + "!\""
          return sTweet
          
class Generator17(TitleGen):
     # Enslaved: The Ebony Older Woman & The Mountain Man Biker Gang 
     def __init__(self):
         super().__init__(ID = 17, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate17()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","lesbian","women"]
          
          GirlNotList = ["Recently-Divorced","Sassy","Tanned","Kitten","Harem","Ice Queen","MILF"]
          Subtitles = []

          self.ExclTemplateTags = ["gay"]
          self.ReqTemplateTags = ["woman"]
          
          Master = char.MaleChar(TempType = TempType.Medium,)
          Gang = char.GangMaleChar(TempType = TempType.Medium)
          
          VerbNotList = ['Taken']
          sTweet = self.VerbsBy.GetWord(NotList = VerbNotList) + "\n"
          
          Girl = char.FemaleChar(Type = GirlType.Good, NotList = GirlNotList, 
                                 TempType = TempType.Medium,
                                 bAllowSpecies = False, bAllowTitle = False)

          Subtitles.append("The " + Girl.Desc + "\nand the\n" + Gang.Desc)
          Subtitles.append("The " + Girl.Desc + "\nand the\n" + Master.Desc)
          #Subtitles.append(AddArticles(Girl.Desc) + " " + WordList(['Adventure','Encounter','Liason','Experience','Episode','Rendezvous']).GetWord())
          
          sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
          
          return sTweet
          
class Generator18(TitleGen):
     # Oh No! My Step-Daughter is a Porn Star
     def __init__(self):
         super().__init__(ID = 18, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ["Sex", "Lesbian","BDSM","Tanned","Recently-Divorced","Sassy","Tanned",
                              "Kitten","Harem","Ice Queen","MILF","Nude","Lactating","Lonely","Bare"]
          Girl = char.FemaleChar(Type = GirlType.Good, NotList = GirlNotList, bAddEndNoun = False, bAllowMaritalStatus = False, bAllowSpecies = False, bAllowTitle = False)
          
          sTweet += "\"" + WordList(["S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"]).GetWord() + "\n" 
          sTweet += "My " + Girl.Desc + " " + WordList(["Girlfriend", "Bride", "Wife", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Step-Sister", "Twin Sister", "Mom", "Wife"]).GetWord() + "\n"
          sTweet += "Is " + WordList(["A Porn Star", "A Lesbian", "A Call-Girl", "A Stripper", "A Whore", "A Dominatrix", "An Anal Whore", 
                                             "An Anal Porn Star", "An Erotic Model", "A Kinky Fetish Model", "A Slut", "A Butt Slut", "A High-Class Hooker",
                                             "A Slutty Bikini Model", "A Wanton Slut", "An Erotica Author"]).GetWord() + "!\""
          
          return sTweet
          
class Generator19(TitleGen):
      # My Daughter's Best Friend is a Busty Virgin Nurse
      # And I Got Her to Pee on Me!
      def __init__(self):
         super().__init__(ID = 19, Priority = GenPriority.Low, Disabled = True)
     
      def GenerateTweet(self):
           super().GenerateTweet()
           sTweet = ""
          
           Verbs = WordList(["Anally Deflowered Her","Ate Her Out","Banged Her","Boned Her","Deflowered Her",
                             "Dry-Humped Her","Fisted Her","Knocked Her Up","Motor-Boated Her Titties",
                             "Mounted Her Bare-back","Rode Her Hard","Took Her From Behind",
                             "Rimmed Her","Spanked Her With a Belt","Popped Her Cherry","Tea-Bagged Her",
                             "Whipped Her With A Leather Riding Crop","Showered Naked With Her",
                             "Sixty-Nined Her","Ate Her Ass","Finger-Banged Her","Put a Finger in Her Ass",
                             "Let Her Pee On Me","Showed Her My Junk","Got Her Pregnant","Made Her Squirt",
                             "Got a Lap Dance from her at the Strip Club"])
           FriendNotList = ["best","friend","mom","MILF","mature","housewife","nude","nudist","naked",
                            "x-rated","escort","call-girl","whore"]
           Girl = char.FemaleChar(NotList = FriendNotList, 
                                  bAllowTrope = False, bAllowRelate = False, bAllowTitle = False, bAllowSpecies = False,
                                  ExclList = [AgeAdjFemale,MaritalStatusFemale,PregState,SpeciesFemale,
                                              RelateFemale,TitlesFemale,AgeNounFemale])
          
           sTweet += "My Daughter's Best Friend\nis " + AddArticles(Girl.Desc) + "\nand\n"
           sTweet += "I " + Verbs.GetWord()
           return sTweet
          
# NOTE: Similar to Generator 138 (spooky version)
class Generator20(TitleGen):
    # I Was Stripped In Public, And I Liked It
    def __init__(self):
        super().__init__(ID = 20, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate7()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["lesbian"]

        sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
        sTweet = "I Was " + sVerbBy
        sTweet += " By "
        if CoinFlip():
        # single man
            Master = char.MaleChar(bAllowGang = False, bAddAnArticle = True, 
                                    MaxChars = 20,
                                    bAllowRelate = True)
            sTweet += Master.Desc
            self.ExclTemplateTags = ["women","lesbian"]
        else:
        # gang bang
            GangNotList = ["S.W.A.T.", "Millennial"]
            GangExclList = [AttitudeMale, GenModMale, TypeModMale, 
                            SkinHairColorMale, AgeAdjMale]
            if CoinFlip():
                Gang = char.GangMaleChar(bAddAnArticle = False, MaxChars = 20,
                                         MaleCharType = MaleCharType.GangPlural,
                                         ExclList = GangExclList, NotList = GangNotList)
                sTweet += "The " + Gang.Desc
            else:
                Gang = char.GangMaleChar(bAddAnArticle = True, MaxChars = 20,
                                         MaleCharType = MaleCharType.GangSingular,
                                         ExclList = GangExclList, NotList = GangNotList)
                sTweet += Gang.Desc
            
            self.ExclTemplateTags = ["women","lesbian","couple"] 
        sTweet += "\nAnd I Liked It!"

        return sTweet
          
class Generator21(TitleGen):
     # Pleasured by the Shape-Shifting Single Dad
     def __init__(self):
         super().__init__(ID = 21, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man"] 
          self.ExclTemplateTags = ["lesbian", "women"] 
          
          Master = char.MaleChar(bAddAnArticle = True, bSplitArticle = True,
                                 sPosArticle = "His", MaxChars = 30,
                                 bAllowRelate = True)
          
          sTweet = self.VerbsBy.GetWord()  + "\nBy "
          sTweet += Master.Desc 
          
          return sTweet
          
class Generator22(TitleGen):
    # The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
    def __init__(self):
        super().__init__(ID = 22, Priority = GenPriority.AboveAverage)
        self.Template = templates.TitleTemplate2()

        self.ExclTemplateTags = ["gay", "straight", "man", "men"] 
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
          
        GirlGood = char.FemaleChar(MaxChars = 22, Type = GirlType.Good, 
                                   ExclList = [SpeciesFemale,SexualityFemale])
         
        GirlLes = char.LesbianChar(MaxChars = 28, NotList = ["nude","naked","nudist"] + GirlGood.GetWordList())
        sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlLes.Desc
        
        if CoinFlip() and CoinFlip():
            sTweet += "\n" + WordList(["A Lesbian","A Secret Lesbian","A Taboo Lesbian","A Forbidden","An FF",]).GetWord() + " " + self.SubtitleCoda.GetWord()
          
        return sTweet
          
# NOTE: part of this was split off to generator 44
class Generator23(TitleGen):
     # The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
     def __init__(self):
         super().__init__(ID = 23, Priority = GenPriority.High)
         self.Template = templates.TitleTemplate2()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian", "straight", "women", "woman"] 
          
          sHisName = PlainNamesMale().FirstName()

          StraightNotList = ["BDSM","taboo"]
          
          StraightGuy = char.MaleChar(TempType = TempType.Medium, 
                                      bAllowGang = False, SelectTemplateID = 9,
                                      ExclList = [DickCharMale, SpeciesMale, GenModMale, AttitudeMale],
                                      NotList = StraightNotList)
          GayGuy = char.GayMaleChar(MaxChars = 24, ReqList = [GayMaleAdj])
          
          sTweet = "The " + StraightGuy.Desc + "\nand\nThe " + GayGuy.Desc
          #sTweet += ":\n" + WordList(["A Gay","A Secret Gay","A Taboo","A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator24(TitleGen):
     # Deep-Throating My Well-Hung Sumo-Wrestler Step-Dad
     def __init__(self):
         super().__init__(ID = 24, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate16()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          self.ExclTemplateTags = ["lesbian", "straight", "women"] 
          
          Gerunds = WordList(['Bedding','Cuddling','Deep-Throating','Double-Teaming','Dry-Humping','Fellating','Going Down on',
                                   'Hooking Up With','Humping','Jerking Off','Licking','Pegging','Riding','Rimming','Shagging',
                                   'Showering With','Sixty-Nining','Sleeping With','Spooning','Straddling','Teasing'])
          Verbs = WordList(['Beds','Cuddles','Deep-Throats','Double-Teams','Dry-Humps','Fellates','Goes Down on',
                                   'Hooks Up With','Humps','Jerks Off','Licks','Mounts','Pegs','Rides','Rims','Shags',
                                   'Showers With','Sixty-Nines','Sleeps With','Spoons','Straddles','Teases'])
          Master = char.MaleChar(bAddAnArticle = True, bAllowRelate = True, sPosArticle = "His")
     
          sTweet = self.HisName + "\n" 
          sTweet += Verbs.GetWord() + "\n" 
          sTweet += Master.Desc
          
          return sTweet
          
class Generator25(TitleGen):
    # Pounded In The Butt By The Motorcycle Gang
    def __init__(self):
        super().__init__(ID = 25, Priority = GenPriority.High)
        self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["lesbian", "straight", "women", "woman"] 
          
        GayNotList = ['anal']
        GayGuy = char.MaleChar(bAddTheArticle = True, sPosArticle = "His",
                               SelectTemplateID = 17,
                               MaxChars = 20,NotList = GayNotList)
        GayGang = char.GangMaleChar(MaxChars = 20, TempType = TempType.Medium,
                                    ExclList = [AttitudeMale])

        if CoinFlip():
        # Gang
            sTweet = "Pounded In The Butt\nBy\nThe " + GayGang.Desc
        else:
            sTweet = "Pounded In The Butt\nBy\n" + GayGuy.Desc
        #GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By\n" + GayGuy.Desc)
        #GayTitles.append(sHisName + " and\n" + GayGuy.Desc)
          
        return sTweet
          
class Generator26(TitleGen):
    # Hotwife for Daddy: A BDSM Romance 
    def __init__(self):
        super().__init__(ID = 26, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate12()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["gay","men"]
        self.ReqTemplateTags = ["woman"]
          
        Girl = char.FemaleChar(TempType = TempType.Medium,
                                ExclList = [PregState,SexualityFemale])
        TabooWord = WordList(["A BDSM","An " + self._getFMs_(), "A Taboo", "A Forbidden", 
                                    "A Forbidden", "A Naughty"]).GetWord()
        SexActs = WordList(["anal", "double anal", "fisting","anal fisting","nipple play", "incest", "twincest",
                                "cum-swapping","bukkake","pee-drinking","hot-wifing","erotic asphyxiation",
                                "double penetration","triple penetration","B.D.S.M.","lactation","age play",
                                "edging","forced orgasm","deep-throating","choke play","extreme penetration",
                                "leather bondage","tea-bagging","full-frontal massage","enema","adulterous",
                                "pegging","butt stuff","sodomy","premarital sex","spanking","paddling"])
          
        sTweet = Girl.Desc + " For Daddy\n"
        sTweet += AddArticles(SexActs.GetWord()).title() + " "
        sTweet += self.SubtitleCoda.GetWord()
          
        return sTweet
          
class Generator27(TitleGen):
    # The Shy Lesbian Gymnast Wore Black
    def __init__(self):
        super().__init__(ID = 27, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate7()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["gay","men"]
        self.ReqTemplateTags = ["woman"]
          
        GirlNotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"]
        Girl = char.FemaleChar(NotList = GirlNotList, Type = GirlType.Good, bAddTheArticle = True, 
                                    bAllowRelate = True, bAllowSpecies = False, bAllowAttitude = False)
        Wearables = WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "a Strap-On",
                                    "a Chastity Belt","a Nose Hook", "a Butt Plug", "a Ponytail Butt Plug",
                                    "a Clit Clamp","a Ball Gag","a Steel Collar","an Anal Hook","Nipple Clamps",
                                    "a Spreader Bar","a Spiked Metal Bra","Assless Chaps"])
          
        sTweet = Girl.Desc 
        if "my" in sTweet.lower():
            sTweet += "\nIs Wearing "
        else:
            sTweet += "\nWore "
        sTweet += Wearables.GetWord() 

        return sTweet

class Generator28(TitleGen):
     #Cuckolded By My Amish Maiden Hotwife
     def __init__(self):
         super().__init__(ID = 28, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(bAddEndNoun = False, 
                                 bAllowMaritalStatus = False, 
                                 bAllowSexuality = False, 
                                 NotList = ['Single', 'Divorced'])
          Man = char.MaleChar(bAddTheArticle = True, bAllowMaritalStatus = False)
          FemaleRelate = WordList(['Wife', 'Wife', 'Fiancé', 'Girlfriend'])
          if CoinFlip():
               sTweet = "Cuckolded By My\n" + Girl.Desc + " " + FemaleRelate.GetWord()
          else:
               sTweet = "My " + FemaleRelate.GetWord() + " "
               sTweet += "And\n" + Man.Desc + ":\nA " + WordList(["Cuckold","Hotwife"]).GetWord() + " "
               sTweet += self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator29(TitleGen):
     # Blackmailing My Step-Dad's Busty Ballerina
     def __init__(self):
         super().__init__(ID = 29, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ["Girlfriend", "Mom", "Dad", "Sister", "Divorced", "Single", "Hotwife", "Virgin", 
                              "Pastor's Wife", "Housewife", "Lesbian", "Bridesmaid", "Nun"]
          Girl = char.FemaleChar(bAddEndNoun = False, bAllowMaritalStatus = False, bAllowTitle = False, NotList = GirlNotList, bAllowSexuality = False)
          
          iRand = randint(1,4)
          sTweet = self.Gerunds.GetWord() + " "
          if iRand == 1:
               sTweet += "My " + WordList(["Father's", "Dad's", "Step-Dad's"]).GetWord() + "\n"
               sTweet += Girl.Desc + " " + WordList(["Wife", "Girlfriend", "Fiancé", "Hotwife", "Bride"]).GetWord()
          elif iRand == 2:
               sTweet += "My " + WordList(["Son's", "Step-Son's"]).GetWord() + "\n"
               sTweet += Girl.Desc + " " + WordList(["Wife", "Wife", "Girlfriend", "Fiancé", "Hotwife", "Bride"]).GetWord()
          elif iRand == 3:
               sTweet += "My " + WordList(["Best Friend's", "Neighbor's", "Boss's"]).GetWord() + "\n"
               sTweet += Girl.Desc + " " + WordList(["Bride", "Wife", "Wife", "Girlfriend", "Fiancé", "Daughter", "Step-Daughter", "Sister", "Hotwife", "Mom", "Step-Mom"]).GetWord()
          else: 
               sTweet += "My " + WordList(["Sister's","Step-Sister's","Mom's","Step-Mom's","Daughter's","Step-Daughter's"]).GetWord() + "\n"
               sTweet += "Lesbian " + Girl.Desc + " " + WordList(["Wife", "Girlfriend"]).GetWord()
          
          return sTweet
          
class Generator30(TitleGen):
     # Bubbly & Plump: 
     # The Chaste Small-Town Girl Barista 
     # Rides a Veiny 9-inch Dick
     def __init__(self):
         super().__init__(ID = 30, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate14()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["lesbian"]
          
          NotGirlList = ["School-Marm"]
          AdjNotList = ["Bikini-Bod","Anal Virgin","Shave","Big-Titty",
                        "Little","Divorced","Soft-Hearted","Bottomed",
                        "Tight-Bodied","Thick","Ample","School-Marm"]
          
          PhysChars = titmisc.PhysCharFemale()

          sAdj1 = titmisc.AttitudeGoodFemale().GetWord(NotList = AdjNotList)
          sAdj2 = PhysChars.GetWord(NotList = AdjNotList + [sAdj1])
               
          NotGirlList = NotGirlList + [sAdj1,sAdj2]
          Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True,
                                 SelectTemplateID = 23, MaxChars = 20) 
          
          sTweet = sAdj1 + " & " + sAdj2 + "\n"
          sTweet += Girl.Desc + " "
               
          sCoda = ""
          iRand = randint(1,15)
          if iRand < 3:
               sCoda += "Exposes Her Naked Body " + WordList(["in a Wal-Mart","on Main Street","at the Grocery Store",
                                                "at Disneyland","on the Jumbotron"]).GetWord()
          elif iRand == 3:
               sCoda += "Has Her First " + WordList(["Threesome","Three-Way","Orgy"]).GetWord()
          elif iRand == 4:
               sCoda += "Has a " + WordList(["4","5","6","8","10","12","20","30","60"]).GetWord() + "-guy Gangbang"
          elif iRand == 5:
               sCoda += "Gets Her Cherry Popped"
          elif iRand == 6:
               sCoda += "Gets Her Anal Cherry Popped"
          elif iRand == 7:
               sCoda += "Goes Down On " + WordList(["a Butch Lesbian","Another Woman","Her Best Friend","Her Lesbian Boss",
                                                              "Her Maid of Honor","Her Bridesmaid","Her Mother-in-Law"]).GetWord()
          elif iRand == 8:
               sCoda += "Makes a Porno"
          elif iRand == 9:
               sCoda += "Tries Anal"
          elif iRand == 10:
               sCoda += "Wears a Butt Plug"
          elif iRand == 11:
               sCoda += "Tries a Glory Hole"
          elif iRand == 12:
               sCoda += "Pounds " + NamesMale().FirstName() + " with a Strap-On"
          else:
               ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
                                "Throbbing","Meaty","Burning","Dripping","Lustful","Passionate","Massive","Fat",
                                "Throbbing","Pulsating","Dripping","Black","Stiff","Girthy"])
               sCoda += WordList(["Rides","Sucks","Mounts","Takes"]).GetWord() + " "
               sCoda += AddArticles(ErectAdjs.GetWord()) + " " 
               sCoda += WordList(["Seven","Seven 1/2","Eight","Eight 1/2","Nine","Nine 1/2","Ten","Ten 1/2",
                                        "Eleven","Eleven 1/2","Twelve","Thirteen","Fourteen"]).GetWord() + "-inch "
               sCoda += WordList(["Dick","Cock","Boner","Prick","Tool"]).GetWord()
               
          sTweet += sCoda

          return sTweet
          
# NOTE: Has some issues
class Generator31(TitleGen):
     # Wanton & Willing: 
     # My Kinky Lesbian Leather-Clad Dominatrix
     # Pegs Me With a Strap-On
     def __init__(self):
         super().__init__(ID = 31, Priority = GenPriority.Lowest, Disabled = True)
         self.Template = templates.TitleTemplate14()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotGirlList = ["Harem Princess"]
          Girl = char.FemaleChar(Type = GirlType.Bad, MaxChars = 18,
                                 NotList = NotGirlList, 
                                 bAllowSpecies = False)

          sAdj1 = ""
          sAdj2 = ""
          if CoinFlip():
               sAdj1 = titmisc.PhysCharFemale().GetWord()
               sAdj2 = titmisc.AttitudeBadFemale().GetWord()
          else:
               sAdj1 = titmisc.AttitudeBadFemale().GetWord()
               sAdj2 = titmisc.PhysCharFemale().GetWord()
               
          sHerName = NamesFemale().FirstName()
          
          sTweet = sAdj1 + " & " + sAdj2 + "\n"
          
          if CoinFlip():
               sTweet += "My " + Girl.Desc + " "
          else:
               sTweet += sHerName + " the " + Girl.Desc + " "
               
          iRand = randint(1,13)
          if iRand < 3:
               ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
                                "Throbbing","Meaty","Burning","Dripping","Purple","Red","Fleshy","Lustful","Passionate",
                                "Throbbing","Pulsating","Vigorous","Virile","Moist","Black","Stiff","Girthy"])
               sTweet += "Gets a " + ErectAdjs.GetWord() + " " + str(randint(7,12)) + "\" Surprise"
          elif iRand == 3:
               sTweet += "Gets Her " + WordList(["Nipples","Clit","Labia","Taint","Ass Dimples"]).GetWord() + " Pierced"
          elif iRand == 4:
               Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
               "at the Chic-fil-a","in the Ball Pit","at the Park","at the Beach","Under an Overpass","at the Gym",
               "on the Eliptical Machine at the Gym","at the Seafood Restaurant","at the Museum","at Burger King",
               "at the Library","at the Farmer's Market","next to the Duck Pond","at Church","at the Bar",
               "in the Window Display of a Shoe Store","at Wal-Mart","at Starbucks","at School","on Campus",
               "in the Church Graveyard","at a Construction Site","at Rush Hour Traffic","at Her Uber Driver",
               "on a Hotel Balcony","Beside the Bike Path","at the Mail Man","at the Amazon Delivery Guy",
               "Behind the Bleachers","In the Back of a Ford 150","In a Movie Theater","at Chipotle","at Barnes & Noble",
               "at Whole Foods","at the Mall","at the CVS"
               ])
               sTweet += "Flashes Her " + WordList(["Tits","Ass","Pussy"]).GetWord() + " " + Places.GetWord()
          elif iRand == 5:
               sTweet += "Has Her First " + WordList(["Threesome","Foursome","Fivesome","Orgy","Gang Bang","Black Gang Bang"]).GetWord()
          elif iRand == 6:
               sTweet += "Has a " + WordList(["Dick","Cock","Penis","Prick"]).GetWord()
          elif iRand == 7:
               sTweet += "Tries a Glory Hole"
          elif iRand == 8:
               sTweet += "Gets " + WordList(["Fisted","Fisted","Anal Fisted"]).GetWord()
          elif iRand > 9 and iRand < 12:
               sTweet += WordList(["Wants","Craves","Is Horny for","Begs for"]).GetWord() + " " 
               sTweet += WordList(["Her Neighbor's","Her Step-Brother's","Her Professor's","Her Teacher's","Her Boss's",
                                        "Her Step-Dad's","Her Uncle's","Her Gym Coach's","Her Gynecologist's","A Stranger's"]).GetWord() + " "
               sTweet += WordList(["Dick","D","Cock","Hard Cock","Fat Dick","Dingus","Meat Stick","Flesh Pole","Fat Boner"]).GetWord()
          else: 
               sTweet += "Is Wearing " + WordList(["a Butt Plug","an Anal Hook","Nipple Clamps","a Ball Gag","a Clit Clamp",
                                                            "Crotchless Panties","a Strap-On","a Remote-Controlled Vibrator",
                                                            "Anal Beads"]).GetWord()
          return sTweet
          
class Generator32(TitleGen):
     # Stripping 
     # For My Best Friend's 
     # Cocky Coal-Miner Brother 
    def __init__(self):
        super().__init__(ID = 32, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate9()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
        
        if CoinFlip():
            self.ReqTemplateTags = ["man"]
            MaleNotList = ['Single', 'Man', 'Dad', 'Father', 'Brother', 'Son']
            Master = char.MaleChar(bAllowGang = False, NotList = MaleNotList, 
                                   TempType = TempType.Medium,
                                   bAllowMaritalStatus = False)
            if Master.Desc[-3:] == "Man":
                sMaster = Master.Desc[0:-4]
            else:
                sMaster = Master.Desc

            sTweet = WordList(["Sleeping With", "Hooking Up With", 
                                "Tempting", "Seducing", "Bedding", 
                                "Stripping For", "Secretly Watching", 
                                "Showering With", "Spying On", 
                                "Sharing", "Playing With", 
                                "Claimed By", "Taken By", 
                                "Deflowered By", "Dominated By", 
                                "Blackmailed By", "Stripped By", 
                                "Tied to the Bed By", 
                                "Pleasured By", "Spanked By", 
                                "Ravished By", "Taken Hard By", 
                                "Massaged By", "Going Down On", 
                                "Impregnated By"]).GetWord() + "\n"
            if CoinFlip():
                sTweet += "My " + WordList(["Best Friend", "Daughter", "Sister", "Step-Sister", "Step-Daughter"]).GetWord() + "'s\n"
                sTweet += sMaster + " " + WordList(["Boyfriend", "Fiancé", "Husband", "Hubby"]).GetWord()
            elif CoinFlip():
                sTweet += "My " + WordList(["Best Friend", "Step-Mom", "Mom", "Mother"]).GetWord() + "'s\n"
                sTweet += sMaster + " " + WordList(["Brother", "Boyfriend", "Boyfriend", "Step-Brother"]).GetWord()
            else:     
                sTweet += "My Best Friend's\n"
                sTweet += sMaster + " " + WordList(["Son", "Brother", "Boyfriend", "Fiancé", "Husband", "Dad", "Father", "Hubby", "Step-Dad"]).GetWord()
        else:
            self.ReqTemplateTags = ["woman"]
            FemNotList = NotList = ['Single','Virgin', 'Girl', 'Woman', 'Mom', 'Sister', 'Mother', 'Daughter', 'Lesbian', 'Maiden', 'Wife']
            Girl = char.FemaleChar(TempType = TempType.Medium, NotList = FemNotList,
                                   bAllowMaritalStatus = False, bAllowTitle = False)
            if Girl.Desc[-4:] == "Girl":
                sGirl = Girl.Desc[0:-5]
            elif Girl.Desc[-5:] == "Woman":
                sGirl = Girl.Desc[0:-6]
            else:
                sGirl = Girl.Desc
            sTweet = WordList(["Sleeping With", "Seducing", "Massaging", "Bedding", "Undressing", "Secretly Watching", "Spying On", "Sharing", "Showering With", "Stripping", "Playing With", "Claiming", "Spanking", "Punishing", "Deflowering", "Going Down On", "Blackmailing", "Pleasuring", "Impregnating"]).GetWord() + "\n"
            if CoinFlip():
                sTweet += "My " + WordList(["Best Friend", "Brother", "Step-Brother", "Step-Son", "Son"]).GetWord() + "'s\n"
                sTweet += sGirl + " " + WordList(["Girlfriend", "Fiancé", "Wife"]).GetWord()
            elif CoinFlip():
                sTweet += "My " + WordList(["Best Friend", "Father", "Dad", "Step-Dad"]).GetWord() + "'s\n"
                sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Girlfriend", "Step-Sister"]).GetWord()
            else:
                sTweet += "My Best Friend's\n"
                sTweet += sGirl + " " + WordList(["Sister", "Girlfriend", "Step-Sister", "Daughter", "Step-Daughter", "Fiancé", "Wife", "Step-Mom", "Mom", "Mother"]).GetWord()
               
        return sTweet
          
# Let's make this a consonant rhyme
class Generator33(TitleGen):
     #Milking Marie: A Pan-sexual Cheerleader Affair
     def __init__(self):
         super().__init__(ID = 33, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate14()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          
          sVerb = self.Gerunds.GetWord()
          
          Girl = char.FemaleChar(MaxChars = 24)
          sTweet = sVerb + " " + self.HerName + "\n"
          sTweet += AddArticles(Girl.Desc) + " " + self.SubtitleCoda.GetWord()

          return sTweet
          
# Rimming the Uptight Librarian Futa
# and her Mom
class Generator34(TitleGen):
     def __init__(self):
         super().__init__(ID = 34, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate14()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          
          sVerb = self.Gerunds.GetWord()
          
          Girl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium, bAddTheArticle = True,
                                        bAllowPregState = False)
          sTweet = sVerb + "\n" + Girl.Desc           
          sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 
                                                       'Twin Sister', 'Best Friend', 'Lesbian Lover', 'Mom']).GetWord()
          sTweet += "!"

          return sTweet
          
class Generator35(TitleGen):
     # Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
     def __init__(self):
         super().__init__(ID = 35, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sVerb = WordList(['Bedding',
               'Bending Over For',
               'Cuckolding',
               'Deep-Throating',
               'Dominating',
               'Fellating',
               'Gagging On',
               'Going Down On',
               'Massaging',
               'Pegging',
               'Playing With',
               'Pleasing',
               'Riding',
               'Rimming',
               'Seducing',
               'Showering With',
               'Straddling',
               'Stroking',
               'Stripping For',
               'Submitting To',
               'Swallowing',
               'Tempting',
               'Touching Myself For',
               'Twerking For',
               'Whipping']).GetWord()
          
          Master = char.MaleChar(bAddAnArticle = True, bAllowGang = False, bAllowTrope = False)
          sTweet = sVerb + " Mr. " + RegularLastNames().GetWord() + ":\n"
          sTweet += "My " + self.SubtitleCoda.GetWord(NotList = ['Story']) + " With\n" + Master.Desc

          return sTweet
          
class Generator36(TitleGen):
     # Turned Gay
     # by
     # The Strong Vegan Back-Door Bandit
     def __init__(self):
         super().__init__(ID = 36, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          if CoinFlip():
               self.ExclTemplateTags = ["man","men","straight"]
               Girl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium,
                                      ExclList = [SpeciesMale])
               
               if CoinFlip():
                    Lesbian = char.LesbianChar(bAddTheArticle = True, MaxChars = 28,
                                              NotList = ['wife','girlfriend', 'married','lesbo'],
                                              ExclList = [SpeciesFemale])
                    sTweet = "Turned Lesbo\nby\n" + Lesbian.Desc
               else:
                    Lesbian = char.LesbianChar(MaxChars = 28,
                                               NotList = ['wife','girlfriend', 'married', 'lesbian'],
                                               ExclList = [SpeciesFemale])
                    sTweet = "Straight " + Girl.Desc + "\nfor\nthe Lesbian " + Lesbian.Desc 
               
          else:
               self.ExclTemplateTags = ["woman","women","straight"]
               Man = char.MaleChar(bAllowGang = False, TempType = TempType.Medium,
                                   ExclList = [SpeciesFemale])
               
               if CoinFlip():
                    Gay = char.GayMaleChar(bAddTheArticle = True, MaxChars = 28,
                                           NotList = ['husband','boyfriend', 'married','gay'])
                    sTweet = "Turned Gay\nby\n" + Gay.Desc
               else:
                    Gay = char.GayMaleChar(MaxChars = 28, 
                                           NotList = ['husband','boyfriend', 'married', 'gay'])
                    sTweet = "Straight " + Man.Desc + "\nfor\nthe Gay " + Gay.Desc 

          return sTweet

# My New Step-Dad Is
# A Tattooed Hard-Drinking Vegan Trillionaire
# and He's Hung Like a Horse!          
class Generator37(TitleGen):
     def __init__(self):
         super().__init__(ID = 37, Priority = GenPriority.AboveAverage)
         self.Template = templates.TitleTemplate3()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man"]
          
          NotList = ['Husband', 'Boyfriend', 'Hubby', 'Widower', 'Fiancé','Erect','Hard']
          Relations = titmisc.RelateMale()
          DickWords = WordList(["Boner","Cock","Dick","Penis","Schlong","Tool","Package","Erection"])
          Gerunds = self.Gerunds
          Dad = char.MaleChar(bAddEndNoun = True, MaxChars = 35, bAllowGang = False, 
                              NotList = NotList, 
                              ExclList = [MaritalStatusMale, RelateMale, AgeAdjMale, DickCharMale])
          
          sTweet += "My New " + Relations.GetWord(NotList = NotList) + "\nIs\n" + AddArticles(Dad.Desc, bMakeUpper = True)
          if CoinFlip():
               sTweet += "\nand\n" + WordList(["He's Hung Like a Horse",
                                               "He Has a Massive " + DickWords.GetWord(),
                                               "He Has a Foot-long " + DickWords.GetWord(),
                                               "His " + DickWords.GetWord() + " is ENORMOUS"]).GetWord()
          sTweet += "!"

          return sTweet
          
class Generator38(TitleGen):
     # My New Step-Dad Is A Visibly-Erect Centaur
     def __init__(self):
         super().__init__(ID = 38, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Tweets = []
          
          NotList = ['Husband', 'Boyfriend', 'Hubby', 'Widower', 'Fiancé','Shape-Shifting']
          Relations = titmisc.RelateMale()
          VerbsBy = WordList(["I'm In Love With", "I Have A Crush On", "I Slept With", "I'm Being Blackmailed By", 
                                   "I'm Horny For", "I'm Turned On By","I Showered Naked With",
                                   "I Did a Strip-Tease For","I French-Kissed", "I Sexted"])
          Dad = char.MaleChar(SelectTemplateID = 10, bAllowGang = False, NotList = NotList, bAllowRelate = True)
          
          sTweet += "\"Oh No! " + VerbsBy.GetWord() + " "
          sTweet += "My " + Dad.Desc + "!\""

          return sTweet
          
class Generator39(TitleGen):
     # Taken Hard By My Big Black Biker 
     def __init__(self):
         super().__init__(ID = 39, Priority = GenPriority.Low, Disabled = True)
         #self.Template = templates.TitleTemplate3()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Tweets = []
          NotList = ["Big", "Black", "BBC", "Cock"]
          BBCNoNoun = char.MaleChar(bAddEndNoun = False, TempType = TempType.Flowery, NotList = NotList, 
                                             bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False, 
                                             bAllowSpecies = False, bAllowDickChar = False)
          BBCNoun = char.MaleChar(TempType = TempType.Short, NotList = NotList, 
                                             bAllowAge = False, bAllowNation = False, bAllowSkinHairColor = False, 
                                             bAllowSpecies = False, bAllowDickChar = False)
          InnocentGirl = char.FemaleChar(Type = GirlType.Good, NotList = ["Black", "Ebony"], bAllowSpecies = False)
          
          Tweets.append(self.VerbsBy.GetWord() + " by the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append(self.VerbsTo.GetWord() + " to the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append(self.HerName + " Gets " + self.VerbsBy.GetWord() + "\nby the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append(self.HerName + " Gets " + self.VerbsTo.GetWord() + "\nto the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append(self.HerName + " and the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append(self.HerName + " Goes Black for the\n" + BBCNoNoun.Desc + " Big Black Cock " + BBCNoun.Desc)
          Tweets.append("The " + InnocentGirl.Desc + "\nGoes Black")

          sTweet = choice(Tweets)
          
          return sTweet

# Note: this 'gang bang' generator has been split in two. See also
# gen 14, gen 57
class Generator40(TitleGen):
     # My Shy Sporty Bride
     # Got Shared
     # by Two-Dozen Nude Leather-Jacketed Varsity Athletes
    def __init__(self):
        super().__init__(ID = 40, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate16()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["lesbian"]
          
        GangNot = ["Dapper","Gang-Bang"]
          
        GirlShort = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, MaxChars = 20,
                                    ExclList = [ClothingFemale, SpeciesFemale])
        
        GangPlurLong = char.GangMaleChar(MaleCharType = MaleCharType.GangPlural, 
                                         bAllowClothing = False, NotList = GangNot,
                                         MaxChars = 32)
          
        GangSize = WordList(["Three","Four","Five","Seven","Nine",
                             "Ten","A Bunch of","A Dozen","Twenty",
                             "Two-Dozen", "Dozens of", "Fifty","One-Hundred",
                             "Hundreds of","A Whole Bunch of"])
          
        sTweet = GirlShort.Desc 
        if sTweet[0:2].lower() == "my":
            sTweet += "\nGot Shared\nby " + GangSize.GetWord() + " " + GangPlurLong.Desc
        else:
            sTweet += "\nGets Shared\nby " + GangSize.GetWord() + " " + GangPlurLong.Desc

          
        return sTweet
          
class Generator41(TitleGen):
     #Seducing Sheryl: The Virginal Nurse and the Big Titty Dominatrix
     def __init__(self):
         super().__init__(ID = 41, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate17()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["women"]
          self.ExclTemplateTags = ["man","men","gay","straight"]
          
          Gerunds = WordList(["Seducing", "Tempting", "Corrupting", "Degrading", "Debauching", "Perverting", "Whipping",
                              "Fisting", "Sixty-Nining", "Scissoring", "Tribbing", "Fingering"])

          GoodGirl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium, MaxChars = 22,
                                     ExclList = [PregState, MaritalStatusFemale, SpeciesFemale, TitlesFemale])
          LesGirl = char.LesbianChar(Type = GirlType.Bad, MaxChars = 22, #SelectTemplateID = 401, 
                                     bAddTheArticle = True, sPosArticle = "Her",
                                     ExclList = [AgeAdjFemale, SpeciesFemale],
                                     NotList = ["straight"])
                                             
          sTweet = Gerunds.GetWord() + " " + self.HerName + ":\n"
          sTweet += "The " + GoodGirl.Desc + "\nand\n" + LesGirl.Desc 

          return sTweet
          
class Generator42(TitleGen):
     # Deflowered in the Pleasure Gardens of the Studly Bare-Chested Pirate Count
     def __init__(self):
         super().__init__(ID = 42, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate13()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["lesbian"]
          
          VNotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]
          SexPlaces = WordList(["Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem", "Stables"])
          Master = char.MaleChar(MaxChars = 30, SelectTemplateID = 15)
          
          sTweet = self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Public"]) + "\n"
          sTweet += "in the " + SexPlaces.GetWord() + "\nof the\n" 
          sTweet += Master.Desc 

          return sTweet

class Generator43(TitleGen):
     # Secret Baby for the Well-Hung Italian Count 
     #          - this is very similar to gen 10.
     def __init__(self):
         super().__init__(ID = 43, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          self.ReqTemplateTags = ["straight","couple"]
          self.ExclTemplateTags = ["kinky"]

          MaleNotList = ["Nude","S.W.A.T.","Naked"]
          TemplateID = choice([3,5])
          Master = char.MaleChar(SelectTemplateID = TemplateID,
                                 ExclList = [MaritalStatusMale,DickCharMale,ProfMale],
                                 ReqList = [NationMale],
                                 NotList = MaleNotList)
          sTweet = WordList(["Secret Baby", "Illegal Baby", "Twin Babies", "Secret Twin Babies", 
                             "Fertile Surrogate", "Secret Surrogate", "Secretly Pregnant", 
                             "Illegally Pregnant", "Illegal Twin Babies"]).GetWord().upper()
          sTweet += "\nfor the " + Master.Desc #+ " " + Nation.GetWord() + " " + Title.GetWord()
          
          return sTweet
          
# NOTE: split off from Gen 23
class Generator44(TitleGen):
     # Frank and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
     def __init__(self):
         super().__init__(ID = 44, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate2()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian", "straight", "women", "woman"] 
          
          sHisName = PlainNamesMale().FirstName()

          GayTitles = []
          
          StraightGuy = char.MaleChar(bAllowGang = False, ExclList = [SpeciesMale])
          GayGuy = char.GayMaleChar(ReqList = [GayMaleAdj])
          
          sTweet = sHisName + "\nand\nThe " + GayGuy.Desc

          return sTweet
          
class Generator45(TitleGen):
     # The Sporty Black Farmer's Daughter
     # Gets Naked at the Museum!]
     def __init__(self):
         super().__init__(ID = 45, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["women", "man"] 

          NudeActions = WordList(["Gets Naked", "Flashes Herself", "Goes Streaking", "Goes Topless", 
                                        "Goes Bottomless", "Exposes Herself", "Goes Nude",
                                        "Strips Naked", "Twerks Naked", "Publically Exposes Herself",
                                        "Takes Her Top Off","Drops Her Panties","Flashes Her Flower"])
          Places = WordList(["in the Park", "on Main Street", "at the Bank", "at the Bar", "in the Pub", 
                                   "at the Grocery Store", "at the Gym", "at the Beach", "on Campus", "at the Museum",
                                   "Downtown","at Starbucks","at Wal-Mart","at the Mall","at the Ball Game",
                                   "at the Stadium","at the Beach","on the Train","on the Subway","in Traffic",
                                   "at School"])
          Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, NotList = ["Nudist"], #bAllowSpecies = False)
                                        ReqList = [SkinHairColorFemale],
                                        ExclList = [SpeciesFemale,AttitudeGoodFemale])
          sTweet += Girl.Desc + "\n"
          sTweet += NudeActions.GetWord() + " " + Places.GetWord() + "!"

          return sTweet

# Secretly In Love With
# My Elf Supermodel Sister
class Generator46(TitleGen):
     def __init__(self):
         super().__init__(ID = 46, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          if CoinFlip():
               self.ReqTemplateTags = ["man"]
               Master = char.MaleChar(bAddEndNoun = False, MaxChars = 32, NotList = ["boyfriend"], 
                                      bAllowRelate = False, bAllowMaritalStatus = False, 
                                      bAllowSpecies = False, bAllowAge = False, 
                                      bAllowTitle = False, bAllowTrope = False)
               Relations = titmisc.RelateMale()
               Prefix = WordList(["Secretly In Love\nWith"])
               sTweet = Prefix.GetWord() + " my\n" + Master.Desc + " " + Relations.GetWord(NotList = ["Boyfriend", "Husband", "Hubbie", "Widower", "Fiancé"])
          else:
               self.ReqTemplateTags = ["woman"]
               Girl = char.FemaleChar(bAddEndNoun = False, MaxChars = 32, 
                                      NotList = ["girlfriend"], bAllowRelate = False, 
                                      bAllowMaritalStatus = False, bAllowSpecies = False, 
                                      bAllowAge = False, bAllowTitle = False, 
                                      bAllowTrope = False)
               Relations = titmisc.RelateFemale()
               Prefix = WordList(["Secretly In Love\nWith"])
               sTweet = Prefix.GetWord() + " my\n" + Girl.Desc + " " + Relations.GetWord(NotList = ["Girlfriend", "Mistress", "Wife"])
          return sTweet
          
# class Generator47(TitleGen):
     # # My Step-Dad Transforms Into A Cocky Gentleman Mer-Man!
     # ID = 47
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # Relate = titmisc.RelateMale()
          # Species = titmisc.SpeciesMale()
          # VerbTrans = WordList(["Transforms", "Transforms", "Changes", "Shifts", "Morphs", "Metamorphs"])
          
          # Master = MaleChar(bAddEndNoun = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowRelate = False, bAllowSpecies = False, bAllowTitle = False)
          
          # sTweet = "My " + Relate.GetWord() + " " + VerbTrans.GetWord() + "\ninto a\n" + Master.Desc + " " + Species.GetWord() + "!"

          # return sTweet
          
class Generator48(TitleGen):
     # Lusting For the Wicked Blonde Fetish Model
     def __init__(self):
         super().__init__(ID = 48, Priority = GenPriority.Low)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]

          GirlNotList = ['elf','skin','tanned','bronzed']
          Girl = char.FemaleChar(bAddTheArticle = True, NotList = GirlNotList, 
                                 MaxChars = 32, bAllowSpecies = False,
                                 ReqList = [SkinHairColorFemale],
                                 ExclList = [AgeAdjFemale,SexualityFemale,MaritalStatusFemale,PregState,NationFemale])
          
          sTweet = self.Gerunds.GetWord() + " " + Girl.Desc
          
          return sTweet          
          
class Generator49(TitleGen):
     # Taken Vigorously
     # in the Men's Restroom by
     # The Dominant Donkey-Dicked Italian Vegan Centaur
     def __init__(self):
         super().__init__(ID = 49, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate17()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["couple"]
          
          PublicPlaces = WordList(["At the Bowling Alley", 
               "In the Produce Section", 
               "In the Baked Goods Section",
               "In the Bakery",
               "At the Wine Tasting",
               "On the Coffee Table", 
               "In the Restroom at Chiopotle", 
               "Behind the Chic-fil-a", 
               "In the Ball Pit", 
               "In the Whole Foods Parking Lot",
               "In the Men's Restroom",
               "In the Women's Restroom",
               "In the Park",
               "At the Beach",
               "on the Eliptical Machine at the Gym",
               "At the Seafood Restaurant",
               "At the Museum",
               "At the Library",
               "At the Farmer's Market",
               "Next to the Duck Pond",
               "In the Window of a Shoe Store",
               "In the Hunting Section at a Wal-Mart",
               "In the Church Graveyard",
               "In the Old Castle Ruins",
               "At the Old Manor House",
               "In the Abandoned Mansion",
               "At the Construction Site",
               "Next to the Assembly Line",
               "On a Hotel Balcony"
               ])
          
          Verbs = WordList(["Claimed", "Claimed",
               "Mounted",
               "Pleasured",
               "Ravished",
               "Taken","Taken","Taken"])
               
          Adverbs = WordList(["Hard","Hard","Hard",
               "Forcefully",
               "Passionately",
               "Roughly",
               "Ruthlessly",
               "Vigorously"])
               
          Master = char.MaleChar(bAddTheArticle = True, bSplitArticle = True,
                                 MaxChars = 20)
          
          if CoinFlip():
               sTweet = Verbs.GetWord()
          else:
               sTweet = Verbs.GetWord() + " " + Adverbs.GetWord() 

          sTweet += "\n" + PublicPlaces.GetWord() + "\n"

          sLine3_4 = "by " + Master.Desc.upper()
          sLine3_4 = sLine3_4.replace("by THE", "by the").replace("by MY", "by my")
          sTweet += sLine3_4
          
          return sTweet
          
class Generator50(TitleGen):
     # What's a Little Deep Throat Between Bros?
     def __init__(self):
         super().__init__(ID = 50, Priority = GenPriority.AboveAverage)
         # self.Template = templates.TitleTemplate8()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          
          Adjective = WordList(["Light ","Light ",
               "Friendly ",
               "Gentle ",
               "Mild ",
               "","","","","","",""])
          
          NaughtinessStraight = WordList(["Anal", 
               "Anal Sex",
               "Ass-Eating",
               "BDSM",
               "Blowjob",
               "Bondage",
               "Bukkake",
               "Butt Sex",
               "Butt Stuff",
               "Creampie",
               "Cum Swapping",
               "Cunnilingus",
               "Deep Throat",
               "Dry-Humping",
               "Dogging",
               "Edging",
               "Fellatio",
               "Fingering",
               "Footjob",
               "Foreplay",
               "Fucking",
               "Hand-Job",
               "Jerking Off",
               "Masturbation",
               "Mutual Masturbation",
               "Nipple Play",
               "Pegging",
               "Rape Play",
               "Rimming",
               "Sex",
               "Spanking",
               "Spooning Naked",
               "Striptease",
               "Tantric Sex",
               "Tea-bagging",
               "Titty Fuck",
               "69ing",
               "Water Sports",
               "Wife-Swapping"])
               
          NaughtinessGay = WordList(["Anal", 
               "Anal Sex",
               "Ass-Eating",
               "Butt Sex",
               "Butt Stuff",
               "Deep Throat",
               "Edging",
               "Fellatio","Fellatio",
               "Gay Sex", "Gay Sex", "Gay Sex",
               "Hand-Job",
               "Jerking Off",
               "Masturbation",
               "Mutual Masturbation",
               "Nipple Play",
               "Rimming",
               "Spanking",
               "Spooning Naked",
               "Striptease",
               "Tea-bagging",
               "69ing",
               "Water Sports"])
               
          NaughtinessLez = WordList(["Ass-Eating",
               "BDSM",
               "Bondage",
               "Butt Stuff",
               "Cunnilingus",
               "Dry-Humping",
               "Finger Bang",
               "Fingering",
               "Fisting",
               "Masturbation",
               "Muff Diving",
               "Mutual Masturbation",
               "Tit Play",
               "Pegging",
               "Rimming",
               "Rug Munching",
               "Spanking",
               "69ing",
               "Water Sports"])
               
          FriendsGen = WordList(["Brother and Sister",
               "Colleagues",
               "Cousins","Cousins",
               "Co-workers","Co-workers",
               "Good Friends",
               "Friends",
               "Platonic Friends",
               "Roommates",
               "Siblings",
               "Step-Siblings",
               "Study Buddies",
               "Teacher and Student",
               "Teammates"])
               
          FriendsGay = WordList(["Boys",
               "Bros",
               "Brothers",
               "Buddies",
               "Cellmates",
               "Cowboys",
               "Dads",
               "Dudes",
               "Good Friends",
               "Fraternity Brothers",
               "Friends",
               "Lumberjacks",
               "Married Men",
               "Monks",
               "Priests",
               "Roommates",
               "Sailors",
               "Step-Brothers",
               "Straight Friends",
               "Twin Brothers"])
          
          FriendsLez = WordList(["Cellmates",
               "Cheerleaders",
               "Cousins","Cousins",
               "Coworkers",
               "Girls",
               "Girlfriends",
               "Married Women",
               "Moms",
               "Nuns",
               "Nurses",
               "Sisters",
               "Sorority Sisters",
               "Step-Sisters",
               "Twin Sisters"])
          
          sTweet = "What's a Little " + Adjective.GetWord()
          
          iRand = randint(1,3)
          if iRand == 1:
               #straight
               self.ReqTemplateTags = ["straight","couple"]
               self.ExclTemplateTags = ["gay"]
               print("Generator #50... STRAIGHT")
               sTweet += NaughtinessStraight.GetWord() + " Between " + FriendsGen.GetWord()
          elif iRand == 2:
               #gay
               self.ExclTemplateTags = ["woman","women"]
               print("Generator #50... GAY")
               sTweet += NaughtinessGay.GetWord() + " Between " + FriendsGay.GetWord()
          else:
               #lesbian
               self.ExclTemplateTags = ["man","men"]
               print("Generator #50... LESBIAN")
               sTweet += NaughtinessLez.GetWord() + " Between " + FriendsLez.GetWord()
                    
          sTweet += "?"
          return sTweet

class Generator51(TitleGen):
     # Juliana the Nudist Damsel in:
     # The Kingdom of the Dildo-Bots
     def __init__(self):
         super().__init__(ID = 51, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate18()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          
          sName = self.HerName 
          Girl = None
          
          Places = WordList(["Land", "Kingdom", "Planet", "World", "Lost Land", "Lost World", "Forgotten Kingdom", "Island", 
                                 "Lost Island", "Zone", "Forbidden Zone"])
          Beings = WordList(["Penisaurs", "Dong-o-saurs", "Fuck Men", "Ass-Eaters", "Ass Apes", "Cock-o-saurus Rex", 
                                 "Tri-cock Men", "Sex Robots", "Dildo-Bots", "Uniporns", "Girthy Griffons", "Boner Beasts", 
                                 "Homo Erectus", "Horny Mermen", "Barewolves", "Lepra-dongs", "Semen Centaurs", "Cum Imps", 
                                 "Dick Dwarves", "Anal Elves", "Anal Aliens", "Naked Barbarians", "Naked Cowboys", 
                                 "Massive Martians", "Cum Commandos", "Knob Goblins", 
                                 "Turgid Trolls", "Bukkake Basilisks", "Bukkake Bugbears", "Blowjob Bugbears",
                                 "Double-Dick Demons","Tea-Bagging Tyrannosaurs","Tea-Bagging Trolls","Frottage Fairies",
                                 "Muff-Diving Mermaids","Muff-Diving Medusas","Dry-Humping Druids","Anal Angels",
                                 "Ass-Eating Angels","Ass-Eating Aliens","Sex Serpents","Penis Pythons"])
          
          if CoinFlip():
               Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, MaxChars = 22,
                                      bAllowMaritalStatus = False, bAllowSpecies = False, 
                                      bAllowPregState = False)
          else:
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddTheArticle = True, MaxChars = 22,
                                      bAllowMaritalStatus = False, bAllowSpecies = False, 
                                      bAllowPregState = False)
               
          sTweet = sName + "\n" + Girl.Desc + "\nin\n"     
          sTweet += "The " + Places.GetWord() + " of the " + Beings.GetWord()

          return sTweet
          
# My Hot Redhead Teacher
# Is Secretly
# A Stripper!
#            - needs work: custom char templates
class Generator52(TitleGen):
     def __init__(self):
         super().__init__(ID = 52, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate2()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay"]
          
          Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])
          
          GoodGirlNotList = ["Co-ed","Mommy Blogger","Model"]
          GoodGirl = char.FemaleChar(Type = GirlType.Good, SelectTemplateID = 8, 
                                     NotList = GoodGirlNotList, 
                                     TempType = TempType.Medium)
                                        
          #iTempID = choice([222,220,205,2,2,2])
          BadGirl = char.FemaleChar(TempType = TempType.Medium, #NotList = BadGirlNotList, 
                                    bAddAnArticle = True, SelectTemplateID = 20)
          
          if CoinFlip():     
               sTweet+= "My " + GoodGirl.Desc + "\nIs Secretly\n" 
               sTweet+= BadGirl.Desc + "!"
          else:
               sTweet+= "My " + GoodGirl.Desc + "\nIs Secretly\n" 
               sTweet += BadGirl.Desc + "!"

          return sTweet     
          
# Daddy Found Out
# His Sweet Little Step-Daughter 
# Is a Sassy Asian Stripper 
# And Now He's Pissed!
#          - also needs work
class Generator53(TitleGen):
     def __init__(self):
         super().__init__(ID = 53, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NiceAdjs1 = WordList(["Bashful","Chaste","Conservative","Demure","Innocent",
                                    "Modest","Sheltered","Shy","Tender","Wholesome","Introverted","Bubbly",
                                    "Sweet","Sweet","Sweet","Little","Little"])
          NiceAdjs2 = WordList(["Christian","Christian","Mormon","Virgin","All-American",
                                    "Athletic","Blonde","British","Brunette","Cheerleader","Dark-Skinned","Curvy",
                                    "Ebony","French","Gymnast","Redheaded","Mormon","Curly-Haired"])
          sNiceAdj1 = NiceAdjs1.GetWord()
          sNiceAdj2 = NiceAdjs2.GetWord()
          
          RelateGirls = WordList(["Step-Daughter","Daughter"])
          
          BadGirlNotList = ['MILF','Masseuse','Housewife']
          Girl = char.FemaleChar(SelectTemplateID = 20, Type = GirlType.Bad, NotList = BadGirlNotList)
          
          sTweet = "Daddy Found Out\nThat His " + sNiceAdj1 + " " + sNiceAdj2 + " " + RelateGirls.GetWord() + "\n"
          sTweet += "Is " + AddArticles(Girl.Desc) + "\nAnd Now He's Pissed!"

          return sTweet     
          
# 8" of Steel:
# The Feisty Princess (Nubile Queen / Virginal Priestess)
# Encounters 
# The Strapping Naked Half-Orc Barbarian 
class Generator54(TitleGen):
     def __init__(self):
         super().__init__(ID = 54, Priority = GenPriority.Lowest, Disabled = True)
         self.Template = templates.TitleTemplate19()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","lesbian"]
          self.ReqTemplateTags = ["fantasy"]
          
          Weapons = WordList(['Steel','Molten Steel','Iron','Molten Iron','Hot Steel','Burning Steel','Hot Iron','Smoldering Steel'])
          LadyAdjs1 = WordList(['Feisty','Nubile','Virginal','Saucy','Wanton','Chaste','Demure','Virginal',
                                     'Winsome','Brazen','Sassy','Willing','Lonesome','Sheltered','Blossoming'])
          LadyAdjs2 = WordList(['Buxom','Ample-Bosomed','Apple-Bottomed','Bosomy','Jiggling','Little','Naked','Narrow-Waisted',
                                     'Nude','Petite','Plump','Ripe','Rubenesque','Shapely','Slender','Willowy','Statuesque',
                                     'Tender','Voluptuous','Young','Undressed','Elf','Elven'])
          Ladies = WordList(['Princess','Queen','Maiden','Priestess','Maid','Nun','Damsel','Handmaiden','Elf Maiden'])
          MaleAdjs1 = WordList(['Beefy','Brawny','Bearded','Broad-Chested','Enormous','Hairy','Handsome','Huge','Muscle-Bound',
                                     'Muscular','Strapping','Hunky'])
          MaleAdjs2 = WordList(['Powerful','Shirtless','Naked','Nude','Brazen','Rakish','Roguish','Cocky','Cocksure',
                                     'Gruff','Dominant','Horny','Lustful','Randy','Savage','Wanton'])
          DickAdjs = WordList(['Donkey-Dicked','Engorged','Erect','Fully Erect','Girthy','Hard','Horse-Cock',
                                     'Hugely Erect','Hung','Hung','Massively Erect','Rock-Hard','Throbbing',
                                    'Visibly Aroused','Visibly Erect','Well-Hung','Well-Hung','Well-Endowed',
                                     'Well-Endowed','Virile'])
          MaleSpecies = WordList(['Dark Elf','Demon','Dwarf','Centaur','Gargoyle','Giant','Goat Man','Goblin',
                                        'Half-Orc','Lizard Man','Orc','Vampire','Werewolf','Dragon Man','Half Dragon',
                                        'Minotaur'])
          MaleClass = WordList(['Barbarian','Warrior','Knight','Ranger','Bandit','Highwayman','Prince','Duke','Mercenary',
                                        'Paladin','Monk','Rogue','Thief','Warlock','Sorcerer','Hunter','Swordsman','Soldier',
                                        'Troubador','Woodsman','Blacksmith'])
                                        
          sLength = choice(["Six","Seven","Eight","Nine","Ten","Eleven","Twelve"])
          sTweet = sLength + " Inches of " + Weapons.GetWord() + "\n"
          sTweet += "The " + LadyAdjs1.GetWord() + " " + LadyAdjs2.GetWord() + " " + Ladies.GetWord() + " "
          sTweet += "Encounters "
          
          sMonster = ""
          if CoinFlip():
               sMonster += MaleAdjs1.GetWord() + " "
          if CoinFlip():
               sMonster += MaleAdjs2.GetWord() + " "
          if CoinFlip():
               sMonster += DickAdjs.GetWord() + " "
               
          #print("Monster string is [" + sMonster.strip() + "]")
          if sMonster.strip():
               sMonster = AddArticles(sMonster, bMakeUpper = True)
          else:
               sMonster = "The " + sMonster
               
          iRand = randint(1,5)
          if iRand == 1 or iRand == 2:
               sMonster += MaleSpecies.GetWord()
          elif iRand == 3 or iRand == 4:
               sMonster += MaleClass.GetWord()
          else:
               sMonster += MaleSpecies.GetWord() + " " + MaleClass.GetWord()
               
          sTweet += sMonster

          return sTweet     
          
# The Sarah Sandwich:
# Fireman on Top,
# Fireman on the Bottom,
# Kinky Airline Stewardess in the Middle
class Generator55(TitleGen):
     def __init__(self):
         super().__init__(ID = 55, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate20()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemmeNames = WordList(['Amy','Alicia','Alice','Alexis','Amanda','Amber','Angelica','Anita','Anna','Ava','Bella','Belle','Bianca',
                                      'Daphne','Delilah','Delores','Donna','Doris','Eliza','Elizabeth','Emma','Ericka','Esmerelda',
                                      'Estelle','Felicia','Felicity','Fiona','Francesca','Georgina','Gisele','Inya','Isabelle',
                                      'Jacinda','Jackie','Jasmine','Josephine','Julie','Juliette','Karen','Katrina','Laurel','Lola',
                                      'Marianna','Marilyn','Marsha','Melina','Molly','Natasha','Olivia','Phillippa',
                                      'Phoebe','Piper','Regina','Rosie','Ruby','Ruth','Sabrina','Sharon','Sylvia','Vanessa','Veronica'
                                      ])
          AllowedProfs = WordList(titmisc.ProfBlueCollarMale().GetWordList() + titmisc.ProfWhiteCollarMale().GetWordList() + titmisc.ProfAthleteMale().GetWordList() + titmisc.ProfRockstarMale().GetWordList())
          sJob1 = AllowedProfs.GetWord()
          sJob2 = AllowedProfs.GetWord(NotList = [sJob1])
          
          GirlNotList = ['Queen','Princess','Single','Concubine','Slave']
          Girl = char.FemaleChar(TempType = TempType.Medium, Type = GirlType.Good, NotList = GirlNotList, 
                                        bAllowAttitude = False, bAllowAge = False, bAllowSpecies = False)
          sHerName = FemmeNames.GetWord()
          
          sTweet = "The " + sHerName + " Sandwich\n"
          sTweet += sJob1 + " on top,\n"
          sTweet += sJob2 + " on the bottom,\n"
          sTweet += Girl.Desc.capitalize() + " in the middle!"

          return sTweet     
          
# The Kinky Brazillian Bikini Model
# is hot for
# Bald Men!
class Generator56(TitleGen):
     def __init__(self):
         super().__init__(ID = 56, Priority = GenPriority.Lowest)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FirstAdjs = WordList(['Sultry','Sexy','Stunning','Hot','Bubbly','Perky','Gorgeous','Foxy','Sensual',
                                     'Passionate','Seductive','Slinky','Spicy','Luscious','Stunning','Nympho'])
          RaceHairColor = WordList(['Korean','Japanese','Brazilian','Argentinian','Swedish','Eastern European','Latvian',
                                          'Coffee-Skinned','Black','Blue-Eyed','Green-Eyed','Redheaded','Platinum Blonde',
                                          'South African','Icelandic','Irish','Pale','Porcelain-Skinned','Chinese',
                                          'Italian','French','Latina','Columbian'])
          PhysAdjs = WordList(['Tall','Stacked','Leggy','Willowy','Slender','Bronzed','Voluptuous','Statuesque','Skinny',
                                    'Jiggling','Tanned','Bubble-Butt','Tight-Bodied','Full-Figured','Curvaceous','Juicy'])
          ExoticGirlJobs = WordList(['Bikini Model','Supermodel','Fashion Model','Flight Attendant','Lingerie Model',
                                             'Masseuse','Playboy Centerfold','Penthouse Pet','Erotic Model','Beach Bunny',
                                             'Beauty Queen','Actress','Starlet','Movie Star'])
          PreFetishes = WordList(['Middle-Aged','Dad Bod','Overweight','Stay-at-Home','Chubby','Nerdy','Geeky','Awkward',
                                    'Anti-Social','Unemployed','Flabby','Paunchy','Short'])
          PostFetishes = WordList(['Bald Spots','Micro Penises','Micro Penises','Beer Bellies','Dad Bods','Bacne','Social Anxiety',
                                         'Drinking Problems','Sleep Apnea'])
          PhysAttr = WordList(['Black','Bearded','Bald','Balding','Curly-Haired','Jewish','Canadian',
                                    'Red-Headed','Ginger','Brown-Haired','Graying','British','Asian','Indian','Polish','Danish',
                                    'Pale','Suburban'])
          Men = WordList(['Men','Dads','Middle Managers','Construction Workers','Doctors','College Students','Virgins',
                              'Cops','Male Nurses','Fire Fighters','Ball Boys','Web Designers','Gym Coaches',
                              'Professors','Engineers','Software Engineers','Lawyers','Preachers','Ministers',
                              'Youth Ministers','Car Salesmen','English Teachers','Math Teachers','IT Technicians',
                              'Guitar Teachers','Realtors','Waiters','Ex-Cons','Hipsters','Single Dads',
                              'Walmart Greeters','Security Guards','Uber Drivers','Old Guys','Guys','Dudes','Janitors',
                              'Consultants','Tax Preparers','Accountants','Insurance Adjustors','Roofing Contractors',
                              'Golf Caddies','Plumbers','Truckers','Drywall Installers','Parole Officers',
                              'Corrections Officers','Dungeon Masters'])
                                             
          sExoticGirl = ""
          if CoinFlip():
               sExoticGirl += FirstAdjs.GetWord() + " "
          if CoinFlip():
               sExoticGirl += RaceHairColor.GetWord() + " "
          if CoinFlip():
               sExoticGirl += PhysAdjs.GetWord() + " "
          sExoticGirl += ExoticGirlJobs.GetWord()
          
          if CoinFlip():
               sMan = PreFetishes.GetWord() + " " + PhysAttr.GetWord() + " " + Men.GetWord()
          else:
               sMan = PhysAttr.GetWord() + " " + Men.GetWord() + " with " + PostFetishes.GetWord()
          
          sTweet = "This " + sExoticGirl + "\n" + WordList(['is hot for','has a thing for']).GetWord() + "\n" + sMan + "!"

          return sTweet     
          
# Taken in the Locker Room 
# by an Entire Team of 
# Muscular Lumberjack Hockey Players
class Generator57(TitleGen):
     def __init__(self):
         super().__init__(ID = 57, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate21()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["couple","lesbian","women"]
          
          Verbs = WordList(['Taken','Gang-Banged','Shared','Claimed','Taken Hard','Claimed Hard','Tied Up & Used','Deflowered',
                                'Fisted','Motor-Boated','Impregnated','Fertilized','Mounted Bareback','Ridden Hard','Pleasured',
                                'Ravished','Satisfied','Oiled Up','Paddled'])
          Teams = WordList(['Hockey Players','Football Players','Basketball Players','Sumo Wrestlers','Rugby Players',
                                'Baseball Players','Olympic Swimmers','Wrestlers','Soccer Players'])
          sTeam = Teams.GetWord()
          MenNotList = [sTeam, 'Single']
          Men = char.MaleChar(TempType = TempType.Medium, bAddEndNoun = False, NotList = MenNotList,
                              bAllowAge = False, bAllowAttitude = False, bAllowGenMod = False, bAllowRelate = False, bAllowTitle = False)
     
          sTweet += Verbs.GetWord() + "\nIn the Locker Room\nby an\nEntire Team of " + Men.Desc + " " + Teams.GetWord()

          return sTweet     
          
# I hooked up with a strapping leather cowboy
# and now I'm pregnant!
class Generator58(TitleGen):
     def __init__(self):
         super().__init__(ID = 58, Priority = GenPriority.Low)
         # self.Template = templates.TitleTemplate4()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","lesbian","women","men"]
          
          ManNotList = ["Widowed"]
          HookUpPhrases = WordList(["Hooked Up With", "Had a One Night Stand With", 
                                    "Slept With", "Banged", "Had a Quickie With", 
                                    "Fooled Around With"])
          MaleRelatives = WordList(["Step-Dad", "Step-Brother", "Brother", "Brother-in-Law", "Father", "Dad", "Daddy", "Step-Father"])
          Man = char.MaleChar(NotList = ManNotList, MaxChars = 30,
                              bAllowRelate = True, bAllowSpecies = True, 
                              bAllowMaritalStatus = False, bAllowGang = False, 
                              bAllowTitle = False)
          sMan = Man.Desc 
          
          if FoundIn(sMan, MaleRelatives.List):
               sTweet = "I " + HookUpPhrases.GetWord() +" My " + sMan + " And Now I'm Pregnant!"
          else:
               sTweet = "I " + HookUpPhrases.GetWord() +" " + AddArticles(sMan, bMakeUpper = True) + " And Now I'm Pregnant!"
          return sTweet
     
# # The hot bikini model prom queen
# # is secretly a lesbian      
# class Generator59(TitleGen):
     # ID = 59
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # sHotAdjs = WordList(["Dirty", "Hot", "Sexy", "Busty", "Jiggly", "Stacked", "Athletic", "Slender", "Apple-Bottomed", "Curvaceous", "Flexible"])
          # sGirlAdjs = WordList(["Blonde", "Redhead", "Asian", "Chocolate", "Giggly", "Flirty", "Curly-Haired", "Tattooed"])
          # GirlNouns = WordList(["Schoolgirl", "Bimbo", "Cheerleader", "Bikini Model", "Prom Queen", "Teen", "Coed", "Gymnast",
                                        # "Baby-Sitter", "Fashion Model", "Beach Bunny", "Surfer Girl", "Goth Girl"])
          # sNoun1 = GirlNouns.GetWord()
          # sNoun2 = GirlNouns.GetWord(NotList = [sNoun1])

          # sTweet = "The " + sHotAdjs.GetWord() + " " + sGirlAdjs.GetWord() + " "
          # sTweet += sNoun1 + " " + sNoun2 + "\n"
          # sTweet += "Is Secretly a Lesbian!" 
          # return sTweet          
          
# Sweet Little Amy
# The Swedish Schoolgirl 
# and her 
# Adventure with the
# Magic Butt Plug
class Generator60(TitleGen):
     def __init__(self):
         super().__init__(ID = 60, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate21()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["man","men"]
          
          NiceNames = WordList(['Amy','Angelica','Annie','Charity','Daisy','Daphne','Elsie',
                                     'Emmy','Frances','Gertrude','Greta','Jeanie','Lacey','Lizzy',
                                     'Mabel','Mary','Maryanne','Molly','Nancy','Nell','Olive','Phoebe',
                                     'Rosie','Shelly','Sophie','Summer','Virginia'])

          ObjectAdjs = WordList(['Demon-Possessed','Enchanted','Haunted','Magic','Magical'])
          ObjectNouns = WordList(['Anal Beads','Anal Hook','Ball Gag','Ben Wa balls','Bull Dyke','Butt Plug',
                                        'Clit Clamp','Clit Pump','Crotchless Panties','Dildo','11\" Dildo',
                                        'Double-Ended Dildo','Gimp Mask','Hitachi Magic Wand','Leather Riding Crop',
                                        'Nipple Clamps','Orgasmatron','Pearl Necklace','Rabbit Vibe','Rubber Fetish Suit','Sex Doll',
                                        'Sex Swing','Spreader Bar','Speculum','Strap-On','Sybian','Thong','Vibrator'])
          sNice1 = ""
          sNice2 = ""

          NiceGirl = char.FemaleChar(SelectTemplateID = 501, bAddTheArticle = True,
                                     ReqList = [DiminuitiveNiceGirl])
          
          sTweet += NiceGirl.Desc

          sTweet += "\nAnd Her Adventure With\n"
          sTweet += "The " + ObjectAdjs.GetWord() + " " + ObjectNouns.GetWord()
          
          return sTweet     

class Generator61(TitleGen):
    # DOMINATED
    # by the
    # Busty Japanese Schoolgirl
    def __init__(self):
        super().__init__(ID = 61, Priority = GenPriority.AboveAverage)
        self.Template = templates.TitleTemplate28() # CHANGe
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
          
        if CoinFlip():
            self.ExclTemplateTags = ["gay","couple"]
            self.ReqTemplateTags = ["woman"]
        else:
            self.ReqTemplateTags = ["femdom"]

        Woman = char.FemaleChar(bAddTheArticle = True, sPosArticle = "My",
                                bAllowRelate = True)

        sTweet = "Dominated\n"
        sTweet += "by\n" + Woman.Desc
          
        return sTweet  
          
# Help!
# A husky investment banker
# has me chained up in his basement (garage/sex dungeon)
# naked!
class Generator62(TitleGen):
    def __init__(self):
        super().__init__(ID = 62, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate22()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        if CoinFlip() and CoinFlip():
            self.ReqTemplateTags = ["tied up","woman"]
            self.ExclTemplateTags = ["femdom"]
        else:
            self.ReqTemplateTags = ["naked","woman"]
          
          
        BadNotList = ["Naked"]
        Exclamations = WordList(["Help!", "Help!", "Oh No!", "Uh Oh!"])
        BadPlaces = WordList(["Basement","Basement","Castle","Dungeon",
                            "Garage", "Attic","Man Cave", "Den", 
                            "Sex Dungeon", "Cellar","Secret Lair", 
                            "Secret Hideout", "Secret Love-Nest", 
                            "Bachelor Pad"])
        BadMan = char.MaleChar(bAddAnArticle = True, NotList = BadNotList, 
                                bAllowGang = False, MaxChars = 18,
                                bAllowSpecies = False, bAllowMaritalStatus = False)
          
        sTweet += Exclamations.GetWord() + "\n" 
        sTweet += BadMan.Desc + "\nHas Me Chained Up In His " + BadPlaces.GetWord() + ",\nNaked!"

        return sTweet     
          
# The Busty Blonde Flight Attendant's 
# Topless Miami Vacation
class Generator63(TitleGen):
    def __init__(self):
        super().__init__(ID = 63, Priority = GenPriority.Normal)
        self.Template = templates.TitleTemplate23()

    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["gay","straight"]
          
        Girl = None
        if CoinFlip():
            Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, 
                                   MaxChars = 20,
                                   bAllowSpecies = False, bAllowMaritalStatus = False, 
                                   bAllowTitle = False)
        else:
            Girl = char.FemaleChar(Type = GirlType.Bad, bAddTheArticle = True, 
                                   MaxChars = 20,
                                   bAllowClothing = False, bAllowSpecies = False, 
                                   bAllowMaritalStatus = False, bAllowTitle = False)

        VacType = WordList(["Topless", "Nudist", "Fully Nude", "Naked", "Fully Nude", "Naked"])
        VacPlace = WordList(["Miami", "Carribean", "Spanish", "Italian", "Greek", "Cancún", "Hawaiian", "Los Angeles", "Bangkok", 
                                "Las Vegas", "Macau", "Ibiza", "Jamaica", "New Orleans", "Rio", "Berlin", "Bali", "Goa", "Australian",
                                "Amsterdam", "Lagos", "Bora Bora", "Thai", "Fiji"])
        VacWord = WordList(["Vacation", "Vacation", "Getaway", "Holiday", "Spring Break"])
                                    
        sTweet = Girl.Desc + "'s\n" + VacType.GetWord() + " " + VacPlace.GetWord() + " " + VacWord.GetWord()
               
        return sTweet     
          
# 'Oh $@*#!'
# My new stepmom is a 
# Tanned Swedish Masseuse
# and 
# Her Ass Looks Amazing! 
class Generator64(TitleGen):
     def __init__(self):
         super().__init__(ID = 64, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Exclamations = WordList(["Oh S@*#!", "Uh Oh!", "WTF?!?", "Oh F*@%!"])
          Relatives = WordList(["Stepmom", "Stepmom", "Step-Sister", "Sister-in-Law", "Step-Daughter"])
          Ender = WordList(["Her Ass Looks Amazing", "She's At Least A Double-D", "She Likes To Sunbathe Nude", 
                                "She Doesn't Wear Panties", "She Likes To Go Braless", "She Likes To Go Commando", 
                                "She's A Shameless Nudist", "She Showers With The Door Open", "Her Boobs Are Incredible",
                                "She Shaves Herself Down There", "She Has The Body Of A Porn Star", "She Has Enormous Coconuts",
                                "And I've Seen Her Tits","And She Is Stacked"])
          Girl = char.FemaleChar(bAddAnArticle = True, bAllowClothing = False, bAllowRelate = False, 
                                        bAllowSexuality = False, bAllowSpecies = False, bAllowNation = True, 
                                        bAllowMaritalStatus = False, bAllowTitle = False, bAllowPregState = False)

          sTweet = Exclamations.GetWord() + "\nMy New " + Relatives.GetWord() + " Is\n" + Girl.Desc + "\nAnd " + Ender.GetWord()
          
          return sTweet     
          
# Anita Gets Serviced 
# By Five Naked Cowboys 
class Generator65(TitleGen):
     def __init__(self):
         super().__init__(ID = 65, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","lesbian"]
          
          Verbs = WordList(["Serviced","Pleasured","Taken","Satisfied","Shared","Ravished","Mounted","Treated Like A Lady"])
          Numbers = WordList(["Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve",
                                   "Thirteen"])
          Adjs = WordList(["Burly","Hairy","Mustachioed","Muscular","Bald","Beefy","Chiseled","Handsome",
                               "Tall","Hung","Hunky","Well-Endowed","Sexy","Rock Hard","Strapping","Strong",
                               "Gruff","Cocky","Powerful","Horny","Skillful","Tattooed"])
          Men = WordList(["Bikers","Cops","Cowboys","Firemen","Football Players","Gangsters","Knights",
                              "Weight Lifters","Mountain Men","Pirates","Scottsmen","Sumo Wrestlers","Werewolves",
                              "Viking Warriors","Bull Riders","Chippendales Dancers","Construction Workers",
                              "Defensive Linemen","Gladiators","MMA Fighters","Sailors","Gentleman","Older Men"])
          
          sTweet = self.HerName + " Gets " + Verbs.GetWord() + "\nBy\n"
          sTweet += Numbers.GetWord() + " " +Adjs.GetWord() + " Naked " + Men.GetWord()

          return sTweet     

# The Bride Wore a Ball Gag          
class Generator66(TitleGen):
     def __init__(self):
         super().__init__(ID = 66, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate7()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","lesbian","couple"]
          
          BrideWore = WordList(['Latex','Black Leather','Body Paint','a Spreader Bar','a Speculum','a Clit Pump','Nipple Clamps',
                                     'a Ball Gag','a Leash','a Butt Plug','an Anal Plug','a Vibrator','Crotchless Panties',
                                     'Assless Leather Chaps','an Anal Tail Plug','a Steel Collar','a Chain-mail Bikini',
                                     'a Clit Clamp','a Gimp Mask','a Leather Body Harness','Chocolate Lingerie','a Cupless Bra',
                                     'a Leather Catsuit','Crotchless Pantyhose','a Fishnet Bodystocking','a Chastity Belt',
                                     '9-inch Heels','Thigh-High Boots','a Steel Bra','a Leather Bikini','a G-string',
                                     'Pasties and a G-string','Handcuffs','a Sheer Black Bodysuit','Spiked Heels',
                                     'a Strap-On', 'a Black Leather Tail','Nothing','Black Latex','Red Leather','Red Latex',
                                     'a Black Body Harness','a Black Bodystocking','a Red Sheer Bodystocking',
                                     'a Black Sheer Bodystocking','a Black Leather Bikini','Black Pasties','Red Pasties'])
                                     
          sTweet = "The Bride\nWore " + BrideWore.GetWord() + "!"

          return sTweet     
          
# "Go easy on me! I'm a teenage coed nun
# and its my first time
# doing anal!"
class Generator67(TitleGen):
     def __init__(self):
         super().__init__(ID = 67, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate4()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Beginnings = WordList(["Please Go Easy On Me", "Please Be Gentle With Me", "Please Be Gentle", "Please Go Slow", 
                                      "Please Be Careful"])
          FirstTimes = WordList(["Doing Anal", "With A Girl", "With Another Woman", "Doing Butt Stuff", 
                                      "Wearing a Butt Plug", "In a Gimp Mask", "Being Punished With a Riding Crop",
                                      "In a Sex Swing", "Deep Throating", "Being Choked", "Trying Erotic Asphyxiation", 
                                      "Wearing Nipple Clamps", "In a Sex Dungeon", "Doing It in Public", "Swallowing",
                                      "With One This Big", "Trying Bukkake", "Trying Double Penetration",
                                      "With Two Dudes", "With Three Guys At Once", "Trying a Gang Bang",
                                      "With an Older Man", "Doing Hardcore Bondage Play", "Wearing a Ball Gag",
                                      "Trying Water Sports"])
          Girl = char.FemaleChar(Type = GirlType.Good, MaxChars = 22,
                                        bAllowMaritalStatus = False, bAllowTitle = False, 
                                        bAllowPregState = False)

          sTweet = "\"" + Beginnings.GetWord() + "!\"\n"
          sTweet += "I'm " + AddArticles(Girl.Desc) + "\n"
          sTweet += "And its my first time " + FirstTimes.GetWord().lower() + "!"

          return sTweet     
          
# I know I'm married,
# but it can't hurt if I try rimming
# with this Italian Don Juan cowboy 
# just this once!
class Generator68(TitleGen):
     def __init__(self):
         super().__init__(ID = 68, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          SexActs = WordList(["69 with","have Anal Sex with","try BDSM with","get a Dirty Sanchez from","try Double Penetration with",
                                   "try Erotic Asphyxiation with","try Leather Bondage with","try Face-Sitting with","get Fisted by",
                                   "get Rimmed by", "try Rimming","try Water Sports with","try Whips and Chains with",
                                   "try Spooning Naked with","try Age Play with","do Butt Stuff with","try Edging with",
                                   "get My Ass Eaten by","try Eating the Ass of","perform an Erotic Massage on",
                                   "do a Strip Tease for","give a Footjob to","try Nipple Play with","Go Down On",
                                   "give a Tit-Job to","get Cunnilingus from","get Eaten Out by","get Fingered by"])
          
          Man = char.MaleChar(bAddAnArticle = True, bAddEndNoun = False, 
                                   bAllowAge = False, bAllowRelate = False, bAllowSpecies = True, 
                                   bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False)
          
          sTweet = "\"I Know " + WordList(["I'm Married","I'm Married","I'm Engaged","I Have a Boyfriend"]).GetWord() + ", But\n"
          sTweet += "It Can't Hurt If I " + SexActs.GetWord() + " " + Man.Desc + " " + titmisc.ProfMale().GetWord() + "\n"
          sTweet += "Just This Once!\""

          return sTweet     
          
# The wholesome blonde Christian girl spreads her legs (bends over/drops her panties/puts out)
# for the cocky Italian DILF!
class Generator69(TitleGen):
     def __init__(self):
         super().__init__(ID = 69, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate24()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","lesbian","kinky","horror"]

          sArticle = "The"
          
          Actions = WordList(["Spreads her Legs","Spreads her Legs",
                              "Bends Over","Drops Her Panties",
                              "Lifts her Skirts","Spreads her Thighs",
                              "Spreads her Cheeks","Opens Her Legs",
                              "Spreads her Lips",
                              "Lubes Herself Up"])
          
          NiceGirl = char.FemaleChar(SelectTemplateID = 501, MaxChars = 16) #, ReqList = [DiminuitiveNiceGirl])
          if FoundIn(NiceGirl.Desc, ["sister","brother","mom","dad","mother",
                                     "father","fiancé","wife","girlfriend",
                                     "teacher","secretary","daughter",
                                     "babysitter","governess","tutor",
                                     "bride"]):
              sArticle = "My"

          Man = char.MaleChar(bAddAnArticle = True, sPosArticle = "Her", 
                              MaxChars = 22,
                              bAllowGang = False, bAllowTitle = True,
                              bAllowRelate = False)
          
          #iRand = randint(1,3)
          #if iRand == 1:
          #     sTweet = NiceGirl.Desc + "\n" + Actions.GetWord().lower() + " for\nThe" + Man.Desc 
          #else:
          sTweet = sArticle + " " + NiceGirl.Desc + "\n" 
          sTweet += Actions.GetWord().lower() + " for\n" + Man.Desc + "!"
               
          return sTweet     
          
# I shot a porn scene
# with a handsome BBC construction worker
class Generator70(TitleGen):
     def __init__(self):
         super().__init__(ID = 70, Priority = GenPriority.Normal, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Beginnings = WordList(["I Shot a Porn Scene", "I Made a Porn Video", "I Made a Porno", "I Shot a Porn Video", "I Did Porn"])
          Endings = WordList(["And His Friends", "And I Liked It", "While My Husband Watched", "And I Didn't Get Paid", 
                                   "And I Was Paid $60", "And Now I'm Pregnant", "While My Boyfriend Watched", "While My Girlfriend Watched",
                                   "And My " + WordList(["Dad","Brother","Step-Dad","Step-Brother"]).GetWord() + " Saw It",
                                   "And His " + str(randint(2,13)) + " Friends", "And I Didn't Tell My Boyfriend", "And I Didn't Tell My Dad",
                                   "And My Dad Found Out"])
                                   
          Man = char.MaleChar(bAddAnArticle = True, 
                                   bAllowSpecies = False, bAllowMaritalStatus = True, bAllowGang = False, 
                                   bAllowTitle = False)

          sTweet = "\"" + Beginnings.GetWord() + "\nwith\n" + Man.Desc
          sTweet+= "\n" + Endings.GetWord()
          sTweet += "\""
          
          return sTweet     
          
class Generator71(TitleGen):
     def __init__(self):
         super().__init__(ID = 71, Priority = GenPriority.Normal, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Beginnings = WordList(["I Shot a Lesbian Porn Scene", "I Made a Lesbian Porn Video", "I Made Lesbian Porn", "I Shot a Lesbian Porn Video", "I Did Lesbian Porn"])
          Endings = WordList(["And Her Friends", "And I Liked It", "While My Husband Watched", "And I Didn't Get Paid", 
                                   "And I Was Paid $50", "While My Boyfriend Watched", "While My Girlfriend Watched",
                                   "And My " + WordList(["Dad","Brother","Step-Dad","Step-Brother"]).GetWord() + " Saw It",
                                   "And Her " + str(randint(2,13)) + " Friends", "And I Didn't Tell My Boyfriend", "And I Didn't Tell My Mom",
                                   "And My Mom Found Out", "While My Wife Watched", "And I Didn't Tell My Girlfriend",
                                   "And Now I'm Pregnant","And Everyone at School Saw It","And All My Co-workers Saw It"])
                                   
          Girl = char.FemaleChar(bAddAnArticle = True, bAllowClothing = False, bAllowRelate = False, 
                                        bAllowSexuality = False, bAllowSpecies = False, bAllowMaritalStatus = True, 
                                        bAllowTitle = False)

          sTweet = "\"" + Beginnings.GetWord() + "\nwith\n" + Girl.Desc
          if CoinFlip():
               sTweet+= "\n" + Endings.GetWord()
          sTweet += "\""

          return sTweet     
          
# My New Coworker
# is a Strapping Long Haul Trucker
# and He Sucked My Titties 
class Generator72(TitleGen):
    def __init__(self):
        super().__init__(ID = 72, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate14()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["man"]
        self.ExclTemplateTags = ["lesbian"]
          
        ManNotList = ["Single"]
        Man = char.MaleChar(MaxChars = 22, bAllowGang = False,
                            ExclList = [MaritalStatusMale, TitlesMale, ProfBlueCollarMale, ProfWhiteCollarMale, ProfFantasyMale, RelateMale,DickCharMale,ClothesMale],
                            NotList = ManNotList)

        Relations = WordList(["Co-worker","Boss","Boss","Step-Brother","Brother-in-Law",
                              "Son-in-Law","Step-Son","Tutoring Student","Gym Coach",
                              "Personal Trainer","Massage Therapist","Nextdoor Neighbor",
                              "Math Teacher","Math Tutor","English Teacher",
                              "Literature Professor","Tennis Coach","Pool Boy"
                             ])
        NaughtyStuff = WordList(["He Ate Me Out","He Ate My Ass","He Sucked My Titties",
                                 "He Finger-banged My Twat","We Sixty-nined",
                                 "I Let Him Fist Me","I Let Him Shave My Cooch",
                                 "I Gave Him Head","I Gave Him a Hand-Job",
                                 "I Gave Him a Foot-Job","I scissored his wife",
                                 "He Whipped My Bare Ass With a Riding Crop",
                                 "I Sat On His Face","He Spanked My Bare Ass",
                                 "I Gave Him Road Head","I've Seen Him Naked",
                                 "We Showered Together","I Jerked Him Off",
                                 "I Dry-Humped Him","I Rimmed His Butt-hole",
                                 "He Wears a Cock Ring","He Has a Cock Piercing",
                                 "We Did Butt Stuff","I Went Down On Him",
                                 "He Went Down On Me", "I Rode Him Hard",
                                 "His cock is huge","his dick is enormous",
                                 "He's hung like a horse","I'm having his baby",
                                 "He tea-bagged me with his hairy balls",
                                 "We've had anal sex","I Deep-Throated Him"])

        sNaughty = NaughtyStuff.GetWord().lower()
        if sNaughty[0] == "i":
            sNaughty = sNaughty.capitalize()

        sTweet = "My New " + Relations.GetWord() + "\n"
        sTweet += "is " + AddArticles(Man.Desc) + "\n"
        sTweet += "and " + sNaughty + "!"
          
        return sTweet     
   
          
# class Generator73(TitleGen):
     # ID = 73
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # return sTweet     
          
class Generator74(TitleGen):
    def __init__(self):
        super().__init__(ID = 74, Priority = GenPriority.Lowest)
        self.Template = templates.TitleTemplate16()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["gay"]
          
        NiceGirl = char.FemaleChar(SelectTemplateID = 501)
        while len(NiceGirl.Desc) > 24:
            NiceGirl = char.FemaleChar(SelectTemplateID = 501)
          
        NaughtyStuff = WordList(["69ing", "Anal Hooks","Anal Sex","BBC","BDSM",
                                "Bukkake","Butt Plugs","Clit Clamps",
                                "a Dirty Sanchez","Double Penetration",
                                "Erotic Asphyxiation","Gang Bangs",
                                "an Interracial Threesome","Hardcore Bondage",
                                "Leather Bondage","Lesbian Sex","Face-Sitting",
                                "Oral Fisting","Vaginal Fisting","Anal Fisting",
                                "Orgies","Nipple Clamps","Public Nudity",
                                "Sex With Another Woman","Spanking",
                                "Stripping at a Club","Swinging","a Threesome",
                                "Big Black Cock","Black Dick","Rimming",
                                "A 12-inch Black Dildo","Whips and Chains",
                                "Hot-Wifing","Pussy","Pee Drinking",
                                "Extreme Vaginal Insertion","Group Sex",
                                "Extreme Anal Insertion","Deep-Throating",
                                "Auto-Erotic Asphyxiation","Scissoring"])

        Reactions = WordList(["Now She Can't Get Enough",
                              "Now She Wants More",
                              "Now She Won't Stop",
                              "Now She Won't Quit",
                              "Now She's Insatiable",
                              "Now She's a Street Whore",
                              "Now She's a Lesbian",
                              "It Turned Her Into A Sex-Crazed Bimbo",
                              "Now She's a Sex Addict",
                              "It Turned Her Into a Lesbian",
                              "Now She's a Professional Porn Star", 
                              "It Was Awkward and Not Really Her Thing"])

        sTweet = "My " + NiceGirl.Desc + "\nTried "
        sTweet += NaughtyStuff.GetWord() + "\n"
        sTweet += "And " + Reactions.GetWord().lower() + "!"
                    
        return sTweet     

class Generator75(TitleGen):
    def __init__(self):
        super().__init__(ID = 75, Priority = GenPriority.Lowest)
        self.Template = templates.TitleTemplate16()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["gay","couple"]
          
        Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])
          
        GirlNotList = ["black","african","ebony","dark-skinned"]
        NiceGirl = char.FemaleChar(SelectTemplateID = 501, NotList = GirlNotList)
        while len(NiceGirl.Desc) > 24:
            NiceGirl = char.FemaleChar(SelectTemplateID = 501)
          
        sTweet += Exclamations.GetWord() + "\n"
        sTweet += "My " + NiceGirl.Desc + " Went Black\n"
        sTweet += "and she won't come back!"

        return sTweet     
          
# My New Neighbor is a 
# Tanned Redheaded Secretary
# and 
# I Ate Her Out
class Generator76(TitleGen):
     def __init__(self):
         super().__init__(ID = 76, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate3()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay"]
          
          WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel","Maiden","Fetish","Call-Girl"]
          Girl = char.FemaleChar(NotList = WomanNotList, bAllowClothing = True, bAllowRelate = False, 
                                        bAllowSexuality = True, bAllowSpecies = False, bAllowMaritalStatus = False, 
                                        bAllowTitle = False, bAllowGenMod = True, bAddEndNoun = True)
          Relations = WordList(["Dad's New Girlfriend","New Next Door Neighbor","New Co-worker","New Boss","New Step-Sister",
                                        "New Step-Daughter","Daughter's New Best Friend","New Student","New Secretary",
                                        "New Sister-in-Law","New Girlfriend's Sister","New Assistant","New Gym Coach",
                                        "New Math Tutor","New English Teacher","Dad's New Wife","New Step-Mom"])
          NaughtyStuff = WordList(["I Ate Her Out","I Ate Her Ass","I Sucked Her Titties","I Finger-Banged Her",
                                         "I Gave Her a Pearl Necklace","I Gave Her a Rim Job","We Sixty-nined","I Fisted Her",
                                         "She Asked Me to Shave Her Cooch","I Took Pictures of Her Doing Nude Yoga","She Sucked Me Off",
                                         "She Gave Me a Hand-job","She Gave Me a Foot-Job","I Gave Her a Booty Massage... Naked",
                                         "She Let Me Play With Her Titties","She Likes to Wear Nipple Clamps",
                                         "I Whipped Her Bare Ass With a Riding Crop","She Sat On My Face",
                                         "She Smothered Me With Her Ass","She Pegged Me With a Strap-On","I Knocked Her Up",
                                         "I Spanked Her Bare Ass With a Steel Paddle","I Rimmed Her Butt-hole",
                                         "I've Seen Her Naked","She Let Me Soap Her Up in the Shower","I Got her Pregnant",
                                         "She Let Me Play With Her Hard Nips","She Let Me Play With Her Nipple Piercings"])
          sTweet = "“My " + Relations.GetWord() + "\nis\n"
          sTweet += AddArticles(Girl.Desc) + "\n"
          sTweet += "and\n" + NaughtyStuff.GetWord() + "!\""
          
          return sTweet     
          
# "I was a fertile harem girl
# for a strapping black cowboy sheikh"
class Generator77(TitleGen):
     def __init__(self):
         super().__init__(ID = 77, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          MateAdjs1 = WordList(["Fertile","Nubile","Breeding","Yielding","Pregnant","Kept","Blushing","Virginal",
                                    "Willing","Lactating","Ripe","Submissive","Subservient","Wide-Eyed","Conjugal",
                                    "Naive Young","Innocent","Bashful"])
          MateAdjs2 = WordList(["Buxom","Petite","Voluptuous","Small-Town","Dark-Eyed","Dark-Skinned","Blonde",
                                     "Brunette","Redheaded","Chubby","BBW","Slender","Coed","Country Girl","Wide-Hipped",
                                     "Full-Bodied","Nude","Shaved"])
          MateNouns = WordList(["Harem Girl","Bride","Mate","Concubine","Courtesan","Mistress","Princess","Wife"])
          ManAdjs = WordList(["Naked","Strapping","Nudist","Well-Hung","Virile","Muscular","Burly",
                                    "Hunky","Bald","Well-Endowed","Beefcake","Girthy","Handsome","Mustachioed",
                                    "Rock-Hard","Horny","Wicked","Kinky","Sensual","Naughty","Throbbing"])
          ManNouns = WordList(["Sheikh","Shah","Prince","Sultan","King","Vizir","Maharaja"])
          sManAdj = ManAdjs.GetWord()
          Man = char.MaleChar(NotList = [sManAdj], 
                                   bAllowRelate = False, bAllowSpecies = False, bAllowMaritalStatus = False, 
                                   bAllowGang = False, bAllowTitle = False, bAllowNation = False, bAddEndNoun = False)

          sMate = ""
          if CoinFlip():
               sMate = MateAdjs1.GetWord() + " " + MateAdjs2.GetWord() + " " + MateNouns.GetWord()
          else:
               sMate = MateAdjs1.GetWord() + " " + MateNouns.GetWord()
          
          iRand = randint(1,2)
          if iRand == 1:
               sTweet += "I Was " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc + " " + ManNouns.GetWord())
          elif iRand == 2:
               sTweet += "I Was " + WordList(["Sold","Gifted","Mated","Bound","Betrothed","Promised","Married","Bred"]).GetWord() + " as " + AddArticles(sMate) + "\nto\n" + AddArticles(sManAdj + " " + Man.Desc + " " + ManNouns.GetWord())
          # else:
               # sTweet += "I Was " + WordList(["Pledged","Trained"]).GetWord() + " as " + AddArticles(sMate) + "\nfor\n" + AddArticles(sManAdj + " " + Man.Desc)

          return sTweet     
     
# His for the Fisting:
# A Submissive Nubile Black Flight-Attendant Story     
class Generator78(TitleGen):
     def __init__(self):
         super().__init__(ID = 78, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()

     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","lesbian"]

          Gerunds = WordList(["69ing","Ass-Eating","Bedding","Binding","Breaking",
                              "Breeding","Caning","Claiming","Deflowering",
                              "Defiling","Dominating","Fingering","Fisting",
                              "Impregnating","Milking","Motor-Boating",
                              "Paddling","Peeing On","Penetrating","Pleasuring",
                              "Porking","Pumping","Rimming","Sharing",
                              "Shaving","Spanking","Spit-Roasting",
                              "Stripping","Stuffing","Taking","Tea-Bagging",
                              "Whipping","Using","Video-Taping"])

          SubAdjs = WordList(["Submissive","Submissive","Subservient",
                              "Compliant","Obedient","Kinky"])

          sSubAdj = SubAdjs.GetWord()
          Girl = char.FemaleChar(MaxChars = 22, TempType = TempType.Medium, 
                                 ExclList = [GenModFemale, AttitudeFemale, SexualityFemale],
                                 NotList = [sSubAdj])
          
          sTweet = "HIS FOR THE " + Gerunds.GetWord().upper() + "\n"
          sTweet += AddArticles(sSubAdj + " " + Girl.Desc, bMakeUpper = True) + " Story"
          return sTweet     
          
class Generator79(TitleGen):
     def __init__(self):
         super().__init__(ID = 79, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","lesbian"]
          
          VerbsTo = WordList(["69","Anally Deflower","Bone","Chain Up","Claim","Claim Hard","Command","Deflower",
                                   "Degrade","Dominate","Enslave","Gag","Hotwife","Humiliate","Hypnotize","Impregnate",
                                   "Knock-Up","Lick","Master","Mind Control","Motor-Boat","Mount Roughly","Paddle",
                                   "Pee On","Penetrate","Pervert","Possess","Publicly Expose","Punish","Ride Hard","Shave",
                                   "Splooge On","Suck On","Take From Behind","Tame","Tea-Bag","Wife-Swap","Undress",
                                   "Use Sexually","Video-Tape"])

          SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
          sSubAdj = SubAdjs.GetWord()
          Girl = char.FemaleChar(MaxChars = 22, TempType = TempType.Medium, 
                                 NotList = [sSubAdj])
          
          sTweet = "HIS TO " + VerbsTo.GetWord().upper() + "\n"
          sTweet += AddArticles(sSubAdj + " " + Girl.Desc, bMakeUpper = True) + " Story"

          return sTweet     
          
# NOTE: Similar to 81
class Generator80(TitleGen):
# I Lost My Virginity
# to 
# A Tanned Leather Cowboy 
    def __init__(self):
        super().__init__(ID = 80, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["man"]
        self.ExclTemplateTags = ["men"]
          
        ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])

        Man = char.MaleChar(MaxChars = 30, bAddAnArticle = True, bAllowGang = False,
                            NotList = ManNotList, 
                            ExclList = [SpeciesMale,MaritalStatusMale,TitlesMale,GenModMale])

        if CoinFlip():
            sTweet = "I Lost My Virginity\n"
            sTweet += "To\n" + Man.Desc + "!"
        else:
            sTweet = "I Got My Cherry Popped\n"
            sTweet += "By\n" + Man.Desc + "!"

         
        return sTweet    
          
# I Lost My Virginity
# to 
# A Tanned Leather Cowboy 
# in 
# The Bathroom at CVS
class Generator81(TitleGen):
    def __init__(self):
        super().__init__(ID = 81, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate3()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["man"]
        self.ExclTemplateTags = ["men"]
          
        ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
        Places = WordList(["at\nThe Bowling Alley","in\nThe Produce Section", "in\nThe Baked Goods Section","in\nThe Bakery",
            "Behind the Chic-fil-a", "in the Ball Pit","Behind a Bench in the Park","at\nThe Beach","Under\nAn Overpass",
            "On\nThe Eliptical Machine at the Gym","In\nThe Locker Room Showers","at\nThe Seafood Restaurant","at\nThe Museum",
            "at\nThe Library","at\nThe Farmer's Market","next to\nThe Duck Pond","in\nThe Back of a Church","On\nTop of the Bar",
            "in\nThe Window Display of a Shoe Store","Under\nThe Boardwalk","in\nThe Hunting Section at a Wal-Mart",
            "in\nThe Church Graveyard","in\nA White Van Under an Overpass","at\nThe Construction Site","next\nto the Assembly Line",
            "on\nA Hotel Balcony","in\nA Room at a Motel 6","in\nmy Parent's Bedroom","at\nThe Pet Store","Beside\nThe Bike Path",
            "Behind the Bleachers","Behind\nThe Bar","In\nThe Back Seat of a Prius","In\nThe Back of a Ford 150",
            "In\nThe Back Seat of a Volvo","In\nThe Back of a Movie Theater"
            ])
        Retailers = WordList(["In-n-Out Burger","Whole Foods","Wal-Mart","Starbucks","Gold's Gym","LA Fitness","Krispy Kreme",
                                    "CVS","Target","Chipotle","Burger King","the Mall","IHOP","the Multiplex","an Apple Store"])
          
        Man = char.MaleChar(MaxChars = 24, bAddAnArticle = True, bAllowGang = False, 
                            ExclList = [SpeciesMale,MaritalStatusMale,TitlesMale,GenModMale],
                            NotList = ManNotList)

        if CoinFlip():
            sTweet = "I Lost My Virginity\n"
            sTweet += "To\n" + Man.Desc + "\n"
        else:
            sTweet = "I Got My Cherry Popped\n"
            sTweet += "By\n" + Man.Desc + "\n"
          
        iRand = randint(1,5)
          
        if iRand == 1:
            sTweet += "In\nThe " + WordList(["Men's Room","Women's Restroom","Parking Lot"]).GetWord() + " " 
            sTweet += "At " + Retailers.GetWord()
          
        elif iRand == 2:
            sTweet += Places.GetWord()
          
        elif iRand == 3:
            sTweet += "and\n" + WordList(["Two","Two","Three","Three","Four","Five","Seven","Nine","Twelve","Thirteen","Twenty"]).GetWord() + " of His Buddies!"
          
        elif iRand == 4:
            iInches = randint(8,12)
            sTweet += "Who Used\n" + WordList(["A Cucumber","A Banana","An Eggplant","An Electric Toothbrush",
                            "A " + str(iInches) + "\" Black Dildo",
                            "A " + str(iInches) + "\" Steel Dildo"]).GetWord() + " On Me!"
        elif iRand == 5:
            sTweet += WordList(["And It Was\nLive on Television!",
                                "And It Was\nLive on the Internet!",
                                "And\nHe Gave Me $100!",
                                "And\nMy Dad Was Pissed When He Found Out!",
                                "And\nI Let His Friends Watch!",
                                "And\nA Cop Caught Us!",
                                "And\nHe Filmed the Whole Thing!",
                                "In\nThe Basement of His Parents House!",
                                "And\nHe Didn't Pull Out!",
                                "And\nHe Did My Ass Too!",
                                "And\nHis Sexy Wife!",
                                "And\nNow I'm Pregnant!"]).GetWord()

        return sTweet     
          
# "I'm a Pregnant Asian Waitress
# and
# I'm Stripping 
# For a Well-Hung Millionaire Sheikh!" (alt: I'm a pregnant asian waitress: what am I doing stripping for...??)
class Generator82(TitleGen):
     def __init__(self):
         super().__init__(ID = 82, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sInnocentAdj = WordList(titmisc.NiceGirlGoodAdjs().List + ["Sweet"]).GetWord()
          
          GirlNotList = ['MILF','Older','Fertile','Slave Girl','Bikini Model','HuCow','Supermodel',
                              'Harem Princess','Penthouse','Slave',sInnocentAdj]
          Girl = char.FemaleChar(NotList = GirlNotList, Type = GirlType.Good, bAllowAttitude = False, 
                                        bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, 
                                        bAllowNation = True, bAllowGenMod = False, bAllowClothing = False, 
                                        bAllowPhysChar = False, bAllowSexuality = False, bAllowMaritalStatus = False)

          ManNotList = ['Shape-Shifting']
          Man = char.MaleChar(NotList = ManNotList, bAddAnArticle = True, bAllowGang = False, bAllowRelate = False, 
                                   bAllowAttitude = True, bAllowSpecies = False, bAllowSkinHairColor = True, 
                                   bAllowTitle = False, bAllowNation = True)
          
          Actions = WordList(["Stripping for","Posing Naked for","Taking Naked Pics for",
                                    "Undressing for","Playing Doctor with","Playing 'Naughty Nurse' with",
                                    "Giving a Full Frontal Massage to","Taking My Clothes Off for",
                                    "Getting Naked for","Dancing Naked for","Modeling Erotic Lingerie for",
                                    "Giving a Nude Massage to","Giving a Nude Lap Dance to","Pole Dancing Naked for",
                                    "Being Handcuffed to a Bed by","Being Bent Over and Paddled by",
                                    "Getting My Bare Bottom Spanked by","Twerking Naked for",
                                    "Getting a full frontal massage from","Giving Head to",
                                    "Cleaning House Naked for","Getting Naked in the Hot-tub with",
                                    "Showering Naked with","Rubbing Baby Oil on the Naked Body of a",
                                    "Getting Oil Poured All Over My Naked Body by"])
          
          sTweet = "\"I'm " + AddArticles(sInnocentAdj + " " + Girl.Desc)
          sTweet += "!\n" + "What Am I Doing " + Actions.GetWord() + "\n"
          sTweet += Man.Desc + "?\""

          
          return sTweet     
          
#The Virgin Christian Redheaded Librarian
#Tries an Interracial Threesome
class Generator83(TitleGen):
    def __init__(self):
        super().__init__(ID = 83, Priority = GenPriority.Normal)
        self.Template = templates.TitleTemplate4()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["couple","gay"]
          
        GirlNotList = ["black","african","ebony","dark-skinned"]
        NiceGirl = char.FemaleChar(SelectTemplateID = 501, NotList = GirlNotList)
        while len(NiceGirl.Desc) > 28:
            NiceGirl = char.FemaleChar(SelectTemplateID = 501, NotList = GirlNotList)
          
        sArticle = "The"
        if FoundIn(NiceGirl.Desc, ["sister","brother","mom","dad","mother",
                                   "father","fiancé","wife","girlfriend",
                                   "teacher","secretary","daughter",
                                   "babysitter","governess","tutor",
                                   "bride"]):
                sArticle = "My"

        NaughtyStuff = WordList(["69", "an Anal Hook","Anal Sex","BBC","BDSM","a Butt Plug","a Clit Clamp",
                                 "a Dirty Sanchez","Double Penetration","Erotic Asphyxiation",
                                 "an Interracial Threesome", "Leather Bondage","a Lesbian Threesome",
                                 "Fisting","Nipple Clamps","Stripping at a Club","a Threesome",
                                 "Watching Hardcore Porn","Butt Stuff","Anal Fisting","Pee Drinking",
                                 "Water Sports","Whips and Chains","Wife Swapping","Anal Beads",
                                 "Getting Her Clit Pierced","Eating Ass","Ass-to-Ass","a Clit Pump",
                                 "an Ass Vibe","a 12 inch Steel Dildo","Deep Throating","Bukkake"])
        Extras = WordList(["with the Pope","with the Dalai Lama","with Miss America","with Her Step-Dad",
                                "with Her Step-Mom","with Her Step-Brother","with Her English Teacher",
                                "with Her Gym Coach","with Her Guidance Counselor","with Her Literature Professor",
                                "with Her Gynecologist","at the Zoo","in a Starbucks Restroom",
                                "in Her Parents Bedroom","in the Locker Room","at College","with Her Best Friend",
                                "with Her Tinder Date","at the Aquarium","with Her SCUBA Partner",
                                "with a Police Officer","with a 65-Year-Old Man","with Her Lab Partner",
                                "on the Coffee Table","on the Dining Room Table","on the Hotel Balcony",
                                "with a Total Stranger"])
        sTryVerb = "Tries"
        if sArticle == "My":
            sTryVerb = "Tried"

        sTweet = sArticle + " " + NiceGirl.Desc + "\n" 
        sTweet += sTryVerb + " " + NaughtyStuff.GetWord() 
        if CoinFlip():
            sTweet += "\n" + Extras.GetWord() + "!"

        return sTweet     
          
# Busty Princess Sophie
# Gets Tea-Bagged by the Goat Men
class Generator84(TitleGen):
     def __init__(self):
         super().__init__(ID = 84, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          AdjNotList = ['Small-Town','Sun-Baked','Tanned','Natural','Succubus','Eager','Hot','Bronzed']
          SpecialAdjs = ['MILF','Virgin','Young','Teenage','Teen','Nubile','Supermodel','Submissive','Party Girl',
                              'Goth','Tomboy','Schoolgirl','Co-ed','Daddy\'s Girl','BBW','Pixie','Chocolate','Wealthy',
                              'Wealthy','Millionaire','Stuck-up','Haughty','Snooty','Snobbish','Rich','Bashful',
                              'Blushing']
          Adjs = WordList(SpecialAdjs + titmisc.AttitudeGoodFemale().List + titmisc.NationFemale().List + titmisc.PhysCharFemale().List + titmisc.SkinHairColorFemale().List + titmisc.SpeciesFemale().List)
          Titles = WordList(['Princess','Princess','Princess','Heiress','Heiress','Queen','Duchess','First Lady','Lady',
                                   'Countess','Contessa'])
          VerbsBy = WordList(['Tea-Bagged','Paddled','Peed On','Used','Stripped in Public','Deflowered',
                                   'Anally Deflowered','Fisted','Anal Fisted','Beaten with a Belt','Enslaved',
                                   'Claimed in Public','Dominated in the Dungeon','Impregnated','Knocked Up',
                                   'Imprisoned in the Sex Dungeon','Milked','Motor-Boated','Mounted Bareback',
                                   'Paddled','Shaved','Pounded','Spanked','Spanked in Public','Spanked with a Belt',
                                   'Publically Whipped','Caught on Video','Gagged','Ball-Gagged','Ridden Bareback',
                                   'Deep Throated','Her Ass Eaten','Her Nipples Pierced','Her Clit Pierced',
                                   'Penetrated','Her Titties Sucked','Bound and Whipped','Bent Over','Spread-Eagled'])
          GangVerbs = WordList(['Peed On','Used','Bukkaked','Deflowered','Anally Deflowered',
                                   'Impregnated','Knocked Up','Imprisoned in the Sex Dungeon','Mounted Bareback',
                                   'Paddled','Pounded','Spanked','Spanked in Public','Ridden Bareback',
                                   'Double Penetrated','Triple Penetrated','Spit-Roasted','Bukkaked','Shared',
                                   'Gang-Banged','Bound and Whipped'])
          MaleNotList = ['Business Man','Charming','Sensitive']
          Master = char.MaleChar(bAddTheArticle = True, sPosArticle = "Her", NotList = MaleNotList, bAllowGang = False,
                                        bAllowTitle = False, bAllowRelate = True)
          Gang = char.GangMaleChar(bAddTheArticle = True, sPosArticle = "Her", NotList = MaleNotList)
          
          if CoinFlip():
               sTweet = self.HerName + " the " + Adjs.GetWord(NotList = AdjNotList) + " " + Titles.GetWord() + "\n"
          else:
               sTweet = Adjs.GetWord(NotList = AdjNotList) + " " + Titles.GetWord() + " " + self.HerName + "\n"
               
          if CoinFlip():
               sTweet += "Gets " + VerbsBy.GetWord() + " by " + Master.Desc
          else:
               sTweet += "Gets " + GangVerbs.GetWord() + " by " + Gang.Desc

          return sTweet     

class Generator85(TitleGen):
     def __init__(self):
         super().__init__(ID = 85, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
          
          Man = char.MaleChar(bAddAnArticle = True, NotList = ManNotList, bAllowGang = False, 
                                   bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = False,
                                   bAllowClothing = False)

          if CoinFlip():
               sTweet = "I Lost My Virginity\n"
               sTweet += "to " + Man.Desc + "\n"
          else:
               sTweet = "I Got My Cherry Popped\n"
               sTweet += "by " + Man.Desc + "\n"
          
          sTweet += WordList(["Live on Television!","Live on the Internet!","And He Gave Me $100!",
                                        "And My Dad Was Pissed When He Found Out!","And I Let His Friends Watch!",
                                        "And " + WordList(["a Cop","My Dad","the Principal","a Teacher","My Step-Brother","a Stranger"]).GetWord() + " Caught Us!",
                                        "And We Filmed the Whole Thing!","And Now I'm So Sore I Can Hardly Walk!",
                                        "And His Dad!","And His Boss!","And I Came 6 Times!","And He Came All Over My Tits",
                                        "And He Didn't Pull Out!","And He Did My Ass Too!","And Then My Parents Came Home!",
                                        "And His Sexy Wife!","And Now I'm Pregnant!","Who Used To Be A Woman!",
                                        "And I Don't Even Know His Name!","And Some Guy Paid To Watch Us Do It!"]).GetWord()

          return sTweet     
          
# I Shared My Innocent Asian Wife 
# with 
# A Well-Hung Beefy Fighter Pilot!
class Generator86(TitleGen):
     def __init__(self):
         super().__init__(ID = 86, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ManNotList = ["Space","Gladiator","Knight","Viking","Warrior","Shape-Shifting","Ghost"]
          WomanNotList = ["Wife","Girlfriend","Fiancé","Virgin","Harem","Slave Girl","Damsel"]
          
          Man = char.MaleChar(bAddAnArticle = True, NotList = ManNotList, bAllowGang = False, 
                                   bAllowMaritalStatus = False, bAllowTitle = False, bAllowGenMod = False)
          Girl = char.FemaleChar(Type = GirlType.Good, NotList = WomanNotList, bAddEndNoun = False,
                                        bAllowSpecies = False, bAllowMaritalStatus = False, bAllowTitle = False)
          
          sTweet = "\"I Shared My " + Girl.Desc + " Wife\n"
          sTweet += "With " + Man.Desc
          
          if CoinFlip():
               sTweet += "\n" + WordList(["And She Let Me Watch","And I Haven't Seen Her Since","And She Let Him Do Butt Stuff",
                                                  "And They Filmed the Whole Thing to Show Me", "And Now She Can't Get Enough",
                                                  "And Now She's Insatiable","And It Turned Her Into A Wanton Slut",
                                                  "And She Says He's Bigger Than I Am","On Our Annivesary",
                                                  "As a Special Valentine's Day Gift","And Next Time It's My Turn",
                                                  "And He Sent Me The Pictures","And Now She's Pregnant",
                                                  "And They Let Me Watch","We Met At The Bar","We Found On Craigslist",
                                                  "Who Has a BDSM Sex Dungeon","On Her Birthday","And That Was a Big Mistake",
                                                  "And He Paid Us $10,000"]).GetWord()
          
          sTweet += "!\""
          
          return sTweet     
          
# Filming My Step-Son's Rich Bitch Wife
# In the Shower
# class Generator87(TitleGen):
     # ID = 87
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Last Night a Sexy Dominatrix (Honey, A Sexy Dominatrix)
# Forced Me 
# To Eat Her Ass 
class Generator88(TitleGen):
     def __init__(self):
         super().__init__(ID = 88, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Actions = WordList(["Forced Me\nTo Eat Her Ass","Spanked Me\nWith a Steel Paddle",
                                   "Whipped Me\nWith a Riding Crop","Dressed Me In Women's Lingerie\nAnd Whipped My Ass",
                                   "Dressed Me In Women's Lingerie\nAnd Made Me Wear a Ball Gag",
                                   "Tied Me to the Bed Naked\nAnd Took Pics","Handcuffed Me\nAnd Whipped My Ass",
                                   "Forced Me\nTo Eat Her Out","Rode My Face","Smothered Me With Her Ass",
                                   "Spanked Me\nWith a Wooden Paddle","Beat Me\nWith a Wooden Spoon",
                                   "Made Me Wear Nipple Clamps","Made Me Wear a Ball Gag",
                                   "Made Me Wear a Gimp Mask","Made Me\nEat Her Panties","Cuffed Me to My Bed",
                                   "Rode Me\nWith a Strap-On","Used a Strap-On\nOn My Ass",
                                   "Made Me\nWear Women's Lingerie","Made Me\nDrink Her Pee",
                                   "Made Me\nEat Her Ass","Spanked Me\nIn Assless Chaps",
                                   "Tied Me To the Bed And Put Nipple Clamps On Me",
                                   "Dominated Me\nWith Her Ass","Dominated Me\nIn Her Sex Dungeon",
                                   "Made Me\nWear a Butt Plug","Smothered Me With Her Huge Ass"])
          
          GirlNotList = ['Desperate','Willing','Little','Fashionable','Anal Virgin','Slave']
          Girl = char.FemaleChar(bAddAnArticle = True, NotList = GirlNotList,
                                      bAllowAge = False, bAllowMaritalStatus = False, bAllowPregState = False, 
                                      bAllowRelate = False, bAllowSexuality = False, bAllowTitle = False)
                                   
          sTweet = "Last Night\n" + Girl.Desc + "\n" + Actions.GetWord()

          return sTweet     
          
# Sweet Little Sophie 
# The Country Virgin Schoolgirl
# and the
# Swollen 8" Purple Dick
class Generator89(TitleGen):
     def __init__(self):
         super().__init__(ID = 89, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          SweetAdjs = WordList(['Sweet', 'Sweet', 'Cute', 'Blonde','Innocent','Bashful','Naive'])
          NiceNames = WordList(['Amy','Angelica','Annie','Charity','Daisy','Daphne','Elsie',
                                     'Emmy','Frances','Gertrude','Greta','Jeanie','Lacey','Lizzy',
                                     'Mabel','Mary','Maryanne','Molly','Nancy','Nell','Olive','Phoebe',
                                     'Rosie','Shelly','Sophie','Summer','Virginia'])
                                     
          Girl = titmisc.NiceGirl()
          sNiceGirl = Girl.Desc
          
          BigAdjs = WordList(["Massive","Enormous","Girthy","Thick","Lengthy","Oversized","Stacked","Swinging",
                                   "Monstrous","Big","Giant","Hulking","Hefty","Heavy","Towering"])
          SwoleAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Hard","Erect","Stiff","Tumescent",
                                     "Fat","Bulging","Rigid","Fully Erect","Hugely Erect"])
          ExtraAdjs = WordList(["Veiny","Throbbing","Meaty","Burning","Dripping","Purple","Red","Exposed",
                                     "Fleshy","Straining","Feverish","Lustful","Passionate","Fervid","Throbbing",
                                     "Pulsating","Vigorous","Virile","Dark","Moist","Black","Rampant"])
          DickSyns = WordList(["Dick","Dick","Cock","Cock","Prick","Erection","Member","Phallus","Tool","Hard-On",
                                    "Dong","Schlong","Penis"])
          sDick = ""
          
          if CoinFlip():
               sDick = BigAdjs.GetWord() + " " + SwoleAdjs.GetWord() + " " + ExtraAdjs.GetWord() + " " + DickSyns.GetWord()
          else:
               sDick = SwoleAdjs.GetWord() + " " + str(randint(8,12)) + "-inch " + ExtraAdjs.GetWord() + " " + DickSyns.GetWord()

          sTweet = SweetAdjs.GetWord() + " Little " + NiceNames.GetWord() + "\n"
          sTweet += "The " + sNiceGirl + "\nand the " + WordList(["Case of the","Tale of the","Adventure of the","Secret of the","Curse of the"]).GetWord() + "\n"
          sTweet += sDick 
          
          return sTweet     
     
# A Big Day for Veronica:
# The Nubile Nympho Teen Slut 
# Gets Anal Fisted 
class Generator90(TitleGen):
     def __init__(self):
         super().__init__(ID = 90, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotGirlList = ["Harem Princess"]
          Girl = char.FemaleChar(Type = GirlType.Bad, NotList = NotGirlList, bAllowSpecies = False)
               
          sHerName = NamesFemale().FirstName()
          
          sTweet = "A Big Day for " + sHerName + ":\n"
          sTweet += "The " + Girl.Desc + "\n"
               
          iRand = randint(1,13)
          if iRand < 3:
               ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
                                "Throbbing","Meaty","Burning","Dripping","Purple","Red","Fleshy","Lustful","Passionate",
                                "Throbbing","Pulsating","Vigorous","Virile","Moist","Black","Stiff","Girthy"])
               sTweet += "Gets a " + ErectAdjs.GetWord() + " " + str(randint(8,12)) + "\" Surprise"
          elif iRand == 3:
               sTweet += "Makes Her First " + WordList(["Lesbian","Hardcore","Anal","Gangbang","Creampie","Bondage"]).GetWord() + " Porno"
          elif iRand == 4:
               sTweet += "Gets Her " + WordList(["Nipples","Clit","Labia","Taint","Ass Dimples"]).GetWord() + " Pierced"
          elif iRand == 5:
               Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
               "at the Chic-fil-a","in the Ball Pit","at the Park","at the Beach","Under an Overpass","at the Gym",
               "on the Eliptical Machine at the Gym","at the Seafood Restaurant","at the Museum","at Burger King",
               "at the Library","at the Farmer's Market","next to the Duck Pond","at Church","at the Bar",
               "in the Window Display of a Shoe Store","at Wal-Mart","at Starbucks","at School","on Campus",
               "in the Church Graveyard","at a Construction Site","at Rush Hour Traffic","at Her Uber Driver",
               "on a Hotel Balcony","Beside the Bike Path","at the Mail Man","at the Amazon Delivery Guy",
               "Behind the Bleachers","In the Back of a Ford 150","In a Movie Theater","at Chipotle","at Barnes & Noble",
               "at Whole Foods","at the Mall","at the CVS"
               ])
               sTweet += "Flashes Her " + WordList(["Tits","Ass","Pussy"]).GetWord() + " " + Places.GetWord()
          elif iRand == 6:
               sTweet += "Has Her First " + WordList(["Threesome","Foursome","Fivesome","Orgy","Gang Bang","Black Gang Bang"]).GetWord()
          elif iRand == 7:
               sTweet += "Has a " + WordList(["Dick","Cock","Penis","Prick"]).GetWord()
          elif iRand == 8:
               sTweet += "Tries a Glory Hole"
          elif iRand == 9:
               sTweet += "Gets " + WordList(["Fisted","Anal Fisted","Bukkake'd","Double-Penetrated","Spit-Roasted",
                                                    "Blindfolded and Whipped","Shared with Strangers"]).GetWord()
          elif iRand > 10 and iRand < 12:
               sTweet += WordList(["Gets"]).GetWord() + " " 
               sTweet += WordList(["Her Neighbor's","Her Step-Brother's","Her Professor's","Her Teacher's","Her Boss's",
                                        "Her Step-Dad's","Her Uncle's","Her Gym Coach's","Her Gynecologist's","A Stranger's"]).GetWord() + " "
               sTweet += WordList(["Dick","D","Cock","Hard Cock","Fat Dick","Dingus","Meat Stick","Flesh Pole","Fat Boner"]).GetWord()
          else: 
               sTweet += "Tries " + WordList(["a Butt Plug","an Anal Hook","Nipple Clamps","a Ball Gag","a Clit Clamp",
                                                            "Crotchless Panties","a Strap-On","a Remote-Controlled Vibrator",
                                                            "Anal Beads"]).GetWord()

          return sTweet     
          
# I Spent the Night With
# A Buff Well-Hung Mossad Agent
# And a Sexy Cheerleader Stripper!
class Generator91(TitleGen):
     def __init__(self):
         super().__init__(ID = 91, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Prefix = WordList(["I Spent the Night with","I Slept with","I Showered with","I Went Down on","I Made Love to",
                                   "I Was Pleasured by","I Got Pounded by","I Was Taken Passionately by",
                                   "I Was Mounted from Behind by","I Had Sex With","I Shared a Night of Passion with",
                                   "I Had a Steamy Affair with", "I Had an Affair with","I Spent a Wild Night with",
                                   "I Shared a Night of Lust with","I Had a Forbidden Affair with",
                                   "I Had a Secret Affair with","I Was Ridden Hard by"])
          
          ManAdjNotList = ['Fine','Naked','Clever','Highly Eligible','Visibly Erect','Bare-Chested']
          ManAdjs = WordList(titmisc.AttitudeMale().List + titmisc.SkinHairColorMale().List + titmisc.NationMale().List + titmisc.PhysCharMale().List + titmisc.DickCharMale().List + ['Older','Married','Heavily-Tattooed','Naked'])
          if CoinFlip():
               sMan = ManAdjs.GetWord(NotList = ManAdjNotList) + " " + titmisc.ProfMale().GetWord()
          else:
               sManAdj1 = ManAdjs.GetWord(NotList = ManAdjNotList)
               sManAdj2 = ManAdjs.GetWord(NotList = ManAdjNotList + [sManAdj1])
               sMan = sManAdj1 + " " + sManAdj2 + " " + titmisc.ProfMale().GetWord()
          
          WomanAdjNotList = ['Little','Natural','Desperate','Moist','Wet','Narrow-Waisted','Flat-Chested','Revealing']
          WomanAdjs = WordList(titmisc.PhysCharFemale().List + titmisc.AttitudeBadFemale().List + ['Older','Pregnant','Cougar','Insatiable','Submissive','Dominant','European','Bisexual','Open-Minded','Pregnant','Teenage','Eager','Nympho','Naughty','Sexy','Horny','Well-Endowed'])
          sWoman = WomanAdjs.GetWord(NotList = WomanAdjNotList) + " " + WordList(['Wife','Girlfriend']).GetWord()
          
          sTweet = "\"" + Prefix.GetWord() + "\n" + AddArticles(sMan) + "\nand his " + sWoman + "!\""

          return sTweet     
          
# "I Gave A Naked Italian Airline Stewardess
# A Full Frontal Massage!"
# class Generator92(TitleGen):
     # ID = 92
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Veronica Puts On Latex (Leather/A Butt Plug):
# Let the Hotwife Games Begin! (Bondage/BDSM/Dominatrix)
# class Generator93(TitleGen):
     # ID = 93
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# "I'm a Stay-at-Home Mommmy Blogger
# And A Billionaire Biker
# Spooned Me Hard!"
# class Generator94(TitleGen):
     # ID = 94
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Welcome to Pound Town, Miss Dixon!
class Generator95(TitleGen):
     def __init__(self):
         super().__init__(ID = 95, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate8()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Suffixes = WordList(["berg","berg","ville","ville","town"," Town"," City"])
          sLastName = ""
          sLastName = InnuendoLastNames().GetWord() 
          
          if CoinFlip():
               #For a woman
               self.ExclTemplateTags = ["gay"]
               Prefixes = WordList(["Drill","Fuchs","Cocks","Pound","Ball","Dix","Pricks","Shafts","Bawl","Cox","Pecker",
                                         "Bang","Peen","Swallow","Pork"])
                                         
               sTweet = "“Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", " + WordList(["Miss","Mrs"]).GetWord() + " " + sLastName + "!\""
          else:
               #For a man
               self.ExclTemplateTags = ["lesbian"]
               Prefixes = WordList(["Beaver","Boob","Ass","Buttes","Kuntz","Slutt","Fuchs","Tits","Brest","Blow","Suck",
                                         "Bang","Anal","Muff","Pork","Booty"])
               sTweet = "“Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", Mr. " + sLastName + "!\""                

          return sTweet     
          
# NOTE: Female version of Gen 132
class Generator96(TitleGen):
# In Love With
# My Innocent Amish Maid's 
# Enormous Coconuts 
     def __init__(self):
         super().__init__(ID = 96, Priority = GenPriority.AboveAverage)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay"]
          
          Girl = titmisc.NiceGirl(NotList = ['Wife','Girlfriend'])
          SizeAdj = WordList(['Enormous','Gigantic','Titantic','Humongous','Massive','Sumptuous','Milky','Giant',
                                   'Honking','Juicy','Jiggling','Double D','Magnificent','Gargantuan','Jumbo',
                                   'Heavenly'])
          Breasts = misc.TittySlang()
                                   
          sTweet = WordList(["In Love with","Falling for","Head-Over-Heels for","Captivated by",
                                 "Bewitched by","Entranced by","Enraptured by","Spellbound by"]).GetWord()
          sTweet += " my " + Girl.Desc + "'s "
          sTweet += SizeAdj.GetWord() + " " + Breasts.GetWord()

          return sTweet     

# The Secretary 
# is wearing
# a butt plug          
class Generator97(TitleGen):
     def __init__(self):
         super().__init__(ID = 97, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate7()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          self.ReqTemplateTags = ["woman"]
          
          Accessories = WordList(['a Butt Plug','Anal Beads','Nipple Clamps','a Clit Clamp','a Strap-On',
                                        'an Anal Hook','a Remote-Controlled Vibrator','Crotchless Panties',
                                        'Edible Panties','Nipple Pasties','a Pony Tail Butt Plug',
                                        'Assless Chaps','a Ball Gag','a Rubber Fetish Mask','a Latex Body Suit',
                                        'a Rubber Fetish Suit','a Transparent Bikini','a Chastity Belt'])
          
          Lady = char.FemaleChar(SelectTemplateID = 1, TempType = TempType.Medium, bAddTheArticle = True)

          sTweet = Lady.Desc + "\nIs Wearing " + Accessories.GetWord() + "!"

          return sTweet     
          
class Generator98(TitleGen):
     def __init__(self):
         super().__init__(ID = 98, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sHerName = NamesFemale().FirstName()
          
          NaughtyStuff = WordList(["Does Nipple Play with","Gets Fisted by","Tries Bukkake with","Jerks Off",
                                         "Tries Forced Feminization with","Gets Spanked by", "Tries Hardcore Bondage with",
                                         "Tries Water-Sports with","Sixty-Nines","Gets Erotically Asphyxiated by",
                                         "Does Anal with","Does Butt Stuff with","Gets Anal Fisted by",
                                         "Tries Double Penetration with","Deep Throats","Gets Tea-Bagged by",
                                         "Tries Triple Penetration with","Gets a Dirty Sanchez from",
                                         "Gets Whipped By","Gets Hotwifed to","Gags On","Gets Her Ass Eaten by",
                                         "Gives a Rim-Job to","Has Twincest with","Tries Leather Bondage with",
                                         "Gets Peed on by"])
                                         
          MaleAdjs = WordList(titmisc.PhysCharMale().List + titmisc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','D.I.L.F.','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
          Species = WordList(["Unicorn","Centaur","Werewolf","Merman","Dragon","Goat Man","Dwarf",
                                   "Space Alien","Tentacle Monster","Pirate","Trapeze Artist","Clown", 
                                   "Sumo Wrestler","Were-Horse","Werewolf","Dinosaur", "Dinosaur",
                                   "Vampire","Martian","Contortionist","Warlock","Minotaur",
                                   "Reverse Centaur","Male Porn Star","Pirate Captain","Giant",
                                   "Green Beret","Navy SEAL","Priest","Biker","Male Model","Unicorn",
                                   "Rodeo Clown","Astronaut","Ghost","Zombie"])
                                   
          sTweet = sHerName + "\n" + NaughtyStuff.GetWord() + "\n"
          sTweet += AddArticles(MaleAdjs.GetWord() + " " + Species.GetWord())

          return sTweet     
          
class Generator99(TitleGen):
     def __init__(self):
         super().__init__(ID = 99, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sHerName = NamesFemale().FirstName()
          
          NaughtyStuff = WordList(["Does Nipple Play with","Gets Fisted by","Tries Bukkake with","Jerks Off",
                                         "Tries Forced Feminization with","Gets Spanked by", "Tries Hardcore Bondage with",
                                         "Tries Water-Sports with","Sixty-Nines","Gets Erotically Asphyxiated by",
                                         "Does Anal with","Does Butt Stuff with","Gets Anal Fisted by",
                                         "Tries Double Penetration with","Deep Throats","Gets Tea-Bagged by",
                                         "Tries Triple Penetration with","Gets a Dirty Sanchez from",
                                         "Gets Whipped By","Gets Hotwifed to","Gags On","Gets Her Ass Eaten by",
                                         "Gives a Rim-Job to","Has Twincest with","Tries Leather Bondage with",
                                         "Gets Peed on by"])
                                         
          MaleAdjs = WordList(titmisc.PhysCharMale().List + titmisc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','D.I.L.F.','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
          Species = WordList(["Unicorn","Centaur","Werewolf","Merman","Goat Man","Dwarf",
                                   "Space Alien","Tentacle Monster","Pirate","Trapeze Artist","Were-Horse",
                                   "Werewolf","Dinosaur", "Dinosaur","Vampire","Martian","Contortionist",
                                   "Warlock","Minotaur","Reverse Centaur","Giant","Unicorn",
                                   "Ghost","Zombie"])
          Jobs = WordList(['Airline Pilot','Astronaut','Assassin','Athlete','Attorney','Body Builder',
                                   'Bodyguard','Boxer','Brain Surgeon','Bull Rider','Business Man',
                                   'Chippendales Dancer','CIA Agent','Coal Miner','Construction Worker',
                                   'Cop','Cowboy','Defensive Lineman','Doctor','Fashion Photographer',
                                   'FBI Agent','Fighter Pilot','Fighter Pilot','Fire Fighter',
                                   'Green Beret','Gunslinger','Gym Coach','Surgeon','Hitman',
                                   'Investment Banker','Killer-for-Hire','Lawyer','Long Haul Trucker',
                                   'Lumberjack','Male Escort','Male Model','Male Nurse','Matador',
                                   'MI5 Agent','Mossad Agent','MMA Fighter','Navy Seal','Pirate',
                                   'Preacher','Priest','Private Eye','Professor','Quarterback',
                                   'Rock Guitarist','Rodeo Clown','Sailor','Secret Agent',
                                   'Secret Service Agent','Sheriff','Deputy','Snowboarder','Spy',
                                   'Stockbroker','Stuntman','Sumo Wrestler','Surfer','Tattoo Artist','Trucker',
                                   'Porn Star','Biker','Contortionist'])
                                   
          sTweet = sHerName + "\n" + NaughtyStuff.GetWord() + "\n"
          sTweet += AddArticles(Species.GetWord() + " " + titmisc.ProfMale().GetWord())

          return sTweet     

# I Secretly Impregnated 
# My Nudist Mommy-Blogger Sister-in-Law!          
class Generator100(TitleGen):
     def __init__(self):
         super().__init__(ID = 100, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate7()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay", "men", "women", "lesbian"]
          
          GirlAdj = WordList(titmisc.PhysCharFemale().List + ['Fertile','Naked','Sassy','Saucy','Sexy','Black','Ebony','Bisexual'])
          GirlNoun = WordList(titmisc.ProfGoodFemale().List + titmisc.SpeciesFemale().List)
          Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
                                   "Daughter-in-Law","Cousin"])
                         
          
          sTweet = "I Secretly Impregnated\nMy " 
          if CoinFlip():
               FemRelate = char.FemaleChar(SelectTemplateID = randint(8,9),NotList = ['wife','girlfriend','Fiancé','concubine'], MaxChars = 32)
               sTweet += FemRelate.Desc
          else:
               FemRelate = char.FemaleChar(SelectTemplateID = randint(8,9),NotList = ['sister','mom','mother'], MaxChars = 32)
               MaleRelate = WordList(["Best Friend's","Step-Father's","Dad's","Boss's","Neighbor's"])
               sTweet += MaleRelate.GetWord() + " " + FemRelate.Desc

          return sTweet     
          
# Butt Stuff 
# With My 
# Biology Professor (Spanish Teacher / Math Tutor)
# class Generator101(TitleGen):
     # ID = 101
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
     
# Backdoor Lovin'
# for the 
# Jiggling Farmer's Daughter     
class Generator102(TitleGen):
     def __init__(self):
         super().__init__(ID = 102, Priority = GenPriority.AboveAverage)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","lesbian","women"]
          
          GirlAdjs = WordList(['Amish','Country','Small-Town','Young','Nubile','Naive','Newlywed','Virginal',
                                    'Virgin','Chaste','Conservative','Submissive','Christian','Mormon','Blushing',
                                    'Bashful','Sheltered','Shy','Wholesome','All-American','Geeky','Sweet',
                                    'Country','Willing','Jiggling','Busty','Curvy','Horny','Naughty','Slender',
                                    'Adventurous','Blossoming','Skinny','Flat-Chested','Round-Bottomed'])
                                    
          GirlTropes = WordList(['Babysitter','Cheerleader','Co-ed','House Maid','Housewife','Librarian',
                                        'Milk Maid','Nanny','Nun','3rd Grade Teacher','1st Grade Teacher','Teacher',
                                        '5th Grade Teacher','Waitress','Stay-at-Home Mom','Maiden','Girl','Lady',
                                        'Southern Bell','Farmer\'s Daughter','Pastor\'s Wife','Wife','Prom Queen',
                                        'Beauty Queen','Virgin','Nurse'])
          
          sTweet = "Backdoor Lovin'\n"
          if CoinFlip():
               sTweet += "for the\n"
               if CoinFlip():
                    sAdj1 = GirlAdjs.GetWord()
                    sTweet += sAdj1 + " " + GirlTropes.GetWord(NotList = [sAdj1])
               else:
                    sAdj1 = GirlAdjs.GetWord()
                    sAdj2 = GirlAdjs.GetWord(NotList = [sAdj1])
                    sTweet += sAdj1 + " " + sAdj2 + " " + GirlTropes.GetWord()
          else:
               sAdj1 = GirlAdjs.GetWord()
               GirlNotList = ['Girl','Lady','Pastor\'s Wife','Farmer\'s Daughter','Babysitter','House Maid',
                                   'Wife','Prom Queen','Teacher','Nurse', 'Milk Maid', sAdj1]
               sTweet += "For My\n" + sAdj1 + " " + GirlTropes.GetWord(NotList = GirlNotList) + " " + WordList(["Step-Daughter","Daughter-in-Law","Sister-in-Law","Step-Sister","Step-Mom","Mother-in-Law","MILF","House Maid","Wife","Bride","Babysitter","Teacher","Nurse"]).GetWord()

          return sTweet     
          
# My Mother-in-Law is 
# A Tanned Cheerleader 
# and I Got Her Pregnant!
class Generator103(TitleGen):
     def __init__(self):
         super().__init__(ID = 103, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate3()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay", "lesbian", "women"]
          
          Girl = char.FemaleChar(bAllowAttitude = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowAge = False)
          Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
                                   "Daughter-in-Law","Cousin"])
                              
          sTweet = "My " + Relate.GetWord() + "\nis\n"
          sTweet += AddArticles(Girl.Desc, bMakeUpper = True) + ",\n"
          sTweet += "and\n" + WordList(["I Got Her Pregnant","I Got Her Pregnant","I Knocked Her Up"]).GetWord() + "!"

          return sTweet     
          
# Claimed on the Coffee Table
# by a Burly Centaur Sailor
class Generator104(TitleGen):
     def __init__(self):
         super().__init__(ID = 104, Priority = GenPriority.AboveAverage)
         self.Template = templates.TitleTemplate6()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","men","lesbian","women"]
          
          Verbs = WordList(['Claimed','Claimed Forcefully','Claimed Hard','Deflowered','Impregnated','Knocked Up',
                                   'Motor-Boated','Mounted','Paddled','Pleasured','Ravished','Ravished','Satisfied',
                                   'Taken','Taken Forcefully','Taken From Behind','Taken Roughly'])
          Location = WordList(['On the Coffee Table','On the Bathroom Floor','On the Kitchen Counter',
                                    'In the Back Seat','On a Park Bench','On the Washing Machine',
                                    'Under a Jungle Gym','On a Merry-Go-Round','On an Elliptical Machine',
                                    'On a Treadmill','On a Trampoline','In a Kiddie Pool','On a See-Saw',
                                    'On the Dining Room Table','On an Ikea Futon'])
          ManNotList = ['Single']
          Man = char.MaleChar(bAddAnArticle = True, bAllowGang = False, 
                              bAllowTitle = False, MaxChars = 32)
          
          sTweet = Verbs.GetWord() + "\n" + Location.GetWord() + "\nby " + Man.Desc

          return sTweet     

# Brigitte Gets Claimed by 
# The Well-Hung Naked Manor Lord 
# On the Back of a Horse          
class Generator105(TitleGen):
     def __init__(self):
         super().__init__(ID = 105, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Adjs = WordList(['Lustily','Vigorously','Ardently','Passionately','From Behind','Fearlessly',
                              'Fervently','Forcefully','Repeatedly','Anally'])
          GirlNames = WordList(['Alice','Alina','Amelia','Anastasia','Anna','Anabel','Beatrice','Belle',
                                     'Brigitte','Carmina','Charity','Chastity','Clover','Colette',
                                     'Constance','Cordelia','Daphne','Delilah','Delores','Eleanor',
                                     'Elizabeth','Emma','Esmerelda','Estelle','Felicia','Felicity',
                                     'Fiona','Greta','Isabelle','Josephine','Juliette','Lilah','Margaret',
                                     'Mary','Molly','Morgan','Nell','Olive','Ophelia','Rosaline','Rose',
                                     'Saffron','Sarah','Sophie','Violet'])
          MaleNouns = WordList(['Barbarian','Warrior','Knight','Bandit','Highwayman','Prince','Duke',
                                        'Paladin','Monk','Rogue','Thief','Warlock','Hunter','Swordsman','Soldier',
                                        'Troubador','Woodsman','Blacksmith','Manor Lord','Marquis','Baron','Pirate',
                                        'Nobleman','Ruffian','Knave','Wizard','Sorcerer','Viking Warrior',
                                        'Crusader','Cavalier'])
          Suffixes = WordList(['On the Back of a Horse','In the Ruins of a Castle','In the Castle Dungeon',
                                    'On Top of a Hay Stack','Behind the Chicken Coop','Behind the Cow Shed',
                                    'While her Entire Village Watches','On the Back of a Horse',
                                    'and His Band of ' + str(randint(3,20)) + ' Merry Men',
                                    'and His Band of ' + str(randint(3,20)) + ' Merry Men',
                                    'and He Doesn\'t Pull Out!','Even Though She\'s a Nun',
                                    'Even Though She\'s a Virgin','In the Enchanted Forest',
                                    'And Then By His Brother','In the Royal Bedchamber',
                                    'In the Castle Privy','In the Great Hall','Using a Magic Spell',
                                    'Using a Broomstick','Wearing a Leather Condom Atop His Cock',
                                    'On the Back of a Donkey','Using Forbidden Sex Magic',
                                    'in a Turnip Field','in the Village Church','in a Monastary',
                                    'and They Live Happily Ever After','and She Finds It Quite Agreeable',
                                    'Who is Secretly the King','In the Smithy','In the Tannery',
                                    'And He Doth Pleasure Her Greatly','And Verily! she is Well Satisfied',
                                    'While a Unicorn Watches','On the Deck of a Pirate Ship',
                                    'In the Old Castle Ruins','After They Meet on Tinder',
                                    'With a Very Comely Cock','Using a Leather Condom for Protection',
                                    'Using a Magical Vibrating Steel Phallus','In the Nunnery',
                                    'Wearing an Enchanted Cock Ring','After He Saves Her From a Flame-Breathing Dragon',
                                    'After He Saves Her From Marrying the Evil Prince'])
                                    
          ManNotList = ['S.W.A.T. Team','Cyborg','Alien','Single','Taboo','Bareback','Millionaire',
                              'Trillionaire','Gazillionaire','CEO','Billionaire','Hipster']
          Man = char.MaleChar(bAddEndNoun = False, bAddTheArticle = True, NotList = ManNotList, sPosArticle = "Her",
                                   bAllowAge = False, bAllowProf = False, bAllowNation = False, bAllowTitle = False, 
                                   bAllowMaritalStatus = False)
          sDesc = Man.Desc.strip()
          
          sTweet = "Lady " + GirlNames.GetWord() + " is Claimed " + Adjs.GetWord() + "\n"
          sTweet += "by " + sDesc + " " + MaleNouns.GetWord()
          sTweet += "\n" + Suffixes.GetWord()

          return sTweet     

# Lady Belle is Claimed Repeatedly
# by The Tattooed Oiled-Up Barbarian          
class Generator106(TitleGen):
     def __init__(self):
         super().__init__(ID = 106, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Adjs = WordList(['Lustily','Vigorously','Ardently','Passionately','From Behind','Fearlessly',
                              'Fervently','Forcefully','Repeatedly','Anally'])
          GirlNames = WordList(['Alice','Alina','Amelia','Anastasia','Anna','Anabel','Beatrice','Belle',
                                     'Brigitte','Carmina','Charity','Chastity','Clover','Colette',
                                     'Constance','Cordelia','Daphne','Delilah','Delores','Eleanor',
                                     'Elizabeth','Emma','Esmerelda','Estelle','Felicia','Felicity',
                                     'Fiona','Greta','Isabelle','Josephine','Juliette','Lilah','Margaret',
                                     'Mary','Molly','Morgan','Nell','Olive','Ophelia','Rosaline','Rose',
                                     'Saffron','Sarah','Sophie','Violet'])
          MaleNouns = WordList(['Barbarian','Warrior','Knight','Bandit','Highwayman','Prince','Duke',
                                        'Paladin','Monk','Rogue','Thief','Warlock','Hunter','Swordsman','Soldier',
                                        'Troubador','Woodsman','Blacksmith','Manor Lord','Marquis','Baron','Pirate',
                                        'Nobleman','Ruffian','Knave','Wizard','Sorcerer','Viking Warrior',
                                        'Crusader','Cavalier'])
                                    
          ManNotList = ['S.W.A.T. Team','Cyborg','Alien','Single','Taboo','Bareback','Millionaire',
                              'Trillionaire','Gazillionaire','CEO','Billionaire','Hipster']
          Man = char.MaleChar(bAddEndNoun = False, bAddTheArticle = True, NotList = ManNotList, sPosArticle = "Her",
                                   bAllowAge = False, bAllowRelate = False, bAllowProf = False, 
                                   bAllowTrope = True, bAllowNation = False, bAllowTitle = False, 
                                   bAllowMaritalStatus = False)
          sDesc = Man.Desc.strip()
          
          sTweet = "Lady " + GirlNames.GetWord() + " is Claimed " + Adjs.GetWord() + "\n"
          sTweet += "by " + sDesc + " " + MaleNouns.GetWord()

          return sTweet     
          
# Claimed at Castle Tittyfuck
class Generator107(TitleGen):
     def __init__(self):
         super().__init__(ID = 107, Priority = GenPriority.High)
         self.Template = templates.TitleTemplate5()
     
     def WordCombiner(self, sFirstWord, sSecWord):
          sCombined = ""
          
          if len(sFirstWord) > 2 and len(sSecWord) > 2:
               if sFirstWord[-2:-1] == sFirstWord[-1:] and sFirstWord[-1:] == sSecWord[0]:
                    # if the last two characters of the first word are the same and they are the same as the second word, remove one 
                    sCombined = sFirstWord[:-1] + sSecWord
               elif sFirstWord[-2:] == "er" and sSecWord[-2:] == "er":
                    # if both words end in 'er', remove the first 'er'
                    sCombined = sFirstWord[:-2] + sSecWord
               elif sFirstWord[-1:] == "a" and sSecWord[0] == "a":
                    # if the first word ends in 'a' and the second word begins with it, remove one
                    sCombined = sFirstWord[:-1] + sSecWord
               elif sFirstWord[-1:] == "r" and sSecWord[0] == "r":
                    # if the first word ends in 'r' and the second word begins with it, remove one
                    sCombined = sFirstWord[:-1] + sSecWord
               else:
                    sCombined = sFirstWord + sSecWord 
          else:
               sCombined = sFirstWord + sSecWord
               
          return sCombined
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["fantasy"]
          
          Prefix = WordList(["Claimed\nat", "Enslaved\nat", "Taken\nat", "Imprisoned\nat", "Claimed\nat","The Dungeons\nof",
                                   "The Halls\nof","The Prisoner\nof","The Princess\nof","The Master\nof","The Baron\nof",
                                   "Deflowered\nat","Despoiled\nat","Ravished\nat","Seduced\nat","The Knight\nof",
                                   "The Lady\nof","The Virgins\nof","The Baroness\nof","The Dutchess\nof",
                                   "Naked\nat","The Harem Girls\nof","The Maidens\nof","The Queen\nof",
                                   "The Mistress\nof","The Wizard\nof","Betrayed\nat"])
          
          FirstNouns = WordList(["cock","cunt","puss","vaj","slut","twat","spunk","prick","butt","tit",
                                   "squirt","scrotum","taint","bum","face","cunny","labia","bitch","clit","cum",
                                   "ball","sack","breast","meat","fuck","anus","sphincter","lip","shaft",
                                   "rack","prick","wang","milk","maiden","splooge","popper","sucker","crotch",
                                   "titty","milf","dick","lady","fudge","anal","wife","sex","cooch","gagging",
                                   "groping","coitus","pissing","shafting","man","cherry","cream","coochy",
                                   "hoar","sucking","anus","rimming"])
          SecNouns = WordList(["cocks","cunts","puss","boobs","sluts","twats","spunk","pricks","butts",
                                   "tits","titties","squirts","taints","fucker","bitch","clits","slits","cum",
                                   "balls","sacks","meat","fucks","sphincter","lips","shafts","rack","wangs",
                                   "milk","maidens","splooge","popper","sucker","crotch","sucker","milf","dicks",
                                   "thrust","eater","swallow","head","spreader","groper","licker","humper","sex",
                                   "bottom","cooch","rider","flower","girth","hymen","wood","boner","wood",
                                   "wood","rump","cream","cooter","hoar","nut","tongue","rimmer"])
          Adjs = WordList(["hard","wet","great","fat","pink","uber","fucker","good","thick","porn",
                                   "bound","bone","dinky","young","teen","spread","stiff","tight",
                                   "deep","black","dark","long","moist","gay","cuck","sex",
                                   "loose","sweet","steel","hard","dark","black","good","iron","harder"])
          Verbs = WordList(["fuck","bang","spunk","smash","piss","cum","grope","squeeze","spurt","rut","pound",
                                   "wank","milk","suck","splooge","bone","slap","thrust","rub","swallow","cuck",
                                   "hump","screw","schtup","bonk","jill","gag","wanna","nut","spank","suck"])
          
          sTweet = Prefix.GetWord() + "\nCastle "
          
          sWord1 = ""
          sWord2 = ""
          
          iRand = randint(1,5)
          if iRand == 1:
               sWord1 = FirstNouns.GetWord()
               sWord2 = Verbs.GetWord(NotList = [sWord1])
          elif iRand == 2:
               sWord1 = FirstNouns.GetWord()
               sWord2 = SecNouns.GetWord(NotList = [sWord1])
          elif iRand == 3:
               sWord1 = Adjs.GetWord()
               sWord2 = FirstNouns.GetWord(NotList = [sWord1])
          elif iRand == 4:
               sWord1 = Adjs.GetWord()
               sWord2 = SecNouns.GetWord(NotList = [sWord1])
          elif iRand == 5:
               sWord1 = Verbs.GetWord()
               sWord2 = "alot"
          elif iRand == 6:
               sWord1 = Adjs.GetWord()
               sWord2 = Verbs.GetWord(NotList = [sWord1])
          else:
               sWord1 = Verbs.GetWord()
               sWord2 = FirstNouns.GetWord(NotList = [sWord1])
               
          sTweet += self.WordCombiner(sWord1, sWord2).capitalize()
               
          return sTweet     
     
# The Buxom Irish Waitress
# Makes Love to a Pirate!     
class Generator108(TitleGen):
     def __init__(self):
         super().__init__(ID = 108, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate12()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          self.ReqTemplateTags = ["woman","man"]
          
          FemAdjNotList = ['Naked','Nudist', 'Bare-Shaven','Anal','Polynesian','Japanese','Brazilian',
                               'Elvish']
          Girl = char.FemaleChar(SelectTemplateID = 17, bAddTheArticle = True, NotList = FemAdjNotList)
          Man = char.MaleChar(bAllowGang = False, bAddTheArticle = True, TempType = TempType.Medium, bAllowRelate = False)
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(["Makes Love to","Is Ravished by","Jumps into Bed with","Gets Bedded by","Spends the Night with",
                                   "Has a Wild Night of Passion with","Has a Forbidden Affair with","Is Claimed by"]).GetWord() + " " 
          sTweet += Man.Desc + "!"

          return sTweet     

# The Modest Swedish Cheerleader
# Does a Naughty Strip-Tease          
class Generator109(TitleGen):
     def __init__(self):
         super().__init__(ID = 109, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(SelectTemplateID = 17, bAddTheArticle = True, NotList = FemNotList)
          
          sTweet = Girl.Desc + "\n"
          sTweet += "Does " + AddArticles(SexyAdjs.GetWord()) + " Strip-Tease"

          return sTweet     
          
# The Innocent Plump Teacher
# Deep Throats Al
# and also Steve
# AND Chuck
# not-to-mention Lenny, Will and Zeke!          
class Generator110(TitleGen):
     def __init__(self):
         super().__init__(ID = 110, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Nude','Elvish']
          Girl = char.FemaleChar(SelectTemplateID = 17, bAddTheArticle = True, NotList = FemNotList)
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless'])
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(["Goes Down on","Bends Over for","Drops Her Panties for","Spreads her Ass Cheeks for",
                                   "Gets Naked for","Blows","Gives a Handjob to","Lubes Herself Up for",
                                   "Flashes her Titties at","Flashes her Coochie at","Pulls Down her Top for",
                                   "Shaves Her Muff for","Dry Humps","Twerks her ass for","Twerks Her Bare Ass for",
                                   "Gets Claimed Hard by","Gets Taken From Behind by","Does an Erotic Dance for",
                                   "Takes Naked Pictures For","Makes a Sex-Tape With","Deep Throats",
                                   "Spreads Her Legs For","Sucks Her Own Titties for","Gets Her Bare Bottom Paddled by",
                                   "Wears a Remote Vibrator for","Gets Tied Up and Spread for",
                                   "Gets Finger-Banged by","Loses Her Virginity to","Showers Naked with",
                                   "Gets a Pearl Necklace from","Takes Nude Selfies for",
                                   "Plays With Her Titties for","Gives a Rim-Job to","Gets a Facial from",
                                   "Gives a Tit-Job to","Gives Head to","Makes Sweet, Sensual Love to",
                                   "Has Loving, Passionate Sex with","Shares Her Nubile Young Body with",
                                   "Jerks Off","Does Doggy Style with","Shares Her Breast Milk with",
                                   "Gets Pounded Hard from Behind by","Shows Her Breast Implants to"]).GetWord() + " " 
          sName1 = PlainNamesMale().FirstName()
          sName2 = PlainNamesMale().FirstName(NotList = [sName1])
          sName3 = PlainNamesMale().FirstName(NotList = [sName1,sName2])
          sName4 = PlainNamesMale().FirstName(NotList = [sName1,sName2,sName3])
          sName5 = PlainNamesMale().FirstName(NotList = [sName1,sName2,sName3,sName4])
          sName6 = PlainNamesMale().FirstName(NotList = [sName1,sName2,sName3,sName4,sName5])
          
          sTweet += sName1
          sTweet += "\nand also " + sName2
          
          if CoinFlip():
               sTweet += "\nAND " + sName3
               if CoinFlip():
                    sTweet += "\nnot-to-mention " + sName4 + ", " + sName5 + " and " + sName6
               
          sTweet += "!"

          return sTweet     

# The Bosomy Jewish Teacher
# Wrestles Another Woman Naked!          
class Generator111(TitleGen):
     def __init__(self):
         super().__init__(ID = 111, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(SelectTemplateID = 17, bAddTheArticle = True, NotList = FemNotList)
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(["Wears a Butt Plug","Wears an Anal Hook","Sixty-Nines Another Woman",
                                  "Does Butt Stuff","Tries Out a Sex Swing","Scissors a Hot Lesbian",
                                   "Learns How to Deep Throat","Gives Head Through a Glory Hole",
                                   "Attends an Orgy","Gets Fisted","Gets an Enema",
                                   "Gets Her Anal Cherry Popped","Takes Off Her Clothes on Stage",
                                   "Wrestles Another Woman Naked","Gets Tied Up and Spread",
                                   "Goes to Class Naked","Goes to Work Naked","Has Anal Sex"]).GetWord() + "!"

          return sTweet     

# My Tight-Bodied Russian Secretary
# Isn't Wearing Any Panties!          
class Generator112(TitleGen):
     def __init__(self):
         super().__init__(ID = 112, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate23()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["man"]
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(Type = GirlType.Good, SelectTemplateID = 16,
                                 #bAllowTropes = False,
                                 #ReqList = [ProfFemale],
                                 #ExclList = [SpeciesFemale,TitlesFemale],
                                 NotList = FemNotList)
          
          sTweet = "My " + Girl.Desc + "\n"
          sTweet += "Isn't Wearing Any Panties!"

          return sTweet     
          
# A Wholesome Amish Babysitter
# Eats Out Jasmine          
class Generator113(TitleGen):
     def __init__(self):
         super().__init__(ID = 113, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList, bAddAnArticle = True)
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(['Scissors','Eats Out','Fists','Finger Bangs','Goes Down On','Seduces',
                                   'Eats Out','Showers Naked With','Gives a Rim-Job to','Plays With Her Titties For',
                                   'Grinds On','Humps','Gives a Nude Frontal Massage to','Tribs','Fngers',
                                   'Has ' + SexyAdjs.GetWord() + ' Lesbian Sex With']).GetWord(NotList = ['Sexy']) + " "
          sTweet += self.HerName 
               
          return sTweet     

# My Classy Eastern European Housewife
# Is Wearing a Butt Plug!          
# --- Very similar to 124
class Generator114(TitleGen):
     def __init__(self):
         super().__init__(ID = 114, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList)
          
          sTweet = "My " + Girl.Desc + "\n"
          sTweet += "Is Wearing " + WordList(['a Strap-On','a Latex Bodysuit','a Chainmail Bikini','a Thong',
                                                       'a Micro Bikini','a Butt Plug','Nipple Clamps',
                                                       'Crotchless Panties','Assless Chaps','a Ponytail Butt Plug',
                                                       'a Ball Gag','a Sheer Bodystocking','a Fishnet Bodystocking',
                                                       'a Chastity Belt','a Leather Bustier','Sexy Lingerie',
                                                       'a Remote-Controlled Vibrator','Nipple Clamps',
                                                       'a Cupless Leather Corset','a See-thru Dress',
                                                       'a Dog Collar','a Leash','a Seethru Bikini']).GetWord() + "!"

          return sTweet     
          
# The Perky Flight Attendant
# Plays Tackle Football Naked!
class Generator115(TitleGen):
     def __init__(self):
         super().__init__(ID = 115, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList, bAddTheArticle = True)
          
          sTweet = Girl.Desc + "\n"
          sTweet += "Plays " 
          if CoinFlip():
               sTweet += WordList(['Nude','Naked','Strip']).GetWord() + " " 
               sTweet += WordList(["Football","Volleyball","Volleyball","Basketball","Soccer","Frisbee",
                                        "Capture the Flag","Twister","Tennis","Baseball","Quidditch",
                                        "Poker"]).GetWord() + "!"
          else:
               sTweet += WordList(["Football","Volleyball","Volleyball","Basketball","Soccer","Golf","Frisbee",
                                        "Capture the Flag","Hide-and-Seek","Twister","Tennis","Water Polo","Rugby",
                                        "Curling","Lacrosse","Baseball","Quidditch","Roller Derby",
                                        "Tackle Football"]).GetWord() + " "
               sTweet += WordList(['Nude','Naked']).GetWord() + "!"
               
          return sTweet     

# My Flirty Italian Milk Maid
# Is A Wanton Hotwife!
class Generator116(TitleGen):
     def __init__(self):
         super().__init__(ID = 116, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude','Schoolgirl','Teen']
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList)
          
          sTweet = "My " + Girl.Desc + "\n"
          sTweet += "Is " + AddArticles(WordList(['Willing','Wanton','Open-Minded','Naughty','Adventurous',
                                                            'Horny','Sexy','Lustful','Experienced','Excited',
                                                            'Fertile','Shameless']).GetWord()) + " Hotwife!" 

          return sTweet     
          
# A Big-Titty German Waitress
# Urinates on Dick!
class Generator117(TitleGen):
    def __init__(self):
        super().__init__(ID = 117, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate12()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["gay","lesbian","couple"]
          
        FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
        Girl = char.FemaleChar(SelectTemplateID = 16, bAddAnArticle = True,
                               NotList = FemNotList)
          
        sTweet = Girl.Desc + "\n"
        sTweet += WordList(['Pees on','Fists','Paddles','Whips','Ties Up',
                            'Pegs','Uses a Steel Dildo on',
                            'Uses a Riding Crop on','Takes a Shit on',
                            'Urinates on','Chokes','Forcibly Feminizes',
                            'Poops on','Handcuffs',
                            'Puts a Leash and Dog Collar on','Spanks']).GetWord() + " " 
        sTweet += self.HisName + "!"

        return sTweet     
     
# I Found Out I Was a Lesbian
# When an Oiled-Up Flight Attendant Ate My Ass      
class Generator118(TitleGen):
    def __init__(self):
        super().__init__(ID = 118, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate14()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman"]
        self.ExclTemplateTags = ["gay","man"]
          
        CharNotList = ['Uptight','Virgin','Male Model','Quarterback','Male Stripper','Camp Counselor','Business Man','Slave',
                       'Defensive Lineman','Virtuous']
        Lesbian1 = char.LesbianChar(bAddAnArticle = True, NotList = CharNotList,
                                    ExclList = [MaritalStatusFemale, SexualityFemale, PregState, TitlesFemale])
        Girl = char.FemaleChar(bAddAnArticle = True, Type = GirlType.Good, 
                                 MaxChars = 30, NotList = CharNotList,
                                 ExclList = [SpeciesFemale])
        
        sTweet = "I Found Out I Was a Lesbian\n"
        sTweet += "When " + Girl.Desc 
        sTweet += "\n" + WordList(["Ate My Ass", "Ate Me Out", "Ate My Pussy", 
                                   "Licked My Snatch","Scissored Me",
                                   "Rode My Face","Rode Me With a Strap-On", 
                                   "Fisted Me", "Fisted My Butt",
                                   "Sucked My Tits","Ate Out My Snatch", 
                                   "Rimmed My Butthole","Sucked My Titties"]).GetWord()
                                           
        return sTweet     
          
# The Nubile Teen Starlet
# Gets an Enema
class Generator119(TitleGen):
     def __init__(self):
         super().__init__(ID = 119, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate23()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman","ass"]
          
          GirlNotList = ['Single','Slave','Nude','Naked','Tanned']
          Girl = char.FemaleChar(bAddTheArticle = True, Type = GirlType.Good, 
                                 MaxChars = 20, NotList = GirlNotList,
                                 ExclList = [SpeciesFemale])
          
          sTweet = Girl.Desc + "\ngets an enema!"

          return sTweet     

# NOTE: Haven't quite figured out how to make this funny with cover pics
class Generator120(TitleGen):
# The Randy Hairy Vegan Gunslinger Multi-Billionaire
# Gets An Enema   
     def __init__(self):
         super().__init__(ID = 120, Priority = GenPriority.Lowest, Disabled = True)
         self.Template = templates.TitleTemplate23()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man","single"]
          #self.ExclTemplateTags = ["woman","women","men"]
          
          GuyNotList = ['Naked','Dwarf','Centaur']
          Guy = char.MaleChar(bAddTheArticle = True, MaxChars = 20,
                              bAllowGang = False, NotList = GuyNotList,
                              ExclList = [TitlesMale,SpeciesMale])
          
          sTweet = Guy.Desc + "\ngets an enema!"

          return sTweet     
          
# Massaging Mrs. Mountcox:
# A Sadistic Bisexual MILF Story
class Generator121(TitleGen):
     def __init__(self):
         super().__init__(ID = 121, Priority = GenPriority.Low, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Gerunds = WordList(['Blackmailing','Dominating','Enslaving','Fisting','Hot-Dogging','Licking',
                                   'Massaging','Milking','Mind Controlling','Motor-Boating','Motor-Boating',
                                   'Mounting','Paddling','Riding','Rimming','Sixty-nining','Showering With',
                                   'Showering With','Spanking','Stripping','Undressing','Videoing',
                                   'Whipping','Filling','Drilling','Pounding','Servicing','Satisfying',
                                   'Nailing','Caning','Humping'])
                                   
          MILFNotList = ['Virgin','Virginal','Maiden','Chaste','Sheltered','Sparkling','Straight','Spirited',
                            'Sweet','Virtuous','Anal Virgin','Angelic','Small-Town Girl','Tomboy','Lesbian',
                            'Little','Schoolgirl','gymnast']
          MILF = char.FemaleChar(SelectTemplateID = 223, NotList = MILFNotList)
                                   
          sTweet = Gerunds.GetWord() + " Mrs. " + AuthorLastNames().GetWord() + ":\n"
          sTweet += "My " + MILF.Desc + " " + WordList(['Liason','Encounter','Rendevous','Affair','Adventure']).GetWord()

          return sTweet     
          
# Speculum for the Horny Mexican MILF
class Generator122(TitleGen):
    def __init__(self):
         super().__init__(ID = 122, Priority = GenPriority.High)
         self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]

          NaughtyStuff = WordList(['Anal Beads','Anal Hook','Ball Gag','Butt Plug','Clit Clamp','Clit Pump',
                                         'Steel Dildo','12-inch Dildo','Double-Ended Dildo','Gimp Mask',
                                         'Nipple Clamps','Pearl Necklace','Sex Swing','Spreader Bar','Speculum',
                                         'Strap-On','Sybian','Anal Dildo','Anal Vibe','Butt Stuff','Fisting',
                                         'Anal Fisting','Bondage Play','Dog Collar','Chastity Belt',
                                         'Pony Play','Ponytail Anal Plug','Horse Whip','Gang Bang',
                                         'Public Nudity'])
                                         
          MILFNotList = ['Virgin','Virginal','Maiden','Chaste','Sheltered','Sparkling','Straight','Spirited',
                              'Sweet','Virtuous','Anal Virgin','Angelic','Small-Town Girl','Tomboy','Lesbian',
                              'Little','Schoolgirl','gymnast']
          MILF = char.FemaleChar(SelectTemplateID = 223, NotList = MILFNotList,
                                 bAddTheArticle = True, bSplitArticle = True)
                                   
          sTweet = NaughtyStuff.GetWord() + "\nfor " + MILF.Desc 

          return sTweet     

# Lady Constance is Claimed Vigorously
# by The Gruff Hairy Well-Hung Manor Lord
# at Bonkalot Keep          
class Generator123(TitleGen):
     def __init__(self):
         super().__init__(ID = 123, Priority = GenPriority.Lowest, Disabled = True)
     
     def WordCombiner(self, sFirstWord, sSecWord):
          sCombined = ""
          
          if len(sFirstWord) > 2 and len(sSecWord) > 2:
               if sFirstWord[-2:-1] == sFirstWord[-1:] and sFirstWord[-1:] == sSecWord[0]:
                    # if the last two characters of the first word are the same and they are the same as the second word, remove one 
                    sCombined = sFirstWord[:-1] + sSecWord
               elif sFirstWord[-2:] == "er" and sSecWord[-2:] == "er":
                    # if both words end in 'er', remove the first 'er'
                    sCombined = sFirstWord[:-2] + sSecWord
               elif sFirstWord[-1:] == "a" and sSecWord[0] == "a":
                    # if the first word ends in 'a' and the second word begins with it, remove one
                    sCombined = sFirstWord[:-1] + sSecWord
               elif sFirstWord[-1:] == "r" and sSecWord[0] == "r":
                    # if the first word ends in 'r' and the second word begins with it, remove one
                    sCombined = sFirstWord[:-1] + sSecWord
               else:
                    sCombined = sFirstWord + sSecWord 
          else:
               sCombined = sFirstWord + sSecWord
               
          return sCombined
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ClaimAdjs = WordList(['Lustily','Vigorously','Ardently','Passionately','From Behind','Fearlessly',
                                     'Fervently','Forcefully','Repeatedly','Anally','Brazenly'])
          GirlNames = WordList(['Alice','Alina','Amelia','Anastasia','Anna','Anabel','Beatrice','Belle',
                                     'Brigitte','Carmina','Charity','Chastity','Clover','Colette',
                                     'Constance','Cordelia','Daphne','Delilah','Delores','Eleanor',
                                     'Elizabeth','Emma','Esmerelda','Estelle','Felicia','Felicity',
                                     'Fiona','Greta','Isabelle','Josephine','Juliette','Lilah','Margaret',
                                     'Mary','Molly','Morgan','Nell','Olive','Ophelia','Rosaline','Rose',
                                     'Saffron','Sarah','Sophie','Violet'])
          MaleNouns = WordList(['Barbarian','Warrior','Knight','Bandit','Highwayman','Prince','Duke',
                                        'Paladin','Monk','Rogue','Thief','Warlock','Hunter','Swordsman','Soldier',
                                        'Troubador','Woodsman','Blacksmith','Manor Lord','Marquis','Baron','Pirate',
                                        'Nobleman','Ruffian','Knave','Wizard','Sorcerer','Viking Warrior',
                                        'Crusader','Cavalier'])
                                    
          ManNotList = ['S.W.A.T. Team','Cyborg','Alien','Single','Taboo','Bareback','Millionaire',
                              'Trillionaire','Gazillionaire','CEO','Billionaire','Hipster','Millennial',
                              'N.Y.P.D.']
          Man = char.MaleChar(bAddEndNoun = False, bAddTheArticle = True, NotList = ManNotList, sPosArticle = "Her",
                                   bAllowAge = False, bAllowRelate = False, bAllowProf = False, 
                                   bAllowTrope = True, bAllowNation = False, bAllowTitle = False, 
                                   bAllowMaritalStatus = False)
          sDesc = Man.Desc.strip()
          
          
          
          FirstNouns = WordList(["cock","cunt","puss","vaj","slut","twat","spunk","prick","butt","tit",
                                   "squirt","scrotum","taint","bum","face","cunny","labia","bitch","clit","cum",
                                   "ball","sack","breast","meat","fuck","anus","sphincter","lip","shaft",
                                   "rack","prick","wang","milk","maiden","splooge","popper","sucker","crotch",
                                   "titty","milf","dick","fudge","anal","wife","sex","cooch","gagging",
                                   "groping","coitus","pissing","shafting","man","cherry","cream","coochy",
                                   "hoar","sucking","anus","rimming"])
          SecNouns = WordList(["cocks","cunts","puss","boobs","sluts","twats","spunk","pricks","butts",
                                   "tits","titties","squirts","taints","fucker","bitch","clits","slits","cum",
                                   "balls","sacks","meat","fucks","sphincter","lips","shafts","rack","wangs",
                                   "milk","maidens","splooge","popper","sucker","crotch","sucker","milf","dicks",
                                   "thrust","eater","swallow","head","spreader","groper","licker","humper","sex",
                                   "bottom","cooch","rider","flower","girth","hymen","wood","boner","wood",
                                   "wood","rump","cream","cooter","hoar","nut","tongue","rimmer"])
          NameAdjs = WordList(["hard","wet","great","fat","pink","uber","fucker","good","thick","porn",
                                    "bound","bone","dinky","young","teen","spread","stiff","tight",
                                    "deep","black","dark","long","moist","gay","cuck","sex",
                                    "loose","sweet","steel","hard","dark","black","good","iron","harder"])
          Verbs = WordList(["fuck","bang","spunk","smash","piss","cum","grope","squeeze","spurt","rut","pound",
                                   "wank","milk","suck","splooge","bone","slap","thrust","rub","swallow","cuck",
                                   "hump","screw","schtup","bonk","jill","gag","wanna","nut","spank","suck"])

          
          sWord1 = ""
          sWord2 = ""
          
          iRand = randint(1,5)
          if iRand == 1:
               sWord1 = FirstNouns.GetWord()
               sWord2 = Verbs.GetWord(NotList = [sWord1])
          elif iRand == 2:
               sWord1 = FirstNouns.GetWord()
               sWord2 = SecNouns.GetWord(NotList = [sWord1])
          elif iRand == 3:
               sWord1 = NameAdjs.GetWord()
               sWord2 = FirstNouns.GetWord(NotList = [sWord1])
          elif iRand == 4:
               sWord1 = NameAdjs.GetWord()
               sWord2 = SecNouns.GetWord(NotList = [sWord1])
          elif iRand == 5:
               sWord1 = Verbs.GetWord()
               sWord2 = "alot"
          elif iRand == 6:
               sWord1 = NameAdjs.GetWord()
               sWord2 = Verbs.GetWord(NotList = [sWord1])
          else:
               sWord1 = Verbs.GetWord()
               sWord2 = FirstNouns.GetWord(NotList = [sWord1])
               
          sTweet = "Lady " + GirlNames.GetWord() + " is Claimed " + ClaimAdjs.GetWord() + "\n"
          sTweet += "by " + sDesc + " " + MaleNouns.GetWord() + "\n"
          
          sCastleName = self.WordCombiner(sWord1, sWord2).capitalize()
          
          sTweet += WordList(["at Castle " + sCastleName, 
                                   "at " + sCastleName + " Keep",
                                   "in the Tower of " + sCastleName,
                                   "High atop " + sCastleName + " Tower",
                                   "at " + sCastleName + " Manor",
                                   "in the Dungeons of " + sCastleName,
                                   "at " + sCastleName + " Abbey",
                                   "in the Forest of " + sCastleName,
                                   "in the Bed of " + WordList(["Count","Lord","Sir","Duke","King","Prince"]).GetWord() + " " + sCastleName]).GetWord()
               
          

          return sTweet     
          
# The Ghost of Richard Nixon
# Ploughed My Girlfriend 
class Generator124(TitleGen):
     def __init__(self):
         super().__init__(ID = 124, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate9()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","lesbian","men","women"]
          
          Undead = WordList(['Undead','The Ghost of','Zombie','Vampire','Werewolf'])
          Celebs = WordList(['Richard Nixon','JFK','Abraham Lincoln','Elvis Presley','Winston Churchill','Mahatma Gandhi',
                                   'Jim Morrison','Tupac','Buddy Holly','George Washington','Albert Einstein','Mao Zedong',
                                   'Humphrey Bogart','Babe Ruth','Colonel Sanders','Napoleon','Bela Lugosi','Groucho Marx',
                                   'Steve Jobs','Mr Rogers','Marlon Brando','Bing Crosby','Jimmy Stewart','Clark Gable',
                                   'James Dean','H.P. Lovecraft','Orson Welles','Henry Kissinger','Sonny Bono','Jimmy Hoffa',
                                   'Charlton Heston','Hugh Hefner','Yul Brynner','Carl Sagan','Yuri Gagarin','Jerry Lewis',
                                   'Benny Hill','Bob Ross','Joe DiMaggio','Don Knotts','Vincent Price','Adam West',
                                   'Frank Sinatra','Casey Kasem','Karl Marx','Jacques Cousteau','Salvador Dali',
                                   'Bob Hope', 'Tupac Shakur', 'Muhammad Ali', 'Jimi Hendrix'])
          Verbs = WordList(['Plowed','Banged','Porked','Drilled','Humped','Made Love to','Nailed','Reamed',
                                'Screwed','Shagged','Stuffed','Cream-pied','Ravished','Ate Out','Sixty-nined',
                                'Boned',])
          
          GirlNotList = ['Single','Mature Woman','Virgin','Unshaven','Maiden','Married','Recently-Divorced']
          Girl = char.FemaleChar(bAddEndNoun = False, NotList = GirlNotList, TempType = TempType.Flowery, Type = GirlType.Good,
               bAllowProf = False, bAllowPregState = False, bAllowAttitude = False, bAllowSpecies = False,
               bAllowTitle = False, bAllowMaritalStatus = False,)
          
          sTweet = Undead.GetWord() + " " + Celebs.GetWord() + "\n" + Verbs.GetWord() + "\n"
          sTweet += "My " + Girl.Desc + " " + WordList(["Wife","Wife","Girlfriend"]).GetWord() + "!"                         

          return sTweet     
          
# The Chaste Secretary
# Gets Deflowered 
# by 
# The Brawny Manly Space Dinosaur Gargoyle          
class Generator125(TitleGen):
    def __init__(self):
        super().__init__(ID = 125, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate25()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["woman","man"]

        VerbNotList = ["Sexually Harrassed At My Workplace","Cuddled"]
        sVerb2 = self.VerbsBy.GetWord(NotList = VerbNotList)

        GirlNotList = []
        NiceGirl = char.FemaleChar(SelectTemplateID = 501, NotList = GirlNotList)

        while len(NiceGirl.Desc) > 22:
            NiceGirl = char.FemaleChar(SelectTemplateID = 501, NotList = GirlNotList)

        sArticle = ""
        sVerb1 = ""
        Man = None

        if FoundIn(NiceGirl.Desc, ["sister","brother","mom","dad","mother",
                                "father","fiancé","wife","girlfriend",
                                "teacher","secretary","daughter",
                                "babysitter","governess","tutor",
                                "bride"]):
            sVerb1 = "Was"
            sArticle = "My"
          
            Man = char.MaleChar(MaxChars = 22, bAddAnArticle = True, 
                                sPosArticle = "My", bAllowRelate = True)
        else:
            sVerb1 = "Gets"
            sArticle = "The"
            Man = char.MaleChar(MaxChars = 22, bAddTheArticle = True, 
                                sPosArticle = "Her", bAllowRelate = True)
          
        sTweet = sArticle + " " + NiceGirl.Desc + "\n"
        sTweet += sVerb1 + " " + sVerb2 + " By\n"
        sTweet += Man.Desc
          
        return sTweet     
          
class Generator126(TitleGen):
     # Sitting On My Well-Hung Sumo-Wrestler Step-Dad's Face
     def __init__(self):
         super().__init__(ID = 126, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(bAddAnArticle = True, bAllowGang = False, bAllowRelate = True, sPosArticle = "Her",
                                        bAllowDickChar = False, bAllowSpecies = False)
     
          #sTweet = WordList(["Sitting on","Riding","Straddling"]).GetWord() + " " + Master.Desc + "'s Face"
          sTweet += self.HerName + " Makes Out with\n"
          sTweet += Master.Desc + " and then\n"
          sTweet += "She Sits On His Face!"
          
          return sTweet
          
# Ava Undresses for The Muscular Space Dwarf Rock Band
class Generator127(TitleGen):
    def __init__(self):
        super().__init__(ID = 127, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate13()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        if CoinFlip():
            self.ReqTemplateTags = ["woman","single"]
        else:
            self.ReqTemplateTags = ["men"]
          
        sStrip = ""
        Gang = char.GangMaleChar(bAddTheArticle = True, MaxChars = 22,
                                bAllowGenMod = False, bAllowTypeMod = False, 
                                bAllowProf = False, bAllowSpecies = False)
          
        sTweet = self.HerName + "\n" 
        sStrip = WordList(["Gets Naked for","Strips Naked for","Twerks Naked for","Undresses for",
                            "Exposes Herself to","Strips for","Shows Her Tits to","Flashes\n",
                            "Does a Strip-Tease for","Takes Her Top Off for"]).GetWord().upper()

        if sStrip[-4: ] == " FOR":
            sStrip = sStrip.replace(sStrip[-4: ], "\nfor")
        elif sStrip[-3: ] == " TO":
            sStrip = sStrip.replace(sStrip[-3: ], "\nto")

        sTweet += sStrip + "\n"
        sTweet += Gang.Desc 

        return sTweet     
          
# Penetrated 
# by 
# The Well-Endowed Dinosaur Space Men
# on Uranus!
class Generator128(TitleGen):
     def __init__(self):
         super().__init__(ID = 128, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate26()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["couple","lesbian","women"]
          
          Verbs = WordList(['Boned','Bred','Claimed','Cream-Pied','Drilled',
                            'Fisted','Humped','Mounted','Nailed','Pleasured',
                            'Plowed','Porked','Ravished','Reamed','Punished',
                            'Rimmed','Spanked','Shagged','Shaved','Stuffed',
                            'Taken','Whipped','Licked','Pegged'])
          AlienPrefixes = WordList(['Alien','Space','Space Alien'])
          AlienNouns = WordList(['Body Builders','Bull Riders','Chippendales Dancers','Coal Miners',
                                        'Construction Workers','Cops','Cowboys','Defensive Linemen','Doctors',
                                        'Fire Fighters','Frat Boys','Long Haul Truckers','Lumberjacks',
                                        'Male Escorts','Male Models','Male Nurses','Male Strippers',
                                        'Matadors','Pirates','Roadies','Rodeo Clowns','Sailors','Stuntmen',
                                        'Sumo Wrestlers','Surfers','Surgeons','Biker Gang','D.I.L.F.s','Jocks',
                                        'Billionaires','Millionaires','Sugar Daddies','Leather Daddies',
                                        'Bounty Hunters','Barbarians','Businessmen','Werewolves',
                                        'Drag Queens','Muscle Marys'])
          MaleNotList = ['Space']  
          Alien = char.GangMaleChar(SelectTemplateID = 404, NotList = MaleNotList)
          while len(Alien.Desc) > 32:
              Alien = char.GangMaleChar(SelectTemplateID = 404, NotList = MaleNotList)
          
          sTweet = Verbs.GetWord() + "\nby\n"
          sTweet += "The " + Alien.Desc 
          sTweet += "\non Uranus!"

          return sTweet     
          
# Spunky Stacked Black Barista
# for
# The Latino Viking
class Generator129(TitleGen):
     def __init__(self):
         super().__init__(ID = 129, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate27()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man","woman"]
          self.ExclTemplateTags = ["gay","lesbian"]
          
          GirlNotList = ['Call-Girl','Escort','Slave','Whore','Stripper','Green-Skinned']
          ManNotList = ['Million','Billion','Trillion','Gazillionaire']
               
          Guy = char.MaleChar(bAddTheArticle = True, TempType = TempType.Medium, 
                              ReqList = [RaceMale], 
                              ExclList = [SpeciesMale,NationMale,TitlesMale,ProfRockstarMale,RelateMale],
                              NotList = ManNotList)

          GirlNotList = GirlNotList + Guy.GetWordList()
          if 'Latino' in GirlNotList:
               GirlNotList.append('Latina')          
          
          iRand = randint(1,3)
          if iRand < 3:
          # Sexy White Girl for the Black Man
               print("<A>")
               Girl = char.FemaleChar(ReqList = [RaceFemale], 
                                      ExclList = [SpeciesFemale,SkinHairColorFemale,NationFemale,SexualityFemale], 
                                      NotList = GirlNotList)
               sTweet = Girl.Desc.upper() + "\nfor\n" + Guy.Desc
          else:
          # Black Mermaid Secretary for the Black Man
               print("<B>")
               Girl = char.FemaleChar(ReqList = [SpeciesFemale,RaceFemale], ExclList = [SkinHairColorFemale,NationFemale,SexualityFemale], NotList = GirlNotList)
               
               sTweet = Girl.Desc.upper() + "\nfor\n" + Guy.Desc

          return sTweet     
          
# Black Merman Quarterback for the White Playboy Centerfold
class Generator130(TitleGen):
     def __init__(self):
         super().__init__(ID = 130, Priority = GenPriority.Low)
         self.Template = templates.TitleTemplate27()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man","woman"]
          self.ExclTemplateTags = ["gay","lesbian"]
          
          GirlNotList = ['Call-Girl','Escort','Slave','Whore']
          ManNotList = ['Bob']
          
          Woman = char.FemaleChar(bAddTheArticle = True, TempType = TempType.Medium,
                                  ReqList = [RaceFemale],
                                  ExclList = [SpeciesFemale,RelateFemale],
                                  NotList = GirlNotList)

          ManNotList = ManNotList + Woman.GetWordList()
          if 'Latina' in ManNotList:
               ManNotList.append('Latino')
          print("ManNotList is " + str(ManNotList))
          
          iRand = randint(1,3)
          if iRand < 3:
          # Sexy White Trucker for the Black Stay-at-Home Mom
               print("<A>")
               Man = char.MaleChar(NotList = ManNotList, bAllowSpecies = False,
                                   ReqList = [RaceMale])
               sTweet = Man.Desc + "\nfor\n" + Woman.Desc
          else:
          # Black Centaur Cowboy for the Latina Flight Attendant
               print("<B>")
               Man = char.MaleChar(NotList = ManNotList, 
                                   ReqList = [SpeciesMale,RaceMale])
               sTweet = Man.Desc + "\nfor\n" + Woman.Desc


          return sTweet     
          
# I watched my wife and an Italian cowboy dinosaur make a porno!
class Generator131(TitleGen):
     def __init__(self):
         super().__init__(ID = 131, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          MaleNotList = ["Taboo"]
          FemRelative = WordList(["Sister", "Wife", "Bride", "Girlfriend", "Lesbian Bride", "Daughter", "Step-daughter",
                                         "Mother-in-Law", "Mom", "Fiancé", "Young Wife", "New Bride", "Highschool Sweetheart",
                                         "Teenage Daughter","Blushing Bride","Virgin Girlfriend","Conservative Girlfriend",
                                         "Conservative Step-Mom", "Hot Sister", "Hot Step-Sister", "Gay Dad","Gay Step-Dad",
                                         "Religious Step-Mom","Gay Husband","Gay Boyfriend","Uptight Wife", "Uptight Fiancé"]).GetWord()
               
          MalePornStar = char.MaleChar(bAllowGang = False, NotList = MaleNotList, bAddAnArticle = True,
               ExclList = [TitlesMale, AttitudeMale, MaritalStatusMale],
               bAllowProf = True, bAllowTrope = True, bAllowNation = True)
               
          sTweet = "I Watched My " + FemRelative + "\n"
          sTweet += "and " + MalePornStar.Desc + "\n"
          sTweet += "Make a Porno"
          
          return sTweet     
          
# Note: Male version of Gen 96
class Generator132(TitleGen):
# In Love With
# My Dentist's 
# Magnificent Meat-Missile
     def __init__(self):
         super().__init__(ID = 132, Priority = GenPriority.Normal)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["man","woman","couple"]

          
          Guy = WordList(['Attorney','Blind Date','Body Guard','Boss','Camp Counselor','Captain','Coach','Date',
                              'Doctor','Duke','Gym Coach','King','Marriage Counselor','Manor Lord','Mechanic',
                              'Minister','New Boyfriend','Pastor','Personal Trainer','Plumber','Priest','Pool Boy',
                              'Prince','Professor','Step-brother','Step-father','Step-son','Teacher',
                              'Divorce Attorney','Yoga Teacher','Physical Therapist','Dentist']).GetWord()
          CockSizeAdj = WordList(['Engorged','Enormous','Gigantic','Titantic','Humongous','Massive','Regal','Giant',
                                        'Big Honking','Magnificent','Gargantuan','Jumbo','Super-Sized','Lengthy','Turgid',
                                        'Pulsating','Throbbing','Rock-hard','Towering','Turgid','Tumescent','Girthy',
                                        'Donkey-Sized','Horse-Sized','King-Sized','Tumescent','XL','Arm-length',
                                        'Black','Big Black','Enormous Fucking','8-inch','10-inch','12-inch',
                                        'Handsome','Beautiful','Glistening']).GetWord()
          Cock = WordList(['Beef Bayonette','Boner','Cock','Cocksickle','Dick','Erection','Hard-on','Joystick','Knob',
                               'Meat','Meat-Missile','Member','Package','Penis','Phallus','Sausage','Schlong','Shaft',
                               'Tool','Trouser Snake','Disco Stick','Prick','Banana']).GetWord(NotList = [CockSizeAdj])
          BallSizeAdj = WordList(['Enormous','Gigantic','Grapefruit-Sized','Huge','Humungous','Jumbo',
                                        'Low-hanging','Massive','Pendulous','Swollen','Heavy','XL','XXL',
                                        'Swaying','Hairy']).GetWord()
          Balls = WordList(['Balls','Ballsack','Nuts','Scrotum','Silk Purse','Testicles']).GetWord(NotList = [BallSizeAdj])
                                   
          sTweet = WordList(["In Love With","Falling For","Head-Over-Heels For","Captivated By",
                                 "Bewitched By","Entranced By","Enraptured By","Spellbound By",
                                 "Enchanted By","Charmed By","Surprised By","Dazzled By","Flustered By",
                                 "Shook By","Overcome By","Astonished By","Breathless From",
                                 "Hypnotized By","Delighted By","Beguiled By","Transfixed By",
                                 "Seduced By","Ensorcelled By","Gaga About","Infatuated With",
                                 "Enamoured By","Swept Away By","Transfixed By"]).GetWord()
                                 
          sTweet += " My " + Guy + "'s "
          
          iRand = randint(1,3)
          if iRand == 1:
               sTweet += BallSizeAdj + " " + Balls
          else:
               sTweet += CockSizeAdj + " " + Cock

          return sTweet     
          
# Forbidden Heat
# A pseudo-incest gorilla double anal story
class Generator133(TitleGen):
     def __init__(self):
         super().__init__(ID = 133, Priority = GenPriority.High)
         self.Template = templates.TitleTemplate11()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sTitle1 = WordList(['Forbidden','Taboo','Lustful','Secret','Dirty','Naked','Sinful','Wicked',
                                   'Dangerous','Indecent','Twisted','Throbbing','Hard','Untamed',
                                   'Sexual','Steamy','Naked','Bound',
                                   'Passionate','Devil\'s','Lesbian','Sizzling','Caged','Desperate',
                                   'Cocky','Scandalous','Professional','Submissive'
                                ]).GetWord()
          sTitle2 = WordList(['Desire','Heat','Secret','Virgin','Sins','Pleasures','Temptation','Cowboy',
                                   'Lust','Release','Danger','Rendevous','Obsession','Persuasion','Embrace',
                                   'Kiss','Lovers','Passion','Daddy','Bachelor','Shame','Scoundrel',
                                   'Seduction','Surrender','Angel','Bad Boy','Possession','Climax',
                                   'Beauty','Touch','Gentleman','Princess','Flower',
                                   'Diaries','Lies','Fire','Desperado','Liason','Tease',
                                   'Secretary','Fantasy','Outlaw'
                                ]).GetWord(NotList = [sTitle1])
                                
          sSubTitle1 = WordList(['Non-Consensual','Interracial','Pseudo-Incest','Dominant','Submissive',
                                      'Twincest','Cuckold','BDSM','Lesbian','Exhibitionist','Trans','Anal']).GetWord(NotList = [sTitle1,sTitle2])
          sSubTitle2 = WordList(["Unicorn", "Centaur", "Werewolf", "Mermaid", "Merman", "Mer-MILF", "Dragon", "Orc", "Goat-Man", 
                                        "Dwarf", "Futanari", "Space Alien", "Tentacle Monster", "Clown", "Sumo Wrestler", "Were-Horse", 
                                        "Gorilla", "Dinosaur", "Dinosaur", "Velociraptor", "Zombie", "Bodybuilder","Martian",
                                        "Troll","Goblin","Vampire","Step-Dad","Dwarf","Housewife","Cheerleader","Hotwife",
                                        "Lumberjack","Biker","Viking","Gargoyle","Construction Worker","Cowboy","Fireman",
                                        "Pro-Wrestler","Priest","Luchador","Furry","Japanese Schoolgirl","Teacher","Viking",
                                        "Nun"]).GetWord(NotList = [sTitle1,sTitle2,sSubTitle1])
          sSubTitle3 = WordList(["Anal", "Double Anal", "Nipple Play", "Fisting", "Incest", "Twincest", "Threesome", 
                                      "Foursome", "Fivesome", "Bukkake", "Feminization", "Paddling", "Rope Play", 
                                      "Water-Sports", "Wife Swapping", "Sixty-Nine", "Erotic Asphyxiation", "Orgy", "Gangbang", 
                                      "Reverse Gangbang", "Milking", "Double Penetration", "Triple Penetration", 
                                      "Pee-Drinking", "Dirty Sanchez", "Sodomy", "Age Play", "BDSM", "Fisting","Toe Sucking",
                                      "Anal Fisting", "Fem-dom","Tea-Bagging","Spanking","Lactation","Cuckolding",
                                      "Cuck-Queaning","Enema","Rimming", "Leather Bondage","Public Humiliation","Cum-Drinking",
                                      "Fellatio","Choking","Glory Hole","Cum-Swapping","Analingus","Ass-Eating","Ass-to-Ass",
                                      "Menage","Lactation","Frottage"
                                      ]).GetWord(NotList = [sTitle1,sTitle2,sSubTitle1,sSubTitle2])

          sTweet = sTitle1 + " " + sTitle2 + "\n"
          sTweet += AddArticles(sSubTitle1 + " " + sSubTitle2 + " " + sSubTitle3 + " Story", bMakeUpper = True)
          
          return sTweet     
          
# Taken by her Lesbian Centaur Boss
class Generator134(TitleGen):
    def __init__(self):
        super().__init__(ID = 134, Priority = GenPriority.High)
        self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""
          
        
        if CoinFlip():
        #gay male
            self.ExclTemplateTags = ["woman","women","lesbian"]

            VerbNot = ['Impregnated','Bred','Hunted','Motor','Harrassed',
                       'Knocked','Eaten']
            sVerb = self.VerbsBy.GetWord(NotList = VerbNot)

            sTweet = sVerb + "\nby "

            Orientation = WordList(['Gay','Gay','Androgynous','Bisexual','Transgender','Otherkin',
                                            'Gender-fluid','Gender-queer','Non-Binary','Pansexual','Polysexual'])
            Species = WordList(['Alien','Alpha Wolf','Centaur','Centaur','Cyborg','Demon',
                                    'Dinosaur','Dinosaur','Dwarf','Gargoyle','Goat-Man',
                                    'Man-o-taur','MANtelope','MANticore','Mer-man','Mer-man',
                                    'Swamp Creature','Tentacle Monster','Undead',
                                    'Vampire','Vampire','Were-Horse','Were-Shark','Werewolf',
                                    'Werewolf','Zombie','Chippendales Dancer','Coal Miner',
                                    'Construction Worker','Cop','Cowboy','Farm Hand',
                                    'Football Players','Frat Boy','Gangsta','Long Haul Trucker',
                                    'Lumberjack','MMA Fighter','Sailor','Sumo Wrestler',
                                    'Millionaire','Billionaire'])
            Relations = WordList(['Blind Date','Body Guard','Boss','Camp Counselor','Coach',
                            'Doctor','Duke','Gym Coach','Marriage Counselor','Manor Lord','Mechanic',
                            'Minister','New Boyfriend','Pastor','Personal Trainer','Plumber','Priest','Pool Boy',
                            'Prince','Professor','Step-brother','Step-father','Step-son','Teacher',
                            'Divorce Attorney','Yoga Teacher','Physical Therapist','Dentist','Youth Pastor',
                            'Principal'
                            ])
            sTweet += "his\n" + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
        else:
        #lesbian female
            self.ExclTemplateTags = ["man","men","gay"]

            VerbNot = ['Impregnated','Bred','Hunted','Cream','Harrassed',
                       'Behind','Plowed','Boned']
            sVerb = self.VerbsBy.GetWord(NotList = VerbNot)

            sTweet = sVerb + "\nby "

            Orientation = WordList(['Lesbian','Lesbian','Dyke','Androgynous','Bisexual','Transgender','Otherkin',
                                            'Gender-fluid','Gender-queer','Non-Binary','Pansexual','Polysexual'])
            Species = WordList(['Elf','Fairy','Futa','Futanari','Green-Skinned Alien',
                                    'Mermaid','Mermaid','Mermaid','Nymph','Succubus','Succubus',
                                    'Vampire','Cougar','MILF','Step-Daughter',
                                    'Zombie'])
            Relations = WordList(['Teacher','English Teacher','Yoga Instructor','Nanny','Math Tutor',
                                        'Babysitter','Nurse','Piano Teacher','Biology Teacher','Personal Trainer',
                                        'Housekeeper','French Maid','Secretary','Therapist',
                                        'Gym Coach','Volleyball Coach','Nun','Nurse','Massage Therapist',
                                        'Cheerleading Captain','Secretary','Fashion Model',
                                        'Stripper','Step-Mom','Mother-in-Law','Principal','Waitress',
                                        'Manager'])
            sTweet += "her\n" + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
        return sTweet     
          
# MILKED by my biker step-son
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
     
#Ass Eating 101:
# My date with the principal
class Generator136(TitleGen):
     def __init__(self):
         super().__init__(ID = 136, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          LastNames = WordList(['Beaver',
                                     'Bell',
                                     'Bottoms',
                                     'Brown',
                                     'Butts',
                                     'Chang',
                                     'Church',
                                     'Clark',
                                     'Cox',
                                     'Cummings',
                                     'Davis',
                                     'Devlyn',
                                     'Goodbody',
                                     'Gray',
                                     'Green',
                                     'Hancock',
                                     'Hill',
                                     'Jefferson',
                                     'Johnson',
                                     'Jones',
                                     'King',
                                     'Lee',
                                     'Long',
                                     'Lopez',
                                     'Moore',
                                     'Moorecox',
                                     'Muncher',
                                     'Peach',
                                     'Pearl',
                                     'Peckwood',
                                     'Peters',
                                     'Philmore',
                                     'Popper',
                                     'Robinson',
                                     'Rogers',
                                     'Ross',
                                     'Sanderson',
                                     'Smith',
                                     'St. Claire',
                                     'Taylor',
                                     'Wang',
                                     'White',
                                     'Williams',
                                     'Wilson',
                                     'Woody'
                                   ])
          
          SexActs = WordList(['Analingus',
                                   'Anal Creampie',
                                   'Anal Fisting',
                                   'Anal Insertion',
                                   'Anal Sex',
                                  'Ass Eating',
                                   'Breast Play',
                                   'Cum Swapping',
                                   'Deep Throating',
                                   'Doggy Style',
                                   'Double Penetration',
                                   'Face-Sitting',
                                   'Fingering',
                                   'Forced Orgasm',
                                   'Giving Head',
                                   'Glory Holes',
                                   'Hand-jobs',
                                   'Hot-Dogging',
                                   'Ménage à Trois',
                                   'Motor-boating',
                                   'Muff-Diving',
                                   'Reverse Cowgirl',
                                   'Rimming',
                                   'Road Head',
                                   'Sixty-Nining',
                                   'Sodomy',
                                   'Strap-Ons',
                                   'Threesomes',
                                   'Tribbing'
                                ])

          ElderJobs = WordList(["Algebra Teacher",
                                    "Anatomy Professor",
                                    "Anatomy Teacher",
                                    "Biology Professor",
                                    "Biology Teacher",
                                    "Criminal Law Professor",
                                    "French Teacher",
                                    "Guidance Counselor",
                                    "Gym Coach",
                                    "History Teacher",
                                    "Lit Professor",
                                    "Math Teacher",
                                    "Music Teacher",
                                    "Personal Tutor",
                                    "Principal",
                                    "Professor",
                                    "Sex-Ed Teacher",
                                    "Spanish Teacher",
                                    "Women's Studies Professor"
                                 ])
          
          sTweet = SexActs.GetWord() + " 101:\n"
          sTweet += "My Date With "
          
          Dates = []
          Dates.append("My " + ElderJobs.GetWord())
          Dates.append("Mr. " + LastNames.GetWord() + ", My " + ElderJobs.GetWord(NotList = ['Professor']) + ")")
          Dates.append("Ms. " + LastNames.GetWord() + ", My " + ElderJobs.GetWord(NotList = ['Professor']))
          
          sTweet += Dates[randint(0,len(Dates) - 1)]

          return sTweet     
          
# Taken in the Graveyard by the Strapping Truck-Driver Zombie 
class Generator137(TitleGen):
     def __init__(self):
         super().__init__(ID = 137, Priority = GenPriority.Lowest, Disabled = False)
         self.Template = templates.TitleTemplate6()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Verbs = WordList(["Bedded",
               "Boned",
               "Claimed", "Claimed",
               "Deflowered",
               "Mounted",
               "Pleasured",
               "Ravished",
               "Taken","Taken","Taken"])
               
          Adverbs = WordList(["Hard","Hard",
               "Forcefully",
               "Passionately",
               "Roughly",
               "Ruthlessly",
               "Vigorously","Vigorously"])
               
          sVerbPhrase = Verbs.GetWord()
          if CoinFlip():
               sVerbPhrase += " " + Adverbs.GetWord()
               
          Places = WordList(['in the Graveyard','in the Graveyard','in the Mausoleum',
                                 'in the Sepulcher','in the Morgue','in the Mortuary',
                                 'in the Haunted House','at the Tomb','in a Casket',
                                 'in a Coffin'])
               
          MaleNotList = ['copper']
          Man = char.MaleChar(bAddTheArticle = True, bAddEndNoun = False, bAllowGang = False, NotList = MaleNotList,
                    bAllowTitle = True, bAllowAttitude= False, bAllowMaritalStatus = False, bAllowProf = False, 
                    bAllowTrope = True, bAllowNation = False, bAllowSpecies = False, bAllowAge = False)
                    
          ManNouns = WordList(['Ghost','Zombie','Vampire','Werewolf','Ghoul','Skeleton','Mummy','Corpse',
                                    'Serial Killer'])
                                    
          sTweet = sVerbPhrase + "\n" + Places.GetWord() + "\nby " + Man.Desc + " " + ManNouns.GetWord()

          return sTweet     
          
#I Was Scissored by a Witch, and I Liked It!
# NOTE: "Undead" version of Generator 20
class Generator138(TitleGen):
     def __init__(self):
         super().__init__(ID = 138, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate7()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ReqTemplateTags = ["woman"]
          self.ExclTemplateTags = ["gay","man","men"]
          
          Verbs = WordList(["Ravished","Fingered","Milked","Scissored","Fisted",
                                "Kissed","Eaten Out","Sixty-Nined","Finger-Banged",
                                "French Kissed","Taken with a Broomstick",
                                "Penetrated with a Broomstick","Bitten",
                                "Defiled with a Broomstick",
                                "Ravished with a Broomstick"])
               
          if CoinFlip():
               NotFemList = ['anal','tease','virgin','fertile','small-town','tender','revealing','mature woman',
                                   'witch']
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddAnArticle = True, SelectTemplateID = 224,
                                      MaxChars = 24, NotList = NotFemList)
                                        
               sTweet = "I Was " + Verbs.GetWord() + " by " + Girl.Desc + "\nAnd I Liked It!"
                                        
          else:
               NotFemList = ['anal','devlish','tease','virgin','fertile','small-town','submissive',
                                'tender','masseuse','mature','little']
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddEndNoun = True, 
                                        SelectTemplateID = 22, MaxChars = 24) #NotList = NotFemList)
               
               sTweet = "I Was " + Verbs.GetWord() + " by an Undead " + Girl.Desc + "\nAnd I Liked It!"

          return sTweet     
     
# My Innocent Sheltered Step-Mom 
# Wore a Butt Plug
# To Church     
class Generator139(TitleGen):
     def __init__(self):
         super().__init__(ID = 139, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NiceGirlAdjs = WordList(['Amish','Chaste','Christian','Conservative','Innocent','Modest',
                                         'Mormon','Sheltered','Shy','Small-Town','Uptight','Wholesome'])
          PhysAdjs = WordList(['Busty','Bubble-Butt','Curvy','Bikini-Bod','Stacked','Slender',
                                    'Full-Bodied','Large Breasted','Round-Bottomed','Petite',
                                    'Statuesque','Fat-Bottomed'])
          NiceGirlNouns = WordList(['Housewife','Nanny','Step-Mother','Secretary','Step-Daughter',
                                          'Step-Sister','Yoga Instructor','Girlfriend','Fiancé','Wife',
                                          'Mom','Sister','Sister-in-Law','Babysitter'])
     
                                        
          KinkNouns = WordList(['Wore Anal Beads','Wore an Anal Hook','Wore a Ball Gag',
                                        'Wore a Butt Plug','Went Commando','Wore a Clit Clamp',
                                        'Wore a Clit Pump','Wore Crotchless Panties','Wore a Chastity Belt',
                                        'Wore Nipple Clamps','Wore a Remote Controlled Vibrator',
                                        'Wore a Rubber Fetish Suit','Wore a Speculum','Wore a Strap-On',
                                        'Wore a Cupless Bra','Went Topless','Went Nude',
                                        'Wore a See-Thru Dress','Wore a Dog Collar','Wore Nothing But High Heels',
                                        'Went Stark Naked','Wore Nipple Pasties',
                                        'Wore a Skirt With No Panties'])
                                        
          sTweet = "My " + NiceGirlAdjs.GetWord() + " "
          if randint(1,3) == 3:
               sTweet += PhysAdjs.GetWord() + " "
          sTweet += NiceGirlNouns.GetWord() + "\n"
          sTweet += KinkNouns.GetWord() + "\n" 
          sTweet += WordList(["To Church","To Church","To the Office","To Class","To the Grocery Store",
                                   "To the Gym","To Sunday School","To Our Yoga Class","To Work"]).GetWord()

          return sTweet     
          
# I Sucked On My Mother-in-Law's Massive Mammaries 
class Generator140(TitleGen):
     def __init__(self):
         super().__init__(ID = 140, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemRelations = WordList(['Mother-in-Law','Sister-in-Law','Daughter-in-Law','Step-Mom',
                                         'Friend\'s Mom','English Teacher','Babysitter','Boss',
                                         'Boss\'s Wife','Mom','Teacher','Secretary','Best Friend'])

          TitsAdjB = WordList(['Bare','Big','Boobalicious','Bouncing','Bountiful'])
          TitsAdjC = WordList(['Collossal','Creamy'])
          TitsAdjD = WordList(['Delicious','Double-D'])
          TitsAdjF = WordList(['Firm','Fulsome'])
          TitsAdjG = WordList(['Gargantuan','Gigantic','Generous'])
          TitsAdjH = WordList(['Heaving','Heavy','Huge'])
          TitsAdjJ = WordList(['Giant','Gigantic','Generous','Jiggling','Juicy','Jumbo'])
          TitsAdjK = WordList(['Nubile','Nibble-able','Naughty'])
          TitsAdjL = WordList(['Lickable','Lovely','Luscious'])
          TitsAdjM = WordList(['Magnificent','Massive'])
          TitsAdjN = WordList(['Nubile','Nibble-able','Naughty','Nude'])
          TitsAdjP = WordList(['Plush','Plump','Pendulous','Perky'])
          TitsAdjR = WordList(['Ripe','Robust','Round'])
          TitsAdjSw = WordList(['Sweet','Swollen','Sumptuous','Succulent','Supple'])
          TitsAdjT = WordList(['Tasty','Titanic','Tender','Tremendous'])
                                   
          TitsNouns = WordList(['Bangers','Bazooms','Boobies','Boobs','Bosoms','Breasts','Cantaloups','Coconuts','Dumplings','Gazongas',
                                     'Globes','Hams','Hooters','Honkers','Jugs','Knockers','Love Balloons',
                                     'Mammaries','Meat Melons','Melons','Pillows','Puppies','Rack',
                                     'Sweater-Puppies','Sweater-Zeppelins','Tatas','Tits','Titties'])
                                     
          sTitsNoun = TitsNouns.GetWord()
          sTitsAdj = ""
          if sTitsNoun[0].lower() == 'b':
               sTitsAdj = TitsAdjB.GetWord()
               
               
          elif sTitsNoun[0].lower() == 'c':
               sTitsAdj = TitsAdjC.GetWord()
               
          elif sTitsNoun[0].lower() == 'd':
               sTitsAdj = TitsAdjD.GetWord()
               
          elif sTitsNoun[0].lower() == 'g':
               sTitsAdj = TitsAdjG.GetWord()
               
          elif sTitsNoun[0].lower() == 'h':
               sTitsAdj = TitsAdjH.GetWord()
               
          elif sTitsNoun[0].lower() == 'j':
               sTitsAdj = TitsAdjJ.GetWord()
               
          elif sTitsNoun[0].lower() == 'k':
               sTitsAdj = TitsAdjK.GetWord()
               
          elif sTitsNoun[0].lower() == 'm':
               sTitsAdj = TitsAdjM.GetWord()
               
          elif sTitsNoun[0].lower() == 'n':
               sTitsAdj = TitsAdjN.GetWord()
               
          elif sTitsNoun[0].lower() == 'p':
               sTitsAdj = TitsAdjP.GetWord()
          
          elif sTitsNoun[0].lower() == 'r':
               sTitsAdj = TitsAdjR.GetWord()
               
          elif sTitsNoun[0:2].lower() == 'sw':
               sTitsAdj = TitsAdjSw.GetWord()
               
          else: 
               sTitsAdj = TitsAdjT.GetWord()
          
                                     
          sTweet += "I " + WordList(['Motor-boated','Played with','Sucked on','Sucked','Milked',
                                             'Fooled Around With']).GetWord() + " My "
          sTweet += FemRelations.GetWord() + "'s " + sTitsAdj + " " + sTitsNoun 

          return sTweet     
          
class Generator141(TitleGen):
# Hypnotized by Her Secretary's
# Wide Lesbian Ass
     def __init__(self):
         super().__init__(ID = 141, Priority = GenPriority.Lowest)
         self.Template = templates.TitleTemplate7()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["gay","man","men","straight"]
          
          ForbiddenFems = WordList(["Mom","Step-Mom","Step-Sister","Mother-in-Law","Aunt","Sister-in-Law",
                                          "Daughter","Step-Daughter","Teacher","Secretary","Maid","Nurse",
                                          "Twin Sister","Co-ed Student"])
          BodyParts = WordList(["Ass","Ass","Ass","Thighs","Thighs","Boobs","Tits","Melons","Knockers","Hips","Nipples","Nips",
                                     "Coconuts","Titties","Jugs","Sweater-Puppies","Sweater-Zeppelins","Buns",
                                     "Booty","Tush","Buttocks","Behind"])
          Adjs = WordList(["Thick","Chubby","Juicy","Ample","Fat","Jiggling","Generous","Ripe",
                               "Voluptuous","Wide","Shapely","Smooth","Phat","Enormous","Rippling",
                               "Big","Chunky","Large","Curvy","Milky","Quivering"])
          sTweet += "Hypnotized by her " + ForbiddenFems.GetWord() + "'s\n"
          sTweet += Adjs.GetWord() + " "
          sTweet += "Lesbian " + BodyParts.GetWord()

          return sTweet

# I Watched My Wife
# Make a Porno
# with Nine Shameless Clean-Shaven Horse-Cock Highlander Luchadors
class Generator142(TitleGen):
     def __init__(self):
         super().__init__(ID = 142, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemRelative = WordList(["Sister", "Wife", "Bride", "Girlfriend", "Lesbian Bride", "Daughter", "Step-daughter",
                                         "Mother-in-Law", "Mom", "Fiancé", "Young Wife", "New Bride", "Highschool Sweetheart",
                                         "Teenage Daughter","Blushing Bride","Virgin Girlfriend","Conservative Girlfriend",
                                         "Conservative Step-Mom", "Hot Sister", "Hot Step-Sister", "Gay Dad","Gay Step-Dad",
                                         "Religious Step-Mom","Gay Husband","Gay Boyfriend","Uptight Wife", "Uptight Fiancé"]).GetWord()
               
          sTweet = "I Watched My " + FemRelative + "\n"
          
          GangNotList = ["Taboo","Millennial"]
          MaleGang = char.GangMaleChar(MaleCharType = MaleCharType.GangPlural,NotList = GangNotList)
          
          Num = WordList(["Two","Two","Three","Three","Four", "Five","Six","Seven","Eight","Nine", "Ten","A Dozen", "17", 
                               "Two Dozen", "Hundreds of"])
          
          sTweet += "Make a Porno\n"
          sTweet += "with " + Num.GetWord() + " " + MaleGang.Desc 
          
          return sTweet   
      
class Generator143(TitleGen):
    def __init__(self):
        super().__init__(ID = 143, Priority = GenPriority.Low)
        self.Template = templates.TitleTemplate8()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ReqTemplateTags = ["couple","straight"]

        Verbs = WordList(["Banged","Boinked","Boned","Creamed",
                          "Did","Drilled","Fingered","Fucked",
                          "Humped","Porked","Rimmed","Stuffed"
                        ])
        FemRelations = WordList(["Your Best Friend","Your Daughter",
                                 "Your Friend","Your Mom","Your Mom",
                                 "Your Sister","Your Step-Mom",
                                 "Your Step-Sister",
                                 "Your Twin Sister","the Babysitter",
                                 "the Nanny","Your Younger Sister"])   

        sTweet += "“Honey, I " + Verbs.GetWord() + " "
        sTweet += FemRelations.GetWord() + "!\""

        return sTweet     

class Generator144(TitleGen):
     # Boned by the Beefy Billionaire
     #  (gen 1 but it rhymes)
     def __init__(self):
         super().__init__(ID = 144, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          self.ExclTemplateTags = ["lesbian"]
          self.ReqTemplateTags = ["woman","man"]
          
          #Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, MaxChars = 32,
          #                       bSplitArticle = True, bAllowGang = True)

          VerbList = WordList()
          for verb in self.VerbsBy.GetWordList():
              if len(verb.split()) == 1:
                  VerbList.AddWord(verb)

          MasterAdjs = WordList(titmisc.GenModMale().GetWordList() + 
                                titmisc.AttitudeMale().GetWordList() +
                                titmisc.ClothesMale().GetWordList() +
                                titmisc.PhysCharMale().GetWordList() + 
                                titmisc.DickCharMale().GetWordList() + 
                                titmisc.NationMale().GetWordList())
          MasterNouns = WordList(titmisc.ProfMale().GetWordList() +
                                 titmisc.SpeciesMale().GetWordList() +
                                 titmisc.TitlesMale().GetWordList() +
                                 titmisc.TropesWealthyMale().GetWordList())

          RhymingVerbNounPair = GetRhymingPair(VerbList.GetWordList(), MasterNouns.GetWordList())
          RhymingAdjNoun = GetRhymingWord(RhymingVerbNounPair[1], MasterAdjs.GetWordList())
          sTweet = RhymingVerbNounPair[0] + "\nBy " + AddArticles(RhymingAdjNoun, bSplitArticle = True) + " " + RhymingVerbNounPair[1]

          return sTweet

class Generator145(TitleGen):
    def __init__(self):
        super().__init__(ID = 145, Priority = GenPriority.Low, Disabled = False)
        #self.Template = templates.TitleTemplate6()
        self.Template = templates.TitleTemplate29()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        sHerName = NamesFemale().FirstName()
        while len(sHerName) < 7:
            sHerName = NamesFemale().FirstName()

        sHerName = sHerName[:-1] + sHerName[-1].upper()

        self.ReqTemplateTags = ["couple","straight"]

        Verbs = WordList(['Banged hard','Boinked hard','Fisted deep','Fucked hard',
                          'Humped Silly','Jack-hammered','Plowed hard','Porked hard',
                          'Reamed Relentlessly','Titty-Fucked','Anal penetration','Spit-roasted',
                          'Bukkake Party','Double Penetrated','Triple Penetration',
                          'Ass-to-Mouth','Anal Fisting','Big Black Cock','Gang-Banged',
                          'Fucked Silly'])
        Location = WordList(["on the bathroom floor","on the kitchen counter", 
                             "in the back seat","on a park bench",
                             "on the washing machine","at the laundromat",
                             "under a jungle gym","on a merry-go-round",
                             "on an elliptical machine","on a treadmill",
                             "on a trampoline","in the ladie's room",
                             "in a kiddie pool","on a see-saw",
                             "on an ikea futon","in the men's room",
                             "in the janitor's closet","on the hood of a Buick",
                             "in the back of a truck"])

        sTweet = sHerName + "\n"
        sTweet += Verbs.GetWord() + "\n" + Location.GetWord() +"!"


        #sTweet = "Regina\nFucked Hard\nat the Laundromat!"
        #sTweet = "Regina\nFucked Hard at the Laundromat"
        

        return sTweet     

class Generator146(TitleGen):
    def __init__(self):
         super().__init__(ID = 146, Priority = GenPriority.AboveAverage)
         self.Template = templates.TitleTemplate1()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        self.ExclTemplateTags = ["gay"]
        self.ReqTemplateTags = ["woman"]

        Gerunds = WordList(['Ass Fucking',
                           'Banging',
                           'Bare-backing',
                           'Bedding',
                           'Boinking',
                           'Boning',
                           'Cavity Searching',
                           'Cream-Pieing',
                           'Deflowering', 
                           'Dominating',           # Daring Dominatrix
                           'Drilling',
                           'Dry Humping',
                           'Eating Out',
                           'Edging',
                           'Fingering',
                           'Fisting',
                           'Gagging',
                           'Gang-Banging',
                           'Hot-Dogging',
                           'Humping',
                           'Impregnating',
                           'Jerking Off On',
                           'Jizzing On',
                           'Knocking Up',
                           'Licking',
                           'Lubing Up',
                           'Masturbating',
                           'Milking',
                           'Motor-Boating',
                           'Mounting',
                           'Nailing',           # the norwegian naughty brat
                           'Paddling',
                           'Penetrating',
                           #'Plowing',          # platinum blonde playboy centerfold
                           'Porking',
                           'Queefing',  
                           'Ravishing',         # rebellious teen
                           'Raw Dogging',
                           'Reaming',
                           'Riding',
                           'Rimming',
                           'Sixty-nining',
                           'Spanking',
                           #Stripping',        # Straight-Laced Stripper
                           'Stuffing',
                           'Taking',
                           'Tea-bagging',
                           'Violating',
                           'Whipping'])

        GirlAdjs = WordList(titmisc.AgeFemaleAdj().GetWordList() + 
                                titmisc.AttitudeFemale().GetWordList() +
                                titmisc.ClothingFemale().GetWordList() +
                                titmisc.GenModFemale().GetWordList() + 
                                titmisc.NationFemale().GetWordList() + 
                                titmisc.PhysCharFemale().GetWordList() +  
                                titmisc.SexualityFemale().GetWordList() +  
                                titmisc.SkinHairColorFemale().GetWordList() +  
                                titmisc.SpeciesFemale().GetWordList() +  
                                titmisc.RaceFemale().GetWordList() +  
                                titmisc.SpeciesFemale().GetWordList())

        GirlNouns = WordList(titmisc.SpeciesFemale().GetWordList() +
                             titmisc.ProfFemale().GetWordList() + 
                             titmisc.GirlFemale().GetWordList() + 
                             titmisc.TitlesFemale().GetWordList() + 
                             titmisc.TropesFemale().GetWordList() + 
                             titmisc.NounsNiceGirl().GetWordList())

        RhymingVerbAdjPair = GetRhymingPair(Gerunds.GetWordList(), GirlAdjs.GetWordList())
        sGerund = RhymingVerbAdjPair[0]
        sAdj = RhymingVerbAdjPair[1]
        #print("Gerund is " + sGerund + ", Adj is " + sAdj)
        sNoun = GetRhymingWord(sAdj, GirlNouns.GetWordList())
        while FoundIn(sNoun, sAdj):
            sNoun = GetRhymingWord(sAdj, GirlNouns.GetWordList())
        
        PersonalRelate = ["sister","brother","mom","dad","mother",
                            "father","fiancé","wife","girlfriend",
                            "teacher","secretary","daughter",
                            "babysitter","governess","tutor",
                            "bride"]
        sArticle = "The"
        if FoundIn(sAdj, PersonalRelate) or FoundIn(sNoun, PersonalRelate):
            sArticle = "My"

        sTweet = sGerund + "\n" + sArticle + "\n" + sAdj + " " + sNoun

        return sTweet     

class Generator147(TitleGen):
    def __init__(self):
         super().__init__(ID = 147, Priority = GenPriority.Normal)
         self.Template = templates.TitleTemplate30()
     
    def GenerateTweet(self):
        super().GenerateTweet()
        sTweet = ""

        ExclGenList = [12,17,26,30,31,51,54,55,62,67,74,78,79,89,90,133,136,147]

        ImgTxtGen = GetTweet(bTest = False, bTweet = False, iGeneratorNo = -1, bAllowPromo = False, bAllowFavTweets = False)
        while int(ImgTxtGen.ID) in ExclGenList or len(ImgTxtGen.ImgTxt) > 55:
            ImgTxtGen = GetTweet(bTest = False, bTweet = False, iGeneratorNo = -1, bAllowPromo = False, bAllowFavTweets = False)
  
        self.ExclTemplateTags = ImgTxtGen.ExclTemplateTags
        self.ReqTemplateTags = ImgTxtGen.ReqTemplateTags

        if len(ImgTxtGen.ImgTxt) > 0:
            sTweet = " ".join(ImgTxtGen.ImgTxt.split("\n"))

        Sequels = WordList(["2","II","III","3","4","IV","5","V","7","VII","8","VIII","10","11","12","13","17","18","20","21","22","37","69"])

        sTweet += "\n" + WordList(["Book","Part","Volume"]).GetWord() + " " + Sequels.GetWord()

        return sTweet

# Testing innuendo name generators          
class Generator999(TitleGen):
     Type = GeneratorType.Test
     def __init__(self):
         super().__init__(ID = 999, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          iNum = 0
          
          if iNum != 0:
          
               sTweet += "Female: " + GetInnName(Gender.Female,iNum)
               sTweet += "\n"
               sTweet += "Male: " + GetInnName(Gender.Male,iNum)
          else:
               sTweet += "Female: " + GetInnName(Gender.Female)
               sTweet += "\n"
               sTweet += "Male: " + GetInnName(Gender.Male)

          return sTweet     
          
#Testing rhyming functions
class Generator1000(TitleGen):
     Type = GeneratorType.Test
     def __init__(self):
         super().__init__(ID = 1000, Priority = GenPriority.Lowest, Disabled = True)
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemAdjList = titmisc.AgeFemaleNoun().List + titmisc.AgeFemaleAdj().List + titmisc.AttitudeFemale().List + titmisc.ClothingFemale().List + titmisc.GenModFemale().List + titmisc.MaritalStatusFemale().List + titmisc.NationFemale().List + titmisc.PhysCharFemale().List + titmisc.PregState().List + titmisc.SexualityFemale().List + titmisc.SkinHairColorFemale().List
          FemNounList = titmisc.ProfFemale().List + titmisc.RelateFemale().List + titmisc.SpeciesFemale().List + titmisc.TropesFemale().List
          #List1 = titmisc.SpeciesFemale().List

          #List2 = sorted(List1)
          
          # List1 = ["strict","stuffy","surly","pseudonymous"]
          # List2 = ["buddy","stranger","psycho"]
          
          aFemResult = GetRhymingPair(FemAdjList,FemNounList)
          sTweet = "Female: " + aFemResult[0] + " " + aFemResult[1] + "\n"
          
          ManAdjList = titmisc.AgeMaleAdj().List + titmisc.AttitudeMale().List + titmisc.GenModMale().List + titmisc.MaritalStatusMale().List + titmisc.NationMale().List + titmisc.PhysCharMale().List + titmisc.DickCharMale().List + titmisc.SkinHairColorMale() .List
          ManNounList = titmisc.ProfMale().List + titmisc.RelateMale().List + titmisc.SpeciesMale().List + titmisc.TitlesMale().List + titmisc.TropesMale().List + titmisc.TropesMale().List 
          
          aManResult = GetRhymingPair(ManAdjList,ManNounList)
          sTweet += "Male: " + aManResult[0] + " " + aManResult[1] + "\n"
          # sNoun = NounList[randint(0,len(NounList) - 1)]
          # sAdj = GetRhymingWord(word = sNoun, list = AdjList)
          
          # if sAdj:
               # sTweet = "Rhyming phrase: [" + sAdj + " " + sNoun + "]"
          # else:
               # sTweet = "No rhyme found for " + sNoun 

          return sTweet     

#Testing specific title generators          
class Generator1001(TitleGen):
     Type = GeneratorType.Test
     def __init__(self):
         super().__init__(ID = 1001, Priority = GenPriority.Lowest, Disabled = True)
         self.Template = templates.TitleTemplate8()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(TempType = TempType.Flowery, 
                                        bAddTheArticle = False, 
                                        bAllowTrope = True, 
                                        SelectTemplateID = 26)
          #Guy = char.MaleChar(TempType = TempType.Flowery, 
          #                         bAddAnArticle = True, 
          #                         bAllowGang = False,
          #                         bAllowTrope = True,
          #                         SelectTemplateID = 14)
          #Gang = char.MaleChar(TempType = TempType.Flowery,
          #                          bAddAnArticle = True,
          #                          bAllowGang = True)
          

          sTweet += AddArticles(Girl.Desc, bMakeUpper = True) + " Gets Sexed the Hell Up!\n"
          #sTweet += AddArticles(Guy.Desc, bMakeUpper = True) + " Took My Wife Hard From Behind!\n"
          #sTweet += Guy.Desc + " Took My Wife Hard From Behind!\n"
          #sTweet += Gang.Desc + " Took Turns With My Wife!"

          return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(TitleGen):
     # ID = 100
     # Priority = GenPriority.Lowest
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
def ShuffleFavs(sFileName = ""):
     if sFileName == "":
          sFileName = titutil.FAVTITLE_FILENAME
          
     sFavTitle = ""
     
     Titles = []
     Titles.append("")
     iTitleCount = 0
          
     with open(sFileName, 'r') as infile:
          for line in infile:
               if line.strip() == titutil.FAVTITLE_DIVIDER:
                    Titles.append("")
                    iTitleCount += 1
               elif not line.strip():
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
                    outfile.write(CleanTitles[x] + FAVTITLE_DIVIDER + "\n")
               else:
                    outfile.write(CleanTitles[x] + "\n" + FAVTITLE_DIVIDER + "\n")

def CurateFavorites(iGen = 0, iMaxLen = 0):
        sInput = ""
        iSkipCount = 0
        iAddCount = 0

        ImgTxtGen = None
     
        while True:
        # Create Title 
            sDetailsLine = ""
            sTxtLine = ""
            sOutput = ""
          
            if iGen > 0:
                ImgTxtGen = GetTweet(bTest = True, bTweet = False, 
                                     iGeneratorNo = iGen, 
                                     bAllowPromo = False, 
                                     bAllowFavTweets = False, 
                                     iMaxLen = iMaxLen)
            else:
                ImgTxtGen = GetTweet(bTest = False, bTweet = False, 
                                     iGeneratorNo = iGen, 
                                     bAllowPromo = False, 
                                     bAllowFavTweets = False, 
                                     iMaxLen = iMaxLen)

        # Get author 
            ImgTxtGen.AuthorName = AuthorBuilder(ImgTxtGen.AuthorGender)

        # Create output string for writing 
            sDetailsLine += "[" + str(ImgTxtGen.ID) + "]"
            #sDetailsLine += "[" + str(ImgTxtGen.Template.ID) + "]"
            sDetailsLine += "[" + type(ImgTxtGen.Template).__name__ + "]"
            
            sDetailsLine += "[" + ImgTxtGen.AuthorName + "]"
            sDetailsLine += "[" + str(ImgTxtGen.AuthorGender).split(".")[1] + "]" 

            sDetailsLine += "["
            if not ImgTxtGen.ReqTemplateTags is None and len(ImgTxtGen.ReqTemplateTags) > 0:
                
                for tagno, tag in enumerate(ImgTxtGen.ReqTemplateTags):
                    sDetailsLine += tag
                    if tagno < len(ImgTxtGen.ReqTemplateTags) - 1:
                        sDetailsLine += ","
            sDetailsLine += "]"

            sDetailsLine += "["
            if not ImgTxtGen.ExclTemplateTags is None and len(ImgTxtGen.ExclTemplateTags) > 0:
                
                for tagno, tag in enumerate(ImgTxtGen.ExclTemplateTags):
                    sDetailsLine += tag
                    if tagno < len(ImgTxtGen.ExclTemplateTags) - 1:
                        sDetailsLine += ","
            sDetailsLine += "]"

            sTxtLine += ImgTxtGen.ImgTxt.strip()
            sOutput = "{{" + sDetailsLine + "}}\n" + sTxtLine  + "\n" + FAVTITLE_DIVIDER + "\n"

        # Print generated title and info
            
            print(sOutput)
            print("Priority = " + str(ImgTxtGen.Priority))

        # Prompt user.
            sInput = input("\nKeep suggested title? [y]es, [n]o, or [q]uit: ")
          
        # If [y], save tweet.
            if sInput.lower().strip() == "y":
                with open(titutil.FAVTITLE_FILENAME, 'a+') as WriteReplyFile:

                    WriteReplyFile.write(sOutput)

                    iAddCount += 1

                    print("Favorited tweet and saved.")
               
        # If [q], quit.
            elif sInput.lower().strip() == "q":
                break
          
         # If [n], do nothing and loop.
            else:
                iSkipCount += 1
                print("Skipped.")

        dPerRejects = 100
        if (iAddCount + iSkipCount) != 0:
            dPerRejects = round((Decimal(iSkipCount)/Decimal(iAddCount + iSkipCount))*100,2)
                    
        print("\nFavorited " + str(iAddCount) + ", rejected " + str(iSkipCount) + ". " + str(dPerRejects) + "% rejection rate.")

        # before ending we may want to shuffle our favorited tweet file.
        # prompt user.
        sInput = input("\nShuffle favorited tweets? [y]es, [n]o: ")
        if sInput.lower().strip() == "y":
            ShuffleFavs()   