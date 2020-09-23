#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Generator base class module

import util

from random import *
from util import GenPriority
from util import GeneratorType

MAXBUCKETTRIES = 1000
MAXGENTRIES = 1000

class Generator():
    def __init__(self, 
                 ID = -1, 
                 Priority = GenPriority.Normal, 
                 Type = GeneratorType.Normal, 
                 Disabled = False, 
                 sTxt = ""):

        # each generator should have a unique ID
        self.ID = ID

        # increasing the Priority increases the chances the generator is randomly selected. But it can only be selected again while it is not currently in the history queue
        self.Priority = Priority

        # most generators are Normal. Setting a generator to Test makes sure it can't be selected randomly. Setting a generator to Promo means it won't be selected for reply tweets
        self.GeneratorType = GeneratorType

        # disabled = true disables the generator so it cannot be selected
        self.Disabled = Disabled 

        # the generated text
        self.Txt = sTxt

        # normal / promo / test
        self.Type = Type

    def Generate(self):
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

        # The optional history q
        if not HistoryQ is None:
            self.HistoryQ = HistoryQ
            # print(" HistoryQ found for " + self.GeneratorClassName)
        else:
            print("=*= WARNING =*= Empty HistoryQ passed to GeneratorContainer() for [" + self.GeneratorClassName + "], new blank queue will be initialized.")
            self.HistoryQ = util.HistoryQ()

        # List of unique generators 
        self.GeneratorList = []

        # Buckets of prioritized generators for random selection
        self.BucketLowest = []
        self.BucketLow = []
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
        #self.PrintGeneratorList()

        #print(self.GeneratorClassName + " Priority Buckets:")
        #print(" * Lowest priority bucket has " + str(len(self.BucketLowest)) + " items")
        #print(" * Low priority bucket has " + str(len(self.BucketLow)) + " items")
        #print(" * Normal priority bucket has " + str(len(self.BucketNormal)) + " items")
        #print(" * Above Average priority bucket has " + str(len(self.BucketAboveAverage)) + " items")
        #print(" * High priority bucket has " + str(len(self.BucketHigh)) + " items")
        #print(" * Super High priority bucket has " + str(len(self.BucketSuperHigh)) + " items")

    def AddGenerator(self, Gen, Priority = GenPriority.Normal):
        bResult = False 

        if Priority == GenPriority.Lowest:
            self.BucketLowest.append(Gen)
        elif Priority == GenPriority.Low:
            self.BucketLow.append(Gen)
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

    # Check to see that our priority buckets contain at least one item
    def AreBucketsEmpty(self):
        bBucketsEmpty = True

        if len(self.BucketLowest) > 0 \
            or len(self.BucketLow) > 0 \
            or len(self.BucketNormal) > 0 \
            or len(self.BucketAboveAverage) > 0 \
            or len(self.BucketHigh) > 0 \
            or len(self.BucketSuperHigh) > 0 \
            :
            bBucketsEmpty = False

        return bBucketsEmpty

    # Get an individual generator by ID or class name
    def GetGenerator(self, GenID):
        Generator = None 

        if len(self.GeneratorList) > 0:
            if isinstance(GenID, int):
                for gen in self.GeneratorList :
                    if gen.ID == GenID:
                        Generator = gen
                        break
            elif isinstance(GenID, str):
                for gen in self.GeneratorList :
                    if type(gen).__name__ == GenID:
                        Generator = gen
                        break

                         
        return Generator

    # Get list of generators
    def GetGeneratorList(self):
        return self.GeneratorList  

    def PrintGeneratorList(self):
        sTxt = ""

        sTxt = "List of generators for " + str(self) + ":\n\n"
        if len(self.BucketLowest) > 0:
            for gen in self.GeneratorList:
                sTxt += " * " + self.GeneratorClassName + " | \tID # " + str(gen.ID) + " | \t" + str(gen.Priority)
                sTxt += "\n"

        print(sTxt)

    # Get list of prioritized generators
    def GetSelectorList(self):
        return self.SelectorList

    def GetBucket(self):
        Bucket = []

        #print(" GeneratorContainer.GetBucket() for " + str(self.GeneratorClassName))

        iCount = 0
        while len(Bucket) == 0 and iCount < MAXBUCKETTRIES:
            iChance = randint(1, 55)                                # 1 + 2 + 3 + 4 + 5 = 15
            
            if iChance == 1:
                Bucket = self.BucketLowest
                #print(" - Lowest bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            elif iChance >= 2 and iChance < 4:      # 2x lowest
                Bucket = self.BucketLow 
                #print(" - Normal bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            elif iChance >= 4 and iChance < 8:      # 2x low
                Bucket = self.BucketNormal 
                #print(" Normal bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            elif iChance >= 8 and iChance < 16:      # 2x normal
                Bucket = self.BucketAboveAverage
                #print(" - AboveAverage bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            elif iChance >= 16 and iChance < 32:     # 2x above average
                Bucket = self.BucketHigh
                #print(" - High bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            elif iChance >= 32 and iChance < 56:     # 1.5x high
                Bucket = self.BucketSuperHigh
                #print(" - SuperHigh bucket selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.")
            else:
                Bucket = self.BucketNormal
                print("=*= WARNING =*= Default bucket (normal) selected (iChance == " + str(iChance) + "). Bucket contains " + str(len(Bucket)) + " items.\n")

            iCount = iCount + 1

        if iCount >= MAXBUCKETTRIES:
            print("=*= WARNING =*= Maximum attempts to choose a bucket exceeded for " + self.GeneratorClassName + " GetBucket(). Bucket " + str(Bucket) + " accepted by default.\n")

        return Bucket

    # Get a random generator
    def RandomGenerator(self, bAllowPromo = False, Type = GeneratorType.Normal):
        Generator = None 
        AllowedTypes = []
        Bucket = []
          
        AllowedTypes = [GeneratorType.Normal, GeneratorType.BookTitle]
          
        if bAllowPromo:
            AllowedTypes.append(GeneratorType.Promo)

        iGetBucketTries = 1

        if not self.AreBucketsEmpty():
            Bucket = self.GetBucket()
            if not len(Bucket) == 0:
                Generator = choice(Bucket)
            else:
                print("=*= WARNING =*= Empty bucket received while attempting to randomly pick a generator for " + str(self.GeneratorClassName) + "!\n")

            iGetGeneratorTries = 1
            while (not Generator.Type in AllowedTypes or not self.HistoryQ.PushToHistoryQ(str(Generator.ID)) or Generator is None) \
                and iGetGeneratorTries < MAXGENTRIES:
                Bucket = self.GetBucket()
                if not len(Bucket) == 0:
                    Generator = choice(Bucket)
                else:
                    print("=*= WARNING =*= Empty bucket received while attempting to randomly pick a generator for " + str(self.GeneratorClassName) + "!\n")

                iGetGeneratorTries = iGetGeneratorTries + 1

            if iGetGeneratorTries >= MAXGENTRIES - 1:
                print("=*= WARNING =*= Max number of tries (" + str(MAXGENTRIES) + ") exceeded while attempting to randomly select a generator of type " + str(self.GeneratorClassName) + "! Accepted #" + str(Generator.ID) + " by default.\n")
                    
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



