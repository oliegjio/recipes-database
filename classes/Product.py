from tkinter import *
from classes.BaseClass import *

class Product(Frame, BaseClass):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)

        self['bg'] = 'white'

        button = Button(self, text="Hello")
        button.pack()
