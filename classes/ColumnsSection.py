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
        products_list.grid(row=0, column=0, sticky=N+E+W+S)
        Grid.columnconfigure(self, 0, weight=1) 
        Grid.rowconfigure(self, 0, weight=1) 

        recipes_list = RecipesList(self)
        recipes_list.grid(row=0, column=1, sticky=N+E+W+S)
        Grid.columnconfigure(self, 1, weight=3) 
        Grid.rowconfigure(self, 0, weight=1) 

