#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
import re # remove later
from PIL import Image, ImageDraw, ImageFont
from random import *
from util import *
from title.bgprofiles import *

PATH = "title/cover_stuff/"
MAX_IMG_NUM = 24
RESOLUTION = 4.167
LOWERTITLETEXTBOUND = 527
HHMAXHEIGHT = 305

iFinalFontSize = 0

BGImgQ = HistoryQ(iQSize = 5)




def WrapText(sText, font, max_line_width):
     # break string into multiple lines that fit max_line_width
     # and return an array of strings
     Lines = []
     
     bEndOfText = False
     iLastWhtSpc = 0
     iLineStart = 0
     sLineSoFar = ""
     sLastValidLine = ""
     while not bEndOfText:
          #width_of_line = 0
          iLastWhtSpc = iLineStart
          
          for charno in range(iLineStart, len(sText)):
               if sText[charno].isspace() or sText[charno] == "-":
                    iLastWhtSpc = charno
               #char_size = font.getsize(sText[charno])
               #width_of_line += char_size[0]
               sLineSoFar += sText[charno]
               sLastValidLine = sText[iLineStart:iLastWhtSpc]
               
               # problem: this now breaks the line only after it has 
               # exceeded the max width.
               if sText[charno] == "\n" or font.getsize(sLineSoFar)[0] >= max_line_width:
                    if iLastWhtSpc >= iLineStart:
                         Lines.append(sLastValidLine)
                         iLineStart = iLastWhtSpc + 1
                         sLastValidLine = ""
                         sLineSoFar = ""
                         break
                    else:
                         iLastWhtSpc = int((charno - iLineStart)/2) 
                         Lines.append(sLastValidLine)
                         iLineStart = iLastWhtSpc + 1
                         sLastValidLine = ""
                         sLineSoFar = ""
                         break
               else:
                    if charno == len(sText) - 1:
                         bEndOfText = True
                         Lines.append(sText[iLineStart:len(sText)])
                         break 
     
     return Lines

# Guesstimate an initial font size based on the # of characters         
def GuesstimateFontSize(sText, iMaxPointSize = 0):
    iFontSize = 3
  
    if iMaxPointSize == 0:
        iTextLen = len(sText)
        if iTextLen <= 45:
            iFontSize = 75
        elif iTextLen <= 60:
            iFontSize = 68
        elif iTextLen <= 75:     #(+  45)
            iFontSize = 60
        elif iTextLen <= 90:     #(+  70)
            iFontSize = 55
        elif iTextLen <= 110:     #(+  80)
            iFontSize = 50
        elif iTextLen <= 150:     #(+ 185)
            iFontSize = 45
        elif iTextLen <= 250:
            iFontSize = 40
        elif iTextLen <= 400:
            iFontSize = 33
        elif iTextLen <= 1000:
            iFontSize = 29
        else: 
            iFontSize = 25
    else:
        iFontSize = iMaxPointSize 

    return iFontSize 

class BlockOfText():
    def __init__(self, sText, sFontName, iMaxPointSize, BoundingBoxSize):
        self.Text = sText 
        self.FontName = sFontName
        self.BoundingBoxWidth = BoundingBoxSize[0]
        self.BoundingBoxHeight = BoundingBoxSize[1] 
        self.TotLineHeight = 0
        self.DecreaseSizeBy = 3
        self.FontSize = GuesstimateFontSize(sText, iMaxPointSize)
        self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize, index = 0)
        
        # wrap the text based on the bounding text box's width
        self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)
       
        # shrink font until lines do not exceed bounding text box's height
        self.FitTextToBox()

        global iFinalFontSize
        iFinalFontSize = self.Font.size
        pass
        
    def CalcTotLineHeight(self):
        iHeight = 0

        for line in self.Lines:
            if line.isspace() or line == "":
                iHeight += self.Font.getsize("a")[1] / 2
            else:
                iHeight += self.Font.getsize(line)[1]
          
        return iHeight

    def FitTextToBox(self):
        # calculate the height of the text
        self.TotLineHeight = self.CalcTotLineHeight()

        while self.TotLineHeight > self.BoundingBoxHeight:
            self.FontSize = (self.FontSize + (self.DecreaseSizeBy * (-1)))
            self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize, index = 0)

            self.TotLineHeight = self.CalcTotLineHeight()

