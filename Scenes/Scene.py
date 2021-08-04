import pygame


class Scene:
    """  
    The schematic for all scenes in our game.
    """
    def __init__(self, game):
        self.__game = game
        self.__texts = []
        self.Myfont = pygame.font.Font(None, 30)  # Font name, size

    def render(self):
        for text in self.__texts:
            self.__game.screen.blit(text[0], text[1])

    def getGame(self):
        return self.__game

    def handleEvents(self, events):
        pass

    def clearText(self):
        self.__texts = []

    def addText(self, text, x=0, y=0, color=[255, 255, 255], background_color=[0, 0, 0], size=17): # Adds text to the blitting queue using the font created in the init. Has some standard values for color and background color incase i forget to add any >.<
        self.__texts.append(
            [self.Myfont.render(text, True, color, background_color), (x, y)])
