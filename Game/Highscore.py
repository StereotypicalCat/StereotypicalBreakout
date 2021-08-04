import hashlib
import operator
import os


class Highscore:
    """ 
    The highscore class keeps track of loading and adding highscores
    Highscore file is in the format of:
    <name> [::] <score> [::] <md5>
    """

    def __init__(self):
        self.__highscore = self.load()

    def getScores(self):
        return self.__highscore

    def load(self):
        highscores = []
        HighscoreFile = open(os.path.join("Assets", "Highscores.dat"), "r") # Opens the file, uses os to make sure it works on multiple platforms.
        for line in HighscoreFile.readlines():
            Username, Score, md5 = line.split("[::]") # Splits the string into Username Score and MD5, and adds them to a list (values are seperated by [::])
            
            md5 = md5.replace("\n", "") # There might be a \n (newline) at the end of the string.

            if hashlib.md5((Username + str(Score) + "SaltySaltWithExtraSalt").encode()).hexdigest() == md5: # Checks if the md5 of name, score and salt equals the md5 in the doument (which it should)
                highscores.append([Username, int(Score), md5]) # Adds the values to the highscore array if theres nothing wrong

        HighscoreFile.close()

        # Sorts the highscore, using the score value, from highest to lowest
        highscores.sort(key=operator.itemgetter(1), reverse=True) 

        # Only keeping top 10
        highscores = highscores[0:9]

        return highscores

    def add(self, Username, Score):
        UserHash = hashlib.md5(
            (Username + str(Score) + "SaltySaltWithExtraSalt").encode()).hexdigest() # Hashes the name, score and salt using md5

        self.__highscore.append([Username, int(Score), UserHash]) # Appends it to the private highscore variable

        HighscoreFile = open(os.path.join("Assets", "Highscores.dat"), 'w') # Overwrites the file (deletes everything there is)
        for name, score, md5 in self.__highscore: # Writes all the different scores in, newline at the end
            HighscoreFile.write(f"{name}[::]{score}[::]{md5}\n")

        HighscoreFile.close()
