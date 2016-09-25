from tkinter import *
from classes.CustomButton import *
from classes.BaseClass import *
from classes.Scrollable import *
from classes.Product import *
from classes.Recipe import *
from classes.RecipeDialog import *

class RecipesList(Frame, BaseClass, Scrollable):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent
        
        self.frame.configure(bg='lightgrey')

        self._create_recipes()
        
        self._button_add_new = CustomButton(
            self,
            view='border_orange',
            text='New',
            width=5,
            height=1,
            font=(self.default_font, 14, 'bold')
        )
        self._button_add_new.place(relx=1, rely=1, x=-110, y=-40)

        self._button_add_new.bind('<Button-1>', self._on_button_add_new_click)

    def _on_button_add_new_click(self, event):
        RecipeDialog(self)

    def _create_recipes(self):
        for i in range(0, 30):
            recipe = Recipe(self.frame)
            recipe.pack(fill=BOTH, pady=2)

