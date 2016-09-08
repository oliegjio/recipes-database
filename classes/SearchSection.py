from tkinter import *

class SearchSection(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent

        self['bg'] = 'green'
        self.grid(row=0, column=0, rowspan=1, sticky=N+S+W+E)
        Grid.rowconfigure(parent, 0, weight=1)
        Grid.columnconfigure(parent, 0, weight=1)

        self.initUi()

    def initUi(self):
        test_button = Button(self, text='Test Button 1')
        test_button.pack()
