from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import * 
from classes.CustomPicture import *
from classes.CustomEntry import *
from classes.BaseClass import *
from classes.NewProductEvent import *
from PIL import Image, ImageTk
from tkinter import filedialog

class ProductDialog(Toplevel, BaseClass):

    def __init__(self, parent, data=None):
        Toplevel.__init__(self, parent)
        BaseClass.__init__(self)
        self.parent = parent

        self['bg'] = 'white'

        self.geometry('400x350')

        for i in range(0, 4):
            Grid.columnconfigure(self, i, weight=1)
            Grid.rowconfigure(self, i, weight=1)

        self._bottom_padding = 20

        self._exit_button = CustomButton(
            self,
            view='normal_red',
            text='Cancel',
            command=self._exit_button_click
        )
        self._exit_button.grid(row=4, column=0, pady=(0, self._bottom_padding))
        
        self._apply_button = CustomButton(
            self,
            view='normal_green',
            text='Apply',
            command=self._apply_button_click
        )
        self._apply_button.grid(row=4, column=2, pady=(0, self._bottom_padding))
        
        self._change_picture_button = CustomButton(
            self,
            view='normal_blue',
            text='Change Picture',
            command=self._change_picture_button_click
        )
        self._change_picture_button.grid(row=1, column=1, sticky=N)

        self._picture_label = CustomPicture(
            self,
            picture=self._get_placeholder(),
            size=150
        )
        self._picture_label.grid(column=1, row=0, pady=(20, 0))

        self._name_field = CustomEntry(self)
        self._name_field.grid(row=2, column=1, columnspan=2)

        self._name_label = CustomLabel(
            self,
            text='Product Name: '
        )
        self._name_label.grid(row=2, column=0, sticky=E)

    def _change_picture_button_click(self):
        picture_path = filedialog.askopenfilename()
        the_file = open(picture_path, 'rb')
        self._new_picture = the_file.read()
        the_file.close()
        self._picture_label.set_image(self._new_picture)

    def _get_placeholder(self):
        self.database.query('select `blob` from meta where text = "placeholder"')
        return self.database.fetch_one()[0]

    def _exit_button_click(self):
        self.destroy()

    def _apply_button_click(self):
        if self._name_field.get() == "" or not hasattr(self, '_new_picture'): return

        self.database.query(
            'insert into products (name, picture) values (?, ?)',
            [self._name_field.get(), self._new_picture]
        )

        data = dict()
        data['name'] = self._name_field.get()
        data['picture'] = self._new_picture

        self.event_dispatcher.dispatch_event(NewProductEvent(NewProductEvent.ASK, data))

        self.destroy()
