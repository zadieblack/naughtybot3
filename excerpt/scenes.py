#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Scenes module

import excerpt.bodyparts
import excerpt.names
import excerpt.people
import excerpt.verbs
import excerpt.misc

from random import * 
from util import *
from excerpt.util import *

class Scene():
     Tags = {}
     Location = None

     VerbPast = ""
     VerbPresent = ""
     VerbGerund = ""
     HisName = ""
     HerName = ""
     HisNamePos = ""
     HerNamePos = ""
     HisPronoun = ""
     HerPronoun = ""
     SceneShortDesc3P = ""
     SceneShortDesc1PHim = ""
     SceneShortDesc1PHer = ""
     
     def __init__(self, sHisName, sHerName, Location = None):
          #print("Scene init() sHisName = " + sHisName + ", sHerName = " + sHerName)
               
          if sHisName == "":
               self.HisName = "he"
               self.HisNamePos = "his"
          else:
               self.HisName = sHisName
               self.HisNamePos = self.HisName + "'s"
               
          if sHerName == "":
               self.HerName = "she"
               self.HerNamePos = "her"
          else: 
               self.HerName = sHerName
               self.HerNamePos = self.HerName + "'s"
               
          if Location == None:
               pass
          else:
               self.Location = Location
               
     def Scene(self, Location = None):
          sScene = ""
          
          return sScene
     
class SceneAnal(Scene):
     Tags = {TAG_DONE_TO_HER, TAG_PEN, TAG_BELOW_BELT}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "butt-fucked"
          self.VerbPresent = "butt-fuck"
          self.VerbGerund = "butt-fucking"
          
          self.SceneShortDesc3P = "he " + WordList(["ass-fucked", "had anal sex with", "anally penetrated"]).GetWord() + " her"
          self.SceneShortDesc1PHim = "I " + WordList(["ass-fucked", "had anal sex with", "anally penetrated"]).GetWord() + " you"
          self.SceneShortDesc1PHer = "you " + WordList(["ass-fucked", "had anal sex with", "anally penetrated"]).GetWord() + " me"
          
     def Scene(self, Location = None):
          sScene = ""
          
          Penis = excerpt.bodyparts.Penis()
          Ass = excerpt.bodyparts.AssFemale()
          Anus = excerpt.bodyparts.AnusFemale()
          Clit = excerpt.bodyparts.Clitoris()
          VerbThrust = excerpt.verbs.VerbThrust()
          
          AdvSpread = WordList(["lovingly", "carefully", "tenderly", "forcefully", "firmly", "gently", "expertly", "roughly"])
          
          Actions = []
          
          if CoinFlip():
               Actions.append(self.HisName.capitalize() + " " + AdvSpread.GetWord() + " spread " + self.HerNamePos + " " + Ass.RandomDescription() + " apart, ")
          else: 
               Actions.append(self.HerName.capitalize() + " winked at him as she " + AdvSpread.GetWord() + " spread her " + Ass.RandomDescription() + " apart, ")
          
          Actions.append("exposing her " + Anus.RandomDescription() + ". ")
          
          if CoinFlip():
               if CoinFlip():
                    Actions.append(self.HisName.capitalize() + " spit on his fingers")
               else:
                    Actions.append(self.HisName.capitalize() + " applied some lube to his fingers")
                    
               Actions.append(", and then gently inserted " + str(randint(1,4)) + " of them into " + self.HerNamePos + " " + Anus.ShortDescription() + ". ")
               
          if CoinFlip():
               Actions.append("When she was ready, he eased the " + Penis.Head.RandomDescription() + " of his " + Penis.ShortDescription() + " into her tight " + Anus.ShortDescription() + ". ")
               
          Actions.append("Before long ")
          
          if CoinFlip():
               Actions.append("he was " + VerbThrust.Gerund() + " her " + Anus.ShortDescription() + " " + AdvSpread.GetWord())
          else:
               Actions.append("he was deep in her " + Ass.RandomDescription() + ", fucking her " + AdvSpread.GetWord())
               
          if CoinFlip():
               Actions.append(", stretching her " + Anus.ShortDescription() + " wide")
               
          if CoinFlip():
               Actions.append(" as he diddled her " + Clit.ShortDescription() + " with his hand")
               
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          sScene += "."
               
          return sScene

class SceneBlowjob(Scene):
     Tags = {TAG_NON_PEN, TAG_DONE_TO_HIM, TAG_BELOW_BELT, TAG_ORAL, TAG_FOREPLAY}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "blew"
          self.VerbPresent = "blow"
          self.VerbGerund = "blowing"
          
          self.SceneShortDesc3P = "she " + WordList(["gave him a blow-job", "sucked his cock"]).GetWord() 
          self.SceneShortDesc1PHim = "you " + WordList(["gave me a blow-job", "sucked my cock"]).GetWord() 
          self.SceneShortDesc1PHer = "I " + WordList(["gave you a blow-job", "sucked your cock"]).GetWord() 
     
     def Scene(self, Location = None):
          sScene = ""
          
          Actions = []
          
          Penis = excerpt.bodyparts.Penis()
          Breasts = excerpt.bodyparts.Breasts()
          
          sScene = self.HerName.capitalize() + " proceeded to " + excerpt.verbs.VerbOralMale().Present() + " him. "
          
          if CoinFlip():
               Actions.append("She tenderly kissed his " + Penis.Head.RandomDescription() + ". ")
               
          if CoinFlip():
               Actions.append("She rubbed his " + Penis.MediumDescription() + " between her " + Breasts.RandomDescription() + ". ")
               
          if CoinFlip():
               Actions.append("She gave the underside of his " + Penis.ShortDescription() + " a long, loving stroke with her tongue. ")
               
          if CoinFlip():
               Actions.append("She lovingly cupped his " + Penis.Testicles.RandomDescription(bAllowShortDesc = True)+ ". ")
               
          if CoinFlip():
               Actions.append("She was licking and kissing every inch of " + self.HisNamePos + " " + Penis.RandomDescription(bAllowShortDesc = True) + ". ")
               
          Actions.append("She took his " + Penis.ShortDescription() + " into her mouth and began to suck it enthusiastically")
          
          if CoinFlip():
               Actions.append(", taking it so deep into her throat that " + self.HisNamePos + " " + Penis.Testicles.ShortDescription() + " were slapping against her chin. ")
          else:
               Actions.append(". ")
               
          if CoinFlip():
               Actions.append("She caressed and sucked on his " + Penis.Testicles.ShortDescription() + ". ")
               
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          sScene += "Before long, thick strands of her saliva were hanging from the length of his " + Penis.ShortDescription() + "."
          
          return sScene 
          
