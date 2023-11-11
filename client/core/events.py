from typing import Type
from pygame.event import Event


class EventHandler:
    handlers = {}
    listeners = {}

    @classmethod
    def register(cls, instance_type_id: Type, event_type: int):
        def decorator(handler):
            cls.handlers.setdefault(event_type, []).append((instance_type_id, handler))
            return handler

        return decorator

    @classmethod
    def add_listener(cls, instance_type_id, instance):
        cls.listeners[instance_type_id] = instance

    @classmethod
    def remove_listener(cls, instance_type: Type):
        del cls.listeners[instance_type]

    @classmethod
    def notify(cls, event: Event):
        active_handlers = cls.handlers.get(event.type, [])

        for instance_type_id, handler in active_handlers:
            instance = cls.listeners.get(instance_type_id)

            if instance is not None:
                handler(instance, event)
