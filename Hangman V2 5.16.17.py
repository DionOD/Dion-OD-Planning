#Dion O'Dowd
#Hangman V2
#16/5/17
import random

def welcomeMessage():
    name = input("What is your name? ")
    print("Welcome to Hangman {}!".format(name))
    int(input("Please pick how many games you would like to play (between 1 - 5)"))

def wordPicker(): #Getting the random word for the hangman game
    WORDLIST =  ["echo", "atmosphere", "bridge", "exception", "diversion", "invention","cargo", "flicker", "grenade", "home", "jagged",
             "kick","legion", "mountain", "nasty", "options", "personal", "quality", "xylophone", "hippopotomus"]
    randomWord = random.choice(WORDLIST)
   
   



welcomeMessage()
wordPicker()
