#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# background profiles module

import random
from util import *

BGLOGFILEPATH = "title/"
BGLOGFILENAME = "bghistory_q.txt"


class BGProfile():
    def __init__(self, ID = -1, Priority = 1, HeaderType = HeaderType.Harlequin, sHHFileName = "", sPHFileName = ""):
        self.ID = ID
        self.Priority = Priority 
        self.HeaderType = HeaderType 

        self._HHFileName = sHHFileName
        self._PHFileName = sPHFileName
        self._HH_yOffset = 234
        self._PH_yOffset = 127
        
        self.UseHarlequinHeader()

        #init all colors to black
        self.MainTitleColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"

    def UsePlainheader(self):
        self.HeaderType = HeaderType.Plain
        self._UsePlainHeader = True 
        self.BGFileName = self._PHFileName
        self.yOffset = self._PH_yOffset

    def UseHarlequinHeader(self):
        self.HeaderType = HeaderType.Harlequin
        self._UsePlainHeader = False 
        self.BGFileName = self._HHFileName
        self.yOffset = self._HH_yOffset

class BGProfileSaxaphone(BGProfile):
    def __init__(self):
        super().__init__(ID = 1,
                           Priority = 12,
                           sHHFileName = "saxophone_hh.png",
                           sPHFileName = "saxophone_ph.png")
        self.MainTitleColor = "rgba(94, 68, 25, 255)"
        self.SecondTitleColor = "rgba(94, 68, 25, 255)"

class BGProfileBeach(BGProfile):
    def __init__(self):
        super().__init__(ID = 2,
                           Priority = 12,
                           sHHFileName = "beach_hh.png",
                           sPHFileName = "beach_ph.png")
        self.MainTitleColor = "rgba(162, 63, 33, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"

class BGProfileCrotchLevel(BGProfile):
    def __init__(self):
        super().__init__(ID = 3,
                           Priority = 12,
                           sHHFileName = "crotch_level_hh.png",
                           sPHFileName = "crotch_level_ph.png")
        self.MainTitleColor = "rgba(193, 29, 63, 255)"
        self.SecondTitleColor = "rgba(83, 117, 88, 255)"
        self.SmallTextColor = "rgba(112, 162, 193, 255)"

class BGProfileBoatNipples(BGProfile):
    def __init__(self):
        super().__init__(ID = 4,
                           Priority = 12,
                           sHHFileName = "boat_nipples_hh.png",
                           sPHFileName = "boat_nipples_ph.png")
        self.MainTitleColor = "rgba(39, 32, 73, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(39, 32, 73, 255)"
        self.AuthorNameColor = "rgba(39, 32, 73, 255)"

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(ID = 5,
                           Priority = 12,
                           sHHFileName = "blue_car_fire_hh.png",
                           sPHFileName = "blue_car_fire_ph.png")
        self.MainTitleColor = "rgba(132, 41, 55, 255)"
        self.SecondTitleColor = "rgba(132, 41, 55, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"

class BGProfileIndian(BGProfile):
    def __init__(self):
        super().__init__(ID = 6,
                           Priority = 12,
                           sHHFileName = "indian_hh.png",
                           sPHFileName = "indian_ph.png")
        self.MainTitleColor = "rgba(157, 44, 43, 255)"
        self.SecondTitleColor = "rgba(157, 44, 43, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileNakedFabio(BGProfile):
    def __init__(self):
        super().__init__(ID = 7,
                           Priority = 12,
                           sHHFileName = "naked_fabio_hh.png",
                           sPHFileName = "naked_fabio_ph.png")
        self.MainTitleColor = "rgba(238, 146, 134, 255)"
        self.SecondTitleColor = "rgba(238, 146, 134, 255)"
        self.SmallTextColor = "rgba(96, 39, 116, 255)"
        self.AuthorNameColor = "rgba(96, 39, 116, 255)"

