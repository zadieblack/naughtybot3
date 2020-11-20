#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# titletemplates module

from util import *
from gen import *

#                       *** RECOMMENDED FONT LIST ***
#
#       ~~ File Name ~~             ~~ Type ~~  ~~ Serif? ~~  ~~ Best Size ~~
# "Absinette W01 Regular.ttf"                        xx             25
# "Adorable MLSJN.ttf"              Script           xx             16
# "Amaze.ttf"                       Script           xx             12
# "Babes In Toyland NF.ttf"         All Caps         xx             23
# "Blacksword.otf"                  Script           xx             13
# "CelticGaramond.ttf"              Old English      xx             24
# "chintzy.ttf.ttf"                 Tech             xx             24
# "Coventry Garden NF.ttf"          All Caps         xx             18
# "FreestyleScriptStd.otf"          Hand-written     xx             22
# "Helenium W01 Regular.ttf"        All Caps         xx             18           
# "Lapidary 333 Bold Italic.otf"                     xx             16              AUTHOR FONT
# "LaserLondon.ttf"                                  xx             26
# "Lightfoot.ttf"                   All Caps         xx             26
# "Moyers.otf"                                       xx             40
# "MutterKrauseNormal.ttf"                           xx             16
# "NimbusRomNo9L-Med.otf"                            xx             14
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

class TitleTemplate(Generator):
    def __init__(self, ID = -1, 
                 Priority = GenPriority.Normal, 
                 Type = GeneratorType.Normal, 
                 Disabled = False, 
                 sTxt = ""):
        super().__init__(ID = ID, Priority = Priority,Type = Type, Disabled = Disabled, sTxt = sTxt)
        self.Lines = []
        self.NextLineID = 1

        self.AuthorLine = TitleLine(OrderNum = 0, 
                                    FontName = "Lapidary 333 Bold Italic.otf",
                                    FontMaxSize = 16,
                                    MaxRows = 1)

    def AddLine(self, OrderNum = -1, FontName = "", FontMaxSize = 16, MaxRows = 2, ColorType = None, AllCaps = False):
        if OrderNum == -1:
            OrderNum = self.NextLineID
            self.NextLineID = self.NextLineID + 1
        else:
            self.NextLineID = OrderNum + 1

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
        super().__init__()

        self.AddLine(FontName = "Walpurgis Night.otf",
                     FontMaxSize = 21,
                     MaxRows = 4,
                     ColorType = LineColorType.MainTitle)


class TitleTemplatePHDefault(TitleTemplate):
    def __init__(self):
        super().__init__()
        self.AddLine(FontName = "Walpurgis Night.otf",
                     FontMaxSize = 21,
                     MaxRows = 5,
                     ColorType = LineColorType.MainTitle)

