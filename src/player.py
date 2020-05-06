# Write a class to hold player information, e.g. what room they are in
# currently.
#
class Player:
    def __init__(self, name, currentRoom):
        self.__name = name
        self.__currentRoom = currentRoom

    def getName(self):
        return self.__name
    
    def getRoom(self):
        return self.__currentRoom

    def setRoom(self, room):
        self.__currentRoom = room
    
    def __str__(self):
        return f'{self.__name} is in {self.__currentRoom}'