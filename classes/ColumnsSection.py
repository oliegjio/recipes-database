from tkinter import *
from classes.ProductsList import *
from classes.RecipesList import *

class ColumnsSection(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self['bg'] = 'yellow'
        self.grid(row=1, column=0, rowspan=10, sticky=N+S+W+E)
        Grid.rowconfigure(parent, 1, weight=10)
        Grid.columnconfigure(parent, 0, weight=10)

        self.initChildren()

    def initChildren(self):
        products_list = ProductsList(self)
        recipes_list = RecipesList(self)
        

