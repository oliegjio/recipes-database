from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.BaseClass import *
from PIL import Image, ImageTk

class Recipe(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)

        self.parent = parent

        self['bg'] = 'white'

        delete = CustomButton(
            self,
            view='normal_red',
            text='Delete'
        )
        delete.grid(row=0, column=0, pady=(10, 10), padx=(10, 0), sticky=W)


        edit = CustomButton(
            self,
            view='normal_green',
            text='Edit'
        )
        edit.grid(row=0, column=1, pady=(10, 10), padx=(0, 10), sticky=E)

        image_size = 150
        
        picture = ImageTk.PhotoImage(Image.open('cake.jpg').resize((image_size, image_size), Image.ANTIALIAS))
        picture_label = CustomLabel(self, image=picture, bg='lightgrey')
        picture_label.image = picture
        picture_label.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))

        Grid.columnconfigure(self, 1, weight=1)

        text_frame = Frame(self, bg='white')
        text_frame.grid(row=1, column=1, sticky=N+E+W+S)

        Grid.columnconfigure(text_frame, 0, weight=1)

        name = CustomLabel(
            text_frame,
            text='Cake',
            font=(self.default_font, 14, 'normal', 'bold')
        )
        name.grid(row=0, column=0, columnspan=2, sticky=W, padx=(50, 0))

        ingredients_column_1 = CustomLabel(
            text_frame,
            text='''
            1. Яицо куриное
            2. Пшеничная мука
            3. Сливки 33%-ные 
            4. Сыр маскарпоне
            5. Молочный шоколад
            6. Вишневый компот
            ''',
            justify=LEFT
        )
        ingredients_column_1.grid(row=1, column=0, sticky=W+N)


        ingredients_column_2 = CustomLabel(
            text_frame,
            text='''
            7. Топленое сливочное масло
            8. Шоколадное печенье
            9. Клубника
            10. Клубничный йогурт
            11. Мягкий творог
            12. Сахар
            ''',
            justify=LEFT
        )
        ingredients_column_2.grid(row=1, column=1, sticky=W+N, padx=(0, 50))
