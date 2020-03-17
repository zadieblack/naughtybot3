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

COVER_PATH = "title/resources/cover_images/"
FONT_PATH = "title/resources/fonts/"
MAX_IMG_NUM = 24
RESOLUTION = 4.167
LOWERTITLETEXTBOUND = 527
MAXWIDTH = 910
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
    #print("GetBGImg() Attemption to open file " + sFileName)
    try:
        BGImg = Image.open(COVER_PATH + sFileName).convert('RGBA')
    except IOError as e:
        print("***ERROR***\nFile save failed in GetBGImg()\n" + e.strerror)
     
    return BGImg

class BGImageHH:
    TitleBoxTop_yOffset = 210
    TitleBoxBottom_yOffset = 525
    FileSuffix = "hh"

    def __init__(self, BGProfile):
        self.MaxHeight = self.TitleBoxBottom_yOffset - self.TitleBoxTop_yOffset
        self.FileName = BGProfile.FileName + "_hh.jpg"
        self.Image = GetBGImg(self.FileName)

class BGImagePH:
    TitleBoxTop_yOffset = 118
    TitleBoxBottom_yOffset = 525
    FileSuffix = "hh"

    def __init__(self, BGProfile):
        self.MaxHeight = self.TitleBoxBottom_yOffset - self.TitleBoxTop_yOffset
        self.FileName = BGProfile.FileName + "_ph.jpg"
        self.Image = GetBGImg(self.FileName)

def GetTextLineSize(font, sLine):
    width, height = (0,0)
    off_width, off_height = (0,0)

    width, height = font.getsize(sLine)
    off_width, off_height = font.getoffset(sLine)

    width = width + off_width 
    height = height - off_height

    return width, height

def CalcMinSpacerHeight(TitleBoxes):
    iMinSpacerHeight = 0

    aDescenderHeights = []

    iLastDescender = 0

    if len(TitleBoxes) > 2:
        for boxno, box in enumerate(TitleBoxes):
            (ascender, descender) = box.Font.getmetrics()

            # first title line, ignore descender
            if boxno == 0:
                pass
            else:
                aDescenderHeights.append(descender)
        if len(aDescenderHeights) > 1:
            iMinSpacerHeight = sorted(aDescenderHeights)[-2]

    elif len(TitleBoxes) == 2:
        iLine1Descender = TitleBoxes[0].Font.getmetrics()[1]
        iLine2Ascender = TitleBoxes[1].Font.getmetrics()[0]
        if iLine1Descender > iLine2Ascender:
            iMinSpacerHeight = iLine2Ascender 
        else:
            iMinSpacerHeight = iLine1Descender
    else:
        iMinSpacerHeight = 0

    iMaxSpacerHeight = CalcMaxSpacerHeight(TitleBoxes)

    if iMinSpacerHeight > iMaxSpacerHeight:
        iMinSpacerHeight = iMaxSpacerHeight 

    return iMinSpacerHeight

def CalcMaxSpacerHeight(TitleBoxes):
    iMaxSpacerHeight = 0 

    for boxno, box in enumerate(TitleBoxes):
        if boxno == 0:
            iMaxSpacerHeight = box.Height 
        else:
            if box.Height > iMaxSpacerHeight:
                iMaxSpacerHeight = box.Height 

    return iMaxSpacerHeight

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
    iLastWhtSpc = 0
    iSubStart = 0
    sLineSoFar = ""
    sLastValidLine = ""

    for charno, char in enumerate(sText):
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

            if iLastWhtSpc < iSubStart:
                iLastWhtSpc = int((charno - iSubStart)/2) 
                
            sLastValidLine = sText[iSubStart:iLastWhtSpc]
            
            # add the last valid text as a new line
            Lines.append(LineOfText(sLastValidLine, len(Lines) + 1))

            # move substring start forward and reset substring values
            iSubStart = iLastWhtSpc + 1
            sLastValidLine = ""
            sLineSoFar = sText[iSubStart:charno + 1]

    Lines.append(LineOfText(sLineSoFar, len(Lines) + 1))        

    return Lines

