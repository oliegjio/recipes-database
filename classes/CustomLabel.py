from tkinter import *
from classes.BaseClass import *

class CustomLabel(Label, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        if not 'bg' in kw: kw['bg'] = 'white'
        if not 'font' in kw: kw['font'] = (self.default_font, 10, 'normal', 'normal')
        Label.__init__(self, parent, **kw)
