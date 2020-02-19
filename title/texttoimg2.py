#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
import re # remove later
from PIL import Image, ImageDraw, ImageFont
from random import *
from util import *
from title.titletemplates import *
from title.bgprofiles import *
from title.generators import Generator

PATH = "title/cover_stuff/"
MAX_IMG_NUM = 24
RESOLUTION = 4.167
LOWERTITLETEXTBOUND = 527
HHMAXHEIGHT = 305
MAXWIDTH = 900
XOFFSET = int(round((971 - MAXWIDTH) / 2))

BGImgQ = HistoryQ(iQSize = 5)

def GetTextLineSize(font, sLine):
    width, height = (0,0)

    width, height = font.getsize(sLine)
    off_width, off_height = font.getoffset(sLine)

    width = width - off_width 
    height = height - off_height

    return width, height

def WrapText(sText, font, max_line_width):
     # break string into multiple lines that fit max_line_width
     # and return an array of strings
     Lines = []
     
     bEndOfText = False
     iLastWhtSpc = 0
     iLineStart = 0
     sLineSoFar = ""
     sLastValidLine = ""
     while not bEndOfText and len(sText) > 0:
          #width_of_line = 0
          iLastWhtSpc = iLineStart
          
          for charno in range(iLineStart, len(sText)):
               if sText[charno].isspace() or sText[charno] == "-":
                    iLastWhtSpc = charno

               sLineSoFar += sText[charno]
               sLastValidLine = sText[iLineStart:iLastWhtSpc]
               
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
def GuesstimateFontSize(sText, FontMaxSize = 0):
    iFontSize = 3
  
    if FontMaxSize == 0:
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
        iFontSize = FontMaxSize 

    return iFontSize 

class BlockOfText():
    def __init__(self, sText, sFontName, FontMaxSize, MaxRows, BoundingBoxSize):
        self.Text = sText 
        self.FontName = sFontName
        self.MaxRows = MaxRows
        self.BoundingBoxWidth = BoundingBoxSize[0]
        self.BoundingBoxHeight = BoundingBoxSize[1] 
        self.TotLineHeight = 0
        self.DecreaseSizeBy = 3
        self.FontSize = FontMaxSize # GuesstimateFontSize(sText, FontMaxSize)
        self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize, index = 0)
        
        self.Lines = []
       
        # shrink font until lines do not exceed bounding text box's height
        self.FitTextToBox()
        
    def CalcTotLineHeight(self):
        iHeight = 0

        for line in self.Lines:
            if line.isspace() or line == "":
                iHeight += GetTextLineSize(self.Font, "a")[1] / 2
            else:
                iHeight += GetTextLineSize(self.Font, line)[1]
          
        return iHeight

    def FitTextToBox(self):
        # wrap the text based on the bounding text box's width
        self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)

        # calculate the height of the text
        self.TotLineHeight = self.CalcTotLineHeight()

        while self.TotLineHeight > self.BoundingBoxHeight or len(self.Lines) > self.MaxRows:
            self.FontSize = (self.FontSize + (self.DecreaseSizeBy * (-1)))
            self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize, index = 0)
            self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)
            self.TotLineHeight = self.CalcTotLineHeight()

