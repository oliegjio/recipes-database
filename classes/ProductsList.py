from tkinter import *
from classes.Product import *

class ProductsList(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        self.parent = parent
        
        self.initChildren()
        self.createProducts()

    def initChildren(self):
        self.canvas = Canvas(self, background='black')
        self.frame = Frame(self.canvas, background='white')
        self.frame.grid_propagate(False)
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.frame_id = self.canvas.create_window(0, 0, window=self.frame, anchor=NW)
        self.canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        self.canvas.bind_all('<Button-4>', self._on_mousewheel)
        self.canvas.bind_all('<Button-5>', self._on_mousewheel)
        def _configure_frame(event):
            size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
            self.canvas.config(scrollregion='0 0 %s %s' % size)
            if self.frame.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.config(width=self.frame.winfo_reqwidth())
        self.frame.bind('<Configure>', _configure_frame)
        def _configure_canvas(event):
            if self.frame.winfo_reqwidth() != self.canvas.winfo_width():
                self.canvas.itemconfigure(self.frame_id, width=self.canvas.winfo_width())
                print(self.canvas.winfo_width())
        self.canvas.bind('<Configure>', _configure_canvas)

    def _on_mousewheel(self, event):
        direction = 0
        if event.num == 5 or event.delta == -120:
            direction = 1
        if event.num == 4 or event.delta == 120:
            direction = -1
        self.canvas.yview_scroll(direction, UNITS)

    def createProducts(self):
        for i in range(0, 50):
            product = Product(self.frame, width=500, height=100)
            product.pack_propagate(0)
            product.pack()



