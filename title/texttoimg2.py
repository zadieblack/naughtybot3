#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
from PIL import Image, ImageDraw, ImageFont
from random import *
from util import *

PATH = "title/cover_stuff/"
MAX_IMG_NUM = 24

BGImgQ = HistoryQ(iQSize = 5)




def WrapText(sText, font, max_line_width):
     # break string into multiple lines that fit max_line_width
     # and return an array of strings
     Lines = []
     
     bEndOfText = False
     iLastWhtSpc = 0
     iLineStart = 0
     while not bEndOfText:
          width_of_line = 0
          iLastWhtSpc = iLineStart
          
          for charno in range(iLineStart, len(sText)):
               if sText[charno].isspace() or sText[charno] == "-":
                    iLastWhtSpc = charno
               char_size = font.getsize(sText[charno])
               width_of_line += char_size[0]
               
               if sText[charno] == "\n" or width_of_line >= max_line_width:
                    if iLastWhtSpc >= iLineStart:
                         Lines.append(sText[iLineStart:iLastWhtSpc])
                         iLineStart = iLastWhtSpc + 1
                         break
                    else:
                         iLastWhtSpc = int((charno - iLineStart)/2) 
                         Lines.append(sText[iLineStart:iLastWhtSpc])
                         iLineStart = iLastWhtSpc + 1
                         break
               else:
                    if charno == len(sText) - 1:
                         bEndOfText = True
                         Lines.append(sText[iLineStart:len(sText)])
                         break 
     
     return Lines

# Guesstimate an initial font size based on the # of characters         
def GuesstimateFontSize(sText):
    iFontSize = 3
  
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

    return iFontSize 

class BlockOfText():
    def __init__(self, sText, sFontName, BoundingBoxSize):
        self.Text = sText 
        self.FontName = sFontName
        self.BoundingBoxWidth = BoundingBoxSize[0]
        self.BoundingBoxHeight = BoundingBoxSize[1] 
        self.TotalLineHeight = 0
        self.DecreaseSizeBy = 3
        self.FontSize = GuesstimateFontSize(sText)
        self.Font = ImageFont.truetype(PATH + self.FontName, size = self.FontSize, index = 0)
        
        # wrap the text based on the bounding text box's width
        self.Lines = WrapText(self.Text, self.Font, self.BoundingBoxWidth)
       
        # shrink font until lines do not exceed bounding text box's height
        self.FitTextToBox()
        
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

def FormatText(sText, BoxWidth, BoxHeight, Color):
    Lines = []
     
    # how much the text in the box is offset from the box
    xOffset = 0     #.027
    yOffset = 0     #.027
     
    # set width and height of the bounding text box
    offset_width = round(BoxWidth - (BoxWidth * xOffset * 2), 0)
    offset_height = round(BoxHeight - (BoxHeight * yOffset * 2), 0)

    TextBlock = BlockOfText(sText, 
                            "Lapidary 333 Bold Italic.otf", 
                            (offset_width, offset_height))
               
    ImgTxt = Image.new('RGBA', (BoxWidth, BoxHeight))
    draw = ImageDraw.Draw(ImgTxt)
               
    y_text = 0
    for x in range(0, len(TextBlock.Lines)):
        width, height = (0, 0)
        if TextBlock.Lines[x].isspace() or TextBlock.Lines[x] == "":
            width, height = TextBlock.Font.getsize("a")
            height = height / 2
        else:
            width, height = TextBlock.Font.getsize(TextBlock.Lines[x])
            width = width - (width * .05) # for some reason width for this font is a little off, so we tack on a 5% fudge

            #draw.text(((offset_width - width)/2, (offset_height - TextBlock.TotalLineHeight)/2 + y_text), 
            #          TextBlock.Lines[x], 
            #          font = TextBlock.Font, 
            #          fill = Color)

            draw.text(((offset_width - width)/2, 0), 
                      TextBlock.Lines[x], 
                      font = TextBlock.Font, 
                      fill = Color)
        y_text += height
     
    return ImgTxt

def DrawBoundingTxtBox(BoxWidth, BoxHeight, sText, Color):
    ImgText = FormatText(sText, BoxWidth, BoxHeight, Color)
     
    return ImgText
     
def GetBGImg(iPicNo = 0):
     BGImg = None 
     
     #if iPicNo == 0:
     #     iPicNo = randint(1, MAX_IMG_NUM)

     #     while not BGImgQ.PushToHistoryQ(iPicNo):
     #          iPicNo = randint(1, MAX_IMG_NUM)

     try:
          BGImg = Image.open(PATH + "saxophone_hh.png").convert('RGBA')
     except IOError as e:
          print("***ERROR***\nFile save failed in SaveImg()\n" + e.strerror)
     
     return BGImg

def CreateImg(TitleTweet):
    # create Image object with the input image
    RGBImgOut = None 

    if isinstance(TitleTweet, GeneratedTitleTweet):
        ImgBase = GetBGImg()
     
        # draw author name
        color = 'rgba(0, 0, 0, 255)' # color should eventually come from template
        
        ImgAuthorNameTxt = FormatText(TitleTweet.AuthorName(),
                                      BoxWidth = 831, #571, 
                                      BoxHeight = 71, #70)
                                      Color = color)
        #ImgAuthorNameTxt = DrawText(ImgBase.size, 
        #                            .643,  #571 1600 - 571 = 1029  1029/1600 = .643 
        #                            .928,   #70  971 - 70 = 901     901/971 = .928                           
        #                    TitleTweet.AuthorName().strip(), 
        #                    color)

        ## draw title
      
        # combine the text and base images
        ImgBase.paste(ImgAuthorNameTxt, (70, 571), mask = ImgAuthorNameTxt)
      
        # save the edited image
        RGBImgOut = ImgBase.convert('RGB')
        #RGBImgOut.name = "tweetimg.jpg"

    return RGBImgOut
