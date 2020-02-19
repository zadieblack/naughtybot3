#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generators module

import sys, threading, traceback
from random import *
from util import *
from title.util import *
from names import *
#from titpeeps import *
from title.texttoimg import *
from title.characters import *
#import title.people as titpeeps
import misc
import title.misc as titmisc
import title.chargenerator as char
import title.titletemplates as templates

PromoHistoryQ = HistoryQ(2)

class Generator():
    ID = -1
    # each generator should have a unique ID
    Priority = 1
    # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
    Type = GeneratorType.Normal
    # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
     
    def SetPriority(self, sText, List, iPriority):
        for x in range(iPriority):
            List.append(sText)
          
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
    
    def __init__(self, ID = -1, Priority = 1, Template = templates.TitleTemplateHHDefault):

        if not ID == -1:
            self.ID = ID
        self.Priority = 1

        self.ImgTxt = ""
        self.TweetTxt = ""
        self.AuthorName = ""

        if CoinFlip():
            self.AuthorGender = Gender.Male 
        else:
            self.AuthorGender = Gender.Female

        self.Template = None

    def GenerateTweet(self):
        self.VerbsBy = misc.BookVerbsBy()
        self.VerbsTo = misc.BookVerbsTo()
        self.Gerunds = misc.BookGerunds()
        self.HerName = NamesFemale().FirstName()
        self.HisName = NamesMale().FirstName()
        self.SubtitleCoda = titmisc.SubtitleCoda()

    def SetImgText(self,stxt):
        if self.Template is None:
            self.Template = templates.TitleTemplateHHDefault

        self.Template.ClearLineText()
        self.Template.AddLineText(stxt)

def GetTweetGenerator(bTest, iGeneratorNo = 0, bAllowPromo = True, Type = None):
     gen = None
     GenType = None 
     
     if not Type is None:
          GenType = Type 
     else:
          GenType = None 
     #print("GetTweet() Generator Type is " + str(GenType))
     
     iSwitch = 999
     
     GenSel = GeneratorSelector()
     if bTest:
          gen = GenSel.GetGenerator(iGeneratorNo)
          if gen == None:
               gen = Generator()
     else:
          gen = GenSel.RandomGenerator(bAllowPromo = bAllowPromo, Type = GenType)
          
     return gen
     
def GetTweet(bTest, bTweet, iGeneratorNo = 0, bAllowPromo = True, Type = None, TweetHistoryQ = None, bAllowFavTweets = True):
    Gen = None
    sTweet = ""
    
    if not bTest and bAllowFavTweets:
        sTweet = GetNextFavTitleFromFile()
        Gen = Generator()
        Gen.ImgTxt = sTweet
    else:
        Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = bAllowPromo)

        if not TweetHistoryQ is None:
            while bTweet and not TweetHistoryQ.PushToHistoryQ(Gen.ID):
                Gen = GetTweetGenerator(bTest, iGeneratorNo, bAllowPromo = bAllowPromo)
     
        sTweet = Gen.GenerateTweet()
        Gen.ImgTxt = sTweet

    return Gen
     
class GeneratorPromo(Generator):
     ID = 0
     Priority = 0
     Type = GeneratorType.Promo
     
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
          
class Generator1(Generator):
     # Blackmailed by the Billionaire Mountain Man 
     def __init__(self):
         super().__init__(ID = 1, Priority = 1)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = False, bAllowGang = True, bAllowTrope = True, bAllowRelate = True)
          
          sTweet = self.VerbsBy.GetWord() + "\nBy The\n" + Master.Desc
          
          self.SetImgText(sTweet)

          return sTweet
          
class Generator2(Generator):
     # Veonica Gets Blackmailed by the Billionaire Mountain Man 
     ID = 2
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          #Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
          #Girl = char.FemaleChar(TempType = TempType.Flowery, bAddArticle = False, bAllowTrope = True)
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowGang = True, bAllowRelate = True, bAllowTrope = True)
          
          sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace"]) + " by\n" + Master.Desc
          
          return sTweet

class Generator3(Generator):
     # Married to the Alpha Wolf
     def __init__(self):
         super().__init__(ID = 3, Priority = 1)
         self.Template = templates.TitleTemplate1()
       
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(TempType = TempType.Flowery, 
                                 bAddTheArticle = True, 
                                 sPosArticle = "Her", 
                                 bSplitArticle = True,
                                 bAllowGang = True, 
                                 bAllowRelate = True, 
                                 bAllowTrope = True)
               
          sTweet = self.VerbsTo.GetWord() + "\nTo " + Master.Desc

          self.SetImgText(sTweet)

          return sTweet

class Generator4(Generator):
     # Veronica Gets Married to the Alpha Wolf     
     ID = 4
     Priority = 1

     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          #Master = MaleChar(iNumMaxCBits = 3, bAddArticle = True, sPosArticle = "Her", bAllowRelate = True)
          #Girl = char.FemaleChar(TempType = TempType.Flowery, bAddArticle = False, bAllowTrope = True)
          Master = char.MaleChar(TempType = TempType.Flowery, bAddTheArticle = True, sPosArticle = "Her", bAllowGang = True, bAllowRelate = True, bAllowTrope = True)
          
          sTweet = self.HerName + " Gets " + self.VerbsTo.GetWord() + " to \n" + Master.Desc
          
          return sTweet
          
class Generator5(Generator):
     # Jackie Shows a Horny French Alpha Wolf her Cunning Stunt
     ID = 5
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          GenNotList = ["BDSM"]
          Girl = None
          Master = None
               
          Master = char.MaleChar(TempType = TempType.Flowery, bAddAnArticle = True, bAllowRelate = True,NotList = GenNotList)

          sTweet = self.HerName + " Shows " + Master.Desc + "\nHer Cunning Stunt" 
          
          return sTweet
          
class Generator6(Generator):
     # Seduced in the Bed of the Billionaire     
     ID = 6
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotList = ["Pledged", "Public", "Charmed", "Cuckolded", "Hunted", "Harrassed", "Sold", 
                         "Gifted", "Pledged", "Bed", "Sex Dungeon","Basement","Dungeon","Surrendered"]
          
          #Girl = char.FemaleChar(TempType = TempType.Medium, bAllowTrope = True, NotList = GenNotList)
          Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True,bAddTheArticle = True)
          #Master = MaleChar(iNumMaxCBits = 3, bAllowGang = False, NotList = NotList, bAddArticle = True)
          
          sTweet += self.VerbsBy.GetWord(NotList = NotList) + " In The Bed Of\n" + Master.Desc 
          
          return sTweet
          
class Generator7(Generator):
     # A Buff Tuxedoed Italian Dinosaur Took My Wife Hard From Behind!
     def __init__(self):
         super().__init__(ID = 3, Priority = 1)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(TempType = TempType.Flowery, 
                                        bAllowRelate = True, 
                                        bAllowTrope = True,
                                        bAddAnArticle = True, 
                                        sPosArticle = "My")
          Verbs = WordList(["Took","Claimed","Ravished","Mounted", "Plowed"])
          
          sTweet = Master.Desc  + "\n"
          sTweet += Verbs.GetWord() + " My Wife From Behind"
          if CoinFlip():
               sTweet += "\n" + WordList(["And They Let Me Watch", "And I Watched","And I Got To Watch"]).GetWord()
          sTweet += "!"

          self.Template.AddLineText(sTweet)

          return sTweet

class Generator8(Generator):
     # My Blind Date is A Uniformed Australian Mer-man Fighter Pilot! 
     def __init__(self):
         super().__init__(ID = 8, Priority = 1)
         self.Template = templates.TitleTemplate1()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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

          self.Template.AddLineText(sTweet)

          return sTweet
          
class Generator9(Generator):
     # The Secretary and the Space Werewolf  
     def __init__(self):
         super().__init__(ID = 9, Priority = 1)
         self.Template = templates.TitleTemplate2()
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotList = ["BDSM"]
          Girl = char.FemaleChar(TempType = TempType.Medium, bAllowRelate = True, bAllowTrope = True, bAllowSpecies = False, bAllowTitle = False, NotList = NotList)
          Master = char.MaleChar(TempType = TempType.Flowery, bAllowRelate = True, bAllowTrope = True, bAddTheArticle = True, sPosArticle = "Her", bSplitArticle = True, NotList = NotList)
          
          sTweet = "The " + Girl.Desc + "\nAnd " + Master.Desc 
          if len(sTweet) > 60:
              sTweet += "\n" + AddArticles(WordList([self._getFMs_(), 
                                                                "BDSM", 
                                                                misc.SexyAdjs().GetWord().lower()]).GetWord()) + " " 
              sTweet += self.SubtitleCoda.GetWord().lower()

          self.Template.AddLineText(sTweet)
          
          return sTweet
          
class Generator10(Generator):
     # I'm Having a Baby for a Stay-at-Home Manticore!
     ID = 10
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(bAddAnArticle = True, sPosArticle = "My", bAllowRelate = True, bAllowDickChar = False, 
                                        NotList = ["naked","nude"])

          sTweet = "\"I'm Having a Baby For\n" + Master.Desc + "!\""

          return sTweet
          
class Generator11(Generator):
     # The Millionaire Sherrif's Virgin
     ID = 11
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Relations = titmisc.RelateFemale()
          Gerunds = self.Gerunds
          
          sTweet = Gerunds.GetWord() + " My " + char.FemaleChar(bAddEndNoun = False, bAllowSpecies = False, 
                                                                                bAllowRelate = False, bAllowAge = False).Desc + " " 
          sTweet += Relations.GetWord(NotList = ['Girlfriend', 'Wife', 'Mistress','Concubine'])

          return sTweet
          
class Generator12(Generator):
     # Babysitter to the Billionaire Uniporn
     ID = 12
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          RelNotList = ["Wife","Girlfriend","Mistress","Concubine","Daughter's Best Friend"]
          Relations = titmisc.RelateFemale()
          Gerunds = self.Gerunds

          sTweet = Gerunds.GetWord() + " "  + self.HerName + ":\n" 
          sTweet += AddArticles(Relations.GetWord(NotList = RelNotList), bMakeUpper = True) + " " 
          sTweet += self.SubtitleCoda.GetWord()

          return sTweet
          
class Generator13(Generator):     
     # I Was an Escort for a Billionaire Uniporn
     ID = 13
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(TempType = TempType.Medium, Type = GirlType.Bad,
                                        bAllowAttitude = False, bAllowGenMod = False, bAllowMaritalStatus = False,
                                        bAllowNation = False, sPosArticle = "My")
          Master = char.MaleChar(bAddAnArticle = True)
          
          sTweet = "I Was " + AddArticles(Girl.Desc) + "\nfor\n" + Master.Desc

          return sTweet
     
