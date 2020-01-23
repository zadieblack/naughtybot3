#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# titletemplates module

class TitleLine():
    def __init__(self, OrderNum = 1, 
                 sFontName = "", 
                 MaxHeight = 78, 
                 MaxRows = 1):
        #self.ID = 0
        self._OrderNum = OrderNum
        self._FontName = sFontName
        self._MaxHeight = MaxHeight
        self._MaxRows = MaxRows 

class TitleTemplate():
    def __init__(self, ID):
        self.ID = ID

        self.Lines = []

    def AddLine(self, OrderNum, sFontName, MaxHeight, MaxRows):
        self.Lines.append(TitleLine(OrderNum,sFontName,MaxHeight,MaxRows))

class TitleTemplateHHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 0)
        self.AddLine(OrderNum = 1,
                     sFontName = "Walpurgis Night.otf",
                     MaxHeight = 308,
                     MaxRows = 4)
        #Max Rows = 5
        #Max Height = 392

class TitleTemplatePHDefault(TitleTemplate):
    def __init__(self):
        super().__init__(ID = 1)
        self.AddLine(TitleLine(OrderNum = 1,
                               sFontName = "Walpurgis Night.otf",
                               MaxRows = 5,
                               MaxHeight = 392))
        #Max Rows = 5
        #Max Height = 392

class TitleTemplate1(TitleTemplate):
    def __init__(self, ID):
        super().__init__()

