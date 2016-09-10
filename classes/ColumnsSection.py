from tkinter import *
from classes.ProductsList import *
from classes.RecipesList import *
from classes.BaseClass import *

class ColumnsSection(Frame, BaseClass):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent

        self.init_children()

    def init_children(self):
        self.products_list = ProductsList(self)
        self.products_list.grid(row=0, column=0, sticky=N+E+W+S)
        Grid.columnconfigure(self, 0, weight=1) 
        Grid.rowconfigure(self, 0, weight=1) 

        self.recipes_list = RecipesList(self)
        self.recipes_list.grid(row=0, column=1, sticky=N+E+W+S)
        Grid.columnconfigure(self, 1, weight=3) 
        Grid.rowconfigure(self, 0, weight=1) 

