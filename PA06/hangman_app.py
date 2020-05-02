"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
def generate_random_word():
    Words="school".split()
    # Words="angry hungry money school".split()
    return random.choice(Words)
# print(generate_random_word())

def get_word_so_far(word,guessed_letters):
    remains=[]
    for x in word:
        if x in guessed_letters:
            remains.append(x)
        else:
            remains.append('-')
    return ''.join(remains)

def print_word(word,guessed_letters):
    remains=[]
    for x in word:
        if x in guessed_letters:
            remains.append(x)
        else:
            remains.append('-')
    print(remains)
    print()

def play_hangman():
    want_to_play = True


    while (want_to_play):
        guessed_letters = []
        word=generate_random_word()
        print_word(word,guessed_letters)
        guesses_left = len(word)
        letter = input("please guess a letter") #asks user for a letter
#         while len(letter)!=1:
#             letter=input("please input correctly one letter!")
#         alphabet="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
        done = False
        while not done:
            if letter in guessed_letters:
                guesses_left-=1 #subtract one from guesses_left
                print("you've already guessed this letter")

            elif letter not in word:
                guessed_letters.append(letter) #add letter to guessed letters
                print('the letter is not in the word') #"tell user the letter is not in the word"
                guesses_left-=1 #"subtract one from the guesses_left"
            else:
                guessed_letters.append(letter) #"add letter to guessed letters"
                print('the letter is in the word') #"tell user the letter is in the word"

            print("you have",guesses_left,"guesses left")

            if len([x for x in word if x not in guessed_letters])==0:#"all the letters in the word have been guessed"
                done=True #"set done to be true and tell the user they won!"
                print('you win!')
            elif guesses_left==0:
                done=True
                print('you lost')#"set done to be true and tell the user they lost!"
            else:
                print_word(word,guessed_letters)
                letter = input("please guess a letter") #asks user for a letter
        want_to_play = input("do you want to play another game? y/n")
        if want_to_play=='y':
            want_to_play=True
        if want_to_play=='n':
            want_to_play=False


if __name__ == '__main__':
    play_hangman()