class BGProfilePirate(BGProfile):
    def __init__(self):
        super().__init__(ID = 8,
                           Priority = 12,
                           sHHFileName = "pirate_hh.png",
                           sPHFileName = "pirate_ph.png")
        self.MainTitleColor = "rgba(65, 112, 130, 255)"
        self.SecondTitleColor = "rgba(39, 32, 73, 255)"
        self.SmallTextColor = "rgba(191, 77, 59, 255)"
        self.AuthorNameColor = "rgba(65, 112, 130, 255)"

class BGProfileAquaTopless(BGProfile):
    def __init__(self):
        super().__init__(ID = 9,
                           Priority = 12,
                           sHHFileName = "aqua_topless_hh.png",
                           sPHFileName = "aqua_topless_ph.png")
        self.MainTitleColor = "rgba(149, 196, 180, 255)"
        self.SecondTitleColor = "rgba(108, 80, 145, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileGay(BGProfile):
    def __init__(self):
        super().__init__(ID = 10,
                           Priority = 12,
                           sHHFileName = "gay_hh.png",
                           sPHFileName = "gay_ph.png")
        self.MainTitleColor = "rgba(189, 109, 65, 255)"
        self.SecondTitleColor = "rgba(189, 109, 65, 255)"
        self.SmallTextColor = "rgba(108, 145, 51, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileSunset(BGProfile):
    def __init__(self):
        super().__init__(ID = 11,
                           Priority = 12,
                           sHHFileName = "sunset_hh.png",
                           sPHFileName = "sunset_ph.png")
        self.MainTitleColor = "rgba(178, 27, 44, 255)"
        self.SecondTitleColor = "rgba(178, 27, 44, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileField(BGProfile):
    def __init__(self):
        super().__init__(ID = 12,
                           Priority = 12,
                           sHHFileName = "field_hh.png",
                           sPHFileName = "field_ph.png")
        self.MainTitleColor = "rgba(214, 149, 123, 255)"
        self.SecondTitleColor = "rgba(139, 121, 171, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileRedVelvet(BGProfile):
    def __init__(self):
        super().__init__(ID = 13,
                           Priority = 12,
                           sHHFileName = "red_velvet_hh.png",
                           sPHFileName = "red_velvet_ph.png")
        self.MainTitleColor = "rgba(181,55, 47, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileRedAndPurple(BGProfile):
    def __init__(self):
        super().__init__(ID = 14,
                           Priority = 12,
                           sHHFileName = "red_and_purple_hh.png",
                           sPHFileName = "red_and_purple_ph.png")
        self.MainTitleColor = "rgba(209, 91, 56, 255)"
        self.SecondTitleColor = "rgba(209, 91, 56, 255)"
        self.SmallTextColor = "rgba(174, 95, 160, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileBlueCarFire(BGProfile):
    def __init__(self):
        super().__init__(ID = 15,
                           Priority = 12,
                           sHHFileName = "blue_car_fire_hh.png",
                           sPHFileName = "blue_car_fire_ph.png")
        self.MainTitleColor = "rgba(132,41, 55, 255)"
        self.SecondTitleColor = "rgba(181,55, 47, 255)"
        self.SmallTextColor = "rgba(6, 51, 103, 255)"
        self.AuthorNameColor = "rgba(6, 51, 103, 255)"

