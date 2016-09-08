from tkinter import *

class ProductsList(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        
        self.grid(row=0, column=0, sticky=N+E+W+S)
        Grid.columnconfigure(parent, 0, weight=1) 
        Grid.rowconfigure(parent, 0, weight=1) 

        self.initChildren()

    def initChildren(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, expand=False)
        canvas = Canvas(self, bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.config(command=canvas.yview)

        self.frame = frame = Frame(canvas)
        frame['bg'] = 'cyan'
        frame.pack(fill=BOTH, expand=True)

        test_button = Button(frame, text='test text')
        test_button.pack()


