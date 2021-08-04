import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *


class PlayingGameScene(Scene):
    """ 
    The scene that runs as long as were playing the game. Makes calls to update positions, loading the next levels, ending the game, etc. 
    You could call it the Game Managers Assistant, since we use most of our time in this scene..
    """

    def __init__(self, game):
        super(PlayingGameScene, self).__init__(game)

    def render(self): # Gets called from Game Manager class max. 60 times a second.
        super(PlayingGameScene, self).render() # 
        game = super(PlayingGameScene, self).getGame()

        if game.getLives() <= 0: # If we dont have anymore lives, then we switch scenes. We lost.
            game.playSound(GameConstants.SOUND_GAMEOVER)
            game.changeScene(GameConstants.GAME_OVER_SCENE)

        balls = game.getBalls() # Reference to all the balls in the game
        pad = game.getPad() # Reference to the paddle in the game.

        for ball in balls: # If we have multiple balls
            
            if game.getLevel().getAmountOfBricksLeft() == 0: # If we destroyed all the bricks in the Level, go to the next level, reset the balls.
                game.getLevel().loadNextLevel()
                for ball in game.getBalls():
                    ball.setMotion(False)

            # Updating the position of the ball, so we can "correct" it before we blit it to the screen.
            ball.updatePosition()

            for brick in game.getLevel().getBricks(): # Tests to see if theres collision between any brick that is not destroyed, and the ball in the current loop.
                if ball.intersects(brick) and not brick.isDestroyed():
                    game.playSound(brick.getHitSound()) # Plays the hit sound
                    brick.hit() # Calls the brick hit function, in case it has any effect (like the speed brick or life brick)
                    game.getLevel().brickHit() # Decreases the amount of bricks left
                    game.increaseScore(brick.getHitPoints())
                    ball.ChangeDirection(brick, 'brick')
                    break # Same brick cannot be hit twice

            # Use below if we want to have more than 1 ball, and want them to collide
            # for ball2 in balls:
            #    if ball != ball2 and ball.intersects(ball2):
            #        ball.ChangeDirection(ball2)
            #        ball2.ChangeDirection(ball)

            if ball.intersects(pad):
                ball.ChangeDirection(pad, 'pad')
                game.playSound(GameConstants.SOUND_PAD_HIT)

            if ball.isBallDead(): # If ball is offscreen
                ball.setMotion(False)
                game.reduceLives()

            game.screen.blit(ball.getSprite(), ball.getPosition()) # Now that the position has been "corrected", we show the player the result (updates the display).

        for brick in game.getLevel().getBricks(): # Displays the brick if its not destroyed.
            if not brick.isDestroyed():
                game.screen.blit(brick.getSprite(), brick.getPosition())

        # pygame uses different case than i do: snake_case instead of mixedCamelCase
        pad.setPosition((pygame.mouse.get_pos()[0], pad.getPosition()[1])) # Gets the mouse position on the x axis, and sets the paddles position to just that. (and its current y)
        game.screen.blit(pad.getSprite(), pad.getPosition()) # Blits the changes. If you do not want the effect of having the ball being a little behind the paddle, then put the pad.setPosition() up to the top of the document.

        self.clearText()
        self.addText(f"Score: {game.getScore()}", 0,
                     GameConstants.SCREEN_SIZE[1] - 30, (0, 0, 255), (0, 0, 0)) # Displays the score
        self.addText(f"Lives: {game.getLives()}",
                     GameConstants.SCREEN_SIZE[0] - 80, GameConstants.SCREEN_SIZE[1] - 30, (0, 0, 255), (0, 0, 0)) # Displays the lives

    def handleEvents(self, events):
        # Lets the scene class handle the non-scene specific events
        super(PlayingGameScene, self).handleEvents(events)

        for event in events:

            if event.type == pygame.QUIT: # If we close the program
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN: # Sets the ball in motion when we click the left mouse button.
                for ball in self.getGame().getBalls():
                    ball.setMotion(True)
