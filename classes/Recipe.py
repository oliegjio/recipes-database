from tkinter import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.BaseClass import *
from classes.CustomPicture import *
from classes.events.RecipeExpandEvent import *
from PIL import Image, ImageTk

class Recipe(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        BaseClass.__init__(self)

        self.parent = parent
        self['bg'] = 'white'
        self._ingredients = list()
        self._description = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam malesuada erat ut turpis. Suspendisse urna nibh, viverra non, semper suscipit, posuere a, pede.

Donec nec justo eget felis facilisis fermentum. Aliquam porttitor mauris sit amet orci. Aenean dignissim pellentesque felis.

Morbi in sem quis dui placerat ornare. Pellentesque odio nisi, euismod in, pharetra a, ultricies in, diam. Sed arcu. Cras consequat.

Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus.
        """

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

        self._label_name.bind('<Button-1>', self._expand)
        self._picture.bind('<Button-1>', self._expand)
        self._label_ingredients_column_1.bind('<Button-1>', self._expand)
        self._label_ingredients_column_2.bind('<Button-1>', self._expand)

        self.event_dispatcher.add_event_listener(RecipeExpandEvent.ASK, self._shrink)

    def _shrink(self, event):
        data = event.data
        if data == self: return
        else:
            if hasattr(self, '_label_description') and self._label_description:
                self._label_description.grid_forget()
                self._label_description.destroy()
                self._label_description = None
                self._label_description_title.grid_forget()
                self._label_description_title.destroy()
                self._label_description_title = None

    def _expand(self, event):
        self.event_dispatcher.dispatch_event(RecipeExpandEvent(RecipeExpandEvent.ASK, self))

        self._label_description_title = CustomLabel(
            self,
            text='Recipe:',
            font=(self.default_font, 14, 'bold')
        )
        self._label_description_title.grid(row=2, column=0, columnspan=2)

        self._label_description = CustomLabel(
            self,
            text=self._description,
            wraplength=(self.winfo_width() - 40),
            justify=LEFT
        )
        self._label_description.grid(row=3, column=0, columnspan=2)

    def _get_placeholder(self):
        self.database.query('select picture from products where name = "{}"'.format('Banana'))
        return self.database.fetch_one()[0]
