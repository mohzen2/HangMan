import random
import string
from hangmanwords import hangmanwords
from HangmanPictures import lives_visual

def GetValidWord(hangmanwords):
    word = random.choice(hangmanwords)
    while '-' in word or ' ' in word:
        word = random.choice(hangmanwords)

    return word.upper()

def hangman():
    word = GetValidWord(hangmanwords)
    word_letters = set(word) # Letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # What the user has guessed so far

    lives = 7

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # Letters used by the player
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print('You have', lives, 'lives left and already have used these letters:', ' '.join(used_letters))

        # what the current word is (W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual[lives])
        print('Current word: ', ''.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1 # subtrats a life from the player count
                print(f'\n Your letter {user_letter} is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that character. Please pick another.')
        else:
            print('\nInvalid character, please try again.')

    # This while loop is closed when len(word_letters) == 0

    if lives == 0:
        print(lives_visual[lives])
        print("Sorry you died. The correct word was,", word,"." )
    else:
        print("Congradulations! You guessed the word,", word,", correctly." )
    


hangman()