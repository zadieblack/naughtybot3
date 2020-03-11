#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
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
AUTHORNAME_YOFFSET = 560
MINSPACERHEIGHT = 13
VERT_SEP_PROP = 2                           # proportion of text height to use as 
                                            # separator between two lines of the 
                                            # the same type
                            

BGImgQ = HistoryQ(iQSize = 5)

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
    off_width, off_height = (0,0)

    width, height = font.getsize(sLine)
    off_width, off_height = font.getoffset(sLine)

    width = width + off_width 
    height = height - off_height

    return width, height

class LineOfText():
    def __init__(self, sText = "", iOrderNo = 0, iHeight = 0, iWidth = 0):
        self.Text = sText
        self.OrderNo = iOrderNo 
        self.StartXY = (0, 0)
        self.Height = iHeight
        self.Width = iWidth

def WrapText(sText, font, max_line_width):
    # break string into multiple lines that fit max_line_width
    # and return an array of strings
    Lines = []
    iNumLines = 0 
    #bEndOfText = False
    iLastWhtSpc = 0
    iSubStart = 0
    sLineSoFar = ""
    sLastValidLine = ""

    for charno, char in enumerate(sText):
        #width_of_line = 0
        #iLastWhtSpc = iSubStart
          
        if char.isspace() or char == "-":
            iLastWhtSpc = charno
            sLastValidLine = sText[iSubStart:iLastWhtSpc]

        sLineSoFar += char
            
        # if character is a line break or line is longer than max 
        # width
        if not len(sLineSoFar) == 0 and \
            (char == "\n" or \
             font.getsize(sLineSoFar)[0] >= max_line_width):
            # if there is no recent whitespace char but we are past
            # the max width, split the middle 

            print(" Line break on character # " + str(charno) + "!")
            print("  sLastValidLine is [" + sLastValidLine + "]")
            print("  iLastWhtSpc = " + str(iLastWhtSpc))
            print("  iSubStart = " + str(iSubStart))
            

            if iLastWhtSpc < iSubStart:
                iLastWhtSpc = int((charno - iSubStart)/2) 
                
            sLastValidLine = sText[iSubStart:iLastWhtSpc]
            
            # add the last valid text as a new line
            Lines.append(LineOfText(sLastValidLine, len(Lines) + 1))

            # move substring start forward and reset substring values
            iSubStart = iLastWhtSpc + 1
            sLastValidLine = ""
            sLineSoFar = sText[iSubStart:charno + 1]
            print("  sLineSoFar is [" + sLineSoFar + "]")

    Lines.append(LineOfText(sLineSoFar, len(Lines) + 1))        

    return Lines

def CalcBoxHeight(sFontName, iMaxFontSize, iMaxRows, Color = (0,0,0,255)):
    iBoxHeight = 0

    print("Attempting to open font file " + PATH + sFontName)
    Font = ImageFont.truetype(PATH + sFontName, size = iMaxFontSize, index = 0)
    iLineHeight = GetTextLineSize(Font,"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")[1]

    iBoxHeight = (iLineHeight * iMaxRows) + (int(round(iLineHeight/VERT_SEP_PROP)) * (iMaxRows - 1))

    return iBoxHeight 

