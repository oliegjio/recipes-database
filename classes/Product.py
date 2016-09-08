from tkinter import *

class Product(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)

        self['bg'] = 'red'

        self.initChildren()

    def initChildren(self):
        button = Button(self, text="Hello")
        button.pack()
