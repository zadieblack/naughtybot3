#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# titletemplates module

class TitleTemplate():
    def __init__(self, ID):
        self.ID = ID

class TitleTemplateDefault(TitleTemplate):
    def __init__(self):
        super().__init__(0)

class TitleTemplate1(TitleTemplate):
    def __init__(self, ID):
        super().__init__()

