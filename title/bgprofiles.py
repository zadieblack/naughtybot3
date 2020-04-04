#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# background profiles module

import random
from util import *
from title.util import Content

BGLOGFILEPATH = "title/"
BGLOGFILENAME = "bghistory_q.txt"
BGQSIZE = 20
MAXTRIES = 500

ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, BGQSIZE)

class BGProfile():
    def __init__(self, ID = -1, Priority = 1, HeaderType = HeaderType.Harlequin, sFileName = ""):
        self.ID = ID
        self.Priority = Priority 
        self.HeaderType = HeaderType 
        self.FileName = sFileName
        self.AdultsOnly = False
        self.Disabled = False

        #self._HH_yOffset = 234
        #self._PH_yOffset = 127

        #init all colors to black
        self.MainTitleColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.AllAges
        self.Tags = []

class BGProfileSaxaphone(BGProfile):
    def __init__(self):
        super().__init__(ID = 1,
                           Priority = 4,
                           sFileName = "saxophone")
        self.MainTitleColor = "rgba(94, 68, 25, 255)"
        self.SecondTitleColor = "rgba(94, 68, 25, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "redhead","muscular"]
        self.Disabled = False

class BGProfileBeach(BGProfile):
    def __init__(self):
        super().__init__(ID = 2,
                           Priority = 4,
                           sFileName = "beach")
        self.MainTitleColor = "rgba(162, 63, 33, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "blonde","shirtless","beach"]
        self.Disabled = False

class BGProfileCrotchLevel(BGProfile):
    def __init__(self):
        super().__init__(ID = 3,
                           Priority = 4,
                           sFileName = "crotch_level")
        self.MainTitleColor = "rgba(193, 29, 63, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.SmallTextColor = "rgba(112, 162, 193, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "brunette","redhead","muscular","mountains"]
        self.Disabled = False

class BGProfileBoatNipples(BGProfile):
    def __init__(self):
        super().__init__(ID = 4,
                           Priority = 4,
                           sFileName = "boat_nipples")
        self.MainTitleColor = "rgba(39, 32, 73, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(39, 32, 73, 255)"
        self.AuthorNameColor = "rgba(39, 32, 73, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","pirate","ship","boat"]
        self.Disabled = False

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(ID = 5,
                           Priority = 4,
                           sFileName = "blue_car_fire")
        self.MainTitleColor = "rgba(132, 41, 55, 255)"
        self.SecondTitleColor = "rgba(181, 55, 47, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"
        self.Tags = ["man","woman","couple","outside","straight","brunette",
                     "modern","car","fire"]
        self.Disabled = False

class BGProfileIndian(BGProfile):
    def __init__(self):
        super().__init__(ID = 6,
                           Priority = 4,
                           sFileName = "indian")
        self.MainTitleColor = "rgba(157, 44, 43, 255)"
        self.SecondTitleColor = "rgba(157, 44, 43, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["man","woman","couple","outside","straight","western",
                     "shirtless","muscular"]
        self.Disabled = False

class BGProfileNakedFabio(BGProfile):
    def __init__(self):
        super().__init__(ID = 7,
                           Priority = 4,
                           sFileName = "naked_fabio")
        self.MainTitleColor = "rgba(238, 146, 134, 255)"
        self.SecondTitleColor = "rgba(238, 146, 134, 255)"
        self.SmallTextColor = "rgba(96, 39, 116, 255)"
        self.AuthorNameColor = "rgba(96, 39, 116, 255)"
        self.Tags = ["man","woman","couple","outside","straight","redhead",
                     "shirtless","muscular","fabio"]
        self.Disabled = False

class BGProfilePirate(BGProfile):
    def __init__(self):
        super().__init__(ID = 8,
                           Priority = 4,
                           sFileName = "pirate")
        self.MainTitleColor = "rgba(65, 112, 130, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(191, 77, 59, 255)"
        self.AuthorNameColor = "rgba(65, 112, 130, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "tied up","pirate","ship","boat"]
        self.Disabled = False

class BGProfileAquaTopless(BGProfile):
    def __init__(self):
        super().__init__(ID = 9,
                           Priority = 4,
                           sFileName = "aqua_topless")
        self.MainTitleColor = "rgba(149, 196, 180, 255)"
        self.SecondTitleColor = "rgba(108, 80, 145, 255)"
        self.Tags = ["man","woman","couple","straight","brunette","topless",
                     "shirtless","muscular"]
        self.Disabled = False

class BGProfileGay(BGProfile):
    def __init__(self):
        super().__init__(ID = 10,
                           Priority = 4,
                           sFileName = "gay")
        self.MainTitleColor = "rgba(189, 109, 65, 255)"
        self.SecondTitleColor = "rgba(189, 109, 65, 255)"
        self.SmallTextColor = "rgba(108, 145, 51, 255)"
        self.Tags = ["man","men","couple","gay","naked","nude","muscular"]
        self.Disabled = False

class BGProfileSunset(BGProfile):
    def __init__(self):
        super().__init__(ID = 11,
                           Priority = 4,
                           sFileName = "sunset")
        self.MainTitleColor = "rgba(178, 27, 44, 255)"
        self.SecondTitleColor = "rgba(178, 27, 44, 255)"
        self.Tags = ["man","woman","couple","outside","straight","brunette",
                     "shirtless","muscular","western"]
        self.Disabled = False

class BGProfileField(BGProfile):
    def __init__(self):
        super().__init__(ID = 12,
                           Priority = 4,
                           sFileName = "field")
        self.MainTitleColor = "rgba(214, 149, 123, 255)"
        self.SecondTitleColor = "rgba(139, 121, 171, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "muscular","brunette"]
        self.Disabled = False

class BGProfileRedVelvet(BGProfile):
    def __init__(self):
        super().__init__(ID = 13,
                           Priority = 4,
                           sFileName = "red_velvet")
        self.MainTitleColor = "rgba(181,55, 47, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.Tags = ["man","woman","couple","straight","brunette","shirtless",
                     "muscular","bed"]
        self.Disabled = False

class BGProfileRedAndPurple(BGProfile):
    def __init__(self):
        super().__init__(ID = 14,
                           Priority = 4,
                           sFileName = "red_and_purple")
        self.MainTitleColor = "rgba(209, 91, 56, 255)"
        self.SecondTitleColor = "rgba(209, 91, 56, 255)"
        self.SmallTextColor = "rgba(174, 95, 160, 255)"
        self.Tags = ["man","woman","couple","straight","redhead","bed",
                     "shirtless","muscular"]
        self.Disabled = False

class BGProfileSeventiesChic(BGProfile):
    def __init__(self):
        super().__init__(ID = 15,
                           Priority = 4,
                           sFileName = "seventies_chic")
        self.MainTitleColor = "rgba(194, 76, 39, 255)"
        self.SecondTitleColor = "rgba(139, 68, 25, 255)"
        self.SmallTextColor = "rgba(165, 150, 58, 255)"
        self.AuthorNameColor = "rgba(139, 68, 25, 255)"
        self.Tags = ["man","woman","couple","straight","blonde"]
        self.Disabled = False

class BGProfileBlueDress(BGProfile):
    def __init__(self):
        super().__init__(ID = 16,
                           Priority = 4,
                           sFileName = "blue_dress")
        self.MainTitleColor = "rgba(181, 79, 75, 255)"
        self.SecondTitleColor = "rgba(181, 79, 75, 255)"
        self.SmallTextColor = "rgba(1, 23, 244, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Tags = ["man","woman","couple","outside","straight","brunette",
                     "shirtless","muscular"]
        self.Disabled = False

class BGProfileDarkBlueFireSuit(BGProfile):
    def __init__(self):
        super().__init__(ID = 17,
                           Priority = 4,
                           sFileName = "dark_blue_fire_suit")
        self.MainTitleColor = "rgba(173, 84, 69, 255)"
        self.SecondTitleColor = "rgba(173, 84, 69, 255)"
        self.SmallTextColor = "rgba(53, 68, 89, 255)"
        self.Tags = ["man","woman","couple","outside","straight",
                     "suit","raven-haired", "fire"]
        self.Disabled = False

class BGProfileDark(BGProfile):
    def __init__(self):
        super().__init__(ID = 18,
                           Priority = 4,
                           sFileName = "dark")
        self.MainTitleColor = "rgba(84, 77, 93, 255)"
        self.SecondTitleColor = "rgba(84, 77, 93, 255)"
        self.Tags = ["man","woman","couple","straight","brunette"]
        self.Disabled = False

