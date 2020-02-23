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
    
    def AddLineText(self, stxt = ""):
        TxtLines = []
        if len(stxt) > 0:
            TxtLines = stxt.split("\n")

        i = 0
        while i < len(TxtLines) and i < len(self.Lines):
            if self.Lines[i].AllCaps:
                self.Lines[i].LineText = TxtLines[i].upper()
            else:
                self.Lines[i].LineText = TxtLines[i]
            i = i + 1

    def ClearLineText(self):
        if len(self.Lines) > 0:
            for line in self.Lines:
                line.LineText = ""

class TitleTemplateHHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 0)

        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 21,
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
# of a
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate1(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 1)

        # Short very large top line
        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 24,
                     MaxHeight = 109,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)

        # Small cursive trans
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 58,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxHeight = 115,
                     MaxRows = 2,
                     yOffset = 410,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# MEDIUM TOP LINE
# of a
# MEDIUM BOTTOM LINE
# possible subtitle
class TitleTemplate2(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 2)

        # Large medium-length top line 
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxHeight = 62,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)

        # Small short second line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 38,
                     MaxRows = 1,
                     yOffset = 260,
                     ColorType = LineColorType.SmallText)

        # Large medium third line
        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxHeight = 116,
                     MaxRows = 2,
                     yOffset = 300,
                     ColorType = LineColorType.SecondTitle)

        # Small possible tag-line
        self.AddLine(OrderNum = 4,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 38,
                     MaxRows = 1,
                     yOffset = 440,
                     ColorType = LineColorType.SmallText)
        

# FEMALE NAME
# Shows A
# MEDIUM CENTER LINE
# Her
# CUNNING STUNT
class TitleTemplate3(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 3)

        # Large short single-word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 20,
                     MaxHeight = 63,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)
        
        # Small trans middle line
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxHeight = 30,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length center line
        self.AddLine(OrderNum = 3,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 14,
                     MaxHeight = 50,
                     MaxRows = 2,
                     yOffset = 260,
                     ColorType = LineColorType.SecondTitle)

        # Small transition line
        self.AddLine(OrderNum = 4,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxHeight = 30,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length bottom line
        self.AddLine(OrderNum = 5,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 16,
                     MaxHeight = 48,
                     MaxRows = 1,
                     yOffset = 440,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line
class TitleTemplate4(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 4)

        self.AddLine(OrderNum = 1,
                     FontName = "Adorable MLSJN.ttf",
                     FontMaxSize = 16,
                     MaxHeight = 47,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.SecondTitle)

        self.AddLine(OrderNum = 2,
                     FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 20,
                     #MaxHeight = 192, #for two lines
                     MaxHeight = 79,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.MainTitle)

        self.AddLine(OrderNum = 3,
                     FontName = "POORICH.ttf",
                     FontMaxSize = 11,
                     MaxHeight = 41,
                     MaxRows = 1,
                     yOffset = 410,
                     ColorType = LineColorType.MainTitle)

# ** Medieval **
# SHORT TOP LINE
# transition
# SHORT BOTTOM LINE
class TitleTemplate5(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 5)

        # Large single word or short top line (medieval)
        self.AddLine(OrderNum = 1,
                     FontName = "CELTG__.ttf",
                     FontMaxSize = 24,
                     MaxHeight = 109,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Smaller single word trans (medieval)
        self.AddLine(OrderNum = 2,
                     FontName = "LaserLondon.ttf",
                     FontMaxSize = 26,
                     MaxHeight = 58,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText)

        # Large medium-length bottom line (medieval)
        self.AddLine(OrderNum = 3,
                     FontName = "OLDENGL.ttf",
                     FontMaxSize = 24,
                     MaxHeight = 115,
                     MaxRows = 1,
                     yOffset = 410,
                     ColorType = LineColorType.SecondTitle)

# SHORT TOP LINE
# MEDIUM LINE
# by the
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate6(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 6)

        # Large single word or short top line
        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 30,
                     MaxHeight = 109,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)

        # Smaller medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxHeight = 58,
                     MaxRows = 1,
                     yOffset = 342,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Medium long 1 or 2 line bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 16,
                     MaxHeight = 115,
                     MaxRows = 2,
                     yOffset = 410,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# ** Punchline **
# MEDIUM TOP LINE
# MEDIUM BOTTOM LINE
class TitleTemplate7(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 7)

        # Small medium length top-line
        self.AddLine(OrderNum = 1,
                     FontName = "EccentricStd.otf",
                     FontMaxSize = 20,
                     MaxHeight = 109,
                     MaxRows = 1,
                     yOffset = 204,
                     ColorType = LineColorType.SecondTitle)

        # Large one or two line bottom line (punchline)
        self.AddLine(OrderNum = 2,
                     FontName = "TestarossaNF.ttf",
                     FontMaxSize = 24,
                     MaxHeight = 115,
                     MaxRows = 2,
                     yOffset = 410,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

# ** Conversational **
# Large long or multi-line line
class TitleTemplate8(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 8)

        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxHeight = 308,
                     MaxRows = 4,
                     yOffset = 204,
                     ColorType = LineColorType.MainTitle)