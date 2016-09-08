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

        search_section = SearchSection(root)
        columns_section = ColumnsSection(root)

def main():
    root = Tk()
    root.title('Recipes Database')
    root.geometry('800x600')

    
    main_window = MainWindow(root)

    root.mainloop()

if __name__ == '__main__' : main() 