class Generator14(Generator):
     # The Virgin Call-Girl's Gang Bang
     ID = 14
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GangNot = ["Dapper","Gang-Bang"]
          
          GirlShort = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium, bAddTheArticle = True, bAllowClothing = False, bAllowSpecies = False)
          GirlLong = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Flowery, bAddTheArticle = True, bAllowClothing = False, bAllowSpecies = False)
          GangSingShort = char.GangMaleChar(TempType = TempType.Medium,MaleCharType = MaleCharType.GangSingular, bAllowClothing = False,NotList = GangNot)
          GangSingLong = char.GangMaleChar(TempType = TempType.Flowery,MaleCharType = MaleCharType.GangSingular, bAllowClothing = False,NotList = GangNot)
          GangPlurShort = char.GangMaleChar(TempType = TempType.Medium,MaleCharType = MaleCharType.GangPlural, bAllowClothing = False,NotList = GangNot)
          GangPlurLong = char.GangMaleChar(TempType = TempType.Flowery,MaleCharType = MaleCharType.GangPlural, bAllowClothing = False,NotList = GangNot)
          
          GangSize = WordList(["Three","Four","Five","Seven","Nine","Ten","A Dozen","Twenty","Two-Dozen","Fifty","One-Hundred"])
          
          Tweets = []
          
          Tweets.append(GirlShort.Desc + "\nHas a Gang Bang with\n" + GangSize.GetWord() + " " + GangPlurLong.Desc) 
          Tweets.append(GirlLong.Desc + "\nHas a Gang Bang with\n" + GangSize.GetWord() + " " + GangPlurShort.Desc)
          Tweets.append(GirlShort.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\nThe " + GangSingLong.Desc)
          Tweets.append(GirlLong.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\nThe " + GangSingShort.Desc)
          Tweets.append(GirlShort.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\n" + GangSize.GetWord() + " " + GangPlurLong.Desc)
          Tweets.append(GirlLong.Desc + "\nGets " + WordList(["Shared","Gang-Banged"]).GetWord() + " By\n" + GangSize.GetWord() + " " + GangPlurShort.Desc)
          
          sTweet = Tweets[randint(0, len(Tweets) - 1)]
          
          return sTweet
          
class Generator15(Generator):
     # The Small-Town Virgin's First Porno
     ID = 15
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, bAllowTitle = False)
          
          sTweet = Girl.Desc + "\n" + WordList(["Makes a Porno","Makes an Anal Porn Flick",
                                                         "Makes a Gangbang Porn Flick","Makes an Interracial Gangbang Porno",
                                                         "Becomes an Anal Porn Star","Becomes a Gangbang Porn Star"]).GetWord()
          if CoinFlip():
               sTweet += ":\nAn " + self._getFMs_() + " " + self.SubtitleCoda.GetWord()

          return sTweet
          
class Generator16(Generator):
# "Oh No! I Went to an Orgy
# And I Accidentally
# Finger-Banged My Asian Step-Sister!"
     ID = 16
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Tweets = []
          
          RelNotList = ['Wife', 'Girlfriend', 'Fiancé','Concubine','Mistress']
          Relations = titmisc.RelateFemale()
          Verbs = WordList(["Boned","Banged","Humped","Had Sex With","Went Down On","Sixty-Nined","Ate Out",
                                "Boinked","Jizzed On","Finger-Banged","Fisted","Did"])
          FemNotList = ["BDSM","little"]
          StepMom = char.FemaleChar(TempType = TempType.Medium, bAddEndNoun = False, NotList = FemNotList,
                                             bAllowMaritalStatus = False, bAllowRelate = False, bAllowSpecies = False,
                                             bAllowAge = False)
          
          sTweet += "\"Oh No! I Went to " + WordList(["an Orgy","a Swinger's Party","a Wild Sex Party"]).GetWord() + "\n"
          if randint(1,4) == 1:
               sTweet += "And I Accidentally\nAte My " + StepMom.Desc + " " + Relations.GetWord(NotList = RelNotList) + "'s Ass!\""
          else:
               sTweet += "And I Accidentally\n" + Verbs.GetWord() + " " 
               sTweet += "My " + StepMom.Desc + " " + Relations.GetWord(NotList = RelNotList) + "!\""
          return sTweet
          
class Generator17(Generator):
     # Enslaved: The Ebony Older Woman & The Mountain Man Biker Gang 
     ID = 17
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ["Recently-Divorced","Sassy","Tanned","Kitten","Harem","Ice Queen","MILF"]
          Subtitles = []
          
          Master = char.MaleChar()
          Gang = char.GangMaleChar()
          
          VerbNotList = ['Taken']
          sTweet = self.VerbsBy.GetWord(NotList = VerbNotList) + ":\n"
          
          Girl = char.FemaleChar(Type = GirlType.Good, NotList = GirlNotList, bAllowSpecies = False, bAllowTitle = False)
          Subtitles.append("The " + Girl.Desc + "\n& The " + Gang.Desc)
          Subtitles.append("The " + Girl.Desc + "\n& The " + Master.Desc)
          Subtitles.append(AddArticles(Girl.Desc) + "\n" + WordList(['Adventure','Encounter','Liason','Experience','Episode','Rendezvous']).GetWord())
          
          sTweet += Subtitles[randint(0, len(Subtitles) - 1)]
          
          return sTweet
          
class Generator18(Generator):
     # Oh No! My Step-Daughter is a Porn Star
     ID = 18
     Priority = 1
     
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
          
class Generator19(Generator):
      # Full Frontal for the Shy Amish Virgin: A BDSM Romance
      ID = 19
      Priority = 1
     
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
          
class Generator20(Generator):
     # I Was Stripped In Public, And I Liked It
     ID = 20
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          
          Master = char.MaleChar(bAllowGang = False, bAddAnArticle = True, bAllowRelate = True)
          Gang = char.GangMaleChar(bAddAnArticle = True)
          
          sTweet = ""

          sVerbBy = self.VerbsBy.GetWord(NotList = ["Charmed", "Kept", "Trained"])
          sTweet = "\"I Was " + sVerbBy
          sTweet += " By\n"
          if CoinFlip():
               sTweet += Master.Desc
          else:
               sTweet += Gang.Desc
          sTweet += ",\nAnd I Liked It!\""

          return sTweet
          
class Generator21(Generator):
     # Pleasured by the Shape-Shifting Single Dad: A Nudist Secretary Story
     ID = 21
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Master = char.MaleChar(bAddTheArticle = True, bAllowRelate = True)
          
          sTweet = self.VerbsBy.GetWord()  + " By\n"
          sTweet += Master.Desc 
          
          return sTweet
          
class Generator22(Generator):
     # The Amish Virgin and the Taboo Butch MILF: A Lesbian Love Story 
     ID = 22
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlGood = char.FemaleChar(TempType = TempType.Medium, Type = GirlType.Good, ExclList = [SpeciesFemale])
          GirlLes = char.LesbianChar(ReqList = [LesFemaleAdj])
          GirlBad = char.LesbianChar(ReqList = [LesFemaleAdj], Type = GirlType.Bad)

          
          if CoinFlip():
               sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlLes.Desc
          else:
               sTweet = "The " + GirlGood.Desc + "\nand the\n" + GirlBad.Desc
          sTweet += ":\n" + WordList(["A Lesbian","A Secret Lesbian","A Taboo Lesbian","A Forbidden","An FF",]).GetWord() + " " + self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator23(Generator):
     # The Boxer and the Gay Widowed Outlaw Daddy: A Forbidden Love Story 
     ID = 23
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sHisName = PlainNamesMale().FirstName()

          GayTitles = []
          
          StraightGuy = char.MaleChar(bAllowGang = False, ExclList = [SpeciesMale])
          GayGuy1 = char.GayMaleChar(ReqList = [GayMaleAdj])
          GayGuy2 = char.GayMaleChar(ReqList = [GayMaleAdj])
          
          GayTitles.append("The " + StraightGuy.Desc + "\nand\nThe " + GayGuy1.Desc)
          GayTitles.append("The " + GayGuy1.Desc + "\nand\nThe " + GayGuy2.Desc) 
          GayTitles.append("The " + StraightGuy.Desc + "\nand\nThe " + GayGuy1.Desc)
          GayTitles.append(sHisName + " and\nThe " + GayGuy1.Desc)
          
          sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
          sTweet += ":\n" + WordList(["A Gay","A Secret Gay","A Taboo","A Gay", "An MM", "An MM"]).GetWord() + " " + self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator24(Generator):
     # Deep-Throating My Well-Hung Sumo-Wrestler Step-Dad
     ID = 24
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
          
class Generator25(Generator):
     # Greg Gets Pounded In The Butt By The Motorcycle Gang
     ID = 25
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sHisName = PlainNamesMale().FirstName()
          
          GayNotList = ['anal']
          GayGuy = char.GayMaleChar(bAddTheArticle = True, sPosArticle = "His", NotList = GayNotList,
                                             ReqList = [GayMaleAdj,DickCharMale])
          GayGang = char.GangMaleChar(ExclList = [AttitudeMale])

          GayTitles = []
          
          GayTitles.append("Pounded In The Butt By\nThe Gay " + GayGang.Desc)
          GayTitles.append("Pounded In The Butt By\n" + GayGuy.Desc)
          GayTitles.append(sHisName + " Gets " + self.VerbsBy.GetWord(NotList=["Impregnated", "Hotwifed"]) + " By\n" + GayGuy.Desc)
          GayTitles.append(sHisName + " and\n" + GayGuy.Desc)
          
          sTweet = GayTitles[randint(0, len(GayTitles) - 1)]
          sTweet += ":\n" + WordList(["A Gay","A Secret","A Taboo Gay","A Gay", "An MM", "An MM","An Anal"]).GetWord() + " " + self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator26(Generator):
     # Hotwife for Daddy: A BDSM Romance 
     ID = 26
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(TempType = TempType.Medium, bAllowPregState = False, bAllowSexuality = False)
          TabooWord = WordList(["A BDSM","An " + self._getFMs_(), "A Taboo", "A Forbidden", 
                                     "A Forbidden", "A Naughty"]).GetWord()
          SexActs = WordList(["anal", "double anal", "fisting","anal fisting","nipple play", "incest", "twincest",
                                   "cum-swapping","bukkake","pee-drinking","hot-wifing","erotic asphyxiation",
                                   "double penetration","triple penetration","B.D.S.M.","lactation","age play",
                                   "edging","forced orgasm","deep-throating","choke play","extreme penetration",
                                   "leather bondage","tea-bagging","full-frontal massage","enema","adulterous",
                                   "pegging","butt stuff","sodomy","premarital sex","spanking","paddling"])
          
          sTweet = Girl.Desc + "\nFor Daddy:\n"
          sTweet += AddArticles(SexActs.GetWord()).title() + " "
          sTweet += self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator27(Generator):
     # The Shy Lesbian Gymnast Wore Black
     ID = 27
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ["Leather", "Latex", "High-Heeled", "Nude", "Naked", "Nudist", "Latex", "Leather"]
          Girl = char.FemaleChar(NotList = GirlNotList, Type = GirlType.Good, bAddTheArticle = True, 
                                        bAllowRelate = True, bAllowSpecies = False, bAllowAttitude = False)
          Wearables = WordList(["Leather", "Latex", "Red", "Black", "Fishnets", "Spiked Heels", "a Strap-On",
                                     "a Chastity Belt","a Nose Hook", "a Butt Plug", "a Ponytail Butt Plug",
                                     "a Clit Clamp","a Ball Gag","a Steel Collar","an Anal Hook","Nipple Clamps",
                                     "a Spreader Bar","a Spiked Metal Bra","Assless Chaps"])
          
          sTweet = Girl.Desc + "\nWore " + Wearables.GetWord() #+ ":\n"
          #sTweet += AddArticles(Wearables.GetWord(), bMakeUpper = True) #+ " " + self.SubtitleCoda.GetWord()

          return sTweet

class Generator28(Generator):
     #Cuckolded By My Amish Maiden Hotwife
     ID = 28
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(bAddEndNoun = False, bAllowMaritalStatus = False, bAllowSexuality = False, NotList = ['Single', 'Divorced'])
          Man = char.MaleChar(bAddTheArticle = True, bAllowMaritalStatus = False)
          FemaleRelate = WordList(['Wife', 'Wife', 'Fiancé', 'Girlfriend'])
          if CoinFlip():
               sTweet = "Cuckolded By My\n" + Girl.Desc + " " + FemaleRelate.GetWord()
          else:
               sTweet = "My " + FemaleRelate.GetWord() + " "
               sTweet += "And\n" + Man.Desc + ":\nA " + WordList(["Cuckold","Hotwife"]).GetWord() + " "
               sTweet += self.SubtitleCoda.GetWord()
          
          return sTweet
          
class Generator29(Generator):
     # Blackmailing My Step-Dad's Busty Ballerina
     ID = 29
     Priority = 1
     
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
          
class Generator30(Generator):
     # Bubbly & Plump: 
     # The Chaste Small-Town Girl Barista 
     # Rides a Veiny 9-inch Dick
     ID = 30
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotGirlList = ["Harem Princess","Slave","Queen","Heiress","Divorced"]
          AdjNotList = ["Bikini-Bod","Anal Virgin","Shave","Big-Titty","Little"]
          
          PhysChars = titmisc.PhysCharFemale()

          sAdj1 = titmisc.AttitudeGoodFemale().GetWord(NotList = AdjNotList)
          sAdj2 = PhysChars.GetWord(NotList = AdjNotList + [sAdj1])
               
          NotGirlList = NotGirlList + [sAdj1,sAdj2]
          Girl = char.FemaleChar(Type = GirlType.Good, NotList = NotGirlList,
                                   bAllowSpecies = False, bAllowSexuality = False, bAllowClothing = False, bAllowTitle = False, 
                                   bAllowAttitude = False, bAllowPhysChar = False,
                                   bAddTheArticle = True) 
          
          sTweet = sAdj1 + " & " + sAdj2 + ":\n"
          sTweet += Girl.Desc + "\n"
               
          iRand = randint(1,15)
          if iRand < 3:
               sTweet += "Exposes Her Naked Body " + WordList(["in a Wal-Mart","on Main Street","at the Grocery Store",
                                                                           "at the Mall","Downtown","on Campus","in Traffic",
                                                                           "at the Office","on the Beach","at the Park",
                                                                           "at Disneyland","on the Jumbotron"]).GetWord()
          elif iRand == 3:
               sTweet += "Has Her First " + WordList(["Threesome","Three-Way","Orgy"]).GetWord()
          elif iRand == 4:
               sTweet += "Has a " + WordList(["4","5","6","8","10","12","20","30","60"]).GetWord() + "-guy Gangbang"
          elif iRand == 5:
               sTweet += "Gets Her Cherry Popped"
          elif iRand == 6:
               sTweet += "Gets Her Anal Cherry Popped"
          elif iRand == 7:
               sTweet += "Goes Down On " + WordList(["a Butch Lesbian","Another Woman","Her Best Friend","Her Lesbian Boss",
                                                              "Her Maid of Honor","Her Bridesmaid","Her Mother-in-Law"]).GetWord()
          elif iRand == 8:
               sTweet += "Makes a Porno"
          elif iRand == 9:
               sTweet += "Tries Anal"
          elif iRand == 10:
               sTweet += "Wears a Butt Plug"
          elif iRand == 11:
               sTweet += "Tries a Glory Hole"
          elif iRand == 12:
               sTweet += "Pounds " + NamesMale().FirstName() + " with a Strap-On"
          else:
               ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
                                "Throbbing","Meaty","Burning","Dripping","Lustful","Passionate","Massive","Fat",
                                "Throbbing","Pulsating","Dripping","Black","Stiff","Girthy"])
               sTweet += WordList(["Rides","Sucks","Mounts","Takes"]).GetWord() + " "
               sTweet += AddArticles(ErectAdjs.GetWord()) + " " 
               sTweet += WordList(["Seven","Seven 1/2","Eight","Eight 1/2","Nine","Nine 1/2","Ten","Ten 1/2",
                                        "Eleven","Eleven 1/2","Twelve","Thirteen","Fourteen"]).GetWord() + "-inch "
               sTweet += WordList(["Dick","Cock","Boner","Prick","Tool"]).GetWord()
               
               

          return sTweet
          
