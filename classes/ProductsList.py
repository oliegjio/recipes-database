from tkinter import *
from classes.Product import *
from classes.BaseClass import *
from classes.Scrollable import *
from classes.events.SearchEvent import *
from classes.events.NewProductEvent import *
from classes.ProductDialogNew import *
from classes.events.DeleteProductEvent import *
import re

class ProductsList(Frame, BaseClass, Scrollable):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent
        self.frame['bg'] = 'lightgrey'

        self._button_add_new = CustomButton(
            self,
            view='border_orange',
            text='New',
            height=1,
            width=5,
            font=(self.default_font, 14, 'bold')
        )
        self._button_add_new.place(relx=1, rely=1, x=-110, y=-40)
        self._button_add_new.bind('<Button-1>', self._on_button_add_new_click)

        self._cache_products()
        self._show_all_products()

        self.event_dispatcher.add_event_listener(SearchEvent.ASK, self._on_search_event_ask)
        self.event_dispatcher.add_event_listener(NewProductEvent.ASK, self._on_new_product_event_ask)
        self.event_dispatcher.add_event_listener(DeleteProductEvent.ASK, self._on_delete_product_event_ask)

    def _on_delete_product_event_ask(self, event):
        data = event.data

        self.database.query('delete from products where name = "{}"'.format(data))

        self._products[data].pack_forget()
        self._products[data].destroy()
        del self._products[data]

        self._show_all_products()

    def _on_new_product_event_ask(self, event):
        data = event.data
        self._products[data['name']] = self._create_product(data['name'], data['picture'])
        self._show_all_products()

    def _on_button_add_new_click(self, event):
        ProductDialogNew(self)
    
    def _forget_products(self):
        for product in self._products.keys():
            self._products[product].pack_forget()

    def _cache_products(self):
        self._products = dict()
        
        self.database.query('select * from products')
        products = self.database.fetch_all()
        for product in products:
            self._products[product[0]] = self._create_product(product[0], product[1])

    def _search_product(self, query):
        matches = list()
        
        for product_name in self._products.keys():
            regex = '\W*({})\W*'.format(query)
            result = re.search(regex, product_name, flags=re.IGNORECASE)
            if result: matches.append(product_name)

        return matches

    def _show_all_products(self):
        self._forget_products()
        for product in self._products:
            self._products[product].pack(fill=BOTH, pady=2)

    def _on_search_event_ask(self, event):
        matches = self._search_product(event.data)
        self._show_products(matches)
        self.reset_scroll()

    def _show_products(self, products):
        self._forget_products()
        for product in products:
            self._products[product].pack(fill=BOTH, pady=2)

    def _create_product(self, name, picture):
        product = Product(self.frame, name=name, picture=picture)    
        self._products[name] = product
        product.pack_propagate(0)

        return product