def CalcBoxHeight(sFontName, iMaxFontSize, iMaxRows, Color = (0,0,0,255)):
    iBoxHeight = 0

    Font = ImageFont.truetype(FONT_PATH + sFontName, size = iMaxFontSize, index = 0)
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
        self.FontFileName = FONT_PATH + self.FontName
        self.FontSize = iFontSize
        self.AdjFontSize = round(int(self.FontSize * RESOLUTION))
        self.MaxRows = iMaxRows
        self.Color = Color
        self.BoundingBoxWidth = MAXWIDTH
        self.BoundingBoxHeight = CalcBoxHeight(self.FontName, self.AdjFontSize, self.MaxRows) 
        self.TotLineHeight = 0
        self.DecreaseSizeBy = 3
        self.VertSepProp = 4
        self.TotalLineSpace = self.BoundingBoxHeight

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
            self.SetFont()
            self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)
            self.TotLineHeight = self.CalcTotLineHeight()

    def SetFont(self):
        #print(" - SetFont() for [" + self.Text + "]. Font is [" + self.FontName + "],  size = " + str(self.FontSize))
        self.Font = ImageFont.truetype(FONT_PATH + self.FontName, size = round(int(self.FontSize * RESOLUTION)), index = 0)

    def SetDimensions(self):
        ImgTxt = None 

        # how much the text in the box is offset from the box
        xOffset = 0     #.027
        yOffset = 0     #.027

        self.SetFont()
        self.Height = 0
     
        if len(self.Lines) > 1:
            self.LineSpace = self.TotalLineSpace / (len(self.Lines) - 1)
        else:
            self.LineSpace = 0

        ascender, descender = (0, 0)
        pad_width, pad_height = (0, 0)
        for iCount, line in enumerate(self.Lines):
            start_x, start_y = (0,0)
            adj_width, adj_height = (0, 0)

            if line.Text.isspace() or line.Text == "":
                adj_width, adj_height = GetTextLineSize(self.Font, "a")
                adj_height = adj_height / 2
            else:
                ascender, descender = self.Font.getmetrics()
                adj_width, adj_height = GetTextLineSize(self.Font, line.Text)
                
                # for some reason Pillow will not start drawing the text at (0,0).
                # you must specify (0, 0 - offset). 

                pad_width, pad_height = self.Font.getoffset(line.Text)
                self.Height = self.Height - pad_height

                # calculate top left corner (x,y) of text
                start_x = ((self.BoundingBoxWidth - adj_width)/2)
                start_y = (self.Height)

                line.StartXY = (start_x, start_y)

                #print(" - Setting dimensions for line #" + str(iCount) + ": [" + line.Text + "]")
                #print("  -- self.Height (top y coord) = " + str(self.Height))
                #print("  -- (pad w, pad h) = " + str((pad_width, pad_height)))
                #print("  -- top left coord (x, y) = " + str(( start_x, start_y)))
                #print("  -- (adj W, adj H) = " + str((adj_width, adj_height))) 
                #print("  -- (ascender, descender) = " + str((ascender, descender))) 
                #print("  -- bottom right coord (x, y) = " + str((start_x + adj_width, start_y + adj_height)))
                
            self.Height = self.Height + ascender + descender
            if iCount < len(self.Lines) - 1:
                self.Height = self.Height + int(round(descender * .4))
                #print("  -- Adding self.LineSpace = " + str(self.LineSpace) + ", (self.LineSpace * 1/2) = " + str((self.LineSpace * .5)))

        #print(" - Final self.Height value = " + str(self.Height))

    def DrawText(self, iTotalLineSpace = -1):
        if iTotalLineSpace >= 0:
            self.TotalLineSpace = iTotalLineSpace
        self.SetDimensions()

    def ShrinkText(self, iStep, iTotalLineSpace = -1):
        bSuccess = False 
        if iTotalLineSpace >= 0:
            self.TotalLineSpace = iTotalLineSpace
        if self.FontSize - iStep > 0:
            self.FontSize = self.FontSize - iStep 
            self.SetDimensions()
            bSuccess = True

        return bSuccess

    def GrowText(self, iStep, iTotalLineSpace = -1):
        bSuccess = False 

        if iTotalLineSpace >= 0:
            self.TotalLineSpace = iTotalLineSpace
        if self.FontSize + iStep < 1000:
            self.FontSize = self.FontSize + iStep
            self.SetDimensions()
            bSuccess = True 

        return bSuccess

    def DrawLines(self, draw, xOffset = 0, yOffset = 0):
        for lineno, line in enumerate(self.Lines):
            draw.text((line.StartXY[0] + xOffset, line.StartXY[1] + yOffset),
                      line.Text, 
                      font = self.Font, 
                      fill = self.Color)

