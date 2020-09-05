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
    pass

class TestGen2(TestGen):
    pass

class TestGen3(TestGen):
    pass

TGC = GeneratorContainer(TestGen)