class BGProfileBlueDress(BGProfile):
    def __init__(self):
        super().__init__(ID = 16,
                           Priority = 12,
                           sHHFileName = "blue_dress_hh.png",
                           sPHFileName = "blue_dress_ph.png")
        self.MainTitleColor = "rgba(181, 79, 75, 255)"
        self.SecondTitleColor = "rgba(181, 79, 75, 255)"
        self.SmallTextColor = "rgba(1, 23, 244, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileDarkBlueFireSuit(BGProfile):
    def __init__(self):
        super().__init__(ID = 17,
                           Priority = 12,
                           sHHFileName = "dark_blue_fire_suit_hh.png",
                           sPHFileName = "dark_blue_fire_suit_ph.png")
        self.MainTitleColor = "rgba(173, 84, 69, 255)"
        self.SecondTitleColor = "rgba(173, 84, 69, 255)"
        self.SmallTextColor = "rgba(53, 68, 89, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileDark(BGProfile):
    def __init__(self):
        super().__init__(ID = 18,
                           Priority = 12,
                           sHHFileName = "dark_hh.png",
                           sPHFileName = "dark_ph.png")
        self.MainTitleColor = "rgba(84, 77, 93, 255)"
        self.SecondTitleColor = "rgba(84, 77, 93, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileGold(BGProfile):
    def __init__(self):
        super().__init__(ID = 19,
                           Priority = 12,
                           sHHFileName = "gold_hh.png",
                           sPHFileName = "gold_ph.png")
        self.MainTitleColor = "rgba(106, 118, 47, 255)"
        self.SecondTitleColor = "rgba(106, 118, 47, 255)"
        self.SmallTextColor = "rgba(106, 118, 47, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileModernBedroom(BGProfile):
    def __init__(self):
        super().__init__(ID = 20,
                           Priority = 12,
                           sHHFileName = "modern_bedroom_hh.png",
                           sPHFileName = "modern_bedroom_ph.png")
        self.MainTitleColor = "rgba(143, 137, 104, 255)"
        self.SecondTitleColor = "rgba(177, 119, 123, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(143, 137, 104, 255)"

class BGProfileShipRomance(BGProfile):
    def __init__(self):
        super().__init__(ID = 21,
                           Priority = 12,
                           sHHFileName = "ship_romance_hh.png",
                           sPHFileName = "ship_romance_ph.png")
        self.MainTitleColor = "rgba(75, 125, 152, 255)"
        self.SecondTitleColor = "rgba(75, 125, 152, 255)"
        self.SmallTextColor = "rgba(200, 159, 193, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileChamberPot(BGProfile):
    def __init__(self):
        super().__init__(ID = 22,
                           Priority = 3,
                           sHHFileName = "chamber_pot_hh.png",
                           sPHFileName = "chamber_pot_ph.png")
        self.MainTitleColor = "rgba(198, 94, 21, 255)"
        self.SecondTitleColor = "rgba(198, 94, 21, 255)"
        self.SmallTextColor = "rgba(170, 60, 133, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileChastityBelt(BGProfile):
    def __init__(self):
        super().__init__(ID = 23,
                           Priority = 3,
                           sHHFileName = "chastity_belt_hh.png",
                           sPHFileName = "chastity_belt_ph.png")
        self.MainTitleColor = "rgba(85, 89, 177, 255)"
        self.SecondTitleColor = "rgba(155, 36, 45, 255)"
        self.SmallTextColor = "rgba(6, 60, 86, 255)"
        self.AuthorNameColor = "rgba(85, 89, 177, 255)"

class BGProfileCowgirlDominatrix(BGProfile):
    def __init__(self):
        super().__init__(ID = 24,
                           Priority = 3,
                           sHHFileName = "cowgirl_dominatrix_hh.png",
                           sPHFileName = "cowgirl_dominatrix_ph.png")
        self.MainTitleColor = "rgba(19, 37, 113, 255)"
        self.SecondTitleColor = "rgba(19, 37, 113, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(199, 149, 60, 255)"

class BGProfileDickNose(BGProfile):
    def __init__(self):
        super().__init__(ID = 25,
                           Priority = 3,
                           sHHFileName = "dick_nose_hh.png",
                           sPHFileName = "dick_nose_hh.png")
        self.MainTitleColor = "rgba(32, 124, 207, 255)"
        self.SecondTitleColor = "rgba(225, 47, 37, 255)"
        self.SmallTextColor = "rgba(198, 78, 107, 255)"
        self.AuthorNameColor = "rgba(225, 47, 37, 255)"

