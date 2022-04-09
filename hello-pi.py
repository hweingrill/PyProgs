print ("hello world")
#hangman_Program
import random 

words = ['chicken', 'dog', 'cat', 'mouse', 'frog']
live_remaing = 14

def pick_a_word():
    word_position = random.randint(0, len(words) - 1)
    return words [word_position]

def process_guess(guess, word):
    global lives_remaining
    lives_remaining = 14
    lives_remaining = lives_remaining - 1
    return False

def play():
    word = pick_a_word()
    while True:
            guess = get_guess(word)
            lives_remaining = 14
            if process_guess(guess, word):
                print ('You win!')
                break
            if lives_remaining == 0:
                print ('You are Hung!')
                print('The word was: ' + word)
                break

def print_word_with_blanks(word):
    print('print_word_with_blanks:not done yet')
    
def get_guess(word):
    print_word_with_blanks(word)
    print ('Lives remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or the whole word?')
    return guess
