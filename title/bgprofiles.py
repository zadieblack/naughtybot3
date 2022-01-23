#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# background profiles module

import random
from util import *
from gen import *
from title.util import Content
import title.util as titutil
from misc import Synonyms

BGLOGFILEPATH = "title/"
BGLOGFILENAME = "bghistory_q.txt"
BGQSIZE = 100
MAXTRIES = 1000

ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, BGQSIZE)

class BGProfile(Generator):
    def __init__(self, ID = -1, Priority = GenPriority.Normal, 
                 HeaderType = HeaderType.Harlequin, 
                 sFileName = "",
                 Orient = ONEUTRAL,
                 Group = GSING):
        super().__init__(ID = ID, Priority = Priority)
        self.HeaderType = HeaderType 
        self.FileName = sFileName
        self.AdultsOnly = False

        #init all colors to black
        self.MainTitleColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.AllAges
        self.Tags = []
        self.Orient = Orient
        self.Group = Group

class BGProfileSaxaphone(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "saxophone",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(94, 68, 25, 255)"
        self.SecondTitleColor = "rgba(94, 68, 25, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "redhead","muscular","mistress","co-ed",
                     "college","jock","biker","rock star",
                     "teen","young","seduce","bad boy",
                     "athletic","alley","fire escape",
                     "window","saxophone","musician","leg",
                     "blue jeans","busty"]
        self.Disabled = False