class BGProfileHandsAndKnees(BGProfile):
    def __init__(self):
        super().__init__(ID = 26,
                           Priority = 4,
                           sHHFileName = "hands_and_knees_hh.png",
                           sPHFileName = "hands_and_knees_ph.png")
        self.MainTitleColor = "rgba(210, 136, 53, 255)"
        self.SecondTitleColor = "rgba(210, 136, 53, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileHarem(BGProfile):
    def __init__(self):
        super().__init__(ID = 27,
                           Priority = 3,
                           sHHFileName = "harem_hh.png",
                           sPHFileName = "harem_ph.png")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(62, 162, 167, 255)"
        self.AuthorNameColor = "rgba(62, 162, 167, 255)"

class BGProfileHotCops(BGProfile):
    def __init__(self):
        super().__init__(ID = 28,
                           Priority = 3,
                           sHHFileName = "hot_cops_hh.png",
                           sPHFileName = "hot_cops_ph.png")
        self.MainTitleColor = "rgba(107, 173, 53, 255)"
        self.SecondTitleColor = "rgba(107, 173, 53, 255)"
        self.SmallTextColor = "rgba(184, 160, 43, 255)"
        self.AuthorNameColor = "rgba(184, 160, 43, 255)"

class BGProfileIndecentProp(BGProfile):
    def __init__(self):
        super().__init__(ID = 29,
                           Priority = 3,
                           sHHFileName = "indecent_prop_hh.png",
                           sPHFileName = "indecent_prop_ph.png")
        self.MainTitleColor = "rgba(186, 155, 47, 255)"
        self.SecondTitleColor = "rgba(113, 25, 24, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(186, 155, 47, 255)"

class BGProfileLadyBottom(BGProfile):
    def __init__(self):
        super().__init__(ID = 31,
                           Priority = 3,
                           sHHFileName = "lady_bottom_hh.png",
                           sPHFileName = "lady_bottom_ph.png")
        self.MainTitleColor = "rgba(15, 84, 120, 255)"
        self.SecondTitleColor = "rgba(15, 84, 120, 255)"
        self.SmallTextColor = "rgba(88, 105, 73, 255)"
        self.AuthorNameColor = "rgba(88, 105, 73, 255)"

class BGProfileLesbianVampires(BGProfile):
    def __init__(self):
        super().__init__(ID = 32,
                           Priority = 3,
                           sHHFileName = "lesbian_vampires_hh.png",
                           sPHFileName = "lesbian_vampires_ph.png")
        self.MainTitleColor = "rgba(123, 83, 137, 255)"
        self.SecondTitleColor = "rgba(123, 83, 137, 255)"
        self.SmallTextColor = "rgba(212, 1, 3, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileMaleSub(BGProfile):
    def __init__(self):
        super().__init__(ID = 33,
                           Priority = 3,
                           sHHFileName = "male_sub_hh.png",
                           sPHFileName = "male_sub_hh.png")
        self.MainTitleColor = "rgba(26, 79, 155, 255)"
        self.SecondTitleColor = "rgba(26, 79, 155, 255)"
        self.SmallTextColor = "rgba(131, 149, 93, 255)"
        self.AuthorNameColor = "rgba(200, 114, 184, 255)"

class BGProfileMoonBoob(BGProfile):
    def __init__(self):
        super().__init__(ID = 34,
                           Priority = 3,
                           sHHFileName = "moon_boob_hh.png",
                           sPHFileName = "moon_boob_ph.png")
        self.MainTitleColor = "rgba(186, 51, 57, 255)"
        self.SecondTitleColor = "rgba(186, 51, 57, 255)"
        self.SmallTextColor = "rgba(31, 51, 82, 255)"
        self.AuthorNameColor = "rgba(224, 183, 108, 255)"

