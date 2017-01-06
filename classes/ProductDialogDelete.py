from tkinter import *
from classes.BaseClass import *
from classes.CustomButton import *
from classes.events.DeleteProductEvent import *
from classes.CustomLabel import *

class ProductDialogDelete(Toplevel, BaseClass):

    def __init__(self, parent, **kw):
        BaseClass.__init__(self)
        Toplevel.__init__(self, parent)

        self._parent = parent
        self['bg'] = 'white'
        self.geometry('350x100')
        if 'data' in kw: self._data = kw['data']

        for i in range(0, 2):
            Grid.columnconfigure(self, i, weight=1)
            Grid.rowconfigure(self, i, weight=1)

        self._button_cancel = CustomButton(
            self,
            view='normal_red',
            text='Cancel'
        )
        self._button_cancel.grid(row=1, column=0)
        self._button_cancel.bind('<Button-1>', self._on_button_cancel_click)

        self._button_apply = CustomButton(
            self,
            view='normal_green',
            text='Accept'
        )
        self._button_apply.grid(row=1, column=1)
        self._button_apply.bind('<Button-1>', self._on_button_apply_click)

        self._label_text = CustomLabel(
            self,
            text='Are you shure you want to delete this product?'
        )
        self._label_text.grid(row=0, column=0, columnspan=2)

    def _on_button_apply_click(self, event):
        self.event_dispatcher.dispatch_event(DeleteProductEvent(DeleteProductEvent.ASK, self._data))
        self.destroy()

    def _on_button_cancel_click(self, event):
        self.destroy()

