from tkinter import *
from classes.BaseClass import *
from classes.CustomButton import *
from classes.CustomLabel import *
from classes.CustomEntry import *
from classes.CustomPicture import *
from classes.events.NewRecipeEvent import *

class RecipeDialogNew(Toplevel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        Toplevel.__init__(self, parent)

        self.parent = parent
        self['bg'] = 'white'
        self.geometry('480x650')

        self._vertical_padding = 20
        self._horizontal_padding = 20

        for i in range(0, 8):
            Grid.columnconfigure(self, i, weight=1)
            Grid.rowconfigure(self, i, weight=1)

        self._label_name = CustomLabel(
            self,
            text="Name: "
        )
        self._label_name.grid(row=0, column=1, sticky=S+W)

        self._entry_name = CustomEntry(
            self,
            width=35
        )
        self._entry_name.grid(row=1, column=1, sticky=N)

        self._label_ingredients = CustomLabel(
            self,
            text='Ingredients:'
        )
        self._label_ingredients.grid(row=2, column=1, sticky=S+W)

        self._frame_ingredients = Frame(self)
        self._frame_ingredients.grid(row=3, column=1, sticky=N+E+W+S)

        self._scrollbar_ingredients = Scrollbar(
            self._frame_ingredients,
            orient=VERTICAL
        )

        self._listbox_ingredients = Listbox(
            self._frame_ingredients,
            selectmode=EXTENDED,
            yscrollcommand=self._scrollbar_ingredients.set
        )
        self._scrollbar_ingredients.config(command=self._listbox_ingredients.yview)
        self._listbox_ingredients.pack(side=LEFT, fill=BOTH, expand=1)
        self._scrollbar_ingredients.pack(side=RIGHT, fill=BOTH)

        for item in self._get_all_ingredients():
            self._listbox_ingredients.insert(END, item[0])

        self._label_description = CustomLabel(
            self, 
            text='Description:'
        )
        self._label_description.grid(row=4, column=1, sticky=S+W)

        self._entry_description = Text(
            self,
            height=10,
            width=50
        )
        self._entry_description.grid(row=5, column=1, sticky=N)

        self._picture = CustomPicture(
            self,
            picture=self._get_placeholder(),
            size=100
        )
        self._picture.grid(row=6, column=1)

        self._button_picture = CustomButton(
            self,
            view='normal_blue',
            text='Change Picture'
        )
        self._button_picture.grid(row=7, column=1, sticky=N)
        self._button_picture.bind('<Button-1>', self._on_button_picture_click)

        self._button_exit = CustomButton(
            self,
            view='normal_red',
            text='Cancel'
        )
        self._button_exit.grid(row=8, column=0, sticky=N+E+W+S, pady=(0, self._vertical_padding), padx=(self._horizontal_padding, 0))
        self._button_exit.bind('<Button-1>', self._on_button_exit_click)

        self._button_apply = CustomButton(
            self,
            view='normal_green',
            text='Apply'
        )
        self._button_apply.grid(row=8, column=2, sticky=N+E+W+S, pady=(0, self._vertical_padding), padx=(0, self._horizontal_padding))
        self._button_apply.bind('<Button-1>', self._on_button_apply_click)

    def _on_button_apply_click(self, event):
        if self._entry_description.get(1.0, END) == '' or not hasattr(self, '_new_picture'): return

        ingredients_indexes = self._listbox_ingredients.curselection()
        ingredients_string = ''
        for i in ingredients_indexes:
            ingredients_string += '|' + self._listbox_ingredients.get(i) + '|'

        self.database.query(
            'insert into recipes (name, description, picture, ingredients) values (?, ?, ?, ?)',
            [
                self._entry_name.get(),
                self._entry_description.get(1.0, END),
                self._new_picture,
                ingredients_string
            ]
        )

        data = dict()
        data['name'] = self._entry_name.get()
        data['description'] = self._entry_description.get(1.0, END)
        data['picture'] = self._new_picture
        data['ingredients'] = ingredients_string

        self.event_dispatcher.dispatch_event(NewRecipeEvent(NewRecipeEvent.ASK, data))

        self.destroy()
        
    def _on_button_exit_click(self, event):
        self.destroy()

    def _get_placeholder(self):
        self.database.query('select `blob` from meta where text = "placeholder"')
        return self.database.fetch_one()[0]

    def _get_all_ingredients(self):
        self.database.query('select `name` from products')
        self._ingredients = self.database.fetch_all()
        return self._ingredients

    def _on_button_picture_click(self, event):
        picture_path  = filedialog.askopenfilename()

        the_file = open(picture_path, 'rb')
        self._new_picture = the_file.read()

        the_file.close()

        self._picture.set_picture(self._new_picture)