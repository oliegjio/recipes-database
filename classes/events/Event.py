class Event():
    """ Abstract event class.
    
    Should be inherited to create custom events.
    Custom event must have ASK and RESPOND constants:
    - ASK constant represents an event type when you need do dispatch that event.
    - RESPOND constant represents an event type when you need to answer back to that event from a listener function.

    Has type constant which represents event type.
    Has data field that contains event data.
    """

    def __init__(self, event_type, data=None):
        self._type = event_type
        self._data = data

    @property
    def type(self):
        return self._type

    @property
    def data(self):
        return self._data
