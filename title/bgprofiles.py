#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# background profiles module

import random
from util import *

BGLOGFILEPATH = "title/"
BGLOGFILENAME = "bghistory_q.txt"
BGQSIZE = 15

ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, BGQSIZE)

class BGProfile():
    def __init__(self, ID = -1, Priority = 1, HeaderType = HeaderType.Harlequin, sFileName = ""):
        self.ID = ID
        self.Priority = Priority 
        self.HeaderType = HeaderType 
        self.FileName = sFileName
        self.AdultsOnly = False

        #self._HH_yOffset = 234
        #self._PH_yOffset = 127

        #init all colors to black
        self.MainTitleColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"

class BGProfileSaxaphone(BGProfile):
    def __init__(self):
        super().__init__(ID = 1,
                           Priority = 10,
                           sFileName = "saxophone")
        self.MainTitleColor = "rgba(94, 68, 25, 255)"
        self.SecondTitleColor = "rgba(94, 68, 25, 255)"

class BGProfileBeach(BGProfile):
    def __init__(self):
        super().__init__(ID = 2,
                           Priority = 10,
                           sFileName = "beach")
        self.MainTitleColor = "rgba(162, 63, 33, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"

class BGProfileCrotchLevel(BGProfile):
    def __init__(self):
        super().__init__(ID = 3,
                           Priority = 10,
                           sFileName = "crotch_level")
        self.MainTitleColor = "rgba(193, 29, 63, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.SmallTextColor = "rgba(112, 162, 193, 255)"

class BGProfileBoatNipples(BGProfile):
    def __init__(self):
        super().__init__(ID = 4,
                           Priority = 10,
                           sFileName = "boat_nipples")
        self.MainTitleColor = "rgba(39, 32, 73, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(39, 32, 73, 255)"
        self.AuthorNameColor = "rgba(39, 32, 73, 255)"

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(ID = 5,
                           Priority = 10,
                           sFileName = "blue_car_fire")
        self.MainTitleColor = "rgba(132, 41, 55, 255)"
        self.SecondTitleColor = "rgba(132, 41, 55, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"

class BGProfileIndian(BGProfile):
    def __init__(self):
        super().__init__(ID = 6,
                           Priority = 10,
                           sFileName = "indian")
        self.MainTitleColor = "rgba(157, 44, 43, 255)"
        self.SecondTitleColor = "rgba(157, 44, 43, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileNakedFabio(BGProfile):
    def __init__(self):
        super().__init__(ID = 7,
                           Priority = 10,
                           sFileName = "naked_fabio")
        self.MainTitleColor = "rgba(238, 146, 134, 255)"
        self.SecondTitleColor = "rgba(238, 146, 134, 255)"
        self.SmallTextColor = "rgba(96, 39, 116, 255)"
        self.AuthorNameColor = "rgba(96, 39, 116, 255)"

class BGProfilePirate(BGProfile):
    def __init__(self):
        super().__init__(ID = 8,
                           Priority = 10,
                           sFileName = "pirate")
        self.MainTitleColor = "rgba(65, 112, 130, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(191, 77, 59, 255)"
        self.AuthorNameColor = "rgba(65, 112, 130, 255)"

class BGProfileAquaTopless(BGProfile):
    def __init__(self):
        super().__init__(ID = 9,
                           Priority = 10,
                           sFileName = "aqua_topless")
        self.MainTitleColor = "rgba(149, 196, 180, 255)"
        self.SecondTitleColor = "rgba(108, 80, 145, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileGay(BGProfile):
    def __init__(self):
        super().__init__(ID = 10,
                           Priority = 10,
                           sFileName = "gay")
        self.MainTitleColor = "rgba(189, 109, 65, 255)"
        self.SecondTitleColor = "rgba(189, 109, 65, 255)"
        self.SmallTextColor = "rgba(108, 145, 51, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileSunset(BGProfile):
    def __init__(self):
        super().__init__(ID = 11,
                           Priority = 10,
                           sFileName = "sunset")
        self.MainTitleColor = "rgba(178, 27, 44, 255)"
        self.SecondTitleColor = "rgba(178, 27, 44, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileField(BGProfile):
    def __init__(self):
        super().__init__(ID = 12,
                           Priority = 10,
                           sFileName = "field")
        self.MainTitleColor = "rgba(214, 149, 123, 255)"
        self.SecondTitleColor = "rgba(139, 121, 171, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileRedVelvet(BGProfile):
    def __init__(self):
        super().__init__(ID = 13,
                           Priority = 10,
                           sFileName = "red_velvet")
        self.MainTitleColor = "rgba(181,55, 47, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileRedAndPurple(BGProfile):
    def __init__(self):
        super().__init__(ID = 14,
                           Priority = 10,
                           sFileName = "red_and_purple")
        self.MainTitleColor = "rgba(209, 91, 56, 255)"
        self.SecondTitleColor = "rgba(209, 91, 56, 255)"
        self.SmallTextColor = "rgba(174, 95, 160, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(ID = 15,
                           Priority = 10,
                           sFileName = "blue_car_fire")
        self.MainTitleColor = "rgba(132,41, 55, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"

