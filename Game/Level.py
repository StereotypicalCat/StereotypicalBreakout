import os
import pygame
from Game.Shared import *
from Game.Bricks import *


class Level:
    """ 
    The level class is used to manage the game levels, loading levels from files, keeping track of how many bricks are left.
    """

    def __init__(self, game):
        self.__game = game
        self.__bricks = [] # An array to keep all our bricks
        self.__amountOfBricksLeft = 0 # To keep track of when the game is over
        self.__currentLevel = 0 # Local reference to currentlevel

        # Setting up sprites for loading levels 
        self.__BrickSprite = pygame.image.load(GameConstants.SPRITE_BRICK)
        self.__SpeedBrickSprite = pygame.image.load(
            GameConstants.SPRITE_SPEEDBRICK)
        self.__LifeBrickSprite = pygame.image.load(
            GameConstants.SPRITE_LIFEBRICK)

    def getBricks(self):
        return self.__bricks

    def getAmountOfBricksLeft(self):
        return self.__amountOfBricksLeft

    def brickHit(self): # Is called when the ball hits and destroys a brick
        self.__amountOfBricksLeft -= 1

    def loadNextLevel(self): # Helper function, this is used instead of having the Breakout class keep track of which Lvel were on.
        self.__currentLevel = self.__currentLevel + 1
        self.load(self.__currentLevel)

    def load(self, level):
        self.__bricks = []

        x, y = 0, 0 # Start position of the bricks

        LevelFile = open(os.path.join(
            "Assets", "Levels", f"level{level}.dat"), "r") # Using os.path to make sure it works on multiple systems, using f strings cause why not.

        for line in LevelFile.readlines():
            for charnumber, currentBrick in enumerate(line):

                if charnumber >= GameConstants.BRICKS_PER_ROW: # If there are more bricks on the line than there are space for in the game
                    break

                if currentBrick == "1": # Normal brick
                    brick = Brick((x, y), self.__BrickSprite, self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "2": # Speed brick
                    brick = SpeedBrick(
                        (x, y), self.__SpeedBrickSprite, self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                elif currentBrick == "3": # Life brick
                    brick = LifeBrick(
                        (x, y), self.__LifeBrickSprite, self.__game)
                    self.__bricks.append(brick)
                    self.__amountOfBricksLeft += 1

                x += GameConstants.BRICK_SIZE[0] # Makes sure bricks spawn next to eachother

            x = 0 # Resets x position
            y += GameConstants.BRICK_SIZE[1] # Goes down a row, uses the bricks y size
