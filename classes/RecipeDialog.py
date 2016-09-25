from tkinter import *
from classes.BaseClass import *
from classes.CustomButton import *
from classes.CustomLabel import *

class RecipeDialog(Toplevel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        Toplevel.__init__(self, parent)

        self.parent = parent
        self['bg'] = 'white'
        self.geometry('500x500')
        self._list_entry_ingredient = list() # TODO!!!!

        self._button_exit = CustomButton(
            self,
            view='normal_red',
            text='Cancel'
        )
        self._button_exit.grid(row=7, column=0)
        self._button_exit.bind('<Button-1>', self._on_button_exit_click)

        self._button_apply = CustomButton(
            self,
            view='normal_green',
            text='Apply'
        )
        self._button_apply.grid(row=7, column=2)
        self._button_apply.bind('<Button-1>', self._on_button_apply_click)

    def _on_button_apply_click(self, event):
        pass
        
    def _on_button_exit_click(self, event):
        self.destroy()
