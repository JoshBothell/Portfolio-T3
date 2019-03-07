#Josh Bothell
#Modular HANGMAN Game
#12/18
#Classic Hangman
#Computer makes random word and player guesses with limited tries
import random
import data

#initialsize variables and define constants.
MAX_WRONG = len(data.HANGMAN) - 1
WORDS = ("FLOAT", "STRING", "LIST", "BOOLEAN", "VARIABLE", "COMMENTS", "FUNCTION", "PARAMETER", "CONSTANT", "LOOP", "INTEGER") #word bank to be drawn from
word = random.choice(WORDS)
so_far = "-" * len(word) #underscores for unguessed letters
wrong = 0 #number of wrong guesses
used = [] #letters already guesed

def guess_input(used):
    guess = input("Enter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    used.append(guess)
    return guess, used

def in_word(guess, word, so_far, wrong):
    if guess in word:
        print("Yes!", guess, "is in the word!")
        new = ""

        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
        return so_far, wrong
    else:
        print("Sorry,", guess, "isn't in the word.")
        wrong += 1
        return so_far, wrong
        
def endgame(wrong, MAX_WRONG):
    if wrong == MAX_WRONG:
        print(data.HANGMAN[wrong])
        print("You've been hanged!")
    else:
        print("You guessed it!")

def main(MAX_WRONG, word, so_far, wrong, used):
    while wrong < MAX_WRONG and so_far != word:
        print(data.HANGMAN[wrong])
        print("You have used the following letters:", used)
        print("So far, the word is: ", so_far)
        guess, used = guess_input(used)
        so_far, wrong = in_word(guess, word, so_far, wrong)
    endgame(wrong, MAX_WRONG)
    print("The word was", word)
    input("Press the enter key to exit.")
        
main(MAX_WRONG, word, so_far, wrong, used)
