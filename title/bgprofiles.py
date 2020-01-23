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
                           Priority = 4,
                           sHHFileName = "saxophone_hh.png",
                           sPHFileName = "saxophone_ph.png")
        self.MainTitleColor = "rgba(94, 68, 25, 255)"
        self.SecondTitleColor = "rgba(94, 68, 25, 255)"

class ProfileSelector():
    def __init__(self):
        self.ProfileList = [] 

        for subclass in BGProfile.__subclasses__():
            item = subclass()
            for x in range(0, item.Priority):
                self.ProfileList.append([item.ID, item])
               
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
     