class Generator31(Generator):
     # Wanton & Willing: 
     # My Kinky Lesbian Leather-Clad Dominatrix
     # Pegs Me With a Strap-On
     ID = 31
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotGirlList = ["Harem Princess"]
          Girl = char.FemaleChar(Type = GirlType.Bad, NotList = NotGirlList, bAllowSpecies = False)

          sAdj1 = ""
          sAdj2 = ""
          if CoinFlip():
               sAdj1 = titmisc.PhysCharFemale().GetWord()
               sAdj2 = titmisc.AttitudeBadFemale().GetWord()
          else:
               sAdj1 = titmisc.AttitudeBadFemale().GetWord()
               sAdj2 = titmisc.PhysCharFemale().GetWord()
               
          sHerName = NamesFemale().FirstName()
          
          sTweet = sAdj1 + " & " + sAdj2 + ":\n"
          
          if CoinFlip():
               sTweet += "My " + Girl.Desc + "\n"
          else:
               sTweet += sHerName + " the " + Girl.Desc + "\n"
               
          iRand = randint(1,13)
          if iRand < 3:
               ErectAdjs = WordList(["Swollen","Engorged","Turgid","Rock Hard","Bulging","Fully Erect","Hugely Erect","Veiny",
                                "Throbbing","Meaty","Burning","Dripping","Purple","Red","Fleshy","Lustful","Passionate",
                                "Throbbing","Pulsating","Vigorous","Virile","Moist","Black","Stiff","Girthy"])
               sTweet += "Gets a " + ErectAdjs.GetWord() + " " + str(randint(7,12)) + "\" Surprise"
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
               sTweet += "Gets " + WordList(["Fisted","Fisted","Anal Fisted"]).GetWord()
          elif iRand > 10 and iRand < 12:
               sTweet += WordList(["Wants","Craves","Is Horny for","Begs for"]).GetWord() + " " 
               sTweet += WordList(["Her Neighbor's","Her Step-Brother's","Her Professor's","Her Teacher's","Her Boss's",
                                        "Her Step-Dad's","Her Uncle's","Her Gym Coach's","Her Gynecologist's","A Stranger's"]).GetWord() + " "
               sTweet += WordList(["Dick","D","Cock","Hard Cock","Fat Dick","Dingus","Meat Stick","Flesh Pole","Fat Boner"]).GetWord()
          else: 
               sTweet += "Is Wearing " + WordList(["a Butt Plug","an Anal Hook","Nipple Clamps","a Ball Gag","a Clit Clamp",
                                                            "Crotchless Panties","a Strap-On","a Remote-Controlled Vibrator",
                                                            "Anal Beads"]).GetWord()
          return sTweet
          
class Generator32(Generator):
     #Stripping For My Best Friend's Cocky Coal-Miner Brother 
     ID = 32
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          #print(misc.RelateMale().List + misc.MaritalStatusMale().List)
          if CoinFlip():
               Master = char.MaleChar(bAllowGang = False, NotList = ['Single', 'Man', 'Dad', 'Father', 'Brother', 'Son'], bAllowMaritalStatus = False, bAllowRelate = False)
               if Master.Desc[-3:] == "Man":
                    sMaster = Master.Desc[0:-4]
               else:
                    sMaster = Master.Desc
               sTweet = WordList(["Sleeping With", "Hooking Up With", "Tempting", "Seducing", "Bedding", "Stripping For", "Secretly Watching", "Showering With", "Spying On", "Sharing", "Playing With", "Claimed By", "Taken By", "Deflowered By", "Dominated By", "Blackmailed By", "Stripped By", "Tied to the Bed By", "Pleasured By", "Spanked By", "Ravished By", "Taken Hard By", "Massaged By", "Going Down On", "Impregnated By"]).GetWord() + "\n"
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
               Girl = char.FemaleChar(NotList = ['Single','Virgin', 'Girl', 'Woman', 'Mom', 'Sister', 'Mother', 'Daughter', 'Lesbian', 'Maiden', 'Wife'], bAllowMaritalStatus = False, bAllowRelate = False, bAllowTitle = False)
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
          
class Generator33(Generator):
     #Milking Marie: A Pan-sexual Cheerleader Affair
     ID = 33
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sVerb = self.Gerunds.GetWord()
          
          Girl = char.FemaleChar(bAddAnArticle = True, sPosArticle = "My")
          sTweet = sVerb + " " + self.HerName + ":\n"
          sTweet += Girl.Desc + "\n" + self.SubtitleCoda.GetWord()

          return sTweet
          
# Rimming the Uptight Librarian Futa
# and her Mom
class Generator34(Generator):
     ID = 34
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          sVerb = self.Gerunds.GetWord()
          
          Girl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium, bAddTheArticle = True,
                                        bAllowPregState = False)
          sTweet = sVerb + " " + Girl.Desc
          
          sTweet += "\nand her " + WordList(['Mother', 'Step-Mom', 'Step-Daughter', 'Daughter', 'Sister', 
                                                       'Twin Sister', 'Best Friend', 'Lesbian Lover', 'Mom']).GetWord()

          return sTweet
          
class Generator35(Generator):
     ID = 35
     Priority = 1
     
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
          
class Generator36(Generator):
     #Turned Gay
     ID = 36
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          if CoinFlip():
               Girl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium,
                                             ExclList = [SpeciesMale])
               
               if CoinFlip():
                    Lesbian = char.LesbianChar(bAddTheArticle = True, NotList = ['wife','girlfriend', 'married','lesbo'],
                                                       ExclList = [SpeciesFemale])
                    sTweet = "Turned Lesbo by " + Lesbian.Desc
               else:
                    Lesbian = char.LesbianChar(NotList = ['wife','girlfriend', 'married', 'lesbian'],
                                                       ExclList = [SpeciesFemale])
                    sTweet = "Straight " + Girl.Desc + "\nfor the \nLesbian " + Lesbian.Desc 
               
          else:
               Man = char.MaleChar(bAllowGang = False, TempType = TempType.Medium,
                                        ExclList = [SpeciesFemale])
               
               if CoinFlip():
                    Gay = char.GayMaleChar(bAddTheArticle = True, NotList = ['husband','boyfriend', 'married','gay'])
                    sTweet = "Turned Gay by " + Gay.Desc
               else:
                    Gay = char.GayMaleChar(NotList = ['husband','boyfriend', 'married', 'gay'])
                    sTweet = "Straight " + Man.Desc + "\nfor the\nGay " + Gay.Desc 

          return sTweet

# My New Step-Dad Is
# A Tattooed Hard-Drinking Vegan Trillionaire
# and He's Hung Like a Horse!          
class Generator37(Generator):
     # 
     ID = 37
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NotList = ['Husband', 'Boyfriend', 'Hubby', 'Widower', 'Fiancé']
          Relations = titmisc.RelateMale()
          DickWords = WordList(["Boner","Cock","Dick","Penis","Schlong","Tool","Package","Erection"])
          Gerunds = self.Gerunds
          Dad = char.MaleChar(bAddEndNoun = True, bAllowGang = False, 
                                   bAllowMaritalStatus = False, bAllowRelate = False,
                                   bAllowAge = False, bAllowDickChar = False)
          
          sTweet += "My New " + Relations.GetWord(NotList = NotList) + " Is\n" + AddArticles(Dad.Desc, bMakeUpper = True)
          if CoinFlip():
               sTweet += "\nand " + WordList(["He's Hung Like a Horse",
                                                       "He Has a Massive " + DickWords.GetWord(),
                                                       "His " + DickWords.GetWord() + " is ENORMOUS"]).GetWord()
          sTweet += "!"

          return sTweet
          
class Generator38(Generator):
     # My New Step-Dad Is A Visibly-Erect Centaur
     ID = 38
     Priority = 1
     
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
          
class Generator39(Generator):
     # Taken Hard By My Big Black Biker 
     ID = 39
     Priority = 1
     
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

# class Generator40(Generator):
     # # I Was Ridden Bareback By A Burly Lumberjack Businessman, And He's Not My Husband!
     # ID = 40
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # NotVerbs = ['Tempted', 'Beaten', 'Broken', 'Captured', 'Caught', 'Charmed', 'Cuddled', 'Hotwifed', 'Ruled', 'Seduced', 'Tamed', 'Trained']
          
          # Master = MaleChar(iNumMaxCBits = 4, bAllowGang = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowSpecies = False)
          # if CoinFlip():
               # sTweet = self.HerName + " Gets " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nAnd He's Not Her Husband!"
          # else:
               # sTweet = "I Was " + self.VerbsBy.GetWord(NotList = NotVerbs) + " By A\n" + Master.Desc + "\nWho Was Not My Husband!"

          # return sTweet
          
class Generator41(Generator):
     #Seducing Sheryl: The Virginal Nurse and the Big Titty Dominatrix
     ID = 41
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Gerunds = WordList(["Seducing", "Tempting", "Corrupting", "Degrading", "Debauching", "Perverting", "Whipping",
                                   "Fisting", "Sixty-Nining", "Scissoring", "Tribbing", "Fingering"])

          GoodGirl = char.FemaleChar(Type = GirlType.Good, TempType = TempType.Medium,
                                             ExclList = [PregState, MaritalStatusFemale, SpeciesFemale, TitlesFemale])
          LesGirl = char.LesbianChar(Type = GirlType.Bad, bAddTheArticle = True, sPosArticle = "Her",
                                             ExclList = [AgeAdjFemale, MaritalStatusFemale, SpeciesFemale, TitlesFemale])
                                             
          sTweet = Gerunds.GetWord() + " " + self.HerName + ":\n"
          sTweet += "The " + GoodGirl.Desc + "\nand\n" + LesGirl.Desc 

          return sTweet
          
class Generator42(Generator):
     # Deflowered in the Pleasure Gardens of the Studly Bare-Chested Pirate Count
     ID = 42
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          VNotList = ["Sold", "Hotwifed", "Humiliated", "Massaged"]
          Nation = titmisc.NationMale()
          Title = titmisc.TitlesMale()
          SexPlaces = WordList(["Bed", "Dungeon", "Sex Dungeon", "Pleasure Gardens", "Harem"])
          Master = char.MaleChar(bAddEndNoun = False, bAllowTrope = False, bAllowRelate = False, 
                                        bAllowMaritalStatus = False, bAllowAge = False, bAllowProf = False, 
                                        bAllowSpecies = False,bAllowTypeMod = False, bAllowTitle = False)
          
          sTweet = self.VerbsBy.GetWord(NotList = ["Sold", "Hotwifed", "Public"]).upper() + "\n"
          sTweet += "in the " + SexPlaces.GetWord() + " of the\n" 
          sTweet += Master.Desc + " " + Title.GetWord()

          return sTweet

class Generator43(Generator):
     # Secret Baby for the Well-Hung Italian Count 
     #          - this is very similar to gen 10.
     ID = 43
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Nation = titmisc.NationMale()
          Title = WordList(titmisc.TitlesMale().GetWordList() + titmisc.TropesWealthyMale().GetWordList())
          
          Master = char.MaleChar(bAddEndNoun = False, TempType = TempType.Medium, bAllowRelate = False, 
                                      bAllowMaritalStatus = False, bAllowNation = False, 
                                      bAllowTitle = False, bAllowAge = False, bAllowProf = False)
          sTweet = WordList(["Secret Baby", "Illegal Baby", "Baby", "Twin Babies", "Secret Twin Babies", 
                                   "Fertile Surrogate", "Secret Surrogate", "Pregnant", "Secretly Pregnant", 
                                   "Illegally Pregnant"]).GetWord()
          sTweet += " for the\n" + Master.Desc + " " + Nation.GetWord() + " " + Title.GetWord()
          
          return sTweet
          
# class Generator44(Generator):
     # # The Amish French Maid Goes Dogging 
     # ID = 44
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # Girl = FemaleChar(iNumMaxCBits = 4, bAddArticle = True, bAllowRelate = True, bAllowSexuality = False, bAllowSpecies = False)
          # Suffixes = WordList(["Spreads Her Legs", "Spreads Her Legs", "Rides Again", "Puts Out", "Takes It Deep", "Rides A Big One", "Spreads Her Cheeks", "Takes A Roll In The Hay", "Assumes the Position", "Goes Down", "Has a Quickie", "Bends Over", "Goes Dogging", "Gets Laid", "Knocks Boots", "Does the Rumpy Pumpy", "Gets Off", "Goes All The Way", "Drops Her Pants"])

          # sTweet = Girl.Desc + "\n" + Suffixes.GetWord()
          
          # return sTweet
          
