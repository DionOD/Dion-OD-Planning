#Dion O'Dowd
#Hangman V4
#20/5/17
import random


name = str(input("What is your name? ")) #Asks for the players name
print("Welcome to Hangman {}!".format(name)) #Displays the welcome message

fails = 0 #Amount of fails
fails_allowed = int(input("How many trys would you like? "))#How many they're allowed
guessed_letter = str()#Letters they guess

WORDLIST =  ["echo", "atmosphere", "bridge", "exception", "diversion", "invention","cargo", "flicker", "grenade", "home", "jagged",
             "kick","legion", "mountain", "nasty", "options", "personal", "quality", "xylophone", "hippopotomus", "jar", "war", "pig",
             "chef", "grid", "call", "bully", "hangman", "playstation", "computer science", "xbox", "wii", "cars"] #The word list that the words get picked from


def correct(user_guess):
    if user_guess in word:
        if user_guess not in guessed_letter: #Finds out if the letter guessed = to the actual letter they need to guess if it does it prints Correct
            print("Correct!")
            return(True)
    else:
        if user_guess not in word and len(user_guess) == 1 and user_guess in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ':
            if user_guess not in guessed_letter: #Does the same as the correct one but prints Incorrect
                print("Incorrect!") 
                return(False)

print("Guess the word")
print("You can input any letter from a - z ")
wordnumber = random.randint(0, len(WORDLIST))
word = (WORDLIST[wordnumber])
print("__ " * len(word)) #Displays the amount of __ there are in the word

while fails < fails_allowed: 
    user_guess = str(input("Input your Letter Guess: ")) #asks the user to input there guess
    if len(user_guess) != 1 or user_guess not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ': #Finds out if the input is valid or not
        print("That is an invalid input!, Please Try Again")

    if user_guess in guessed_letter:
        print("You have already guessed that letter, Please try again") #Tells the user if they have already inputted the word they just guessed
    is_correct = correct(user_guess)
    guessed_letter = guessed_letter, user_guess

    if is_correct == True:
        print("Still figuring out word display") #Still need to figure out the word display so it replaces the __ with the correct letter

    if is_correct == False: #Tells the user if they got there recent input wrong
        print("Try again")
        fails = fails + 1
        print("You have" , fails_allowed , "guesses left.") #Tells the user how many guesses they have left

    if fails == fails_allowed:
        replay = str(input("Press Y to play again or N to finish game. ")) #Figures out if the user wants to play another game or stop playing
        if replay == "y":
            break
        else:
            quit()


    
    
    


  
   
   