class BGProfileNaughtyBuddha(BGProfile):
    def __init__(self):
        super().__init__(ID = 35,
                           Priority = 2,
                           sHHFileName = "naughty_buddha_hh.png",
                           sPHFileName = "naughty_buddha_ph.png")
        self.MainTitleColor = "rgba(9, 71, 161, 255)"
        self.SecondTitleColor = "rgba(9, 71, 161, 255)"
        self.SmallTextColor = "rgba(21, 85, 76, 255)"
        self.AuthorNameColor = "rgba(209, 155, 14, 255)"

class BGProfilePervyDummy(BGProfile):
    def __init__(self):
        super().__init__(ID = 36,
                           Priority = 3,
                           sHHFileName = "pervy_dummy_hh.png",
                           sPHFileName = "pervy_dummy_ph.png")
        self.MainTitleColor = "rgba(196, 50, 45, 255)"
        self.SecondTitleColor = "rgba(196, 50, 45, 255)"
        self.SmallTextColor = "rgba(123, 77, 151, 255)"
        self.AuthorNameColor = "rgba(123, 77, 151, 255)"

class BGProfilePoodleBondage(BGProfile):
    def __init__(self):
        super().__init__(ID = 37,
                           Priority = 3,
                           sHHFileName = "poodle_bondage_hh.png",
                           sPHFileName = "poodle_bondage_ph.png")
        self.MainTitleColor = "rgba(119, 10, 7, 255)"
        self.SecondTitleColor = "rgba(119, 10, 7, 255)"
        self.SmallTextColor = "rgba(83, 84, 141, 255)"
        self.AuthorNameColor = "rgba(83, 84, 141, 255)"

class BGProfileScaryMirror(BGProfile):
    def __init__(self):
        super().__init__(ID = 38,
                           Priority = 3,
                           sHHFileName = "scary_mirror_hh.png",
                           sPHFileName = "scary_mirror_ph.png")
        self.MainTitleColor = "rgba(202, 141, 14, 255)"
        self.SecondTitleColor = "rgba(202, 141, 14, 255)"
        self.SmallTextColor = "rgba(62, 122, 79, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileSkeleton(BGProfile):
    def __init__(self):
        super().__init__(ID = 39,
                           Priority = 2,
                           sHHFileName = "skeleton_hh.png",
                           sPHFileName = "skeleton_ph.png")
        self.MainTitleColor = "rgba(157, 16, 16, 255)"
        self.SecondTitleColor = "rgba(157, 16, 16, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileSnowWhiteSevenDwarves(BGProfile):
    def __init__(self):
        super().__init__(ID = 40,
                           Priority = 2,
                           sHHFileName = "snow_white_7_dwarves_hh.png",
                           sPHFileName = "snow_white_7_dwarves_ph.png")
        self.MainTitleColor = "rgba(52, 117, 47, 255)"
        self.SecondTitleColor = "rgba(52, 117, 47, 255)"
        self.SmallTextColor = "rgba(30, 63, 139, 255)"
        self.AuthorNameColor = "rgba(30, 63, 139, 255)"

class BGProfileSnowWhiteAss(BGProfile):
    def __init__(self):
        super().__init__(ID = 41,
                           Priority = 3,
                           sHHFileName = "snow_white_ass_hh.png",
                           sPHFileName = "snow_white_ass_ph.png")
        self.MainTitleColor = "rgba(39, 22, 95, 255)"
        self.SecondTitleColor = "rgba(231, 43, 38, 255)"
        self.SmallTextColor = "rgba(81, 151, 92, 255)"
        self.AuthorNameColor = "rgba(81, 151, 92, 255)"

