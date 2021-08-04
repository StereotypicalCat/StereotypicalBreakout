from Game.Shared import *


class Pad(GameObject):
    """ 
    The pad is our paddle, which the player moves around with his mouse. This class is mostly just to make sure the paddle does not go out of bounds.
    """

    def __init__(self, position, sprite):
        super(Pad, self).__init__(
            position, GameConstants.PAD_SIZE, sprite, 'pad')

    def setPosition(self, position): # Custom set position, that makes sure the pad does not go off screen (cause the mouse position can make the pa dgo offscreen). If it is offscreen, the setPosition sets our pad back, and the runs the setposition function from the gameobject
        NewPosition = [position[0], position[1]]
        if NewPosition[0] + GameConstants.PAD_SIZE[0] > GameConstants.SCREEN_SIZE[0]:
            NewPosition[0] = GameConstants.SCREEN_SIZE[0] - \
                GameConstants.PAD_SIZE[0]
        super(Pad, self).setPosition(NewPosition)
