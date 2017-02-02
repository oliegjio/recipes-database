from classes.events.Event import *

class NewRecipeEvent(Event):
    """ Event that fired when a new recipe is created.
    
    Extends:
        Event
    
    Variables:
        ASK {str} -- Event type that should be used when you need to dispatch the event.
        RESPOND {str} -- Event type that should be used when you need to answer back to the event from a listener function.
    """

    ASK = 'NewRecipeEventAsk'
    RESPOND = 'NewRecipeEventRespond'