class BGProfileBlueDress(BGProfile):
    def __init__(self):
        super().__init__(ID = 16,
                           Priority = 10,
                           sFileName = "blue_dress")
        self.MainTitleColor = "rgba(181, 79, 75, 255)"
        self.SecondTitleColor = "rgba(181, 79, 75, 255)"
        self.SmallTextColor = "rgba(1, 23, 244, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileDarkBlueFireSuit(BGProfile):
    def __init__(self):
        super().__init__(ID = 17,
                           Priority = 10,
                           sFileName = "dark_blue_fire_suit")
        self.MainTitleColor = "rgba(173, 84, 69, 255)"
        self.SecondTitleColor = "rgba(173, 84, 69, 255)"
        self.SmallTextColor = "rgba(53, 68, 89, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileDark(BGProfile):
    def __init__(self):
        super().__init__(ID = 18,
                           Priority = 10,
                           sFileName = "dark")
        self.MainTitleColor = "rgba(84, 77, 93, 255)"
        self.SecondTitleColor = "rgba(84, 77, 93, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileGold(BGProfile):
    def __init__(self):
        super().__init__(ID = 19,
                           Priority = 10,
                           sFileName = "gold")
        self.MainTitleColor = "rgba(106, 118, 47, 255)"
        self.SecondTitleColor = "rgba(106, 118, 47, 255)"
        self.SmallTextColor = "rgba(106, 118, 47, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileModernBedroom(BGProfile):
    def __init__(self):
        super().__init__(ID = 20,
                           Priority = 10,
                           sFileName = "modern_bedroom")
        self.MainTitleColor = "rgba(143, 137, 104, 255)"
        self.SecondTitleColor = "rgba(177, 119, 123, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(143, 137, 104, 255)"

class BGProfileShipRomance(BGProfile):
    def __init__(self):
        super().__init__(ID = 21,
                           Priority = 10,
                           sFileName = "ship_romance")
        self.MainTitleColor = "rgba(75, 125, 152, 255)"
        self.SecondTitleColor = "rgba(75, 125, 152, 255)"
        self.SmallTextColor = "rgba(200, 159, 193, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileBath(BGProfile):
    def __init__(self):
        super().__init__(ID = 22,
                           Priority = 8,
                           sFileName = "bath")
        self.MainTitleColor = "rgba(209, 165, 48, 255)"
        self.SecondTitleColor = "rgba(145, 55, 63, 255)"
        self.SmallTextColor = "rgba(27, 112, 105, 255)"
        self.AuthorNameColor = "rgba(27, 112, 105, 255)"
        
class BGProfileBedSurprise(BGProfile):
    def __init__(self):
        super().__init__(ID = 23,
                           Priority = 10,
                           sFileName = "bed_surprise")
        self.MainTitleColor = "rgba(186, 73, 27, 255)"
        self.SecondTitleColor = "rgba(186, 73, 27, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"

class BGProfileBoatTowel(BGProfile):
    def __init__(self):
        super().__init__(ID = 24,
                           Priority = 10,
                           sFileName = "boat_towel")
        self.MainTitleColor = "rgba(175, 98, 53, 255)"
        self.SecondTitleColor = "rgba(175, 98, 53, 255)"
        self.SmallTextColor = "rgba(7, 10, 14, 255)"
        self.AuthorNameColor = "rgba(7, 10, 14, 255)"