# Calculate the total box height WITH or WITHOUT spaces 
def CalcTotalBoxHeight(boxes, bNoSpaces = False):
    iTotalBoxHeight = 0

    iSpacerHeight = 0 
    if not bNoSpaces:
        iSpacerHeight = CalcMinSpacerHeight(boxes)

    for boxno, box in enumerate(boxes):
        (ascender, descender) = box.Font.getmetrics()

        iTotalBoxHeight = iTotalBoxHeight + box.Height

        # first title line, ignore spacer
        if boxno == 0:
            pass
        else:
            iTotalBoxHeight = iTotalBoxHeight + iSpacerHeight

    return iTotalBoxHeight

def CalcSpaceHeight(iMaxHeight, boxes):
    iSpaceHeight = 0
    
    iSpaceHeight = int((iMaxHeight - CalcTotalBoxHeight(boxes))/(len(boxes)))

    return iSpaceHeight

def CreateImg(ImgTxtGen):
    # create Image object with the input image
    RGBImgOut = None 
    
    # get a random cover profile 
    BGProfile = GetBGProfileGenerator(ReqTags = ImgTxtGen.ReqTemplateTags,
                                      ExclTags = ImgTxtGen.ExclTemplateTags)
    print("BGProfile #" + str(BGProfile.ID) + " (" + BGProfile.FileName + ") selected")

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

        #init image objects
        BGImg = bg.Image

        if BGImg is not None:
            # calculate vertical spacing of title bounded text boxes
            #print("CreateImg() Init calculation of bounded text boxes.")
            xOffset = XOFFSET + width_offset
            yOffset = bg.TitleBoxTop_yOffset
            iTotalBoxHeight = 0
            yLineSpace = 0

            if len(TitleBoxes) > 0:
                # draw the text boxes
                for box in TitleBoxes:
                    box.SetDimensions()

                # the minimum vert space height should be the 
                # height of the largest descender. 
                iMinSpacerHeight = CalcMinSpacerHeight(TitleBoxes) 

            # 1. Attempt to fit title sections at max font sizes 

            # 2. If title sections don't fit, use plain header background 
            #    and try again.
                iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)
                iTotalBoxHeightNoSpaces = CalcTotalBoxHeight(TitleBoxes, bNoSpaces = False)

                if iTotalBoxHeightNoSpaces > bg.MaxHeight + 50:
                    bg = BGImagePH(BGProfile)
                    BGImg = bg.Image
                    #print(" - Switched to plain header background.")

            # 3. If title sections don't fit, shrink fonts proportionately by 
            #    1 and try again.
                #print(" - iTotalHeight = " + str(iTotalBoxHeight) + ", bg.MaxHeight = " + str(bg.MaxHeight))

                if iTotalBoxHeight > bg.MaxHeight:
                    bBreak = False 
                    #print("- SetImage() Shrinking fonts proportionately.")
                    while iTotalBoxHeight > bg.MaxHeight:
                        #print(" -- iTotalBoxHeight = " + str(iTotalBoxHeight))
                        #print(" -- bg.MaxHeight = " + str(bg.MaxHeight))
                        for box in TitleBoxes:
                            if not box.ShrinkText(1):
                                bBreak = True
                                break 
                        if bBreak:
                            break
                        iTotalBoxHeight = CalcTotalBoxHeight(TitleBoxes)

                #calculate the starting height
                draw = ImageDraw.Draw(BGImg)

                iyOffsetLine = bg.TitleBoxTop_yOffset + int(round((bg.TitleBoxBottom_yOffset - bg.TitleBoxTop_yOffset - iTotalBoxHeight) / 2))
            
                #print("  -- Starting iyOffsetLine = " + str(iyOffsetLine))
                #print(" - Drawing title sections")
                # draw the text boxes
                for boxno, box in enumerate(TitleBoxes):
                    #print("  -- box.Text is [" + box.Text + "]")
                    #print("  -- box.Height = " + str(box.Height))
                    #print("  -- iyOffsetLine = " + str(iyOffsetLine))
                    box.DrawLines(draw, xOffset, iyOffsetLine)
                    iyOffsetLine = iyOffsetLine + box.Height + iMinSpacerHeight

                # draw author name
                AuthorTemplate = ImgTxtGen.Template.AuthorLine
 
                AuthorNameSection = TitleSection(ImgTxtGen.AuthorName,
                                                 sFontName = AuthorTemplate.FontName,
                                                 iFontSize = AuthorTemplate.FontMaxSize,
                                                 iMaxRows = AuthorTemplate.MaxRows,
                                                 Color = BGProfile.AuthorNameColor)
                AuthorNameSection.SetDimensions()
                AuthorNameSection.DrawLines(draw, xOffset, AUTHORNAME_YOFFSET)
        else:
            print("ERROR. File name '" + bg.FileName + "' not found for background " + str(bg))

    return  BGImg.convert("RGB")