class SceneBreastPlay(Scene):     
     Tags = {TAG_ABOVE_BELT, TAG_DONE_TO_HER, TAG_FOREPLAY, TAG_NON_PEN}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "groped"
          self.VerbPresent = "grope"
          self.VerbGerund = "groping"
          
          sTits = excerpt.bodyparts.Breasts().ShortDescription()
          
          self.SceneShortDesc3P = "he " + WordList(["played with her " + sTits, "sucked on her " + sTits]).GetWord() 
          self.SceneShortDesc1PHim = "I " + WordList(["played with your " + sTits, "sucked on your " + sTits]).GetWord()  
          self.SceneShortDesc1PHer = "you " + WordList(["played with my " + sTits, "sucked on my " + sTits]).GetWord()  

     def Scene(self):
          sScene = ""
          
          Actions = []
          
          FemBodyParts = excerpt.bodyparts.BodyFemale()
          Breasts = FemBodyParts.Breasts
          Nipples = Breasts.Nipples
          
          if CoinFlip():
               Actions.append(self.HisName.capitalize() + " grabbed " + self.HerNamePos + " " + Breasts.RandomDescription() + " and squeezed them.")
          else:
               Actions.append(self.HisName.capitalize() + " gently carressed " + self.HerNamePos + " " + Breasts.RandomDescription() + ".")
               
          Actions.append("He covered the " + excerpt.bodyparts.Skin().RandomDescription() + " of her breasts with " + WordList(["sweet", "sloppy", "gentle", "tender", "loving", "hungry", "lustful", "tantalizing"]).GetWord() + " kisses.")
          Actions.append("He lifted her one of her " + Breasts.MediumDescription() + " and kissed the underside of it.")
          Actions.append("He trailed his finger around one of her " + Breasts.ShortDescription() + ", spiraling up it until he brushed her " + WordList(["tingling", "sensitive", "hardening", "yearning", "stiffening", "expectant", "perky"]).GetWord() + " nipple.")
          Actions.append("Taking her " + Nipples.RandomDescription() + " between his fingers, he began to " + WordList(["stimulate", "tweak", "tease", "roll", "rub" "play with"]).GetWord() + " them " + WordList(["sensually", "erotically", "sensuously", "tenderly", "expertly"]).GetWord() + ".")
          Actions.append("He kissed one of her " + Nipples.RandomDescription() + " and than began to " + WordList(["suck on it", "suckle it", "swirl his tongue around it", "nibble it", "kiss and nip it"]).GetWord() + ".")
          
          iRand = randint(1,3)
          for x in sorted(sample(range(0, len(Actions)), iRand)):
               sScene += Actions[x] + " "
          
          sScene = sScene.rstrip()
               
          return sScene 
          
class SceneCowgirl(Scene):     
     #She straddled his hips. . He had an intimate view of her succulent peach and snug asshole as she lowered herself onto him. She began to grind against his mouth as he licked and sucked her hole, coating his chin in her juices.
     Tags = {TAG_BELOW_BELT, TAG_DONE_TO_HIM, TAG_PEN, TAG_POSITION}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "rode"
          self.VerbPresent = "ride"
          self.VerbGerund = "riding"
          
          sDick = excerpt.bodyparts.Penis().ShortDescription()
          
          self.SceneShortDesc3P = "she straddled him and rode his " + sDick
          self.SceneShortDesc1PHim = "you straddled me and rode my " + sDick
          self.SceneShortDesc1PHer = "I straddled you and rode your " + sDick

     def Scene(self):
          sScene = ""
          
          Vagina = excerpt.bodyparts.Vagina()
          Breasts = excerpt.bodyparts.Breasts()
          Hips = excerpt.bodyparts.Hips()
          Penis = excerpt.bodyparts.Penis()
          VerbThrust = excerpt.verbs.VerbThrust()
          
          Actions = []
          
          Actions.append(self.HerName.capitalize() + " straddled " + self.HisNamePos + " hips. ")
          
          if CoinFlip():
               Actions.append("Grabbing his erect " + Penis.GetNoun(NotList = ["erection"]) + ", she guided it to her entrance. ")

          Actions.append("She lowered her hips, impaling herself on his " + Penis.RandomDescription() )
          
          if CoinFlip():
               Actions.append(" with a " + WordList(["whimper", "sigh", "moan", "wail", "gasp", "cry"]).GetWord() + " of pleasure")
               
          if CoinFlip():
               Actions.append(". She began thrusting herself " + WordList(["forcefully", "passionately", "feverishly", "urgently", "lovingly", "tenderly", "rhythmically"]).GetWord() + " up and down as she rode his " + Penis.MediumDescription())
               if CoinFlip():
                    Actions.append(", her " + Breasts.ShortDescription() + " bouncing vigorously")
          else:
               Actions.append(". She began rotating her " + Hips.MediumDescription() + " sensually, grinding on his " + Penis.MediumDescription() + ", feeling him move inside of her")
               if CoinFlip():
                    Actions.append(". As she did so he grabbed her " + Breasts.MediumDescription() + " and squeezed them")
                    
          if CoinFlip():
               Actions.append(". " + self.HisName.capitalize() + " watched this " + excerpt.misc.WomanAdjs().GetWord() + " creature take advantage of him in amazement")
               
          Actions.append(".")
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene 

