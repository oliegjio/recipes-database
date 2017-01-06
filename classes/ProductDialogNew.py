from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import * 
from classes.CustomPicture import *
from classes.CustomEntry import *
from classes.BaseClass import *
from classes.events.NewProductEvent import *
from PIL import Image, ImageTk
from tkinter import filedialog

class ProductDialogNew(Toplevel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        Toplevel.__init__(self, parent)

        self.parent = parent
        self['bg'] = 'white'

        self.geometry('500x350')

        for i in range(0, 4):
            Grid.columnconfigure(self, i, weight=1)
            Grid.rowconfigure(self, i, weight=1)

        self._bottom_padding = 20

        self._button_exit = CustomButton(
            self,
            view='normal_red',
            text='Cancel',
            command=self._on_button_exit_click
        )
        self._button_exit.grid(row=4, column=0, pady=(0, self._bottom_padding))
        
        self._button_apply = CustomButton(
            self,
            view='normal_green',
            text='Apply',
            command=self._on_button_apply_click
        )
        self._button_apply.grid(row=4, column=2, pady=(0, self._bottom_padding))
        
        self._button_change_picture = CustomButton(
            self,
            view='normal_blue',
            text='Change Picture',
            command=self._on_button_change_picture_click
        )
        self._button_change_picture.grid(row=1, column=1, sticky=N)

        self._picture = CustomPicture(
            self,
            picture=self._get_placeholder(),
            size=150
        )
        self._picture.grid(column=1, row=0, pady=(20, 0))

        self._entry_name = CustomEntry(
            self,
            width=25
        )
        self._entry_name.grid(row=2, column=1, columnspan=2, sticky=W+E)

        self._label_name = CustomLabel(
            self,
            text='Product Name: '
        )
        self._label_name.grid(row=2, column=0, sticky=W+E)

    def _on_button_change_picture_click(self):
        picture_path = filedialog.askopenfilename()

        the_file = open(picture_path, 'rb')
        self._new_picture = the_file.read()

        the_file.close()

        self._picture.set_picture(self._new_picture)

    def _get_placeholder(self):
        self.database.query('select `blob` from meta where text = "placeholder"')
        return self.database.fetch_one()[0]

    def _on_button_exit_click(self):
        self.destroy()

    def _on_button_apply_click(self):
        if self._entry_name.get() == "" or not hasattr(self, '_new_picture'): return

        self.database.query(
            'insert into products (name, picture) values (?, ?)',
            [self._entry_name.get(), self._new_picture]
        )

        data = dict()
        data['name'] = self._entry_name.get()
        data['picture'] = self._new_picture

        self.event_dispatcher.dispatch_event(NewProductEvent(NewProductEvent.ASK, data))

        self.destroy()
