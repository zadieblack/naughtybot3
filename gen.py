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

        # Buckets of prioritized generators for random selection
        self.BucketLowest = []
        self.BucketNormal = []
        self.BucketAboveAvg = []
        self.BucketHigh = []
        self.BucketSuperHigh = []

        # If generator IDs are not given the container will add them
        self.NextGenID = iFirstID

        # Build generator list
        for subclass in GeneratorClass.__subclasses__():
            item = subclass()
            if not item.Disabled:
                if item.ID == -1:
                    item.ID = self.NextGenID
                if item.Priority == GenPriority.Lowest:
                    self.BucketLowest.append(item)
                elif item.Priority == GenPriority.AboveAvg:
                    self.BucketAboveAvg.append(item)
                elif item.Priority == GenPriority.High:
                    self.BucketHigh.append(item)
                elif item.Priority == GenPriority.SuperHigh:
                    self.BucketSuperHigh.append(item)
                else:
                    self.BucketNormal.append(item)
                self.GeneratorList.append(item)
                self.NextGenID = item.ID + 1

        # Validate generator list
        self.ValidateGenIDs()

        # Print list (uncomment for debugging)
        self.PrintGeneratorList()

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

    def PrintGeneratorList(self):
        print("List of generators for " + str(self))
        if len(self.GeneratorList) > 0:
            for gen in self.GeneratorList :
                print(" * " + self.GeneratorClassName + " ID # " + str(gen.ID))

    # Get list of prioritized generators
    def GetSelectorList(self):
        return self.SelectorList

    # Get a random generator
    def RandomGenerator(self, bAllowPromo = True, Type = None):
        Generator = Generator()
        AllowedTypes = []
        Bucket = []
          
        if not Type is None:
            AllowedTypes = [Type] 
        else:
            AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
        if bAllowPromo:
            AllowedTypes.append(GeneratorType.Promo)

        MAXTRIES = 100

        iCount = 0
        while len(Bucket) == 0 and iCount < MAXTRIES:
            iChance = randint(1, 15)                                # 1 + 2 + 3 + 4 + 5 = 15

            if iChance == 1:
                Bucket = self.LowestBucket
                print(" Lowest bucket selected (iChance == " + str(iChance) + ")")
            elif iChance > 1 and iChance <= 3:      # 2x
                Bucket = self.NormalBucket 
                print(" Normal bucket selected (iChance == " + str(iChance) + ")")
            elif iChance > 3 and iChance <= 6:      # 3x
                Bucket = self.AboveAverageBucket
                print(" AboveAverage bucket selected (iChance == " + str(iChance) + ")")
            elif iChance > 6 and iChance <= 10:     # 4x
                Bucket = self.HighBucket 
                print(" High bucket selected (iChance == " + str(iChance) + ")")
            elif iChance > 10 and iChance <= 15:    # 5x
                Bucket = self.SuperHighBucket
                print(" SuperHigh bucket selected (iChance == " + str(iChance) + ")")
            else:
                Bucket = self.NormalBucket 
                print(" WARNING: Default bucket (normal) selected (iChance == " + str(iChance) + ")")
               
        Generator = choose(Bucket)
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
            for gen in self.GeneratorList:
                if gen.ID in IDList:
                    print("=*= WARNING =*= " + self.GeneratorClassName + " ID # " + str(gen.ID) + " has a duplicate.\n")
                    bValid = False
                else:
                    IDList.append(gen.ID)

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