class Generator45(Generator):
     # The Sporty Black Farmer's Daughter
     # Gets Naked at the Museum!]
     ID = 45
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
class Generator46(Generator):
     ID = 46
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          if CoinFlip():
               Master = char.MaleChar(bAddEndNoun = False, NotList = ["boyfriend"], bAllowRelate = False, 
                                             bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, 
                                             bAllowTitle = False, bAllowTrope = False)
               Relations = titmisc.RelateMale()
               Prefix = WordList(["Secretly In Love With"])
               sTweet = Prefix.GetWord() + "\nMy " + Master.Desc + " " + Relations.GetWord(NotList = ["Boyfriend", "Husband", "Hubbie", "Widower", "Fiancé"])
          else:
               Girl = char.FemaleChar(bAddEndNoun = False, NotList = ["girlfriend"], bAllowRelate = False, 
                                             bAllowMaritalStatus = False, bAllowSpecies = False, bAllowAge = False, 
                                             bAllowTitle = False, bAllowTrope = False)
               Relations = titmisc.RelateFemale()
               Prefix = WordList(["Secretly In Love With"])
               sTweet = Prefix.GetWord() + "\nMy " + Girl.Desc + " " + Relations.GetWord(NotList = ["Girlfriend", "Mistress", "Wife"])
          return sTweet
          
# class Generator47(Generator):
     # # My Step-Dad Transforms Into A Cocky Gentleman Mer-Man!
     # ID = 47
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # Relate = titmisc.RelateMale()
          # Species = titmisc.SpeciesMale()
          # VerbTrans = WordList(["Transforms", "Transforms", "Changes", "Shifts", "Morphs", "Metamorphs"])
          
          # Master = MaleChar(bAddEndNoun = False, bAllowAge = False, bAllowMaritalStatus = False, bAllowNation = False, bAllowRelate = False, bAllowSpecies = False, bAllowTitle = False)
          
          # sTweet = "My " + Relate.GetWord() + " " + VerbTrans.GetWord() + "\ninto a\n" + Master.Desc + " " + Species.GetWord() + "!"

          # return sTweet
          
class Generator48(Generator):
     # Lusting For the Wicked Blonde Fetish Model
     ID = 48
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          GirlNotList = ['elf','skin','tanned','bronzed']
          Girl = char.FemaleChar(bAddTheArticle = True, NotList = GirlNotList, bAllowSpecies = False,
                                        ReqList = [SkinHairColorFemale],
                                        ExclList = [AgeAdjFemale,SexualityFemale,MaritalStatusFemale,PregState,NationFemale])
          
          sTweet = self.Gerunds.GetWord() + " " + Girl.Desc
          
          return sTweet          
          
class Generator49(Generator):
     # Taken Vigorously
     # in the Men's Restroom by
     # The Dominant Donkey-Dicked Italian Vegan Centaur
     ID = 49
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          PublicPlaces = WordList(["at the Bowling Alley", 
               "in the Produce Section", 
               "in the Baked Goods Section",
               "in the Bakery",
               "at the Wine Tasting",
               "on the Coffee Table", 
               "in the Restroom at Chiopotle", 
               "Behind the Chic-fil-a", 
               "in the Ball Pit", 
               "in the Whole Foods Parking Lot",
               "in the Men's Restroom",
               "in the Women's Restroom",
               "in the Park",
               "at the Beach",
               "on the Eliptical Machine at the Gym",
               "at the Seafood Restaurant",
               "at the Museum",
               "at the Library",
               "at the Farmer's Market",
               "next to the Duck Pond",
               "in the Window of a Shoe Store",
               "in the Hunting Section at a Wal-Mart",
               "in the Church Graveyard",
               "in the Old Castle Ruins",
               "at the Old Manor House",
               "in the Abandoned Mansion",
               "at the Construction Site",
               "next to the Assembly Line",
               "on a Hotel Balcony"
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
               
          Master = char.MaleChar(bAddTheArticle = True)
          
          if CoinFlip():
               sTweet = Verbs.GetWord()
          else:
               sTweet = Verbs.GetWord() + " " + Adverbs.GetWord() 

          sTweet += "\n" + PublicPlaces.GetWord() + " by\n" + Master.Desc

          return sTweet
          
class Generator50(Generator):
     # What's a Little Deep Throat Between Bros?
     ID = 50
     Priority = 1
     
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
               sTweet += NaughtinessStraight.GetWord() + " Between " + FriendsGen.GetWord()
          elif iRand == 2:
               #gay
               sTweet += NaughtinessGay.GetWord() + " Between " + FriendsGay.GetWord()
          else:
               #lesbian
               sTweet += NaughtinessLez.GetWord() + " Between " + FriendsLez.GetWord()
                    
          sTweet += "?"
          return sTweet

class Generator51(Generator):
     # Juliana the Nudist Damsel in:
     # The Kingdom of the Dildo-Bots
     ID = 51
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
               Girl = char.FemaleChar(Type = GirlType.Good, bAllowMaritalStatus = False, 
                                             bAllowSpecies = False, bAllowPregState = False)
          else:
               Girl = char.FemaleChar(Type = GirlType.Bad, bAllowMaritalStatus = False, 
                                             bAllowSpecies = False, bAllowPregState = False)
               
          sTweet = sName + " the " + Girl.Desc + " in:\n"     
          sTweet += "The " + Places.GetWord() + " of the " + Beings.GetWord()

          return sTweet
          
# My Hot Redhead Teacher
# Is Secretly
# A Stripper!
#            - needs work
class Generator52(Generator):
     ID = 52
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])

          SexyAdjs = WordList(["Hot","Sexy","Cute","Busty","Stacked","Thicc","Tanned","Bikini-Bod",
                                    "Chesty","Young","Nubile"
                                   ])
          sSexyAdj = SexyAdjs.GetWord()
          GoodJobs = WordList(["Teacher","English Teacher","Yoga Instructor","Librarian","Nanny","Math Tutor","Babysitter",
                                    "Nurse","Piano Teacher","Dance Teacher","Algebra Teacher","Biology Teacher","Personal Trainer",
                                    "House Maid","French Maid","Secretary","Intern","Assistant","Physical Therapist","Therapist",
                                    "Violin Teacher","Dance Instructor","Gym Coach","Volleyball Coach"
                                    ])
          sJob = GoodJobs.GetWord()
          
          GoodGirlNotList = [sSexyAdj,sJob,'Slave Girl','Concubine']
          GoodGirl = char.FemaleChar(Type = GirlType.Good, NotList = GoodGirlNotList, bAddEndNoun = False,
                                        bAllowTitle = False, bAllowPregState = False, bAllowSpecies = False, 
                                        bAllowMaritalStatus = False, bAllowAge = False)
                                        
          iTempID = choice([222,220,205,2,2,2])
          print("iTempID = " + str(iTempID))
          
          BadGirlNotList = [sSexyAdj,sJob,'Slave Girl','Concubine','Naked','Nude','Gymnast','Secretary']
          print("BadGirlNotList is " + str(BadGirlNotList))
          BadGirl = char.FemaleChar(TempType = TempType.Medium, NotList = BadGirlNotList, bAddAnArticle = True,
                                             SelectTemplateID = iTempID)
          
          BadGirlNotList = ['Nun','Nurse','Gymnast','Masseuse','Cheerleader','Starlet','Secretary','Housewife','Fashion Model','French Maid']
          if CoinFlip():
               sTweet += Exclamations.GetWord() + " "
          if CoinFlip():     
               sTweet+= "My " + sSexyAdj + " " + GoodGirl.Desc + " " + sJob + " Is Secretly\n" 
               sTweet+= BadGirl.Desc + "!"
          else:
               sTweet+= "My " + sSexyAdj + " " + GoodGirl.Desc + " " + sJob + " Is Secretly\n" 
               sTweet += BadGirl.Desc + "!"
          
          return sTweet     
          
# Daddy Found Out
# His Sweet Little Step-Daughter 
# Is a Sassy Asian Stripper 
# And Now He's Pissed!
#          - also needs work
class Generator53(Generator):
     ID = 53
     Priority = 1
     
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
class Generator54(Generator):
     ID = 54
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
                                        
          iLength = randint(8,12)
          sTweet = str(iLength) + " Inches of " + Weapons.GetWord() + ":\n"
          sTweet += "The " + LadyAdjs1.GetWord() + " " + LadyAdjs2.GetWord() + " " + Ladies.GetWord() + "\n"
          sTweet += "Encounters\n"
          
          sMonster = ""
          if CoinFlip():
               sMonster += MaleAdjs1.GetWord() + " "
          if CoinFlip():
               sMonster += MaleAdjs2.GetWord() + " "
          if CoinFlip():
               sMonster += DickAdjs.GetWord() + " "
               
          #print("Monster string is [" + sMonster.strip() + "]")
          if sMonster.strip():
               sMonster = AddArticles(sMonster)
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
class Generator55(Generator):
     ID = 55
     Priority = 1
     
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
          
          sTweet = "The " + sHerName + " Sandwich:\n"
          sTweet += sJob1 + " on Top,\n"
          sTweet += sJob2 + " on the Bottom,\n"
          sTweet += Girl.Desc + " in the Middle"

          return sTweet     
          
# The Kinky Brazillian Bikini Model
# is hot for
# Bald Men!
class Generator56(Generator):
     ID = 56
     Priority = 1
     
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
class Generator57(Generator):
     ID = 57
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Verbs = WordList(['Taken','Gang-Banged','Shared','Claimed','Taken Hard','Claimed Hard','Tied Up & Used','Deflowered',
                                'Fisted','Motor-Boated','Impregnated','Fertilized','Mounted Bareback','Ridden Hard','Pleasured',
                                'Ravished','Satisfied','Oiled Up','Paddled'])
          Teams = WordList(['Hockey Players','Football Players','Basketball Players','Sumo Wrestlers','Rugby Players',
                                'Baseball Players','Olympic Swimmers','Wrestlers','Soccer Players'])
          sTeam = Teams.GetWord()
          MenNotList = [sTeam, 'Single']
          Men = char.MaleChar(TempType = TempType.Medium, bAddEndNoun = False, NotList = MenNotList,
                              bAllowAge = False, bAllowAttitude = False, bAllowGenMod = False, bAllowRelate = False, bAllowTitle = False)
     
          sTweet += Verbs.GetWord() + " in the Locker Room\nby an Entire Team of\n" + Men.Desc + " " + Teams.GetWord()

          return sTweet     
          
# I hooked up with a strapping leather cowboy
# and now I'm pregnant!
class Generator58(Generator):
     ID = 58
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ManNotList = ["Widowed"]
          HookUpPhrases = WordList(["Hooked Up With", "Had a One Night Stand With", "Slept With", "Banged", "Had a Quickie With", "Fooled Around With"])
          MaleRelatives = WordList(["Step-Dad", "Step-Brother", "Brother", "Brother-in-Law", "Father", "Dad", "Daddy", "Step-Father"])
          Man = char.MaleChar(NotList = ManNotList, bAllowRelate = True, 
                                   bAllowSpecies = True, bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False)
          sMan = Man.Desc 
          
          if FoundIn(sMan, MaleRelatives.List):
               sTweet = "I " + HookUpPhrases.GetWord() +" My " + sMan + "\nAnd Now I'm Pregnant!"
          else:
               sTweet = "I " + HookUpPhrases.GetWord() +" " + AddArticles(sMan) + "\nAnd Now I'm Pregnant!"
          return sTweet
     
# # The hot bikini model prom queen
# # is secretly a lesbian      
# class Generator59(Generator):
     # ID = 59
     # Priority = 1
     
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
class Generator60(Generator):
     ID = 60
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          SweetAdjs = WordList(['Sweet', 'Sweet', 'Cute', 'Blonde','Innocent','Bashful','Naive'])
          NiceNames = WordList(['Amy','Angelica','Annie','Charity','Daisy','Daphne','Elsie',
                                     'Emmy','Frances','Gertrude','Greta','Jeanie','Lacey','Lizzy',
                                     'Mabel','Mary','Maryanne','Molly','Nancy','Nell','Olive','Phoebe',
                                     'Rosie','Shelly','Sophie','Summer','Virginia'])
          NiceGirlAdjs = WordList(['All-American','Amish','Apple-Bottomed','Athletic','Asian','Blue-Eyed',
                                         'Busty','Buxom','Country','Curvy','Freshman','Korean','Leggy','Modest','Nubile',
                                         'Pale','Repressed','Small-Town','Swedish','Teen Beauty Queen','Virgin'])
          NiceGirlNouns = WordList(['Babysitter','Cheerleader','Coed','Daddy\'s Girl','Farmer\'s Daughter',
                                          'Freshman','Geek Girl', 'Gymnast','Maiden','Nerd Girl','Schoolgirl','Southern Belle',
                                          'Step-Daughter','Teen Model','Virgin'])
          ObjectAdjs = WordList(['Demon-Possessed','Enchanted','Haunted','Magic','Magical'])
          ObjectNouns = WordList(['Anal Beads','Anal Hook','Ball Gag','Ben Wa balls','Bull Dyke','Butt Plug',
                                        'Clit Clamp','Clit Pump','Crotchless Panties','Dildo','11\" Dildo',
                                        'Double-Ended Dildo','Gimp Mask','Hitachi Magic Wand','Leather Riding Crop',
                                        'Nipple Clamps','Orgasmatron','Pearl Necklace','Rabbit Vibe','Rubber Fetish Suit','Sex Doll',
                                        'Sex Swing','Spreader Bar','Speculum','Strap-On','Sybian','Thong','Vibrator'])
          sNice1 = ""
          sNice2 = ""
          
          sTweet += NiceNames.GetWord() + " the " 
          if CoinFlip():
               sTweet += SweetAdjs.GetWord() + " "
          sTweet += "Little "
          if CoinFlip():
               sNice1 = NiceGirlAdjs.GetWord()
               sTweet += sNice1 + " "
          sNice2 = NiceGirlAdjs.GetWord(NotList = [sNice1])
          sTweet += sNice2 + " " + NiceGirlNouns.GetWord(NotList = [sNice1, sNice2]) + "\nand her\nAdventure with\n"
          sTweet += "The " + ObjectAdjs.GetWord() + " " + ObjectNouns.GetWord()
          
          return sTweet     

