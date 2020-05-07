# Write a class to hold player information, e.g. what room they are in
# currently.
#
from item import Item

class Player:
    def __init__(self, name, currentRoom, itemList = []):
        self.__name = name
        self.__currentRoom = currentRoom
        self.__itemList = itemList
        self.__itemCount = 2

    def getName(self):
        return self.__name
    
    def getRoom(self):
        return self.__currentRoom

    def setRoom(self, room):
        self.__currentRoom = room

    def addItem(self, item):
        if(self.__itemList < 2):
            self.__itemList.append(Item(item))
        else:
            print('Inventory is full can only carry 2 items at a time')
    
    def dropItem(self, item):
        self.__itemList.remove(item)

    
    def __str__(self):
        return f'{self.__name} is in {self.__currentRoom}'