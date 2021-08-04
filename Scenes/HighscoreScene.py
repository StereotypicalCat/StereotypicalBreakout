from Game.Scenes.Scene import Scene
from Game.Shared import *
from Game import Highscore
import pygame


class HighscoreScene(Scene):
    """  
    A scene for displaying Highscores (not adding them).
    """
    def __init__(self, game):
        super(HighscoreScene, self).__init__(game)
        self.__GameOverSprite = pygame.image.load(
            GameConstants.SPIRTE_HIGHSCORE) # Loads the sprite for use later
        self.__highscore = Highscore() # Loads the highscores.

    def render(self): # A bunch of the objects in this class could be moved to the init class, but its down here incase we want some cool effects on the highscore scene, because then we need to redraw text
        self.getGame().screen.blit(self.__GameOverSprite, (0, 0))

        self.clearText() # Clears text from the blitting queue

        # Defines start position of text
        x = GameConstants.SCREEN_SIZE[0]*0.5 
        y = GameConstants.SCREEN_SIZE[1]*0.2

        self.__highscore.load() # reloads the highscores.

        for score in self.__highscore.getScores(): # Puts each score in the blitting queue
            self.addText(score[0], x, y, (133, 133, 133))
            self.addText(str(score[1]), x + 200, y, (133, 133, 133))

            y += 30 # Makes sure the text is not on top of eachother

        self.addText("Press F1 to restart the game",
                     GameConstants.SCREEN_SIZE[0]/2, GameConstants.SCREEN_SIZE[1]-60) # Text to guide the user, how to restart

        super(HighscoreScene, self).render()

    def handleEvents(self, events):
        super(HighscoreScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1: # Restarts the game if F1 is pressed 
                    game = self.getGame()
                    game.change_scene(GameConstants.PLAYING_SCENE)

            if event.type == pygame.QUIT: # Exits the program, if we close it down.
                exit()