class SceneCreamPie(Scene):
     Tags = {TAG_PEN, TAG_DONE_TO_HER, TAG_CLIMAX, TAG_BELOW_BELT}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          sVagina = excerpt.bodyparts.Vagina().ShortDescription()
          sSemen = excerpt.bodyparts.Semen().ShortDescription()
          
          self.VerbPast = "cream-pied"
          self.VerbPresent = "cream-pie"
          self.VerbGerund = "cream-pieing"
          
          self.SceneShortDesc3P = "he " + WordList(["came inside her " + sVagina, "filled her " + sVagina + " with his " + sSemen]).GetWord() 
          self.SceneShortDesc1PHim = "I " + WordList(["came inside your " + sVagina, "filled your " + sVagina + " with my " + sSemen]).GetWord() 
          self.SceneShortDesc1PHer = "you " + WordList(["came inside my " + sVagina, "filled my " + sVagina + " with your " + sSemen]).GetWord()  
     
     def Scene(self, Location = None, bIsVagina = True):
          Penis = excerpt.bodyparts.Penis()
          Semen = excerpt.bodyparts.Semen()
          Vagina = excerpt.bodyparts.Vagina()
          Anus = excerpt.bodyparts.AnusFemale()
          Thighs = excerpt.bodyparts.Thighs()
          DripVerbs = excerpt.verbs.VerbDrip()
          SemenGobs = excerpt.misc.Gobs()
          VEjac = excerpt.verbs.VerbEjaculate()
          sScene = ""
          
          if bIsVagina:
               sScene = "He was soon " + VEjac.Gerund() + " deep within her " + Vagina.RandomDescription() + " as an intense orgasm wracked her body. "
          else:
               sScene = "He was soon " + VEjac.Gerund() + " deep within her " + Anus.RandomDescription() + " as an intense orgasm wracked her body. "
          
          sScene += Semen.GetNewAdj().capitalize() + " " + SemenGobs.GetWord() +" of " + Semen.GetNoun() + " " + DripVerbs.Past() + " from " + self.HerNamePos 
          
          if bIsVagina:
               iRandPussyDesc = randint(1, 3)
               
               if iRandPussyDesc == 1:
                    sScene += " " + Vagina.RandomDescription(bAllowShortDesc = True)
               elif iRandPussyDesc == 2:
                    sScene += " " + Vagina.InnerLabia.RandomDescription(bAllowShortDesc = True)
               else:
                    sScene += " " + Vagina.InnerVag.RandomDescription(bAllowShortDesc = True)
          else:
               sScene += " " + Anus.RandomDescription(bAllowShortDesc = True)
          
          iRandAfter = randint (1,10)
          
          if iRandAfter % 2 == 0:
               sScene += " and down her " + Thighs.RandomDescription(bAllowShortDesc = True)
          if iRandAfter > 4:
               if not self.Location == None:
                    sScene += " and onto the " + self.Location.Ground 
          if iRandAfter % 3 == 0: 
               sScene += ". She scooped some up with her fingers and tasted it"
          if iRandAfter > 6:
               sScene += ". " + self.HerName.capitalize() + " got down on her knees and began to lick the " + Semen.RandomDescription() + " from his " + Penis.RandomDescription()
          
          #print("sScene[len(sScene) - 1] = " + sScene[len(sScene) - 1])
          if not sScene[len(sScene) - 1] == ".":
               sScene += "."
               
          return sScene
          
