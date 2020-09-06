#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class testing module

from random import *
from util import *
from gen import *

TestGen1 = Generator(ID = 1, Priority = 2)

#class TestGenContainer(GeneratorContainer):
#    pass

class TestGen(Generator):
    pass

class TestGen1(TestGen):
    def __init__(self):
         super().__init__(ID = 1, Priority = 1)

    def GenerateTxt(self):
        sTxt = "This is TestGen1!"

        return sTxt

class TestGen2(TestGen):
    def __init__(self):
         super().__init__(ID = 2, Priority = 1)

    def GenerateTxt(self):
        sTxt = "This is TestGen2!"

        return sTxt

class TestGen3(TestGen):
    def __init__(self):
         super().__init__(ID = 3, Priority = 1)

    def GenerateTxt(self):
        sTxt = "This is TestGen3!"

        return sTxt

class TestGen4(TestGen):
    def GenerateTxt(self):
        sTxt = "This is TestGen4!"

        return sTxt

class TestGen5(TestGen):
    def GenerateTxt(self):
        sTxt = "This is TestGen5!"

        return sTxt

class TestGen6(TestGen):
    def __init__(self):
         super().__init__(ID = 7, Priority = 1)

    def GenerateTxt(self):
        sTxt = "This is TestGen6!"

        return sTxt

class TestGen7(TestGen):
   def GenerateTxt(self):
        sTxt = "This is TestGen7!"

        return sTxt

TGC = GeneratorContainer(TestGen)

Gen = TGC.RandomGenerator()
print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")

Gen = TGC.RandomGenerator()
print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")

Gen = TGC.RandomGenerator()
print("Gen # " + str(Gen.ID) + ":\n[" + Gen.GenerateTxt() + "]\n")