class ObserverAble : 
    def __init__(self) : 
        self.handlers = [] 
    def add_observer(self , *handlers ): 
        self.handlers.extend(handlers) 
    def remove_observer(self , *handlers):
        for handler in handlers :
            if handler in self.handlers: 
                self.handlers.remove(handler)
    def call_observers(self , *args): 
        for handler in self.handlers: 
            handler(*args) 
    @property
    def get_observers(self):
        return self.handlers.copy() 
        