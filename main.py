from tkinter import *
import sqlite3
from classes.ColumnsSection import *
from classes.SearchSection import *

# connection = sqlite3.connect('data.db')
# connection.execute('''
#         select * from products
#         ''')

class MainWindow():

    def __init__(self, root):
        self.root = root

        self.search_section = SearchSection(root)
        self.search_section.grid(row=0, column=0, rowspan=1, sticky=N+S+W+E)
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)

        self.columns_section = ColumnsSection(root)
        self.columns_section.grid(row=1, column=0, rowspan=10, sticky=N+S+W+E)
        Grid.rowconfigure(self.root, 1, weight=10)
        Grid.columnconfigure(self.root, 0, weight=10)

def main():
    root = Tk()
    root.title('Recipes Database')
    root.geometry('800x600')

    main_window = MainWindow(root)

    root.mainloop()

if __name__ == '__main__' : main() 