# [THREE LINES]
# SHORT TOP LINE
# of a
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate1(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Short very large top line
        self.AddLine(FontName = "Walpurgis Night.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small cursive trans
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

# [FOUR LINES]
# MEDIUM TOP LINE
# of a
# MEDIUM BOTTOM LINE
# possible subtitle
class TitleTemplate2(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large medium-length top line 
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small short second line
        self.AddLine(FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Large medium third line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

        # Small possible tag-line
        self.AddLine(FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)
        

# [FIVE LINES]
# FEMALE NAME
# Shows A
# MEDIUM CENTER LINE
# Her
# CUNNING STUNT
class TitleTemplate3(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large short single-word top line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 23,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)
        
        # Small trans middle line
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length center line
        self.AddLine(FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 17,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

        # Small transition line
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length bottom line
        self.AddLine(FontName = "Sabado Regular.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)


# [THREE LINES]
# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line

# Templates: 7, 83
class TitleTemplate4(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Medium long line or two lines normal type
        self.AddLine(FontName = "MutterKrauseNormal.ttf" ,
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Large medium length line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)


# [THREE LINES]
# ** Medieval **
# SHORT TOP LINE
# transition
# SHORT BOTTOM LINE

class TitleTemplate5(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large single word or short top line (medieval)
        self.AddLine(FontName = "CelticGaramond.ttf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Smaller single word trans (medieval)
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 14,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Large medium-length bottom line (medieval)
        self.AddLine(FontName = "oldengl.ttf",
                     FontMaxSize = 22,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)


# [THREE LINES]
# SHORT TOP LINE
# MEDIUM LINE
# LONG TWO-ROW BOTTOM LINE

class TitleTemplate6(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large single word or short top line
        self.AddLine(FontName = "Walpurgis Night.otf",
                     FontMaxSize = 30,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Smaller medium-length second line
        self.AddLine(FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Medium long 1 or 2 line bottom line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 16,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [TWO LINES]
# ** Punchline **
# MEDIUM TOP LINE
# MEDIUM BOTTOM LINE

class TitleTemplate7(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Small medium length top-line
        self.AddLine(FontName = "Lightfoot.ttf",
                     FontMaxSize = 23,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Large one or two line bottom line (punchline)
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)
                     #This needs extra space to work


# [ONE LINE]
# ** Conversational **
# One large long or multi-line line

# Generators: 143
class TitleTemplate8(TitleTemplate):
    def __init__(self):
        super().__init__()

        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 4,
                     ColorType = LineColorType.MainTitle)


# [THREE LINES]
# SHORT TOP LINE
# MEDIUM LINE
# LONG TWO-ROW BOTTOM LINE

# Generators: 124
class TitleTemplate9(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Small single word or short top line
        self.AddLine(FontName = "Blacksword.otf",
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length second line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long 1 or 2 line bottom line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [TWO LINES]
# ** Punchline **
# LONG TOP LINE
# MEDIUM BOTTOM LINE

class TitleTemplate10(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Small medium length top-line
        self.AddLine(FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 20,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)

        # Large one or two line bottom line (punchline)
        self.AddLine(FontName = "TestarossaNF.ttf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [TWO LINES]
# SHORT TOP LINE (ALL CAPS!!!)
# LONG TWO-ROW BOTTOM LINE

class TitleTemplate11(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Short very large top line
        self.AddLine(FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 25,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # One or two-line medium-sized bottom line
        self.AddLine(FontName = "Sabado Regular.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)


# [TWO LINES]
# Large medium-length top line 
# LONG TWO-ROW BOTTOM LINE

# Generators: 11, 12, 26, 45, 78, 108, 117
class TitleTemplate12(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large medium-length top line 
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)

        # One or two-line medium-sized bottom line
        self.AddLine(FontName = "Sabado Regular.otf",
                     FontMaxSize = 16,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)


# [FOUR LINES]
# SHORT TOP LINE
# MEDIUM LINE
# by the
# LONG TWO-ROW BOTTOM LINE

# Generators: 42, 127
class TitleTemplate13(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Small single word or short top line
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length second line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small transition line
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium long 1 or 2 line bottom line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [THREE LINES]
# ADJ1 & ADJ2
# Medium long (2-3 lines) middle line
# Small medium-length tag (excited!)

class TitleTemplate14(TitleTemplate):
    # Generators: 30, 72, 118
    def __init__(self):
        super().__init__()

        # Two large word top line
        self.AddLine(FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 27,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long (2-3 lines) middle line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 3,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)


# [TWO LINES]
# Top Line: I'm Having a Baby for
# LONG TWO-ROW BOTTOM LINE
class TitleTemplate15(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Small single word or short top line
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 27,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # One or two-line medium-sized bottom line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)


# [THREE LINES]
# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line

class TitleTemplate16(TitleTemplate):
    # Generators: 14, 24, 40, 74 76
    def __init__(self):
        super().__init__()

        # Medium long line or two lines normal type
        self.AddLine(FontName = "MutterKrauseNormal.ttf" ,
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Large medium length line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 17,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)


# [FOUR LINES]
# ONE OR TWO WORD TOP ROW
# MEDIUM SECOND ROW
# and the
# MEDIUM THIRD ROW

class TitleTemplate17(TitleTemplate):
    # Generators: 30, 41
    def __init__(self):
        super().__init__()

        # One large word top line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 28,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium long (1-2 lines) middle line
        self.AddLine(FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 15,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Small cursive trans
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Medium long (1-2 lines) middle line
        self.AddLine(FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 15,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)


# [FOUR LINES]
# Short large top line
# Medium-length large second line 
# Small cursive trans
# One or two-line medium-sized bottom line
class TitleTemplate18(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Short large top line
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium-length large second line 
        self.AddLine(FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

        # Small cursive trans
        self.AddLine(FontName = "Amaze.ttf",
                     FontMaxSize = 12,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)


# [TWO LINES]
# ** Medieval **
# 8 INCHES OF STEEL
# MEDIUM length MEDIUM sized second line
class TitleTemplate19(TitleTemplate):
    def __init__(self):
        super().__init__()

        #8 INCHES OF STEEL (medieval)
        self.AddLine(FontName = "CelticGaramond.ttf",
                     FontMaxSize = 17,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # MEDIUM length MEDIUM sized second line
        self.AddLine(FontName = "PerpetuaStd.otf",
                     FontMaxSize = 15,
                     MaxRows = 3,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [FOUR LINES]
# LARGE two-or-three word (1-2 lines) top line
# MEDIUM medium-length second line
# MEDIUM medium-length third line
# MEDIUM medium-length punch-line 

class TitleTemplate20(TitleTemplate):
    # Generators: 55
    def __init__(self):
        super().__init__()

        # LARGE two-or-three word (1-2 lines) top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 22,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # MEDIUM medium-length second line
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


# [FOUR LINES]
# LARGE ONE OR TWO WORD top row
# LARGE SHORT 2nd row
# by
# MEDIUM LONG-length 4th row

class TitleTemplate21(TitleTemplate):
    # Generators: 30, 41
    def __init__(self):
        super().__init__()

        # One large word top line
        self.AddLine(OrderNum = 1,
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


# [FOUR LINES]
# ** Conversational **
# Medium Top Line
# Large Middle Line
# Small Bottom Line
class TitleTemplate22(TitleTemplate):
    # Templates: 62
    def __init__(self):
        super().__init__()

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
        self.AddLine(OrderNum = 3,
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


# [TWO LINES]
# ** Conversational **
# Medium Top Line
# Punch-line
class TitleTemplate23(TitleTemplate):
    # Templates: 63, 112, 119
    def __init__(self):
        super().__init__()

        # Large short 1-2 word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Sabado Regular.otf",
                     FontMaxSize = 26,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText ,AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 2,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 21,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)


# [THREE LINES]
# Large medium-length top line 
# Small single word or short top line
# One or two-line medium-sized bottom line

class TitleTemplate24(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large medium-length top line 
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 23,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)

        # Small single word or short top line
        self.AddLine(OrderNum = 2,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)


# [THREE LINES]
# ** Punchline **
# LONG TOP LINE
# MEDIUM medium-length second line
# # MEDIUM medium-length bottom line 

class TitleTemplate25(TitleTemplate):
    # Generators: 125
    def __init__(self):
        super().__init__()

        # Small medium length top-line
        self.AddLine(OrderNum = 1,
                     FontName = "Quaint Gothic SG OT Regular.ttf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # MEDIUM medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "MutterKrauseNormal.ttf",
                     FontMaxSize = 10,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # MEDIUM medium-length bottom line 
        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 15,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [FOUR LINES]
# **SCI FI**
# Large short single-word top line
# of a
# Medium 1-2 line center line
# Medium short-length punchline!

class TitleTemplate26(TitleTemplate):
    def __init__(self):
        super().__init__()

        # Large short single-word top line
        self.AddLine(OrderNum = 1,
                     FontName = "chintzy.ttf",
                     FontMaxSize = 26,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)
        
        # Small trans middle line
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 10,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium medium-length center line
        self.AddLine(OrderNum = 3,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 16,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)

        # Medium medium-length bottom line
        self.AddLine(OrderNum = 4,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 19,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)


# [THREE LINES]
# Large medium-length top line 
# Small single word or short top line
# One or two-line medium-sized bottom line

class TitleTemplate27(TitleTemplate):
    def __init__(self):
        super().__init__()

        # One or two-line medium-sized bottom line
        self.AddLine(OrderNum = 1,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 18,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small single word or short top line
        self.AddLine(OrderNum = 2,
                     FontName = "FreestyleScriptStd.otf",
                     FontMaxSize = 16,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)
        
        # Large medium-length top line 
        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 17,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)
        

# [THREE LINES]
# ONE OR TWO WORD TOP ROW
# and the
# LONG MEDIUM-SIZED THIRD ROW

class TitleTemplate28(TitleTemplate):
    # Generators: 61
    def __init__(self):
        super().__init__()

        # One large word top line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 28,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Small cursive trans line
        self.AddLine(OrderNum = 3,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText)

        # Medium long (1-2 lines) last line
        self.AddLine(OrderNum = 4,
                     FontName = "Absinette W01 Regular.ttf",
                     FontMaxSize = 12,
                     MaxRows = 2,
                     ColorType = LineColorType.SecondTitle)


# [THREE LINES]
# ONE OR TWO WORD TOP ROW
# MEDIUM LENGTH MEDIUM-SIZED SECOND ROW
# Small medium-length tag (excited!)

class TitleTemplate29(TitleTemplate):
    # Generators: 145
    def __init__(self):
        super().__init__()

        # Short very large top line
        self.AddLine(OrderNum = 1,
                     FontName = "Moyers.otf",
                     FontMaxSize = 47,
                     MaxRows = 1,
                     ColorType = LineColorType.MainTitle)

        # Small medium-length line 
        self.AddLine(OrderNum = 1,
                     FontName = "NimbusRomNo9L-Med.otf" ,
                     FontMaxSize = 14,
                     MaxRows = 1,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)

        # Small medium-length tag (excited!)
        self.AddLine(OrderNum = 3,
                     FontName = "Blacksword.otf",
                     FontMaxSize = 13,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)


# [TWO LINES]
# LONG ONE OR TWO LINE TOP ROW
# Part III

class TitleTemplate30(TitleTemplate):
    # Generators: 145
    def __init__(self):
        super().__init__()

        # Large very long line
        self.AddLine(OrderNum = 1,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 24,
                     MaxRows = 3,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

        # Medium short length line
        self.AddLine(OrderNum = 2,
                     FontName =  "Sabado Regular.otf",
                     FontMaxSize = 12,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText,
                     AllCaps = True)


# [TWO LINES]
# Short very large top line
# Small long-length line

class TitleTemplate31(TitleTemplate):
    # Generators: 4
    def __init__(self):
        super().__init__()

        # Short very large top line
        self.AddLine(OrderNum = 1,
                     FontName = "Moyers.otf",
                     FontMaxSize = 34,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle)

        # Small long-length line 
        self.AddLine(OrderNum = 2,
                     FontName = "PerpetuaStd.otf",
                     FontMaxSize = 13,
                     MaxRows = 3,
                     ColorType = LineColorType.SecondTitle,
                     AllCaps = True)


# [THREE LINES]
# ** Punchline **
# LONG TOP LINE
# MEDIUM medium-length second line
# # MEDIUM medium-length bottom line 

class TitleTemplate32(TitleTemplate):
    # Generators: 125
    def __init__(self):
        super().__init__()

        # Small medium length top-line
        self.AddLine(OrderNum = 1,
                     FontName = "Moyers.otf",
                     FontMaxSize = 20,
                     MaxRows = 2,
                     ColorType = LineColorType.SmallText)

        # MEDIUM medium-length second line
        self.AddLine(OrderNum = 2,
                     FontName = "Amaze.ttf",
                     FontMaxSize = 11,
                     MaxRows = 1,
                     ColorType = LineColorType.SecondTitle)

        # MEDIUM medium-length bottom line 
        self.AddLine(OrderNum = 3,
                     FontName = "Verona-ExtraBold.otf",
                     FontMaxSize = 15,
                     MaxRows = 2,
                     ColorType = LineColorType.MainTitle,
                     AllCaps = True)

# Title templates are generators and can be randomly selected but we aren't using this right now

TTS = GeneratorContainer(TitleTemplate)
