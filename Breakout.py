import sys
sys.path.append('..')
import pygame
from Game import *
from Game.Scenes import *
from Game.Shared import GameConstants

# temp
from random import randint


class Breakout:
    """  The breakout class is the "Game Manager". It manages the scores, the fps, most of pygame, lives, switches between
     different scenes, and almost every class i made has a reference to it. If everything else in this project it paint
     this is the painter, who puts it all together.
    """

    def __str__(self):  # defines what print(Breakout) outputs
        return "An Instance of the Breakout Class, used to manage the game"

    def __init__(self):  # Initating the Game
        self.__lives = GameConstants.START_LIVES  # Reset Lives
        self.__score = 0  # Reset Scores

        # Creating an instance of the Level class, and creating a reference to it
        self.__level = Level(self)
        self.__level.load(0)  # Loads the first levle.

        self.__pad = Pad( # Creates our paddle at half the screen's size in x, and 2 paddle's size space between the bottom
                (GameConstants.SCREEN_SIZE[0]/2,
                GameConstants.SCREEN_SIZE[1] - (2 * GameConstants.PAD_SIZE[1])
                ),
            pygame.image.load(GameConstants.SPRITE_PAD) # The pads sprite.
        )

        self.__balls = [ # Creates a reference to all the balls in the game. You can add more if you want. Though the coordinats get reset as long as its not in motion
            Ball(
                (400, 200),
                pygame.image.load(GameConstants.SPRITE_BALL),
                self
            ),
        ]

        # Initilizing Pygame
        pygame.init()
        pygame.mixer.init()

        # Set the pygame-window's title
        pygame.display.set_caption("Stereotypical Breakout")

        # Starts the pygame clock, and adds a reference to it (used to make sure the game does not run faster than x fps.
        self.__clock = pygame.time.Clock()

        # Creates a new pygame-display. DOUBLEBUFF = doublebuffering = Antialiasing. 32 = Color depth.
        self.screen = pygame.display.set_mode(
            GameConstants.SCREEN_SIZE, pygame.DOUBLEBUF, 32)
        
        pygame.mouse.set_visible(False)  # Removes the cursor

        self.__scenes = (  # Sets up the different scenes i have
            PlayingGameScene(self),
            GameOverScene(self),
            HighscoreScene(self),
        )

        self.__currentScene = 0 # currentScene can be set via. a method. Look at self.__scenes to see what number represents what, or look in GameConstants

        self.__sounds = (  # Creates a list to reference different sound files. For ease of use, the indexes have been written down in GameConstants
            pygame.mixer.Sound(GameConstants.SOUND_FILE_GAMEOVER),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_SPEEDUP),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_EXTRALIFE),
            pygame.mixer.Sound(GameConstants.SOUND_FILE_LOSE_LIFE),
            # I have multiple sound files for the brick or wall hit. Im creating a nested list for those
            ( 
                pygame.mixer.Sound(GameConstants.SOUND_FILE_BRICK_OR_WALL_HIT1),
                pygame.mixer.Sound(GameConstants.SOUND_FILE_BRICK_OR_WALL_HIT2),
                pygame.mixer.Sound(GameConstants.SOUND_FILE_BRICK_OR_WALL_HIT3)
            ),
            # Same as above.
            (
                pygame.mixer.Sound(GameConstants.SOUND_FILE_PADHIT1),
                pygame.mixer.Sound(GameConstants.SOUND_FILE_PADHIT2),
                pygame.mixer.Sound(GameConstants.SOUND_FILE_PADHIT3)
            )



        )

    def start(self):
        while True: # This is the game loop, this is the whole program.
            self.__clock.tick(GameConstants.FPS_LIMIT) # Sets the fps limit to 60
            self.screen.fill((0, 0, 0))  # Fills the screen with black

            currentScene = self.__scenes[self.__currentScene] # References the already instantiated currentScene
            currentScene.handleEvents(pygame.event.get()) # Calls the event handler of the scene
            currentScene.render() # Makes the scene do its stuff

            pygame.display.update() # Displays the queued objects to the screen.

    def changeScene(self, scene):
        self.__currentScene = scene

    def getLevel(self):
        return self.__level

    def getScore(self):
        return self.__score

    def increaseScore(self, score):
        self.__score += score

    def getLives(self):
        return self.__lives

    def getBalls(self):
        return self.__balls

    def getPad(self):
        return self.__pad

    def playSound(self, sound_clip):
        if type(self.__sounds[sound_clip]) is tuple: # Checks to see if there are more than one sound effect
            SoundToPlay = self.__sounds[sound_clip][randint(0, 2)] # Choses a random sound effect.
        else:
            SoundToPlay = self.__sounds[sound_clip] # Else it just choses the sound at that index
        SoundToPlay.stop()
        SoundToPlay.play()

    def reduceLives(self):
        self.__lives -= 1

    def increaseLives(self):
        self.__lives += 1

    def reset(self): # Resets the game
        self.__lives = GameConstants.START_LIVES
        self.__score = 0
        self.__level.load(0)


Breakout().start() # THE GAME STARTER!!!!!!!!!!!! This is the only command (aside form imports) that isnt in a class.

