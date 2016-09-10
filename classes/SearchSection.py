from tkinter import *
from classes.BaseClass import *

class SearchSection(Frame, BaseClass):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent

        self['bg'] = 'green'

        test_button = Button(self, text='Test Button 1')
        test_button.pack()