class BGProfileSnowWhiteDungeon(BGProfile):
    def __init__(self):
        super().__init__(ID = 42,
                           Priority = 3,
                           sHHFileName = "snow_white_dungeon_hh.png",
                           sPHFileName = "snow_white_dungeon_ph.png")
        self.MainTitleColor = "rgba(32, 89, 161, 255)"
        self.SecondTitleColor = "rgba(32, 89, 161, 255)"
        self.SmallTextColor = "rgba(238, 64, 130, 255)"
        self.AuthorNameColor = "rgba(241, 148, 33, 255)"

class BGProfileSnowWhiteSpanking(BGProfile):
    def __init__(self):
        super().__init__(ID = 43,
                           Priority = 4,
                           sHHFileName = "snow_white_spanking_hh.png",
                           sPHFileName = "snow_white_spanking_ph.png")
        self.MainTitleColor = "rgba(131, 58, 110, 255)"
        self.SecondTitleColor = "rgba(131, 58, 110, 255)"
        self.SmallTextColor = "rgba(23, 81, 136, 255)"
        self.AuthorNameColor = "rgba(23, 81, 136, 255)"

class BGProfileStretchyArms(BGProfile):
    def __init__(self):
        super().__init__(ID = 44,
                           Priority = 2,
                           sHHFileName = "stretchy_arms_hh.png",
                           sPHFileName = "stretchy_arms_ph.png")
        self.MainTitleColor = "rgba(227, 31, 15, 255)"
        self.SecondTitleColor = "rgba(227, 31, 15, 255)"
        self.SmallTextColor = "rgba(74, 61, 34, 255)"
        self.AuthorNameColor = "rgba(74, 61, 34, 255)"

class BGProfileSurroundedByPervs(BGProfile):
    def __init__(self):
        super().__init__(ID = 45,
                           Priority = 3,
                           sHHFileName = "surrounded_by_pervs_hh.png",
                           sPHFileName = "surrounded_by_pervs_hh.png")
        self.MainTitleColor = "rgba(66, 103, 86, 255)"
        self.SecondTitleColor = "rgba(196, 107, 28, 255)"
        self.SmallTextColor = "rgba(79, 89, 174, 255)"
        self.AuthorNameColor = "rgba(79, 89, 174, 255)"

class BGProfileTallWoman(BGProfile):
    def __init__(self):
        super().__init__(ID = 46,
                           Priority = 3,
                           sHHFileName = "tall_woman_hh.png",
                           sPHFileName = "tall_woman_ph.png")
        self.MainTitleColor = "rgba(77, 172, 243, 255)"
        self.SecondTitleColor = "rgba(77, 172, 243, 255)"
        self.SmallTextColor = "rgba(210, 119, 82, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileTheDevil(BGProfile):
    def __init__(self):
        super().__init__(ID = 47,
                           Priority = 3,
                           sHHFileName = "the_devil_hh.png",
                           sPHFileName = "the_devil_ph.png")
        self.MainTitleColor = "rgba(212, 80, 83, 255)"
        self.SecondTitleColor = "rgba(0, 0, 0, 255)"
        self.SmallTextColor = "rgba(47, 84, 51, 255)"
        self.AuthorNameColor = "rgba(47, 84, 51, 255)"

class BGProfileTrousersDown(BGProfile):
    def __init__(self):
        super().__init__(ID = 48,
                           Priority = 2,
                           sHHFileName = "trousers_down_hh.png",
                           sPHFileName = "trousers_down_ph.png")
        self.MainTitleColor = "rgba(34, 116, 95, 255)"
        self.SecondTitleColor = "rgba(34, 116, 95, 255)"
        self.SmallTextColor = "rgba(106, 87, 133, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

class BGProfileVampire(BGProfile):
    def __init__(self):
        super().__init__(ID = 49,
                           Priority = 2,
                           sHHFileName = "vampire_hh.png",
                           sPHFileName = "vampire_hh.png")
        self.MainTitleColor = "rgba(23, 72, 199, 255)"
        self.SecondTitleColor = "rgba(23, 72, 199, 255)"
        self.SmallTextColor = "rgba(91, 48, 162, 255)"
        self.AuthorNameColor = "rgba(91, 48, 162, 255)"

