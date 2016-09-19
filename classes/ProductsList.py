from tkinter import *
from classes.Product import *
from classes.BaseClass import *
from classes.Scrollable import *

class ProductsList(Frame, BaseClass, Scrollable):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)
        Scrollable.__init__(self)

        self.parent = parent

        self.frame['bg'] = 'lightgrey'

        self.create_products()

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

        

    def create_products(self):
        for i in range(0, 30):
            product = Product(self.frame)
            product.pack_propagate(0)
            product.pack(fill=BOTH, pady=2)

