
  #Dion O'Dowd
#Hangman V9
#29/5/17
import random
import time

name = str(input("What is your name? ")) #Asks for the players name
print("Welcome to Hangman", name,"!") #Displays the welcome message

fails = 0 #Amount of fails
FAILS_ALLOWED = 3#How many they're allowed
guessed = []#Letters they guess

WORDLIST =  ["echo", "atmosphere", "bridge", "exception", "diversion", "invention","cargo", "flicker", "grenade", "home", "jagged",
             "kick","legion", "mountain", "nasty", "options", "personal", "quality", "xylophone", "hippopotomus", "jar", "war", "pig",
             "chef", "grid", "call", "bully", "hangman", "playstation", "computer science", "xbox", "wii", "cars"] #The word list that the words get picked from


def correct(user_guess):
    if user_guess in word:
        if user_guess not in guessed: #Finds out if the letter guessed = to the actual letter they need to guess if it does it prints Correct
            print("{} is Correct!".format(user_guess))
            return(True)
    else:
        if user_guess not in word and len(user_guess) == 1 and user_guess in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if user_guess not in guessed: #Does the same as the correct one but prints Incorrect
                print("{} is Incorrect!".format(user_guess))
                return(False)

            



print("Guess the word")
print("You can input any letter from aA - zZ and the space bar")
wordnumber = random.randint(0, len(WORDLIST))
word = (WORDLIST[wordnumber])
guessed_letters = len(word) * ['__']
print(' '.join(guessed_letters))#Displays the amount of __ there are in the word


while fails < FAILS_ALLOWED:
    user_guess = str(input("Input your Letter Guess: ")) #asks the user to input there guess
    if len(user_guess) != 1 or user_guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ': #Finds out if the input is valid or not
        print("That is an invalid input!, Please Try Again")

    if user_guess in guessed:
        print("You have already guessed that letter, Please try again") #Tells the user if they have already inputted the word they just guessed
    is_correct = correct(user_guess)
    guessed = guessed, user_guess

    if is_correct == True:
        for position, letter in enumerate(word):
            if letter == user_guess:
                guessed_letters[position] = letter
                print(' '.join(guessed_letters))

    if is_correct == False: #Tells the user if they got there recent input wrong
        print("Try again")
        fails = fails + 1
        print("You have" , FAILS_ALLOWED ,"guesses left.")#Tells the user how many guesses they have left


    if word == fails:
        print("Sorry you have ran out of guesses")

    else:
        print("You have guessed the word!")

    if fails == FAILS_ALLOWED:
        replay = str(input("Press 1 to play again, press 2 to exit."))
        if replay == 1:
            break
        else:
            quit()




