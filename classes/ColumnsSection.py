from tkinter import *
from classes.ProductsList import *
from classes.RecipesList import *
from classes.BaseClass import *

class ColumnsSection(Frame, BaseClass):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent

        self._products_list = ProductsList(self)
        self._products_list.grid(row=0, column=0, sticky=N+E+W+S)
        self._products_list.grid_propagate(0)
        Grid.columnconfigure(self, 0, weight=2, minsize=300) 
        Grid.rowconfigure(self, 0, weight=1) 

        self._recipes_list = RecipesList(self)
        self._recipes_list.grid(row=0, column=1, sticky=N+E+W+S)
        Grid.columnconfigure(self, 1, weight=2) 

