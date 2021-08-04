from Game.Bricks import Brick
from Game.Shared import *


class SpeedBrick(Brick):
    """  
    Increases the speed of the ball
    """
    def __init__(self, position, sprite, game):
        super(SpeedBrick, self).__init__(position, sprite, game)

    def hit(self): # Increases the speed of all balls by 1
        for ball in self.getGame().getBalls():
            ball.setSpeed(ball.getSpeed() + 1)
        super(SpeedBrick, self).hit()

    def getHitSound(self):
        return GameConstants.SOUND_SPEEDUP