class BGProfileGold(BGProfile):
    def __init__(self):
        super().__init__(ID = 19,
                           Priority = 4,
                           sFileName = "gold")
        self.MainTitleColor = "rgba(106, 118, 47, 255)"
        self.SecondTitleColor = "rgba(106, 118, 47, 255)"
        self.SmallTextColor = "rgba(106, 118, 47, 255)"
        self.Tags = ["man","woman","couple","outside","straight","shirtless",
                     "muscular","topless","raven-haired"]
        self.Disabled = False

class BGProfileModernBedroom(BGProfile):
    def __init__(self):
        super().__init__(ID = 20,
                           Priority = 4,
                           sFileName = "modern_bedroom")
        self.MainTitleColor = "rgba(143, 137, 104, 255)"
        self.SecondTitleColor = "rgba(177, 119, 123, 255)"
        self.AuthorNameColor = "rgba(143, 137, 104, 255)"
        self.Tags = ["man","woman","couple","inside","straight","redhead",
                     "shirtless","muscular","bed"]
        self.Disabled = False

class BGProfileShipRomance(BGProfile):
    def __init__(self):
        super().__init__(ID = 21,
                           Priority = 4,
                           sFileName = "ship_romance")
        self.MainTitleColor = "rgba(75, 125, 152, 255)"
        self.SecondTitleColor = "rgba(75, 125, 152, 255)"
        self.SmallTextColor = "rgba(200, 159, 193, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "ship","boat","pirate"]
        self.Disabled = False

class BGProfileBath(BGProfile):
    def __init__(self):
        super().__init__(ID = 22,
                           Priority = 4,
                           sFileName = "bath")
        self.MainTitleColor = "rgba(209, 165, 48, 255)"
        self.SecondTitleColor = "rgba(145, 55, 63, 255)"
        self.SmallTextColor = "rgba(27, 112, 105, 255)"
        self.AuthorNameColor = "rgba(27, 112, 105, 255)"
        self.Tags = ["man","woman","couple","inside","straight","brunette",
                     "topless","nude","naked"]
        self.Content = Content.PG13
        self.Disabled = False
        
class BGProfileBedSurprise(BGProfile):
    def __init__(self):
        super().__init__(ID = 23,
                           Priority = 4,
                           sFileName = "bed_surprise")
        self.MainTitleColor = "rgba(186, 73, 27, 255)"
        self.SecondTitleColor = "rgba(186, 73, 27, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"
        self.Tags = ["woman","single","redhead","bed"]
        self.Disabled = False

class BGProfileBoatTowel(BGProfile):
    def __init__(self):
        super().__init__(ID = 24,
                           Priority = 4,
                           sFileName = "boat_towel")
        self.MainTitleColor = "rgba(175, 98, 53, 255)"
        self.SecondTitleColor = "rgba(175, 98, 53, 255)"
        self.SmallTextColor = "rgba(7, 10, 14, 255)"
        self.AuthorNameColor = "rgba(7, 10, 14, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "fabio","shirtless","muscular","ship","boat","pirate"]
        self.Disabled = False

class BGProfileCastle(BGProfile):
    def __init__(self):
        super().__init__(ID = 25,
                           Priority = 4,
                           sFileName = "castle")
        self.MainTitleColor = "rgba(107, 66, 113, 255)"
        self.SecondTitleColor = "rgba(158, 162, 61, 255)"
        self.SmallTextColor = "rgba(141, 50, 33, 255)"
        self.AuthorNameColor = "rgba(87, 170, 207, 255)"
        self.Tags = ["man","woman","couple","outside","straight","fantasy",
                     "blonde","medieval","castle"]
        self.Disabled = False

class BGProfileKinkyCuffs(BGProfile):
    def __init__(self):
        super().__init__(ID = 26,
                           Priority = 4,
                           sFileName = "kinky_cuffs")
        self.MainTitleColor = "rgba(170, 26, 24, 255)"
        self.SecondTitleColor = "rgba(170, 26, 24, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"
        self.Content = Content.PG13
        self.Tags = ["woman","single","outside","kinky","blonde","tied up"]
        self.Disabled = False
        
class BGProfileMansion(BGProfile):
    def __init__(self):
        super().__init__(ID = 27,
                           Priority = 4,
                           sFileName = "mansion")
        self.MainTitleColor = "rgba(221, 132, 34, 255)"
        self.SecondTitleColor = "rgba(41, 89, 135, 255)"
        self.SmallTextColor = "rgba(47, 78, 83, 255)"
        self.AuthorNameColor = "rgba(41, 89, 135, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","mansion"]
        self.Disabled = False

class BGProfileShower(BGProfile):
    def __init__(self):
        super().__init__(ID = 28,
                           Priority = 3,
                           sFileName = "shower")
        self.MainTitleColor = "rgba(199, 54, 60, 255)"
        self.SecondTitleColor = "rgba(210, 150, 78, 255)"
        self.SmallTextColor = "rgba(74, 155, 189, 255)"
        self.AuthorNameColor = "rgba(199, 54, 60, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","straight","brunette","naked","nude",
                     "tits","suit","single"]
        self.Disabled = False

class BGProfileSuperHero(BGProfile):
    def __init__(self):
        super().__init__(ID = 29,
                           Priority = 3,
                           sFileName = "superhero")
        self.MainTitleColor = "rgba(189, 42, 20, 255)"
        self.SecondTitleColor = "rgba(189, 42, 20, 255)"
        self.SmallTextColor = "rgba(205, 66, 109, 255)"
        self.AuthorNameColor = "rgba(122, 86, 172, 255)"
        self.Tags = ["man","woman","couple","straight","brunette",
                     "shirtless","muscular"]
        self.Disabled = False

class BGProfileSwingers(BGProfile):
    def __init__(self):
        super().__init__(ID = 30,
                           Priority = 4,
                           sFileName = "swingers")
        self.MainTitleColor = "rgba(203, 62, 76, 255)"
        self.SecondTitleColor = "rgba(203, 62, 76, 255)"
        self.SmallTextColor = "rgba(99, 113, 160, 255)"
        self.AuthorNameColor = "rgba(184, 172, 84, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","nature"]
        self.Disabled = False
        
class BGProfileSwordKilt(BGProfile):
    def __init__(self):
        super().__init__(ID = 31,
                           Priority = 4,
                           sFileName = "sword_kilt")
        self.MainTitleColor = "rgba(135, 49, 40, 255)"
        self.SecondTitleColor = "rgba(79, 86, 194, 255)"
        self.SmallTextColor = "rgba(41, 67, 193, 255)"
        self.AuthorNameColor = "rgba(135, 49, 58, 255)"
        self.Tags = ["man","woman","couple","outside","straight","fantasy",
                     "brunette","shirtless","muscular","kilt","sword",
                     "forest"]
        self.Disabled = False

class BGProfileTightButts(BGProfile):
    def __init__(self):
        super().__init__(ID = 32,
                           Priority = 2,
                           sFileName = "tight_butts")
        self.MainTitleColor = "rgba(108, 178, 234, 255)"
        self.SecondTitleColor = "rgba(99, 36, 2, 255)"
        self.SmallTextColor = "rgba(72, 87, 56, 255)" 
        self.AuthorNameColor = "rgba(108, 178, 234, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","gay","outside","naked","nude","butt",
                     "tanlines"]
        self.Disabled = False

class BGProfileTropicalPirate(BGProfile):
    def __init__(self):
        super().__init__(ID = 33,
                           Priority = 4,
                           sFileName = "tropical_pirate")
        self.MainTitleColor = "rgba(195, 21, 48, 255)"
        self.SecondTitleColor = "rgba(195, 21, 48, 255)"
        self.SmallTextColor = "rgba(35, 135, 63, 255)"
        self.AuthorNameColor = "rgba(38, 167, 207, 255)"
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "shirtless","muscular","ship","historical"]
        self.Disabled = False

class BGProfileBeefcakeAngel(BGProfile):
    def __init__(self):
        super().__init__(ID = 34,
                           Priority = 4,
                           sFileName = "beefcake_angel")
        self.MainTitleColor = "rgba(205, 99, 139, 255)"
        self.SecondTitleColor = "rgba(205, 99, 139, 255)"
        self.SmallTextColor = "rgba(101, 44, 84, 255)"
        self.AuthorNameColor = "rgba(101, 44, 84, 255)"
        self.Tags = ["man","woman","muscular","shirtless","angel","fantasy",
                     "brunette"]
        self.Disabled = False
        
class BGProfileChamberPot(BGProfile):
    def __init__(self):
        super().__init__(ID = 35,
                           Priority = 3,
                           sFileName = "chamber_pot")
        self.MainTitleColor = "rgba(198, 94, 21, 255)"
        self.SecondTitleColor = "rgba(198, 94, 21, 255)"
        self.SmallTextColor = "rgba(170, 60, 133, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","fantasy","historical","kinky","brunette",
                     "man","flower","tuxedo","naked","nude","tits","ass",
                     "single"]
        self.Disabled = False

