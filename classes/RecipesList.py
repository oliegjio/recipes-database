from tkinter import *

class RecipesList(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.initChildren()

    def initChildren(self):
        test_button = Button(self, text='test text')
        test_button.pack()
