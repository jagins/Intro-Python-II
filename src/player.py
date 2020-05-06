# Write a class to hold player information, e.g. what room they are in
# currently.
#
class Player:
    def __init__(self, name, currentRoom):
        self.name = name
        self.currentRoom = currentRoom
    
    def getRoom(self):
        return self.currentRoom

    def setRoom(self, room):
        self.currentRoom = room
    
    def __str__(self):
        return f'{self.name} is in {self.currentRoom}'