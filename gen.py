#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class module

from random import *
from util import *

class GeneratorContainer():
    # List of unique generators 
    GeneratorList = []

    # List of prioritized generators for random selection
    SelectorList = []

    # If generator IDs are not given the container will add them
    NextGenID = 1

    # The container can also track the history Q
    HistoryQ 

    def __init__(self, Q = None, iFirstID = 1):
        if not Q is None:
            self.HistoryQ = Q

        self.GeneratorList = []
        self.SelectorList = [] 
        self.NextGenID = iFirstID

    # Get an individual generator by ID
    def GetGenerator(self, GenNo):
        Generator = None 
          
        if len(self.GeneratorList) > 0:
            for gen in self.GeneratorList :
                if gen.ID == GenNo:
                    Generator = gen
                    break
                         
        return Generator

    # Get list of generators
    def GetGeneratorList(self):
        return self.GeneratorList  

    # Get list of prioritized generators
    def GetSelectorList(self):
        return self.SelectorList

    # Get a random generator
    def RandomGenerator(self, bAllowPromo = True, Type = None):
        Generator = None
        AllowedTypes = []
          
        if not Type is None:
            AllowedTypes = [Type] 
        else:
            AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
        if bAllowPromo:
            AllowedTypes.append(GeneratorType.Promo)
               
        if len(self.SelectorList) > 0:

            Generator = choose(self.SelectorList)
            while not Generator.Type in AllowedTypes or Generator.Disabled:
                Generator = choose(self.SelectorList)
                    
        return Generator 

    # Generators adding themselves to the container must call this
    def AddMe(self, gen):
        if isinstance(gen, Generator):
            self.GeneratorList.append(gen)
            if not gen.Priority is None:
                i = 0 
                if not gen.Disabled:
                    while i < gen.Priority:
                        self.SelectorList.append(gen)
                        i = i + 1

            if gen.ID is None or gen.ID < 0:
                gen.ID = self.NextGenID
                self.NextGenID = self.NextGenID + 1

    def ValidateGenIDs(self):
        bValid = True

        IDList = []

        if len(self.GeneratorList) > 0:
            for gen in self.GeneratorList :
                if gen.ID in IDList:
                    print("=*= WARNING =*= Title generator ID # " + str(gen.ID) + " is a duplicate")
                    bValid = False

        return bValid


class Generator():
    ID = -1
    # each generator should have a unique ID
    Priority = 1
    # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
    Type = GeneratorType.Normal
    # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
    Disabled = False
    # the generated text
    Txt = ""
    # a container object to hold all the generators for selection
    self.Container = None
    
    def __init__(self, 
                 ID = -1, 
                 iPriority = 1, 
                 Container = None,
                 GeneratorType = GeneratorType.Normal, 
                 bDisabled = False, 
                 sTxt = ""):

        if not ID == -1:
            self.ID = ID
        self.Priority = iPriority
        if not Container is None and isinstance(Container, GeneratorContainer):
            Container.AddMe(self)
        self.GeneratorType = GeneratorType
        self.Disabled = bDisabled 
        self.Txt = sTxt

    def Generate(self):
        self.Txt = self.GenerateTxt()

    # this will be overridden by most generators but this is how it should look
    def GenerateTxt(self):
        sTweet = ""

        return sTweet

