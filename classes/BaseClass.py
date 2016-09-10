class BaseClass():

    def __init__(self):
        pass

    def update_root(self):
        self.update()
        self.update_idletasks()
        if(getattr(self.parent, 'parent', False)):
            self.parent.update_root()
        else:
            self.parent.update()
            self.parent.update_idletasks()

