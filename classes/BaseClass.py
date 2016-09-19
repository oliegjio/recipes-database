from classes.Event import *

class BaseClass():

    def __init__(self):
        self.event_dispatcher = EventDispatcher()

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
