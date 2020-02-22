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
VERT_SEP_PROP = 2                           # proportion of text height to use as 
                                            # separator between two lines of the 
                                            # the same type
                            

BGImgQ = HistoryQ(iQSize = 5)

def GetBGImg(sFileName):
    BGImg = None 

    try:
        BGImg = Image.open(PATH + sFileName).convert('RGBA')
    except IOError as e:
        print("***ERROR***\nFile save failed in GetBGImg()\n" + e.strerror)
     
    return BGImg

class BGImageHH:
    TitleBoxTop_yOffset = 215
    TitleBoxBottom_yOffset = 523
    FileSuffix = "hh"

    def __init__(self, BGProfile):
        self.MaxHeight = self.TitleBoxBottom_yOffset - self.TitleBoxTop_yOffset
        self.Image = GetBGImg(BGProfile.FileName + "_hh.png")

class BGImagePH:
    TitleBoxTop_yOffset = 128
    TitleBoxBottom_yOffset = 523
    FileSuffix = "hh"

    def __init__(self, BGProfile):
        self.MaxHeight = self.TitleBoxBottom_yOffset - self.TitleBoxTop_yOffset
        self.Image = GetBGImg(BGProfile.FileName + "_ph.png")

def GetTextLineSize(font, sLine):
    width, height = (0,0)

    width, height = font.getsize(sLine)
    off_width, off_height = font.getoffset(sLine)

    width = width + off_width 
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

def CalcBoxHeight(sFontName, iMaxFontSize, iMaxRows):
    iBoxHeight = 0

    Font = ImageFont.truetype(PATH + sFontName, size = iMaxFontSize, index = 0)
    iLineHeight = GetTextLineSize(Font,"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")[1]

    iBoxHeight = (iLineHeight * iMaxRows) + (int(round(iLineHeight/VERT_SEP_PROP)) * (iMaxRows - 1))

    return iBoxHeight 