class TitleSection:
    def __init__(self, 
                 sText = "", 
                 sFontName = "", 
                 iFontSize = 10, 
                 iMaxRows = 1, 
                 Color = (0,0,0,255)):
        self.Text = sText
        self.FontName = sFontName
        self.FontFileName = PATH + self.FontName
        self.FontSize = iFontSize
        self.AdjFontSize = int(round(self.FontSize * RESOLUTION, 0))
        self.MaxRows = iMaxRows
        self.Color = Color
        self.BoundingBoxWidth = MAXWIDTH
        self.BoundingBoxHeight = CalcBoxHeight(self.FontName, self.AdjFontSize, self.MaxRows) 
        self.TotLineHeight = 0
        self.DecreaseSizeBy = 3
        self.VertSepProp = 4
        self.TotalLineSpace = 0

        self.Height = 0
        self.Width = 0
        self.LineSpace = 0
        self.Lines = []

        self.SetFont()

        # shrink font until lines do not exceed bounding text box's height
        self.FitTextToBox()

    def CalcTotLineHeight(self):
        iHeight = 0

        for line in self.Lines:
            if line.Text.isspace() or line.Text == "":
                iHeight += GetTextLineSize(self.Font, "a")[1] / 2
            else:
                iHeight += GetTextLineSize(self.Font, line.Text)[1]
          
        return iHeight

    def FitTextToBox(self):
        # wrap the text based on the bounding text box's width
        self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)

        # calculate the height of the text
        self.TotLineHeight = self.CalcTotLineHeight()

        while self.TotLineHeight > self.BoundingBoxHeight or len(self.Lines) > self.MaxRows:
            self.FontSize = (self.FontSize + (self.DecreaseSizeBy * (-1)))
            self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize * RESOLUTION, index = 0)
            self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)
            self.TotLineHeight = self.CalcTotLineHeight()

    def SetFont(self):
        self.Font = ImageFont.truetype(PATH + self.FontName, size = int(self.FontSize * RESOLUTION), index = 0)

    def SetDimensions(self):
        ImgTxt = None 

        # how much the text in the box is offset from the box
        xOffset = 0     #.027
        yOffset = 0     #.027

        self.SetFont()
     
        if len(self.Lines) > 1:
            self.LineSpace = self.TotalLineSpace / (len(self.Lines) - 1)
        else:
            self.LineSpace = self.TotalLineSpace

        pad_width, pad_height = (0, 0)
        for iCount, line in enumerate(self.Lines):
            start_x, start_y = (0,0)
            adj_width, adj_height = (0, 0)
            #ImgLine = Image.new('RGBA', (offset_width, offset_height), (0, 0, 0, 0))
            #draw = ImageDraw.Draw(ImgLine)

            if line.Text.isspace() or line.Text == "":
                adj_width, adj_height = GetTextLineSize(self.Font, "a")
                adj_height = adj_height / 2
            else:
                adj_width, adj_height = GetTextLineSize(self.Font, line.Text)
                
                # for some reason Pillow will not start drawing the text at (0,0).
                # you must specify (0, 0 - offset). (does this need to happen every time??)

                pad_width, pad_height = self.Font.getoffset(line.Text)
                self.Height = self.Height - pad_height

                # calculate top left corner (x,y) of text
                start_x = ((self.BoundingBoxWidth - adj_width)/2)
                start_y = (self.Height)

                line.StartXY = (start_x, start_y)

                #print(" - Setting dimensions for line #" + str(iCount) + ": [" + line + "]")
                #print("  -- self.Height (top y coord) = " + str(self.Height))
                #print("  -- pad W x H = " + str((pad_width, pad_height)))
                #print("  -- top left coord (x, y) = " + str(( start_x, start_y)))
                #print("  -- adj W x H = " + str((adj_width, adj_height))) 
                #print("  -- bottom right coord (x, y) = " + str((start_x + adj_width, start_y + adj_height)))
                
            self.Height = self.Height + adj_height
            if iCount < len(self.Lines) - 1:
                self.Height = self.Height + int(self.LineSpace * .5)

            #ImgTxt = Image.alpha_composite(ImgTxt, ImgLine)
            #ImgTxt.alpha_composite(ImgLine, (xOffset, iyOffsetLine))
            print("  -- self.LineSpace = " + str(self.LineSpace) + ", (self.LineSpace * 1/2) " + str((self.LineSpace * .5)))

        print(" - Final y_text value = " + str(self.Height))

    def DrawText(self, iTotalLineSpace = 0):
        self.TotalLineSpace = iTotalLineSpace
        self.SetDimensions()

    def ShrinkText(self, iStep, iTotalLineSpace = 0):
        bSuccess = False 

        self.TotalLineSpace = iTotalLineSpace
        if self.FontSize - iStep > 0:
            self.FontSize = self.FontSize - iStep 
            self.SetDimensions()
            bSuccess = True

        return bSuccess

    def GrowText(self, iStep, iTotalLineSpace = 0):
        bSuccess = False 

        self.TotalLineSpace = iTotalLineSpace
        if self.FontSize + iStep < 1000:
            self.FontSize = self.FontSize + iStep
            self.SetDimensions()
            bSuccess = True 

        return bSuccess

    def DrawLines(self, draw, xOffset = 0, yOffset = 0):
        for line in self.Lines:
            draw.text((line.StartXY[0] + xOffset, line.StartXY[1] + yOffset),
                      line.Text, 
                      font = self.Font, 
                      fill = self.Color)

