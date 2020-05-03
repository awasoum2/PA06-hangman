"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
         'word':'interesting',
		 'word_so_far':'-----',
         'guesses_left':10,
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
    return render_template('hangman.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/start')
def start():
    global state
    state['word']=hangman_app.generate_random_word()
    state['guesses'] = []
    word_so_far=hangman_app.get_word_so_far(state['word'],state['guesses'])
    state['word_so_far']=word_so_far
    state['guesses_left']=len(state['word'])
    return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
    """ plays hangman game """
    global state

    if request.method == 'GET':
    	return play()

    elif request.method == 'POST':
        # guesses_left=len(state['word'])
        letter = request.form['guess']
        if letter in state['guesses']:#check if letter has already been guessed
            state['guesses_left']-=1
            print("you've already guessed it")# and generate a response to guess again
        elif letter not in state['word']:# else check if letter is in word
            print("the letter is not in the word")
            state['guesses'] += [letter]
            state['guesses_left']-=1
        else:
            print("the letter is in the word")
            state['guesses'] += [letter]

        # state['guesses_left']

        if len([x for x in state['word'] if x not in state['guesses']])==0:#"all the letters in the word have been guessed"
            state['done']=True #"set done to be true and tell the user they won!"
            print('you win!')

        elif state['guesses_left']==0:
            state['done']=True
            print('you lost')#"set done to be true and tell the user they lost!"
        else:
            # print_word(word,guessed_letters)
            word_so_far=hangman_app.get_word_so_far(state['word'],state['guesses'])
            state['word_so_far']=word_so_far
            letter = request.form['guess']
        # then see if the word is complete
        # if letter not in word, then tell them
        # state['guesses']+=[letter]
        return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
