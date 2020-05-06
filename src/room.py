# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
    
    def __str__(self):
        return f'{self.__name}, {self.__description}'