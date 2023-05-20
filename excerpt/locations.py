#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Locations module

from random import *
#from enum import * 

import excerpt.util as exutil
from util import *
import excerpt.bodyparts
import excerpt.clothes as clothes

Loc_FemWardrobe = clothes.FemWardrobe()
Loc_MaleWardrobe = clothes.MaleWardrobe()

class Location():
    def __init__(self, LocMan = None, LocWoman = None):
        if LocMan is None:
            LocMan = excerpt.bodyparts.Man()
        if LocWoman is None:
            LocWoman = excerpt.bodyparts.Woman()

        self.Man = LocMan
        self.Woman = LocWoman

        self.FemWardrobe = Loc_FemWardrobe
        self.MaleWardrobe = Loc_MaleWardrobe
        self.Name = ""
        self.NamePrep = ""
        self.Loc = exutil.LocInOutType.Indoors
        self.BeginDesc = ""
        self.EndDesc = ""
        self.BentOver = ""
        self.KneelingOn = ""
        self.SittingOn = ""
        self.LyingOn = ""
        self.Ground = "ground"
        self.Despite = ""
        self.MaleTopClothing = self.MaleWardrobe.Tshirt.RandomDescription(bLongDesc = False)
        self.MaleBottomClothing = self.MaleWardrobe.Jeans.RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
    def RemoveMaleClothing(self):
        sTakeItOff = ""

        ExposedParts = None
        if CoinFlip():
            ExposedParts = self.Man.Penis
        else:
            ExposedParts = self.Man.Ass
        sExposedParts = ExposedParts.RandomDescription(bLongDesc = False)
           
        if not self.MaleTopClothing == "":
            sTakeItOff = "stripped off his " + self.MaleTopClothing + " and pulled down his " + self.MaleBottomClothing  + " exposing his " + sExposedParts
        elif not self.MaleBottomClothing == "":
            sTakeItOff = "pulled down his " + self.MaleBottomClothing + " exposing his " + sExposedParts
        else: 
            sTakeItOff = "was naked, his " + sExposedParts + " on full display"

        #sTakeItOff += excerpt.bodyparts.Penis.RandomDescription(bLongDesc = False)     
          
        return sTakeItOff
               
    def RemoveFemaleClothing(self):
        Vagina = self.Woman.Vagina
        Ass = self.Woman.Ass
        Breasts = self.Woman.Breasts

        sTakeItOff = ""
          
        if not self.FemaleTopClothing == "" and not self.FemaleBottomClothing == "":
            if CoinFlip():
                sTakeItOff += "pulled off her " + self.FemaleTopClothing + " and slipped out of her " + self.FemaleBottomClothing + ", "
                if CoinFlip():
                        sTakeItOff += "baring her " + Vagina.RandomDescription(bLongDesc = False)
                else:
                        sTakeItOff += "revealing her " + Ass.RandomDescription(bLongDesc = False)
            else:
                sTakeItOff += "slipped out of her " + self.FemaleBottomClothing + " and pulled off her " + self.FemaleTopClothing + ", revealing her " + Breasts.RandomDescription(bLongDesc = False)
        elif not self.FemaleBottomClothing == "":
            if CoinFlip():
                sTakeItOff += "pulled down her " + self.FemaleBottomClothing + ", baring her " + Vagina.RandomDescription(bLongDesc = False)
            else:
                sTakeItOff += "pulled down her " + self.FemaleBottomClothing + ", revealing her " + Ass.RandomDescription(bLongDesc = False)
        elif not self.FemaleTopClothing == "":
            sTakeItOff += "pulled off her " + self.FemaleTopClothing + ", revealing her " + Breasts.RandomDescription(bLongDesc = False)
        else:
            sTakeItOff += "was naked, her " + Breasts.RandomDescription(bLongDesc = False) + " and "
            if CoinFlip():
                sTakeItOff += Ass.RandomDescription(bLongDesc = False)
            else:
                sTakeItOff += Vagina.RandomDescription(bLongDesc = False)
            sTakeItOff += " exposed in all their glory"
               
        return sTakeItOff
               
    def PutOnMaleClothing(self, bBottomOnly = False):
        sPutItOn = ""
          
        if not self.MaleTopClothing == "":
            if bBottomOnly:
                sPutItOn = "pulled his " + self.MaleBottomClothing + " up"
            else:
                sPutItOn = "pulled his " + self.MaleBottomClothing + " up and put on his " + self.MaleTopClothing
        elif not self.MaleBottomClothing == "":
            sPutItOn = "pulled up his " + self.MaleBottomClothing
        else:
            sPutItOn = "began to pull on some clothes"
               
        return sPutItOn
          
    def PutOnFemaleClothing(self, bBottomOnly = False):
        sPutItOn = ""
          
        if not self.FemaleTopClothing == "":
            if bBottomOnly:
                sPutItOn = "wiggled into her " + self.FemaleBottomClothing
            else:
                sPutItOn = "wiggled into her " + self.FemaleBottomClothing + " and then he helped her into her " + self.FemaleTopClothing
        elif not self.FemaleBottomClothing == "":
            sPutItOn = "wiggled into her " + self.FemaleBottomClothing
        else:
            sPutItOn = "began to pull on some clothes"
               
        return sPutItOn
          
