# dog.py


class Dog:
    # define the constructor
    def __init__(self, name):
        self._name = name
    # encapsulation of instance variables

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name
    # add behavior

    def bark(self):
        print("bark"*3)
