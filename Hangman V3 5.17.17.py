#Dion O'Dowd
#Hangman V3
#17/5/17
import random


name = str(input("What is your name? ")) #Asks for the players name
print("Welcome to Hangman {}!".format(name)) #Displays the welcome message

fails = 0 #Amount of fails
fails_allowed = int(input("How many trys would you like? "))#How many theyre allowed
guessed_letter = str()#Letters they guess

WORDLIST =  ["echo", "atmosphere", "bridge", "exception", "diversion", "invention","cargo", "flicker", "grenade", "home", "jagged",
             "kick","legion", "mountain", "nasty", "options", "personal", "quality", "xylophone", "hippopotomus"] #The word list that the words get picked from


def correct(user_guess):
    if user_guess in word:
        if user_guess not in guessed_letter: #Finds out if the letter guessed = to the actual letter they need to guess if it does it prints Correct
            print("Correct!")
            return(True)
    else:
        if user_guess not in word and len(user_guess) == 1 and guess in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if user_guess not in guessed_letter: #Does the same as the top one but prints Incorrect
                print("Incorrect!") 
                return(False)

print("Guess the word")
print("You can input any letter from a - z ")
wordnumber = random.randint(0, len(WORDLIST))
word = (WORDLIST[wordnumber])
print("__ " * len(word))
while fails < fails_allowed:
    user_guess = str(input("Input your Letter Guess "))
    if len(user_guess) != 1 or user_guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
        print("That is an invalid input!, Please Try Again")
    


  
   
   