# class Generator61(Generator):
     # ID = 61
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Help!
# A husky investment banker
# has me chained up in his basement (garage/sex dungeon)
# naked!
class Generator62(Generator):
     ID = 62
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          BadNotList = ["Naked"]
          Exclamations = WordList(["Help!", "Help!", "Oh No!", "Uh Oh!", "What Do I Do?!?"])
          BadPlaces = WordList(["Basement", "Basement", "Dungeon", "Garage", "Attic", "Man Cave", "Den", "Sex Dungeon", "Cellar", "Secret Lair", "Secret Hideout", "Secret Love-Nest", "Swanky Bachelor Pad"])
          BadMan = char.MaleChar(bAddAnArticle = True, NotList = BadNotList, 
                                        bAllowSpecies = False, bAllowMaritalStatus = False, bAllowGang = False)
          
          sTweet = "\"" + Exclamations.GetWord() + "\n" + BadMan.Desc + "\nHas Me Chained Up In His " + BadPlaces.GetWord() + ",\nNaked!\""

          return sTweet     
          
# The Busty Blonde Flight Attendant's 
# Topless Miami Vacation
class Generator63(Generator):
     ID = 63
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = None
          if CoinFlip():
               Girl = char.FemaleChar(Type = GirlType.Good, bAddTheArticle = True, 
                                             bAllowClothing = False, bAllowRelate = False, bAllowSexuality = False, 
                                             bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, 
                                             bAllowTitle = False)
          else:
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddTheArticle = True, 
                                             bAllowClothing = False, bAllowRelate = False, bAllowSexuality = True, 
                                             bAllowSpecies = False, bAllowNation = True, bAllowMaritalStatus = False, 
                                             bAllowTitle = False)
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
class Generator64(Generator):
     ID = 64
     Priority = 1
     
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
class Generator65(Generator):
     ID = 65
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
          
          sTweet = self.HerName + " Gets " + Verbs.GetWord() + " By\n"
          sTweet += Numbers.GetWord() + " " +Adjs.GetWord() + " Naked " + Men.GetWord()

          return sTweet     

# The Bride Wore a Ball Gag          
class Generator66(Generator):
     ID = 66
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
                                     
          sTweet = "The Bride Wore " + BrideWore.GetWord()

          return sTweet     
          
# "Go easy on me! I'm a teenage coed nun
# and its my first time
# doing anal!"
class Generator67(Generator):
     ID = 67
     Priority = 1
     
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
          Girl = char.FemaleChar(Type = GirlType.Good, bAllowClothing = False, bAllowRelate = False, 
                                        bAllowNation = True, bAllowMaritalStatus = False, bAllowTitle = False, 
                                        bAllowPregState = False)

          sTweet = "\"" + Beginnings.GetWord() + "!\nI'm " + AddArticles(Girl.Desc) + "\nAnd Its My First Time\n" + FirstTimes.GetWord() + "!\""

          return sTweet     
          
# I know I'm married,
# but it can't hurt if I try rimming
# with this Italian Don Juan cowboy 
# just this once!
class Generator68(Generator):
     ID = 68
     Priority = 1
     
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
class Generator69(Generator):
     ID = 69
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Actions = WordList(["Spreads her Legs for","Spreads her Legs for","Bends Over for","Drops Her Panties for","Goes Down On","Lifts her Skirt for","Spreads her Thighs for","Spreads her Cheeks for","Opens Her Legs for","Lubes Herself Up for"])
          Girl = titmisc.NiceGirl()
          sNiceGirl = Girl.Desc
          
          Man = char.MaleChar(bAddTheArticle = True, bAllowRelate = False, bAllowMaritalStatus = True, 
                                   bAllowGang = False, bAllowTitle = True)
          
          iRand = randint(1,3)
          if iRand == 1:
               sTweet = "The " + Girl.Desc + "\n" + Actions.GetWord() + "\n" + Man.Desc 
          elif iRand == 2:
               sTweet = NamesFemale().FirstName() + " the " + Girl.Desc + "\n" + Actions.GetWord() + "\n" + Man.Desc 
          else:
               sTweet = "My " + Girl.Desc + "\n" + Actions.GetWord() + "\n" + Man.Desc
               
          return sTweet     
          
# I shot a porn scene
# with a handsome BBC construction worker
class Generator70(Generator):
     ID = 70
     Priority = 1
     
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
          
class Generator71(Generator):
     ID = 71
     Priority = 1
     
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
# is a Strapping Long Haul Truckers
# and He Sucked My Titties 
class Generator72(Generator):
     ID = 72
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ManNotList = ["Single"]
          Man = char.MaleChar(NotList = ManNotList, bAddAnArticle = True, bAllowGang = False,
                                   bAllowSpecies = True, bAllowMaritalStatus = False, bAllowTitle = False, 
                                   bAllowGenMod = True, bAllowTrope = False)
          Relations = WordList(["Co-worker","Boss","Boss","Step-Brother","Brother-in-Law","Son-in-Law","Step-Son",
                                        "Tutoring Student","Gym Coach","Personal Trainer","Massage Therapist",
                                        "Nextdoor Neighbor","Math Teacher","Math Tutor","English Teacher",
                                        "Literature Professor","Tennis Coach","Pool Boy"
                                        ])
          NaughtyStuff = WordList(["He Ate Me Out","He Ate My Ass","He Sucked My Titties","I Let Him Finger Me",
                                        "We Sixty-nined","I Let Him Fist Me","I Let Him Shave My Cooch","I Gave Him Head",
                                         "I Gave Him a Hand-Job","I Gave Him a Foot-Job","I Let Him Play With My Titties",
                                         "He Whipped My Bare Ass With a Riding Crop","I Sat On His Face",
                                         "He Spanked My Ass","I Gave Him Road Head","I've Seen Him Naked",
                                         "We Showered Together","I Jerked Him Off","I Dry-Humped Him",
                                         "I Gave Him a Rim-Job","He Wears a Cock Ring","He Has a Cock Piercing",
                                         "He Likes to be Pegged","We Did Butt Stuff","I Went Down On Him",
                                         "He Went Down On Me"])

          sTweet = "\"My New " + Relations.GetWord() + " is\n"
          sTweet += Man.Desc + "\n"
          sTweet += "and\n" + NaughtyStuff.GetWord() + "!\""
          
          return sTweet     

          return sTweet     
          
# class Generator73(Generator):
     # ID = 73
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # return sTweet     
          
class Generator74(Generator):
     ID = 74
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = titmisc.NiceGirl()
          sNiceGirl = Girl.Desc
          
          NaughtyStuff = WordList(["69ing", "an Anal Hook","Anal Sex","BBC","BDSM","Bukkake","a Butt Plug","a Clit Clamp","a Dirty Sanchez","Double Penetration","Erotic Asphyxiation","a Gang Bang",
                                              "an Interracial Threesome", "Leather Bondage","Lesbian Sex","Face-Sitting","Fisting","an Orgy","Nipple Clamps","Nudism","Rimming","Sex With Another Woman","Spanking",
                                              "Stripping at a Club","Swinging","a Threesome","Watching Porn","Water Sports","Whips and Chains","Wife Swapping"])
          Reactions = WordList(["Now She Can't Get Enough","She Loves It","She Wants More","Now She Won't Stop","Now She Won't Quit","Now She's Insatiable",
                                     "It Turned Her Into A Slut","It Turned Her Into A Sex-Crazed Bimbo","Now She's a Sex Addict","It Turned Her Into A Ho","It Turned Her Into a Lesbian",
                                     "Now She's a Professional Porn Star", "She Decided to Become a Porn Star","Now All She Does Is Masturbate","It Was Awkward and Not Really Her Thing"])

          sTweet = "My " + sNiceGirl + "\nTried " + NaughtyStuff.GetWord() + "\nAnd " + Reactions.GetWord() + "!"
                    
          return sTweet     

class Generator75(Generator):
     ID = 75
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Exclamations = WordList(["Oh S@*#!", "Oh No!", "WTF?!?", "Oh F*@%!"])
          Girl = titmisc.NiceGirl()
          sNiceGirl = Girl.Desc
          
          if CoinFlip():
               sTweet += Exclamations.GetWord() + " "
          sTweet += "My " + sNiceGirl + " Went Black and She Won't Come Back!"

          return sTweet     
          
# My New Neighbor is a 
# Tanned Redheaded Secretary
# and 
# I Ate Her Out
class Generator76(Generator):
     ID = 76
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
          sTweet = "\"My " + Relations.GetWord() + " is\n"
          sTweet += AddArticles(Girl.Desc) + "\n"
          sTweet += "and\n" + NaughtyStuff.GetWord() + "!\""
          
          return sTweet     
          
# "I was a fertile harem girl
# for a strapping black cowboy sheikh"
class Generator77(Generator):
     ID = 77
     Priority = 1
     
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
class Generator78(Generator):
     ID = 78
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""

          Gerunds = WordList(["69ing","Ass-Eating","Bedding","Binding","Breaking","Breeding","Caning","Claiming","Deflowering",
                                  "Defiling","Dominating","Edging","Exposing","Fingering","Fisting","Impregnating","Ogling","Milking","Motor-Boating",
                                   "Paddling","Peeing On","Penetrating","Pleasuring","Porking","Pumping","Rimming","Sharing","Shaving","Spanking","Spraying","Spread-Eagling",
                                   "Spit-Roasting","Stripping","Stuffing","Taking","Tasting","Tea-Bagging","Touching","Toying","Whipping",
                                   "Undressing","Using","Video-Taping"])
          SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
          sSubAdj = SubAdjs.GetWord()
          Girl = char.FemaleChar(NotList = [sSubAdj], bAllowClothing = True, 
                                        bAllowRelate = True, bAllowSexuality = True, bAllowSpecies = True, 
                                        bAllowMaritalStatus = True, bAllowTitle = True)
          
          sTweet = "His for the " + Gerunds.GetWord() + ":\n"
          sTweet += AddArticles(sSubAdj + " " + Girl.Desc) + " Story"
          return sTweet     
          
class Generator79(Generator):
     ID = 79
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          VerbsTo = WordList(["69","Anally Deflower","Bone","Chain Up","Claim","Claim Hard","Command","Deflower",
                                   "Degrade","Dominate","Enslave","Gag","Hotwife","Humiliate","Hypnotize","Impregnate",
                                   "Knock-Up","Lick","Master","Mind Control","Motor-Boat","Mount Roughly","Paddle",
                                   "Pee On","Penetrate","Pervert","Possess","Publicly Expose","Punish","Ride Hard","Shave",
                                   "Splooge On","Suck On","Take From Behind","Tame","Tea-Bag","Wife-Swap","Undress",
                                   "Use Sexually","Video-Tape"])

          SubAdjs = WordList(["Submissive","Submissive","Subservient","Compliant","Slave Girl","Obedient","Kinky"])
          sSubAdj = SubAdjs.GetWord()
          Girl = char.FemaleChar(NotList = [sSubAdj], TempType = TempType.Medium,
                                        bAllowClothing = True, bAllowRelate = True, bAllowSexuality = True, 
                                        bAllowSpecies = True, bAllowMaritalStatus = True, bAllowTitle = True)
          
          sTweet = "His To " + VerbsTo.GetWord() + ":\n"
          sTweet += AddArticles(sSubAdj + " " + Girl.Desc) + " Story"

          return sTweet     
          
