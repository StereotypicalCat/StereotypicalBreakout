import os


class GameConstants:
    """  
    ALL OF THE CONSTANTS IN THE GAME. IN CAPITAL FOR AUTOCOMPLETION EASE OF USE :=)
    """


    BRICK_SIZE = [128,16]
    BRICKS_PER_ROW = 8
    SCREEN_SIZE = [BRICK_SIZE[0] * BRICKS_PER_ROW , 600] # X Calculated for brick sizes. (8 Bricks per row)
    BALL_SPEED = 3
    BALL_SIZE = [16,16]
    PAD_SIZE = [128,16]
    START_LIVES = 1
    FPS_LIMIT = 60

    # Sprites
    SPRITE_BALL = os.path.join("Assets", "Ball_Small.png") # Os is used when doing cross platform. When it takes the game directory and the file, and then makes the path available cross platform
    SPRITE_BRICK = os.path.join("Assets", "Brick.png")
    SPRITE_SPEEDBRICK = os.path.join("Assets", "Slowness Brick (1).png")
    SPRITE_LIFEBRICK = os.path.join("Assets", "Heart Brick.png")
    SPRITE_PAD = os.path.join("Assets", "pad.png")
    SPIRTE_HIGHSCORE = os.path.join("Assets","Highscore.png")

    # Sounds
    SOUND_FILE_EXTRALIFE = os.path.join("Assets","ExtraLife.wav")
    SOUND_FILE_SPEEDUP = os.path.join("Assets","SpeedUp.wav")
    SOUND_FILE_GAMEOVER = os.path.join("Assets","GameOver.wav")
    SOUND_FILE_BRICK_OR_WALL_HIT1 = os.path.join("Assets","Hit1.wav")
    SOUND_FILE_BRICK_OR_WALL_HIT2 = os.path.join("Assets","Hit2.wav")
    SOUND_FILE_BRICK_OR_WALL_HIT3 = os.path.join("Assets","Hit3.wav")
    SOUND_FILE_LOSE_LIFE = os.path.join("Assets","LoseLife.wav")
    SOUND_FILE_PADHIT1 = os.path.join("Assets","PadHit1.ogg")
    SOUND_FILE_PADHIT2 = os.path.join("Assets","PadHit2.ogg")
    SOUND_FILE_PADHIT3 = os.path.join("Assets","PadHit3.ogg")
    
    # For ease of use when in need of haaving the Game Manager (Breakout) class play a sound
    SOUND_GAMEOVER = 0
    SOUND_SPEEDUP = 1
    SOUND_EXTRALIFE = 2
    SOUND_LOSELIFE = 3
    SOUND_BRICK_OR_WALL_HIT = 4
    SOUND_PAD_HIT = 5

    # Specefying scenes, so code seems more clean. Same as above.
    PLAYING_SCENE = 0
    GAME_OVER_SCENE = 1
    HIGH_SCORE_SCENE = 2
    MENU_SCENE = 3