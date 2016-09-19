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

        self._switcher = Button(
            self,
            text='Show Available',
            bg='sea green',
            fg='white',
            font=('Halvetica', 14, 'normal', 'bold'),
            height=1,
            width=14
        )
        self._switcher.grid(column=0, row=0)

        self._search_label = Label(
            self,
            text='Search: ',
            bg='white smoke',
            font=('Halvetica', 12, 'normal', 'normal')
        )
        self._search_label.grid(column=1, row=0, sticky=E)

        # input_dropdown = InputDropdown(self, width=50)
        # input_dropdown.grid(column=2, row=0, padx=(0, 40), sticky=W)

        self._search_input = Entry(
            self,
            text='Text',
            width=50,
            font=('Halvetica', 12, 'normal', 'normal')
        )
        self._search_input.grid(column=2, row=0, padx=(0, 40), sticky=W)
        # self._search_input.bind('<FocusIn>', self._search_input_focus_in)
        # self._search_input.bind('<FocusOut>', self._search_input_focus_out)
        self._search_input.bind('<Key>', self._search_input_key)
        self.get_root().bind('<Button-1>', self._search_input_remove_focus)

    def _search_input_key(self, event):
        self.event_dispatcher.dispatch_event(Search(Search.ASK, self._search_input.get()))

    # def _search_input_focus_in(self, event):
    #     print('Focus in')
    #
    # def _search_input_focus_out(self, event):
    #     print('Focus out')

    def _search_input_remove_focus(self, event):
        if event.widget == self._search_input: return
        self.get_root().focus()
