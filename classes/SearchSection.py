from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.CustomEntry import *
from classes.BaseClass import *
from classes.InputDropdown import *
from classes.SearchEvent import *

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

        self._button_switcher = CustomButton(
            self,
            view='border_green',
            text='Show Available',
            font=(self.default_font, 14, 'normal', 'bold'),
            height=1,
            width=14
        )
        self._button_switcher.grid(column=0, row=0)

        self._label_search = CustomLabel(
            self,
            text='Search: ',
            bg='white smoke',
            font=('Halvetica', 12, 'normal', 'normal')
        )
        self._label_search.grid(column=1, row=0, sticky=E)

        self._entry_search = CustomEntry(
            self,
            text='Text',
            width=50
        )
        self._entry_search.grid(column=2, row=0, padx=(0, 40), sticky=W)
        self._entry_search.bind('<Key>', self._on_entry_search_key)
        self.get_root().bind('<Button-1>', self._remove_focus)

    def _on_entry_search_key(self, event):
        self.event_dispatcher.dispatch_event(SearchEvent(SearchEvent.ASK, self._entry_search.get()))

    def _remove_focus(self, event):
        if event.widget == self._entry_search: return
        self.get_root().focus()