class BGProfileChastityBelt(BGProfile):
    def __init__(self):
        super().__init__(ID = 36,
                           Priority = 4,
                           sFileName = "chastity_belt")
        self.MainTitleColor = "rgba(85, 89, 177, 255)"
        self.SecondTitleColor = "rgba(155, 36, 45, 255)"
        self.SmallTextColor = "rgba(6, 60, 86, 255)"
        self.AuthorNameColor = "rgba(85, 89, 177, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","straight","kinky","fantasy","topless",
                     "shirtless","muscular","tits","blonde","historical",
                     "femdom"]
        self.Disabled = False

class BGProfileCowgirlDominatrix(BGProfile):
    def __init__(self):
        super().__init__(ID = 37,
                           Priority = 3,
                           sFileName = "cowgirl_dominatrix")
        self.MainTitleColor = "rgba(19, 37, 113, 255)"
        self.SecondTitleColor = "rgba(19, 37, 113, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 149, 60, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","kinky","blonde",
                     "naked","nude","tits","BDSM","femdom"]
        self.Disabled = False

class BGProfileDickNose(BGProfile):
    def __init__(self):
        super().__init__(ID = 38,
                           Priority = 4,
                           sFileName = "dick_nose")
        self.MainTitleColor = "rgba(32, 124, 207, 255)"
        self.SecondTitleColor = "rgba(225, 47, 37, 255)"
        self.SmallTextColor = "rgba(198, 78, 107, 255)"
        self.AuthorNameColor = "rgba(225, 47, 37, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","outside","straight","kinky",
                     "blonde","topless","shirtless","muscular","circus",
                     "nose","bed"]
        self.Disabled = False

class BGProfileHandsAndKnees(BGProfile):
    def __init__(self):
        super().__init__(ID = 39,
                           Priority = 4,
                           sFileName = "hands_and_knees")
        self.MainTitleColor = "rgba(210, 136, 53, 255)"
        self.SecondTitleColor = "rgba(210, 136, 53, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.PG13
        self.Tags = ["woman","fantasy","kinky","redhead","loincloth",
                     "suit","historical","single"]
        self.Disabled = False

class BGProfileHarem(BGProfile):
    def __init__(self):
        super().__init__(ID = 40,
                           Priority = 1,
                           sFileName = "harem")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(62, 162, 167, 255)"
        self.AuthorNameColor = "rgba(62, 162, 167, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","woman","women","fantasy","brunette","blodne",
                     "bikini","tits","harem","straight"]
        self.Disabled = False

class BGProfileHotCops(BGProfile):
    def __init__(self):
        super().__init__(ID = 41,
                           Priority = 3,
                           sFileName = "hot_cops")
        self.MainTitleColor = "rgba(107, 173, 53, 255)"
        self.SecondTitleColor = "rgba(107, 173, 53, 255)"
        self.SmallTextColor = "rgba(184, 160, 43, 255)"
        self.AuthorNameColor = "rgba(184, 160, 43, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","redhead",
                     "blonde","cops","threesome","shirtless","muscular",
                     "topless","tits"]
        self.Disabled = False

class BGProfileIndecentProp(BGProfile):
    def __init__(self):
        super().__init__(ID = 42,
                           Priority = 3,
                           sFileName = "indecent_prop")
        self.MainTitleColor = "rgba(186, 155, 47, 255)"
        self.SecondTitleColor = "rgba(113, 25, 24, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(186, 155, 47, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","brunette",
                     "nude","naked","tits","ass","money","gambling",
                     "tuxedo","historic","casino"]
        self.Disabled = False

class BGProfileLadyBottom(BGProfile):
    def __init__(self):
        super().__init__(ID = 43,
                           Priority = 3,
                           sFileName = "lady_bottom")
        self.MainTitleColor = "rgba(15, 84, 120, 255)"
        self.SecondTitleColor = "rgba(15, 84, 120, 255)"
        self.SmallTextColor = "rgba(88, 105, 73, 255)"
        self.AuthorNameColor = "rgba(88, 105, 73, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","outside","fantasy","blonde","nude",
                     "naked","horse"]
        self.Disabled = False

class BGProfileLesbianVampires(BGProfile):
    def __init__(self):
        super().__init__(ID = 44,
                           Priority = 3,
                           sFileName = "lesbian_vampires")
        self.MainTitleColor = "rgba(123, 83, 137, 255)"
        self.SecondTitleColor = "rgba(123, 83, 137, 255)"
        self.SmallTextColor = "rgba(212, 1, 3, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","women","inside","lesbian","kinky","horror",
                     "castle","raven-haired","redhead","blonde","vampire"]
        self.Disabled = False

class BGProfileMaleSub(BGProfile):
    def __init__(self):
        super().__init__(ID = 45,
                           Priority = 3,
                           sFileName = "male_sub")
        self.MainTitleColor = "rgba(26, 79, 155, 255)"
        self.SecondTitleColor = "rgba(26, 79, 155, 255)"
        self.SmallTextColor = "rgba(131, 149, 93, 255)"
        self.AuthorNameColor = "rgba(200, 114, 184, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","kinky",
                     "femdom","nude","naked","shirtless","topless","tits",
                     "brunette","bed"]
        self.Disabled = False

class BGProfileMoonBoob(BGProfile):
    def __init__(self):
        super().__init__(ID = 46,
                           Priority = 4,
                           sFileName = "moon_boob")
        self.MainTitleColor = "rgba(186, 51, 57, 255)"
        self.SecondTitleColor = "rgba(186, 51, 57, 255)"
        self.SmallTextColor = "rgba(31, 51, 82, 255)"
        self.AuthorNameColor = "rgba(224, 183, 108, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","outside","straight","blonde",
                     "naked","nude","shirtless","topless","tits","ocean",
                     "bed"]
        self.Disabled = False

class BGProfileFlex(BGProfile):
    def __init__(self):
        super().__init__(ID = 47,
                           Priority = 4,
                           sFileName = "flex")
        self.MainTitleColor = "rgba(199, 47, 19, 255)"
        self.SecondTitleColor = "rgba(49, 114, 44, 255)"
        self.SmallTextColor = "rgba(1, 77, 119, 255)"
        self.AuthorNameColor = "rgba(1, 77, 119, 255)"
        self.Tags = ["man","indoors","muscular","shirtless","single"]
        self.Disabled = False

class BGProfilePervyDummy(BGProfile):
    def __init__(self):
        super().__init__(ID = 47,
                           Priority = 3,
                           sFileName = "pervy_dummy")
        self.MainTitleColor = "rgba(196, 50, 45, 255)"
        self.SecondTitleColor = "rgba(196, 50, 45, 255)"
        self.SmallTextColor = "rgba(123, 77, 151, 255)"
        self.AuthorNameColor = "rgba(123, 77, 151, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","kinky","man","fantasy","dwarf",
                     "naked","nude","tits","ass","pissing"]
        self.Disabled = False

class BGProfilePoodleBondage(BGProfile):
    def __init__(self):
        super().__init__(ID = 48,
                           Priority = 3,
                           sFileName = "poodle_bondage")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(83, 84, 141, 255)"
        self.AuthorNameColor = "rgba(83, 84, 141, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","kinky","blonde","brunette",
                     "femdom","topless","naked","nude","tits","ass",
                     "tied up"]
        self.Disabled = False

class BGProfileScaryMirror(BGProfile):
    def __init__(self):
        super().__init__(ID = 49,
                           Priority = 4,
                           sFileName = "scary_mirror")
        self.MainTitleColor = "rgba(202, 141, 14, 255)"
        self.SecondTitleColor = "rgba(202, 141, 14, 255)"
        self.SmallTextColor = "rgba(62, 122, 79, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","inside","horror","blonde",
                     "bed","masturbation","bed","single"]
        self.Disabled = False

class BGProfileSkeleton(BGProfile):
    def __init__(self):
        super().__init__(ID = 50,
                           Priority = 2,
                           sFileName = "skeleton")
        self.MainTitleColor = "rgba(157, 16, 16, 255)"
        self.SecondTitleColor = "rgba(157, 16, 16, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","horror","brunette","topless",
                     "naked","nude","bed","skeleton","tits","bush"]
        self.Disabled = False

class BGProfileSnowWhiteSevenDwarves(BGProfile):
    def __init__(self):
        super().__init__(ID = 51,
                           Priority = 2,
                           sFileName = "snow_white_7_dwarves")
        self.MainTitleColor = "rgba(52, 117, 47, 255)"
        self.SecondTitleColor = "rgba(52, 117, 47, 255)"
        self.SmallTextColor = "rgba(30, 63, 139, 255)"
        self.AuthorNameColor = "rgba(30, 63, 139, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","inside","kinky","fantasy","dwarf",
                     "raven-haired", "naked", "nude", "tits",
                     "panties","bed","single"]
        self.Disabled = False

