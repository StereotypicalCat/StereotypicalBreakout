
class GameObject:
    """  
    The standard class for all objects in our game (Bricks, Paddle, Ball). This contains some usefull functions for Collision detection, and blitting.
    """

    def __init__(self, position, size, sprite, ObjectType):
        self.__position = position
        self.__size = size
        self.__sprite = sprite
        self.__type = ObjectType

    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    def getSize(self):
        return self.__size

    def getSprite(self):
        return self.__sprite

    def getType(self):
        return self.__type

    def __intersectsY(self, other):
        otherPositionY = other.getPosition()[1]
        otherSizeY = other.getSize()[1]

        if (self.__position[1] >= otherPositionY) and (self.__position[1] <= (otherPositionY + otherSizeY)): # Checks if the upper part of our object is in the other object
            return True
        if ((self.__position[1] + self.__size[1]) >= otherPositionY) and ((self.__position[1] + self.__size[1]) <= (otherPositionY + otherSizeY)): # Checks if the lower part of our object is in the other object
            return True
        return False

    def __intersectsX(self, other):
        otherPositionX = other.getPosition()[0]
        otherSizeX = other.getSize()[0]

        if (self.__position[0] >= otherPositionX) and (self.__position[0] <= (otherPositionX + otherSizeX)): # Checks if the left part of our object is inbetween the other objecct
            return True
        if((self.__position[0] + self.__size[0]) >= otherPositionX) and ((self.__position[0] + self.__size[0]) <= (otherPositionX + otherSizeX)): # Check if the right part of our object is inbetween the other object
            return True
        return False

    def intersects(self, other):
        if self.__intersectsX(other) and self.__intersectsY(other):
            return True
