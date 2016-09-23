from tkinter import *
from classes.BaseClass import *
from classes.CustomLabel import *
from io import BytesIO
from PIL import Image, ImageTk

class CustomPicture(CustomLabel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)

        picture = ImageTk.PhotoImage(Image.open(BytesIO(kw['picture'])).resize((kw['size'], kw['size']), Image.ANTIALIAS))
        self._size = kw['size']

        del kw['picture']
        del kw['size'] 

        kw['image'] = picture
        CustomLabel.__init__(self, parent, **kw)

        self.image = picture

    def set_picture(self, picture):
        picture = ImageTk.PhotoImage(Image.open(BytesIO(picture)).resize((self._size, self._size), Image.ANTIALIAS))
        self['image'] = picture
        self.image = picture

