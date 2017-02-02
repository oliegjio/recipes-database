class EventDispatcher():
""" Application event manager.

Singletone class that can send events, add or remove listeners to some event.
"""

    class __EventDispatcher():

        def __init__(self):
            self._events = dict()

        def __del__(self):
            self._events = None

        def has_listener(self, event_type, listener):
            """ Checks if the event has the listener.
            
            Arguments:
                event_type {Event} -- The event to check for the listener.
                listener {function} -- Listener function.
            
            Returns:
                {bool} -- Is the event has the listener.
            """

            if event_type in self._events.keys():
                return listener in self._events[event_type]
            else:
                return False

        def dispatch_event(self, event):
            """ Sends the event to all listeners attached to it.

            The event will be dispatched only if there is listeners attached to it.
            
            Arguments:
                event {Event} -- The event to dispatch, has type and data fields.
            """

            if event.type in self._events.keys():
                listeners = self._events[event.type]

                for listener in listeners:
                    listener(event)

        def add_event_listener(self, event_type, listener):
            """ Attaches the listener to the event.
            
            Arguments:
                event_type {Event} -- The event to listen.
                listener {function} -- Listener function.
            """

            if not self.has_listener(event_type, listener):
                listeners = self._events.get(event_type, [])

                listeners.append(listener)

                self._events[event_type] = listeners

        def remove_event_listener(self, event_type, listener):
            """ Detaches the listener from the event.
            
            Arguments:
                event_type {Event} -- Event from which to detach the listener.
                listener {function} -- Listener funciton to detach from the event.
            """

            if self.has_listener(event_type, listener):
                listeners = self._events[event_type]

                if len(listeners) == 1:
                    del self._events[event_type]
                else:
                    listenters.remove(listener)

                    self._events[event_type] = listeners
    
    instance = None

    def __new__(cls):
        if not EventDispatcher.instance:
            EventDispatcher.instance = EventDispatcher.__EventDispatcher()
        return EventDispatcher.instance 

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)
