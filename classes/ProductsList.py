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
            borderwidth=0,
            highlightthickness=0,
            height=1,
            width=5,
            font=('Halvetica', 18, 'bold')
        )
        # add_new.pack(side=BOTTOM, fill=BOTH)
        add_new.place(relx=1, rely=1, x=-130, y=-45)

        self.update_root()

    def create_products(self):
        for i in range(0, 30):
            product = Product(self.frame, height=100)
            product.pack_propagate(0)
            product.pack(fill=BOTH, pady=2)

