from Game.Shared import GameObject
from Game.Shared import GameConstants


class Brick(GameObject):
    """  
    Can be hit, can be destroyed, increases score. All around a good guy.
    """
    def __init__(self, position, sprite, game):
        self.__game = game
        self.__hitPoints = 100 # For creating bricks that needs multiple hits.
        self.__lives = 1 # Bricks that have multiple lives.
        super(Brick, self).__init__(
            position, GameConstants.BRICK_SIZE, sprite, 'brick')

    def getGame(self):
        return self.__game

    def isDestroyed(self): 
        return self.__lives <= 0

    def getHitPoints(self):
        return self.__hitPoints

    def hit(self):
        self.__lives -= 1

    def getHitSound(self):
        return GameConstants.SOUND_BRICK_OR_WALL_HIT