# # When the Princess
# # Met the Cowboy...
# # ...and they had wild interracial sex!
# class Generator80(Generator):
     # ID = 80
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""
          
          # SexAdjs1 = WordList(["Wild","Illicit","Unbridled","Unprotected","Passionate","Hate-Fueled",
                                        # "Interracial","Wall-Banging","Steamy","Wanton","Lustful","Hot",
                                        # "Steamy","Lust-Fueled","Loud","Filthy"])
          # SexAdjs2 = WordList(["Illicit","Unbridled","Unprotected","Passionate","Extramarital",
                                        # "Interracial","Wild","Loud","Kinky"])
          # sSexAdj1 = SexAdjs1.GetWord()
          # sSexAdj2 = SexAdjs2.GetWord(NotList = [sSexAdj1])
          
          # ManNotList = []
          # Man = MaleChar(iNumMaxCBits = 3, iNumMinCBits = 2, NotList = ManNotList, bAddArticle = False, bAllowGang = False, bAllowRelate = False, bAllowAttitude = False, bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, bAllowNation = False)
          # GirlNotList = []
          # Girl = FemaleChar(iNumMaxCBits = 3, iNumMinCBits = 2, NotList = GirlNotList, bAddArticle = False, bAllowRelate = False, bAllowAttitude = False, bAllowSpecies = False, bAllowSkinHairColor = False, bAllowTitle = False, bAllowNation = False)

          # sTweet = "When the " + Girl.Desc + "\n"
          # sTweet += "Met the " + Man.Desc + "\n"
          
          # iRand = randint(1,3)
          # if iRand == 1:
               # PublicPlaces = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section",
                    # "on the Coffee Table","in the Restroom at Chiopotle","Behind the Dumpster","Behind the Chic-fil-a", 
                    # "in the Ball Pit", "in the Whole Foods Parking Lot","in the Men's Room","in a Stall in the Ladies Room",
                    # "on a Bench in the Park","Under the Boardwalk at the Beach","on the Eliptical Machine at the Gym",
                    # "at the Seafood Restaurant","in the Locker Room Showers","at the Museum","in the Non-Fiction Section at the Library",
                    # "at the Farmer's Market","in the Window of a Shoe Store","in the Auto Parts Section at a Wal-Mart",
                    # "in the Church Graveyard","in the Back of a Church","in a House They Broke Into","in a Motel 6",
                    # "next to the Assembly Line","on a Hotel Balcony","in Her Parents Bedroom","on the Floor of the Restroom",
                    # "in a Truck Stop Bathroom","in a Parking Garage","in a Changing Room"
                    # ])
               # sTweet += "...and They Had " + sSexAdj1 + ", " + sSexAdj2 + " Sex " + PublicPlaces.GetWord() + "!"
          # elif iRand == 2:
               # Gangs = WordList(["a Construction Crew","a Biker Gang","a Basketball Team","the Football Team","some Carnies",
                                        # "a Chain Gang","some Chippendales Dancers","some Coal Miners","the Cops","some Cowboys","some Firemen",
                                        # "a Hockey Team","Identical Triplets","a Men's Volleyball Team","the Guys at the Gym",
                                        # "some Rednecks","some Mountain Men","a Band of Pirates","a Rock Band","some Pro Wrestlers",
                                        # "some Sumo Wrestlers","a Rugby Team","a S.W.A.T. Team","a Viking Horde","a Werewolf Pack",
                                        # "a Group of Sailors","some Fraternity Brothers","some Professional Bull Riders",
                                        # "the Kappa Omega Kappa Fraternity House","some Gay-for-Pay Porn Stars"])
               # sTweet += "...and They Had " + WordList(["Group Sex","an Orgy","a Gang Bang"]).GetWord() + " With " + Gangs.GetWord() + "!"
          # else:
               # sTweet += "...and They Had " + sSexAdj1 + ", " + sSexAdj2 + " Sex!"
          
          # return sTweet     
          
# I Lost My Virginity To 
# A Tanned Leather Cowboy 
# And he was my old 7th grade chemistry teacher
class Generator81(Generator):
     ID = 81
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          ManNotList = (["Teenage","Young","College","Visibly Erect","Space"])
          Places = WordList(["at the Bowling Alley","in the Produce Section", "in the Baked Goods Section","in the Bakery",
               "Behind the Chic-fil-a", "in the Ball Pit","Behind a Bench in the Park","at the Beach","Under an Overpass",
               "on the Eliptical Machine at the Gym","In the Locker Room Showers","at the Seafood Restaurant","at the Museum",
               "at the Library","at the Farmer's Market","next to the Duck Pond","in the Back of a Church","On Top of the Bar",
               "in the Window Display of a Shoe Store","Under the Boardwalk","in the Hunting Section at a Wal-Mart",
               "in the Church Graveyard","in a White Van Under an Overpass","at the Construction Site","next to the Assembly Line",
               "on a Hotel Balcony","in a Room at a Motel 6","in my Parent's Bedroom","at the Pet Store","Beside the Bike Path",
               "Behind the Bleachers","Behind the Bar","In the Back Seat of a Prius","In the Back of a Ford 150",
               "In the Back Seat of a Volvo","In the Back of a Movie Theater"
               ])
          Retailers = WordList(["In-n-Out Burger","Whole Foods","Wal-Mart","Starbucks","Gold's Gym","LA Fitness","Krispy Kreme",
                                     "CVS","Target","Chipotle","Burger King","the Mall","IHOP","the Multiplex","an Apple Store"])
          
          Man = char.MaleChar(NotList = ManNotList, bAllowRelate = False, bAllowSpecies = False, 
                                   bAllowMaritalStatus = False, bAllowGang = False, bAllowTitle = False, 
                                   bAllowGenMod = False)

          if CoinFlip():
               sTweet = "I Lost My Virginity\n"
               sTweet += "to " + AddArticles(Man.Desc) + "\n"
          else:
               sTweet = "I Got My Cherry Popped\n"
               sTweet += "by " + AddArticles(Man.Desc) + "\n"
          
          iRand = randint(1,7)
          
          if iRand == 1:
               sTweet += "in the " + WordList(["Men's Room","Women's Restroom","Parking Lot"]).GetWord() + " " 
               sTweet += "at " + Retailers.GetWord()
          
          elif iRand == 2:
               sTweet += Places.GetWord()
          
          elif iRand == 3:
               sTweet += "and " + WordList(["Two","Two","Three","Three","Four","Five","Seven","Nine","Twelve","Thirteen","Twenty"]).GetWord() + " of His Buddies!"
          
          elif iRand == 4:
               iInches = randint(8,12)
               sTweet += "Who Used " + WordList(["a Cucumber","a Banana","an Eggplant","an Electric Toothbrush",
                              "a " + str(iInches) + "\" Black Dildo",
                              "a " + str(iInches) + "\" Steel Dildo"]).GetWord() + " On Me!"
          elif iRand == 5:
               sTweet += "Who Used To Be My " + WordList(["High School Chemistry Teacher","High School English Teacher","French Teacher",
                              "Gym Teacher","6th Grade Teacher","7th Grader Teacher","8th Grade Teacher","Chemistry Teacher","Algebra Teacher",
                              "Literature Professor","Boss","Boss at " + Retailers.GetWord(),"Math Tutor","Next Door Neighbor","Gym Coach","Track Coach",
                              "Basketball Coach","Pediatrician","Gynecologist"]).GetWord() + "!"
          elif iRand == 6:
               sTweet += "and Then I Realized He Was " + WordList(["My New Step-Dad","My New Step-Brother",
                              "My New Next Door Neighbor","My New Brother-in-Law","My Literature Professor",
                              "My Biology Professor","My Gynecologist", "My Mom's New Boyfriend"]).GetWord() + "!"
          else:
               sTweet += WordList(["Live on Television!","Live on the Internet!","And He Gave Me $100!",
                                        "And My Dad Was Pissed When He Found Out!","And I Let His Friends Watch!",
                                        "And a Cop Caught Us!","And We Filmed the Whole Thing!",
                                        "In the Basement of His Parents House!","Upstairs at His Parents House!",
                                        "And He Didn't Pull Out!","And He Did My Ass Too!","And Then My Parents Came Home!",
                                        "And His Sexy Wife!","And Now I'm Pregnant!"]).GetWord()
          
          return sTweet     
          
# "I'm a Pregnant Asian Waitress
# and
# I'm Stripping 
# For a Well-Hung Millionaire Sheikh!" (alt: I'm a pregnant asian waitress: what am I doing stripping for...??)
class Generator82(Generator):
     ID = 82
     Priority = 1
     
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
class Generator83(Generator):
     ID = 83
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          NiceGirl = titmisc.NiceGirl()
          
          NaughtyStuff = WordList(["69", "an Anal Hook","Anal Sex","BBC","BDSM","a Butt Plug","a Clit Clamp",
                                         "a Dirty Sanchez","Double Penetration","Erotic Asphyxiation",
                                         "an Interracial Threesome", "Leather Bondage","Lesbian Sex","Face-Sitting",
                                         "Fisting","Nipple Clamps","Stripping at a Club","a Threesome",
                                         "Watching Hardcore Porn","Butt Stuff","Anal Fisting","Edible Lube",
                                         "Water Sports","Whips and Chains","Wife Swapping","Anal Beads",
                                         "Getting Her Clit Pierced","Eating Ass","Ass-to-Ass","a Clit Pump",
                                         "an Ass Vibe","a 12 inch Steel Dildo"])
          Extras = WordList(["with the Pope","with the Dalai Lama","with Miss America","with Her Step-Dad",
                                 "with Her Step-Mom","with Her Step-Brother","with Her English Teacher",
                                 "with Her Gym Coach","with Her Guidance Counselor","with Her Literature Professor",
                                 "with Her Gynecologist","at the Zoo","in a Starbucks Restroom",
                                 "in Her Parents Bedroom","in the Locker Room","at College","with Her Best Friend",
                                 "with Her Tinder Date","at the Aquarium","with Her SCUBA Partner",
                                 "with a Police Officer","with a 65-Year-Old Man","with Her Lab Partner",
                                 "on the Coffee Table","on the Dining Room Table","on the Hotel Balcony",
                                 "with a Total Stranger"])

          sTweet = "The " + NiceGirl.Desc + "\nTries " + NaughtyStuff.GetWord() 
          if CoinFlip():
               sTweet += "\n" + Extras.GetWord() + "!"

          return sTweet     
          
# Busty Princess Sophie
# Gets Tea-Bagged by the Goat Men
class Generator84(Generator):
     ID = 84
     Priority = 1
     
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

class Generator85(Generator):
     ID = 85
     Priority = 1
     
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
class Generator86(Generator):
     ID = 86
     Priority = 1
     
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
# class Generator87(Generator):
     # ID = 87
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Last Night a Sexy Dominatrix (Honey, A Sexy Dominatrix)
# Forced Me 
# To Eat Her Ass 
class Generator88(Generator):
     ID = 88
     Priority = 1
     
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
class Generator89(Generator):
     ID = 89
     Priority = 1
     
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
class Generator90(Generator):
     ID = 90
     Priority = 1
     
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
class Generator91(Generator):
     ID = 91
     Priority = 1
     
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
# class Generator92(Generator):
     # ID = 92
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Veronica Puts On Latex (Leather/A Butt Plug):
# Let the Hotwife Games Begin! (Bondage/BDSM/Dominatrix)
# class Generator93(Generator):
     # ID = 93
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# "I'm a Stay-at-Home Mommmy Blogger
# And A Billionaire Biker
# Spooned Me Hard!"
# class Generator94(Generator):
     # ID = 94
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# Welcome to Pound Town, Miss Dixon!
class Generator95(Generator):
     ID = 95
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Suffixes = WordList(["berg","berg","ville","ville","town"," Town"," City"])
          sLastName = ""
          sLastName = InnuendoLastNames().GetWord() 
          
          if CoinFlip():
               #For a woman
               Prefixes = WordList(["Drill","Fuchs","Cocks","Pound","Ball","Dix","Pricks","Shafts","Bawl","Cox","Pecker",
                                         "Bang","Peen","Swallow","Pork"])
                                         
               sTweet = "\"Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", " + WordList(["Miss","Mrs"]).GetWord() + " " + sLastName + "!\""
          else:
               #For a man
               Prefixes = WordList(["Beaver","Boob","Ass","Buttes","Kuntz","Slutt","Fuchs","Tits","Brest","Blow","Suck",
                                         "Bang","Anal","Muff","Pork","Booty"])
               sTweet = "\"Welcome to " + Prefixes.GetWord() + Suffixes.GetWord() + ", Mr. " + sLastName + "!\""                

          return sTweet     
          
# In Love With
# My Innocent Amish Maid's 
# Enormous Coconuts 
class Generator96(Generator):
     ID = 96
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = titmisc.NiceGirl(NotList = ['Wife','Girlfriend'])
          SizeAdj = WordList(['Enormous','Gigantic','Titantic','Humongous','Massive','Sumptuous','Milky','Giant',
                                   'Honking','Juicy','Jiggling','Double D','Magnificent','Gargantuan','Jumbo',
                                   'Heavenly'])
          Breasts = WordList(['Coconuts','Tatas','Breasticles','Gazongas','Titties','Mammaries','Melons',
                                   'Cantaloups','Jugs','Fun-Bags','Jubblies','Knockers','Hooters','Bazooms','Bosoms',
                                   'Milk Balloons','Juice-Bags','Sweater-Zeppelins','Grapefruits','Pumpkins',
                                   'Grand Tetons','Hangers','Bongos','Meat-Melons','Love-Pillows','Udders'])
                                   
          sTweet = WordList(["In Love With","Falling For","Head-Over-Heels For","Captivated By",
                                 "Bewitched By","Entranced By","Enraptured By","Spellbound By"]).GetWord()
          sTweet += "\nMy " + Girl.Desc + "'s\n"
          sTweet += SizeAdj.GetWord() + " " + Breasts.GetWord()

          return sTweet     

# The Secretary 
# is wearing
# a butt plug          
class Generator97(Generator):
     ID = 97
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Accessories = WordList(['a Butt Plug','Anal Beads','Nipple Clamps','a Clit Clamp','a Strap-On',
                                        'an Anal Hook','a Remote-Controlled Vibrator','Crotchless Panties',
                                        'Edible Panties','Nipple Pasties','a Pony Tail Butt Plug',
                                        'Assless Chaps','a Ball Gag','a Rubber Fetish Mask','a Latex Body Suit',
                                        'a Rubber Fetish Suit','a Transparent Bikini','a Chastity Belt'])
          
          Lady = char.FemaleChar(SelectTemplateID = 1, TempType = TempType.Medium, bAddTheArticle = True)

          sTweet = Lady.Desc + "\nIs Wearing\n" + Accessories.GetWord()

          return sTweet     
          
