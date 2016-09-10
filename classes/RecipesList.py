from tkinter import *
from classes.BaseClass import *
from classes.Scrollable import *
from classes.Product import *

class RecipesList(Frame, BaseClass, Scrollable):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent
        
        self.frame.configure(bg='white')
        test_button = Button(self.frame, text='test text')
        test_button.pack()

