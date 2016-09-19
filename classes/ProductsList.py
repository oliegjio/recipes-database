from tkinter import *
from classes.Product import *
from classes.BaseClass import *
from classes.Scrollable import *
# from StringIO import StringIO
from io import StringIO, BytesIO
from base64 import *
import struct

class ProductsList(Frame, BaseClass, Scrollable):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent

        self.frame['bg'] = 'lightgrey'

        self._products = dict()

        # self.create_products()

        add_new = Button(
            self,
            text='New',
            bg='orange',
            fg='white',
            borderwidth=1,
            highlightthickness=1,
            highlightbackground='white',
            highlightcolor='white',
            height=1,
            width=5,
            font=('Halvetica', 14, 'bold')
        )
        add_new.place(relx=1, rely=1, x=-110, y=-40)

        self.update_root()

        self.event_dispatcher.add_event_listener(Search.ASK, self._on_search_ask)

    def _on_search_ask(self, event):
        data = event.data

        self.database.query("select * from products where name like '%{}%'".format(data))
        fetched_products = self.database.fetch_all()
        if fetched_products:
            for key in self._products.keys():
                self._products[key].pack_forget()
                self._products[key].destroy()
            for product in fetched_products:
                self._create_product(product[0], BytesIO(product[1]))

    def _create_product(self, name, picture):
        product = Product(self.frame, name=name, picture=picture)    
        self._products[name] = product
        product.pack_propagate(0)
        product.pack(fill=BOTH, pady=2)

