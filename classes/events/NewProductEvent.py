from classes.events.Event import *

class NewProductEvent(Event):
    """ Event that fires when a new product is created.
    
    Extends:
        Event
    
    Variables:
        ASK {str} -- Event type that should be used when you need to dispatch the event.
        RESPOND {str} -- Event type that should be used when you need to answer back to the event from a listener function.
    """

    ASK = 'NewProductEventAsk'
    RESPOND = 'NewProductEventRespond'