class Generator98(Generator):
     ID = 98
     Priority = 1
     
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
                                         
          MaleAdjs = WordList(titmisc.PhysCharMale().List + titmisc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','DILF','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
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
          
class Generator99(Generator):
     ID = 99
     Priority = 1
     
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
                                         
          MaleAdjs = WordList(titmisc.PhysCharMale().List + titmisc.DickCharMale().List + ['Giant','Enormous','Black','Black','Married','Heavily-Tattooed','DILF','Naked','Nudist','Virile','Wealthy','Millionaire','Billionaire'])
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
class Generator100(Generator):
     ID = 100
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlAdj = WordList(titmisc.PhysCharFemale().List + ['Fertile','Naked','Sassy','Saucy','Sexy','Black','Ebony','Bisexual'])
          GirlNoun = WordList(titmisc.ProfGoodFemale().List + titmisc.SpeciesFemale().List)
          Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
                                   "Daughter-in-Law","Cousin"])
                         
          
          sTweet = "I Secretly Impregnated\nMy " 
          if CoinFlip():
               FemRelate = char.FemaleChar(SelectTemplateID = randint(8,9),NotList = ['wife','girlfriend','Fiancé','concubine'])
               sTweet += FemRelate.Desc
          else:
               FemRelate = char.FemaleChar(SelectTemplateID = randint(8,9),NotList = ['sister','mom','mother'])
               MaleRelate = WordList(["Best Friend's","Step-Father's","Dad's","Boss's","Neighbor's"])
               sTweet += MaleRelate.GetWord() + "\n" + FemRelate.Desc

          return sTweet     
          
# Butt Stuff 
# With My 
# Biology Professor (Spanish Teacher / Math Tutor)
# class Generator101(Generator):
     # ID = 101
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
     
# Backdoor Lovin'
# for the 
# Jiggling Farmer's Daughter     
class Generator102(Generator):
     ID = 102
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
class Generator103(Generator):
     ID = 103
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(bAllowAttitude = False, bAllowMaritalStatus = False, bAllowPregState = False, bAllowAge = False)
          Relate = WordList(["Mother-in-Law","Step-Mom","Sister-in-Law","Step-Sister","Half Sister","Step-Daughter",
                                   "Daughter-in-Law","Cousin"])
                              
          sTweet = "My " + Relate.GetWord() + " is\n"
          sTweet += AddArticles(Girl.Desc) + ",\n"
          sTweet += "and " + WordList(["I Got Her Pregnant","I Got Her Pregnant","I Knocked Her Up"]).GetWord() + "!"

          return sTweet     
          
# Claimed on the Coffee Table
# by a Burly Centaur Sailor
class Generator104(Generator):
     ID = 104
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Verbs = WordList(['Claimed','Claimed Forcefully','Claimed Hard','Deflowered','Impregnated','Knocked Up',
                                   'Motor-Boated','Mounted','Paddled','Pleasured','Ravished','Ravished','Satisfied',
                                   'Taken','Taken Forcefully','Taken From Behind','Taken Roughly'])
          Location = WordList(['On the Coffee Table','On the Bathroom Floor','On the Kitchen Counter',
                                    'In the Back Seat','On a Park Bench','On the Washing Machine',
                                    'Under a Jungle Gym','On a Merry-Go-Round','On an Elliptical Machine',
                                    'On a Treadmill','On a Trampoline','In a Kiddie Pool','On a See-Saw',
                                    'On the Dining Room Table','On an Ikea Futon'])
          ManNotList = ['Single']
          Man = char.MaleChar(bAddAnArticle = True, bAllowGang = False, bAllowTitle = False)
          
          sTweet = Verbs.GetWord() + " " + Location.GetWord() + "\nby " + Man.Desc

          return sTweet     

# Brigitte Gets Claimed by 
# The Well-Hung Naked Manor Lord 
# On the Back of a Horse          
class Generator105(Generator):
     ID = 105
     Priority = 1
     
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
class Generator106(Generator):
     ID = 106
     Priority = 1
     
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
class Generator107(Generator):
     ID = 107
     Priority = 1
     
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
          
          Prefix = WordList(["Claimed at", "Enslaved at", "Taken at", "Imprisoned at", "Claimed at","The Dungeons of",
                                   "The Halls of","The Prisoner of","The Princess of","The Master of","The Baron of",
                                   "Deflowered at","Despoiled at","Ravished at","Seduced at","The Knight of",
                                   "The Lady of","The Virgins of","The Baroness of","The Dutchess of",
                                   "Naked at","The Harem Girls of","The Maidens of","The Queen of",
                                   "The Mistress of","The Wizard of","Betrayed at"])
          
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
          
          sTweet = Prefix.GetWord() + " Castle "
          
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
class Generator108(Generator):
     ID = 108
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemAdjNotList = ['Naked','Nudist', 'Bare-Shaven','Anal','Polynesian','Japanese','Brazilian',
                               'Elvish']
          Girl = char.FemaleChar(SelectTemplateID = 17, bAddTheArticle = True, NotList = FemAdjNotList)
          Man = char.MaleChar(bAllowGang = False, bAddTheArticle = True, TempType = TempType.Medium, bAllowRelate = False)
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(["Makes Love to","Is Ravished by","Jumps into Bed with","Gets Bedded by","Spends the Night with",
                                   "Has a Wild Night of Passion with","Has a Forbidden Affair with","Is Claimed by"]).GetWord() + "\n" 
          sTweet += Man.Desc + "!"

          return sTweet     

# The Modest Swedish Cheerleader
# Does a Naughty Strip-Tease          
class Generator109(Generator):
     ID = 109
     Priority = 1
     
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
class Generator110(Generator):
     ID = 110
     Priority = 1
     
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
class Generator111(Generator):
     ID = 111
     Priority = 1
     
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
class Generator112(Generator):
     ID = 112
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          SexyAdjs = WordList(['Sexy','Naughty','Erotic','Dirty','Steamy','Filthy','Shameless','Explicit','X-Rated'])
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList)
          
          sTweet = "My " + Girl.Desc + "\n"
          sTweet += "Isn't Wearing Any Panties!"

          return sTweet     
          
# A Wholesome Amish Babysitter
# Eats Out Jasmine          
class Generator113(Generator):
     ID = 113
     Priority = 1
     
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
class Generator114(Generator):
     ID = 114
     Priority = 1
     
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
class Generator115(Generator):
     ID = 115
     Priority = 1
     
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
class Generator116(Generator):
     ID = 116
     Priority = 1
     
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
class Generator117(Generator):
     ID = 117
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          FemNotList = ['Naked','Nudist','Bikini','Lingerie','Nude']
          Girl = char.FemaleChar(SelectTemplateID = 17, NotList = FemNotList, bAddAnArticle = True)
          
          sTweet = Girl.Desc + "\n"
          sTweet += WordList(['Pees on','Fists','Paddles','Whips','Ties Up','Pegs','Uses a Steel Dildo on',
                                   'Uses a Riding Crop on','Takes a Shit on','Urinates on','Chokes',
                                   'Forcibly Feminizes','Poops on','Handcuffs',
                                   'Puts a Leash and Dog Collar on','Spanks']).GetWord() + " " 
          sTweet += self.HisName + "!"

          return sTweet     
     
# I Found Out I Was a Lesbian
# When an Oiled-Up Flight Attendant Ate My Ass      
class Generator118(Generator):
     ID = 118
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          CharNotList = ['Uptight','Virgin','Male Model','Quarterback','Male Stripper','Camp Counselor','Business Man','Slave',
                              'Defensive Lineman','Virtuous']
          Lesbian1 = char.LesbianChar(bAddAnArticle = True, bAddEndNoun = False, NotList = CharNotList,
                                             ReqList = [LesFemaleAdj],
                                             ExclList = [MaritalStatusFemale, SexualityFemale, PregState, TitlesFemale])
          GirlJobs = titmisc.ProfFemale()
          GuyJobs = titmisc.ProfMale()
                                        
          sTweet = "I Found Out I Was a Lesbian When\n"
          # if CoinFlip():
          sTweet += Lesbian1.Desc + " " + GirlJobs.GetWord()
          # else:
               # sTweet += Lesbian2.Desc + " Lady " + GuyJobs.GetWord()
          sTweet += "\n" + WordList(["Ate My Ass", "Ate Me Out", "Ate My Pussy", "Licked My Snatch", "Scissored Me",
                                           "Rode My Face", "Rode Me With a Strap-On", "Fisted Me", "Fisted My Butt",
                                           "Sucked My Tits", "Ate Out My Snatch", "Rimmed My Butthole",
                                           "Sucked My Titties"]).GetWord()
                                           
          return sTweet     
          
class Generator119(Generator):
     ID = 119
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ['Single','Slave','Nude','Naked','Tanned']
          Girl = char.FemaleChar(bAddTheArticle = True, Type = GirlType.Good, NotList = GirlNotList)
          
          sTweet = Girl.Desc + "\nGets An Enema"

          return sTweet     

# The Randy Hairy Vegan Gunslinger Multi-Billionaire
# Gets An Enema          
class Generator120(Generator):
     ID = 120
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GuyNotList = ['Single']
          Guy = char.MaleChar(bAddTheArticle = True, bAllowGang = False, NotList = GuyNotList,
                                   bAllowTitle = False, bAllowSpecies = False)
          
          sTweet = Guy.Desc + "\nGets An Enema"

          return sTweet     
          
# Massaging Mrs. Mountcox:
# A Sadistic Bisexual MILF Story
class Generator121(Generator):
     ID = 121
     Priority = 1
     
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
class Generator122(Generator):
     ID = 122
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
          MILF = char.FemaleChar(SelectTemplateID = 223, NotList = MILFNotList,bAddTheArticle = True)
                                   
          sTweet = NaughtyStuff.GetWord() + " for " + MILF.Desc 

          return sTweet     

# Lady Constance is Claimed Vigorously
# by The Gruff Hairy Well-Hung Manor Lord
# at Bonkalot Keep          
class Generator123(Generator):
     ID = 123
     Priority = 1
     
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
class Generator124(Generator):
     ID = 124
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Undead = WordList(['Undead','The Ghost of','Zombie','Vampire','Werewolf'])
          Celebs = WordList(['Richard Nixon','JFK','Abraham Lincoln','Elvis Presley','Winston Churchill','Mahatma Gandhi',
                                   'Jim Morrison','Tupac','Buddy Holly','George Washington','Albert Einstein','Mao Zedong',
                                   'Humphrey Bogart','Babe Ruth','Colonel Sanders','Napoleon','Bela Lugosi','Groucho Marx',
                                   'Steve Jobs','Mr Rogers','Marlon Brando','Bing Crosby','Jimmy Stewart','Clark Gable',
                                   'James Dean','H.P. Lovecraft','Orson Welles','Henry Kissinger','Sonny Bono','Jimmy Hoffa',
                                   'Charlton Heston','Hugh Hefner','Yul Brynner','Carl Sagan','Yuri Gagarin','Jerry Lewis',
                                   'Benny Hill','Bob Ross','Joe DiMaggio','Don Knotts','Vincent Price','Adam West',
                                   'Frank Sinatra','Casey Kasem','Karl Marx','Jacques Cousteau','Salvador Dali',
                                   'Bob Hope'])
          Verbs = WordList(['Plowed','Banged','Porked','Drilled','Humped','Made Love to','Nailed','Reamed',
                                'Screwed','Shagged','Stuffed','Cream-pied','Ravished','Ate Out','Sixty-nined',
                                'Boned',])
          
          GirlNotList = ['Single','Mature Woman','Virgin','Unshaven','Maiden','Married','Recently-Divorced']
          Girl = char.FemaleChar(bAddEndNoun = False, NotList = GirlNotList, TempType = TempType.Flowery, Type = GirlType.Good,
               bAllowProf = False, bAllowPregState = False, bAllowAttitude = False, bAllowSpecies = False,
               bAllowTitle = False, bAllowMaritalStatus = False,)
          
          sTweet = Undead.GetWord() + " " + Celebs.GetWord() + " " + Verbs.GetWord() + " "
          sTweet += "My " + Girl.Desc + " " + WordList(["Wife","Wife","Girlfriend"]).GetWord() + "!"                         

          return sTweet     
          
# The Chaste Secretary
# Gets Deflowered by The Brawny Manly Space Dinosaur Gargoyle          
class Generator125(Generator):
     ID = 125
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = titmisc.NiceGirl()
          
          Master = char.MaleChar(bAddTheArticle = True, sPosArticle = "Her", bAllowRelate = True)
          
          sTweet = "The " + Girl.Desc + "\n"
          sTweet += "Gets " + self.VerbsBy.GetWord(NotList = ["Sexually Harrassed At My Workplace","Cuddled"]) + " "
          sTweet += "by " + Master.Desc
          
          return sTweet     
          