class BGProfileCastle(BGProfile):
    def __init__(self):
        super().__init__(ID = 25,
                           Priority = 10,
                           sFileName = "castle")
        self.MainTitleColor = "rgba(107, 66, 113, 255)"
        self.SecondTitleColor = "rgba(158, 162, 61, 255)"
        self.SmallTextColor = "rgba(141, 50, 33, 255)"
        self.AuthorNameColor = "rgba(87, 170, 207, 255)"

class BGProfileKinkyCuffs(BGProfile):
    def __init__(self):
        super().__init__(ID = 26,
                           Priority = 10,
                           sFileName = "kinky_cuffs")
        self.MainTitleColor = "rgba(170, 26, 24, 255)"
        self.SecondTitleColor = "rgba(170, 26, 24, 255)"
        self.SmallTextColor = "rgba(94, 134, 120, 255)"
        self.AuthorNameColor = "rgba(1, 54, 100, 255)"
        self.AdultsOnly = True
        
class BGProfileMansion(BGProfile):
    def __init__(self):
        super().__init__(ID = 27,
                           Priority = 10,
                           sFileName = "mansion")
        self.MainTitleColor = "rgba(221, 132, 34, 255)"
        self.SecondTitleColor = "rgba(41, 89, 152, 135)"
        self.SmallTextColor = "rgba(47, 78, 83, 255)"
        self.AuthorNameColor = "rgba(41, 89, 135, 255)"

class BGProfileShower(BGProfile):
    def __init__(self):
        super().__init__(ID = 28,
                           Priority = 3,
                           sFileName = "shower")
        self.MainTitleColor = "rgba(199, 54, 60, 255)"
        self.SecondTitleColor = "rgba(210, 150, 78, 255)"
        self.SmallTextColor = "rgba(74, 155, 78, 189)"
        self.AuthorNameColor = "rgba(199, 54, 60, 255)"
        self.AdultsOnly = True

class BGProfileSuperHero(BGProfile):
    def __init__(self):
        super().__init__(ID = 29,
                           Priority = 10,
                           sFileName = "superhero")
        self.MainTitleColor = "rgba(189, 42, 20, 255)"
        self.SecondTitleColor = "rgba(189, 42, 20, 255)"
        self.SmallTextColor = "rgba(205, 66, 109, 255)"
        self.AuthorNameColor = "rgba(122, 86, 172, 255)"

class BGProfileSwingers(BGProfile):
    def __init__(self):
        super().__init__(ID = 30,
                           Priority = 10,
                           sFileName = "swingers")
        self.MainTitleColor = "rgba(203, 62, 76, 255)"
        self.SecondTitleColor = "rgba(203, 62, 76, 255)"
        self.SmallTextColor = "rgba(99, 113, 160, 255)"
        self.AuthorNameColor = "rgba(184, 172, 84, 255)"
        
class BGProfileSwordKilt(BGProfile):
    def __init__(self):
        super().__init__(ID = 31,
                           Priority = 10,
                           sFileName = "sword_kilt")
        self.MainTitleColor = "rgba(135, 49, 40, 255)"
        self.SecondTitleColor = "rgba(79, 86, 194, 255)"
        self.SmallTextColor = "rgba(41, 67, 193, 255)"
        self.AuthorNameColor = "rgba(135, 49, 58, 255)"

class BGProfileTightButts(BGProfile):
    def __init__(self):
        super().__init__(ID = 32,
                           Priority = 8,
                           sFileName = "tight_butts")
        self.MainTitleColor = "rgba(108, 178, 234, 255)"
        self.SecondTitleColor = "rgba(99, 36, 2, 255)"
        self.SmallTextColor = "rgba(72, 87, 56, 255)" 
        self.AuthorNameColor = "rgba(108, 178, 234, 255)"
        self.AdultsOnly = True

class BGProfileTropicalPirate(BGProfile):
    def __init__(self):
        super().__init__(ID = 33,
                           Priority = 10,
                           sFileName = "tropical_pirate")
        self.MainTitleColor = "rgba(195, 21, 48, 255)"
        self.SecondTitleColor = "rgba(195, 21, 48, 255)"
        self.SmallTextColor = "rgba(35, 135, 63, 255)"
        self.AuthorNameColor = "rgba(38, 167, 207, 255)"

