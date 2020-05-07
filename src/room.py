# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = []):
        self.__name = name
        self.__description = description
        self.__items = items
    
    def getRoomItems():
        return self.__items

    def __str__(self):
        return f'{self.__name}, {self.__description}, {self.__items}'