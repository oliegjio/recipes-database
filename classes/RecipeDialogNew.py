from tkinter import *
from classes.BaseClass import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.CustomEntry import *
from classes.CustomPicture import *

class RecipeDialogNew(Toplevel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        Toplevel.__init__(self, parent)

        self.parent = parent
        self['bg'] = 'white'
        self.geometry('480x500')
        self._list_entry_ingredient = list() # TODO!!!!

        self._vertical_padding = 20
        self._horizontal_padding = 20

        for i in range(0, 8):
            Grid.columnconfigure(self, i, weight=1)
            Grid.rowconfigure(self, i, weight=1)

        self._button_exit = CustomButton(
            self,
            view='normal_red',
            text='Cancel'
        )
        self._button_exit.grid(row=8, column=0, sticky=N+E+W+S, pady=(0, self._vertical_padding), padx=(self._horizontal_padding, 0))
        self._button_exit.bind('<Button-1>', self._on_button_exit_click)

        self._button_apply = CustomButton(
            self,
            view='normal_green',
            text='Apply'
        )
        self._button_apply.grid(row=8, column=2, sticky=N+E+W+S, pady=(0, self._vertical_padding), padx=(0, self._horizontal_padding))
        self._button_apply.bind('<Button-1>', self._on_button_apply_click)

        self._label_name = CustomLabel(
            self,
            text="Name: "
        )
        self._label_name.grid(row=0, column=1, sticky=S+W)

        self._entry_name = CustomEntry(
            self,
            width=35
        )
        self._entry_name.grid(row=1, column=1, sticky=N)

        self._label_description = CustomLabel(
            self, 
            text='Description:'
        )
        self._label_description.grid(row=4, column=1, sticky=S+W)

        self._entry_description = Text(
            self,
            height=10,
            width=50
        )
        self._entry_description.grid(row=5, column=1, sticky=N)

        self._picture = CustomPicture(
            self,
            picture=self._get_placeholder(),
            size=100
        )
        self._picture.grid(row=6, column=1)

        self._button_picture = CustomButton(
            self,
            view='normal_blue',
            text='Change Picture'
        )
        self._button_picture.grid(row=7, column=1, sticky=N)

    def _on_button_apply_click(self, event):
        pass
        
    def _on_button_exit_click(self, event):
        self.destroy()

    def _get_placeholder(self):
        self.database.query('select `blob` from meta where text = "placeholder"')
        return self.database.fetch_one()[0]