#class BGProfileUSA(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 34,
#                           Priority = 10,
#                           sFileName = "usa")
#        self.MainTitleColor = "rgba(210, 1, 28, 255)"
#        self.SecondTitleColor = "rgba(210, 1, 28, 255)" 
#        self.SmallTextColor = "rgba(107, 202, 245, 255)"
#        self.AuthorNameColor = "rgba(16, 37, 56, 255)"
        
class BGProfileChamberPot(BGProfile):
    def __init__(self):
        super().__init__(ID = 35,
                           Priority = 3,
                           sFileName = "chamber_pot")
        self.MainTitleColor = "rgba(198, 94, 21, 255)"
        self.SecondTitleColor = "rgba(198, 94, 21, 255)"
        self.SmallTextColor = "rgba(170, 60, 133, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileChastityBelt(BGProfile):
    def __init__(self):
        super().__init__(ID = 36,
                           Priority = 3,
                           sFileName = "chastity_belt")
        self.MainTitleColor = "rgba(85, 89, 177, 255)"
        self.SecondTitleColor = "rgba(155, 36, 45, 255)"
        self.SmallTextColor = "rgba(6, 60, 86, 255)"
        self.AuthorNameColor = "rgba(85, 89, 177, 255)"
        self.AdultsOnly = True

class BGProfileCowgirlDominatrix(BGProfile):
    def __init__(self):
        super().__init__(ID = 37,
                           Priority = 3,
                           sFileName = "cowgirl_dominatrix")
        self.MainTitleColor = "rgba(19, 37, 113, 255)"
        self.SecondTitleColor = "rgba(19, 37, 113, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 149, 60, 255)"
        self.AdultsOnly = True

class BGProfileDickNose(BGProfile):
    def __init__(self):
        super().__init__(ID = 38,
                           Priority = 3,
                           sFileName = "dick_nose")
        self.MainTitleColor = "rgba(32, 124, 207, 255)"
        self.SecondTitleColor = "rgba(225, 47, 37, 255)"
        self.SmallTextColor = "rgba(198, 78, 107, 255)"
        self.AuthorNameColor = "rgba(225, 47, 37, 255)"
        self.AdultsOnly = True

class BGProfileHandsAndKnees(BGProfile):
    def __init__(self):
        super().__init__(ID = 39,
                           Priority = 4,
                           sFileName = "hands_and_knees")
        self.MainTitleColor = "rgba(210, 136, 53, 255)"
        self.SecondTitleColor = "rgba(210, 136, 53, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileHarem(BGProfile):
    def __init__(self):
        super().__init__(ID = 4,
                           Priority = 8,
                           sFileName = "harem")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(62, 162, 167, 255)"
        self.AuthorNameColor = "rgba(62, 162, 167, 255)"
        self.AdultsOnly = True

class BGProfileHotCops(BGProfile):
    def __init__(self):
        super().__init__(ID = 41,
                           Priority = 3,
                           sFileName = "hot_cops")
        self.MainTitleColor = "rgba(107, 173, 53, 255)"
        self.SecondTitleColor = "rgba(107, 173, 53, 255)"
        self.SmallTextColor = "rgba(184, 160, 43, 255)"
        self.AuthorNameColor = "rgba(184, 160, 43, 255)"
        self.AdultsOnly = True

class BGProfileIndecentProp(BGProfile):
    def __init__(self):
        super().__init__(ID = 42,
                           Priority = 3,
                           sFileName = "indecent_prop")
        self.MainTitleColor = "rgba(186, 155, 47, 255)"
        self.SecondTitleColor = "rgba(113, 25, 24, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(186, 155, 47, 255)"
        self.AdultsOnly = True

class BGProfileLadyBottom(BGProfile):
    def __init__(self):
        super().__init__(ID = 43,
                           Priority = 3,
                           sFileName = "lady_bottom")
        self.MainTitleColor = "rgba(15, 84, 120, 255)"
        self.SecondTitleColor = "rgba(15, 84, 120, 255)"
        self.SmallTextColor = "rgba(88, 105, 73, 255)"
        self.AuthorNameColor = "rgba(88, 105, 73, 255)"
        self.AdultsOnly = True

