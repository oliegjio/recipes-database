class EventDispatcher():

    class __EventDispatcher():

        def __init__(self):
            self._events = dict()

        def __del__(self):
            self_events = None

        def has_listener(self, event_type, listener):
            if event_type in self._events.keys():
                return listener in self._events[event_type]
            else:
                return False

        def dispatch_event(self, event):
            if event.type in self._events.keys():
                listeners = self._events[event.type]

                for listener in listeners:
                    listener(event)

        def add_event_listener(self, event_type, listener):
            if not self.has_listener(event_type, listener):
                listeners = self._events.get(event_type, [])

                listeners.append(listener)

                self._events[event_type] = listeners

        def remove_event_listener(self, event_type, listener):
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