class SceneCunnilingus(Scene):     
     Tags = {TAG_NON_PEN, TAG_DONE_TO_HER, TAG_BELOW_BELT, TAG_ORAL, TAG_FOREPLAY}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "went down on"
          self.VerbPresent = "go down on"
          self.VerbGerund = "going down on"
          
          sVagina = excerpt.bodyparts.Vagina().ShortDescription()
          
          self.SceneShortDesc3P = "he " + WordList(["went down on her", "ate out her " + sVagina, "licked her " + sVagina]).GetWord() 
          self.SceneShortDesc1PHim = "I " + WordList(["went down on you", "ate out your " + sVagina, "licked your " + sVagina]).GetWord() 
          self.SceneShortDesc1PHer = "you " + WordList(["went down on me", "ate out my " + sVagina, "licked my " + sVagina]).GetWord() 
     
     def Scene(self, Location = None):
          sScene = ""
          
          Vagina = excerpt.bodyparts.Vagina()
          InnerLabia = excerpt.bodyparts.VaginaInnerLabia()
          OuterLabia = excerpt.bodyparts.VaginaOuterLabia()
          InnerVag = excerpt.bodyparts.VaginaInner()
          Clit = excerpt.bodyparts.Clitoris()
          Anus = excerpt.bodyparts.AnusFemale()
          Thighs = excerpt.bodyparts.Thighs()
          
          Actions = []
          
          Actions.append(self.HisName.capitalize() + " spread apart her " + Thighs.RandomDescription(bAllowShortDesc = True) + " and ")
          
          if CoinFlip():
               Actions.append("licked her from her " + Anus.ShortDescription() + " to her " + Clit.ShortDescription() + ".")
          else:
               Actions.append("kissed his way up them until his lips brushed against her " + OuterLabia.MediumDescription() + ".")
               
          if CoinFlip():
               Actions.append(" He covered her " + OuterLabia.MediumDescription() + " with slobbery kisses, ")
          else:
               Actions.append(" With skillful strokes of his tongue he bathed her " + Vagina.MediumDescription() + " with his saliva, ")
               
          if CoinFlip():
               Actions.append("then he gently teased her " + InnerLabia.RandomDescription() + ", ")
               
          Actions.append("and nibbled on her " + Clit.RandomDescription(bAllowShortDesc = True) + ". ")
          Actions.append("Spreading open her " + InnerLabia.MediumDescription() + ", ")
          
          if CoinFlip():
               Actions.append("he began to lick his way around the delicate pink inside of her " + Vagina.ShortDescription() + ", ")
               if CoinFlip():
                    Actions.append("before tongue-fucking her " + InnerVag.ShortDescription() + " vigorously.")
               else:
                    Actions.append("before inserting two fingers deep inside her " + InnerVag.ShortDescription() + ".")
          else:
               Actions.append("he buried his face in her " + Vagina.ShortDescription() + ", eating her " + Vagina.RandomDescription(bAllowShortDesc = True) + " until his chin was dripping with her juices.")
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene
          
class SceneDoggy(Scene):     
     Tags = {TAG_PEN, TAG_DONE_TO_HER, TAG_POSITION, TAG_BELOW_BELT}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "did it doggy-style"
          self.VerbPresent = "do it doggy-style"
          self.VerbGerund = "doing it doggy-style"
          
          self.SceneShortDesc3P = "he " + WordList(["took her hard from behind", "fucked her from behind", "fucked her doggy-style"]).GetWord() 
          self.SceneShortDesc1PHim = "I " + WordList(["took you hard from behind", "fucked you from behind", "fucked you doggy-style"]).GetWord() 
          self.SceneShortDesc1PHer = "you " + WordList(["took me hard from behind", "fucked me from behind", "fucked me doggy-style"]).GetWord()  
     
     def Scene(self, Location = None):
          sScene = ""
          
          Vagina = excerpt.bodyparts.Vagina()
          Ass = excerpt.bodyparts.AssFemale()
          Penis = excerpt.bodyparts.Penis()
          VerbThrust = excerpt.verbs.VerbThrust()
          
          Actions = []
          
          if CoinFlip():
               Actions.append(self.HerName.capitalize() + " got on her knees, showing him her lovely, " + Ass.GetNewAdj(NotList = ["lovely"]) + " " + Ass.ShortDescription() + ", her " + Vagina.ShortDescription() + ", and her " + Ass.Anus.RandomDescription() + ". ")
          else:
               Actions.append(self.HisName.capitalize() + " bent her over, shoving her head down so that her " + Ass.MediumDescription() + " was up in the air, ready for his " + Penis.MediumDescription() + ". ")
               
          Actions.append("He grabbed her by the hips")
               
          if CoinFlip():
               Actions.append(", and began to rub his cock against her ")
               if CoinFlip():
                    Actions.append("crack")
               else:
                    Actions.append(Vagina.OuterLabia.ShortDescription() + "")
                    
          Actions.append(". Positioning his " + Penis.Head.MediumDescription() + " against her entrance, ")
          
          if CoinFlip():
               Actions.append("he suddenly " + VerbThrust.Past() + " into her.")
          else:
               Actions.append("he gently eased himself inside her.")
               
          Actions.append(" In moments he was " + VerbThrust.Gerund() + " in and out of her " + Vagina.InnerVag.MediumDescription() + " as she " + excerpt.verbs.VerbMoan().Past() + " with pleasure.")
          
               
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene 
          
class SceneFacesitting(Scene):     
     Tags = {TAG_BELOW_BELT, TAG_DONE_TO_HIM, TAG_NON_PEN, TAG_ORAL}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "face-sat on"
          self.VerbPresent = "face-sit on"
          self.VerbGerund = "face-sitting on"
          
          self.SceneShortDesc3P = "she sat on his face"
          self.SceneShortDesc1PHim = "you sat on my face"
          self.SceneShortDesc1PHer = "I sat on his face"  

     def Scene(self):
          sScene = ""
          
          Vagina = excerpt.bodyparts.Vagina()
          Ass = excerpt.bodyparts.AssFemale()
          
          Actions = []
          
          Actions.append(self.HerName.capitalize() + " straddled " + self.HisNamePos + " face. He had an intimate view of her " + Vagina.OuterLabia.RandomDescription() + " and " + Ass.Anus.RandomDescription() + " as she lowered herself onto him. She began to grind against his mouth as he ")
          
          if CoinFlip():
               Actions.append("rimmed and tongue-fucked her " + Ass.Anus.RandomDescription())
          else:
               Actions.append("licked her " + Vagina.OuterLabia.RandomDescription())
               if CoinFlip():
                    Actions.append(" and sucked on her " + Vagina.InnerLabia.RandomDescription())
               if CoinFlip():
                    Actions.append(", coating his chin in her juices")
          
          Actions.append(".")
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene 
          
