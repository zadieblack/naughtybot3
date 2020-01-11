#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
from PIL import Image, ImageDraw, ImageFont
from random import *
from util import *

PATH = "title/resources/"
FONT = "Florsn35.ttf"
MAX_IMG_NUM = 24

BGImgQ = HistoryQ(iQSize = 5)

def SaveImg(img, filename = ""):
     try:
          if filename == "":
               img.save('test' + str(time.time()) + '.jpg')
          else:
               img.save(filename)
     except IOError as e:
          print("***ERROR***\nFile save failed in SaveImg()\n" + e.strerror)
          
          
def WrapText(sText, font, offset_width):
     # break string into multi-lines that fit base_width
     Lines = []
     
     bEndOfText = False
     iLastWhtSpc = 0
     iLineStart = 0
     while not bEndOfText:
          width_of_line = 0
          iLastWhtSpc = iLineStart
          
          for x in range(iLineStart, len(sText)):
               if sText[x].isspace() or sText[x] == "-":
                    iLastWhtSpc = x
               char_size = font.getsize(sText[x])
               width_of_line += char_size[0]
               
               if sText[x] == "\n" or width_of_line >= offset_width:
                    if iLastWhtSpc >= iLineStart:
                         Lines.append(sText[iLineStart:iLastWhtSpc])
                         iLineStart = iLastWhtSpc + 1
                         break
                    else:
                         iLastWhtSpc = int((x - iLineStart)/2) 
                         Lines.append(sText[iLineStart:iLastWhtSpc])
                         iLineStart = iLastWhtSpc + 1
                         break
               else:
                    if x == len(sText) - 1:
                         bEndOfText = True
                         Lines.append(sText[iLineStart:len(sText)])
                         break 
     
     return Lines
     
def CalcTotalLineHeight(Lines, font):
     iTotLineHeight = 0
     for line in Lines:
          if line.isspace() or line == "":
               iTotLineHeight += font.getsize("a")[1] / 2
          else:
               iTotLineHeight += font.getsize(line)[1]
          
     return iTotLineHeight
          
def FormatText(sText, size, color):
     Lines = []
     base_width = size[0]
     base_height = size[1]
     
     xOffset = .027
     yOffset = .027
     
     offset_width = round(base_width - (base_width * xOffset * 2), 0)
     offset_height = round(base_height - (base_height * yOffset * 2), 0)
     
     iFontSize = 3
     
     #print("FormatText() sText length: " + str(len(sText)))
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

          
     #print("FormatText() Starting font size is " + str(iFontSize))
     
     font = ImageFont.truetype(PATH + FONT, size = iFontSize, index = 0)
     
     iTotLineHeight = 0
     
     Lines = WrapText(sText, font, offset_width)
     
     iTotLineHeight = CalcTotalLineHeight(Lines, font)
     
     #if the height of our lines exceeds the height of the image area, reduce font and try again
     while iTotLineHeight > offset_height:
          print("FormatText() offset_height exceeded for font size " + str(iFontSize) + ", shrinking font by 3 and trying again")
          iFontSize += (-3)
          
          font = ImageFont.truetype(PATH + FONT, size = iFontSize)
          
          Lines = WrapText(sText, font, offset_width)
          
          iTotLineHeight = CalcTotalLineHeight(Lines, font)
          
     print("FormatText() Final font size is " + str(iFontSize))
               
     ImgTxt = Image.new('RGBA', (base_width, base_height), (0,0,0,95))
     draw = ImageDraw.Draw(ImgTxt)
               
     y_text = 0
     for x in range(0, len(Lines)):
          width, height = (0, 0)
          if Lines[x].isspace() or Lines[x] == "":
               width, height = font.getsize("a")
               height = height / 2
          else:
               width, height = font.getsize(Lines[x])
               width = width - (width * .05) # for some reason width for this font is a little off, so we tack on a 5% fudge

               #print("Base Width: [" + str(base_width) + "]  Offset Width: [" + str(offset_width) + "]  Line Width: [" + str(width) + "]  (Offset Width - Width)/2: [" + str((offset_width - width)/2) + "]")
               draw.text(((offset_width - width)/2, (offset_height - iTotLineHeight)/2 + y_text), Lines[x], font=font, fill=color)
          y_text += height
     
     return ImgTxt

def DrawText(size, sText, color): 
     bg_width = size[0]
     bg_height = size[1]
     
     stest = "d e"
     #print(stest[1].isspace()) 
     ImgTxt = FormatText(sText, (bg_width - int(bg_width * .075), bg_height - int(bg_height * .075)), color)
     
     ImgFrame = Image.new('RGBA', size, (255,255,255,0))
     
     ImgFrame.paste(ImgTxt, (int((bg_width - ImgTxt.size[0])/2), int((bg_height - ImgTxt.size[1])/2)))

     return ImgFrame
     
def GetBGImg(iPicNo = 0):
     BGImg = None 
     
     if iPicNo == 0:
          iPicNo = randint(1, MAX_IMG_NUM)

          while not BGImgQ.PushToHistoryQ(iPicNo):
               iPicNo = randint(1, MAX_IMG_NUM)

     try:
          BGImg = Image.open(PATH + "bg_" + str(iPicNo) + ".jpg").convert('RGBA')
     except IOError as e:
          print("***ERROR***\nFile save failed in SaveImg()\n" + e.strerror)
     
     return BGImg

def CreateImg(sText):
     # create Image object with the input image
     
     #for i in range(1, MAX_IMG_NUM + 1):
     #ImgBase = GetBGImg(iPicNo = i)
     ImgBase = GetBGImg()
     
     color = 'rgb(255, 255, 255)' # black color
     
     ImgTxt = DrawText(ImgBase.size, sText.strip(), color)
      
     # composite the text and base images
     ImgOut = Image.alpha_composite(ImgBase, ImgTxt)
      
     # save the edited image
      
     return ImgOut.convert('RGB')