class TitleSection:
    def __init__(self, sText = "", sFontName = "", iFontSize = 10, iMaxRows = 1, Color = (0,0,0,255)):
        self.Text = sText
        self.FontName = sFontName
        self.FontSize = iFontSize
        self.MaxRows = iMaxRows
        self.Color = Color
        self.VertSepProp = 4
        self.LineSpacer_yOffset = 0
        self.Image = Image.new('RGBA', (0,0)) 

    def DrawTextBox(self):
        ImgTxt_Cropped = None
        ImgTxt = None 

        # adjust point size for pixel density
        iAdjFontMaxSize = int(round(self.FontSize * RESOLUTION, 0))

        # how much the text in the box is offset from the box
        xOffset = 0     #.027
        yOffset = 0     #.027
     
        # calculate width and height of the bounding text box
        offset_width = round(MAXWIDTH - (MAXWIDTH * xOffset * 2), 0)
        offset_height = CalcBoxHeight(self.FontName, iAdjFontMaxSize, self.MaxRows)

        TextBlock = BlockOfText(self.Text, 
                                self.FontName, 
                                iAdjFontMaxSize,
                                self.MaxRows,
                                (offset_width, offset_height))
               
        ImgTxt = Image.new('RGBA', (offset_width, offset_height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(ImgTxt)
             
        y_text = 0
        iCount = 0 
        while iCount < len(TextBlock.Lines):
            line = TextBlock.Lines[iCount]

            width, height = (0, 0)

            if line.isspace() or line == "":
                width, height = GetTextLineSize(TextBlock.Font, "a")
                height = height / 2
            else:
                width, height = GetTextLineSize(TextBlock.Font, line)
                
                # for some reason Pillow will not start drawing the text at (0,0).
                # you must specify (0, 0 - offset). (does this need to happen every time??)
                draw.text(
                          ((offset_width - width)/2, y_text - TextBlock.Font.getoffset(line)[1]), 
                          line, 
                          font = TextBlock.Font, 
                          fill = self.Color)
                          #features=['-vkrn']) # <-- needs libraqm library? 
        
            y_text = y_text + height
            if iCount < len(TextBlock.Lines) - 1:
                y_text = y_text + int(self.LineSpacer_yOffset * .5)

            iCount = iCount + 1
        
        ImgTxt_Cropped = ImgTxt.crop((0, 0, offset_width, y_text))
        #draw.rectangle([(0, 0), (ImgTxt.width, ImgTxt.height)], outline ="blue", width = 2)

        return ImgTxt_Cropped

    def DrawText(self, iLineSpace = 0):
        self.LineSpacer_yOffset = iLineSpace
        self.Image = self.DrawTextBox()

    def ShrinkText(self, iStep, iLineSpace = 0):
        bSuccess = False 

        self.LineSpacer_yOffset = iLineSpace
        if self.FontSize - iStep > 0:
            self.FontSize = self.FontSize - iStep 
            self.Image = self.DrawTextBox()
            bSuccess = True

        return bSuccess

    def GrowText(self, iStep, iLineSpace = 0):
        bSuccess = False 

        self.LineSpacer_yOffset = iLineSpace
        if self.FontSize + iStep < 1000:
            self.FontSize = self.FontSize + iStep 
            self.Image = self.DrawTextBox()
            bSuccess = True 

        return bSuccess

def CalcTotalBoxHeight(boxes):
    iTotalBoxHeight = 0

    for box in boxes:
        iTotalBoxHeight = iTotalBoxHeight + box.Image.height

    return iTotalBoxHeight

def CalcSpaceHeight(iMaxHeight, boxes):
    iSpaceHeight = 0
    
    iSpaceHeight = int((iMaxHeight - CalcTotalBoxHeight(boxes))/(len(boxes)))

    return iSpaceHeight

def PositionBoxesVertically(BGProfile,
                            Boxes = [], 
                            xOffset = 0):
    bg = BGImageHH(BGProfile)
    yOffset = bg.TitleBoxTop_yOffset
    iTotalBoxHeight = 0
    yLineSpace = 0

    MINSPACERHEIGHT = 13

    if len(Boxes) > 0:
    # 1. Attempt to fit title sections at max font sizes 

    # 2. If title sections don't fit, shrink fonts proportionately by 
    #    .5 and try again.

        iTotalBoxHeight = CalcTotalBoxHeight(Boxes)
        if iTotalBoxHeight > bg.MaxHeight or CalcSpaceHeight(bg.MaxHeight, Boxes) < MINSPACERHEIGHT:
            for box in Boxes:
                box.ShrinkText(.5)
            iTotalBoxHeight = CalcTotalBoxHeight(Boxes)  

    # 3. If title sections don't fit, use plain header background 
    #    and try again.
            if iTotalBoxHeight > bg.MaxHeight or CalcSpaceHeight(bg.MaxHeight, Boxes) < MINSPACERHEIGHT:
                bg = BGImagePH(BGProfile)
                yOffset = bg.TitleBoxTop_yOffset
                iTotalBoxHeight = CalcTotalBoxHeight(Boxes)

    # 4. If title sections still don't fit, keep shrinking fonts 
    #    proportionately until they do.
                if iTotalBoxHeight > bg.MaxHeight:
                    bBreak = False 
                    while iTotalBoxHeight > bg.MaxHeight or bBreak:
                        for box in Boxes:
                            if not box.ShrinkText(.5):
                                bBreak = True
                        iTotalBoxHeight = CalcTotalBoxHeight(Boxes)


    #divide up remaining vert space between boxes
    yLineSpace = CalcSpaceHeight(bg.MaxHeight, Boxes)

    # draw the text boxes
    BGImg = bg.Image
    iyOffsetLine = bg.TitleBoxTop_yOffset
    for box in Boxes:
        box.DrawText(iLineSpace = yLineSpace)
        BGImg.alpha_composite(box.Image, (xOffset, iyOffsetLine))
        iyOffsetLine = iyOffsetLine + box.Image.height + yLineSpace

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

    # use to off-center horizontally.
    width_offset = 27

    if isinstance(ImgTxtGen, Generator):
        # calculate text size score
        dScore = CalcTextSizeScore(' '.join(ImgTxtGen.ImgTxt.split('\n')))

        AuthorTemplate = ImgTxtGen.Template.AuthorLine

        # draw author name
        AuthorNameSection = TitleSection(ImgTxtGen.AuthorName,
                                     sFontName = AuthorTemplate.FontName,
                                     iFontSize = AuthorTemplate.FontMaxSize,
                                     iMaxRows = AuthorTemplate.MaxRows,
                                     Color = BGProfile.AuthorNameColor)
        AuthorNameSection.DrawText()
        
        TitleBoxes = []

        #draw title lines
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

                section = TitleSection(line.LineText,
                                       sFontName = line.FontName,
                                       iFontSize = line.FontMaxSize,
                                       iMaxRows = line.MaxRows,
                                       Color = Color)
                section.DrawText()

            #if dScore > 23:
            #    BGProfile.UsePlainheader()

                TitleBoxes.append(section)

        # get bg image and combine with text boxes
        ImgBase = PositionBoxesVertically(BGProfile = BGProfile,
                                          Boxes = TitleBoxes,
                                          xOffset = XOFFSET + width_offset)

        # combine the author name and base images
        ImgBase.alpha_composite(AuthorNameSection.Image, (XOFFSET + width_offset, 560))

        # save the edited image
        RGBImgOut = ImgBase.convert('RGB')

    return RGBImgOut
