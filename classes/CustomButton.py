from tkinter import *
from classes.BaseClass import *

class CustomButton(Button, BaseClass):
    
    def __init__(self, parent, **kw):
        BaseClass.__init__(self)

        if not 'font' in kw: kw['font'] = (self.default_font, 10, 'normal', 'underline')
        if not 'borderwidth' in kw: kw['borderwidth'] = 0

        if 'view' in kw:
            
            if kw['view'] == 'border_orange':
                if not 'bg' in kw: kw['bg'] = 'orange'
                if not 'highlightthickness' in kw: kw['highlightthickness'] = 2
                if not 'fg' in kw: kw['fg'] = 'white'
                if not 'highlightbackground' in kw: kw['highlightbackground'] = kw['bg']

            elif kw['view'] == 'border_green':
                if not 'bg' in kw: kw['bg'] = 'sea green'
                if not 'highlightthickness' in kw: kw['highlightthickness'] = 2
                if not 'fg' in kw: kw['fg'] = 'white'
                if not 'highlightbackground' in kw: kw['highlightbackground'] = kw['bg']
                    
            elif kw['view'] == 'normal_red':
                if not 'bg' in kw: kw['bg'] = 'white'
                if not 'highlightthickness' in kw: kw['highlightthickness'] = 0
                if not 'fg' in kw: kw['fg'] = 'red'
                if not 'highlightbackground' in kw: kw['highlightbackground'] = kw['bg']

            elif kw['view'] == 'normal_green':
                if not 'bg' in kw: kw['bg'] = 'white'
                if not 'highlightthickness' in kw: kw['highlightthickness'] = 0
                if not 'fg' in kw: kw['fg'] = 'green'
                if not 'highlightbackground' in kw: kw['highlightbackground'] = kw['bg']

            elif kw['view'] == 'normal_blue':
                if not 'bg' in kw: kw['bg'] = 'white'
                if not 'highlightthickness' in kw: kw['highlightthickness'] = 0
                if not 'fg' in kw: kw['fg'] = 'blue'
                if not 'highlightbackground' in kw: kw['highlightbackground'] = kw['bg']

            else:
                raise Exception('wrong "view" kwarg!')

            del kw['view']

        else:
            raise Exception('"view" kwarg not exist in CustomButton class instance!')

        Button.__init__(self, parent, **kw)

