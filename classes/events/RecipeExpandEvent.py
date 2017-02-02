from classes.events.Event import *

class RecipeExpandEvent(Event):
    """ Event that fires when a recipe is expanded.
    
    Extends:
        Event
    
    Variables:
        ASK {str} -- Event type that should be used when you need to dispatch the event.
        RESPOND {str} -- Event type that should be used when you need to answer back to the event from a listener function.
    """

    ASK = 'RecipeExpandEventAsk'
    RESPOND = 'RecipeExpandEventRespond'
