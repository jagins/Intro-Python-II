class Item: 
    def __init__(self, name):
        self.__name = name

    def getItemName(self):
        return self.__name

    def setItemName(self, name):
        self.__name = name

    def __str__(self):
        return f'{self.__name}'