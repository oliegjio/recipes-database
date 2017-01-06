from tkinter import *
import sqlite3
from classes.ColumnsSection import *
from classes.SearchSection import *
from PIL import Image, ImageTk

class MainWindow(BaseClass, Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        BaseClass.__init__(self)
        self.root = root

        self.columns_section = ColumnsSection(self)
        self.columns_section.grid(row=1, column=0, rowspan=10, sticky=N+S+W+E)
        Grid.rowconfigure(self, 1, weight=9)
        Grid.columnconfigure(self, 0, weight=9)

        self.search_section = SearchSection(self)
        self.search_section.grid(row=0, column=0, sticky=N+S+W+E)
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

def main():
    root = Tk()
    icon = ImageTk.PhotoImage(Image.open('images/icon.png'))
    root.title('Recipes Database')
    root.tk.call('wm', 'iconphoto', root._w, icon)
    root.geometry('1000x600')

    main_window = MainWindow(root)
    main_window.pack(fill=BOTH, expand=True)

    root.mainloop()

if __name__ == '__main__' : main() 

