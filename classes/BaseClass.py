from classes.Event import *
from classes.EventDispatcher import *
from classes.Database import *

class BaseClass():

    def __init__(self):
        self.event_dispatcher = EventDispatcher()
        self.database = Database()
        self.default_font = 'Halvetica'

    def update_root(self):
        self.update()
        self.update_idletasks()
        if(getattr(self.parent, 'parent', False)):
            self.parent.update_root()
        else:
            self.parent.update()
            self.parent.update_idletasks()

    def get_root(self):
        if(getattr(self, 'root', False)):
            return self.root
        return self.parent.get_root()
