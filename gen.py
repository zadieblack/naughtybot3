#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class module

from random import *
from util import *

class GeneratorContainer():
    def __init__(self, GeneratorClass, iFirstID = 1, HistoryQ = None):
        super().__init__()  # just in case

        GeneratorObj = GeneratorClass()
        self.GeneratorClassName = str(type(GeneratorObj).__name__)
        print("Generator class name is " + self.GeneratorClassName)

        # The optional history q
        if not HistoryQ is None:
            self.HistoryQ = HistoryQ
        else:
            self.HistoryQ = None

        # List of unique generators 
        self.GeneratorList = []

        # List of prioritized generators for random selection
        self.SelectorList = [] 

        # If generator IDs are not given the container will add them
        self.NextGenID = iFirstID

        for subclass in GeneratorClass.__subclasses__():
            item = subclass()
            if not item.Disabled:
                #for x in range(0, item.Priority):
                
                self.GeneratorList.append([item.ID, item])

        print(self.GeneratorList)

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

    ## Generators adding themselves to the container must call this
    #def AddMe(self, gen):
    #    if isinstance(gen, Generator):
    #        self.GeneratorList.append(gen)
    #        if not gen.Priority is None:
    #            i = 0 
    #            if not gen.Disabled:
    #                while i < gen.Priority:
    #                    self.SelectorList.append(gen)
    #                    i = i + 1

    #        if gen.ID is None or gen.ID < 0:
    #            gen.ID = self.NextGenID
    #            self.NextGenID = self.NextGenID + 1

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
    def __init__(self, 
                 Container = None,
                 ID = -1, 
                 Priority = 1, 
                 GeneratorType = GeneratorType.Normal, 
                 bDisabled = False, 
                 Func = None,
                 sTxt = ""):

        # each generator should have a unique ID
        self.ID = ID

        # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
        self.Priority = Priority

        # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
        self.GeneratorType = GeneratorType
        self.Disabled = bDisabled 

        # the generated text
        self.Txt = sTxt

        ## a container object to hold all the generators for selection
        #if not Container is None and isinstance(Container, GeneratorContainer):
        #    Container.AddMe(self)

    # pass in a custom function for this object
    def Generate(self, Func):
        self.Txt = self.GenerateTxt()

    # this will be overridden by most generators but this is how it should look
    def GenerateTxt(self):
        sTxt = ""

        return sTxt

        return sTweet

