from Game.Shared import *
import pygame


class Ball(GameObject):
    """ 
    The ball is a class used to create balls in our games, and houses most of all collision detection.
    """


    def __init__(self, position, sprite, game):
        self.__game = game
        self.__speed = GameConstants.BALL_SPEED
        self.__increment = [2, 2] # To know how much to increment x and y. To be used in the future for creating more advanced collision detection.
        self.__direction = [1, -1]
        self.__inMotion = False

        super(Ball, self).__init__(
            position, GameConstants.BALL_SIZE, sprite, 'ball')

    def setSpeed(self, newSpeed):
        self.__speed = newSpeed

    def resetSpeed(self):
        self.setSpeed(GameConstants.BALL_SPEED)

    def getSpeed(self):
        return self.__speed

    def inMotion(self):
        return self.__inMotion

    def setMotion(self, isMoving):
        self.__inMotion = isMoving
        self.resetSpeed()

    def ChangeDirection(self, gameObject, ObjectHit): # Changes the balls direction according to the placement of the other game object.

        BallSize = self.getSize()
        BallPosition = self.getPosition()
        OtherSize = gameObject.getSize()
        OtherPosition = gameObject.getPosition()

        if ObjectHit == 'brick':
            """  
            We know the objects have hit eachother. Now we just need to figure out from which side.
            """
            BallPreviousPosition = [
                BallPosition[0] - (self.__increment[0] *
                                   self.__speed * self.__direction[0]),
                BallPosition[1] - (self.__increment[1] *
                                   self.__speed * self.__direction[1])
            ]
            
            if (BallPreviousPosition[0] >= (OtherPosition[0] + OtherSize[0])) or ((BallPreviousPosition[0] + BallSize[0]) <= OtherPosition[0]):
                # This is a hit form the side, since the balls left and right x was not in the range of the gameObjects x values. You could say its "Most likely" a hit form the side
                self.__direction[0] *= -1 # Shifts the x direction
                self.setPosition(
                    (
                        BallPreviousPosition[0],
                        BallPosition[1]
                    ) # Puts the ball nicely outside the brick
                )
            else:
                # If its not a hit form the side, its a hit from the top / bottom
                self.__direction[1] *= -1 # Shifts the y direction
                self.setPosition(
                    (
                        BallPosition[0],
                        BallPreviousPosition[1]
                    ) # Puts the ball nicely outside the brick.
                )

        if ObjectHit == 'pad':
            """ 
            We know the two objects hit eachother. Now, all we need to figure out is, where on the paddle it hit. I split it up into three different parts. Firstly, we have the left part of the paddle.
            The left part will always result in a ball, going the left direction. Hitting the right part of the paddle, will make the ball go right. Hitting the middle, will keep the ball going in the direction its already heading.
            """

            if (BallSize[0]/2 + BallPosition[0]) < (OtherPosition[0] + (0.4 * OtherSize[0])): # Ball center is Leftmost of the paddle. Launches the ball to the left of the paddle
                self.__direction[0] = -1
                self.__direction[1] = -1
                self.setPosition(
                    (
                        BallPosition[0],
                        OtherPosition[1] - BallSize[1]
                    )
                )
            elif (BallSize[0]/2 + BallPosition[0]) > (OtherPosition[0] + (0.6 * OtherSize[0])): # Ball center is Rightmost of the paddle. Launches the ball to the right of the paddle
                self.__direction[0] = 1
                self.__direction[1] = -1
                self.setPosition(
                    (
                        BallPosition[0],
                        OtherPosition[1] - BallSize[1]
                    )
                )
            else: # Ball center is close to the middle of the paddle Just flips the x direction.
                self.__direction[0] *= -1
                self.__direction[1] = -1
                self.setPosition(
                    (
                        BallPosition[0],
                        OtherPosition[1] - BallSize[1]
                    )
                )

    def updatePosition(self):

        if not self.inMotion(): # If its not in motion, we want the paddle floating close to the top of the paddle.
            padPosition = self.__game.getPad().getPosition()
            newPosition = [
                padPosition[0] + ((GameConstants.PAD_SIZE[0] - GameConstants.BALL_SIZE[0])/2), # Puts the ball in the center of the paddle
                padPosition[1] - GameConstants.BALL_SIZE[1] - 10 # Puts the ball a bit above the upper part ofthe paddle (10 pixels.)
            ]
            self.setPosition(newPosition)

            # If it is not in motion (game not started), then dont move the ball
            return

        position = self.getPosition()
        size = self.getSize()

        NewPosition = [
            position[0] + (self.__increment[0] * self.__speed) *
            self.__direction[0],
            position[1] + (self.__increment[1] * self.__speed) *
            self.__direction[1]
        ]

        # Test if the ball is off screen:

        game = self.__game

        if NewPosition[0] + size[0] >= GameConstants.SCREEN_SIZE[0]:  # X aksen ->
            self.__direction[0] *= -1
            NewPosition = [GameConstants.SCREEN_SIZE[0] -
                           size[0], NewPosition[1]]
            game.playSound(GameConstants.SOUND_BRICK_OR_WALL_HIT)

        if NewPosition[0] <= 0:  # X aksen <-
            self.__direction[0] *= -1
            NewPosition = [0, NewPosition[1]]
            game.playSound(GameConstants.SOUND_BRICK_OR_WALL_HIT)

        if NewPosition[1] <= 0:  # y aksen /\
            self.__direction[1] *= -1
            NewPosition = [NewPosition[0], 0]
            game.playSound(GameConstants.SOUND_BRICK_OR_WALL_HIT)

        self.setPosition(NewPosition)

    def isBallDead(self): # Checks if the ball is out of bounds (o)
        position = self.getPosition()
        size = self.getSize()

        if position[1] + size[1] >= GameConstants.SCREEN_SIZE[1]:
            return True
        return False
