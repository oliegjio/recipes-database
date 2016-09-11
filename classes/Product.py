from tkinter import *
from PIL import Image, ImageTk
from classes.BaseClass import *

class Product(Frame, BaseClass):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        BaseClass.__init__(self)

        self['bg'] = 'white'

        Grid.columnconfigure(self, 1, weight=1)
        
        image_size = 70

        picture = ImageTk.PhotoImage(Image.open('cupcake.jpg').resize((image_size, image_size), Image.ANTIALIAS))
        picture_label = Label(self, image=picture, bg='lightgrey')
        picture_label.image = picture
        picture_label.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))

        name = Label(
            self,
            text='Cupcake',
            bg='white',
            font=('Halvetica', 13, 'normal', 'underline')
        )
        name.grid(column=1, row=1, sticky=W, padx=(20, 0), pady=(0, 10))

        delete = Button(
            self,
            text='Delete',
            bg='white',
            fg='red',
            command=self.delete_event,
            borderwidth=0,
            highlightthickness=0
        )
        delete.grid(column=0, row=0, sticky=W, pady=(10, 5), padx=(15, 0))

        edit = Button(
            self,
            text='Edit',
            bg='white',
            fg='green',
            borderwidth=0,
            highlightthickness=0,
            command=self.edit_event
        )
        edit.grid(column=1, row=0, sticky=E, pady=(10, 5), padx=(0, 15))

    def delete_event(self):
        print('Delete event')

    def edit_event(self):
        print('Edit event')
