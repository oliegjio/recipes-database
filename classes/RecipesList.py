from tkinter import *
from classes.BaseClass import *
from classes.Scrollable import *
from classes.Product import *
from classes.Recipe import *

class RecipesList(Frame, BaseClass, Scrollable):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent
        
        self.frame.configure(bg='lightgrey')

        self.create_recipes()
        
        add_new = Button(
            self,
            text='New',
            bg='orange',
            fg='white',
            borderwidth=1,
            highlightthickness=1,
            highlightbackground='white',
            highlightcolor='white',
            width=5,
            height=1,
            font=('Halvetica', 14, 'normal', 'bold')
        )
        add_new.place(relx=1, rely=1, x=-110, y=-40)

    def create_recipes(self):
        for i in range(0, 30):
            recipe = Recipe(self.frame)
            recipe.pack(fill=BOTH, pady=2)