def DrawTextBox(sText, BoxWidth, BoxHeight, FontName, Color, iMaxPointSize = 0):
    # adjust point size for pixel density
    iAdjMaxPointSize = int(round(iMaxPointSize * RESOLUTION, 0))

    # how much the text in the box is offset from the box
    xOffset = 0     #.027
    yOffset = 0     #.027
     
    # set width and height of the bounding text box
    offset_width = round(BoxWidth - (BoxWidth * xOffset * 2), 0)
    offset_height = round(BoxHeight - (BoxHeight * yOffset * 2), 0)

    TextBlock = BlockOfText(sText, 
                            FontName, 
                            iAdjMaxPointSize,
                            (offset_width, offset_height))
               
    ImgTxt = Image.new('RGBA', (BoxWidth, BoxHeight))
    draw = ImageDraw.Draw(ImgTxt)
               
    y_text = 0
    for line in TextBlock.Lines:
        width, height = (0, 0)
        if line.isspace() or line == "":
            width, height = TextBlock.Font.getsize("a")
            height = height / 2
        else:
            width, height = TextBlock.Font.getsize(line)

            draw.text(
                      ((offset_width - width)/2, 
                       (offset_height - TextBlock.TotLineHeight)/2 + y_text), 
                      line, 
                      font = TextBlock.Font, 
                      fill = Color)
        y_text += height
     
    return ImgTxt
     
def GetBGImg(BGProfile):
    BGImg = None 

    try:
        BGImg = Image.open(PATH + BGProfile.BGFileName).convert('RGBA')
    except IOError as e:
        print("***ERROR***\nFile save failed in SaveImg()\n" + e.strerror)
     
    return BGImg

def CalcTextSizeScore(sText):
    dScore = 0.0
    # = (Char Count /4) +(Upper Case Num + Avg Word Size)+(- White Spaces)
    # > 23 needs larger template

    iCharCount = len(sText)
    words = re.findall(r"[\w']+", sText)
    iNumWords = len(words)
    dAvgWordLen = len(sText)/iNumWords
    
    iWhiteSpaceChars = len(words) - 1

    iUpperCaseChars = 0
    for c in sText:
        if c.isupper():
            iUpperCaseChars = iUpperCaseChars + 1 

    dScore = (iCharCount/4) + (iUpperCaseChars + dAvgWordLen) + (-1 * iWhiteSpaceChars)
    
    return dScore
    #with open("word_stats.txt", 'a') as StatsLine:
    #    StatsLine.write(sText + "," 
    #                    + str(iFinalFontSize) + ","
    #                    + str(len(sText)) + ","
    #                    + str(iWhiteSpaceChars) + ","
    #                    + str(iUpperCaseChars) + ","
    #                    + str(iNumRealWords) + ","
    #                    + str(dAvg)
    #                    + "\n")


def CreateImg(TitleTweet):
    # create Image object with the input image
    RGBImgOut = None 
    
    # for testing purposes only! REMOVE!
    #TitleTweet.SetImgTxt("Punished in Public by the Oiled-Up Hung High-school Teacher BBC from Uranus")
    iFinalFontSize = 0

    # get a random cover profile 
    BGProfile = GetBGProfileGenerator()

    sFileName = ""

    # cover elements are not perfectly centered. so the text needs to be
    # slightly off-center as well. just add this when specifying the
    # coordinates of the text bounding box.

    width_offset = 12

    if isinstance(TitleTweet, GeneratedTitleTweet):
        # calculate text size score
        dScore = CalcTextSizeScore(' '.join(TitleTweet.ImgTxt().split('\n')))

        # draw author name
        color = 'rgba(0, 0, 0, 255)' # color should eventually come from template
        
        ImgAuthorNameTxt = DrawTextBox(TitleTweet.AuthorName(),
                                      BoxWidth = 861,  
                                      BoxHeight = 78, 
                                      FontName = "Lapidary 333 Bold Italic.otf",
                                      Color = BGProfile.AuthorNameColor,
                                      iMaxPointSize = 16)
        
        # draw title
        ImgTxt = DrawTextBox(' '.join(TitleTweet.ImgTxt().split('\n')),
                                      BoxWidth = 872,  
                                      BoxHeight = 392, 
                                      #MaxHeight = LOWERTITLETEXTBOUND - BGProfile.yOffset,
                                      FontName = "Walpurgis Night.otf",
                                      Color = BGProfile.MainTitleColor)

        # check to see if the textbox is extra tall, requiring us to switch to the
        # plain header 

        if dScore > 23:
            BGProfile.UsePlainheader()

        # get background image for the current bg profile
        ImgBase = GetBGImg(BGProfile)

        # combine the author name and base images
        ImgBase.paste(ImgAuthorNameTxt, (55 + width_offset, 540), mask = ImgAuthorNameTxt)

        # combine the title text and base images
        ImgBase.paste(ImgTxt, (54 + width_offset, 138), mask = ImgTxt)
             
        # save the edited image
        RGBImgOut = ImgBase.convert('RGB')

    return RGBImgOut
