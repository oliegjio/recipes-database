from tkinter import *
from classes.Product import *
from classes.BaseClass import *
from classes.Scrollable import *
from classes.SearchEvent import *
from io import StringIO, BytesIO
import re

class ProductsList(Frame, BaseClass, Scrollable):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent

        self.frame['bg'] = 'lightgrey'

        self._visible_products = list()

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

        self._cache_products()
        self._display_all_products()

        self.event_dispatcher.add_event_listener(SearchEvent.ASK, self._on_search_ask)

    def _cache_products(self):
        self._products = dict()
        
        self.database.query('select * from products')
        products = self.database.fetch_all()
        for product in products:
            self._products[product[0]] = self._create_product(product[0], BytesIO(product[1]))

    def _search_product(self, query):
        matches = list()
        
        for product_name in self._products.keys():
            regex = '\W*({})\W*'.format(query)
            result = re.search(regex, product_name, flags=re.IGNORECASE)
            if result: matches.append(product_name)

        return matches

    def _display_all_products(self):
        for product in self._products:
            self._products[product].pack(fill=BOTH, pady=2)

    def _on_search_ask(self, event):
        matches = self._search_product(event.data)
        self._show_products(matches)

    def _show_products(self, products):
        for product in self._products.keys():
            self._products[product].pack_forget()
        for product in products:
            self._products[product].pack(fill=BOTH, pady=2)

    def _create_product(self, name, picture):
        product = Product(self.frame, name=name, picture=picture)    
        self._products[name] = product
        product.pack_propagate(0)

        return product

