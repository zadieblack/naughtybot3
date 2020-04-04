#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# titletemplates module

from util import *

#                       *** RECOMMENDED FONT LIST ***
#
#       ~~ File Name ~~             ~~ Type ~~  ~~ Serif? ~~  ~~ Best Size ~~
# "Absinette W01 Regular.ttf"                        xx             25
# "Adorable MLSJN.ttf"              Script           xx             16
# "Amaze.ttf"                       Script           xx             12
# "Babes In Toyland NF.ttf"         All Caps         xx             23
# "CelticGaramond.ttf"              Old English      xx             24
# "Coventry Garden NF.ttf"          All Caps         xx             18
# "FreestyleScriptStd.otf"          Hand-written     xx             22
# "Helenium W01 Regular.ttf"        All Caps         xx             18
# "Lapidary 333 Bold Italic.otf"                     xx             16
# "LaserLondon.ttf"                                  xx             26
# "Lightfoot.ttf"                   All Caps         xx             26
# "MutterKrauseNormal.ttf"                           xx             16
# "oldengl.ttf"                     Old English      xx             24
# "PerpetuaStd.otf"                 All Caps         xx             19
# "poorrichard.ttf"                                  xx             12
# "Quaint Gothic SG OT Regular.ttf" All Caps         xx             20
# "Sabado Regular.otf"              Small Caps       xx             18
# "TestarossaNF.ttf"                All Caps                        24
# "Verona-ExtraBold.otf"                             xx             22
# "Walpurgis Night.otf"             Small Caps       xx             21
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16
# "blah.otf"                        All Caps         xx             16

class TitleLine():
    def __init__(self, OrderNum = 1, 
                 FontName = "", 
                 FontMaxSize = 16,
                 MaxRows = 2,
                 ColorType = LineColorType.MainTitle,
                 AllCaps = False):
        #self.ID = 0
        self.OrderNum = OrderNum
        self.FontName = FontName
        self.FontMaxSize = FontMaxSize
        self.MaxRows = MaxRows 
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
                                    MaxRows = 1)

    def AddLine(self, OrderNum = 1, FontName = "", FontMaxSize = 16, MaxRows = 2, ColorType = None, AllCaps = False):
        self.Lines.append(TitleLine(OrderNum = OrderNum,FontName = FontName,FontMaxSize = FontMaxSize,MaxRows = MaxRows,ColorType = ColorType,AllCaps = AllCaps))
    
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

        self.AddLine(OrderNum = 0,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 21,
                     MaxRows = 4,
                     ColorType = LineColorType.MainTitle)


class TitleTemplatePHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = -1)
        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 21,
                     MaxRows = 5,
                     ColorType = LineColorType.MainTitle)

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
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small cursive trans
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 2,
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
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small short second line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Large medium third line
        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

        # Small possible tag-line
        self.AddLine(OrderNum = 4,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
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
                     FontMaxSize = 23,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)
        
        # Small trans middle line
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length center line
        self.AddLine(OrderNum = 3,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 17,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

        # Small transition line
        self.AddLine(OrderNum = 4,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length bottom line
        self.AddLine(OrderNum = 5,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line
# Templates: 7
class TitleTemplate4(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 4)

        # Medium long line or two lines normal type
        self.AddLine(OrderNum = 1,
                     FontName = "MutterKrauseNormal.ttf" ,
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Large medium length line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 3,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

# ** Medieval **
# SHORT TOP LINE
# transition
# SHORT BOTTOM LINE
class TitleTemplate5(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 5)

        # Large single word or short top line (medieval)
        self.AddLine(OrderNum = 1,
                     FontName = "CelticGaramond.ttf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Smaller single word trans (medieval)
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 14,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Large medium-length bottom line (medieval)
        self.AddLine(OrderNum = 3,
                     FontName = "oldengl.ttf",
                     FontMaxSize = 22,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

# SHORT TOP LINE
# MEDIUM LINE
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate6(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 6)

        # Large single word or short top line
        self.AddLine(OrderNum = 1,
                     FontName = "Walpurgis Night.otf",
                     FontMaxSize = 30,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Smaller medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Medium long 1 or 2 line bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 16,
                     MaxRows = 2,
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
                     #FontName = "Babes In Toyland NF.ttf",
                     FontName = "Lightfoot.ttf",
                     FontMaxSize = 23,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Large one or two line bottom line (punchline)
        self.AddLine(OrderNum = 2,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)
                     #This needs extra space to work

# ** Conversational **
# Large long or multi-line line
# Generators: 143
class TitleTemplate8(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 8)

        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 4,
                     ColorType = LineColorType.MainTitle)

# SHORT TOP LINE
# MEDIUM LINE
# LONG TWO-ROW BOTTOM LINE
# Generators: 124
class TitleTemplate9(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 9)

        # Small single word or short top line
        self.AddLine(OrderNum = 1,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long 1 or 2 line bottom line
        self.AddLine(OrderNum = 4,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# ** Punchline **
# LONG TOP LINE
# MEDIUM BOTTOM LINE
class TitleTemplate10(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 10)

        # Small medium length top-line
        self.AddLine(OrderNum = 1,
                     FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 20,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)

        # Large one or two line bottom line (punchline)
        self.AddLine(OrderNum = 2,
                     FontName = "TestarossaNF.ttf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# SHORT TOP LINE (ALL CAPS!!!)
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate11(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 11)

        # Short very large top line
        self.AddLine(OrderNum = 11,
                     FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 25,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 2,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

# Large medium-length top line 
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate12(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 12)

        # Large medium-length top line 
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 2,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 16,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

# SHORT TOP LINE
# MEDIUM LINE
# by the
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate13(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 13)

        # Small single word or short top line
        self.AddLine(OrderNum = 1,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small transition line
        self.AddLine(OrderNum = 3,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium long 1 or 2 line bottom line
        self.AddLine(OrderNum = 4,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# ADJ1 & ADJ2
# TWO OR EVEN THREE ROW
# Generators: 30
class TitleTemplate14(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 14)

        # Two large word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 27,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long (2-3 lines) middle line
        self.AddLine(OrderNum = 2,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 3,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 3,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

# Top Line: I'm Having a Baby for
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate15(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 15)

        # Small single word or short top line
        self.AddLine(OrderNum = 1,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 27,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line
# Generators: 14, 24, 40
class TitleTemplate16(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 16)

        # Medium long line or two lines normal type
        self.AddLine(OrderNum = 1,
                     FontName = "MutterKrauseNormal.ttf" ,
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Large medium length line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 3,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

# ONE OR TWO WORD TOP ROW
# MEDIUM SECOND ROW
# and the
# MEDIUM THIRD ROW
# Generators: 30, 41
class TitleTemplate17(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 17)

        # One large word top line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 28,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long (1-2 lines) middle line
        self.AddLine(OrderNum = 2,
                     FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 15,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Small cursive trans
        self.AddLine(OrderNum = 3,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Medium long (1-2 lines) middle line
        self.AddLine(OrderNum = 4,
                     FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 15,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

# SHORT TOP LINE
# of a
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate18(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 18)

        # Short large top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium-length large second line 
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small cursive trans
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# ** Medieval **
# 8 INCHES OF STEEL
# MEDIUM length MEDIUM sized second line
class TitleTemplate19(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 19)

        #8 INCHES OF STEEL (medieval)
        self.AddLine(OrderNum = 1,
                     FontName = "CelticGaramond.ttf",
                     FontMaxSize = 17,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # MEDIUM length MEDIUM sized second line
        self.AddLine(OrderNum = 2,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 15,
                     MaxRows = 3,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# LARGE two-or-three word (1-2 lines) top line
# MEDIUM medium-length second line
# MEDIUM medium-length third line
# MEDIUM medium-length punch-line 
# Generators: 55
class TitleTemplate20(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 20)

        # LARGE two-or-three word (1-2 lines) top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # MEDIUM medium-length third line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 13,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # MEDIUM medium-length third line
        self.AddLine(OrderNum = 3,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 13,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # MEDIUM medium-length punch-line 
        self.AddLine(OrderNum = 4,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 20,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

# LARGE ONE OR TWO WORD top row
# LARGE SHORT 2nd row
# by
# MEDIUM LONG-length 4th row
# Generators: 30, 41
class TitleTemplate21(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 21)

        # One large word top line
        self.AddLine(OrderNum = 2,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 28,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long (1-2 lines) middle line
        self.AddLine(OrderNum = 2,
                     FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 15,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

        # Small cursive trans
        self.AddLine(OrderNum = 3,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 13,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium long (1-2 lines) middle line
        self.AddLine(OrderNum = 4,
                     FontName =  "PerpetuaStd.otf",
                     FontMaxSize = 15,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line
# Templates: 62
class TitleTemplate22(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 22)

        # Large short 1-2 word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 26,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long line or two lines normal type
        self.AddLine(OrderNum = 2,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 18,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Large medium length line
        self.AddLine(OrderNum = 2,
                     FontName =  "Sabado Regular.otf",
                     FontMaxSize = 13,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 4,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 25,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

# ** Conversational **
# Medium Top Line
# Punch-line
# Templates: 63, 119
class TitleTemplate23(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 23)

        # Large short 1-2 word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 26,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText ,AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 4,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

class TitleTemplateSelector():
    def __init__(self):
        self.TitleTemplateList = [] 

        for subclass in TitleTemplate.__subclasses__():
            self.TitleTemplateList.append(subclass())

    #def RandomTitleTemplate(self):
    #    TitleTemplate = []

    #    if len(self.TitleTemplateList) > 0:
    #        TitleTemplate = choice(self.TitleTemplateList)
                    
    #    return TitleTemplate
          
    def GetTitleTemplate(self, iTemplateID):
        SelectedTemplate = None 
          
        if len(self.TitleTemplateList) > 0:
            for template in self.TitleTemplateList :
                if template.ID == iTemplateID:
                    SelectedTemplate = template
                    break
                         
        return SelectedTemplate
  
     