class BGProfileLesbianVampires(BGProfile):
    def __init__(self):
        super().__init__(ID = 44,
                           Priority = 3,
                           sFileName = "lesbian_vampires")
        self.MainTitleColor = "rgba(123, 83, 137, 255)"
        self.SecondTitleColor = "rgba(123, 83, 137, 255)"
        self.SmallTextColor = "rgba(212, 1, 3, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileMaleSub(BGProfile):
    def __init__(self):
        super().__init__(ID = 45,
                           Priority = 3,
                           sFileName = "male_sub")
        self.MainTitleColor = "rgba(26, 79, 155, 255)"
        self.SecondTitleColor = "rgba(26, 79, 155, 255)"
        self.SmallTextColor = "rgba(131, 149, 93, 255)"
        self.AuthorNameColor = "rgba(200, 114, 184, 255)"
        self.AdultsOnly = True

class BGProfileMoonBoob(BGProfile):
    def __init__(self):
        super().__init__(ID = 46,
                           Priority = 3,
                           sFileName = "moon_boob")
        self.MainTitleColor = "rgba(186, 51, 57, 255)"
        self.SecondTitleColor = "rgba(186, 51, 57, 255)"
        self.SmallTextColor = "rgba(31, 51, 82, 255)"
        self.AuthorNameColor = "rgba(224, 183, 108, 255)"
        self.AdultsOnly = True

#class BGProfileNaughtyBuddha(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 35,
#                           Priority = 2,
#                           sFileName = "naughty_buddha",
#                           sPHFileName = "naughty_buddha_ph.png")
#        self.MainTitleColor = "rgba(9, 71, 161, 255)"
#        self.SecondTitleColor = "rgba(9, 71, 161, 255)"
#        self.SmallTextColor = "rgba(21, 85, 76, 255)"
#        self.AuthorNameColor = "rgba(209, 155, 14, 255)"

class BGProfilePervyDummy(BGProfile):
    def __init__(self):
        super().__init__(ID = 47,
                           Priority = 3,
                           sFileName = "pervy_dummy")
        self.MainTitleColor = "rgba(196, 50, 45, 255)"
        self.SecondTitleColor = "rgba(196, 50, 45, 255)"
        self.SmallTextColor = "rgba(123, 77, 151, 255)"
        self.AuthorNameColor = "rgba(123, 77, 151, 255)"
        self.AdultsOnly = True

class BGProfilePoodleBondage(BGProfile):
    def __init__(self):
        super().__init__(ID = 48,
                           Priority = 3,
                           sFileName = "poodle_bondage")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(83, 84, 141, 255)"
        self.AuthorNameColor = "rgba(83, 84, 141, 255)"
        self.AdultsOnly = True

class BGProfileScaryMirror(BGProfile):
    def __init__(self):
        super().__init__(ID = 49,
                           Priority = 3,
                           sFileName = "scary_mirror")
        self.MainTitleColor = "rgba(202, 141, 14, 255)"
        self.SecondTitleColor = "rgba(202, 141, 14, 255)"
        self.SmallTextColor = "rgba(62, 122, 79, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileSkeleton(BGProfile):
    def __init__(self):
        super().__init__(ID = 50,
                           Priority = 2,
                           sFileName = "skeleton")
        self.MainTitleColor = "rgba(157, 16, 16, 255)"
        self.SecondTitleColor = "rgba(157, 16, 16, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileSnowWhiteSevenDwarves(BGProfile):
    def __init__(self):
        super().__init__(ID = 51,
                           Priority = 2,
                           sFileName = "snow_white_7_dwarves")
        self.MainTitleColor = "rgba(52, 117, 47, 255)"
        self.SecondTitleColor = "rgba(52, 117, 47, 255)"
        self.SmallTextColor = "rgba(30, 63, 139, 255)"
        self.AuthorNameColor = "rgba(30, 63, 139, 255)"
        self.AdultsOnly = True

#class BGProfileSnowWhiteAss(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 52,
#                           Priority = 3,
#                           sFileName = "snow_white_ass")
#        self.MainTitleColor = "rgba(39, 22, 95, 255)"
#        self.SecondTitleColor = "rgba(231, 43, 38, 255)"
#        self.SmallTextColor = "rgba(81, 151, 92, 255)"
#        self.AuthorNameColor = "rgba(81, 151, 92, 255)"

