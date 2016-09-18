from tkinter import *
from classes.BaseClass import *
from classes.InputDropdown import *

class SearchSection(Frame, BaseClass):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent

        self['bg'] = 'white smoke'

        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)

        switcher = Button(
            self,
            text='Show Available',
            bg='sea green',
            fg='white',
            font=('Halvetica', 14, 'normal', 'bold'),
            height=1,
            width=14
        )
        switcher.grid(column=0, row=0)

        search_label = Label(
            self,
            text='Search: ',
            bg='white smoke',
            font=('Halvetica', 12, 'normal', 'normal')
        )
        search_label.grid(column=1, row=0, sticky=E)

        input_dropdown = InputDropdown(self, width=50)
        input_dropdown.grid(column=2, row=0, padx=(0, 40), sticky=W)