class SceneFacial(Scene):
     Tags = {TAG_ABOVE_BELT, TAG_DONE_TO_HER, TAG_CLIMAX, TAG_NON_PEN}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "facialed"
          self.VerbPresent = "facial"
          self.VerbGerund = "facialing"
          
          VerbEjac = excerpt.verbs.VerbEjaculate()
          
          self.SceneShortDesc3P = "he " + VerbEjac.Past() + " all over her face"
          self.SceneShortDesc1PHim = "I " + VerbEjac.Past() + " on your face"
          self.SceneShortDesc1PHer = "you " + VerbEjac.Past() + "  on my face"
     
     def Scene(self, Location = None):
          sScene =""
          
          Actions = []
          
          Semen = excerpt.bodyparts.Semen()
          FemBodyParts = excerpt.bodyparts.BodyFemale()
          Eyes = FemBodyParts.Eyes 
          Lips = FemBodyParts.Lips
          Hair = FemBodyParts.Hair
          Breasts = FemBodyParts.Breasts
          Skin = FemBodyParts.Skin 
          Face = FemBodyParts.Face
          Penis = excerpt.bodyparts.Penis()
          VerbEjac = excerpt.verbs.VerbEjaculate()
          VerbDrip = excerpt.verbs.VerbDrip()
          Gobs = excerpt.misc.Gobs()
          
          VerbSpew = WordList(["splattered", "spurted", "squirted", "spewed", "sprayed", "splashed", "spattered"])
          
          if CoinFlip():
               sScene = "'" + excerpt.misc.Exclamations().GetWord(bHappy = True).capitalize() + "!' " + self.HisName + " " + excerpt.verbs.VerbMoan().Past() + ", 'I'm coming!' "
          else:
               sScene = self.HisName.capitalize() + " grunted. "
               
          if CoinFlip():
               sScene += "The " + Penis.Head.RandomDescription(bAllowShortDesc = True) + " of his " + Penis.ShortDescription() + " " + excerpt.verbs.VerbEjaculate().Past() + ". "
          else:
               sScene += self.HisNamePos.capitalize() + " " + Penis.RandomDescription(bAllowLongDesc = False) + " " + WordList(["jerked", "pulsed", "pulsated", "quivered", "bucked", "jumped"]).GetWord() + " and then he began " + VerbEjac.Gerund() + " all over " + self.HerNamePos + " " + Face.RandomDescription(bAllowLongDesc = False) + ". "
          
          Actions.append("She squeezed her eyes shut as " + Gobs.GetWord() + " of " + Semen.ShortDescription() + " " + VerbSpew.GetWord() + " across them" + WordList([", smearing her eyeliner", ""]).GetWord() + ".")
          Actions.append(Gobs.GetWord().capitalize() + " of it got stuck in her " + Hair.RandomDescription(bAllowLongDesc = False) + ".")
          Actions.append(Semen.RandomDescription().capitalize() + " dribbled from her " + Lips.RandomDescription(bAllowLongDesc = False) + ".")
          Actions.append(Gobs.GetWord().capitalize() + " of " + Semen.ShortDescription() + " " + VerbDrip.Past() + " from her chin.")
          Actions.append("A string of sticky pearls was " + VerbSpew.GetWord() + " across her slender neck.")
          if CoinFlip():
               Actions.append("And " + Gobs.GetWord() + " of " + Semen.ShortDescription() + " " + WordList(["glazed", "adorned", "spackled", "dripped down", "pooled on"]).GetWord() + " " + self.HerNamePos + " " + Breasts.RandomDescription())
          else:
               Actions.append("And a single " + WordList(["globule", "pearl", "bead", "rope"]).GetWord() + " of " + Semen.RandomDescription() + " clung to " + self.HerNamePos + " " + Breasts.Nipples.GetNewAdj() + " nipple.")
          
          iRand = randint(1,5)
          for x in sorted(sample(range(0, len(Actions)), iRand)):
               sScene += Actions[x] + " "
          
          sScene = sScene.rstrip()
          if sScene[len(sScene) - 1] != ".":
               sScene += "."
               
          return sScene
          
class SceneMakeOut(Scene):     
     Tags = {TAG_CLOTHED, TAG_NON_PEN, TAG_FOREPLAY, TAG_ABOVE_BELT, TAG_NON_PEN}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "french-kissed"
          self.VerbPresent = "french-kiss"
          self.VerbGerund = "french-kissing"
          
          self.SceneShortDesc3P = "they " + WordList(["kissed", "french kissed", "made out"]).GetWord()
          self.SceneShortDesc1PHim = "I " + WordList(["kissed", "french kissed", "made out with"]).GetWord() + " you"
          self.SceneShortDesc1PHer = "I " + WordList(["kissed", "french kissed", "made out with"]).GetWord() + " you"

     def Scene(self):
          sScene = ""
          
          FemBodyParts = excerpt.bodyparts.BodyFemale()
          Lips = FemBodyParts.Lips
          Face = FemBodyParts.Face 
          Mouth = FemBodyParts.Mouth
          
          Actions = []
          
          if CoinFlip():
               # he initiates
               Actions.append(self.HisName.capitalize() + " leaned in and " + WordList(["kissed", "pecked", "brushed"]).GetWord() + " " + self.HerName + " on her " + Lips.RandomDescription() + ". She returned his kiss with " + WordList(["a fiery", "an impassioned", "a red-hot", "an ardent", "an intense"]).GetWord() + " one of her own. ")
               Actions.append("Passions ingited. Before she knew it they were locked in a " + WordList(["lustful", "sensual", "wanton", "wild"]).GetWord() + " embrace. His hands were " + WordList(["roaming all over her body", "squeezing her " + FemBodyParts.Ass.ShortDescription(), "rubbing her crotch", "fondling her breasts"]).GetWord() + ", and he was exploring her " + Mouth.RandomDescription(bAllowShortDesc = True) + " with his talented tongue.")
          else:
               # she initiates
               Actions.append(self.HerName.capitalize() + " reached up and caressed " + self.HisNamePos + " " + excerpt.bodyparts.BodyMale().Jaw.MediumDescription() + ", then she suddenly kissed him with her " + Lips.MediumDescription() + ". He returned her kiss with " + WordList(["a fiery", "an impassioned", "a red-hot", "an ardent", "an intense"]).GetWord() + " one of his own. ")
               Actions.append("Passions ingited. Before he knew it they were locked in a " + WordList(["lustful", "sensual", "wanton", "wild"]).GetWord() + " embrace. Her hands were " + WordList(["rubbing the bulge in his crotch", "squeezing his " + FemBodyParts.Ass.ShortDescription(), "working their way down the front of his trousers", "up his shirt"]).GetWord() + ", and she was exploring his mouth with her talented tongue.")
          
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene 
          
