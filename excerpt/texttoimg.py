#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# Text-to-Image module

import os, sys, time
from PIL import Image, ImageDraw, ImageFont
from random import *
from excerpt.util import *

PATH = "excerpt/resources/"
FONT = "NoticiaText-Regular.ttf"
MAX_IMG_NUM = 38

BGImgQ = HistoryQ(iQSize = 5)

def SaveImg(img, filename = ""):
	try:
		if filename == "":
			img.save('test' + str(time.time()) + '.jpg')
		else:
			img.save(filename)
	except IOError as e:
		print("***ERROR***\nFile save failed in SaveImg()\n" + e.reason)
		
		
def WrapText(sText, font, offset_width):
	# break string into multi-lines that fit base_width
	Lines = []
	
	bEndOfText = False
	iLastWhtSpc = 0
	iLineStart = 0
	
	#this loop is complex and very carefully engineered. don't fuck with it unless you're confident
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
					#line is too wide, break at last white space and append to Lines
					Lines.append(sText[iLineStart:iLastWhtSpc])
					iLineStart = iLastWhtSpc + 1
					break
				else:
					#word too wide, break in the middle and append to Lines
					iLastWhtSpc = int((x - iLineStart)/2) 
					Lines.append(sText[iLineStart:iLastWhtSpc])
					iLineStart = iLastWhtSpc + 1
					break
			else:
				#line is not too wide, keep going
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
	
	xOffset = .018
	yOffset = .018
	
	offset_width = round(base_width - (base_width * xOffset * 2), 0)
	offset_height = round(base_height - (base_height * yOffset * 2), 0)
	
	iFontSize = 30
	
	iTextLen = len(sText)
	if iTextLen <= 140:
		iFontSize = 95
	elif iTextLen <= 185:	
		iFontSize = 80
	elif iTextLen <= 255:	
		iFontSize = 70
	elif iTextLen <= 335:	
		iFontSize = 60
	elif iTextLen <= 520:	
		iFontSize = 55
	elif iTextLen <= 685:
		iFontSize = 48
	elif iTextLen <= 1000:
		iFontSize = 40
	elif iTextLen <= 1400:
		iFontSize = 34
	else: 
		iFontSize = 30

	#print("FormatText() Starting font size is " + str(iFontSize))
	
	font = ImageFont.truetype(PATH + FONT, size = iFontSize)
	
	iTotLineHeight = 0
	
	Lines = WrapText(sText, font, offset_width)
	
	iTotLineHeight = CalcTotalLineHeight(Lines, font)
	
	#if the height of our lines exceeds the height of the image area, reduce font and try again
	while iTotLineHeight > offset_height:
		print("FormatText() offset_height exceeded for font size " + str(iFontSize) + ", shrinking font by 1 and trying again")
		iFontSize += (-1)
		
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

			draw.text((int(base_width * xOffset), round((offset_height - iTotLineHeight)/2) + y_text), Lines[x], font=font, fill=color)
		y_text += height
	
	return ImgTxt

def DrawText(size, sText, color): 
	bck_width = size[0]
	bck_height = size[1]
	
	stest = "d e"
	ImgTxt = FormatText(sText, (bck_width - int(bck_width * .075), bck_height - int(bck_height * .075)), color)
	
	ImgFrame = Image.new('RGBA', size, (255,255,255,0))
	
	ImgFrame.paste(ImgTxt, (int((bck_width - ImgTxt.size[0])/2), int((bck_height - ImgTxt.size[1])/2)))

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
		print("***ERROR***\nFile save failed in SaveImg()\n" + e.reason)
	
	return BGImg

def CreateImg(sText):
	# create Image object with the input image
	
	ImgBase = GetBGImg()
	
	color = 'rgb(255, 255, 255)' # black color
	
	ImgTxt = DrawText(ImgBase.size, sText, color)
	 
	# composite the text and base images

	ImgOut = Image.alpha_composite(ImgBase, ImgTxt)
	 
	# convert to jpeg
	
	ImgOut = ImgOut.convert('RGB')
	 
	return ImgOut