class BGProfileSnowWhiteDungeon(BGProfile):
    def __init__(self):
        super().__init__(ID = 53,
                           Priority = 3,
                           sFileName = "snow_white_dungeon")
        self.MainTitleColor = "rgba(32, 89, 161, 255)"
        self.SecondTitleColor = "rgba(32, 89, 161, 255)"
        self.SmallTextColor = "rgba(238, 64, 130, 255)"
        self.AuthorNameColor = "rgba(241, 148, 33, 255)"
        self.AdultsOnly = True

class BGProfileSnowWhiteSpanking(BGProfile):
    def __init__(self):
        super().__init__(ID = 54,
                           Priority = 4,
                           sFileName = "snow_white_spanking")
        self.MainTitleColor = "rgba(131, 58, 110, 255)"
        self.SecondTitleColor = "rgba(131, 58, 110, 255)"
        self.SmallTextColor = "rgba(23, 81, 136, 255)"
        self.AuthorNameColor = "rgba(23, 81, 136, 255)"
        self.AdultsOnly = True

class BGProfileStretchyArms(BGProfile):
    def __init__(self):
        super().__init__(ID = 55,
                           Priority = 2,
                           sFileName = "stretchy_arms")
        self.MainTitleColor = "rgba(227, 31, 15, 255)"
        self.SecondTitleColor = "rgba(227, 31, 15, 255)"
        self.SmallTextColor = "rgba(74, 61, 34, 255)"
        self.AuthorNameColor = "rgba(74, 61, 34, 255)"
        self.AdultsOnly = True

class BGProfileSurroundedByPervs(BGProfile):
    def __init__(self):
        super().__init__(ID = 56,
                           Priority = 3,
                           sFileName = "surrounded_by_pervs")
        self.MainTitleColor = "rgba(66, 103, 86, 255)"
        self.SecondTitleColor = "rgba(196, 107, 28, 255)"
        self.SmallTextColor = "rgba(79, 89, 174, 255)"
        self.AuthorNameColor = "rgba(79, 89, 174, 255)"
        self.AdultsOnly = True

class BGProfileTallWoman(BGProfile):
    def __init__(self):
        super().__init__(ID = 57,
                           Priority = 3,
                           sFileName = "tall_woman")
        self.MainTitleColor = "rgba(77, 172, 243, 255)"
        self.SecondTitleColor = "rgba(77, 172, 243, 255)"
        self.SmallTextColor = "rgba(210, 119, 82, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileTheDevil(BGProfile):
    def __init__(self):
        super().__init__(ID = 58,
                           Priority = 3,
                           sFileName = "the_devil")
        self.MainTitleColor = "rgba(212, 80, 83, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(47, 84, 51, 255)"
        self.AuthorNameColor = "rgba(47, 84, 51, 255)"
        self.AdultsOnly = True

#class BGProfileTrousersDown(BGProfile):
#    def __init__(self):
#        super().__init__(ID = 59,
#                           Priority = 2,
#                           sFileName = "trousers_down")
#        self.MainTitleColor = "rgba(34, 116, 95, 255)"
#        self.SecondTitleColor = "rgba(34, 116, 95, 255)"
#        self.SmallTextColor = "rgba(106, 87, 133, 255)"
#        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileVampire(BGProfile):
    def __init__(self):
        super().__init__(ID = 60,
                           Priority = 2,
                           sFileName = "vampire")
        self.MainTitleColor = "rgba(23, 72, 199, 255)"
        self.SecondTitleColor = "rgba(23, 72, 199, 255)"
        self.SmallTextColor = "rgba(91, 48, 162, 255)"
        self.AuthorNameColor = "rgba(91, 48, 162, 255)"
        self.AdultsOnly = True

class BGProfileUnderBedCreeper(BGProfile):
    def __init__(self):
        super().__init__(ID = 61,
                           Priority = 6,
                           sFileName = "under_bed_creeper")
        self.MainTitleColor = "rgba(130, 43, 39, 255)"
        self.SecondTitleColor = "rgba(199, 131, 61, 255)"
        self.SmallTextColor = "rgba(127, 117, 53, 255)"
        self.AuthorNameColor = "rgba(130, 43, 39, 255)"