def DrawTextBox(sText, FontName, FontMaxSize, MaxRows, BoxWidth, BoxHeight, Color):
    # adjust point size for pixel density
    iAdjFontMaxSize = int(round(FontMaxSize * RESOLUTION, 0))

    # how much the text in the box is offset from the box
    xOffset = 0     #.027
    yOffset = 0     #.027
     
    # set width and height of the bounding text box
    offset_width = round(BoxWidth - (BoxWidth * xOffset * 2), 0)
    offset_height = round(BoxHeight - (BoxHeight * yOffset * 2), 0)

    TextBlock = BlockOfText(sText, 
                            FontName, 
                            iAdjFontMaxSize,
                            MaxRows,
                            (offset_width, offset_height))
               
    ImgTxt = Image.new('RGBA', (offset_width, offset_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(ImgTxt)
             
    iTestCnt = 1 # debug only, delete later
    y_text = 0
    for line in TextBlock.Lines:
        width, height = (0, 0)
        if line.isspace() or line == "":
            width, height = GetTextLineSize(TextBlock.Font, "a")
            height = height / 2
        else:
            width, height = GetTextLineSize(TextBlock.Font, line)

            draw.text(
                      ((offset_width - width)/2, y_text), 
                      line, 
                      font = TextBlock.Font, 
                      fill = Color)
                      #features=['-vkrn'])
        #draw.rectangle([((offset_width - width)/2, y_text), (width, height)], outline ="red", width = 5)
        draw.line([((offset_width - width)/2, y_text),((offset_width - width)/2,height)], fill = "red", width = 5)
        #print("iTestCnt = " + str(iTestCnt) + ", line [" + line + "]")
        y_text = y_text + height + int(round(height/5))
        #iTestCnt = iTestCnt + 1
   
    #draw2 = ImageDraw.Draw(ImgTxt)  
    #draw.rectangle([(0, 0), (ImgTxt.width, ImgTxt.height)], outline ="red")
        #ImgTxt

    return ImgTxt
     
def GetBGImg(BGProfile):
    BGImg = None 

    try:
        BGImg = Image.open(PATH + BGProfile.BGFileName).convert('RGBA')
    except IOError as e:
        print("***ERROR***\nFile save failed in GetBGImg()\n" + e.strerror)
     
    return BGImg

def PositionBoxesVertically(BGImg,
                            Boxes = [], 
                            ImgTitleBoxHeight = 0, 
                            ImgTitleBoxWidth = 0,
                            yOffset = 0,
                            xOffset = 0):
    iTotalBoxHeight = 0
    yVCenterOffset = 0
    #ImgTitleArea = Image.new('RGBA', (ImgTitleBoxWidth, ImgTitleBoxHeight))
    #draw = ImageDraw.Draw(ImgTitleArea)

    # add up combined height of boxes
    for box in Boxes:
        iTotalBoxHeight = iTotalBoxHeight + box.height

    # calculate off-set required to center vertically
    # yVCenterOffset = int((ImgTitleBoxHeight - iTotalBoxHeight)/2)

    yLineSpace = 0
    # calculate space between lines 
    if iTotalBoxHeight < ImgTitleBoxHeight:
        #calculate # of vert spaces needed (# boxes - 1)
        #divide up remaining vert space between boxes
        yLineSpace = int((ImgTitleBoxHeight - iTotalBoxHeight)/(len(Boxes)))
    else:
        yLineSpace = 12

    iyOffsetLine = yOffset
    # draw the text boxes
    for box in Boxes:
        #iyOffsetLine = iyOffsetLine #+ yLineSpace
        #BGImg.paste(box, (xOffset, iyOffsetLine), mask = box)
        BGImg.alpha_composite(box, (xOffset, iyOffsetLine))
        iyOffsetLine = iyOffsetLine + box.height #+ yLineSpace

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

def CreateImg(ImgTxtGen):
    # create Image object with the input image
    RGBImgOut = None 
    
    # get a random cover profile 
    BGProfile = GetBGProfileGenerator()

    sFileName = ""

    # cover elements are not perfectly centered. so the text needs to be
    # slightly off-center as well. just add this when specifying the
    # coordinates of the text bounding box.

    width_offset = 12

    if isinstance(ImgTxtGen, Generator):
        # calculate text size score
        dScore = CalcTextSizeScore(' '.join(ImgTxtGen.ImgTxt.split('\n')))

        AuthorTemplate = ImgTxtGen.Template.AuthorLine

        # get background image for the current bg profile
        ImgBase = GetBGImg(BGProfile)

        # draw author name
        color = 'rgba(0, 0, 0, 255)' # color should eventually come from template
        
        ImgAuthorNameTxt = DrawTextBox(ImgTxtGen.AuthorName,
                                       FontName = AuthorTemplate.FontName,
                                       FontMaxSize = AuthorTemplate.FontMaxSize,
                                       MaxRows = AuthorTemplate.MaxRows,
                                       BoxWidth = 872,  
                                       BoxHeight = AuthorTemplate.MaxHeight, 
                                       Color = BGProfile.AuthorNameColor)
        
        TitleBoxes = []

        for line in ImgTxtGen.Template.Lines:
            if not line is None and len(line.LineText) > 0:
                # draw title
                Color = "rgba(0, 0, 0, 255)" 
            
                if line.ColorType == LineColorType.MainTitle:
                    Color = BGProfile.MainTitleColor
                elif line.ColorType == LineColorType.SecondTitle:
                    Color = BGProfile.SecondTitleColor
                elif line.ColorType == LineColorType.SmallText:
                    Color = BGProfile.SmallTextColor
                elif line.ColorType == LineColorType.AuthorName:
                    Color = BGProfile.AuthorNameColor

                ImgTxt = DrawTextBox(line.LineText,
                                    FontName = line.FontName,
                                    FontMaxSize = line.FontMaxSize,
                                    MaxRows = line.MaxRows,
                                    BoxWidth = MAXWIDTH,  
                                    BoxHeight = line.MaxHeight,                                          
                                    Color = Color)

            # check to see if the textbox is extra tall, requiring us to switch to the
            # plain header 

            #if dScore > 23:
            #    BGProfile.UsePlainheader()

                TitleBoxes.append(ImgTxt)

            
        # combine the title text and base images
        ImgBase = PositionBoxesVertically(BGImg = ImgBase,
                                          Boxes = TitleBoxes,
                                          ImgTitleBoxHeight = 326,
                                          ImgTitleBoxWidth = MAXWIDTH,
                                          yOffset = 206,
                                          xOffset = XOFFSET + width_offset)
        #ImgBase.paste(ImgTxt, (54 + width_offset, 234), mask = ImgTxt)

        # combine the author name and base images
        # ImgBase.paste(ImgAuthorNameTxt, (XOFFSET + width_offset, 540), mask = ImgAuthorNameTxt)
        ImgBase.alpha_composite(ImgAuthorNameTxt, (XOFFSET + width_offset, 540))

        # save the edited image
        RGBImgOut = ImgBase.convert('RGB')

    return RGBImgOut