class BGProfileUnderBedCreeper(BGProfile):
    def __init__(self):
        super().__init__(ID = 50,
                           Priority = 4,
                           sHHFileName = "under_bed_creeper_hh.png",
                           sPHFileName = "under_bed_creeper_ph.png")
        self.MainTitleColor = "rgba(130, 43, 39, 255)"
        self.SecondTitleColor = "rgba(199, 131, 61, 255)"
        self.SmallTextColor = "rgba(127, 117, 53, 255)"
        self.AuthorNameColor = "rgba(130, 43, 39, 255)"

class BGProfileUnderVictorianOrgy(BGProfile):
    def __init__(self):
        super().__init__(ID = 51,
                           Priority = 3,
                           sHHFileName = "victorian_orgy_hh.png",
                           sPHFileName = "victorian_orgy_ph.png")
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.MainTitleColor = "rgba(79, 117, 188, 255)"
        self.SmallTextColor = "rgba(171, 27, 108, 255)"
        self.AuthorNameColor = "rgba(48, 76, 124, 255)"

class BGProfileVoyeur(BGProfile):
    def __init__(self):
        super().__init__(ID = 52,
                           Priority = 3,
                           sHHFileName = "voyeur_hh.png",
                           sPHFileName = "voyeur_ph.png")
        self.MainTitleColor = "rgba(154, 46, 93, 255)"
        self.SecondTitleColor = "rgba(38, 95, 145, 255)"
        self.SmallTextColor = "rgba(67, 102, 122, 255)"
        self.AuthorNameColor = "rgba(154, 46, 93, 255)"

class BGProfileWizardPony(BGProfile):
    def __init__(self):
        super().__init__(ID = 53,
                           Priority = 2,
                           sHHFileName = "wizard_pony_hh.png",
                           sPHFileName = "wizard_pony_ph.png")
        self.MainTitleColor = "rgba(244, 63, 233, 255)"
        self.SecondTitleColor = "rgba(244, 63, 233, 255)"
        self.SmallTextColor = "rgba(2, 47, 249, 255)"
        self.AuthorNameColor = "rgba(2, 47, 249, 255)"

class BGProfileDoggyStyle(BGProfile):
    def __init__(self):
        super().__init__(ID = 54,
                           Priority = 1,
                           sHHFileName = "doggy_style_hh.png",
                           sPHFileName = "doggy_style_ph.png")
        self.MainTitleColor = "rgba(113, 54, 24, 255)"
        self.SecondTitleColor = "rgba(113, 54, 24, 255)"
        self.SmallTextColor = "rgba(0, 0, 0, 255)"
        self.AuthorNameColor = "rgba(0, 0, 0, 255)"

# this is for debugging bgprofile frequency. delete later.
def indexof(list, searchobj):
    iIndex = 0
    bFound = False

    while iIndex < len(list):
        if list[iIndex][0][1].BGFileName == searchobj[1].BGFileName:
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
            for x in range(0, item.Priority):
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

        #for item in ProfileCountTable:
        #    sTable += str(item[0][1].BGFileName) + ": " + str(item[1]) + "\n"
        #sTable += "\n"

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

    if ProfileHistoryQ is None:
        ProfileHistoryQ = HistoryQWithLog(BGLOGFILEPATH + BGLOGFILENAME, iQSize = 15)

    ProfSel = ProfileSelector()
    if iProfileID > 0:
        SelectedProfile = ProfSel.GetProfile(iProfileID)
        if SelectedProfile == None:
            SelectedProfile = BGProfile()
    else:
        SelectedProfile = ProfSel.RandomProfile()[1]
        while not ProfileHistoryQ.PushToHistoryQ(SelectedProfile.ID):
            SelectedProfile = ProfSel.RandomProfile()[1]
          
    return SelectedProfile
     