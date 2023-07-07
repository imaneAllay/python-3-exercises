class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Custom Class the extends `Exceptions` base class.
#Takes only 1 parameter- message
# Line 4 INVOKES the __init__ of the 'Exception' class

#raise ValidationException