class BGProfileBeach(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "beach",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(162, 63, 33, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "blonde","shirtless","beach","swimsuit",
                     "vacation","water","island",]
        self.Disabled = False

class BGProfileCrotchLevel(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "crotch_level",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(193, 29, 63, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.SmallTextColor = "rgba(112, 162, 193, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "brunette","redhead","muscular","indian",
                     "mountains","bird","eagle","warrior","barbarian",
                     "giant","oral",
                     ]
        self.Disabled = False

class BGProfileBoatNipples(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "boat_nipples",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(39, 32, 73, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(39, 32, 73, 255)"
        self.AuthorNameColor = "rgba(39, 32, 73, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","pirate","ship","boat",
                     "fantasy","historic","prince",]
        self.Disabled = False

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "blue_car_fire",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(132, 41, 55, 255)"
        self.SecondTitleColor = "rgba(181, 55, 47, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"
        self.Tags = ["man","woman","couple","outside","straight","brunette",
                     "modern","car","fire","wealthy","road","wife","husband",
                     "babysitter","bachelor",]
        self.Disabled = False

class BGProfileBlueCity(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "blue_city",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(132, 41, 55, 255)"
        self.SecondTitleColor = "rgba(181, 55, 47, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "modern","city","night","shirtless","muscular",
                     "wealthy","prince","slender","prom queen",]
        self.Disabled = False

class BGProfileIndian(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "indian",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(157, 44, 43, 255)"
        self.SecondTitleColor = "rgba(157, 44, 43, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["man","woman","couple","outside","straight","western",
                     "shirtless","muscular","indian"]
        self.Disabled = False

class BGProfileNakedFabio(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "naked_fabio",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(238, 146, 134, 255)"
        self.SecondTitleColor = "rgba(238, 146, 134, 255)"
        self.SmallTextColor = "rgba(96, 39, 116, 255)"
        self.AuthorNameColor = "rgba(96, 39, 116, 255)"
        self.Tags = ["man","woman","couple","outside","straight","redhead",
                     "shirtless","muscular","fabio","kidnapped","hairy",
                     "lingerie","corset","busty","cleavage","clouds",
                     "windy","teen","warrior","barbarian","fantasy",
                     "strip","exposed","giant"]
        self.Disabled = False

class BGProfilePirate(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "pirate",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(65, 112, 130, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(191, 77, 59, 255)"
        self.AuthorNameColor = "rgba(65, 112, 130, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "tied up","pirate","ship","maledom","bound",
                     "kidnapped","milf","mom",
                     "brunette","older man","fantasy","lord","pirate",
                     "busty","breasts","cleavage","strip",]
        self.Disabled = False

class BGProfileAquaTopless(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "aqua_topless",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(149, 196, 180, 255)"
        self.SecondTitleColor = "rgba(108, 80, 145, 255)"
        self.Tags = ["man","woman","couple","straight","brunette","topless",
                     "shirtless","muscular","young","teen","virgin",
                     "daughter",]
        self.Disabled = False

class BGProfileGay(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "gay",
                           Orient = OGAY,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(189, 109, 65, 255)"
        self.SecondTitleColor = "rgba(189, 109, 65, 255)"
        self.SmallTextColor = "rgba(108, 145, 51, 255)"
        self.Tags = ["man","men","couple","gay","naked","muscular"]
        self.Disabled = False

class BGProfileSunset(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "sunset",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(178, 27, 44, 255)"
        self.SecondTitleColor = "rgba(178, 27, 44, 255)"
        self.Tags = ["man","woman","couple","outside","straight","brunette",
                     "shirtless","muscular","western","historic","outlaw",
                     "cowboy","older man","dad","dilf","fire","sunset",
                     "blue jeans","strip","wife","teacher","country",
                     "school-marm","lady","bandit","robber","biker",]
        self.Disabled = False

class BGProfileField(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "field",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(214, 149, 123, 255)"
        self.SecondTitleColor = "rgba(139, 121, 171, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "muscular","brunette","fantasy","historic","muscular",]
        self.Disabled = False

class BGProfileRedVelvet(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "red_velvet",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(181,55, 47, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.Tags = ["man","woman","couple","straight","brunette","shirtless",
                     "muscular","bed","lord","lady","red dress","blonde",
                     "tits","busty","groped","boss",
                     "prince","daughter","dad",]
        self.Disabled = False

class BGProfileRedAndPurple(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "red_and_purple",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(209, 91, 56, 255)"
        self.SecondTitleColor = "rgba(209, 91, 56, 255)"
        self.SmallTextColor = "rgba(174, 95, 160, 255)"
        self.Tags = ["man","woman","couple","straight","redhead","bed",
                     "shirtless","muscular","lingerie","nightgown",
                     "cleavage","breasts","busty","boss",
                     "fantasy","strip","jock","secretary","mistress",]
        self.Disabled = False

class BGProfileSeventiesChic(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "seventies_chic",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(194, 76, 39, 255)"
        self.SecondTitleColor = "rgba(139, 68, 25, 255)"
        self.SmallTextColor = "rgba(165, 150, 58, 255)"
        self.AuthorNameColor = "rgba(139, 68, 25, 255)"
        self.Tags = ["man","woman","couple","straight","blonde","boss",
                     "secretary","wife","business","CEO","tie","dress",
                     "mistress","mom","milf","cleavage","busty","tits",
                     "fireplace","shag carpet","carpet","bachelor",]
        self.Disabled = False

class BGProfileBlueDress(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "blue_dress",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(181, 79, 75, 255)"
        self.SecondTitleColor = "rgba(181, 79, 75, 255)"
        self.SmallTextColor = "rgba(1, 23, 244, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "shirtless","muscular","legs","leggy","busty",
                     "dress","blue","medieval","fantasy","historic",
                     "prince","nobleman","wealthy","manor lord",
                     "princess",]
        self.Disabled = False

class BGProfileDarkBlueFireSuit(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "dark_blue_fire_suit",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(173, 84, 69, 255)"
        self.SecondTitleColor = "rgba(173, 84, 69, 255)"
        self.SmallTextColor = "rgba(53, 68, 89, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "suit","raven-haired", "fire","boss","teacher",
                     "sunset","bachelor","jewish",]
        self.Disabled = False

class BGProfileDark(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "dark",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(84, 77, 93, 255)"
        self.SecondTitleColor = "rgba(84, 77, 93, 255)"
        self.Tags = ["man","woman","couple","straight","brunette",
                     "busty","undressing","historic","fantasy",
                     "night","latina","french","lady","prince",
                     "lord","fantasy","dress","shoulder",]
        self.Disabled = False

class BGProfileGold(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "gold",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(106, 118, 47, 255)"
        self.SecondTitleColor = "rgba(106, 118, 47, 255)"
        self.SmallTextColor = "rgba(106, 118, 47, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "muscular","topless","raven-haired","brunette","jock",
                     "towel","bachelor","asian","french","japanese","jewish",]
        self.Disabled = False

class BGProfileModernBedroom(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "modern_bedroom",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(143, 137, 104, 255)"
        self.SecondTitleColor = "rgba(177, 119, 123, 255)"
        self.AuthorNameColor = "rgba(143, 137, 104, 255)"
        self.Tags = ["man","woman","couple","inside","straight","redhead",
                     "shirtless","muscular","bed","horny","bedroom",
                     "lingerie","dad","daughter","younger","mistress",
                     "boss","secretary","coach","jock","bachelor"]
        self.Disabled = False

class BGProfileShipRomance(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "ship_romance",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(75, 125, 152, 255)"
        self.SecondTitleColor = "rgba(75, 125, 152, 255)"
        self.SmallTextColor = "rgba(200, 159, 193, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "ship","boat","pirate","kidnap","bound","tied up",
                     "prisoner","captive","busty","breasts","tits",
                     "strip","undress","lord","lady","baron","duke",
                     "slave","fantasy","hstoric","sea","ocean",]
        self.Disabled = False

class BGProfileBath(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "bath",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(209, 165, 48, 255)"
        self.SecondTitleColor = "rgba(145, 55, 63, 255)"
        self.SmallTextColor = "rgba(27, 112, 105, 255)"
        self.AuthorNameColor = "rgba(27, 112, 105, 255)"
        self.Tags = ["man","woman","couple","inside","straight","brunette",
                     "topless","nude","naked","bath","tub","dad",
                     "older man","father","soap","wet","french"]
        self.Content = Content.PG13
        self.Disabled = False
        
class BGProfileBedSurprise(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "bed_surprise",
                           Orient = ONEUTRAL,
                           Group = GSING)
        self.MainTitleColor = "rgba(186, 73, 27, 255)"
        self.SecondTitleColor = "rgba(186, 73, 27, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"
        self.Tags = ["woman","single","redhead","bed","sleep","bottle",
                     "drink","surprise","maledom","scotch","irish",]
        self.Disabled = False

class BGProfileBoatTowel(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "boat_towel",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(175, 98, 53, 255)"
        self.SecondTitleColor = "rgba(175, 98, 53, 255)"
        self.SmallTextColor = "rgba(7, 10, 14, 255)"
        self.AuthorNameColor = "rgba(7, 10, 14, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "fabio","shirtless","muscular","ship","boat","pirate",
                     "modern",]
        self.Disabled = False

class BGProfileCastle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "castle",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(107, 66, 113, 255)"
        self.SecondTitleColor = "rgba(158, 162, 61, 255)"
        self.SmallTextColor = "rgba(141, 50, 33, 255)"
        self.AuthorNameColor = "rgba(87, 170, 207, 255)"
        self.Tags = ["man","woman","couple","outside","straight","fantasy",
                     "blonde","medieval","castle","princess","prince",
                     "boots","gown","kidnapped","historic","german",
                     "french","irish","english","british",]
        self.Disabled = False

class BGProfileKinkyCuffs(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "kinky_cuffs",
                           Orient = ONEUTRAL,
                           Group = GSING)
        self.MainTitleColor = "rgba(170, 26, 24, 255)"
        self.SecondTitleColor = "rgba(170, 26, 24, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"
        self.Content = Content.PG13
        self.Tags = ["woman","single","outside","kinky","blonde","tied up","bound",
                     "maledom","cuffs","surprise","busty","nipple",
                     "teacher","secretary","wife","prisoner",]
        self.Disabled = False
        
class BGProfileMansion(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "mansion",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(221, 132, 34, 255)"
        self.SecondTitleColor = "rgba(41, 89, 135, 255)"
        self.SmallTextColor = "rgba(47, 78, 83, 255)"
        self.AuthorNameColor = "rgba(41, 89, 135, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","mansion","manor","wealthy","business",
                     "businessman","lord","millionaire","billionaire",
                     "sunset","teen","business","businessman","suit",
                     "boss",]
        self.Disabled = False

class BGProfileShower(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "shower",
                           Orient = OSTRAIGHT,
                           Group = GSING)
        self.MainTitleColor = "rgba(199, 54, 60, 255)"
        self.SecondTitleColor = "rgba(210, 150, 78, 255)"
        self.SmallTextColor = "rgba(74, 155, 189, 255)"
        self.AuthorNameColor = "rgba(199, 54, 60, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","straight","brunette","naked","nude",
                     "tits","suit","single","shower","surprise",
                     "teen","co-ed","college","young","daughter",
                     "business","dad","father","locker room",
                     "bath","wet","young","voyeur","babysitter",
                     "breasts","ass","butt","expose","undress",
                     "brat",]
        self.Disabled = False

class BGProfileSuperHero(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "superhero",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(189, 42, 20, 255)"
        self.SecondTitleColor = "rgba(189, 42, 20, 255)"
        self.SmallTextColor = "rgba(205, 66, 109, 255)"
        self.AuthorNameColor = "rgba(122, 86, 172, 255)"
        self.Tags = ["man","woman","couple","straight","brunette",
                     "shirtless","muscular","superhero","cape",
                     "nightgown","busty","tits","breasts",
                     "kidnap","capture","rescue","grab","warrior",
                     "stars",]
        self.Disabled = False

class BGProfileSwingers(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "swingers",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(203, 62, 76, 255)"
        self.SecondTitleColor = "rgba(203, 62, 76, 255)"
        self.SmallTextColor = "rgba(99, 113, 160, 255)"
        self.AuthorNameColor = "rgba(184, 172, 84, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","nature","swing","pink","dress",
                     "young","teen","daughter","sister","innocent","virgin",
                     "pink dress","historic","brother","lord","duke",
                     "prince","princess","swing","park","forest","giant",
                     "large",]
        self.Disabled = False
        
class BGProfileSwordKilt(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "sword_kilt",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(135, 49, 40, 255)"
        self.SecondTitleColor = "rgba(79, 86, 194, 255)"
        self.SmallTextColor = "rgba(41, 67, 193, 255)"
        self.AuthorNameColor = "rgba(135, 49, 58, 255)"
        self.Tags = ["man","woman","couple","outside","straight","fantasy",
                     "brunette","shirtless","muscular","kilt","sword",
                     "forest","warrior","teen","young","scot",
                     "park","leggy","legs","trees","nightgown","shirt",
                     "jock","lord","serv","daughter","sister","slender",]
        self.Disabled = False

class BGProfileTightButts(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "tight_butts",
                           Orient = OGAY,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(108, 178, 234, 255)"
        self.SecondTitleColor = "rgba(99, 36, 2, 255)"
        self.SmallTextColor = "rgba(72, 87, 56, 255)" 
        self.AuthorNameColor = "rgba(108, 178, 234, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","gay","outside","naked","nude","butt",
                     "tanlines","muscular","water","boat","ass","wet",
                     "bronzed","buns","thong",]
        self.Disabled = False

class BGProfileTropicalPirate(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "tropical_pirate",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(195, 21, 48, 255)"
        self.SecondTitleColor = "rgba(195, 21, 48, 255)"
        self.SmallTextColor = "rgba(35, 135, 63, 255)"
        self.AuthorNameColor = "rgba(38, 167, 207, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","ship","historical","beach",
                     "palm tree","island","tropical","vacation","island",
                     "lady","lord","prince","duke","baron","fantasy",
                     "pirate","busty","pink dress","ponytail",]
        self.Disabled = False

class BGProfileBeefcakeAngel(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "beefcake_angel",
                           Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(205, 99, 139, 255)"
        self.SecondTitleColor = "rgba(205, 99, 139, 255)"
        self.SmallTextColor = "rgba(101, 44, 84, 255)"
        self.AuthorNameColor = "rgba(101, 44, 84, 255)"
        self.Tags = ["man","woman","muscular","shirtless","angel","fantasy",
                     "brunette","straight","couple","stars","belt","brunette",
                     "wings","warrior","giant","large","amish",
                     ]
        self.Disabled = False
        
class BGProfileChamberPot(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "chamber_pot",
                           Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(198, 94, 21, 255)"
        self.SecondTitleColor = "rgba(198, 94, 21, 255)"
        self.SmallTextColor = "rgba(170, 60, 133, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","fantasy","historical","kinky","brunette",
                     "man","flower","tuxedo","naked","nude","tits","ass",
                     "butt","single","tuxedo","suit","bed","peed",
                     "pissed","wealthy","millionaire","billionaire",
                     "lord","lady","duke","stockings","breasts",
                     "busty","rose","mature","older man","older woman",
                     "milf","exposed","french","porn star",]
        self.Disabled = False

class BGProfileChastityBelt(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                         sFileName = "chastity_belt",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(85, 89, 177, 255)"
        self.SecondTitleColor = "rgba(155, 36, 45, 255)"
        self.SmallTextColor = "rgba(6, 60, 86, 255)"
        self.AuthorNameColor = "rgba(85, 89, 177, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","straight","kinky","fantasy","topless",
                     "shirtless","muscular","tits","blonde","historical",
                     "femdom","boobs","breasts","curls","chastity belt",
                     "lock","lady","duchess","princess","queen",
                     "mistress","throne","chair","swedish","french",
                     "wife","husband",]
        self.Disabled = False

class BGProfileCowgirlDominatrix(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                         sFileName = "cowgirl_dominatrix",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(19, 37, 113, 255)"
        self.SecondTitleColor = "rgba(19, 37, 113, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 149, 60, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","kinky","blonde",
                     "naked","nude","tits","BDSM","femdom","cowgirl",
                     "straddled","ridden","breasts","boots","vest",
                     "prisoner","cowboy","american",]
        self.Disabled = False

class BGProfileDickNose(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "dick_nose",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(32, 124, 207, 255)"
        self.SecondTitleColor = "rgba(225, 47, 37, 255)"
        self.SmallTextColor = "rgba(198, 78, 107, 255)"
        self.AuthorNameColor = "rgba(225, 47, 37, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","outside","straight","kinky",
                     "blonde","topless","shirtless","muscular","arabic","circus",
                     "nose","bed","october","older man","bald","busty",
                     "tits","breasts","underwear","lingerie","fellatio",
                     "blowjob","bed","circus","oral","porn","call girl",
                     "whore",]
        self.Disabled = False

class BGProfileHandsAndKnees(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "hands_and_knees",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(210, 136, 53, 255)"
        self.SecondTitleColor = "rgba(210, 136, 53, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.PG13
        self.Tags = ["woman","fantasy","kinky","redhead","loincloth",
                     "suit","historical","single","straight",
                     "maledom","knees","hands and knees","all fours",
                     "ass","butt","tits","breasts","suit","brunette",
                     "busty","stripped","exposed","broken","slave",
                     ]
        self.Disabled = False

class BGProfileHarem(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "harem",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(62, 162, 167, 255)"
        self.AuthorNameColor = "rgba(62, 162, 167, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","woman","women","fantasy","brunette","blonde",
                     "bikini","tits","harem","straight","nipple","nipslip",
                     "pillow","sheikh","concubine","sultan","lord",
                     "sheikh","king","young","fantasy","breasts",
                     "wealthy","millionaire","billionaire","slut",]
        self.Disabled = False

class BGProfileHotCops(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "hot_cops",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(107, 173, 53, 255)"
        self.SecondTitleColor = "rgba(107, 173, 53, 255)"
        self.SmallTextColor = "rgba(184, 160, 43, 255)"
        self.AuthorNameColor = "rgba(184, 160, 43, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","redhead",
                     "blonde","cops","cop","threesome","shirtless","muscular",
                     "topless","tits","femdom","police","american","swedish",
                     "french","stripper","porn","orgy",]
        self.Disabled = False

class BGProfileIndecentProp(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "indecent_prop",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(186, 155, 47, 255)"
        self.SecondTitleColor = "rgba(113, 25, 24, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(186, 155, 47, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","brunette",
                     "nude","naked","tits","ass","money","gambling",
                     "tuxedo","historic","casino","straight","money",
                     "suit","victorian","butt","wealthy","lord","lady",
                     "slut","bed","stockings","heels","party",
                     "call girl","money",]
        self.Disabled = False

class BGProfileLadyBottom(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "lady_bottom",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(15, 84, 120, 255)"
        self.SecondTitleColor = "rgba(15, 84, 120, 255)"
        self.SmallTextColor = "rgba(88, 105, 73, 255)"
        self.AuthorNameColor = "rgba(88, 105, 73, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","outside","fantasy","blonde","nude",
                     "naked","horse","straight","medieval","historic",
                     "stockings","knight","warrior","lady",
                     "ass","tits","nude","queen","princess",
                     "hat","horse","french","maiden",
                     ]
        self.Disabled = False

class BGProfileLesbianVampires(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "lesbian_vampires",
                         Orient = OLES,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(123, 83, 137, 255)"
        self.SecondTitleColor = "rgba(123, 83, 137, 255)"
        self.SmallTextColor = "rgba(212, 1, 3, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","women","inside","lesbian","kinky","horror",
                     "castle","raven-haired","redhead","blonde","vampire","october",
                     "medieval","fantasy","nails","brunette","castle","horror",
                     "undressed","horny","stripped","strips","undresses",
                     "seduced","fingered","panties","busty","lady","maiden",]
        self.Disabled = False

class BGProfileMaleSub(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "male_sub",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(26, 79, 155, 255)"
        self.SecondTitleColor = "rgba(26, 79, 155, 255)"
        self.SmallTextColor = "rgba(131, 149, 93, 255)"
        self.AuthorNameColor = "rgba(200, 114, 184, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","kinky",
                     "femdom","nude","naked","shirtless","topless","tits",
                     "brunette","bed","cunnilingus","breasts","busty",
                     "brunette","older woman","mature","cougar","bed",
                     "stockings","panties","lingerie","mistress",
                     "horny","duchess","lady",]
        self.Disabled = False

class BGProfileMoonBoob(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "moon_boob",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(186, 51, 57, 255)"
        self.SecondTitleColor = "rgba(186, 51, 57, 255)"
        self.SmallTextColor = "rgba(31, 51, 82, 255)"
        self.AuthorNameColor = "rgba(224, 183, 108, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "naked","nude","shirtless","topless","tits","ocean",
                     "bed","sea","water","breasts","nipple","kiss","sex",
                     "horny","bridge","porch","moon","bed",]
        self.Disabled = False

class BGProfileFlex(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "flex",
                         Orient = ONEUTRAL,
                           Group = GSING)
        self.MainTitleColor = "rgba(199, 47, 19, 255)"
        self.SecondTitleColor = "rgba(49, 114, 44, 255)"
        self.SmallTextColor = "rgba(1, 77, 119, 255)"
        self.AuthorNameColor = "rgba(1, 77, 119, 255)"
        self.Tags = ["man","indoors","muscular","shirtless","single",
                     "strong","flex","giant","large","gym",
                     "body builder",]
        self.Disabled = False

class BGProfilePervyDummy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "pervy_dummy",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(196, 50, 45, 255)"
        self.SecondTitleColor = "rgba(196, 50, 45, 255)"
        self.SmallTextColor = "rgba(123, 77, 151, 255)"
        self.AuthorNameColor = "rgba(123, 77, 151, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","kinky","man","fantasy","dwarf",
                     "naked","nude","tits","ass","pissing","straight",
                     "butt","busty","breasts","slut","horny","pee",
                     "peed","wet","water","barrel",]
        self.Disabled = False

class BGProfilePoodleBondage(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "poodle_bondage",
                         Orient = ONEUTRAL,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(83, 84, 141, 255)"
        self.AuthorNameColor = "rgba(83, 84, 141, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","kinky","blonde","brunette",
                     "femdom","topless","naked","nude","tits","ass",
                     "tied up","straight","dog","poodle","bound",
                     "butt","breasts","teen","duchess","heiress",
                     "horny","panties","lady","spoiled","stockings",
                     ]
        self.Disabled = False

class BGProfileScaryMirror(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "scary_mirror",
                         Orient = ONEUTRAL,
                           Group = GSING)
        self.MainTitleColor = "rgba(202, 141, 14, 255)"
        self.SecondTitleColor = "rgba(202, 141, 14, 255)"
        self.SmallTextColor = "rgba(62, 122, 79, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","inside","horror","blonde",
                     "bed","masturbation","bed","single",
                     "surprise","horny","slut","young","teen",
                     "co-ed","college","wife","breasts","tits",
                     "naked","nude","naughty","expose",
                     "strip","undress","swedish","jilling",
                     "mirror","surprise",]
        self.Disabled = False

class BGProfileSkeleton(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "skeleton",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(157, 16, 16, 255)"
        self.SecondTitleColor = "rgba(157, 16, 16, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","horror","brunette","topless",
                     "naked","nude","bed","skeleton","tits","bush",
                     "october","undead","breasts","pussy","undress",
                     "strip","fantasy","lady","mature","wife",
                     "sleep","busty","mom","mother","milf","knife",
                     "warrior","mature","older woman","surprise",
                     "bone",]
        self.Disabled = False

class BGProfileSnowWhiteSevenDwarves(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "snow_white_7_dwarves",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(52, 117, 47, 255)"
        self.SecondTitleColor = "rgba(52, 117, 47, 255)"
        self.SmallTextColor = "rgba(30, 63, 139, 255)"
        self.AuthorNameColor = "rgba(30, 63, 139, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","inside","kinky","fantasy","dwarf",
                     "raven-haired", "naked", "nude", "tits",
                     "panties","bed","single","straight",
                     "dwarves","brunette","underwear","teen",
                     "young","innocent","busty","kidnap",
                     "expose","strip","undress","daughter",

                     ]
        self.Disabled = False

class BGProfileDangerMine(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "danger_mine",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(205, 97, 71, 255)"
        self.SecondTitleColor = "rgba(231, 140, 81, 255)"
        self.SmallTextColor = "rgba(1, 77, 119, 255)"
        self.AuthorNameColor = "rgba(79, 27, 36, 255)"
        self.Tags = ["man","woman","outdoors","blonde","couple","straight",
                     "danger","mine"]
        self.Disabled = False

class BGProfileSnowWhiteDungeon(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "snow_white_dungeon",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(32, 89, 161, 255)"
        self.SecondTitleColor = "rgba(32, 89, 161, 255)"
        self.SmallTextColor = "rgba(238, 64, 130, 255)"
        self.AuthorNameColor = "rgba(241, 148, 33, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","fantasy","kinky","knight","raven-haired",
                     "tied up","topless","tits","straight","warrior","busty",
                     "tits","breasts","panties","rescue","princess","lady",
                     "captive","prisoner","cuff","submit","maledom","teen",
                     "older man","castle","dungeon","chain","nipples",
                     "nightgown","lingerie","monster","lord","lady","strip",
                     "undress","maiden",]
        self.Disabled = False

class BGProfileSnowWhiteSpanking(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "snow_white_spanking",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(131, 58, 110, 255)"
        self.SecondTitleColor = "rgba(131, 58, 110, 255)"
        self.SmallTextColor = "rgba(23, 81, 136, 255)"
        self.AuthorNameColor = "rgba(23, 81, 136, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","men","fantasy","kinky","viking",
                     "raven-haired","naked","nude","ass","spanking",
                     "straight","maledom","warrior","butt","brat",
                     "teen","strip","expose","punish","discipline",
                     "young","daughter","brunette","pale","king",
                     "undress","pound","paddle","beat",]
        self.Disabled = False

class BGProfileStretchyArms(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "stretchy_arms",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(227, 31, 15, 255)"
        self.SecondTitleColor = "rgba(227, 31, 15, 255)"
        self.SmallTextColor = "rgba(74, 61, 34, 255)"
        self.AuthorNameColor = "rgba(74, 61, 34, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","blonde",
                     "shirtless","nude","naked","tits","weird arms",
                     "monster","alien","redhead","stretch",
                     "tentacles","teen","mom","slut","waitress",
                     "grab","hold","capture","prisoner","bed",
                     "strip","breasts","shirtless",]
        self.Disabled = False

class BGProfileSurroundedByPervs(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "surrounded_by_pervs",
                         Orient = OSTRAIGHT,
                           Group = GGROUP)
        self.MainTitleColor = "rgba(66, 103, 86, 255)"
        self.SecondTitleColor = "rgba(196, 107, 28, 255)"
        self.SmallTextColor = "rgba(79, 89, 174, 255)"
        self.AuthorNameColor = "rgba(79, 89, 174, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","men","kinky","man","blonde","naked",
                     "nude","masturbation","single","straight",
                     "perv","voyeur","teen","masturb","horny",
                     "slut","college","co-ed","daughter",
                     "sister","fantasy","medieval","historic",
                     "dwarf","stockings","blue","chair",
                     "princess","lady","lord","duke","baron",
                     "vest","strip","expose","undress","nudist",]
        self.Disabled = False

class BGProfileTallWoman(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "tall_woman",
                         Orient = OSTRAIGHT,
                           Group = GCOUP)
        self.MainTitleColor = "rgba(77, 172, 243, 255)"
        self.SecondTitleColor = "rgba(77, 172, 243, 255)"
        self.SmallTextColor = "rgba(210, 119, 82, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","brunette",
                     "topless","tits","femdom","giantess","femdom","widow",
                     "tutor","governess","busty","big tit","breasts",
                     "strip","babysitter","chair","nylons","stockings",
                     "business","CEO","wealthy","bachelor",]
        self.Disabled = False

class BGProfileTheDevil(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "the_devil",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(212, 80, 83, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(47, 84, 51, 255)"
        self.AuthorNameColor = "rgba(47, 84, 51, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","naked","nude","october",
                     "topless","tits","brunette","vampire","horror",
                     "bed","sex","monster","red","breast","nipple","strip",
                     "undress","expose","grab","horns","horny",
                     "slut","dead","stripper","devil",]
        self.Disabled = False

class BGProfileFireplaceBeauty(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "fireplace_beauty",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(213, 22, 24, 255)"
        self.SecondTitleColor = "rgba(254, 171, 15, 255)"
        self.SmallTextColor = "rgba(11, 84, 115, 255)"
        self.AuthorNameColor = "rgba(11, 84, 115, 255)"
        self.Tags = ["woman","indoors","blonde","butt","fireplace",
                     "mirror","single","flower","teen","lady",
                     "young","nightgown","lingerie","fire",
                     "innocent","starlet",
                     ]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileVampire(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "vampire",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(23, 72, 199, 255)"
        self.SecondTitleColor = "rgba(23, 72, 199, 255)"
        self.SmallTextColor = "rgba(91, 48, 162, 255)"
        self.AuthorNameColor = "rgba(91, 48, 162, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","inside","kinky","horror","blonde","october",
                     "vampire","blood","fangs","naked","nude","tits",
                     "ass","butt","killer","curvy","bite","vixen","whore","slut",
                     "strip","horny","bed","bad girl","violent",]
        self.Disabled = False

class BGProfileUnderBedCreeper(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "under_bed_creeper",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(130, 43, 39, 255)"
        self.SecondTitleColor = "rgba(199, 131, 61, 255)"
        self.SmallTextColor = "rgba(127, 117, 53, 255)"
        self.AuthorNameColor = "rgba(130, 43, 39, 255)"
        self.Tags = ["man","woman","couple","inside","men","voyeur",
                     "brunette","bed","arabic","shirtless","muscular",
                     "straight","kinky","cuckold","sheikh","wife",
                     "daughter","teen","panties","lingerie",
                     "stockings","secretary","watch","sultan","pale",
                     ]
        self.Disabled = False

class BGProfileVictorianOrgy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "victorian_orgy",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(48, 76, 124, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","fantasy",
                     "bed","orgy","nude","nudist","lord","duke","baron",
                     "count","serv","harem","breasts","tits","busty",
                     "ass","daughter","maid","wealthy","older woman",
                     "cougar","swinger","teen","young","governess",
                     "strip","undress","expose","victorian"]
        self.Disabled = False

class BGProfileVoyeur(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "voyeur",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(154, 46, 93, 255)"
        self.SecondTitleColor = "rgba(38, 95, 145, 255)"
        self.SmallTextColor = "rgba(67, 102, 122, 255)"
        self.AuthorNameColor = "rgba(154, 46, 93, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","women","inside","bed",
                     "jealous","threesome","lord","lady","wealthy",
                     "watch","spy","blonde","redhead","brunette",
                     "sex","brother","sister","busty","boobs",
                     "tits","breasts","voyeur","sultan","sheikh",]
        self.Disabled = False

class BGProfileWizardPony(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "wizard_pony",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(215, 67, 47, 255)"
        self.SecondTitleColor = "rgba(38, 91, 152, 255)"
        self.SmallTextColor = "rgba(29, 36, 0, 255)"
        self.AuthorNameColor = "rgba(29, 36, 0, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","men","inside","kinky","fantasy",
                     "wizard","femdom","straight","busty","breasts",
                     "tits","nude","naked","nudist","expose","strip",
                     "slut","older man","old man","ass","butt",
                     "dwarf","teen",]
        self.Disabled = False

class BGProfileDoggyStyle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "doggy_style",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(113, 54, 24, 255)"
        self.SecondTitleColor = "rgba(113, 54, 24, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","naked",
                     "nude","tits","ass","pussy","sex","whore","horny",
                     "bed","hardcore","stockings","slut","porn star",
                     "penis","erect","bronzed","mom","milf",
                     "mature","wife","concubine",]
        self.Disabled = False

class BGProfileBathhouse(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "bathhouse",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(30, 102, 139, 255)"
        self.SecondTitleColor = "rgba(150, 85, 45, 255)"
        self.SmallTextColor = "rgba(150, 85, 45, 255)"
        self.AuthorNameColor = "rgba(196, 89, 81, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","inside","fantasy","gay","historic",
                     "naked","nude","shirtless","muscular","bath",
                     "pool","towel","wet",]
        self.Disabled = False

class BGProfileJilling(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "jilling",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(91, 24, 45, 255)"
        self.SecondTitleColor = "rgba(181, 48, 43, 255)"  
        self.SmallTextColor ="rgba(106, 102, 69, 255)"
        self.AuthorNameColor = "rgba(91, 24, 45, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","inside","topless",
                     "tits","bed","teen","nightgown","young","college",
                     "co-ed", "panties","yellow nightgown","bed",
                     "jilling","pussy","jewish","french","horny",]
        self.Disabled = False

class BGProfileBranded(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "branded",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(66, 75, 132, 255)"
        self.SecondTitleColor = "rgba(200, 82, 65, 255)"  
        self.SmallTextColor ="rgba(54, 50, 74, 255)"
        self.AuthorNameColor = "rgba(66, 75, 132, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","outside","gay","cowboy",
                     "nude","naked","shirtless","muscular",
                     "penis","thong","brand","cowboys",
                     "cowboy hat","gun","pistol","ranch",
                     "bandit","bulge","country","thong",]
        self.Disabled = False

#class BGProfileGrapes(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 69,
#                           Priority = 4,
#                           sFileName = "grapes")
#        self.MainTitleColor = "rgba(228, 171, 62, 255)"
#        self.SecondTitleColor = "rgba(152, 53, 88, 255)"  
#        self.SmallTextColor ="rgba(100, 135, 70, 255)"
#        self.AuthorNameColor = "rgba(152, 53, 88, 255)"
#        self.Content = Content.PG13
#        self.Tags = ["man","single","gay"]
#        self.Disabled = False

class BGProfileUnderwater(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "underwater",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(228, 171, 62, 255)"
        self.SecondTitleColor = "rgba(150, 97, 131, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(228, 171, 62, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","outside","gay","underwater","swim",
                     "nude","naked","abs","muscular","butt","ass",
                     "athletic","fit","jock","twink",]
        self.Disabled = False

class BGProfileSlaves(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "slaves",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(169, 61, 55, 255)"
        self.SecondTitleColor = "rgba(212, 167, 84, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(50, 158, 194, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","kinky","outside","gay","fantasy",
                     "historic","shirtless","muscular","codpiece",
                     "whip","tied up","bondage","slave","slaves",
                     "thong","jock","bulge","penis","bdsm","gym",]
        self.Disabled = False

class BGProfileNakedCowboy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "naked_cowboy",
                         Orient = OGAY,
                         Group = GSING)
        self.MainTitleColor = "rgba(138, 52, 46, 255)"
        self.SecondTitleColor = "rgba(83, 125, 148, 255)"  
        self.SmallTextColor ="rgba(205, 163, 106, 255)"
        self.AuthorNameColor = "rgba(138, 52, 46, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","single","outside","gay","nude","naked",
                     "shirtless","muscular","cowboy","horse","hat",
                     "ass","butt",]
        self.Disabled = False

class BGProfileTwoGirls(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "two_girls",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(255, 210, 47, 255)"
        self.SecondTitleColor = "rgba(83, 115, 148, 255)"  
        self.SmallTextColor ="rgba(205, 66, 35, 255)"
        self.AuthorNameColor = "rgba(83, 115, 148, 255)"  
        self.Content = Content.PG13
        self.Tags = ["woman","women","lesbian","redhead","blonde",
                     "college","co-ed","teen","underwear","bra",
                     "panties","butt","ass","strip","undress",
                     "stripper","slut","cheerleader","horny",]
        self.Disabled = False

class BGProfileSpaceMonster(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "space_monster",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.SmallTextColor = "rgba(199, 22, 30, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 
        self.Tags = ["woman","outside","kinky","tentacles","space",
                     "scifi","single","alien","slender","busty",
                     "mom","milf","grab","capture","probe","milf",
                     "silver","jumpsuit","brunette","helmet",
                     "stars","spaceship","athletic","tall",
                     "sporty","monster",]
        self.Disabled = False

class BGProfileOneEyedAlien(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "one_eyed_alien",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(219, 103, 122, 255)"
        self.SecondTitleColor = "rgba(72, 146, 145, 255)"  
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 
        self.Tags = ["women","woman","outside","scifi","alien",
                     "space","camera","stripper","butt","ass",
                     "brunette","blonde","watched","strip",
                     "stripping","stripped","undressed",
                     "undressing","underwear","panties",
                     "stockings","stars","topless","teen",]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileSpaceGirl(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "space_girl",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(48, 66, 138, 255)"
        self.SecondTitleColor = "rgba(48, 66, 138, 255)"
        self.SmallTextColor = "rgba(245, 180, 47, 255)"
        self.AuthorNameColor = "rgba(229, 79, 24, 255)" 
        self.Content = Content.PG13
        self.Tags = ["woman","single","outside","space","scifi",
                     "blonde","brunette","redhead","helmet",
                     "ray gun", "jetpack", "pinup", "teen",
                     "young", "co-ed", "college", "starlet",
                     "scotch","irish","american","alien",]
        self.Disabled = False

class BGProfileHawaiianCleavage(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "hawaiian_cleavage",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(105, 113, 163, 255)"
        self.SecondTitleColor = "rgba(120, 162, 147, 255)"
        self.SmallTextColor = "rgba(208, 150, 60, 255)"
        self.AuthorNameColor = "rgba(208, 150, 60, 255)" 
        self.Tags = ["man","woman","couple","outside","straight","busty",
                     "breasts","tits","cleavage","island","tropical",
                     "slut","teen","fantasy","prince","lord","boss",
                     "latina","asian","hawaiian","vacation",]
        self.Disabled = False

class BGProfileCowboyIndian(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "cowboy_indian",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(247, 147, 135, 255)"
        self.SecondTitleColor = "rgba(156, 79, 153, 255)"
        self.SmallTextColor = "rgba(36, 57, 117, 255)"
        self.AuthorNameColor = "rgba(36, 57, 117, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "minority","indian","cowboy","older man",
                     "soldier","blonde","historic","princess",
                     "horse","sunset","busty","legs","leggy"]
        self.Disabled = False

class BGProfileHorseRiders(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "horse_riders",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(212, 94, 36, 255)"
        self.SecondTitleColor = "rgba(220, 64, 52, 255)"
        self.SmallTextColor = "rgba(160, 80, 143, 255)"
        self.AuthorNameColor = "rgba(128, 176, 224, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "cowboy","cowgirl","bandit","sheriff",
                     "country",]
        self.Disabled = False

class BGProfileShowSomeLeg(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "show_some_leg",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(64, 85, 27, 255)"
        self.SecondTitleColor = "rgba(113, 42, 43, 255)"
        self.SmallTextColor = "rgba(208, 150, 60, 255)"
        self.AuthorNameColor = "rgba(208, 150, 60, 255)"
        self.Tags = ["man","woman","couple","outside","straight","lord",
                     "boss","legs","leggy","cleavage","brunette",
                     "muscular","shirtless","jock","duke","prince",
                     "business","wealthy","millionaire","billionaire",
                     "park","bachelor",]
        self.Disabled = False

class BGProfileLesbians(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "lesbians",
                         Orient = OLES,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(195, 100, 72, 255)"
        self.SecondTitleColor = "rgba(47, 104, 117, 255)"
        self.SmallTextColor = "rgba(218, 149, 162, 255)"
        self.AuthorNameColor = "rgba(195, 100, 72, 255)"
        self.Tags = ["woman","women","inside","lesbian","bed","smoking",
                     "cigarette","blonde","brunette","pillow","lingerie",
                     "nightgown","teen","waitress","threesome",]
        self.Disabled = False

#class BGProfileRedDressParty(BGProfile):
#    def __init__(self):
#        super().__init__(Priority = 4,
#                           sFileName = "red_dress_party")
#        self.MainTitleColor = "rgba(191, 41, 32, 255)"
#        self.SecondTitleColor = "rgba(88, 118, 85, 255)"
#        self.SmallTextColor = "rgba(124, 50, 19, 255)"
#        self.AuthorNameColor = "rgba(234, 182, 73, 255)"
#        self.Tags = ["man","woman","straight"]
#        self.Disabled = False

class BGProfileLesbianTemptation(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "lesbian_temptation",
                         Orient = OLES,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(191, 57, 32, 255)"
        self.SecondTitleColor = "rgba(229, 170, 3, 255)"
        self.SmallTextColor = "rgba(153, 102, 153, 255)"
        self.AuthorNameColor = "rgba(191, 57, 32, 255)"
        self.Tags = ["woman","women","inside","lesbian","bed","blonde",
                     "brunette","underwear","nightgown","topless",
                     "lady","teen",]
        self.Disabled = False

class BGProfileRedBedCutie(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "red_bed_cutie",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(188, 9, 2, 255)"
        self.SecondTitleColor = "rgba(188, 9, 2, 255)"
        self.SmallTextColor = "rgba(153, 102, 153, 255)"
        self.Tags = ["woman","single","inside","brunette","bed","young","teen",
                     "slender","legs","leggy","college","co-ed","daughter",
                     "sister","wife","lingerie","bra","secretary","innocent",
                     "starlet",]
        self.Disabled = False

class BGProfilePinkShower(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "pink_shower",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(205, 79, 107, 255)"
        self.SecondTitleColor = "rgba(241, 166, 150, 255)"
        self.SmallTextColor = "rgba(158, 162, 225, 255)"
        self.AuthorNameColor = "rgba(136, 67, 107, 255)"
        self.Tags = ["woman","single","inside","nude","naked",
                     "bathroom","shower","phone","brunette",
                     "milf","mom","bath","wet","leggy","legs",
                     ]
        self.Disabled = False

#class BGProfileGolf(BGProfile):
#    def __init__(self):
#        super().__init__(Priority = 4,
#                           sFileName = "golf")
#        self.MainTitleColor = "rgba(91, 160, 201, 255)"
#        self.SecondTitleColor = "rgba(77, 179, 117, 255)"
#        self.SmallTextColor = "rgba(157, 68, 148, 255)"
#        self.AuthorNameColor = "rgba(77, 179, 117, 255)"
#        self.Tags = ["man","woman","men","women","outside","voyeur"]
#        self.Disabled = False

class BGProfileFlowers(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "flowers",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(198, 77, 94, 255)"
        self.SecondTitleColor = "rgba(228, 156, 82, 255)"
        self.SmallTextColor = "rgba(186, 113, 189, 255)"
        self.AuthorNameColor = "rgba(71, 116, 56, 255)"
        self.Tags = ["man","woman","couple","straight",
                     "boss","CEO","secretary",
                     "wealthy","millionaire",
                     "billionaire","lady","bachelor",]
        self.Disabled = False

class BGProfileHelloSailor(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "hello_sailor",
                         Orient = OGAY,
                         Group = GSING)
        self.MainTitleColor = "rgba(82, 126, 183, 255)"
        self.SecondTitleColor = "rgba(82, 126, 183, 255)"
        self.SmallTextColor = "rgba(202, 179, 194, 255)"
        self.AuthorNameColor = "rgba(194, 82, 31, 255)"
        self.Tags = ["man","single","shirtless","muscular","outdoors","sailor",
                     "bronzed",]
        self.Disabled = False

class BGProfileLatinoCowboy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "latino_cowboy",
                         Orient = OGAY,
                         Group = GSING)
        self.MainTitleColor = "rgba(138, 19, 20, 255)"
        self.SecondTitleColor = "rgba(147, 115, 73, 255)"
        self.SmallTextColor = "rgba(164, 91, 56, 255)"
        self.AuthorNameColor = "rgba(164, 91, 56, 255)"
        self.Tags = ["man","single","cowboy","shirtless","muscular","gay",
                     "minority","latino","jeans","horse","dark skinned",
                     "queen",]
        self.Disabled = False

#class BGProfileDemiGod(BGProfile):
#    def __init__(self):
#        super().__init__(Priority = 4,
#                           sFileName = "demi_god")
#        self.MainTitleColor = "rgba(208, 66, 32, 255)"
#        self.SecondTitleColor = "rgba(45, 75, 63, 255)"
#        self.SmallTextColor =  "rgba(147, 115, 73, 255)"
#        self.AuthorNameColor = "rgba(45, 75, 63, 255)"
#        self.Tags = ["man","single"]
#        self.Disabled = False

class BGProfileNudeSailorButt(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "nude_sailor_butt",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(45, 84, 112, 255)"
        self.SecondTitleColor = "rgba(206, 77, 87, 255)"
        self.AuthorNameColor = "rgba(45, 84, 112, 255)"
        self.Tags = ["man","men","gay","inside","sailor","bed","drinking",
                     "butt","ass","smoking","tattooed","hat",]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileOceanHorse(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "ocean_horse",
                         Orient = OGAY,
                         Group = GSING)
        self.MainTitleColor = "rgba(232, 191, 72, 255)"
        self.SecondTitleColor = "rgba(232, 191, 72, 255)"
        self.SmallTextColor =  "rgba(152, 102, 58, 255)" 
        self.AuthorNameColor = "rgba(105, 154, 170, 255)"
        self.Tags = ["man","single","outside","horse","nude","naked",
                     "muscular","shirtless","latino","hispanic",
                     "asian","rangy","cowboy","fantasy",]
        self.Disabled = False

#class BGProfileCaveCouple(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 91,
#                           Priority = 4,
#                           sFileName = "cave_couple")
#        self.MainTitleColor = "rgba(82, 126, 183, 255)"
#        self.SecondTitleColor = "rgba(11, 115, 24, 255)"
#        self.SmallTextColor =  "rgba(192, 111, 21, 255)" 
#        self.AuthorNameColor = "rgba(11, 115, 24, 255)"
#        self.Tags = ["man","woman","straight","couple","outside","caveman"]
#        self.Disabled = False

class BGProfileRedSatinSheets(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "red_satin_sheets",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(134, 15, 55, 255)"
        self.SecondTitleColor = "rgba(6, 108, 17, 255)"
        self.AuthorNameColor = "rgba(134, 15, 55, 255)"
        self.Tags = ["man","woman","straight","couple","inside","bed",
                     "blonde","nightgown","lingerie","shirtless",
                     "muscular","seduce",]
        self.Disabled = False

class BGProfileFabioHero(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "fabio_hero",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(24, 99, 209, 255)"
        self.SecondTitleColor = "rgba(87, 87, 89, 255)"
        self.SmallTextColor = "rgba(125, 47, 30, 255)"
        self.AuthorNameColor = "rgba(87, 87, 89, 255)"
        self.Tags = ["man","outside","fantasy","fabio","single",
                     "vest","sword","warrior","knight",
                     "historic","bulge","giant","large",
                     ]
        self.Disabled = False

class BGProfileBigCity(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "big_city",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(204, 40, 29, 255)"
        self.SecondTitleColor = "rgba(25, 51, 107, 255)"
        self.Tags = ["man","woman","outside","city","couple","straight",
                     "blonde","pink","stars","night","wealthy","suit",
                     "bowtie","wife","husband",]
        self.Disabled = False

class BGProfileInterracial(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "interracial",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(228, 113, 164, 255)"
        self.SecondTitleColor = "rgba(228, 113, 164, 255)"
        self.SmallTextColor = "rgba(71, 136, 200, 255)"
        self.AuthorNameColor = "rgba(71, 136, 200, 255)"
        self.Tags = ["man","woman","straight","modern","minority","bbc",
                     "slut","nude","naked","undressing","stripping",
                     "exposed","stripped","tits","breasts","ass","butt",
                     "wife","teen","blonde","co-ed","panties","horny",
                     "black","porn",
                     ]
        self.Content = Content.AdultsOnly
        self.Disabled = False

class BGProfileRedCape(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "red_cape",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(208, 51, 4, 255)"
        self.SecondTitleColor = "rgba(174, 111, 165, 255)"
        self.SmallTextColor = "rgba(18, 18, 23, 255)"
        self.AuthorNameColor = "rgba(208, 51, 4, 255)"
        self.Tags = ["woman","blonde","single","teen","busty",
                     "dress","cape","leggy","legs","slender",
                     "prom","breasts","tits","wife","succubus",
                     "slut",]
        self.Disabled = False

class BGProfileValleyLake(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "valley_lake",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(202, 141, 138, 255)"
        self.SecondTitleColor = "rgba(71, 168, 169, 255)"
        self.SmallTextColor = "rgba(71, 168, 169, 255)"
        self.AuthorNameColor = "rgba(202, 141, 138, 255)"
        self.Tags = ["woman","man","couple","straight","fantasy","outside",
                     "knight","warrior","hero","jock","dad","father","teen",
                     "daughter","prince","princess","king","duke","baron",
                     "lord","lady","undress","gown","pink gown","leg",
                     "slender","wind","mountain","lake","shirtless","wife",
                     "husband",]
        self.Disabled = False

class BGProfileIslandUndressing(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "island_undressing",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(170, 8, 4, 255)"
        self.SecondTitleColor = "rgba(170, 8, 4, 255)"
        self.SmallTextColor = "rgba(93, 108, 19, 255)"
        self.AuthorNameColor = "rgba(93, 108, 19, 255)"
        self.Tags = ["woman","outside","undressing","naked","nude",
                     "single","brunette","redhead","strip",
                     "bird","tropical","busty","leg",
                     "slender","teen","strip","virgin",
                     "college","irish","scotch","voyeur",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfilePinUp(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "pin_up",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(232, 36, 23, 255)"
        self.SecondTitleColor = "rgba(232, 36, 23, 255)"
        self.SmallTextColor = "rgba(89, 186, 160, 255)"
        self.AuthorNameColor = "rgba(239, 104, 123, 255)"
        self.Tags = ["woman","blonde","single","flower","stockings",
                     "heels","secretary","butt","ass","stripper",
                     "teen","irish","horny",]
        self.Disabled = False

class BGProfileWindowVoyeur(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "window_voyeur",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(195, 63, 47, 255)"
        self.SecondTitleColor = "rgba(25, 117, 164, 255)"
        self.SmallTextColor = "rgba(54, 132, 122, 255)"
        self.AuthorNameColor = "rgba(25, 117, 164, 255)"
        self.Tags = ["woman","man","undress","kinky","blonde",
                     "single","straight","strip","voyeur",
                     "daughter","watch","spy","window",
                     "busty","teacher","skirt","night","gun",
                     ]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileInterracialThreesome(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "interracial_threesome",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(57, 187, 210, 255)"
        self.SecondTitleColor = "rgba(201, 16, 113, 255)"
        self.SmallTextColor = "rgba(52, 49, 98, 255)"
        self.AuthorNameColor = "rgba(52, 49, 98, 255)"
        self.Tags = ["woman","man","men","naked","indoors","kinky",
                     "bed","femdom","unzipped","mistress","porn",
                     "call girl","black","tits","ass","afro",
                     "teacher","voyeur","wife","college",
                     "muscular",]
        self.Content = Content.AdultsOnly
        self.Disabled = False

class BGProfileDrMcChesty(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "dr_mc_chesty",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(76, 136, 175, 255)"
        self.SecondTitleColor = "rgba(223, 150, 89, 255)"
        self.SmallTextColor = "rgba(155, 70, 159, 255)"
        self.AuthorNameColor = "rgba(223, 150, 89, 255)"
        self.Tags = ["woman","man","straight","couple","indoors",
                     "shirtless","window","teacher","doctor",
                     "boss",]
        self.Disabled = False

class BGProfileBadDoctor(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "bad_doctor",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(217, 80, 66, 255)"
        self.SecondTitleColor = "rgba(217, 80, 66, 255)"
        self.SmallTextColor = "rgba(122, 120, 44, 255)"
        self.AuthorNameColor = "rgba(122, 120, 44, 255)"
        self.Tags = ["woman","man","straight","indoors","redhead",
                     "doctor",]
        self.Disabled = False

class BGProfileAutumnHeadband(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "autumn_headband",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(233, 140, 2, 255)"
        self.SecondTitleColor = "rgba(125, 99, 3, 255)"
        self.SmallTextColor = "rgba(139, 106, 69, 255)"
        self.AuthorNameColor = "rgba(125, 99, 3, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors","fall","october",
                     "redhead","athletic","fit","gym coach","trees","park",
                     "yoga","sporty","large","giant",]
        self.Disabled = False

class BGProfileIndianPrincess(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "indian_princess",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(218, 124, 1, 255)"
        self.SecondTitleColor = "rgba(148, 39, 20, 255)"
        self.SmallTextColor = "rgba(55, 74, 121, 255)"
        self.AuthorNameColor = "rgba(148, 39, 20, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors",
                     "brunette","indian"]
        self.Disabled = False

class BGProfileOrangeFromBehind(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "orange_from_behind",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(243, 108, 1, 255)"
        self.SecondTitleColor = "rgba(119, 141, 38, 255)"
        self.SmallTextColor = "rgba(154, 91, 163, 255)"
        self.AuthorNameColor = "rgba(154, 91, 163, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors",
                     "fall","october","mountains","fantasy",
                     "bent over","leggy","legs","dad","boss",
                     "grass","meadow","lady","lord",
                     ]
        self.Disabled = False

class BGProfileCabinFever(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "cabin_fever",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(171, 0, 34, 255)"
        self.SecondTitleColor = "rgba(171, 0, 34, 255)"
        self.SmallTextColor = "rgba(48, 89, 135, 255)"
        self.AuthorNameColor = "rgba(48, 89, 135, 255)"
        self.Tags = ["woman","man","straight","couple","indoors",
                     "blonde","cabin","night","gentleman",
                     "wealthy","busty","older man","dad","dilf",
                     "businessman","undressing","bachelor","wife",
                     "swedish",]
        self.Disabled = False

class BGProfileCensorEagle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "censor_eagle",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(233, 109, 51, 255)"
        self.SecondTitleColor = "rgba(233, 109, 51, 255)"
        self.SmallTextColor = "rgba(105, 168, 213, 255)"
        self.AuthorNameColor = "rgba(105, 168, 213, 255)"
        self.Tags = ["man","outdoors","ocean","nude","naked",
                     "shirtless","muscular","single","gay",
                     "eagle","bird","penis",]
        self.Disabled = False

class BGProfileLesbianKiss(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "lesbian_kiss",
                         Orient = OLES,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(210, 161, 51, 255)"
        self.SecondTitleColor = "rgba(210, 161, 51, 255)"
        self.SmallTextColor = "rgba(181, 57, 41, 255)"
        self.AuthorNameColor = "rgba(181, 57, 41, 255)"
        self.Tags = ["woman","women","lesbian","indoors","couple","bed",
                     "kiss","nude","naked","blonde","brunette","sex",
                     ]
        self.Disabled = False

class BGProfileLesboThreesome(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "lesbo_threesome",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(92, 142, 142, 255)"
        self.SecondTitleColor = "rgba(92, 142, 142, 255)"
        self.SmallTextColor = "rgba(207, 105, 61, 255)"
        self.AuthorNameColor = "rgba(207, 161, 98, 255)"
        self.Tags = ["woman","women","lesbian","indoors","bed","shower",
                     "nude","towel","brunette","blonde","redhead",
                     "busty","tits","cleavage","stockings","nightgown",
                     "lingerie","teen","older woman","mature","cougar",
                     "secretary","whore","slut",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileSharingBed(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "sharing_bed",
                         Orient = OLES,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(198, 74, 53, 255)"
        self.SecondTitleColor = "rgba(84, 135, 137, 255)"
        self.SmallTextColor = "rgba(101, 67, 102, 255)"
        self.AuthorNameColor = "rgba(101, 67, 102, 255)"
        self.Tags = ["woman","women","lesbian","indoors","bed","busty"
                     "breasts","tits","brunette","redhead","nightgown",
                     "undress","strip","sister","innocent","secretary",
                     ]
        self.Disabled = False

class BGProfileHotLasso(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "hot_lasso",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(198, 68, 42, 255)"
        self.SecondTitleColor = "rgba(52, 162, 137, 255)"
        self.SmallTextColor = "rgba(120, 115, 147, 255)"
        self.AuthorNameColor = "rgba(120, 115, 147, 255)"
        self.Tags = ["man","outdoors","cowboy","single","bulge","blue jeans",
                     "american","country","muscular","shirtless","lasso",
                     "hairy","tall",]
        self.Disabled = False

class BGProfileThirdMan(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "third_man",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(150, 45, 23, 255)"
        self.SecondTitleColor = "rgba(32, 104, 43, 255)"
        self.AuthorNameColor = "rgba(150, 45, 23, 255)"
        self.Tags = ["man","men", "woman", "indoors", "bed","kinky","voyeur",
                     "threesome","wife","business","secretary","CEO","hotel",
                     "mistress","undress","brunette","redhead","shirtless",
                     "kidnap","captive","in the bed","whore","slut","suit",
                     "secretary","cuckold","pillow","slender","leg","jock",
                     "bachelor","teacher","surprise","scotch","irish",]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileFileCabinet(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "file_cabinet",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(236, 53, 36, 255)"
        self.SecondTitleColor = "rgba(221, 97, 99, 255)"
        self.SmallTextColor = "rgba(2, 117, 71, 255)"
        self.AuthorNameColor = "rgba(133, 123, 32, 255)"
        self.Tags = ["woman","indoors","blonde","single","bra",
                     "secretary","office","file cabinet",]
        self.Disabled = False

class BGProfileWindowCreeper(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "window_creeper",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(219, 49, 26, 255)"
        self.SecondTitleColor = "rgba(232, 174, 36, 255)"
        self.SmallTextColor = "rgba(8, 70, 131, 255)"
        self.AuthorNameColor = "rgba(3, 71, 15, 255)"
        self.Tags = ["woman","indoors","bed","voyeur","blonde",
                     "single","october","straight","horror",
                     "killer","stalker","cleavage","red nightgown",
                     "nightgown","lingerie","window","watch",
                     "book","teen","young","wife","daughter",
                     "busty","perv","creeper","surprise",]
        self.Disabled = False

class BGProfileLesboFriend(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "lesbo_friend",
                         Orient = OLES,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(170, 43, 40, 255)"
        self.SecondTitleColor = "rgba(94, 146, 95, 255)"
        self.SmallTextColor = "rgba(85, 120, 154, 255)"
        self.AuthorNameColor = "rgba(85, 120, 154, 255)"
        self.Tags = ["woman","women","lesbian","indoors","blonde",
                     "brunette","teen","student","daughter",
                     "young","sweater","library","librarian",
                     "book","school-girl",]
        self.Disabled = False

class BGProfileNaughtyBarn(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "naughty_barn",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(249, 49, 37, 255)"
        self.SecondTitleColor = "rgba(204, 145, 88, 255)"
        self.SmallTextColor = "rgba(71, 106, 116, 255)"
        self.AuthorNameColor = "rgba(71, 106, 116, 255)"
        self.Tags = ["woman","man","straight","blonde","barn","couple","hay",
                     "country","dress","dad","father","teen","legs","leggy",
                     "kidnap","surprise","co-ed","farmer","older man",
                     "CEO","young","prom queen","wife","husband",]
        self.Disabled = False

class BGProfileBulgingCodpieces(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "bulging_codpieces",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(142, 22, 25, 255)"
        self.SecondTitleColor = "rgba(194, 102, 52, 255)"
        self.SmallTextColor = "rgba(143, 138, 40, 255)"
        self.AuthorNameColor = "rgba(194, 102, 52, 255)"
        self.Tags = ["men","man","muscular","fantasy","outdoors","shirtless",
                     "codpiece","warrior","black","minority","strong",
                     "thong","barbarian","rock","threesome","gym","giant",
                     "large",]
        self.Disabled = False

class BGProfileLesboBoudoir(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "lesbo_boudoir",
                         Orient = OLES,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(216, 107, 111, 255)"
        self.SecondTitleColor = "rgba(110, 173, 69, 255)"
        self.SmallTextColor = "rgba(126, 63, 100, 255)"
        self.AuthorNameColor = "rgba(110, 173, 69, 255)"
        self.Tags = ["woman","women","blonde","brunette",
                     "lesbian","nightgown","lingerie","seduced",
                     "sister",]
        self.Disabled = False

class BGProfileOctoAttack(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "octo_attack",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(223, 112, 77, 255)"
        self.SecondTitleColor = "rgba(71, 109, 63, 255)"
        self.SmallTextColor = "rgba(44, 117, 179, 255)"
        self.AuthorNameColor = "rgba(44, 117, 179, 255)"
        self.Tags = ["woman","outdoors","underwater","bikini","blonde",
                     "octopus","tentacles","milf","swimming","wet",
                     "whore",
                     ]
        self.Disabled = False

class BGProfileNurseTriangle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "nurse_triangle",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(93, 133, 72, 255)"
        self.SecondTitleColor = "rgba(93, 133, 72, 255)"
        self.SmallTextColor = "rgba(139, 64, 56, 255)"
        self.AuthorNameColor = "rgba(198, 77, 44, 255)"
        self.Tags = ["woman","man","couple","nurse","redhead",
                     "indoors","hospital","suit","straight",
                     "doctor","businessman","older man",
                     "dad","father","wealthy","cuckolded",
                     "hotwife","wife","millionaire",
                     "billionaire","tits",]
        self.Disabled = False

class BGProfileNurseTriangleMFF(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "nurse_triangle_mff",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(217, 67, 22, 255)"
        self.SecondTitleColor = "rgba(70, 128, 129, 255)"
        self.SmallTextColor = "rgba(22, 73, 97, 255)"
        self.AuthorNameColor = "rgba(22, 73, 97, 255)"
        self.Tags = ["woman","man","couple","nurse","blonde",
                     "indoors","hospital","doctor","straight",
                     "threesome","blonde","brunette","young",
                     "co-ed","mom","slut","horny","undressed",
                     "stripped",]
        self.Disabled = False

class BGProfileBoatBoys(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "boat_boys",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(139, 183, 218, 255)"
        self.SecondTitleColor = "rgba(202, 49, 27, 255)"
        self.SmallTextColor = "rgba(106, 55, 39, 255)"
        self.AuthorNameColor = "rgba(106, 55, 39, 255)"
        self.Tags = ["man","men","shirtless","muscular",
                     "outdoors","ocean","boat","threesome"]
        self.Disabled = False

class BGProfileLoveCanoe(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "love_canoe",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(214, 66, 31, 255)"
        self.SecondTitleColor = "rgba(86, 124, 29, 255)"
        self.SmallTextColor = "rgba(59, 12, 109, 255)"
        self.AuthorNameColor = "rgba(59, 12, 109, 255)"
        self.Tags = ["woman","man","outdoors","boat","straight",
                     "couple","cowboy","brunette","river",
                     "night","latina","minority","dad",
                     "brother",]
        self.Disabled = False

class BGProfileBarbarianBulge(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "barbarian_bulge",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(31, 78, 143, 255)"
        self.SecondTitleColor = "rgba(199, 95, 52, 255)"
        self.SmallTextColor = "rgba(65, 88, 55, 255)"
        self.AuthorNameColor = "rgba(65, 88, 55, 255)"
        self.Tags = ["man","single","fantasy","barbarian","sword",
                     "muscular","shirtless","warrior","well-hung",
                     "thong","abs","giant","large",]
        self.Disabled = False

class BGProfileStartledBedMan(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "startled_bed_man",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(231, 81, 111, 255)"
        self.SecondTitleColor = "rgba(30, 134, 80, 255)"
        self.SmallTextColor = "rgba(107, 50, 65, 255)"
        self.AuthorNameColor = "rgba(231, 81, 111, 255)"
        self.Tags = ["man" ,"single","indoors","bed","horror",
                     "muscular","shirtless","scared","femdom",
                     "surprised","dad","father",]
        self.Disabled = False

class BGProfileAgainstATree(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "against_a_tree",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(212, 105, 41, 255)"
        self.SecondTitleColor = "rgba(71, 139, 64, 255)"
        self.SmallTextColor = "rgba(101, 20, 81, 255)"
        self.AuthorNameColor = "rgba(101, 20, 81, 255)"
        self.Tags = ["woman","man","outdoors","tree","straight",
                     "couple","shirtless","muscular","blonde",
                     "medieval","blonde","forest","wood",
                     "busty","fantasy","legs","leggy"]
        self.Disabled = False

class BGProfileMermaidPirateStorm(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "mermaid_pirate_storm",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(237, 89, 53, 255)"
        self.SecondTitleColor = "rgba(25, 162, 36, 255)"
        self.SmallTextColor = "rgba(139, 55, 30, 255)"
        self.AuthorNameColor = "rgba(78, 120, 171, 255)"
        self.Tags = ["woman","man","outdoors","straight","blonde",
                     "couple","topless","mermaid","ship","boat",
                     "pirate","ocean","storm","busty","tits",
                     "bird","fantasy","hat","waves","lightning",
                     "topless",
                     ]
        self.Disabled = False

class BGProfileSkiSweaters(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "ski_sweaters",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(180, 21, 43, 255)"
        self.SecondTitleColor = "rgba(117, 74, 120, 255)"
        self.SmallTextColor = "rgba(4, 106, 103, 255)"
        self.AuthorNameColor = "rgba(180, 21, 43, 255)"
        self.Tags = ["woman","man","outdoors","straight","blonde",
                     "sweater","teen","nerd","co-ed","college",
                     "blue jeans","brother","sister",
                     "babysitter","snow","winter","day","ski",
                     "nerd","athletic","wealthy","gentleman",
                     "sporty",]
        self.Disabled = False

class BGProfileBigPole(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "big_pole",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(70, 174, 210, 255)"
        self.SecondTitleColor = "rgba(225, 144, 118, 255)"
        self.SmallTextColor = "rgba(125, 96, 78, 255)"
        self.AuthorNameColor = "rgba(70, 174, 210, 255)"
        self.Tags = ["man","men","gay","penis","naked",
                     "shirtless","muscular","bed","sleep",
                     "roommate","erect","masturbate",
                     "boys","pillow",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileBadNun(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "bad_nun",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(173, 13, 19, 255)"
        self.SecondTitleColor = "rgba(111, 154, 187, 255)"
        self.SmallTextColor = "rgba(91, 38, 6, 255)"
        self.AuthorNameColor = "rgba(91, 38, 6, 255)"
        self.Tags = ["woman","smoking","nun","single","stockings",
                     "Christian","Catholic","underwear","church",
                     "porn star",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileSkinnyDipping(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "skinny_dipping",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(173, 51, 15, 255)"
        self.SecondTitleColor = "rgba(207, 123, 9, 255)"
        self.SmallTextColor = "rgba(43, 99, 102, 255)"
        self.AuthorNameColor = "rgba(43, 99, 102, 255)"
        self.Tags = ["woman","single","nude","naked","ass","outside","night",
                     "blonde","butt","skinny dip","wet","ocean","water",
                     "beach","breasts","tits","teen","college","co-ed",
                     "young","innocent","curvy","strip","undress","expose",
                     "swim","mermaid",
                     ]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileCopsInLove(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "cops_in_love",
                         Orient = OGAY,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(218, 79, 158, 255)"
        self.SecondTitleColor = "rgba(85, 138, 205, 255)"
        self.SmallTextColor = "rgba(113, 59, 36, 255)"
        self.AuthorNameColor = "rgba(199, 171, 57, 255)"
        self.Tags = ["men","cops","police","indoors","gay","bed",
                     "undressing",]
        self.Disabled = False

class BGProfileBondageMattress(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "bondage_mattress",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(223, 60, 38, 255)"
        self.SecondTitleColor = "rgba(224, 153, 17, 255)"
        self.SmallTextColor = "rgba(140, 93, 137, 255)"
        self.AuthorNameColor = "rgba(140, 93, 137, 255)"
        self.Tags = ["woman","women","man","indoors","bondage","kinky",
                     "maledom","bound","belt","whip","busty","legs",
                     "leggy","mattress","rope","tied up","redhead",
                     "blonde","milf","mature","cougar","tits",
                     "breasts","broken","discipline","punish",
                     "gentleman","wealthy","millionaire","billionaire",
                     "boss","older man","porn star",]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileUpsideDownWhip(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "upside_down_whip",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(237, 47, 86, 255)"
        self.SecondTitleColor = "rgba(224, 153, 17, 255)"
        self.SmallTextColor = "rgba(168, 93, 158, 255)"
        self.AuthorNameColor = "rgba(168, 93, 158, 255)"
        self.Tags = ["woman","women","indoors","bondage","kinky","naked",
                     "nude","tits","whip","lesbian","femdom","strip",
                     "expose","bound","tied up","punish","discipline",
                     "dominatrix","brunette","redhead","busty","tits",
                     "breasts","bdsm","upside-down","butt","ass",
                     "historic","fantasy","lady","secretary","flexible",
                     "older woman","mature","mom","mother","daughter",]
        self.Content = Content.AdultsOnly
        self.Disabled = False

class BGProfileSprayed(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "sprayed",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(229, 105, 86, 255)"
        self.SecondTitleColor = "rgba(86, 123, 140, 255)"
        self.SmallTextColor = "rgba(142, 66, 167, 255)"
        self.AuthorNameColor = "rgba(115, 161, 154, 255)"
        self.Tags = ["woman","single","outdoors","wet","blonde","facial",
                     "spray","wife","bukkake","cum","college","co-ed",
                     "pretty","dress",]
        self.Disabled = False

class BGProfileGayArmy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "gay_army",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(58, 134, 208, 255)"
        self.SecondTitleColor = "rgba(229, 154, 51, 255)"
        self.AuthorNameColor = "rgba(58, 134, 208, 255)"
        self.Tags = ["gay","man","men","army","water","shirtless","naked",
                     "nude","jungle","outdoors","towel"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileChainedToTheBed(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "cuffed_to_the_bed",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(217, 43, 38, 255)"
        self.SecondTitleColor = "rgba(214, 154, 40, 255)"
        self.Tags = ["man","woman","bed","naked","straight","kinky","nude",
                     "femdom","bound","bondage","blonde","bondage","cuffs",
                     "handcuffed",]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileCivilWarHorse(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "civil_war_horse",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(117, 176, 195, 255)"
        self.SecondTitleColor = "rgba(220, 100, 81, 255)"
        self.SmallTextColor = "rgba(166, 80, 175, 255)"
        self.AuthorNameColor = "rgba(117, 176, 195, 255)"
        self.Tags = ["man","woman","shirtless","outside","historical","horse",
                     "straight","couple","blonde","sunset","warrior",
                     "soldier","army","undressing","legs","leggy","slender",
                     "field",]
        self.Disabled = False

class BGProfileShirtlessSpaceman(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "shirtless_spaceman",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(217, 8, 7, 255)"
        self.SecondTitleColor = "rgba(217, 8, 7, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(114, 144, 90, 255)"
        self.Tags = ["man","single","shirtless","outside","scifi","space",
                     "femdom","sub","future","bondage","dad","older man",
                     "cuff","chain","father","alien","asteroid",
                     "spaceship",]
        self.Disabled = False

class BGProfileGorillaVoyeur(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "gorilla_voyeur",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(206, 62, 45, 255)"
        self.SecondTitleColor = "rgba(232, 144, 146, 255)"
        self.SmallTextColor = "rgba(43, 58, 32, 255)"
        self.AuthorNameColor = "rgba(43, 58, 32, 255)"
        self.Tags = ["man","woman","couple","gorilla","inside",
                     "blonde","voyeur","kinky","straight",
                     "young","businessman","chair","monkey",
                     "voyeur",]
        self.Disabled = False

class BGProfileWaterfallKnife(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "waterfall_knife",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(214, 47, 37, 255)"
        self.SecondTitleColor = "rgba(53, 103, 83, 255)"
        self.SmallTextColor = "rgba(133, 70, 48, 255)"
        self.AuthorNameColor = "rgba(133, 70, 48, 255)"
        self.Tags = ["man","woman","couple","outside","blonde","straight",
                     "waterfall","shirtless","knife", "nature","busty",
                     "cleavage","warrior","indian","caveman","barbarian",
                     "loincloth","white dress","white gown","gown",
                     "lady","fantasy","muscular","river","wet","leg",
                     "latino","bronzed","tan","pale",]
        self.Disabled = False

class BGProfilePantyPerv(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "panty_perv",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(76, 180, 179, 255)"
        self.SecondTitleColor = "rgba(154, 143, 194, 255)"
        self.SmallTextColor = "rgba(76, 57, 50, 255)"
        self.AuthorNameColor = "rgba(76, 57, 50, 255)"
        self.Tags = ["man","woman","inside","bikini","bed"
                     "panties","underwear","kinky","straight",
                     "older man","sleep","underwear","lingerie",
                     "dad","father","teen","old man",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileAstroBabes(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "astrobabes",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(204, 65, 63, 255)"
        self.SecondTitleColor = "rgba(77, 74, 156, 255)"
        self.SmallTextColor = "rgba(8, 54, 98, 255)"
        self.AuthorNameColor = "rgba(28, 115, 56, 255)"
        self.Tags = ["woman","women","outside","redhead","brunette"
                     "space","spaceship","alien","ass","future","scifi",
                     "butt","busty","bent over","ladder","helmet",
                     "computer",]
        self.Disabled = False

class BGProfileCowgirlPanties(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "cowgirl_panties",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(222, 78, 18, 255)"
        self.SecondTitleColor = "rgba(177, 118, 51, 255)"
        self.SmallTextColor = "rgba(29, 104, 198, 255)"
        self.AuthorNameColor = "rgba(68, 158, 227, 255)"
        self.Tags = ["woman","outside","brunette","horse","cowgirl",
                     "panties","western","pinup","single","historic",
                     "busty","boobs","tits","country","american",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileGingerDiver(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "ginger_diver",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(183, 42, 3, 255)"
        self.SecondTitleColor = "rgba(192, 65, 5, 255)"
        self.SmallTextColor = "rgba(36, 65, 30, 255)"
        self.AuthorNameColor = "rgba(14, 81, 164, 255)"
        self.Tags = ["woman","outside","redhead","underwater","bikini",
                     "diving","single","pinup","swimsuit","swimming",
                     "fish","busty","tits","breasts","ass","butt",
                     "mermaid","scotch","irish",]
        self.Disabled = False

class BGProfilePublicBedroom(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "public_bedroom",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(208, 68, 86, 255)"
        self.SecondTitleColor = "rgba(207, 179, 52, 255)"
        self.SmallTextColor = "rgba(78, 92, 72, 255)"
        self.AuthorNameColor = "rgba(78, 92, 72, 255)"
        self.Tags = ["man","woman","blonde","inside","bedroom",
                     "voyeur","couple","sex","hardcore","audience",
                     "kinky","straight","exposed","exhibit",
                     "orgy","brother","sister","mom","mother",
                     "milf","cougar","older woman","bed","naked",
                     "nude","suit",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileBoobGrab(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "boob_grab",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(186, 16, 23, 255)"
        self.SecondTitleColor = "rgba(88, 145, 126, 255)"
        self.SmallTextColor = "rgba(93, 43, 64, 255)"
        self.AuthorNameColor = "rgba(93, 43, 64, 255)"
        self.Tags = ["man","woman","brunette","outside","couple",
                     "beach","windy","straight","older man",]
        self.Disabled = False

class BGProfilePurpleBarechested(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "purple_barechested",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(255, 55, 127, 255)"
        self.SecondTitleColor = "rgba(146, 55, 116, 255)"
        self.SmallTextColor = "rgba(111, 41, 137, 255)"
        self.AuthorNameColor = "rgba(111, 41, 137, 255)"
        self.Tags = ["man","woman","outside","couple","shirtless",
                     "mountains","fantasy","beach","windy",
                     "straight","brunette","blonde","redhead",
                     "busty","cleavage","purple","dress",
                     "muscular","lord","duke","prince","king",
                     "lady","princess","duchess","brother",
                     "sister","day","wealthy","jock","giant",
                     "large",]
        self.Disabled = False

class BGProfileTheFrenchDoctor(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "french_doctor",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(206, 73, 60, 255)"
        self.SecondTitleColor = "rgba(58, 109, 126, 255)"
        self.SmallTextColor = "rgba(57, 94, 59, 255)"
        self.AuthorNameColor = "rgba(58, 109, 126, 255)"
        self.Tags = ["man","woman","bed","inside","doctor","blonde",
                     "straight","doctor","busty","tits","breasts",
                     "older man","dad","father","bed","nightgown",
                     "suit","seduce",]
        self.Disabled = False

class BGProfilePokerWifeBet(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "poker_wife_bet",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(126, 166, 51, 255)"
        self.SecondTitleColor = "rgba(115, 55, 60, 255)"
        self.SmallTextColor = "rgba(100, 114, 148, 255)"
        self.AuthorNameColor = "rgba(126, 166, 51, 255)"
        self.Tags = ["men","man","woman","blonde","inside","poker",
                     "maledom","kinky","bondage","smoking","bald",
                     "modern","straight","wife","hotwife",
                     "whiskey","drinking","bet","gambling",
                     "bound","rope","tits","breasts","busty",
                     "panties","teen","dad","father","threesome",
                     "cards","business","businessman","boss",
                     "office","wealthy","millionaire",
                     "billionaire","stripped","exposed",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileCopTorture(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "cop_torture",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(212, 38, 34, 255)"
        self.SecondTitleColor = "rgba(71, 77, 116, 255)"
        self.SmallTextColor = "rgba(58, 37, 32, 255)"
        self.AuthorNameColor = "rgba(58, 37, 32, 255)"
        self.Tags = ["men","man","woman","women","inside","blonde",
                     "femdom","kinky","bondage","shirtless","baseball",
                     "modern","minority","brunette","baseball",
                     "underwear","gay","bbc","busty","naked",
                     "bound",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileGayMedieval(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "gay_medieval",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(188, 36, 29, 255)"
        self.SecondTitleColor = "rgba(197, 144, 52, 255)"
        self.SmallTextColor = "rgba(71, 126, 57, 255)"
        self.AuthorNameColor = "rgba(71, 126, 57, 255)"
        self.Tags = ["men","man","inside","knight","king",
                     "medieval","fantasy","gay","threesome",
                     "warrior","princess","elf","fairy",
                     "breasts","tits","nipple","crown",
                     "throne","beard","older man",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileMoonlightSkinnyDippers(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "moonlight_skinny_dippers",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(254, 43, 172, 255)"
        self.SecondTitleColor = "rgba(168, 20, 217, 255)"
        self.SmallTextColor = "rgba(13, 114, 212, 255)"
        self.AuthorNameColor = "rgba(13, 114, 212, 255)"
        self.Tags = ["man","woman","couple","straight","shirtless","water",
                     "brunette","night","moon","nude","naked","lake",
                     "teen","skinny dipping","embrace",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileGoldWater(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "gold_water",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(26, 132, 198, 255)"
        self.SecondTitleColor = "rgba(26, 132, 198, 255)"
        self.SmallTextColor = "rgba(72, 38, 14, 255)"
        self.AuthorNameColor = "rgba(72, 38, 14, 255)"
        self.Tags = ["woman","wet","naked","cherub","gold","yellow",
                     "water","urine","nude","tits","breasts","pubes",
                     "bush","full frontal","kinky","single","indoors",
                     "pissed","pee","peeing","pissing","peed","pussy",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileRobotTentacles(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "robot_tentacles",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(203, 63, 76, 255)"
        self.SecondTitleColor = "rgba(229, 119, 27, 255)"
        self.SmallTextColor = "rgba(102, 48, 40, 255)"
        self.AuthorNameColor = "rgba(102, 48, 40, 255)"
        self.Tags = ["woman","monster","robot","brunette",
                     "table","kinky","panties","tied up",
                     "maledom","topless","skirt",
                     "strip","expose","undress","surprise",
                     "legs","leggy","athletic",
                     "statuesque","kidnap","bound",
                     "rope","milf","cougar","co-ed",
                     "college","grope","tentacles",
                     "probe","space","alien",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfilePirateRomance(BGProfile):
    def __init__(self):
        super().__init__(ID = 157,
                           Priority = GenPriority.AboveAverage,
                           sFileName = "pirate_romance",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(184, 49, 38, 255)"
        self.SecondTitleColor = "rgba(46, 71, 135, 255)"
        self.SmallTextColor = "rgba(43, 33, 29, 255)"
        self.AuthorNameColor = "rgba(46, 71, 135, 255)"
        self.Tags = ["woman","man","outdoors","straight","couple","pirate","ocean","water",
                     "blonde","bird","ship","boat","fantasy","muscles","shirtless",
                     "teen","young","daughter","sword","warrior","princess","lady",
                     ]
        self.Disabled = False

class BGProfileHotdogFlirt(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "hot_dog_flirt",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(213, 60, 73, 255)"
        self.SecondTitleColor = "rgba(0, 149, 91, 255)"
        self.SmallTextColor = "rgba(6, 89, 103, 255)"
        self.AuthorNameColor = "rgba(0, 169, 165, 255)"
        self.Tags = ["woman","man","outdoors","straight","couple","modern","hotdog",
                     "blonde","food","secretary","boss","wife","businessman","teen",
                     "dad","father","brother","sis","barbecue","cookout","grill",
                     "backyard","american","tall",]
        self.Disabled = False

class BGProfileFantasy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "fantasy",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(238, 47, 43, 255)"
        self.SecondTitleColor = "rgba(170, 47, 84, 255)"
        self.SmallTextColor = "rgba(14, 10, 23, 255)"
        self.AuthorNameColor = "rgba(170, 47, 84, 255)"
        self.Tags = ["woman","man","outdoors","straight",
                     "couple","fantasy","women","warrior",
                     "brunette","shield","knight","tits",
                     "warrior","queen","princess",
                     "horse","legs","leggy","sleep",
                     "rescue","lord","lady",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileBadVampireTouch(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "bad_vampire_touch",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(186, 77, 56, 255)"
        self.SecondTitleColor = "rgba(195, 123, 58, 255)"
        self.SmallTextColor = "rgba(94, 147, 196, 255)"
        self.AuthorNameColor = "rgba(94, 147, 196, 255)"
        self.Tags = ["woman","man","indoors","straight","fantasy","vampire",
                     "tits","breasts","boobs","pussy","maledom","sleep",
                     "horror","naked","nude","sofa"]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileReadyForYou(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "ready_for_you",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(244, 87, 220, 255)"
        self.SecondTitleColor = "rgba(46, 123, 237, 255)"
        self.SmallTextColor = "rgba(117, 24, 156, 255)"
        self.AuthorNameColor = "rgba(117, 24, 156, 255)"
        self.Tags = ["woman","tits","breasts","boobs","ass","butt",
                     "panties","brunette","high heels",
                     "naked","nude","maledom","spanked","spanking",
                     "teen","paddle","panties","undress","strip",
                     "twerk","submit","submissive","heels","co-ed",
                     "daughter","young","wife","cuckold","horny",
                     "slut",
                     ]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileVampireAssCastle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "vampire_ass_castle",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(219, 62, 48, 255)"
        self.SecondTitleColor = "rgba(43, 43, 149, 255)"
        self.SmallTextColor = "rgba(287, 70, 48, 255)"
        self.AuthorNameColor = "rgba(43, 43, 149, 255)"
        self.Tags = ["woman","tits","breasts","boobs","ass",
                     "busty","blonde","vampire",
                     "naked","nude","lingerie","straight",
                     "couple","horror","castle","fantasy",
                     "outdoors","lingerie","princess",
                     "castle","pubes","bush","pussy","buns",
                     "strip","expose","undead","monster",
                     "horny","slut","lady","october",
                     "bride","widow","wife","stockings",
                     "ditzy","older man","count","duke",
                     "kidnap","maiden",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileGirlsAssWhipped(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "girls_ass_whipped",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(224, 100, 10, 255)"
        self.SecondTitleColor = "rgba(119, 44, 87, 255)"
        self.SmallTextColor = "rgba(30, 97, 173, 255)"
        self.AuthorNameColor = "rgba(119, 44, 87, 255)"
        self.Tags = ["woman","women","straight","kinky","minority","black","blonde",
                     "brunette","poc","bbc","teen","student","co-ed","medieval",
                     "whip","spanking","maledom","discipline","ass",
                     "bottomless","butt","fantasy","whipped","young",
                     "exposed","student","teacher","school-girl",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileHotFishing(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "hot_fishing",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(227, 76, 55, 255)"
        self.SecondTitleColor = "rgba(244, 116, 15, 255)"
        self.SmallTextColor = "rgba(60, 131, 115, 255)"
        self.AuthorNameColor = "rgba(244, 116, 15, 255)"
        self.Tags = ["woman","women","straight","men","bikini","underwater","fishing","boat",
                     "blonde","brunette","outdoors"]
        self.Disabled = False

class BGProfileLongFlowingHair(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "long_flowing_hair",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(250, 63, 53, 255)"
        self.SecondTitleColor = "rgba(242, 150, 77, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(59, 133, 202, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors",
                     "fantasy","shirtless","blonde","muscular",
                     "blonde","hair","slender","legs","leggy",]
        self.Disabled = False

class BGProfileWindyBeach(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "windy_beach",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(126, 45, 29, 255)"
        self.SecondTitleColor = "rgba(124, 69, 32, 255)"
        self.SmallTextColor = "rgba(20, 82, 108, 255)"
        self.AuthorNameColor = "rgba(20, 82, 108, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors","beach",
                     "sea","ocean","modern","brunette","dress","storm",
                     "busty","leg","sweater","dad","boss","secretary",]
        self.Disabled = False

class BGProfilePrinceLover(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "prince_lover",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(230, 130, 53, 255)"
        self.SecondTitleColor = "rgba(48, 155, 136, 255)"
        self.SmallTextColor = "rgba(154, 105, 90, 255)"
        self.AuthorNameColor = "rgba(230, 130, 53, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors","prince","king","brunette",
                     "castle","fantasy","lady","mistress","father","orange","wealthy",
                     "young","teen","daughter","sister","brother","furs","cloak","seduce",
                     "seduction",]
        self.Disabled = False

class BGProfileGetARoom(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "get_a_room",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(216, 99, 121, 255)"
        self.SecondTitleColor = "rgba(148, 94, 52, 255)"
        self.SmallTextColor = "rgba(37, 77, 139, 255)"
        self.AuthorNameColor = "rgba(65, 133, 180, 255)"
        self.Tags = ["woman","women","man","men","straight","couple","outdoors","brunette",
                     "fantasy","sea","ocean","dock","ship","night","fantasy","medieval",
                     "inn","boat","lord","lady","brunette",]
        self.Disabled = False

class BGProfileThreeDicks(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "three_dicks",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(222, 197, 99, 255)"
        self.SecondTitleColor = "rgba(224, 136, 83, 255)"
        self.SmallTextColor = "rgba(1, 53, 136, 255)"
        self.AuthorNameColor = "rgba(222, 197, 99, 255)"
        self.Tags = ["man","men","gay","nude","outdoors","towel",
                     "sea","ocean","beach","penis","ass",
                     "butt","threesome","strip","beach",
                     "sea","vacation","bronzed","tan","buns",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfilePinupWithBird(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "pinup_with_bird",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(238, 122, 155, 255)"
        self.SecondTitleColor = "rgba(72, 140, 149, 255)"
        self.SmallTextColor = "rgba(1, 53, 136, 255)"
        self.AuthorNameColor = "rgba(145, 167, 210, 255)"
        self.Tags = ["woman","single","nude","tits","bird","brunette",
                     "breasts","naked","strip","stripped","stripping",
                     "teen","young","daughter",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileCastleSunset(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "castle_sunset",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(236, 165, 71, 255)"
        self.SecondTitleColor = "rgba(75, 148, 181, 255)"
        self.SmallTextColor = "rgba(120, 62, 118, 255)"
        self.AuthorNameColor = "rgba(75, 148, 181, 255)"
        self.Tags = ["woman","man","couple","straight","brunette",
                     "fantasy","castle","dress","outdoors",
                     "knight","warrior","armor","gown","prince",
                     "king","princess","duke","lord","lady",
                     "german","french",]
        self.Disabled = False

class BGProfileBigGayCop(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Lowest,
                           sFileName = "big_gay_cop",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(254, 147, 43, 255)"
        self.SecondTitleColor = "rgba(82, 182, 100, 255)"
        self.SmallTextColor = "rgba(247, 217, 77, 255)"
        self.AuthorNameColor = "rgba(82, 182, 100, 255)"
        self.Tags = ["man","men","cop","police","nude","naked",
                     "gay","sunglasses","moustache","leather",
                     "penis","well-hung","erect","moustache",
                     "boots","sunglasses",
                     "muscular","giant",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileLaundromatAss(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "laundromat_ass",
                         Orient = OGAY,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(180, 44, 20, 255)"
        self.SecondTitleColor = "rgba(190, 87, 42, 255)"
        self.SmallTextColor = "rgba(67, 112, 184, 255)"
        self.AuthorNameColor = "rgba(67, 112, 184, 255)"
        self.Tags = ["man","men","couple","gay","shirtless",
                     "nude","modern","laundry","laundromat",
                     "ass","butt","underwear","muscular",
                     "muscles","indoors","day"]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileNudeReflectingBoi(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "nude_reflecting_boi",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(238, 0, 95, 255)"
        self.SecondTitleColor = "rgba(210, 70, 147, 255)"
        self.SmallTextColor = "rgba(21, 107, 188, 255)"
        self.AuthorNameColor = "rgba(21, 107, 188, 255)"
        self.Tags = ["man","nude","outdoors","beach","ocean","sea",
                     "naked","shirtless","gay","single","naked",
                     "muscular",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileGayVampireSex(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "gay_vampire_sex",
                         Orient = OGAY,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(228, 8, 29, 255)"
        self.SecondTitleColor = "rgba(72, 40, 148, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(93, 159, 175, 255)"
        self.Tags = ["man","men","couple","bed","indoors","nude","naked",
                     "bare-chested","shirtless","sex","october","pillows",
                     "vampire","horror","night","moon","night",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileGayMexicoRevolution(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "gay_mexico_revolution",
                         Orient = OGAY,
                         Group = GSING)
        self.MainTitleColor = "rgba(230, 98, 79, 255)"
        self.SecondTitleColor = "rgba(25, 117, 78, 255)"
        self.SmallTextColor = "rgba(114, 79, 53, 255)"
        self.AuthorNameColor = "rgba(234, 158, 167, 255)"
        self.Tags = ["man","gay","nude","horse","ethnic","latino",
                     "moustache","heels","kinky","naked","hat",
                     "mexico","legs","ass","single"]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileClipboardJealousy(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "clipboard_jealousy",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(175, 100, 130, 255)"
        self.SecondTitleColor = "rgba(179, 85, 38, 255)"
        self.SmallTextColor = "rgba(75, 70, 53, 255)"
        self.AuthorNameColor = "rgba(175, 100, 130, 255)"
        self.Tags = ["man","woman","straight","sweater","brunette","outdoors",
                     "couple","vest","older man","dad","dilf","boss",
                     "younger woman","teen","secretary","christian","mormon",
                     "virgin","innocent",]
        self.Disabled = False

class BGProfileWhippedDress(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "whipped_dress",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(216, 89, 38, 255)"
        self.SecondTitleColor = "rgba(174, 100, 68, 255)"
        self.SmallTextColor = "rgba(26, 56, 74, 255)"
        self.AuthorNameColor = "rgba(216, 89, 38, 255)"
        self.Tags = ["man","shirtless","woman","maledom","outdoors","fire","whip","kinky",
                     "bondage","voyeur","beach","ethnic","minority","kidnap","bound",
                     "captive","prisoner","black","cowboy","red dress","exposed","torn",
                     "punish","discipline","bbc","desert","beach","western","hat",
                     "strip","brat","indian","western",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileAssForHorseman(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "ass_for_horseman",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(186, 51, 66, 255)"
        self.SecondTitleColor = "rgba(45, 142, 161, 255)"
        self.SmallTextColor = "rgba(134, 166, 46, 255)"
        self.AuthorNameColor = "rgba(186, 51, 66, 255)"
        self.Tags = ["woman","nude","tits","ass","breasts","brunette","outdoors",
                     "fantasy","medieval","floating head","man","horse","maledom",
                     "warrior","butt","nipples","bent over","archer","busty",
                     ]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileGayBoatFoursome(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "gay_boat_foursome",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(253, 156, 123, 255)"
        self.SecondTitleColor = "rgba(212, 116, 141, 255)"
        self.SmallTextColor = "rgba(71, 115, 94, 255)"
        self.AuthorNameColor = "rgba(212, 116, 141, 255)"
        self.Tags = ["man","men","nude","gay","foursome","outdoors","boat","sea",
                     "sailors","penis","muscles","shirtless"]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileBathhouseButtocks(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "bathhouse_buttocks",
                         Orient = OGAY,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(240, 147, 147, 255)"
        self.SecondTitleColor = "rgba(133, 111, 78, 255)"
        self.SmallTextColor = "rgba(57, 52, 53, 255)"
        self.AuthorNameColor = "rgba(57, 52, 53, 255)"
        self.Tags = ["man","men","nude","gay","foursome","indoors","bath","water",
                     "bathhouse","ass","naked","muscles","shirtless","hairy",
                     "asian","pool","butt","giant","large","well-hung",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileGayShower(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Low,
                           sFileName = "gay_shower",
                         Orient = OGAY,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(240, 147, 147, 255)"
        self.SecondTitleColor = "rgba(133, 111, 78, 255)"
        self.SmallTextColor = "rgba(57, 52, 53, 255)"
        self.AuthorNameColor = "rgba(57, 52, 53, 255)"
        self.Tags = ["man","men","nude","gay","shower","indoors","bath","water",
                     "penis","muscles","shirtless","soap","steam",
                     "tanlines"]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileHawaiianThongRemoval(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.Normal,
                           sFileName = "hawaiian_thong_removal",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(230, 36, 63, 255)"
        self.SecondTitleColor = "rgba(172, 62, 43, 255)"
        self.SmallTextColor = "rgba(83, 41, 31, 255)"
        self.AuthorNameColor = "rgba(230, 36, 63, 255)"
        self.Tags = ["man","woman","straight","outdoors","asian","black hair",
                     "minority","hawaiian","tropical","topless","buttocks",
                     "thong","shirtless","couple","black",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileBlueBikiniRedPhone(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "blue_bikini_red_phone",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(1, 123, 201, 255)"
        self.SecondTitleColor = "rgba(211, 2, 13, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["woman","single","pinup","inside","indoors","blonde","bikini",
                     "lingerie","pinup","red phone","heels","blue ribbon",
                     "high heeled","swedish","german","porn star","call girl",
                     "dancer","penthouse","centerfold",]
        self.Disabled = False

class BGProfileZipperLady(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "zipper_lady",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(224, 40, 33, 255)"
        self.SecondTitleColor = "rgba(243, 118, 49, 255)"
        self.SmallTextColor = "rgba(30, 21, 151, 255)"
        self.AuthorNameColor = "rgba(30, 21, 151, 255)"
        self.Tags = ["woman","single","pinup","redhead","nude","breasts","cum",
                     "weird","kinky","zipper","leather","barechested","nude",
                     "strip","horny","slut",]
        self.Disabled = False
        self.Content = Content.AdultsOnly

class BGProfileLesbianCellmate(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.High,
                           sFileName = "lesbian_cellmate",
                         Orient = OLES,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(205, 62, 41, 255)"
        self.SecondTitleColor = "rgba(230, 102, 165, 255)"
        self.SmallTextColor = "rgba(27, 31, 33, 255)"
        self.AuthorNameColor = "rgba(230, 102, 165, 255)"
        self.Tags = ["woman","women","panties","ass","underwear",
                     "lingerie","lesbian","jail","prison",
                     "brunette","black","minority","kinky",
                     "butt","femdom","cell","prison","prisoner",
                     "captured","locked","trapped","imprisoned",
                     "kidnapped",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileHotMeal(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "hot_meal",
                         Orient = ONEUTRAL,
                         Group = GSING)
        self.MainTitleColor = "rgba(229, 60, 31, 255)"
        self.SecondTitleColor = "rgba(213, 94, 231, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(229, 60, 31, 255)"
        self.Tags = ["woman","single","brunette","provocative",
                     "outdoors","picnic","legs open","food","pie",
                     "suggestive","teen","waitress","stockings",
                     "pussy","slut","american","young","horny",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileNylonFingers(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "nylon_fingers",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(233, 45, 104, 255)"
        self.SecondTitleColor = "rgba(197, 45, 225, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(197, 45, 225, 255)"
        self.Tags = ["woman","man","couple","straight","lingerie",
                     "nylons","stockings","undressing","stripping",
                     "blue jeans","underwear","stripper","whore",
                     "mistress","underwear",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileHotSecretary(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "hot_secretary",
                         Orient = OSTRAIGHT,
                         Group = GSING)
        self.MainTitleColor = "rgba(224, 43, 55, 255)"
        self.SecondTitleColor = "rgba(79, 151, 203, 255)"
        self.SmallTextColor = "rgba(90, 12, 106, 255)"
        self.AuthorNameColor = "rgba(90, 12, 106, 255)"
        self.Tags = ["woman","man","straight","secretary","boss",
                     "office","desk","clipboard","purple dress",
                     "CEO","blonde","cleavage","busty","suit",
                     "business","illionaire","cleavage","legs",
                     "leggy","pencil","wealthy","swedish",
                     "french","teacher",]
        self.Disabled = False

class BGProfileHotwifeBusiness(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "hotwife_business",
                         Orient = OSTRAIGHT,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(252, 84, 113, 255)"
        self.SecondTitleColor = "rgba(38, 99, 125, 255)"
        self.SmallTextColor = "rgba(176, 17, 33, 255)"
        self.AuthorNameColor = "rgba(176, 17, 33, 255)"
        self.Tags = ["woman","man","straight","secretary","boss",
                     "threesome","dinner","pink dress","brunette",
                     "CEO","cleavage","busty","suit","hotwife",
                     "business","illionaire","cleavage","legs",
                     "leggy","wife","suit","tie","table",
                     "dinner table","husband","wealthy",
                     "older man","dad","father","brother",
                     "sister","smoking","cigar","french",]
        self.Disabled = False

class BGProfileAwkwardPose(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "awkward_pose",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(1, 123, 201, 255)"
        self.SecondTitleColor = "rgba(211, 2, 13, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["woman","man","straight","couple","redhead",
                     "busty","cleavage","shirtless","outdoors",
                     "grope","felt up","grope","flowers",
                     "sleep","dancer","scot","irish",]
        self.Disabled = False

class BGProfileLesbianNuns(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "lesbian_nuns",
                         Orient = OLES,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(216, 61, 16, 255)"
        self.SecondTitleColor = "rgba(214, 139, 70, 255)"
        self.SmallTextColor = "rgba(41, 81, 48, 255)"
        self.AuthorNameColor = "rgba(214, 139, 70, 255)"
        self.Tags = ["woman","women","lesbian","couple","nun",
                     "leg","habit","church","voyeur",
                     "garden","stockings","kiss","spied",
                     "watch","medieval","historic","blue robe",
                     "red robe",]
        self.Disabled = False

class BGProfileRecliningLesbo(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "reclining_lesbo",
                         Orient = OLES,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(215, 118, 157, 255)"
        self.SecondTitleColor = "rgba(106, 180, 154, 255)"
        self.SmallTextColor = "rgba(133, 81, 82, 255)"
        self.AuthorNameColor = "rgba(229, 152, 4, 255)"
        self.Tags = ["woman","women","lesbian","couple","nightgown",
                     "lingerie","pink nightgown","ping gown",
                     "menswear","butch","seduce","brunette","redhead",
                     "busty","trans","cleavage",]
        self.Disabled = False

class BGProfileInterracialHaystack(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "interracial_haystack",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(236, 81, 145, 255)"
        self.SecondTitleColor = "rgba(67, 167, 220, 255)"
        self.SmallTextColor = "rgba(164, 82, 21, 255)"
        self.AuthorNameColor = "rgba(67, 167, 220, 255)"
        self.Tags = ["woman","man","straight","couple","black",
                     "brunette","pink dress","haystack","country",
                     "interracial","business","busty","boss",
                     "wife","cousin","outdoors","farm","white",]
        self.Disabled = False

class BGProfileInterracialLapStraddle(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "interracial_lap_straddle",
                         Orient = OSTRAIGHT,
                         Group = GCOUP)
        self.MainTitleColor = "rgba(236, 81, 145, 255)"
        self.SecondTitleColor = "rgba(22, 125, 172, 255)"
        self.SmallTextColor = "rgba(102, 62, 136, 255)"
        self.AuthorNameColor = "rgba(22, 125, 172, 255)"
        self.Tags = ["woman","man","straight","couple","black",
                     "blonde","white","panties","underwear",
                     "topless","butt","bbc","shirtless",
                     "muscular","lap","strip","porn star",]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfilePrettyGymBoys(BGProfile):
    def __init__(self):
        super().__init__(Priority = GenPriority.AboveAverage,
                           sFileName = "pretty_gym_boys",
                         Orient = ONEUTRAL,
                         Group = GGROUP)
        self.MainTitleColor = "rgba(247, 27, 96, 255)"
        self.SecondTitleColor = "rgba(129, 142, 96, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(85, 147, 173, 255)"
        self.Tags = ["man","men","gay","gym","weight lifter",
                     "body builder","muscular","shirtless",
                     "strong","weights","workout","athlete",
                     "jock","bulge","sweatpants","t-shirt",
                     "thong","boys","olympic","medal",
                     "gloves","locker room",]
        self.Disabled = False

def PopRandomTag(TagList):
    if len(TagList) > 0:
        TagList.pop(randint(0, len(TagList) - 1))

    return TagList

class BGProfileContainer(GeneratorContainer):

    def HasReqTags(self, TagList1, TagList2):
        bHasTags = True

        for tag1 in TagList1:
            bFoundMatch = False 
            for tag2 in TagList2:
                if tag1 == tag2:
                    bFoundMatch = True
                    break
            if not bFoundMatch:
                bHasTags = False
                break

        return bHasTags

    def HasExclTags(self, TagList1, TagList2):
        bHasTags = False

        for tag1 in TagList1:
            for tag2 in TagList2:
                if tag1 == tag2:
                    bHasTags = True
                    break
            if bHasTags:
                break

        return bHasTags

def PickBGProfile(ImgTxtGen, ProfileHistoryQ = None, bAllowPromo = True, Type = None):
    Gen = None

    ReqTags = ImgTxtGen.ReqTemplateTags
    ExclTags = ImgTxtGen.ExclTemplateTags
    OptTags = ImgTxtGen.OptionalTemplateTags
    Orients = ImgTxtGen.Orients
    Groups = ImgTxtGen.Groups

    print(" - Optional tags: " + str(OptTags))
    print(" - Required tags: " + str(ReqTags))
    print(" - Excluded tags: " + str(ExclTags))

    iTries = 0

    if ProfileHistoryQ is None:
        #print("ProfileHistoryQ is None, initializing new history q")
        ProfileHistoryQ = HistoryQWithLog(titutil.BGPROFILEQ_FILENAME, iQSize = titutil.BGPROFILEQ_SIZE)

    iTopProfile = -1
    iTopScore = 0
    ScoredProfiles = []

    for subclass in BGProfile.__subclasses__():
        item = subclass()
        iScore = 0
        MatchedTags = []

        if (len(Orients) == 0 or item.Orient in Orients) and \
            (len(Groups) == 0 or item.Group in Groups):

            for synonym in Synonyms:
                if synonym[0] in item.Tags:
                    if synonym[1] not in item.Tags:
                        item.Tags.append(synonym[1])

            for tag in item.Tags:
                if tag in OptTags:
                    iScore += 2
                    MatchedTags.append(tag)
                if tag in ExclTags:
                    iScore -= 3
            for tag in ReqTags:
                if tag in item.Tags:
                    iScore += 3
            #iScore += item.Priority
            #iScore += 3 - item.Content

            #print(str(type(item).__name__)[9:] + " " + str(MatchedTags) + ", TOTAL: " + str(iScore))
               
            ScoredProfiles.append([item, iScore])
            if iTopProfile == -1 or iScore > iTopScore:
                iTopScore = iScore
                iTopProfile = len(ScoredProfiles) - 1
        #else:
        #    print(" - " + str(type(item).__name__) + " not Orient:" + str(Orient) + " or Group:" + str(Group))

    if len(ScoredProfiles) > 0 and iTopScore > -1:
        TopProfileMatches = GeneratorContainer(HistoryQ = ProfileHistoryQ)
        TopProfileMatches.GeneratorClassName = "BGProfile"
        for i, profile in enumerate(ScoredProfiles):
            if ScoredProfiles[i][1] >= iTopScore - 3:
                if ScoredProfiles[i][1] == iTopScore:
                    TopProfileMatches.AddGenerator(profile[0], GenPriority.High)
                else:
                    if profile[0].Content == Content.AllAges:
                        TopProfileMatches.AddGenerator(profile[0], GenPriority.AboveAverage)
                    elif profile[0].Content == Content.PG13:
                        TopProfileMatches.AddGenerator(profile[0], GenPriority.Normal)
                    else:
                        TopProfileMatches.AddGenerator(profile[0], GenPriority.Low)

        Gen = TopProfileMatches.RandomGenerator()

        #TopScoredProfiles = []
        #for i, profile in enumerate(ScoredProfiles):
        #    if profile[1] >= iTopScore:
        #        TopScoredProfiles.append(ScoredProfiles[i])

        #    if len(TopScoredProfiles) > 0:
        #        Gen = TopScoredProfiles[randint(0,len(TopScoredProfiles) - 1)][0]
    else:
        print("=*= WARNING =*= No scored profiles, picking BG profile at total random!")
        ProfSel = GeneratorContainer(GeneratorClass = BGProfile, HistoryQ = ProfileHistoryQ)
        Gen = ProfSel.RandomGenerator()

    ProfileHistoryQ.LogHistoryQ()    

    return Gen
   
def GetBGProfileGenerator(ImgTxtGen, 
                          iProfileID = 0, 
                          ProfileHistoryQ = None):
    SelectedProfile = None
    #print("GetBGProfileGenerator() iProfileID = " + str(iProfileID))

    iTries = 0

    if ProfileHistoryQ is None:
        #print("ProfileHistoryQ is None, initializing new history q")
        ProfileHistoryQ = HistoryQWithLog(titutil.BGPROFILEQ_FILENAME, iQSize = titutil.BGPROFILEQ_SIZE)

    ProfSel = GeneratorContainer(GeneratorClass = BGProfile, HistoryQ = ProfileHistoryQ)
    if iProfileID > 0:
        SelectedProfile = ProfSel.GetProfile(iProfileID)
        if SelectedProfile == None:
            SelectedProfile = BGProfile()
    else:
        SelectedProfile = PickBGProfile(ImgTxtGen = ImgTxtGen)

    #print("GetBGProfileGenerator()\n - Selected BG Profile is " + str(SelectedProfile) + ", it took " + str(iTries) + " tries.")
    ProfileHistoryQ.LogHistoryQ()    
    
    return SelectedProfile
     
MasterTagList = []
for subclass in BGProfile.__subclasses__():
    item = subclass()
    for synonym in Synonyms:
        if synonym[0] in item.Tags:
            if synonym[1] not in item.Tags:
                item.Tags.append(synonym[1])
    for tag in item.Tags:
        if tag not in MasterTagList:
            MasterTagList.append(tag)
        


#print ("MasterTagList is " + str(MasterTagList))