class BGProfileVictorianOrgy(BGProfile):
    def __init__(self):
        super().__init__(ID = 62,
                           Priority = 3,
                           sFileName = "victorian_orgy")
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(48, 76, 124, 255)"
        self.AdultsOnly = True

class BGProfileVoyeur(BGProfile):
    def __init__(self):
        super().__init__(ID = 63,
                           Priority = 3,
                           sFileName = "voyeur")
        self.MainTitleColor = "rgba(154, 46, 93, 255)"
        self.SecondTitleColor = "rgba(38, 95, 145, 255)"
        self.SmallTextColor = "rgba(67, 102, 122, 255)"
        self.AuthorNameColor = "rgba(154, 46, 93, 255)"
        self.AdultsOnly = True

class BGProfileWizardPony(BGProfile):
    def __init__(self):
        super().__init__(ID = 64,
                           Priority = 2,
                           sFileName = "wizard_pony")
        self.MainTitleColor = "rgba(244, 63, 233, 255)"
        self.SecondTitleColor = "rgba(244, 63, 233, 255)"
        self.SmallTextColor = "rgba(2, 47, 249, 255)"
        self.AuthorNameColor = "rgba(2, 47, 249, 255)"
        self.AdultsOnly = True

class BGProfileDoggyStyle(BGProfile):
    def __init__(self):
        super().__init__(ID = 65,
                           Priority = 1,
                           sFileName = "doggy_style")
        self.MainTitleColor = "rgba(113, 54, 24, 255)"
        self.SecondTitleColor = "rgba(113, 54, 24, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.AdultsOnly = True

class BGProfileBathhouse(BGProfile):
    def __init__(self):
        super().__init__(ID = 65,
                           Priority = 8,
                           sFileName = "bathhouse")
        self.MainTitleColor = "rgba(30, 102, 139, 255)"
        self.SecondTitleColor = "rgba(150, 85, 45, 255)"
        self.SmallTextColor = "rgba(150, 85, 45, 255)"
        self.AuthorNameColor = "rgba(196, 89, 81, 255)"

class BGProfileJilling(BGProfile):
    def __init__(self):
        super().__init__(ID = 66,
                           Priority = 6,
                           sFileName = "jilling")
        self.MainTitleColor = "rgba(91, 24, 45, 255)"
        self.SecondTitleColor = "rgba(181, 48, 43, 255)"  
        self.SmallTextColor ="rgba(106, 102, 69, 255)"
        self.AuthorNameColor = "rgba(91, 24, 45, 255)"
        self.AdultsOnly = True

class BGProfileBranded(BGProfile):
    def __init__(self):
        super().__init__(ID = 67,
                           Priority = 6,
                           sFileName = "branded")
        self.MainTitleColor = "rgba(66, 75, 132, 255)"
        self.SecondTitleColor = "rgba(200, 82, 65, 255)"  
        self.SmallTextColor ="rgba(54, 50, 74, 255)"
        self.AuthorNameColor = "rgba(66, 75, 132, 255)"
        self.AdultsOnly = True

class BGProfileGrapes(BGProfile):
    def __init__(self):
        super().__init__(ID = 68,
                           Priority = 10,
                           sFileName = "grapes")
        self.MainTitleColor = "rgba(228, 171, 62, 255)"
        self.SecondTitleColor = "rgba(152, 53, 88, 255)"  
        self.SmallTextColor ="rgba(100, 135, 70, 255)"
        self.AuthorNameColor = "rgba(152, 53, 88, 255)"

class BGProfileUnderwater(BGProfile):
    def __init__(self):
        super().__init__(ID = 69,
                           Priority = 10,
                           sFileName = "underwater")
        self.MainTitleColor = "rgba(228, 171, 62, 255)"
        self.SecondTitleColor = "rgba(150, 97, 131, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(228, 171, 62, 255)"

class BGProfileSlaves(BGProfile):
    def __init__(self):
        super().__init__(ID = 70,
                           Priority = 10,
                           sFileName = "slaves")
        self.MainTitleColor = "rgba(169, 61, 55, 255)"
        self.SecondTitleColor = "rgba(212, 167, 84, 255)"  
        self.SmallTextColor ="rgba(50, 158, 194, 255)"
        self.AuthorNameColor = "rgba(50, 158, 194, 255)"

