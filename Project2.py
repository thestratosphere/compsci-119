#TODO 0:
#COMPSCI 119.01 - Project 2 - Jacqueline "Nora" Cole - Date Submitted: November 10th, 2022
'''
We use random to pick a random word from the supplied words list (saved in the words.py file)
If there is an issue importing the supplied word_list, 
    the smaller word_list will be used instead (this is the try-except statement below)
The failure could have been do to not having the provided words.py file in the same folder as this Project2.py file
'''
from random import choice
try:
    from words import word_list
except:
    print("failed to import large word_list, using the smaller list")
    word_list = ["JAZZ", "APPLES", "GRAPES", "PINEAPPLE", "LACES", "HORSES", "NEWSPAPER", "TO"]

'''
These are several constant variables that will be used by the program
It is better to have them here at the top, so that they are easy to change
These variables were created outside the 'scope' of any other function, so all the code in this file can use them
'''
NUM_TRIES = 6
ENTRY = '\n\t WELCOME TO THE WORD-GUESSER\n'
INSTRUCTION = f"What is your Guess?\n"


'''
This function accepts a letter guess from the user and returns that letter to the caller
It takes an integer, the number of times they have guessed a wrong letter
'''
def prompt(i):
  return input(f"\nEnter letter ({NUM_TRIES-i} left): ").upper()


'''
TODO 1 (Write the function entirely)
We want to create a list that represents the hangman board
This list should be the same number of letters as the given string cw (the chosen word)
Every element of the list should be a _ when it's created, as the player hasn't guessed any of the letters yet
This function should return the list
FOR EXAMPLE: If we are given the word "chosen" for the paramter cw we need to return a list that looks like this:
['_','_','_','_','_','_']
'''
def create_board(cw):
    board = []
    for char in cw:
        board.append("_")
    return board
'''
TODO 2 
(Fill in the ??? lines)
Printer is a helper function, it takes in the list that represents the board
and it prints out that board for the user
If the board looks like this: ['_', 'A', 'Z', 'Z']
then the following should be printed:
    _ A Z Z
This function should not return anything, just print something out
'''
def printer(current):
    to_String = '\t'
    for char in current:
        to_String += char + " "
    print(to_String)

'''
TODO 6
Fill in all the blanks (???) for the play game method

The play game method is our main function for running a single play of the game
It takes the blank game board and the word that was chosen for the player to guess
This function doesn't need to return anything
EXTRA CREDIT 1 and 3 are here too
''' 
def play_game(board, chosen_word):
    wrong_guesses = 0
    guess_history = []

    #What should go here???
    while (wrong_guesses < NUM_TRIES):
        guess = prompt(wrong_guesses)
        #This loop should keep accepting input from the user while 
        # they provide a guess they have guessed before 
        # EXTRA CREDIT 3 HERE AS WELL
        #If the user keeps provided guesses they have tried before, these should not count as wrong guesses
        while (guess in guess_history != True):
          print(f"You have guessed {guess} before, or it is not a single letter")
          guess = prompt(wrong_guesses)
        #add guess to history
        guess_history.append(guess)
        
        #We need to loop through the chosen_word and check to see if the guessed character
        #matched any of the letters in the chosen_word
        #  if we do find the guessed character in the chosen word,
        #  we should update the game board to show the guess at that index instead of _
        #  we then set the flag was_correct so we know that the guess did change the board
        #HINT: The enumerate() function we talked about in class could help here!
        was_correct = False
        for i in range(len(chosen_word)):
            if(chosen_word[i] == guess):
                board[i] = guess
                was_correct = True
    
        
        #If we didn't add a letter to the board
        #  We should let them know the it was a wrong guess
        #  and we should increase the number of wrong guesses
        if(was_correct == False):
            wrong_guesses = wrong_guesses + 1
            if NUM_TRIES-wrong_guesses > 1:
                print(f"You guessed a wrong letter, {NUM_TRIES-wrong_guesses} tries left.")
            else:
                print(f"You guessed a wrong letter, {NUM_TRIES-wrong_guesses} try left, you can do it!")
        
        #print the board so player can see any progress (HINT REMEMBER YOUR HELPER FUNCTIONS)
        printer(board)
        
        #print the guess history so the player knows what guesses have been made
        #EXTRA CREDIT 1 is here too
        print(guess_history)

        #Check if the player has won the game, and let them know if they have
        #  We should also end the function somehow, as the game isn't being played anymore  
        # this should return (nothing or something up to you, just needs to return)
        if(list(chosen_word) == board):
            print(f"Congratulations, you won!")
            return

    #If the first loop above has ended, what should we do?
    #  What does that mean in terms of the game?
    print(f"Game over! The word was {chosen_word}.")
    

'''
This is your main method, it gets run first!
TODO 3 TODO 4 TODO 5 are in the main method, as well as EXTRA CREDIT 2
'''
if __name__ == '__main__':
    #EXTRA CREDIT 2: Modify the main method so after a game ends, 
    #the code repeats, a new word is chosen, entry and instruction are printed again, the board is reset and the game is played again
    #this should repeat infinitely
    while(True):

        #You do not need to change the next three lines of code
        chosen_word = choice(word_list) #uses the choice function from random library to pick a word
        print(ENTRY)
        print(INSTRUCTION)

        #gives the chosen word to a helper function, that makes the game board
        #If the chosen word is "chosen" game_board should be ['_','_','_','_','_','_']
        game_board = create_board(chosen_word) #TODO 4    

        #TODO 5 Print the current board with the helper function (should be all _)
        #This lets the player know how many letters are in the word
        printer(game_board) 
    
        #TODO 3 we should call the play_game function with appropriate arguments
        play_game(game_board,chosen_word)
