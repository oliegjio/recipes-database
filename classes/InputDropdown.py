from tkinter import *
from classes.BaseClass import *

class InputDropdown(Frame, BaseClass):

    def __init__(self, parent, **kw):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent
        if kw['width']: self.width = kw['width']

        self.search_var = StringVar()
        self.search_var.trace('w', lambda name, index, mode: self._update_list())
        self.entry = Entry(
            self,
            textvariable=self.search_var,
            width=self.width,
            font=('Halvetica', 12, 'normal', 'normal')
        )
        self.entry.pack()
        self.entry.bind('<FocusIn>', self._focus_in)
        self.entry.bind('<FocusOut>', self._focus_out)
        self.entry.bind('<Button-1>', self._focus_in)
        self.get_root().bind('<Button-1>', self._focus_out)
        # self.entry.grid(column=2, row=0, padx=(0, 40), sticky=W)

    def _update_list(self):
        search_term = self.search_var.get()
        
        listbox_list = ['Apple', 'Cake', 'Egg']

        self.listbox.delete(0, END)

        for item in listbox_list:
            if search_term.lower() in item.lower():
                self.listbox.insert(END, item)

    def _focus_in(self, event):
        if getattr(self, 'listbox', False):
            return
        self.listbox = Listbox(
            self.get_root(),
            width=self.width,
            font=('Halvetica', 12, 'normal', 'normal')
        )
        self.listbox.bind('<<ListboxSelect>>', self._listbox_select)
        self.listbox.place(x=self.winfo_x() + 1, y=self.winfo_y() + 25)
        self._update_list()

    def _focus_out(self, event):
        if getattr(self, 'listbox', False) and (event.widget == self.entry or event.widget == self.listbox):
            return
        if getattr(self, 'listbox', False):
            self._destroy_list()

    def _destroy_list(self):
        self.listbox.destroy()
        self.listbox = None
        self._remove_focus_from_entry()

    def _remove_focus_from_entry(self):
        self.get_root().focus()

    def _listbox_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])

        print(value)

        self._destroy_list()
