import random

def wordPicker(): #Getting the random word for the hangman game
    WORDLIST =  ["echo", "atmosphere", "bridge", "exception", "diversion", "invention","cargo", "flicker", "grenade", "home", "jagged",
             "kick","legion", "mountain", "nasty", "options", "personal", "quality", "xylophone", "hippopotomus"]
    randomWord = random.choice(WORDLIST)
    if letter in len(randomWord):
        letter = "__"
   




wordPicker()
