from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.CustomPicture import *
from classes.BaseClass import *

class Product(Frame, BaseClass):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)
        if kw['picture']: self.picture = kw['picture']
        if kw['name']: self.name = kw['name']

        self['bg'] = 'white'

        Grid.columnconfigure(self, 1, weight=1)
        
        picture = CustomPicture(
            self,
            picture=self.picture,
            size=70
        )
        picture.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))

        name = CustomLabel(
            self,
            font=(self.default_font, 11, 'bold'),
            text=self.name
        )
        name.grid(column=1, row=1, sticky=W, padx=(10, 0), pady=(0, 10))

        delete = CustomButton(
            self,
            view='normal_red',
            text='Delete',
            command=self.delete_event
        )
        delete.grid(column=0, row=0, sticky=W, pady=(10, 5), padx=(15, 0))

        edit = CustomButton(
            self,
            view='normal_green',
            text='Edit',
            command=self.edit_event
        )
        edit.grid(column=1, row=0, sticky=E, pady=(10, 5), padx=(0, 15))

    def delete_event(self):
        print('Delete event')

    def edit_event(self):
        print('Edit event')