class Generator126(Generator):
     # Sitting On My Well-Hung Sumo-Wrestler Step-Dad's Face
     ID = 126
     Priority = 1
     
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
class Generator127(Generator):
     ID = 127
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Gang = char.GangMaleChar(bAddTheArticle = True, bAllowGenMod = False, bAllowTypeMod = False, bAllowProf = False,
                                             bAllowSpecies = False)
          
          sTweet = self.HerName + " " + WordList(["Gets Naked for","Strips Naked for","Twerks Naked for","Undresses for",
                                                            "Exposes Her Nubile Naked Body to","Shamelessly Strips Naked for",
                                                            "Goes Skinny-Dipping with","Does a Shameless Strip-Tease for",
                                                            "Takes All Her Clothes Off in front of","Shows Her Tits to",
                                                            "Takes Her Top Off for"]).GetWord() + " "
          sTweet += Gang.Desc 

          return sTweet     
          
# Penetrated by the Well-Endowed Dinosaur Space Alien Rodeo Clowns
# on Uranus!
class Generator128(Generator):
     ID = 128
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Verbs = WordList(['Boned','Bred','Claimed','Cream-Pied','Drilled','Fisted','Humped','Mounted',
                                'Nailed','Pleasured','Plowed','Porked','Ravished','Reamed','Punished',
                                'Rimmed','Spanked','Shagged','Shaved','Stuffed','Taken','Whipped','Licked',
                                'Pegged'])
          AlienPrefixes = WordList(['Alien','Space','Space Alien'])
          AlienNouns = WordList(['Body Builders','Bull Riders','Chippendales Dancers','Coal Miners',
                                        'Construction Workers','Cops','Cowboys','Defensive Linemen','Doctors',
                                        'Fire Fighters','Frat Boys','Long Haul Truckers','Lumberjacks',
                                        'Male Escorts','Male Models','Male Nurses','Male Strippers',
                                        'Matadors','Pirates','Roadies','Rodeo Clowns','Sailors','Stuntmen',
                                        'Sumo Wrestlers','Surfers','Surgeons','Biker Gang','DILFs','Jocks',
                                        'Billionaires','Millionaires','Sugar Daddies','Leather Daddies',
                                        'Bounty Hunters','Barbarians','Businessmen','Werewolves',
                                        'Drag Queens','Muscle Marys'])
          MaleNotList = ['Space']
          AlienPref = char.MaleChar(bAddEndNoun = False, bAllowGang = False, NotList = MaleNotList, 
               ExclList = [MaritalStatusMale, TitlesMale, NationMale, SpeciesMale, AttitudeMale])
          AlienNoun = char.GangMaleChar(bAddEndNoun = True, NotList = MaleNotList, TempType = TempType.Short,
               ExclList = [TitlesMale, NationMale, SpeciesMale])     
          Alien = char.MaleChar(bAddEndNoun = False, bAllowGang = False, NotList = MaleNotList, 
               ExclList = [MaritalStatusMale, TitlesMale, NationMale,SpeciesMale,AttitudeMale])
          
          sTweet = Verbs.GetWord() + " by the "
          if CoinFlip():
               sTweet += AlienPref.Desc + " " + AlienPrefixes.GetWord() + " " + AlienNoun.Desc
          else:
               sTweet += Alien.Desc + " Space Men"
          sTweet += "\non Uranus!"

          return sTweet     
          
class Generator129(Generator):
     ID = 129
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ['Call-Girl','Escort','Slave','Whore','Stripper','Green-Skinned']
          ManNotList = ['Million','Billion','Trillion','Gazillionaire']
               
          Guy = char.MaleChar(NotList = ManNotList, bAddTheArticle = True, TempType = TempType.Medium, 
                                   bAllowTrope = False, bAllowSpecies = False,
                                   ReqList = [RaceMale], 
                                   ExclList = [SpeciesMale,SkinHairColorMale,NationMale,TitlesMale,ProfRockstarMale])

          GirlNotList = GirlNotList + Guy.GetWordList()
          if 'Latino' in GirlNotList:
               GirlNotList.append('Latina')          
          
          iRand = randint(1,3)
          if iRand == 1:
          # Sexy White Girl for the Black Man
               print("<A>")
               Girl = char.FemaleChar(ReqList = [RaceFemale], ExclList = [SpeciesFemale,SkinHairColorFemale,NationFemale,SexualityFemale], NotList = GirlNotList)
               sTweet = Girl.Desc + " for " + Guy.Desc
          elif iRand == 2:
          # Sexy Mermaid for the Black Man
               print("<B>")
               Girl = char.FemaleChar(ReqList = [SpeciesFemale], ExclList = [SkinHairColorFemale,NationFemale,SexualityFemale], NotList = GirlNotList)
               sTweet = Girl.Desc + " for " + Guy.Desc
          else:
          # Black Mermaid Secretary for the Black Man
               print("<C>")
               Girl = char.FemaleChar(ReqList = [SpeciesFemale,RaceFemale], ExclList = [SkinHairColorFemale,NationFemale,SexualityFemale], NotList = GirlNotList)
               
               sTweet = Girl.Desc + " for " + Guy.Desc

          return sTweet     
          
# Black Merman Quarterback for the White Playboy Centerfold
class Generator130(Generator):
     ID = 130
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          GirlNotList = ['Call-Girl','Escort','Slave','Whore']
          ManNotList = ['Bob']
          
          Woman = char.FemaleChar(bAddTheArticle = True, TempType = TempType.Medium, 
                                        NotList = GirlNotList, bAllowSpecies = False, 
                                        ReqList = [RaceFemale],
                                        ExclList = [SpeciesFemale])
          ManNotList = ManNotList + Woman.GetWordList()
          if 'Latina' in ManNotList:
               ManNotList.append('Latino')
          print("ManNotList is " + str(ManNotList))
          
          iRand = randint(1,3)
          if iRand == 1:
          # Sexy White Trucker for the Black Stay-at-Home Mom
               print("<A>")
               Man = char.MaleChar(NotList = ManNotList, bAllowSpecies = False,
                                        ReqList = [RaceMale])
               sTweet = Man.Desc + " for " + Woman.Desc
          elif iRand == 2:
          # Black Fighter Pilot Cowboy for the Asian Secretary
               print("<B>")
               Man = char.MaleChar(NotList = ManNotList, ReqList = [SpeciesMale])
               sTweet = Man.Desc + " for " + Woman.Desc
          else:
          # Black Centaur Cowboy for the Latina Flight Attendant
               print("<C>")
               Man = char.MaleChar(NotList = ManNotList, 
                                        ReqList = [SpeciesMale,RaceMale])
               sTweet = Man.Desc + " for " + Woman.Desc


          return sTweet     
          
# I watched my wife and an Italian cowboy dinosaur make a porno!
class Generator131(Generator):
     ID = 131
     Priority = 1
     
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
          
# In Love With
# My Dentist's 
# Magnificent Meat-Missile
class Generator132(Generator):
     ID = 132
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
                                 
          sTweet += "\nMy " + Guy + "'s\n"
          
          iRand = randint(1,3)
          if iRand == 1:
               sTweet += BallSizeAdj + " " + Balls
          else:
               sTweet += CockSizeAdj + " " + Cock

          return sTweet     
          
# Forbidden Heat
# A pseudo-incest gorilla double anal story
class Generator133(Generator):
     ID = 133
     Priority = 1
     
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

          sTweet = "~" + sTitle1.upper() + " " + sTitle2.upper() + "~\n\n"
          sTweet += AddArticles(sSubTitle1).lower() + " " + sSubTitle2.lower() + " " + sSubTitle3.lower() + " story"
          
          return sTweet     
          
# Taken by her Lesbian Centaur Boss
class Generator134(Generator):
     ID = 134
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          VerbNot = ['Impregnated','Bred','Hunted']
          sVerb = self.VerbsBy.GetWord(NotList = VerbNot)

          sTweet = sVerb + " by "
          if CoinFlip():
          #gay male
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
               sTweet += "his " + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
          else:
          #lesbian female
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
               sTweet += "her " + Orientation.GetWord() + " " + Species.GetWord() + " " + Relations.GetWord()
          return sTweet     
          
# MILKED by my biker step-son
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
     
#Ass Eating 101:
# My date with the principal
class Generator136(Generator):
     ID = 136
     Priority = 1
     
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
class Generator137(Generator):
     ID = 137
     Priority = 1
     
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
                                    
          sTweet = sVerbPhrase + "\n" + Places.GetWord() + " by\n" + Man.Desc + " " + ManNouns.GetWord()

          return sTweet     
          
#I Was Scissored by a Witch, and I Liked It!
class Generator138(Generator):
     ID = 138
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Verbs = WordList(["Ravished","Fingered","Milked","Scissored","Fisted",
                                "Kissed","Eaten Out","Sixty-Nined","Finger-Banged",
                                "French Kissed","Taken with a Broomstick",
                                "Penetrated with a Broomstick","Bitten",
                                "Defiled with a Broomstick",
                                "Ravished with a Broomstick"])
               
          if CoinFlip():
               NotFemList = ['anal','tease','virgin','fertile','small-town','tender','revealing','mature woman',
                                   'witch']
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddAnArticle = True, bAddEndNoun = False, NotList = NotFemList,
                                        bAllowSexuality = False, bAllowMaritalStatus = False, bAllowProf = False, bAllowTitle = False,
                                        bAllowGenMod = False)
                                        
               sTweet = "I Was " + Verbs.GetWord() + " by " + Girl.Desc + " Witch, And I Liked It!"
                                        
          else:
               NotFemList = ['anal','devlish','tease','virgin','fertile','small-town','submissive',
                                'tender','masseuse','mature','little']
               Girl = char.FemaleChar(Type = GirlType.Bad, bAddEndNoun = True, NotList = NotFemList,
                                        bAllowSexuality = False, bAllowMaritalStatus = False, bAllowAttitude = False, 
                                        bAllowGenMod = False, bAllowSpecies = False, bAllowTitle = False)
               
               sTweet = "I Was " + Verbs.GetWord() + " by an Undead " + Girl.Desc + ", And I Liked It!"

          return sTweet     
     
# My Innocent Sheltered Step-Mom 
# Wore a Butt Plug
# To Church     
class Generator139(Generator):
     ID = 139
     Priority = 1
     
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
class Generator140(Generator):
     ID = 140
     Priority = 1
     
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
          
class Generator141(Generator):
     ID = 141
     Priority = 1
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
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
class Generator142(Generator):
     ID = 142
     Priority = 1
     
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

# Testing innuendo name generators          
class Generator999(Generator):
     ID = 999
     Priority = 1
     Type = GeneratorType.Test
     
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
class Generator1000(Generator):
     ID = 1000
     Priority = 1
     Type = GeneratorType.Test
     
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
class Generator1001(Generator):
     ID = 1001
     Priority = 1
     Type = GeneratorType.Test
     
     def GenerateTweet(self):
          super().GenerateTweet()
          sTweet = ""
          
          Girl = char.FemaleChar(TempType = TempType.Flowery, 
                                        bAddTheArticle = False, 
                                        bAllowTrope = True, 
                                        SelectTemplateID = 128)
          Guy = char.MaleChar(TempType = TempType.Flowery, 
                                   bAddAnArticle = True, 
                                   bAllowGang = False,
                                   bAllowTrope = True,
                                   SelectTemplateID = 14)
          #Gang = char.MaleChar(TempType = TempType.Flowery,
          #                          bAddAnArticle = True,
          #                          bAllowGang = True)
          

          sTweet += AddArticles(Girl.Desc, bMakeUpper = True) + " Gets Sexed the Hell Up!\n"
          #sTweet += AddArticles(Guy.Desc, bMakeUpper = True) + " Took My Wife Hard From Behind!\n"
          sTweet += Guy.Desc + " Took My Wife Hard From Behind!\n"
          #sTweet += Gang.Desc + " Took Turns With My Wife!"

          return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
# class Generator100(Generator):
     # ID = 100
     # Priority = 1
     
     # def GenerateTweet(self):
          # super().GenerateTweet()
          # sTweet = ""

          # return sTweet     
          
class GeneratorSelector():
     GeneratorList = []
     
     def __init__(self):
          for subclass in Generator.__subclasses__():
               item = subclass()
               for x in range(0, item.Priority):
                    self.GeneratorList.append([item.ID, item])
               
     def RandomGenerator(self, bAllowPromo = True, Type = None):
          Generator = None
          AllowedTypes = []
          
          if not Type is None:
               AllowedTypes = [Type] 
          else:
               AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
          if bAllowPromo:
               AllowedTypes.append(GeneratorType.Promo)
               
          #print("RandomGenerator() Allowed types: " + str(AllowedTypes))
          if len(self.GeneratorList) > 0:

               Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
               while not Generator.Type in AllowedTypes:
                    Generator = self.GeneratorList[randint(0, len(self.GeneratorList) - 1)][1]
                    
          return Generator 
          
     def GetGeneratorsSequential(self, bAllowPromo = True, Type = None):
          GeneratorList = []
          AllowedTypes = []
          
          if not Type is None:
               AllowedTypes = [Type] 
          else:
               AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
          if bAllowPromo:
               AllowedTypes.append(GeneratorType.Promo)

          for subclass in Generator.__subclasses__():
               gen = subclass()

               if gen.Type in AllowedTypes:
                    GeneratorList.append(gen)
               
          return GeneratorList  
          
     def GetGenerator(self, iGen):
          Generator = None 
          
          if len(self.GeneratorList) > 0:
               for gen in self.GeneratorList :
                    if gen[1].ID == iGen:
                         Generator = gen[1]
                         break
                         
          return Generator
          