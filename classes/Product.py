from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.CustomPicture import *
from classes.BaseClass import *
from classes.ProductDeleteDialog import *

class Product(Frame, BaseClass):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)

        if kw['picture']: self._picture = kw['picture']
        if kw['name']: self._name = kw['name']
        self['bg'] = 'white'

        Grid.columnconfigure(self, 1, weight=1)
        
        self._picture_product = CustomPicture(
            self,
            picture=self._picture,
            size=70
        )
        self._picture_product.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))

        self._label_product_name = CustomLabel(
            self,
            font=(self.default_font, 11, 'bold'),
            text=self._name
        )
        self._label_product_name.grid(column=1, row=1, sticky=W, padx=(10, 0), pady=(0, 10))

        self._button_delete_product = CustomButton(
            self,
            view='normal_red',
            text='Delete',
            command=self._on_button_delete_product_click
        )
        self._button_delete_product.grid(column=0, row=0, sticky=W, pady=(10, 5), padx=(15, 0))

        self._button_edit_product = CustomButton(
            self,
            view='normal_green',
            text='Edit',
            command=self._on_button_edit_product_click
        )
        self._button_edit_product.grid(column=1, row=0, sticky=E, pady=(10, 5), padx=(0, 15))

    def _on_button_delete_product_click(self):
        ProductDeleteDialog(self, data=self._name)

    def _on_button_edit_product_click(self):
        pass