class PublicLocation(Location):
    PubPriv = exutil.LocPubPrivType.Public
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)
        
        self.HurryReason = ""
        self.Caught = ""
        self.Excuse = ""
        self.Consequence = ""
        self.AuthorityFigure = ""
     
class PrivateLocation(Location):
    PubPriv = exutil.LocPubPrivType.Private

class PublicOutdoors(PublicLocation):
    InOut = exutil.LocInOutType.Outdoors

class PublicIndoors(PublicLocation):
    InOut = exutil.LocInOutType.Indoors

class PrivateOutdoors(PrivateLocation):
    InOut = exutil.LocInOutType.Outdoors

class PrivateIndoors(PrivateLocation):
    InOut = exutil.LocInOutType.Indoors
     
class Alley(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the alley behind the bar"
        self.NamePrep = "in the alley behind the bar"
        self.BeginDesc = "A dim yellow light over the back door of the bar was the only illumination in the alley."
        self.Despite = "their unsavory surroundings"
        self.BentOver = "a stack of pallets"
        self.KneelingOn = "a stack of pallets"
        self.SittingOn = "a stack of pallets"
        self.LyingOn = "a strip of cardboard"
        self.HurryReason = "Someone might see us"
        self.Caught = "'Hey! What's going on over there?' yelled the bartender."
        self.Excuse = "'Don't come back here!' he yelled back."
        self.AuthorityFigure = "the bartender"
        self.Consequence = "as the bartender watched them"
        self.Ground = "the pavement"

class Balcony(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the hotel balcony"
        self.NamePrep = "on the hotel balcony"
        self.BeginDesc = "The city spread out below them and the horizon was blue ocean."
        self.Despite = "the fact that they were exposed to anyone who looked up"
        self.BentOver = "the balcony rail"
        self.KneelingOn = "on a patio chair"
        self.SittingOn = "the broad ledge of the balcony"
        self.LyingOn = "the reclining patio chair"
        self.HurryReason = "What if someone is watching?"
        self.Caught = "'I think those people down there are videoing us with their iPhones!"
        self.Excuse = "'Let's give them a show, baby!' he replied."
        self.AuthorityFigure = "a crowd"
        self.Consequence = "a small crowd gathered to watch them"
        self.Ground = "ground"
        self.MaleTopClothing = ""
        self.MaleBottomClothing = self.MaleWardrobe.GetUnderwear().RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.Bra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)

class Beach(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the beach"
        self.NamePrep = "at the beach"
        self.BeginDesc = "A hot sun shone down as blue waves lapped at the sand."
        self.Despite = "the sand that got into every crack"
        self.BentOver = "the sand dune"
        self.KneelingOn = "on the beach towel"
        self.SittingOn = "on the beach towel"
        self.LyingOn = "on the beach towel"
        self.HurryReason = "The lifeguard will be here any minute"
        self.Caught = "'What are you doing?' shouted the lifeguard."
        self.Excuse = "'We're just putting on lotion!' he replied."
        self.AuthorityFigure = "the lifeguard"
        self.Consequence = "the lifeguard watched"
        self.Ground = "tiled floor"
        self.MaleTopClothing = ""
        if CoinFlip():
            self.MaleBottomClothing = self.MaleWardrobe.Trunks.RandomDescription(bLongDesc = False)
        else:
            self.MaleBottomClothing = self.MaleWardrobe.Speedo.RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
     
class Boat(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the boat"
        self.NamePrep = "on a boat"
        self.BeginDesc = "The boat rocked gently in the open water. It was a perfect day."
        self.Despite = "the sun beating down on them"
        self.BentOver = "the side rail"
        self.KneelingOn = "on the stern of the boat"
        self.SittingOn = "on the stern of the boat"
        self.LyingOn = "the deck"
        self.Ground = "deck"
        self.MaleTopClothing = ""
        if CoinFlip():
            self.MaleBottomClothing = self.MaleWardrobe.Trunks.RandomDescription(bLongDesc = False)
        else:
            self.MaleBottomClothing = self.MaleWardrobe.Speedo.RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
     
class Bedroom(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the bedroom"
        self.NamePrep = "in the bedroom"
        self.Despite = "some fumbling awkwardness"
        self.BeginDesc = "Candles were lit all around the four-poster king-sized bed."
        self.BentOver = "the end of the bed"
        self.KneelingOn = "the bed"
        self.SittingOn = "a stack of cushions"
        self.LyingOn = "the king-sized bed"
        self.Ground = "the thick comforter"
        self.FemaleTopClothing = self.FemWardrobe.Bra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class CampingTent(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "a tent"
        self.NamePrep = "in a tent"
        self.Despite = "the thin canvas walls of the tent"
        self.BeginDesc = "The tent was just big enough for two."
        self.BentOver = "her heavy backpack"
        self.KneelingOn = "a bedroll"
        self.SittingOn = "a bedroll"
        self.LyingOn = "a sleeping bag"
        self.Ground = "the thick sleeping bag"
        self.FemaleTopClothing = "cute little sweater"
        self.FemaleBottomClothing = self.FemWardrobe.Jeans.RandomDescription(bLongDesc = False)
     
class CarBackseat(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the backseat of the car"
        self.NamePrep = "in the backseat of the car"
        self.BeginDesc = "The couple scrambled into the backseat of the car."
        self.Despite = "the extremely tight space"
        self.BentOver = "the back seat"
        self.KneelingOn = "on the back seat"
        self.SittingOn = "on the back seat"
        self.LyingOn = "on the back seat"
        self.HurryReason = "I hear someone pulling up"
        self.Caught = "'There was a knock on the steamed-up window. 'Everything OK in there?' asked a cop."
        self.Excuse = "'Just a little engine trouble,' he replied."
        self.AuthorityFigure = "a policeman"
        self.Consequence = "the cop shone his flashlight through the window"
        self.Ground = "leather upholstery"
        self.FemaleTopClothing = self.FemWardrobe.Blouse.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.ShortSkirt.RandomDescription(bLongDesc = False)
     
class Church(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name = "the church"
        self.NamePrep = "in the church"
        self.BeginDesc = "Colored light flooded through a stained glass window."
        self.Despite = "the sacred atmosphere"
        self.BentOver = "the pulpit"
        self.KneelingOn = "on the altar steps"
        self.SittingOn = "on a pew"
        self.LyingOn = "on a pew"
        self.HurryReason = "someone will catch us in our sin"
        self.Caught = "'Whis is the meaning of this?' shouted the minister."
        self.AuthorityFigure = "the minister"
        self.Excuse = "'We were just praying!' he replied."
        self.Consequence = "as the minister looked on in horror"
        self.Ground = "soft carpet"
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class Classroom(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the classroom"
        self.NamePrep ="in the classroom"
        self.BeginDesc = "The blackboard was covered in notes and the rows of student desks were straight and orderly."
        self.Despite = "the threat of being caught"
        self.BentOver = "the teacher's desk"
        self.KneelingOn = "on a student desk"
        self.SittingOn = "the teacher's desk"
        self.LyingOn = "the teacher's desk"
        self.HurryReason = "someone will catch us"
        self.AuthorityFigure = "someone"
        self.Caught ="Suddenly the door opened. A male student carrying a textbook walked in."
        self.Excuse = "'This isn't what it looks like!' he said."
        self.Consequence = "the student tugged feverishly at his crotch"
        self.Ground = "the floor"
        self.FemaleTopClothing = self.FemWardrobe.Blouse.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.ShortSkirt.RandomDescription(bLongDesc = False)
     
class ClubParkingLot(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the club parking lot"
        self.NamePrep ="on the hood of the car in the club parking lot"
        self.BeginDesc = "The night was tinged with neon light and there was a distant sound of thumping bass."
        self.Despite = "the fact that they were in a parking lot"
        self.BentOver = "the hood of a car"
        self.KneelingOn = "the hood of a car"
        self.SittingOn = "the hood of a car"
        self.LyingOn = "the hood of the car"
        self.HurryReason = "Someone might see us"
        self.Caught ="'Hey! What's going on over there?' yelled the bouncer."
        self.Excuse = "'Just a little engine trouble,' he replied."
        self.AuthorityFigure = "a bouncer"
        self.Consequence = "as the bouncer watched them"
        self.Ground = "the hood of the car"
        self.FemaleTopClothing = self.FemWardrobe.Blouse.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.ShortSkirt.RandomDescription(bLongDesc = False)
     
class Den(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the den"
        self.NamePrep ="in the den"
        self.Loc = exutil.LocInOutType.Indoors
        self.Despite = "a little shyness"
        self.BeginDesc = "A fire was crackling in the fireplace of the cozy den."
        self.BentOver = "the arm of the couch"
        self.KneelingOn = "the sofa"
        self.SittingOn = "a thick cushion"
        self.LyingOn = "the sofa"
        self.Ground = "the thick fur rug"
        self.FemaleTopClothing = "tight leather corset"
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class DoctorsOffice(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the doctor's office"
        self.NamePrep ="in the doctor's office"
        self.BeginDesc = "The examination table in the doctor's office had a clean sheet of paper on it."
        self.Despite = "the danger of being heard"
        self.BentOver = "the examination table"
        self.KneelingOn = "the examination table"
        self.LyingOn = "the examination table"
        self.SittingOn = "the examination table"
        self.HurryReason = "a nurse will hear us"
        self.Caught ="'Is everyone OK in there?' called a nurse through the door. 'I'm coming in!'"
        self.Excuse = "'It's alright!' he yelled."
        self.AuthorityFigure = "the nurse"
        self.Consequence = "a cute nurse in scrubs looked on in shock"
        self.Ground = "the floor"
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class DormRoom(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the dorm room"
        self.NamePrep ="in the dorm room"
        self.BeginDesc = "The narrow bed took up half the dorm room."
        self.Despite = "the cramped space"
        self.BentOver = "the desk"
        self.KneelingOn = "on the edge of the bed"
        self.SittingOn = "on the edge of the bed"
        self.LyingOn = "on the tiny bed"
        self.Ground = "the thin carpet"
        self.FemaleTopClothing = self.FemWardrobe.Tshirt.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Jeans.RandomDescription(bLongDesc = False)
     
class DressingRoom(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the dressing room"
        self.NamePrep ="in the dressing room"
        self.BeginDesc = "Whispering and giggling, they locked themselves in the dressing room."
        self.Despite = "the danger of being heard"
        self.BentOver = "the bench in the dressing room"
        self.KneelingOn = "on the bench in the dressing room"
        self.LyingOn = "on the floor"
        self.SittingOn = "on the dressing room bench"
        self.HurryReason = "they'll hear us"
        self.Caught ="'Excuse me? Do you need help in there?' called a store clerk."
        self.Excuse = "'Don't come in!' he yelled."
        self.AuthorityFigure = "the store clerk"
        self.Consequence = "the clerk shouted 'I'm calling security'"
        self.Ground = "the carpet"
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class Farm(PrivateOutdoors):     
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the farm"
        self.NamePrep ="on a farm"
        self.Despite = "the mooing of nearby cows"
        self.BeginDesc = "A rambling wood fence encircled a field dotted with hay bales."
        self.BentOver = "a wood fence"
        self.KneelingOn = "a square hay bale"
        self.SittingOn = "a square hay bale" 
        self.LyingOn = "the lush green grass"
        self.Ground = "the grass"
        self.FemaleTopClothing = self.FemWardrobe.Tshirt.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Jeans.RandomDescription(bLongDesc = False)
        self.MaleTopClothing = self.MaleWardrobe.Tshirt.RandomDescription(bLongDesc = False)
        self.MaleBottomClothing = self.MaleWardrobe.Tshirt.RandomDescription(bLongDesc = False)
     
class Hottub(PrivateOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the hot tub"
        self.NamePrep ="in the hot tub"
        self.Despite = "the heat"
        self.BeginDesc = "They slipped into the warm water of the hot tub."
        self.BentOver = "the side of the tub"
        self.KneelingOn = "the seat in the tub"
        self.SittingOn = "a seat in the tub" 
        self.LyingOn = "the side of the tub"
        self.Ground = "steaming water"
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
        self.MaleTopClothing = ""
        if CoinFlip():
            self.MaleBottomClothing = self.MaleWardrobe.Trunks.RandomDescription(bLongDesc = False)
        else:
            self.MaleBottomClothing = self.MaleWardrobe.Speedo.RandomDescription(bLongDesc = False)
     
class Gym(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the gym"
        self.NamePrep ="at the gym"
        self.BeginDesc = "The mirrors on the wall of the gym reflected their bodies back at them."
        self.Despite = "the sweat which covered their bodies"
        self.BentOver = "a weight bench"
        self.KneelingOn = "on an exercise machine"
        self.SittingOn = "a weight bench"
        self.LyingOn = "a weight bench"
        self.HurryReason = "someone will catch us"
        self.Caught ="A girl wearing a leotard walked in. 'Holy fuck!' the girl said."
        self.Excuse = "'We are just stretching!' he yelled."
        self.Consequence = "the girl with the leotard watched open-mouthed"
        self.AuthorityFigure = "someone"
        self.Ground = "rubber mat"
        self.FemaleTopClothing = self.FemWardrobe.SportsBra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.YogaPants.RandomDescription(bLongDesc = False)
     
class HikingTrail(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the hiking trail"
        self.NamePrep ="on the side of a mountain"
        self.BeginDesc = "The hike up the mountain had been exhausting, but the stunning view was worth it."
        self.Despite = "the dirt and mosquitos"
        self.BentOver = "a large boulder"
        self.KneelingOn = "on a large boulder"
        self.SittingOn = "on a broad, smooth boulder"
        self.LyingOn = "a broad, smooth boulder"
        self.HurryReason = "someone might come up the trail"
        self.Caught ="They heard the crunch of heavy boots and saw that a hiker was rounding the bend of the trail."
        self.Excuse = "'Don't come up here, there's bears!' he called out."
        self.Consequence = "a bearded hiker looked on in surprise"
        self.AuthorityFigure = "a park ranger"
        self.Ground = "the rocky mountainside"
        self.FemaleTopClothing = self.FemWardrobe.SportsBra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = "spandex shorts"
     
class Kitchen(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the kitchen"
        self.NamePrep ="in the kitchen"
        self.BeginDesc = "A pan of bacon was frying on the kitchen stove."
        self.Despite = "the crackling of cooking bacon"
        self.BentOver = "the counter"
        self.KneelingOn = "on a kitchen chair"
        self.SittingOn = "on the kitchen table"
        self.LyingOn = "on the kitchen table"
        self.Ground = "black and white tiled floor"
        self.MaleTopClothing = ""
        self.MaleBottomClothing = self.MaleWardrobe.GetUnderwear().RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.Tshirt.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class Library(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the library"
        self.NamePrep ="in the library"
        self.BeginDesc = "It was quiet and stuffy amongst the stacks."
        self.Despite = "the need for silence"
        self.BentOver = "a stack of books"
        self.KneelingOn = "on a table strewn with books"
        self.SittingOn = "on a study desk"
        self.LyingOn = "a table strewn with books"
        self.HurryReason = "someone will hear us"
        self.Caught ="'Please, you must be quiet!' called out a librarian."
        self.Consequence = "the librarian listened"
        self.Excuse = "'We are just about to check out!' he called back."
        self.AuthorityFigure = "the librarian"
        self.Ground = "soft carpet"
        self.FemaleTopClothing = self.FemWardrobe.Blouse.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.ShortSkirt.RandomDescription(bLongDesc = False)
     
class MassageRoom(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="a massage room"
        self.NamePrep ="in a massage room"
        self.BeginDesc = "Ambient ocean sounds and the smell of incense filled the massage room."
        self.Despite = "the danger of being caught"
        self.BentOver = "the massage table"
        self.KneelingOn = "on the massage table"
        self.SittingOn = "on the massage table"
        self.LyingOn = "on the massage table"
        self.Ground = "soft carpet"
        self.FemaleTopClothing = "towel"
        self.MaleTopClothing = ""
        self.MaleBottomClothing = "towel"
     
class MensRoom(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="men's restroom"
        self.NamePrep ="in the men's restroom"
        self.BeginDesc = "Crude graffiti was scrawled on the walls of the cramped stall."
        self.Despite = "the extremely cramped quarters"
        self.BentOver = "the toilet"
        self.KneelingOn = "on the toilet seat"
        self.SittingOn = "on the toilet"
        self.LyingOn = "on the tiled floor"
        self.HurryReason = "Someone might hear us!"
        self.Caught ="Someone pounded on the door and shouted 'Hurry up!'"
        self.Consequence = "someone called out 'Fuck her good, man'"
        self.AuthorityFigure = "some strange man"
        self.Excuse = "'Busy!' he shouted back."
        self.Ground = "tiled floor"
        self.FemaleTopClothing = self.FemWardrobe.Blouse.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.ShortSkirt.RandomDescription(bLongDesc = False)
     
class MovieTheater(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the movie theater"
        self.NamePrep ="in the movie theater"
        self.BeginDesc = "They had the darkened back row of the movie theater to themselves."
        self.Despite = "being in a public movie theater"
        self.BentOver = "the seat"
        self.KneelingOn = "the seat"
        self.SittingOn = "a seat"
        self.LyingOn = "the theater seats"
        self.HurryReason = "people will notice"
        self.Caught ="The middle aged woman in the row in front of them turned and stared."
        self.AuthorityFigure = "the audience member"
        self.Excuse = "'Just watch the movie!' he snapped."
        self.Consequence = "the woman got up from her seat and stomped out of the theater"
        self.Ground = "the floor"
        self.FemaleTopClothing = "tight sweater"
        self.FemaleBottomClothing = "hip-hugging pants"

class Office(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the office"
        self.NamePrep ="in the office"
        self.BeginDesc = "A large oak desk stood in the center of the corner office."
        self.Despite = "the danger of being caught"
        self.BentOver = "the massive desk"
        self.KneelingOn = "on the boss's desk"
        self.SittingOn = "on the surface of the desk"
        self.LyingOn = "on the boss's desk"
        self.HurryReason = "Someone will catch us!"
        self.Caught ="The door opened and a tall man walked in. 'Fuck, its my boss!' she said."
        self.Consequence = "her boss watched, open-mouthed"
        self.Excuse = "'This isn't what it looks like!' he shouted."
        self.AuthorityFigure = "your boss"
        self.Ground = "carpet"
        self.FemaleTopClothing = self.FemWardrobe.PencilDress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
        self.MaleTopClothing = "dress shirt"
        self.MaleBottomClothing = self.MaleWardrobe.Slacks.RandomDescription(bLongDesc = False)
     
class OpenWindow(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the open window"
        self.NamePrep ="in front of an open window"
        self.BeginDesc = "Sunlight flooded through the large open window that looked down on the street."
        self.Despite = "the open window"
        self.BentOver = "the window sill"
        self.KneelingOn = "on the wide window sill"
        self.SittingOn = "on sofa in front of the window"
        self.LyingOn = "on the the wide window sill"
        self.HurryReason = "the neighbors will see us"
        self.Caught ="'I think the neighbors are watching us!' she said."
        self.AuthorityFigure = "the neighbors"
        self.Excuse = "'Let them,' he replied."
        self.Consequence = "the people next door looked on"
        self.Ground = "thick carpet"
        self.FemaleTopClothing = self.FemWardrobe.Bra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class ParkAfterDark(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the park"
        self.NamePrep ="in the park after sundown"
        self.BeginDesc = "The lush green park was transformed into a place of shadows and secrets in the moonlight."
        self.Despite = "being hidden only by the shadows"
        self.BentOver = "a park bench"
        self.KneelingOn = "the edge of a stone fountain"
        self.SittingOn = "a park bench"
        self.LyingOn = "on the end of a playground slide"
        self.HurryReason = "we'll get caught"
        self.Caught ="A beam of light flicked on. A night watchman was pointing it right at them."
        self.AuthorityFigure = "a night watchman"
        self.Excuse = "'This isn't what it looks like!' he shouted."
        self.Consequence = "the watchman enjoyed the view"
        self.Ground = "the ground"
        self.FemaleTopClothing = "tight sweater"
        self.FemaleBottomClothing = self.FemWardrobe.Jeans.RandomDescription(bLongDesc = False)
     
class ParkBench(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="a park bench"
        self.NamePrep ="on a park bench"
        self.BeginDesc = "There seemed to be no-one nearby the secluded little park-bench."
        self.Despite = "being in a public park"
        self.BentOver = "a park bench"
        self.KneelingOn = "the edge of a park bench"
        self.SittingOn = "a park bench"
        self.LyingOn = "on a park bench"
        self.HurryReason = "we'll get caught"
        self.Caught ="They heard footsteps. A jogger came running around the corner and pulled up short."
        self.AuthorityFigure = "a jogger"
        self.Excuse = "'I'm not stopping now, baby!' he panted."
        self.Consequence = "the jogger looked on with surprise"
        self.Ground = "the ground"
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
     
class PoolPatio(PrivateOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the pool patio"
        self.NamePrep ="beside the pool"
        self.Despite = "some fumbling awkwardness"
        self.BeginDesc = "The sun was high in the sky and the pool water looked cool and inviting."
        self.BentOver = "the pool steps"
        self.KneelingOn = "the edge of the pool"
        self.SittingOn = "a deck chair"
        self.LyingOn = "a patio chair"
        self.Ground = "the pool deck"
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
     
class PrivateBeach(PrivateOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="a private beach"
        self.NamePrep ="on a private beach"
        self.BeginDesc = "Waves rolled onto the sand. They had the beach all to themselves."
        self.Despite = "the sand that got into every crack"
        self.BentOver = "a sand dune"
        self.KneelingOn = "on the beach towel"
        self.SittingOn = "a beach chair"
        self.LyingOn = "on the beach towel"
        self.Ground = "sand"
        self.MaleTopClothing = ""
        self.MaleBottomClothing = "speedo"
        self.FemaleTopClothing = ""
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
     
class PublicBathroom(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        sPlace = WordList(["7-Eleven","Ace Hardware","Aldi","Applebee's",
                           "Bass Pro Shop","Cheesecake Factory",
                           "Chick-fil-a","Chili's","Chipotle",
                           "Chuck E. Cheese","Circle K","Costco",
                           "Cracker Barrel","CVS","Dollar General",
                           "Dollar Tree","Five Guys","Home Depot","IHOP",
                           "Ikea","In-N-Out Burger","Kroger",
                           "McDonald's","Olive Garden","PetSmart",
                           "Piggly Wiggly","Rite-Aid","Safeway",
                           "Shake Shack","Subway","Superstore",
                           "Taco Bell","Target","Wal-mart","Wendy's",
                           "Whole Foods"]).GetWord()
        sBath = WordList(["bathroom","restroom","men's room","ladies room"]).GetWord()
        sTileCondition = WordList(["white","stained","streaked","chipped","polished","grimy"]).GetWord() 
        if CoinFlip():
            TopFemClothing = self.FemWardrobe.GetTop(bDresses = False,
                                                     NotList = ["bikini","bra","eveningdress",
                                                                "nightgown","robe","sportsbra",
                                                               ])

            BottomFemClothing = self.FemWardrobe.GetBottom(NotList = ["bikini"])
        else:
            TopFemClothing = self.FemWardrobe.GetDress()

            BottomFemClothing = self.FemWardrobe.Panties
        self.Name = sPlace + " " + sBath
        self.NamePrep ="in the " + sBath + " at " + sPlace
        self.BeginDesc = "The " + sPlace + " " + sBath + " " 
        self.BeginDesc += WordList(["was cramped and filthy",
                                    "was large with rows of shiny stalls",
                                    "featured gleaming white tile and a strong chemical odor",
                                    "had yellowing tile and an EMPLOYEES MUST WASH HANDS sign",
                                    "was spotless and white but had a malignant odor",
                                    "was grungy and smelled like a homeless guy had been living there",
                                    "was dimly lit and smelled of disinfectant",
                                    "featured a single chipped porcelain toilet beneath the flickering fluorescent lights",
                                    "had crude graffiti scrawled across the stained tile",
                                   ]).GetWord() + "."
        self.Despite = "the extremely cramped quarters"
        self.BentOver = WordList(["the toilet","the chipped porcelain toilet","the sink","the changing table"]).GetWord()
        self.KneelingOn = WordList(["on the toilet seat","on the tiled floor"]).GetWord()
        self.SittingOn = WordList(["on the toilet","on the chipped porcelain toilet","on the back of the toilet"]).GetWord()
        self.LyingOn = "on the " + sTileCondition + " tiled floor"
        self.HurryReason = "Someone might hear us!"
        self.Caught ="Someone pounded on the door and shouted 'Hurry up!'"
        self.Excuse = "'Busy!' he shouted back."
        self.Consequence = "someone called, 'I think they're fucking in the " + sPlace + " " + sBath + "'"
        self.AuthorityFigure = sPlace + " employee"
        self.Ground = sTileCondition + " tiled floor"
        self.FemaleTopClothing = TopFemClothing.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = BottomFemClothing.RandomDescription(bLongDesc = False)
     
class Shower(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the shower"
        self.NamePrep ="in the shower"
        self.Despite = "the slippery floor"
        self.BeginDesc = "The hot shower water rained down on them."
        self.BentOver = "against the wall"
        self.KneelingOn = "the floor of the shower stall"
        self.SittingOn = "on a seat in the shower stall"
        self.LyingOn = "on the floor of the shower stall"
        self.Ground = "wet floor"
        self.FemaleTopClothing = ""
        self.FemaleBottomClothing = ""
        self.MaleTopClothing = ""
        self.MaleBottomClothing = ""
     
class StarbucksBathroom(PublicIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="Starbucks bathroom"
        self.NamePrep ="in the bathroom at Starbucks"
        self.BeginDesc = "The bathroom at Starbucks was small and smelled of coffee."
        self.Despite = "the extremely cramped quarters"
        self.BentOver = "the toilet"
        self.KneelingOn = "on the toilet seat"
        self.SittingOn = "on the toilet"
        self.LyingOn = "on the tiled floor"
        self.HurryReason = "Someone might hear us!"
        self.Caught ="Someone pounded on the door and shouted 'Hurry up!'"
        self.Excuse = "'Busy!' he shouted back."
        self.Consequence = "someone called, 'I think they're having sex in the Starbucks bathroom'"
        self.AuthorityFigure = "a Starbucks barista"
        self.Ground = "tiled floor"
        self.FemaleTopClothing = self.FemWardrobe.Dress.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.Panties.RandomDescription(bLongDesc = False)
     
class Surf(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the surf"
        self.NamePrep ="in the water at the beach"
        self.BeginDesc = "A hot sun shone down as the waves crested against their bodies."
        self.Despite = "the breaking waves"
        self.BentOver = "in the water"
        self.KneelingOn = "in the shallow water"
        self.SittingOn = "in the shallow water"
        self.LyingOn = "the wet sand"
        self.HurryReason = "People will notice us!"
        self.Caught ="'That lifeguard is coming towards us!' she said."
        self.Excuse = "'Let them enjoy it, baby,' he said."
        self.Consequence = "the lifeguard watched"
        self.AuthorityFigure = "the lifeguard"
        self.Ground = "the dark green water"
        self.MaleTopClothing = ""
        if CoinFlip():
            self.MaleBottomClothing = self.MaleWardrobe.Trunks.RandomDescription(bLongDesc = False)
        else:
            self.MaleBottomClothing = self.MaleWardrobe.Speedo.RandomDescription(bLongDesc = False)
        self.FemaleTopClothing = self.FemWardrobe.BikiniTop.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.BikiniBottoms.RandomDescription(bLongDesc = False)
     
class Woods(PublicOutdoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="the woods"
        self.NamePrep ="out in the woods"
        self.BeginDesc = "The leafy trees were thick in every direction."
        self.Despite = "the dirt and mosquitos"
        self.BentOver = "a mossy log"
        self.KneelingOn = "on a large smooth rock"
        self.SittingOn = "on a tree stump"
        self.LyingOn = "a broad, smooth boulder"
        self.HurryReason = "someone might see us"
        self.Caught ="'Oh my god, there is a homeless guy watching us,' she whispered."
        self.Excuse = "'Fuck off!' he yelled at the man."
        self.Consequence = "the homeless man watched them and masturbated"
        self.AuthorityFigure = "someone"
        self.Ground = "thick carpet of leaves"
        self.FemaleTopClothing = "cute flannel top"
        self.FemaleBottomClothing = self.FemWardrobe.Jeans.RandomDescription(bLongDesc = False)
     
class YogaStudio(PrivateIndoors):
    def __init__(self, LocMan = None, LocWoman = None):
        super().__init__(LocMan = LocMan, LocWoman = LocWoman)

        self.Name ="a yoga studio"
        self.NamePrep ="in a yoga studio"
        self.BeginDesc = "The relaxing drone of zen meditation music filled the warm studio."
        self.Despite = "not having stretched properly"
        self.BentOver = "a large yoga ball"
        self.KneelingOn = "a yoga mat"
        self.SittingOn = "a balance ball"
        self.LyingOn = "a yoga mat"
        self.Ground = "the purple yoga mat"
        self.FemaleTopClothing = self.FemWardrobe.SportsBra.RandomDescription(bLongDesc = False)
        self.FemaleBottomClothing = self.FemWardrobe.YogaPants.RandomDescription(bLongDesc = False)

     
class LocationSelector():
     def __init__(self):
          self.Locations = [] 

          for sub in PublicOutdoors.__subclasses__():
               self.Locations.append(sub)

          for sub in PublicIndoors.__subclasses__():
               self.Locations.append(sub)
               
          for sub in PrivateOutdoors.__subclasses__():
               self.Locations.append(sub)
               
          for sub in PrivateIndoors.__subclasses__():
               self.Locations.append(sub)
     
     def Location(self, InOut = exutil.LocInOutType.Either, PubPrivType = exutil.LocPubPrivType.Either, LocMan = None, LocWoman = None):
          ThisLoc = Location(LocMan = LocMan, LocWoman = LocWoman)
          MatchingLocations = []
          
          if InOut == None:
               InOut = exutil.LocInOutType.Either
          if PubPrivType == None:
               PubPrivType = LocPubPrivType.Either

          # PubPriv = exutil.LocPubPrivType.Private
          # InOut = exutil.LocInOutType.Outdoors
          if not self.Locations is None and len(self.Locations) > 0:
               for loc in self.Locations:
                    if InOut == exutil.LocInOutType.Either or loc.InOut == InOut:
                         if PubPrivType == exutil.LocPubPrivType.Either or loc.PubPriv == PubPrivType:
                              MatchingLocations.append(loc)
               
               if len(MatchingLocations) > 0:
                    ThisLoc = choice(MatchingLocations)(LocMan = LocMan, LocWoman = LocWoman)
          
          return ThisLoc
          
     
     