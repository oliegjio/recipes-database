from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.BaseClass import *
from classes.CustomPicture import *
from PIL import Image, ImageTk

class Recipe(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)

        self.parent = parent
        self['bg'] = 'white'

        self._button_delete = CustomButton(
            self,
            view='normal_red',
            text='Delete'
        )
        self._button_delete.grid(row=0, column=0, pady=(10, 10), padx=(10, 0), sticky=W)


        self._button_edit = CustomButton(
            self,
            view='normal_green',
            text='Edit'
        )
        self._button_edit.grid(row=0, column=1, pady=(10, 10), padx=(0, 10), sticky=E)

        # picture = ImageTk.PhotoImage(Image.open('cake.jpg').resize((image_size, image_size), Image.ANTIALIAS))
        # picture_label = CustomLabel(self, image=picture, bg='lightgrey')
        # picture_label.image = picture
        # picture_label.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))
        self._picture = CustomPicture(self, picture=self._get_placeholder(), size=150)
        self._picture.grid(column=0, row=1, pady=(0, 10), padx=(10, 0))
        
        Grid.columnconfigure(self, 1, weight=1)

        self._frame_text = Frame(self, bg='white')
        self._frame_text.grid(row=1, column=1, sticky=N+E+W+S)

        Grid.columnconfigure(self._frame_text, 0, weight=1)

        self._label_name = CustomLabel(
            self._frame_text,
            text='Cake',
            font=(self.default_font, 14, 'normal', 'bold')
        )
        self._label_name.grid(row=0, column=0, columnspan=2, sticky=W, padx=(50, 0))

        self._label_ingredients_column_1 = CustomLabel(
            self._frame_text,
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
        self._label_ingredients_column_1.grid(row=1, column=0, sticky=W+N)


        self._label_ingredients_column_2 = CustomLabel(
            self._frame_text,
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
        self._label_ingredients_column_2.grid(row=1, column=1, sticky=W+N, padx=(0, 50))

    def _get_placeholder(self):
        self.database.query('select picture from products where name = "{}"'.format('Apple'))
        return self.database.fetch_one()[0]
