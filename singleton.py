class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated
    
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance
    
    def __call__(self):
        raise TypeError('Singleton')
    
    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
