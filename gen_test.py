#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class testing module

from random import *
from util import *
from gen import *
import names
import title.titletemplates as titles

TestGen1 = Generator(ID = 1, Priority = 2)

#class TestGenContainer(GeneratorContainer):
#    pass

class TestGen(Generator):
    def __init__(self, ID = -1, Priority = GenPriority.Normal, sAuthorName = "Bob", AuthorGender = None, iNum = -1):
        super().__init__(ID = ID, Priority = Priority)

        if AuthorGender is None:
            if CoinFlip():
                self._AuthorGender = Gender.Female 
            else:
                self._AuthorGender = Gender.Male 
        else:
            self._AuthorGender = AuthorGender 

        if sAuthorName != "":
            self._AuthorName = sAuthorName 
        else:
            self._AuthorName = ""

        if iNum == -1:
            self.Num = randint(1,99)
        else:
            self.Num = iNum


    def AuthorName(self):
        return self._AuthorName 

    def AuthorGender(self):
        return self._AuthorGender

    def GenerateTxt(self):
        sTxt = "This is " + str(type(self).__name__) + "! Author " + self.AuthorName() + " is a " + str(self.AuthorGender()) + " and their favorite number is " + str(self.Num) + "!"

        return sTxt

class TestGen1(TestGen):
    def __init__(self):
         super().__init__(ID = 1, Priority = GenPriority.Lowest, sAuthorName = "Chris")

class TestGen2(TestGen):
    def __init__(self):
         super().__init__(ID = 2, Priority = GenPriority.Normal, sAuthorName = "Jean")

class TestGen3(TestGen):
    def __init__(self):
         super().__init__(ID = 3, Priority = GenPriority.AboveAverage)

class TestGen4(TestGen):
    def __init__(self):
         super().__init__(ID = 3, Priority = GenPriority.High)

class TestGen5(TestGen):
    def __init__(self):
         super().__init__(ID = 3, Priority = GenPriority.SuperHigh)

class TestGen6(TestGen):
    def __init__(self):
         super().__init__(ID = 7, sAuthorName = "Jo")

class TestGen7(TestGen):
   def __init__(self):
         super().__init__(Priority = GenPriority.AboveAverage)

class TestGen8(TestGen):
   def __init__(self):
         super().__init__(ID = 10, Priority = GenPriority.AboveAverage)

class TestGen9(TestGen):
   def __init__(self):
         super().__init__(ID = 11, Priority = GenPriority.Normal)

class TestGen10(TestGen):
   def __init__(self):
         super().__init__(ID = 11, sAuthorName = "Mo")

class TestGen11(TestGen):
   def __init__(self):
         super().__init__(Priority = GenPriority.Lowest, sAuthorName = "Pat")

#TGC = GeneratorContainer(TestGen)

#Gen = TGC.RandomGenerator()
#print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")

#Gen = TGC.RandomGenerator()
#print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")

#Gen = TGC.RandomGenerator()
#print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")

#print("Her name is " + names.GetInnName(Gender.Female))
#print("His name is " + names.GetInnName(Gender.Male))

TTS = GeneratorContainer(titles.TitleTemplate)
Gen = TTS.RandomGenerator()
print(Gen)