class SceneMissionary(Scene):     
     Tags = {TAG_DONE_TO_HER, TAG_BELOW_BELT, TAG_POSITION, TAG_PEN}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "did it in the missionary position"
          self.VerbPresent = "do it in the missionary position"
          self.VerbGerund = "doing it in the missionary position"
          
          self.SceneShortDesc3P = "she spread her legs for him and he fucked her on her back"
          self.SceneShortDesc1PHim = "you spread your legs for me and I fucked you on your back"
          self.SceneShortDesc1PHer = "I spread my legs for you and you fucked me on my back"

     def Scene(self, Location = None):
          sScene = ""
          
          Vagina = excerpt.bodyparts.Vagina()
          Legs = excerpt.bodyparts.Legs()
          Breasts = excerpt.bodyparts.Breasts()
          Penis = excerpt.bodyparts.Penis()
          VerbThrust = excerpt.verbs.VerbThrust()
          
          Actions = []
          
          Actions.append(self.HisName.capitalize() + " spread her " + Legs.MediumDescription() + " wide and pushed them up. ")
          Actions.append(self.HerNamePos.capitalize() + " " + Vagina.RandomDescription(bAllowShortDesc = True) + " was wide open, exposing her " + Vagina.InnerVag.RandomDescription(bAllowShortDesc = True) + ". ")
          if CoinFlip():
               Actions.append("She wrapped her legs around him, pulling him down to her. ")
               if CoinFlip():
                    Actions.append("They kissed as ")
               else:
                    Actions.append("He played with her " + Breasts.RandomDescription(bAllowLongDesc = False) + " as ")
               Actions.append("he entered her " + Vagina.InnerVag.RandomDescription() + ". ")
          else:
               Actions.append("He inserted his " + Penis.RandomDescription() + " into her " + Vagina.InnerVag.RandomDescription() + ". ")
               
          if CoinFlip():
               Actions.append("She was " + WordList(["already wet", "sopping wet", "practically gushing", "moist and inviting", "moist and slick"]).GetWord() + " and eager to receive him. ")
               
          Actions.append(self.HisName.capitalize() + " began " + VerbThrust.Gerund() + " in and out of " + self.HerNamePos + " " + Vagina.RandomDescription(bAllowLongDesc = False) + " " + WordList(["forcefully", "passionately", "feverishly", "urgently", "lovingly", "tenderly", "rhythmically"]).GetWord() + " ")
          
          if CoinFlip():
               Actions.append("driving balls-deep with every powerful thrust")
          else:
               Actions.append("as she coated his " + Penis.ShortDescription() + " with her milky juices")
               
          Actions.append(".")
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
          
          return sScene 
          
class SceneRimjobHerScene(Scene):
     Tags = {TAG_NON_PEN, TAG_DONE_TO_HER, TAG_BELOW_BELT, TAG_ORAL, TAG_FOREPLAY}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "rimmed" 
          self.VerbPresent = "rim"
          self.VerbGerund = "rimming"
          
          sAnus = excerpt.bodyparts.AnusFemale().ShortDescription()
          
          self.SceneShortDesc3P = "he " + WordList(["gave her a rim-job", "rimmed her " + sAnus, "licked her " + sAnus]).GetWord() 
          self.SceneShortDesc1PHim = "I " + WordList(["gave you a rim-job", "rimmed your " + sAnus, "licked your " + sAnus]).GetWord() 
          self.SceneShortDesc1PHer = "You " + WordList(["gave me a rim-job", "rimmed my " + sAnus, "licked my " + sAnus]).GetWord() 
     
     def Scene(self, Location = None):
          sScene = ""
          
          Actions = []
          
          Ass = excerpt.bodyparts.AssFemale()
          Anus = excerpt.bodyparts.AnusFemale()
          Penis = excerpt.bodyparts.Penis()
          Breasts = excerpt.bodyparts.Breasts()
          Vagina = excerpt.bodyparts.Vagina()
          
          sScene = self.HisName.capitalize() + " turned her around and bent her over. "
          
          if CoinFlip():
               Actions.append("He tenderly kissed her " + Ass.RandomDescription(bAllowShortDesc = True))
          else:
               Actions.append("He began to massage her " + Ass.RandomDescription(bAllowShortDesc = True))
               
          Actions.append(" and then he spread her " + Ass.ShortDescription() + " apart, revealing her " + Anus.RandomDescription(bAllowShortDesc = True) + ". ")
               
          if CoinFlip():
               Actions.append("He wet his finger with his tongue and then began to gently slide it around her " + Anus.GetNewAdj() + " rim. ")
          else:
               Actions.append("He nestled his face between her cheeks and gently kissed her rim. ")
               
          Actions.append("Then he began to lick it with his " + WordList(["long", "agile", "talented", "expert"]).GetWord() + " tongue. ")
          
          if CoinFlip():
               Actions.append("He heard her " + WordList(["moaning", "groaning", "sighing", "cooing"]).GetWord() + " with pleasure. ")
               
          if CoinFlip():
               Actions.append("He reached between her spread legs and ran his finger along her " + Vagina.OuterLabia.RandomDescription(bAllowShortDesc = True) + ". It was dripping wet. Fingering it, he ")
          else:
               Actions.append("He ")
          
          Actions.append("continued to rim her " + Anus.ShortDescription() + " eagerly")
          if CoinFlip():
               Actions.append(", enjoying the taste of her on his tongue.")
          else:
               Actions.append(", inserting the tip of her finger into her " + WordList(["snug", "tight", "constricting", "taut"]).GetWord() + " " + Anus.ShortDescription() + ".")
          
               
          for x in range(0, len(Actions)):
               sScene += Actions[x]
          
          return sScene 

