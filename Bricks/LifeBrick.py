from Game.Bricks import Brick
from Game.Shared import *


class LifeBrick(Brick):
    """  
    Increases the amount of lives when hit. 
    """
    def __init__(self, position, sprite, game):
        super(LifeBrick, self).__init__(position, sprite, game)

    def hit(self): # Increases lives
        self.getGame().increaseLives()
        super(LifeBrick, self).hit()

    def getHitSound(self):
        return GameConstants.SOUND_EXTRALIFE