class BGProfileNakedCowboy(BGProfile):
    def __init__(self):
        super().__init__(ID = 71,
                           Priority = 4,
                           sFileName = "naked_cowboy")
        self.MainTitleColor = "rgba(138, 52, 46, 255)"
        self.SecondTitleColor = "rgba(83, 125, 148, 255)"  
        self.SmallTextColor ="rgba(205, 163, 106, 255)"
        self.AuthorNameColor = "rgba(138, 52, 46, 255)",
        self.AdultsOnly = True

class BGProfileTwoGirls(BGProfile):
    def __init__(self):
        super().__init__(ID = 72,
                           Priority = 10,
                           sFileName = "two_girls")
        self.MainTitleColor = "rgba(255, 210, 47, 255)"
        self.SecondTitleColor = "rgba(83, 115, 148, 255)"  
        self.SmallTextColor ="rgba(205, 66, 35, 255)"
        self.AuthorNameColor = "rgba(83, 115, 148, 255)"  

class BGProfileSpaceMonster(BGProfile):
    def __init__(self):
        super().__init__(ID = 72,
                           Priority = 10,
                           sFileName = "space_monster")
        self.MainTitleColor = "rgba(0, 0, 0, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"  
        self.SmallTextColor = "rgba(199, 22, 30, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 

class BGProfileOneEyedAlien(BGProfile):
    def __init__(self):
        super().__init__(ID = 72,
                           Priority = 10,
                           sFileName = "one_eyed_alien")
        self.MainTitleColor = "rgba(219, 103, 122, 255)"
        self.SecondTitleColor = "rgba(72, 146, 145, 255)"  
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 22, 30, 255)" 

class BGProfileSpaceGirl(BGProfile):
    def __init__(self):
        super().__init__(ID = 72,
                           Priority = 10,
                           sFileName = "space_girl")
        self.MainTitleColor = "rgba(48, 66, 138, 255)"
        self.SecondTitleColor = "rgba(48, 66, 138, 255)"
        self.SmallTextColor = "rgba(245, 180, 47, 255)"
        self.AuthorNameColor = "rgba(229, 79, 24, 255)" 

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

            # A multiplier effect for the "SFW" profiles.
            iFactor = 1
            if item.AdultsOnly == False:
                iFactor = 15

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

        #iSFWCount = 0
        #iAdultsOnlyCount = 0 
        #for item in ProfileCountTable:
        #    sTable += str(item[0][1].FileName) + ": " + str(item[1]) + "\n"
        #    if item[1] > 5:
        #        iSFWCount = iSFWCount + item[1]
        #    else:
        #        iAdultsOnlyCount = iAdultsOnlyCount + item[1]
        #sTable += "\n\n"
        #sTable += "# Safe For Work: " + str(iSFWCount) + "\n"
        #sTable += "# Adults Only: " + str(iAdultsOnlyCount) + "\n"

        #print(sTable)

    def RandomProfile(self):
        Profile = []

        if len(self.ProfileList) > 0:
            Profile = choice(self.ProfileList)
                    
        return Profile
          
    def GetProfile(self, iProfileID):
        SelectedProfile = None 
          
        if len(self.ProfileList) > 0:
            for profile in self.ProfileList :
                if profile.ID == iProfileID:
                    SelectedProfile = profile
                    break
                         
        return SelectedProfile
   
def GetBGProfileGenerator(iProfileID = 0, ProfileHistoryQ = None):
    SelectedProfile = None
    print("GetBGProfileGenerator() iProfileID = " + str(iProfileID))

    if ProfileHistoryQ is None:
        ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, iQSize = BGQSIZE)

    ProfSel = ProfileSelector()
    if iProfileID > 0:
        SelectedProfile = ProfSel.GetProfile(iProfileID)
        if SelectedProfile == None:
            SelectedProfile = BGProfile()
    else:
        SelectedProfile = ProfSel.RandomProfile()[1]
        while not ProfileHistoryQ.PushToHistoryQ(SelectedProfile.ID):
            SelectedProfile = ProfSel.RandomProfile()[1]
    
    ProfileHistoryQ.LogHistoryQ()       
    return SelectedProfile
     