class SceneRimjobHim(Scene):
     Tags = {TAG_NON_PEN, TAG_DONE_TO_HIM, TAG_BELOW_BELT, TAG_ORAL, TAG_FOREPLAY}
     
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "rimmed" 
          self.VerbPresent = "rim"
          self.VerbGerund = "rimming"
          
          sAnus = excerpt.bodyparts.AnusFemale().ShortDescription()
          
          self.SceneShortDesc3P = "she " + WordList(["gave him a rim-job", "rimmed his " + sAnus, "licked his " + sAnus]).GetWord() 
          self.SceneShortDesc1PHim = "you " + WordList(["gave me a rim-job", "rimmed my " + sAnus, "licked my " + sAnus]).GetWord() 
          self.SceneShortDesc1PHer = "I " + WordList(["gave you a rim-job", "rimmed your " + sAnus, "licked your " + sAnus]).GetWord() 
     
     def Scene(self, Location = None):
          sScene = ""
          
          Actions = []
          
          Ass = excerpt.bodyparts.AssMale()
          Anus = excerpt.bodyparts.AnusFemale()
          Penis = excerpt.bodyparts.Penis()
          Breasts = excerpt.bodyparts.Breasts()
          
          sScene = self.HerName.capitalize() + " turned him around and knelt down behind him. "
          
          if CoinFlip():
               Actions.append("She tenderly kissed his " + Ass.RandomDescription(bAllowShortDesc = True))
          else:
               Actions.append("She began to massage his " + Ass.RandomDescription(bAllowShortDesc = True))
               
          Actions.append(" and then she spread his " + Ass.ShortDescription() + " apart, revealing his " + WordList(["hairy", "brown", "tight", "sensitive", "puckered"]).GetWord() + " " + Anus.ShortDescription() + ". ")
               
          if CoinFlip():
               Actions.append("She wet her finger with her tongue and then began to gently slide it around his rim. ")
          else:
               Actions.append("She nestled her face between his cheeks and gently kissed his rim. ")
               
          Actions.append("Then she began to lick it with her " + WordList(["long", "agile", "talented", "expert"]).GetWord() + " tongue. ")
          
          if CoinFlip():
               Actions.append("She heard him " + WordList(["moaning", "groaning", "sighing"]).GetWord() + " with pleasure. ")
               
          if CoinFlip():
               Actions.append("She reached around and took hold of his " + Penis.ShortDescription() + ". He was hard as a rock. Stroking it she ")
          else:
               Actions.append("She ")
          
          Actions.append("continued to rim his " + Anus.ShortDescription() + " eagerly")
          if CoinFlip():
               Actions.append(", enjoying the taste of him on her tongue.")
          else:
               Actions.append(", inserting the tip of her finger into his " + WordList(["snug", "tight", "constricting", "taut"]).GetWord() + " " + Anus.ShortDescription() + ".")
          
               
          for x in range(0, len(Actions)):
               sScene += Actions[x]
          
          return sScene 
          
class Scene69(Scene):     
     Tags = {TAG_BELOW_BELT, TAG_ORAL, TAG_POSITION}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "sixty-nined"
          self.VerbPresent = "sixty-nine"
          self.VerbGerund = "sixty-nining"
          
          self.SceneShortDesc3P = "they sixty-nined" 
          self.SceneShortDesc1PHim = "we sixty-nined"
          self.SceneShortDesc1PHer = "we sixty-nined"

     def Scene(self):
          sScene = ""
          
          FemBodyParts = excerpt.bodyparts.BodyFemale()
          MaleBodyParts = excerpt.bodyparts.BodyMale()
          Penis = MaleBodyParts.Penis 
          Vagina = FemBodyParts.Vagina
          Ass = FemBodyParts.Ass 
          
          Actions = []
          sText = ""
          
          if CoinFlip():
               Actions.append(self.HisName.capitalize() + " turned around and straddled " + self.HerNamePos + " " + FemBodyParts.Face.GetNewAdj() + " face and buried his face in her crotch. ")
          else:
               sText = self.HerName.capitalize() + " turned around and straddled " + self.HisNamePos + " face so that he had an intimate view of her " + Vagina.MediumDescription() + " and "
               if CoinFlip():
                    sText += Ass.MediumDescription() + ". Then she bent over his crotch. "
               else:
                    sText += Ass.Anus.MediumDescription() + ". Then she bent over his crotch. "
               Actions.append(sText)
          Actions.append(self.HisName.capitalize() + " began to " + WordList(["eat out", "lick", "suck on"]).GetWord() + " " + self.HerNamePos + " " + FemBodyParts.GetRandomHole(bIncludeMouth = False, bAllowShortDesc = True) + " while she took his " + Penis.RandomDescription() + " into her " + FemBodyParts.Mouth.RandomDescription(bAllowShortDesc = True) + " and " + excerpt.verbs.VerbOralMale().Past() + " him " + WordList(["passionately", "enthusiastically", "sloppily", "noisily", "eagerly", "expertly", "vigorously"]).GetWord() + ".")
          
          
          for x in range(0, len(Actions)):
               sScene += Actions[x]
               
          return sScene 
          