class BGProfileDangerMine(BGProfile):
    def __init__(self):
        super().__init__(ID = 52,
                           Priority = 4,
                           sFileName = "danger_mine")
        self.MainTitleColor = "rgba(205, 97, 71, 255)"
        self.SecondTitleColor = "rgba(231, 140, 81, 255)"
        self.SmallTextColor = "rgba(1, 77, 119, 255)"
        self.AuthorNameColor = "rgba(79, 27, 36, 255)"
        self.Tags = ["man","woman","outdoors","blonde","couple","straight",
                     "danger","mine"]
        self.Disabled = False

class BGProfileSnowWhiteDungeon(BGProfile):
    def __init__(self):
        super().__init__(ID = 53,
                           Priority = 3,
                           sFileName = "snow_white_dungeon")
        self.MainTitleColor = "rgba(32, 89, 161, 255)"
        self.SecondTitleColor = "rgba(32, 89, 161, 255)"
        self.SmallTextColor = "rgba(238, 64, 130, 255)"
        self.AuthorNameColor = "rgba(241, 148, 33, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","fantasy","kinky","knight","raven-haired",
                     "tied up","topless","tits"]
        self.Disabled = False

class BGProfileSnowWhiteSpanking(BGProfile):
    def __init__(self):
        super().__init__(ID = 54,
                           Priority = 4,
                           sFileName = "snow_white_spanking")
        self.MainTitleColor = "rgba(131, 58, 110, 255)"
        self.SecondTitleColor = "rgba(131, 58, 110, 255)"
        self.SmallTextColor = "rgba(23, 81, 136, 255)"
        self.AuthorNameColor = "rgba(23, 81, 136, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","men","fantasy","kinky","viking",
                     "raven-haired","naked","nude","ass","spanking"]
        self.Disabled = False

class BGProfileStretchyArms(BGProfile):
    def __init__(self):
        super().__init__(ID = 55,
                           Priority = 2,
                           sFileName = "stretchy_arms")
        self.MainTitleColor = "rgba(227, 31, 15, 255)"
        self.SecondTitleColor = "rgba(227, 31, 15, 255)"
        self.SmallTextColor = "rgba(74, 61, 34, 255)"
        self.AuthorNameColor = "rgba(74, 61, 34, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","blonde",
                     "shirtless","nude","naked","tits","weird arms"]
        self.Disabled = False

class BGProfileSurroundedByPervs(BGProfile):
    def __init__(self):
        super().__init__(ID = 56,
                           Priority = 3,
                           sFileName = "surrounded_by_pervs")
        self.MainTitleColor = "rgba(66, 103, 86, 255)"
        self.SecondTitleColor = "rgba(196, 107, 28, 255)"
        self.SmallTextColor = "rgba(79, 89, 174, 255)"
        self.AuthorNameColor = "rgba(79, 89, 174, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","men","kinky","man","blonde","naked",
                     "nude","masturbation","single"]
        self.Disabled = False

class BGProfileTallWoman(BGProfile):
    def __init__(self):
        super().__init__(ID = 57,
                           Priority = 4,
                           sFileName = "tall_woman")
        self.MainTitleColor = "rgba(77, 172, 243, 255)"
        self.SecondTitleColor = "rgba(77, 172, 243, 255)"
        self.SmallTextColor = "rgba(210, 119, 82, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","brunette",
                     "topless","tits"]
        self.Disabled = False

class BGProfileTheDevil(BGProfile):
    def __init__(self):
        super().__init__(ID = 58,
                           Priority = 2,
                           sFileName = "the_devil")
        self.MainTitleColor = "rgba(212, 80, 83, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(47, 84, 51, 255)"
        self.AuthorNameColor = "rgba(47, 84, 51, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","straight","naked","nude",
                     "topless","tits","brunette","vampire","horror",
                     "bed"]
        self.Disabled = False

class BGProfileFireplaceBeauty(BGProfile):
    def __init__(self):
        super().__init__(ID = 59,
                           Priority = 40,
                           sFileName = "fireplace_beauty")
        self.MainTitleColor = "rgba(213, 22, 24, 255)"
        self.SecondTitleColor = "rgba(254, 171, 15, 255)"
        self.SmallTextColor = "rgba(11, 84, 115, 255)"
        self.AuthorNameColor = "rgba(11, 84, 115, 255)"
        self.Tags = ["woman","indoors","blonde","butt","fireplace",
                     "mirror","single"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileVampire(BGProfile):
    def __init__(self):
        super().__init__(ID = 60,
                           Priority = 2,
                           sFileName = "vampire")
        self.MainTitleColor = "rgba(23, 72, 199, 255)"
        self.SecondTitleColor = "rgba(23, 72, 199, 255)"
        self.SmallTextColor = "rgba(91, 48, 162, 255)"
        self.AuthorNameColor = "rgba(91, 48, 162, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","inside","kinky","horror","blonde",
                     "vampire","blood","fangs","naked","nude","tits",
                     "ass"]
        self.Disabled = False

class BGProfileUnderBedCreeper(BGProfile):
    def __init__(self):
        super().__init__(ID = 61,
                           Priority = 2,
                           sFileName = "under_bed_creeper")
        self.MainTitleColor = "rgba(130, 43, 39, 255)"
        self.SecondTitleColor = "rgba(199, 131, 61, 255)"
        self.SmallTextColor = "rgba(127, 117, 53, 255)"
        self.AuthorNameColor = "rgba(130, 43, 39, 255)"
        self.Tags = ["man","woman","couple","inside","men","voyeur",
                     "brunetted","bed","arabic","shirtless","muscular"]
        self.Disabled = False

class BGProfileVictorianOrgy(BGProfile):
    def __init__(self):
        super().__init__(ID = 62,
                           Priority = 4,
                           sFileName = "victorian_orgy")
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(48, 76, 124, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","women","inside","kinky","fantasy",
                     "bed"]
        self.Disabled = False

class BGProfileVoyeur(BGProfile):
    def __init__(self):
        super().__init__(ID = 63,
                           Priority = 4,
                           sFileName = "voyeur")
        self.MainTitleColor = "rgba(154, 46, 93, 255)"
        self.SecondTitleColor = "rgba(38, 95, 145, 255)"
        self.SmallTextColor = "rgba(67, 102, 122, 255)"
        self.AuthorNameColor = "rgba(154, 46, 93, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","women","inside","bed"]
        self.Disabled = False

class BGProfileWizardPony(BGProfile):
    def __init__(self):
        super().__init__(ID = 64,
                           Priority = 2,
                           sFileName = "wizard_pony")
        self.MainTitleColor = "rgba(244, 63, 233, 255)"
        self.SecondTitleColor = "rgba(244, 63, 233, 255)"
        self.SmallTextColor = "rgba(2, 47, 249, 255)"
        self.AuthorNameColor = "rgba(2, 47, 249, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","men","inside","kinky","fantasy",
                     "wizard","femdom"]
        self.Disabled = False

class BGProfileDoggyStyle(BGProfile):
    def __init__(self):
        super().__init__(ID = 65,
                           Priority = 1,
                           sFileName = "doggy_style")
        self.MainTitleColor = "rgba(113, 54, 24, 255)"
        self.SecondTitleColor = "rgba(113, 54, 24, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["man","woman","couple","inside","straight","naked",
                     "nude","tits","ass","pussy","sex","bed"]
        self.Disabled = False

class BGProfileBathhouse(BGProfile):
    def __init__(self):
        super().__init__(ID = 66,
                           Priority = 4,
                           sFileName = "bathhouse")
        self.MainTitleColor = "rgba(30, 102, 139, 255)"
        self.SecondTitleColor = "rgba(150, 85, 45, 255)"
        self.SmallTextColor = "rgba(150, 85, 45, 255)"
        self.AuthorNameColor = "rgba(196, 89, 81, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","inside","fantasy","gay","historic",
                     "naked","nude","shirtless","muscular"]
        self.Disabled = False

class BGProfileJilling(BGProfile):
    def __init__(self):
        super().__init__(ID = 67,
                           Priority = 4,
                           sFileName = "jilling")
        self.MainTitleColor = "rgba(91, 24, 45, 255)"
        self.SecondTitleColor = "rgba(181, 48, 43, 255)"  
        self.SmallTextColor ="rgba(106, 102, 69, 255)"
        self.AuthorNameColor = "rgba(91, 24, 45, 255)"
        self.Content = Content.AdultsOnly
        self.Tags = ["woman","single","inside","masturbation","topless",
                     "tits","bed"]
        self.Disabled = False

