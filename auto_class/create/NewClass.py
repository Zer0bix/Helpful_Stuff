class Car:
    # Attributes
    _location = None
    _height = None
    _age = None

    # Initialize
    def __init__(self, location = None, height = None, age = None):

        self._location = location
        self._height = height
        self._age = age

    # Getters
    def getLocation(self):
        return self._location

    def getHeight(self):
        return self._height

    def getAge(self):
        return self._age


    # Mutators
    def setLocation(self, location):
        self._location = location

    def setHeight(self, height):
        self._height = height

    def setAge(self, age):
        self._age = age


