import pygame
from Game.Scenes.Scene import Scene
from Game.Shared import *
from Game import Highscore


class GameOverScene(Scene):
    """  
    A scene for adding your highscore.
    """

    __PlayerName = ""

    def __init__(self, game):
        super(GameOverScene, self).__init__(game)

    def render(self):

        self.clearText() # Clears text already in the blitting queue

        # Displays what the user is typing right now
        self.addText("Your Name:", x=400, y=400, color=[125, 125, 125]) 
        self.addText(self.__PlayerName, x=600, y=400, color=[125, 125, 125])

        super(GameOverScene, self).render()

    def handleEvents(self, events):
        # Lets the scene class handle the non-scene specific events
        super(GameOverScene, self).handleEvents(events)

        for event in events:
            if event.type == pygame.KEYDOWN: # If a key has been pressed
                
                if event.key == pygame.K_RETURN: # If its the enter key
                    game = self.getGame()
                    UsersScore = game.getScore()
                    UsersName = self.__PlayerName
                    Highscore().add(UsersName, UsersScore) # Creates a new instance of the highscore class, and adds the highscore.
                    game.reset() # Resets the playingGameScene variables
                    game.changeScene(GameConstants.HIGH_SCORE_SCENE) # Conteniues to the Highscore scene

                elif (chr(event.key)).isalpha() and len(self.__PlayerName) < 7: # If the user is pressing an alphabetic character on the keyboard, and the playername is less than 7
                    self.__PlayerName = self.__PlayerName + \
                        (chr(event.key)).upper() # Adds the uppercase version of the character (we dont want small letters)
 
                elif event.key == pygame.K_BACKSPACE: # Deletes a letter
                    self.__PlayerName = self.__PlayerName[:-1]

                elif event.key == pygame.K_SPACE: # Creates a space in the name
                    self.__PlayerName = self.__PlayerName + " "

            if event.type == pygame.QUIT:
                exit()
