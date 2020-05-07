# Write a class to hold player information, e.g. what room they are in
# currently.
#

class Player:
    def __init__(self, name, currentRoom, itemList = []):
        self.__name = name
        self.__currentRoom = currentRoom
        self.__itemList = itemList
        self.__itemCount = 2
        self.__error = ''

    def getName(self):
        return self.__name
    
    def getRoom(self):
        return self.__currentRoom

    def setRoom(self, room):
        self.__currentRoom = room

    def addItem(self, item):
        if(len(self.__itemList) < 2):
            self.__error = ''
            self.__itemList.append(item)
        else:
            self.__error =  'Inventory is full can only carry 2 items at a time'
    
    def dropItem(self, item):
        self.__itemList.remove(item)

    def getItems(self):
        return self.__itemList

    def getErrorMessage(self):
        return self.__error
    
    def __str__(self):
        return f'{self.__name} is in {self.__currentRoom} {self.__error}'