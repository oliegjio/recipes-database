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
        
        self.create_products()

    def create_products(self):
        for i in range(0, 30):
            product = Product(self.frame, height=100)
            product.pack_propagate(0)
            product.pack(fill=BOTH)