def CalcTotalBoxHeight(boxes):
    iTotalBoxHeight = 0

    for box in boxes:
        iTotalBoxHeight = iTotalBoxHeight + box.Height

    return iTotalBoxHeight

def CalcSpaceHeight(iMaxHeight, boxes):
    iSpaceHeight = 0
    
    iSpaceHeight = int((iMaxHeight - CalcTotalBoxHeight(boxes))/(len(boxes)))

    return iSpaceHeight



def CreateImg(ImgTxtGen):
    # create Image object with the input image
    RGBImgOut = None 
    
    # get a random cover profile 
    BGProfile = GetBGProfileGenerator()

    sFileName = ""

    # use to off-center horizontally.
    width_offset = 17

    if isinstance(ImgTxtGen, Generator):
        TitleBoxes = []

        #color and format title lines
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

                TitleBoxes.append(section)

        # get bg image 
        bg = BGImageHH(BGProfile)

        # calculate vertical spacing of title bounded text boxes
        xOffset = XOFFSET + width_offset
        yOffset = bg.TitleBoxTop_yOffset
        iTotalBoxHeight = 0
        yLineSpace = 0

        if len(TitleBoxes) > 0:
        # 1. Attempt to fit title sections at max font sizes 

        # 2. If title sections don't fit, shrink fonts proportionately by 
        #    .5 and try again.

            iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)
            if iTotalBoxHeight > bg.MaxHeight or \
                CalcSpaceHeight(bg.MaxHeight, TitleBoxes) < MINSPACERHEIGHT:
                for box in TitleBoxes:
                    box.ShrinkText(.5)
                iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)  

        # 3. If title sections don't fit, use plain header background 
        #    and try again.
                if iTotalBoxHeight > bg.MaxHeight or CalcSpaceHeight(bg.MaxHeight, Boxes) < MINSPACERHEIGHT:
                    bg = BGImagePH(BGProfile)
                    #yOffset = bg.TitleBoxTop_yOffset
                    #iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)

        # 4. If title sections still don't fit, keep shrinking fonts 
        #    proportionately until they do.
                    if iTotalBoxHeight > bg.MaxHeight:
                        bBreak = False 
                        while iTotalBoxHeight > bg.MaxHeight or bBreak:
                            for box in TitleBoxes:
                                if not box.ShrinkText(.5):
                                    bBreak = True
                            iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)

        #divide up remaining vert space between boxes
        yLineSpace = CalcSpaceHeight(bg.MaxHeight, TitleBoxes)

        #init image objects
        BGImg = bg.Image
        draw = ImageDraw.Draw(BGImg)

        iyOffsetLine = bg.TitleBoxTop_yOffset

        # draw the text boxes
        for box in TitleBoxes:
            box.SetDimensions()
            box.DrawLines(draw, xOffset, iyOffsetLine)
            iyOffsetLine = iyOffsetLine + box.Height + yLineSpace

        # draw author name
        AuthorTemplate = ImgTxtGen.Template.AuthorLine
 
        AuthorNameSection = TitleSection(ImgTxtGen.AuthorName,
                                         sFontName = AuthorTemplate.FontName,
                                         iFontSize = AuthorTemplate.FontMaxSize,
                                         iMaxRows = AuthorTemplate.MaxRows,
                                         Color = BGProfile.AuthorNameColor)
        AuthorNameSection.SetDimensions()
        AuthorNameSection.DrawLines(draw, xOffset, AUTHORNAME_YOFFSET)

    return  BGImg
    #    # save the edited image
    #    RGBImgOut = ImgBase.convert('RGB')

    #return RGBImgOut