class BGProfileBranded(BGProfile):
    def __init__(self):
        super().__init__(ID = 68,
                           Priority = 2,
                           sFileName = "branded")
        self.MainTitleColor = "rgba(66, 75, 132, 255)"
        self.SecondTitleColor = "rgba(200, 82, 65, 255)"  
        self.SmallTextColor ="rgba(54, 50, 74, 255)"
        self.AuthorNameColor = "rgba(66, 75, 132, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","outside","gay","cowboy",
                     "nude","naked","shirtless","muscular"]
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
        super().__init__(ID = 70,
                           Priority = 4,
                           sFileName = "underwater")
        self.MainTitleColor = "rgba(228, 171, 62, 255)"
        self.SecondTitleColor = "rgba(150, 97, 131, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(228, 171, 62, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","outside","gay","underwater"]
        self.Disabled = False

class BGProfileSlaves(BGProfile):
    def __init__(self):
        super().__init__(ID = 71,
                           Priority = 4,
                           sFileName = "slaves")
        self.MainTitleColor = "rgba(169, 61, 55, 255)"
        self.SecondTitleColor = "rgba(212, 167, 84, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(50, 158, 194, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","men","kinky","outside","gay","fantasy",
                     "historic","shirtless","muscular","codpiece",
                     "whip","tied up"]
        self.Disabled = False

class BGProfileNakedCowboy(BGProfile):
    def __init__(self):
        super().__init__(ID = 72,
                           Priority = 4,
                           sFileName = "naked_cowboy")
        self.MainTitleColor = "rgba(138, 52, 46, 255)"
        self.SecondTitleColor = "rgba(83, 125, 148, 255)"  
        self.SmallTextColor ="rgba(205, 163, 106, 255)"
        self.AuthorNameColor = "rgba(138, 52, 46, 255)"
        self.Content = Content.PG13
        self.Tags = ["man","single","outside","gay","nude","naked",
                     "shirtless","muscular","cowboy"]
        self.Disabled = False

class BGProfileTwoGirls(BGProfile):
    def __init__(self):
        super().__init__(ID = 73,
                           Priority = 4,
                           sFileName = "two_girls")
        self.MainTitleColor = "rgba(255, 210, 47, 255)"
        self.SecondTitleColor = "rgba(83, 115, 148, 255)"  
        self.SmallTextColor ="rgba(205, 66, 35, 255)"
        self.AuthorNameColor = "rgba(83, 115, 148, 255)"  
        self.Content = Content.PG13
        self.Tags = ["woman","women","lesbian"]
        self.Disabled = False

class BGProfileSpaceMonster(BGProfile):
    def __init__(self):
        super().__init__(ID = 74,
                           Priority = 2,
                           sFileName = "space_monster")
        self.SmallTextColor = "rgba(199, 22, 30, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 
        self.Tags = ["woman","outside","kinky","tentacles","space",
                     "scifi","single"]
        self.Disabled = False

