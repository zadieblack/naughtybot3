#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# titletemplates module

from util import *

class TitleLine():
    def __init__(self, OrderNum = 1, 
                 FontName = "", 
                 FontMaxSize = 75,
                 MaxHeight = 78, 
                 MaxRows = 1,
                 yOffset = 234,
                 ColorType = LineColorType.MainTitle,
                 AllCaps = False):
        #self.ID = 0
        self.OrderNum = OrderNum
        self.FontName = FontName
        self.FontMaxSize = FontMaxSize
        self.MaxHeight = MaxHeight
        self.MaxRows = MaxRows 
        self.yOffset = yOffset
        self.LineText = ""
        self.ColorType = ColorType
        self.AllCaps = AllCaps

class TitleTemplate():
    def __init__(self, ID):
        self.ID = ID

        self.Lines = []

        self.AuthorLine = TitleLine(OrderNum = 0, 
                                    FontName = "Lapidary 333 Bold Italic.otf",
                                    FontMaxSize = 16,
                                    MaxHeight = 78,
                                    MaxRows = 1,
                                    yOffset = 540)

    def AddLine(self, OrderNum, FontName, FontMaxSize, MaxHeight, MaxRows, yOffset, ColorType,AllCaps = False):
        self.Lines.append(TitleLine(OrderNum,FontName,FontMaxSize,MaxHeight,MaxRows,yOffset,ColorType,AllCaps = AllCaps))
    
    def AddLineText(self, stxt):
        TxtLines = stxt.split("\n")

        i = 0
        while i < len(TxtLines) and i < len(self.Lines):
            if self.Lines[i].AllCaps:
                self.Lines[i].LineText = TxtLines[i].upper()
            else:
                self.Lines[i].LineText = TxtLines[i]
            i = i + 1

    def ClearLineText(self):
        for line in self.Lines:
            line.LineText = ""

class TitleTemplateHHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 0)

        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 24,
                     MaxHeight = 308,
                     MaxRows = 4,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)


class TitleTemplatePHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 1)
        self.AddLine(TitleLine(OrderNum = 1,
                               FontName = "Walpurgis Night.otf",
                               MaxRows = 5,
                               MaxHeight = 392))

# SHORT TOP LINE
# transition
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate1(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 0)

        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 22,
                     MaxHeight = 109,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)

        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 58,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText)

        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 17,
                     MaxHeight = 115,
                     MaxRows = 2,
                     yOffset = 410,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# MEDIUM TOP LINE
# trans
# MEDIUM BOTTOM LINE
# possible subtitle
class TitleTemplate2(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 0)

        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxHeight = 62,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)

        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 38,
                     MaxRows = 1,
                     yOffset = 260,
                     ColorType = LineColorType.SmallText)

        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxHeight = 116,
                     MaxRows = 2,
                     yOffset = 300,
                     ColorType = LineColorType.MainTitle)

        self.AddLine(OrderNum = 4,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 38,
                     MaxRows = 1,
                     yOffset = 440,
                     ColorType = LineColorType.SmallText)
        

