from classes.events.Event import *

class SearchEvent(Event):
    """ Event that fires when user types in search bar.
     
    Extends:
        Event

    Variables:
        ASK {str} -- Event type that should be used when you need to dispatch the event.
        RESPOND {str} -- Event type that should be used when you need to answer back to the event from a listener function.
    """

    ASK = 'SearchEventAsk'
    RESPOND = 'SearchEventRespond'
