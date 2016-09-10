from tkinter import *

class Scrollable():

    def __init__(self):
        self._canvas = Canvas(self, bd=0)
        self.frame = Frame(self._canvas)
        self.frame.grid_propagate(False)
        self._scrollbar = Scrollbar(self, orient=VERTICAL, command=self._canvas.yview)
        self._canvas.configure(yscrollcommand=self._scrollbar.set)
        self._scrollbar.pack(side=RIGHT, fill=Y)
        self._canvas.xview_moveto(0)
        self._canvas.yview_moveto(0)
        self._canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self._frame_id = self._canvas.create_window(0, 0, window=self.frame, anchor=NW)
        self.frame.bind('<Enter>', self._on_enter)
        self.frame.bind('<Leave>', self._on_leave)
        def _configure_frame(event):
            size = (self.frame.winfo_reqwidth(), self.frame.winfo_reqheight())
            self._canvas.config(scrollregion='0 0 %s %s' % size)
            if self.frame.winfo_reqwidth() != self._canvas.winfo_width():
                self._canvas.config(width=self.frame.winfo_reqwidth())
        self.frame.bind('<Configure>', _configure_frame)
        def _configure_canvas(event):
            if self.frame.winfo_reqwidth() != self._canvas.winfo_width():
                self._canvas.itemconfigure(self._frame_id, width=self._canvas.winfo_width())
        self._canvas.bind('<Configure>', _configure_canvas)
    
    def _on_enter(self, event):
        self._mouse_wheel_event_1 = self._canvas.bind_all('<MouseWheel>', self._on_mousewheel)
        self._mouse_wheel_event_2 = self._canvas.bind_all('<Button-4>', self._on_mousewheel)
        self._mouse_wheel_event_3 = self._canvas.bind_all('<Button-5>', self._on_mousewheel)

    def _on_leave(self, event):
        self._canvas.unbind('<MouseWheel>', self._mouse_wheel_event_1)
        self._canvas.unbind('<Button-4>', self._mouse_wheel_event_2)
        self._canvas.unbind('<Button-5>', self._mouse_wheel_event_3)

    def _on_mousewheel(self, event):
        if not (self.winfo_height() >= self.frame.winfo_height()):
            direction = 0
            if event.num == 5 or event.delta == -120:
                direction = 1
            if event.num == 4 or event.delta == 120:
                direction = -1
            self._canvas.yview_scroll(direction, UNITS)