class BGProfileOneEyedAlien(BGProfile):
    def __init__(self):
        super().__init__(ID = 75,
                           Priority = 4,
                           sFileName = "one_eyed_alien")
        self.MainTitleColor = "rgba(219, 103, 122, 255)"
        self.SecondTitleColor = "rgba(72, 146, 145, 255)"  
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 
        self.Tags = ["women","woman","outside","scifi"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileSpaceGirl(BGProfile):
    def __init__(self):
        super().__init__(ID = 76,
                           Priority = 4,
                           sFileName = "space_girl")
        self.MainTitleColor = "rgba(48, 66, 138, 255)"
        self.SecondTitleColor = "rgba(48, 66, 138, 255)"
        self.SmallTextColor = "rgba(245, 180, 47, 255)"
        self.AuthorNameColor = "rgba(229, 79, 24, 255)" 
        self.Content = Content.PG13
        self.Tags = ["woman","single","outside","space","scifi",
                     "blonde"]
        self.Disabled = False

class BGProfileHawaiianCleavage(BGProfile):
    def __init__(self):
        super().__init__(ID = 77,
                           Priority = 4,
                           sFileName = "hawaiian_cleavage")
        self.MainTitleColor = "rgba(105, 113, 163, 255)"
        self.SecondTitleColor = "rgba(120, 162, 147, 255)"
        self.SmallTextColor = "rgba(208, 150, 60, 255)"
        self.AuthorNameColor = "rgba(208, 150, 60, 255)" 
        self.Tags = ["man","woman","couple","outside","straight"]
        self.Disabled = False

class BGProfileCowboyIndian(BGProfile):
    def __init__(self):
        super().__init__(ID = 78,
                           Priority = 4,
                           sFileName = "cowboy_indian")
        self.MainTitleColor = "rgba(247, 147, 135, 255)"
        self.SecondTitleColor = "rgba(156, 79, 153, 255)"
        self.SmallTextColor = "rgba(36, 57, 117, 255)"
        self.AuthorNameColor = "rgba(36, 57, 117, 255)"
        self.Tags = ["man","woman","couple","outside","straight"]
        self.Disabled = False

class BGProfileHorseRiders(BGProfile):
    def __init__(self):
        super().__init__(ID = 79,
                           Priority = 4,
                           sFileName = "horse_riders")
        self.MainTitleColor = "rgba(212, 94, 36, 255)"
        self.SecondTitleColor = "rgba(220, 64, 52, 255)"
        self.SmallTextColor = "rgba(160, 80, 143, 255)"
        self.AuthorNameColor = "rgba(128, 176, 224, 255)"
        self.Tags = ["man","woman","couple","outside","straight"]
        self.Disabled = False

class BGProfileShowSomeLeg(BGProfile):
    def __init__(self):
        super().__init__(ID = 80,
                           Priority = 4,
                           sFileName = "show_some_leg")
        self.MainTitleColor = "rgba(64, 85, 27, 255)"
        self.SecondTitleColor = "rgba(113, 42, 43, 255)"
        self.SmallTextColor = "rgba(208, 150, 60, 255)"
        self.AuthorNameColor = "rgba(208, 150, 60, 255)"
        self.Tags = ["man","woman","couple","outside","straight"]
        self.Disabled = False

class BGProfileLesbians(BGProfile):
    def __init__(self):
        super().__init__(ID = 81,
                           Priority = 4,
                           sFileName = "lesbians")
        self.MainTitleColor = "rgba(195, 100, 72, 255)"
        self.SecondTitleColor = "rgba(47, 104, 117, 255)"
        self.SmallTextColor = "rgba(218, 149, 162, 255)"
        self.AuthorNameColor = "rgba(195, 100, 72, 255)"
        self.Tags = ["woman","women","inside","lesbian","bed"]
        self.Disabled = False

#class BGProfileRedDressParty(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 81,
#                           Priority = 4,
#                           sFileName = "red_dress_party")
#        self.MainTitleColor = "rgba(191, 41, 32, 255)"
#        self.SecondTitleColor = "rgba(88, 118, 85, 255)"
#        self.SmallTextColor = "rgba(124, 50, 19, 255)"
#        self.AuthorNameColor = "rgba(234, 182, 73, 255)"
#        self.Tags = ["man","woman","straight"]
#        self.Disabled = False

class BGProfileLesbianTemptation(BGProfile):
    def __init__(self):
        super().__init__(ID = 82,
                           Priority = 4,
                           sFileName = "lesbian_temptation")
        self.MainTitleColor = "rgba(191, 57, 32, 255)"
        self.SecondTitleColor = "rgba(229, 170, 3, 255)"
        self.SmallTextColor = "rgba(153, 102, 153, 255)"
        self.AuthorNameColor = "rgba(191, 57, 32, 255)"
        self.Tags = ["woman","women","inside","lesbian"]
        self.Disabled = False

class BGProfileRedBedCutie(BGProfile):
    def __init__(self):
        super().__init__(ID = 83,
                           Priority = 4,
                           sFileName = "red_bed_cutie")
        self.MainTitleColor = "rgba(188, 9, 2, 255)"
        self.SecondTitleColor = "rgba(188, 9, 2, 255)"
        self.SmallTextColor = "rgba(153, 102, 153, 255)"
        self.Tags = ["woman","single","inside","brunette","bed"]
        self.Disabled = False

class BGProfilePinkShower(BGProfile):
    def __init__(self):
        super().__init__(ID = 84,
                           Priority = 4,
                           sFileName = "pink_shower")
        self.MainTitleColor = "rgba(205, 79, 107, 255)"
        self.SecondTitleColor = "rgba(241, 166, 150, 255)"
        self.SmallTextColor = "rgba(158, 162, 225, 255)"
        self.AuthorNameColor = "rgba(136, 67, 107, 255)"
        self.Tags = ["woman","single","inside","nude","naked",
                     "bathroom","shower","phone"]
        self.Disabled = False

#class BGProfileGolf(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 85,
#                           Priority = 4,
#                           sFileName = "golf")
#        self.MainTitleColor = "rgba(91, 160, 201, 255)"
#        self.SecondTitleColor = "rgba(77, 179, 117, 255)"
#        self.SmallTextColor = "rgba(157, 68, 148, 255)"
#        self.AuthorNameColor = "rgba(77, 179, 117, 255)"
#        self.Tags = ["man","woman","men","women","outside","voyeur"]
#        self.Disabled = False

class BGProfileFlowers(BGProfile):
    def __init__(self):
        super().__init__(ID = 86,
                           Priority = 4,
                           sFileName = "flowers")
        self.MainTitleColor = "rgba(198, 77, 94, 255)"
        self.SecondTitleColor = "rgba(228, 156, 82, 255)"
        self.SmallTextColor = "rgba(186, 113, 189, 255)"
        self.AuthorNameColor = "rgba(71, 116, 56, 255)"
        self.Tags = ["man","woman","couple","straight"]
        self.Disabled = False

class BGProfileHelloSailor(BGProfile):
    def __init__(self):
        super().__init__(ID = 87,
                           Priority = 4,
                           sFileName = "hello_sailor")
        self.MainTitleColor = "rgba(82, 126, 183, 255)"
        self.SecondTitleColor = "rgba(82, 126, 183, 255)"
        self.SmallTextColor = "rgba(202, 179, 194, 255)"
        self.AuthorNameColor = "rgba(194, 82, 31, 255)"
        self.Tags = ["man","single","shirtless","muscular","outdoors"]
        self.Disabled = False

class BGProfileLatinoCowboy(BGProfile):
    def __init__(self):
        super().__init__(ID = 88,
                           Priority = 4,
                           sFileName = "latino_cowboy")
        self.MainTitleColor = "rgba(138, 19, 20, 255)"
        self.SecondTitleColor = "rgba(147, 115, 73, 255)"
        self.SmallTextColor = "rgba(164, 91, 56, 255)"
        self.AuthorNameColor = "rgba(164, 91, 56, 255)"
        self.Tags = ["man","single","cowboy","shirtless","muscular"]
        self.Disabled = False

#class BGProfileDemiGod(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 89,
#                           Priority = 4,
#                           sFileName = "demi_god")
#        self.MainTitleColor = "rgba(208, 66, 32, 255)"
#        self.SecondTitleColor = "rgba(45, 75, 63, 255)"
#        self.SmallTextColor =  "rgba(147, 115, 73, 255)"
#        self.AuthorNameColor = "rgba(45, 75, 63, 255)"
#        self.Tags = ["man","single"]
#        self.Disabled = False

class BGProfileNudeSailorButt(BGProfile):
    def __init__(self):
        super().__init__(ID = 90,
                           Priority = 4,
                           sFileName = "nude_sailor_butt")
        self.MainTitleColor = "rgba(45, 84, 112, 255)"
        self.SecondTitleColor = "rgba(206, 77, 87, 255)"
        self.AuthorNameColor = "rgba(45, 84, 112, 255)"
        self.Tags = ["man","men","gay","inside","sailor","bed"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileOceanHorse(BGProfile):
    def __init__(self):
        super().__init__(ID = 90,
                           Priority = 4,
                           sFileName = "ocean_horse")
        self.MainTitleColor = "rgba(232, 191, 72, 255)"
        self.SecondTitleColor = "rgba(232, 191, 72, 255)"
        self.SmallTextColor =  "rgba(152, 102, 58, 255)" 
        self.AuthorNameColor = "rgba(105, 154, 170, 255)"
        self.Tags = ["man","single","outside","horse","nude","naked",
                     "muscular","shirtless"]
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
        super().__init__(ID = 92,
                           Priority = 4,
                           sFileName = "red_satin_sheets")
        self.MainTitleColor = "rgba(134, 15, 55, 255)"
        self.SecondTitleColor = "rgba(6, 108, 17, 255)"
        self.AuthorNameColor = "rgba(134, 15, 55, 255)"
        self.Tags = ["man","woman","straight","couple","inside","bed",
                     "blonde"]
        self.Disabled = False

class BGProfileFabioHero(BGProfile):
    def __init__(self):
        super().__init__(ID = 93,
                           Priority = 4,
                           sFileName = "fabio_hero")
        self.MainTitleColor = "rgba(24, 99, 209, 255)"
        self.SecondTitleColor = "rgba(87, 87, 89, 255)"
        self.SmallTextColor = "rgba(125, 47, 30, 255)"
        self.AuthorNameColor = "rgba(87, 87, 89, 255)"
        self.Tags = ["man","outside","fantasy","fabio","single"]
        self.Disabled = False

class BGProfileBigCity(BGProfile):
    def __init__(self):
        super().__init__(ID = 94,
                           Priority = 4,
                           sFileName = "big_city")
        self.MainTitleColor = "rgba(204, 40, 29, 255)"
        self.SecondTitleColor = "rgba(25, 51, 107, 255)"
        self.Tags = ["man","woman","outside","city","couple","straight"]
        self.Disabled = False

class BGProfileInterracial(BGProfile):
    def __init__(self):
        super().__init__(ID = 95,
                           Priority = 4,
                           sFileName = "interracial")
        self.MainTitleColor = "rgba(228, 113, 164, 255)"
        self.SecondTitleColor = "rgba(228, 113, 164, 255)"
        self.SmallTextColor = "rgba(71, 136, 200, 255)"
        self.AuthorNameColor = "rgba(71, 136, 200, 255)"
        self.Tags = ["man","woman","straight","modern","minority"]
        self.Content = Content.AdultsOnly
        self.Disabled = False

class BGProfileRedCape(BGProfile):
    def __init__(self):
        super().__init__(ID = 96,
                           Priority = 4,
                           sFileName = "red_cape")
        self.MainTitleColor = "rgba(208, 51, 4, 255)"
        self.SecondTitleColor = "rgba(174, 111, 165, 255)"
        self.SmallTextColor = "rgba(18, 18, 23, 255)"
        self.AuthorNameColor = "rgba(208, 51, 4, 255)"
        self.Tags = ["woman","blonde","single"]
        self.Disabled = False

class BGProfileValleyLake(BGProfile):
    def __init__(self):
        super().__init__(ID = 97,
                           Priority = 4,
                           sFileName = "valley_lake")
        self.MainTitleColor = "rgba(202, 141, 138, 255)"
        self.SecondTitleColor = "rgba(71, 168, 169, 255)"
        self.SmallTextColor = "rgba(71, 168, 169, 255)"
        self.AuthorNameColor = "rgba(202, 141, 138, 255)"
        self.Tags = ["woman","man","couple","straight","fantasy","outside"]
        self.Disabled = False

class BGProfileIslandUndressing(BGProfile):
    def __init__(self):
        super().__init__(ID = 98,
                           Priority = 4,
                           sFileName = "island_undressing")
        self.MainTitleColor = "rgba(170, 8, 4, 255)"
        self.SecondTitleColor = "rgba(170, 8, 4, 255)"
        self.SmallTextColor = "rgba(93, 108, 19, 255)"
        self.AuthorNameColor = "rgba(93, 108, 19, 255)"
        self.Tags = ["woman","outside","undressing","naked","nude",
                     "single"]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfilePinUp(BGProfile):
    def __init__(self):
        super().__init__(ID = 99,
                           Priority = 4,
                           sFileName = "pin_up")
        self.MainTitleColor = "rgba(232, 36, 23, 255)"
        self.SecondTitleColor = "rgba(232, 36, 23, 255)"
        self.SmallTextColor = "rgba(89, 186, 160, 255)"
        self.AuthorNameColor = "rgba(239, 104, 123, 255)"
        self.Tags = ["woman","blonde","single"]
        self.Disabled = False

class BGProfileWindowVoyeur(BGProfile):
    def __init__(self):
        super().__init__(ID = 100,
                           Priority = 4,
                           sFileName = "window_voyeur")
        self.MainTitleColor = "rgba(195, 63, 47, 255)"
        self.SecondTitleColor = "rgba(25, 117, 164, 255)"
        self.SmallTextColor = "rgba(54, 132, 122, 255)"
        self.AuthorNameColor = "rgba(25, 117, 164, 255)"
        self.Tags = ["woman","man","undressing","kinky","blonde",
                     "single"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileInterracialThreesome(BGProfile):
    def __init__(self):
        super().__init__(ID = 101,
                           Priority = 3,
                           sFileName = "interracial_threesome")
        self.MainTitleColor = "rgba(57, 187, 210, 255)"
        self.SecondTitleColor = "rgba(201, 16, 113, 255)"
        self.SmallTextColor = "rgba(52, 49, 98, 255)"
        self.AuthorNameColor = "rgba(52, 49, 98, 255)"
        self.Tags = ["woman","man","men","naked","indoors","kinky",
                     "bed"]
        self.Content = Content.AdultsOnly
        self.Disabled = False

class BGProfileDrMcChesty(BGProfile):
    def __init__(self):
        super().__init__(ID = 102,
                           Priority = 4,
                           sFileName = "dr_mc_chesty")
        self.MainTitleColor = "rgba(76, 136, 175, 255)"
        self.SecondTitleColor = "rgba(223, 150, 89, 255)"
        self.SmallTextColor = "rgba(155, 70, 159, 255)"
        self.AuthorNameColor = "rgba(223, 150, 89, 255)"
        self.Tags = ["woman","man","straight","couple","indoors",
                     "shirtless"]
        self.Disabled = False

class BGProfileBadDoctor(BGProfile):
    def __init__(self):
        super().__init__(ID = 103,
                           Priority = 4,
                           sFileName = "bad_doctor")
        self.MainTitleColor = "rgba(217, 80, 66, 255)"
        self.SecondTitleColor = "rgba(217, 80, 66, 255)"
        self.SmallTextColor = "rgba(122, 120, 44, 255)"
        self.AuthorNameColor = "rgba(122, 120, 44, 255)"
        self.Tags = ["woman","man","straight","indoors"]
        self.Disabled = False

class BGProfileAutumnHeadband(BGProfile):
    def __init__(self):
        super().__init__(ID = 104,
                           Priority = 4,
                           sFileName = "autumn_headband")
        self.MainTitleColor = "rgba(233, 140, 2, 255)"
        self.SecondTitleColor = "rgba(125, 99, 3, 255)"
        self.SmallTextColor = "rgba(139, 106, 69, 255)"
        self.AuthorNameColor = "rgba(125, 99, 3, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors"]
        self.Disabled = False

class BGProfileIndianPrincess(BGProfile):
    def __init__(self):
        super().__init__(ID = 105,
                           Priority = 4,
                           sFileName = "indian_princess")
        self.MainTitleColor = "rgba(218, 124, 1, 255)"
        self.SecondTitleColor = "rgba(148, 39, 20, 255)"
        self.SmallTextColor = "rgba(55, 74, 121, 255)"
        self.AuthorNameColor = "rgba(148, 39, 20, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors",
                     "brunette","indian"]
        self.Disabled = False

class BGProfileOrangeFromBehind(BGProfile):
    def __init__(self):
        super().__init__(ID = 106,
                           Priority = 4,
                           sFileName = "orange_from_behind")
        self.MainTitleColor = "rgba(243, 108, 1, 255)"
        self.SecondTitleColor = "rgba(119, 141, 38, 255)"
        self.SmallTextColor = "rgba(154, 91, 163, 255)"
        self.AuthorNameColor = "rgba(154, 91, 163, 255)"
        self.Tags = ["woman","man","straight","couple","outdoors"]
        self.Disabled = False

class BGProfileCabinFever(BGProfile):
    def __init__(self):
        super().__init__(ID = 107,
                           Priority = 4,
                           sFileName = "cabin_fever")
        self.MainTitleColor = "rgba(171, 0, 34, 255)"
        self.SecondTitleColor = "rgba(171, 0, 34, 255)"
        self.SmallTextColor = "rgba(48, 89, 135, 255)"
        self.AuthorNameColor = "rgba(48, 89, 135, 255)"
        self.Tags = ["woman","man","straight","couple","indoors"]
        self.Disabled = False

class BGProfileCensorEagle(BGProfile):
    def __init__(self):
        super().__init__(ID = 108,
                           Priority = 4,
                           sFileName = "censor_eagle")
        self.MainTitleColor = "rgba(233, 109, 51, 255)"
        self.SecondTitleColor = "rgba(233, 109, 51, 255)"
        self.SmallTextColor = "rgba(105, 168, 213, 255)"
        self.AuthorNameColor = "rgba(105, 168, 213, 255)"
        self.Tags = ["man","outdoors","ocean","nude","naked",
                     "shirtless","muscular","single"]
        self.Disabled = False

class BGProfileLesbianKiss(BGProfile):
    def __init__(self):
        super().__init__(ID = 109,
                           Priority = 4,
                           sFileName = "lesbian_kiss")
        self.MainTitleColor = "rgba(210, 161, 51, 255)"
        self.SecondTitleColor = "rgba(210, 161, 51, 255)"
        self.SmallTextColor = "rgba(181, 57, 41, 255)"
        self.AuthorNameColor = "rgba(181, 57, 41, 255)"
        self.Tags = ["woman","women","lesbian","indoors","couple","bed"]
        self.Disabled = False

class BGProfileLesboThreesome(BGProfile):
    def __init__(self):
        super().__init__(ID = 110,
                           Priority = 4,
                           sFileName = "lesbo_threesome")
        self.MainTitleColor = "rgba(92, 142, 142, 255)"
        self.SecondTitleColor = "rgba(92, 142, 142, 255)"
        self.SmallTextColor = "rgba(207, 105, 61, 255)"
        self.AuthorNameColor = "rgba(207, 161, 98, 255)"
        self.Tags = ["woman","women","lesbian","indoors","bed","naked",
                     "nude","couple"]
        self.Disabled = False
        self.Content = Content.PG13

class BGProfileSharingBed(BGProfile):
    def __init__(self):
        super().__init__(ID = 111,
                           Priority = 4,
                           sFileName = "sharing_bed")
        self.MainTitleColor = "rgba(198, 74, 53, 255)"
        self.SecondTitleColor = "rgba(84, 135, 137, 255)"
        self.SmallTextColor = "rgba(101, 67, 102, 255)"
        self.AuthorNameColor = "rgba(101, 67, 102, 255)"
        self.Tags = ["woman","women","lesbian","indoors"]
        self.Disabled = False

class BGProfileHotLasso(BGProfile):
    def __init__(self):
        super().__init__(ID = 112,
                           Priority = 4,
                           sFileName = "hot_lasso")
        self.MainTitleColor = "rgba(198, 68, 42, 255)"
        self.SecondTitleColor = "rgba(52, 162, 137, 255)"
        self.SmallTextColor = "rgba(120, 115, 147, 255)"
        self.AuthorNameColor = "rgba(120, 115, 147, 255)"
        self.Tags = ["man","outdoors","cowboy","single"]
        self.Disabled = False

class BGProfileThirdMan(BGProfile):
    def __init__(self):
        super().__init__(ID = 113,
                           Priority = 4,
                           sFileName = "third_man")
        self.MainTitleColor = "rgba(150, 45, 23, 255)"
        self.SecondTitleColor = "rgba(32, 104, 43, 255)"
        self.AuthorNameColor = "rgba(150, 45, 23, 255)"
        self.Tags = ["man","men", "woman", "indoors", "bed"]
        self.Content = Content.PG13
        self.Disabled = False

class BGProfileFileCabinet(BGProfile):
    def __init__(self):
        super().__init__(ID = 114,
                           Priority = 2,
                           sFileName = "file_cabinet")
        self.MainTitleColor = "rgba(236, 53, 36, 255)"
        self.SecondTitleColor = "rgba(221, 97, 99, 255)"
        self.SmallTextColor = "rgba(2, 117, 71, 255)"
        self.AuthorNameColor = "rgba(133, 123, 32, 255)"
        self.Tags = ["woman","indoors","blonde","single"]
        self.Disabled = False

class BGProfileWindowCreeper(BGProfile):
    def __init__(self):
        super().__init__(ID = 115,
                           Priority = 4,
                           sFileName = "window_creeper")
        self.MainTitleColor = "rgba(219, 49, 26, 255)"
        self.SecondTitleColor = "rgba(232, 174, 36, 255)"
        self.SmallTextColor = "rgba(8, 70, 131, 255)"
        self.AuthorNameColor = "rgba(3, 71, 15, 255)"
        self.Tags = ["woman","indoors","bed","voyeur","blonde","single"]
        self.Disabled = False

class BGProfileLesboFriend(BGProfile):
    def __init__(self):
        super().__init__(ID = 116,
                           Priority = 4,
                           sFileName = "lesbo_friend")
        self.MainTitleColor = "rgba(170, 43, 40, 255)"
        self.SecondTitleColor = "rgba(94, 146, 95, 255)"
        self.SmallTextColor = "rgba(85, 120, 154, 255)"
        self.AuthorNameColor = "rgba(85, 120, 154, 255)"
        self.Tags = ["woman","women","lesbian","indoors","blonde",
                     "brunette"]
        self.Disabled = False

class BGProfileNaughtyBarn(BGProfile):
    def __init__(self):
        super().__init__(ID = 117,
                           Priority = 4,
                           sFileName = "naughty_barn")
        self.MainTitleColor = "rgba(249, 49, 37, 255)"
        self.SecondTitleColor = "rgba(204, 145, 88, 255)"
        self.SmallTextColor = "rgba(71, 106, 116, 255)"
        self.AuthorNameColor = "rgba(71, 106, 116, 255)"
        self.Tags = ["woman","man","straight","blonde","barn","couple"]
        self.Disabled = False

class BGProfileBulgingCodpieces(BGProfile):
    def __init__(self):
        super().__init__(ID = 118,
                           Priority = 4,
                           sFileName = "bulging_codpieces")
        self.MainTitleColor = "rgba(142, 22, 25, 255)"
        self.SecondTitleColor = "rgba(194, 102, 52, 255)"
        self.SmallTextColor = "rgba(143, 138, 40, 255)"
        self.AuthorNameColor = "rgba(194, 102, 52, 255)"
        self.Tags = ["men","man","muscular","fantasy","outdoors","gay"]
        self.Disabled = False

class BGProfileLesboBoudoir(BGProfile):
    def __init__(self):
        super().__init__(ID = 119,
                           Priority = 4,
                           sFileName = "lesbo_boudoir")
        self.MainTitleColor = "rgba(216, 107, 111, 255)"
        self.SecondTitleColor = "rgba(110, 173, 69, 255)"
        self.SmallTextColor = "rgba(126, 63, 100, 255)"
        self.AuthorNameColor = "rgba(110, 173, 69, 255)"
        self.Tags = ["woman","women","blonde","brunette",
                     "lesbian"]
        self.Disabled = False

class BGProfileOctoAttack(BGProfile):
    def __init__(self):
        super().__init__(ID = 120,
                           Priority = 4,
                           sFileName = "octo_attack")
        self.MainTitleColor = "rgba(223, 112, 77, 255)"
        self.SecondTitleColor = "rgba(71, 109, 63, 255)"
        self.SmallTextColor = "rgba(44, 117, 179, 255)"
        self.AuthorNameColor = "rgba(44, 117, 179, 255)"
        self.Tags = ["woman","outdoors","underwater","bikini","blonde",
                     "octopus","tentacles"]
        self.Disabled = False

class BGProfileNurseTriangle(BGProfile):
    def __init__(self):
        super().__init__(ID = 121,
                           Priority = 40,
                           sFileName = "nurse_triangle")
        self.MainTitleColor = "rgba(93, 133, 72, 255)"
        self.SecondTitleColor = "rgba(93, 133, 72, 255)"
        self.SmallTextColor = "rgba(139, 64, 56, 255)"
        self.AuthorNameColor = "rgba(198, 77, 44, 255)"
        self.Tags = ["woman","man","couple","nurse","redhead",
                     "indoors","hospital","suit","straight"]
        self.Disabled = False

class BGProfileNurseTriangleMFF(BGProfile):
    def __init__(self):
        super().__init__(ID = 122,
                           Priority = 40,
                           sFileName = "nurse_triangle_mff")
        self.MainTitleColor = "rgba(217, 67, 22, 255)"
        self.SecondTitleColor = "rgba(70, 128, 129, 255)"
        self.SmallTextColor = "rgba(22, 73, 97, 255)"
        self.AuthorNameColor = "rgba(22, 73, 97, 255)"
        self.Tags = ["woman","man","couple","nurse","blonde",
                     "indoors","hospital","doctor","straight",
                     "threesome"]
        self.Disabled = False

class BGProfileBoatBOys(BGProfile):
    def __init__(self):
        super().__init__(ID = 123,
                           Priority = 40,
                           sFileName = "boat_boys")
        self.MainTitleColor = "rgba(139, 183, 218, 255)"
        self.SecondTitleColor = "rgba(202, 49, 27, 255)"
        self.SmallTextColor = "rgba(106, 55, 39, 255)"
        self.AuthorNameColor = "rgba(106, 55, 39, 255)"
        self.Tags = ["man","men","shirtless","muscular",
                     "outdoors","ocean","boat","threesome"]
        self.Disabled = False






# this is for debugging bgprofile frequency. delete later.
def indexof(list, searchobj):
    iIndex = 0
    bFound = False

    while iIndex < len(list):
        if list[iIndex][0][1].FileName == searchobj[1].FileName:
            bFound = True
            break
        iIndex = iIndex + 1
    
    if not bFound:
        iIndex = -1

    return iIndex

class ProfileSelector():
    def __init__(self):
        self.ProfileList = [] 

        for subclass in BGProfile.__subclasses__():
            item = subclass()

            # A multiplier effect for the "safe for work" profiles.
            iFactor = 1
            if item.Content == Content.AllAges:
                iFactor = 10
            elif item.Content == Content.PG13:
                iFactor = 5 
            iFactor = 1

            if not item.Disabled:
                for x in range(0, item.Priority * iFactor):
                    self.ProfileList.append([item.ID, item])
         
        # this is for debugging bgprofile frequency. delete later.

        #sTable = "[object name]: [count]\n"
        #ProfileCountTable = []
        #for profile in self.ProfileList:
        #    i = indexof(ProfileCountTable, profile)
        #    if i > -1:
        #        ProfileCountTable[i][1] = ProfileCountTable[i][1] + 1
        #    else:
        #        ProfileCountTable.append([profile, 1])

        #iAllAgesCount = 0
        #iPG13Count = 0
        #iAdultsOnlyCount = 0 
        #for item in ProfileCountTable:
        #    sTable += str(item[0][1].FileName) + ": " + str(item[1]) + "\n"
        #    if item[0][1].Content == Content.AdultsOnly:
        #        iAdultsOnlyCount = iAdultsOnlyCount + item[1]
        #    elif item[0][1].Content == Content.PG13:
        #        iPG13Count = iPG13Count + item[1]
        #    else:
        #        iAllAgesCount = iAllAgesCount + item[1]
        #sTable += "\n\n"
        #sTable += "# All Ages: " + str(iAllAgesCount) + "\n"
        #sTable += "# PG13: " + str(iPG13Count) + "\n"
        #sTable += "# Adults Only: " + str(iAdultsOnlyCount) + "\n\n"
        #sTable += "% PG13 = " + str(round((iPG13Count / (iAllAgesCount + iPG13Count + iAdultsOnlyCount)) * 100, 2)) + "%\n"
        #sTable += "% Adults Only = " + str(round((iAdultsOnlyCount / (iAllAgesCount + iPG13Count + iAdultsOnlyCount)) * 100, 2)) + "%\n"

        #print(sTable)

    def RandomProfile(self, ReqTags = [], ExclTags = []):
        Profile = []

        iTries = 0

        if len(self.ProfileList) > 0:
            Profile = choice(self.ProfileList)

            while iTries < MAXTRIES and \
                (not self.HasReqTags(ReqTags, Profile[1].Tags) or self.HasExclTags(ExclTags, Profile[1].Tags)):
                Profile = choice(self.ProfileList)
                iTries = iTries + 1
            print("After " + str(iTries) + " tries, " + str(Profile[1]) + " was selected.\n")

        return Profile
          
    def GetProfile(self, iProfileID):
        SelectedProfile = None 
          
        if len(self.ProfileList) > 0:
            for profile in self.ProfileList :
                if profile.ID == iProfileID:
                    SelectedProfile = profile
                    break
                         
        return SelectedProfile

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

   
def GetBGProfileGenerator(iProfileID = 0, 
                          ProfileHistoryQ = None,
                          ReqTags = [],
                          ExclTags = []):
    SelectedProfile = None
    #print("GetBGProfileGenerator() iProfileID = " + str(iProfileID))

    iTries = 0

    if ProfileHistoryQ is None:
        ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, iQSize = BGQSIZE)

    ProfSel = ProfileSelector()
    if iProfileID > 0:
        SelectedProfile = ProfSel.GetProfile(iProfileID)
        if SelectedProfile == None:
            SelectedProfile = BGProfile()
    else:
        SelectedProfile = ProfSel.RandomProfile(ReqTags, ExclTags)[1]
        iTries = 1
        while iTries < 20 and \
            not ProfileHistoryQ.PushToHistoryQ(SelectedProfile.ID):
            SelectedProfile = ProfSel.RandomProfile(ReqTags, ExclTags)[1]
            iTries = iTries + 1

    #print("GetBGProfileGenerator()\n - Selected BG Profile is " + str(SelectedProfile) + ", it took " + str(iTries) + " tries.")
    ProfileHistoryQ.LogHistoryQ()    
    
    return SelectedProfile
     