# class SceneX(Scene):     
     # def __init__(self, sHisName, sHerName, Location = None):
          # super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          # SceneShortDesc3P = "he "
          # SceneShortDesc1PHim = "I " 
          # SceneShortDesc1PHer = "you " 

     # def Scene(self):
          # sScene = ""
          
          # Actions = []
          
          # for x in range(0, len(Actions)):
               # sScene += Actions[x]
               
          # return sScene 
          
class SceneTitFuck(Scene):     
     Tags = {TAG_NON_PEN, TAG_DONE_TO_HER, TAG_FOREPLAY, TAG_ABOVE_BELT}
     def __init__(self, sHisName, sHerName, Location = None):
          super().__init__(sHisName = sHisName, sHerName = sHerName, Location = Location)
          
          self.VerbPast = "tit-fucked"
          self.VerbPresent = "tit-fuck"
          self.VerbGerund = "tit-fucking"
          
          self.SceneShortDesc3P = "he " + WordList(["tit-fucked", "titty-fucked"]).GetWord() + " her"
          self.SceneShortDesc1PHim = "I " + WordList(["tit-fucked", "titty-fucked"]).GetWord() + " you"
          self.SceneShortDesc1PHer = "you " + WordList(["tit-fucked", "titty-fucked"]).GetWord() + " me"
     
     def Scene(self):
          sScene = ""
          
          Breasts = excerpt.bodyparts.Breasts()
          Penis = excerpt.bodyparts.Penis()
          
          Actions = []
          
          sBreastAdj1 = Breasts.GetNewAdj()
          sPenisAdj1 = Penis.GetNewAdj()
     
          Actions.append(self.HerName.capitalize() + " squeezed her "+ sBreastAdj1 + ", " + Breasts.GetNewAdj(NotList = [sBreastAdj1]) + " " + Breasts.GetNoun() + " together. ")
          if CoinFlip():
               Actions.append(self.HisName.capitalize() + " spit into them and she rubbed them together sensually until they were slick and gleaming. ")
          else:
               Actions.append(self.HisName .capitalize()+ " poured some baby oil on them and then began to massage her " + Breasts.ShortDescription() + " and " + Breasts.Nipples.RandomDescription(bAllowShortDesc = True) + " until she was squirming with pleasure. ")
               
          Actions.append("Then he mounted her chest and began to slide his " + sPenisAdj1 + ", " + Penis.GetNewAdj(NotList = [sPenisAdj1]) + " " + Penis.ShortDescription() + " back-and-forth between them.")
     
          for x in range(0, len(Actions)):
               sScene += Actions[x]
          
          return sScene
          

          

#class SceneFingerHer(Scene):
#class SceneRubOnHim(Scene):
#class ScenePullOutFront(Scene):
#class ScenePullOutBack(Scene):
#class DryHump(Scene):
#class FootJob(Scene):
#class RimJobHim(Scene):

#class SceneSexAct(Scene):


# TAG_PEN = "sex act with penetration scene"
# TAG_NON_PEN = "non-penetrative sex act scene"
# TAG_DONE_TO_HER = "done to her scene"
# TAG_DONE_TO_HIM = "done to him scene"
# TAG_CLIMAX = "orgasm scene"
# TAG_POSITION = "sex position scene"
# TAG_FOREPLAY = "foreplay scene"
# TAG_ABOVE_BELT = "above-the-belt sex act scene"
# TAG_BELOW_BELT = "below-the-belt sex act scene"
# TAG_ORAL = "oral sex scene"
# TAG_CLOTHED = "scene where they still have clothes on"
          
class SceneSelector():
     def GetScene(self, sHisName, sHerName, Tags = None, NotTags = None, Location = None):
          ThisScene = None
          ThisLocation = None
          AllScenes = []
          MatchingScenes = []
          MatchingTags = set()
          MatchingNotTags = set()
          
          if not Tags is None:
               MatchingTags = Tags 
          else:
               MatchingTags = set()
               
          if not NotTags is None:
               MatchingNotTags = NotTags 
          else:
               MatchingNotTags = set()
               
          if not Location is None:
               ThisLocation = Location 
          else:
               ThisLocation = None
               
          for sub in Scene.__subclasses__():
               AllScenes.append(sub(sHisName = sHisName, sHerName = sHerName, Location = ThisLocation))
          
          if not AllScenes is None and len(AllScenes) > 0:
               for scene in AllScenes:
                    if (MatchingTags <= scene.Tags) and (MatchingNotTags & scene.Tags == set()):
                         MatchingScenes.append(scene)
               
          if len(MatchingScenes) > 0:
               ThisScene = MatchingScenes[randint(0, len(MatchingScenes) - 1)]
          
          return ThisScene

          