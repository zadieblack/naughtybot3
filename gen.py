#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class module

from random import *
from util import *

class Generator():
    def __init__(self, 
                 Container = None,
                 ID = -1, 
                 Priority = GenPriority.Normal, 
                 Type = GeneratorType.Normal, 
                 bDisabled = False, 
                 Func = None,
                 sTxt = ""):

        # each generator should have a unique ID
        self.ID = ID

        # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
        self.Priority = Priority

        # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
        self.GeneratorType = GeneratorType

        # disabled = true disables the generator so it cannot be selected
        self.Disabled = bDisabled 

        # the generated text
        self.Txt = sTxt

        # normal / promo / test
        self.Type = Type

    # pass in a custom function for this object
    def Generate(self, Func):
        self.Txt = self.GenerateTxt()

    # this will be overridden by most generators but this is how it should look
    def GenerateTxt(self):
        sTxt = ""

        return sTxt


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
        self.BucketAboveAverage = []
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

                self.AddGenerator(item, item.Priority)
                self.NextGenID = item.ID + 1

        # Validate generator list
        self.ValidateGenIDs()

        # Print list (uncomment for debugging)
        self.PrintGeneratorList()

    def AddGenerator(self, Gen, Priority = GenPriority.Normal):
        bResult = False 

        if Priority == GenPriority.Lowest:
            self.BucketLowest.append(Gen)
        elif Priority == GenPriority.AboveAverage:
            self.BucketAboveAverage.append(Gen)
        elif Priority == GenPriority.High:
            self.BucketHigh.append(Gen)
        elif Priority == GenPriority.SuperHigh:
            self.BucketSuperHigh.append(Gen)
        else:
            self.BucketNormal.append(Gen)
        self.GeneratorList.append(Gen)

        bResult = True

        return bResult 

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
        sTxt = ""

        sTxt = "List of generators for " + str(self) + ":\n\n"
        if len(self.GeneratorList) > 0:
            for gen in self.GeneratorList:
                sTxt += " * " + self.GeneratorClassName + " | ID # " + str(gen.ID) + " | " + str(gen.Priority)
                sTxt += "\n"

        print(sTxt)

    # Get list of prioritized generators
    def GetSelectorList(self):
        return self.SelectorList

    def GetBucket(self):
        Bucket = []

        MAXTRIES = 100

        iCount = 0
        while len(Bucket) == 0 and iCount < MAXTRIES:
            iChance = randint(1, 15)                                # 1 + 2 + 3 + 4 + 5 = 15

            if iChance == 1:
                Bucket = self.BucketLowest
                #print(" Lowest bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance > 1 and iChance <= 3:      # 2x
                Bucket = self.BucketNormal 
                #print(" Normal bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance > 3 and iChance <= 6:      # 3x
                Bucket = self.BucketAboveAverage
                #print(" AboveAverage bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance > 6 and iChance <= 10:     # 4x
                Bucket = self.BucketHigh
                #print(" High bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            elif iChance > 10 and iChance <= 15:    # 5x
                Bucket = self.BucketSuperHigh
                #print(" SuperHigh bucket selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")
            else:
                Bucket = self.BucketNormal
                #print(" WARNING: Default bucket (normal) selected (iChance == " + str(iChance) + "). Bucket contains #" + str(len(Bucket)) + " items.")

            iCount = iCount + 1

        return Bucket

    # Get a random generator
    def RandomGenerator(self, bAllowPromo = True, Type = None):
        Generator = None 
        AllowedTypes = []
        Bucket = []
          
        if not Type is None:
            AllowedTypes = [Type] 
        else:
            AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
        if bAllowPromo:
            AllowedTypes.append(GeneratorType.Promo)

        Bucket = self.GetBucket()
        Generator = choice(Bucket)
        while not Generator.Type in AllowedTypes:
            Bucket = self.GetBucket()
            Generator = choice(Bucket)
                    
        return Generator 

    def GetGeneratorsSequential(self, bAllowPromo = True, Type = None):
          GeneratorList = []
          AllowedTypes = []
          
          if not Type is None:
               AllowedTypes = [Type] 
          else:
               AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
          if bAllowPromo:
               AllowedTypes.append(GeneratorType.Promo)

          for gen in self.GeneratorList:
               if gen.Type in AllowedTypes:
                    GeneratorList.append(gen)
               
          return GeneratorList     

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



