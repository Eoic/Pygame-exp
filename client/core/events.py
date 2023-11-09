class EventHandler:
    targets = {}

    @classmethod
    def register(cls, event_type):
        def decorator(func):
            if hasattr(func, '__self__') and func.__self__ is not None:
                print('Registered with self')
                func_type = (func.__self__, event_type)
            else:
                print('Registered none')
                func_type = (None, event_type)

            EventHandler.targets.setdefault(func_type, []).append(func)

        return decorator

    @classmethod
    def notify(cls, event, instance):
        # handlers = cls.targets[event.type] if event.type in EventHandler.targets else []
        for func_type, handlers in cls.targets.items():
            instance, event_type = func_type
            if event_type == event.type:
                for func in handlers:
                    if instance is None or (event.__self__ is not None and instance == event.__self__):
                        func(instance, event)

        # for func in handlers:
        #     func(event)
