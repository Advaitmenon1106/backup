import random
from english_words import get_english_words_set
from easy_logic import *

words = list(get_english_words_set(['web2'], lower=False))
words = [word for word in words if len(word) == 5]

letters = [chr(i) for i in range (97, 97+26)]
symbol_letters = [Symbol(letter) for letter in letters]

pos = [str(i) for i in range (0, 5)]
pos_symbols = [Symbol(p) for p in pos]

class WordleAI:
    def __init__(self):
        self.guesses = []
        self.evals = {}
        self.knowledge = And()

    def eval_a_guess(self, answer, guess):
        self.guesses.append(guess)
        evaluation = ''
        for i in range (0, len(answer)):
            if answer[i] == guess[i]:
                evaluation+='G'
            elif guess[i] in answer and guess[i]!= answer[i]:
                evaluation+='Y'
            else:
                evaluation+='R'
        self.evals[guess] = evaluation
    
    def interpret(self, eval): #parameter is the colour coding, eg. RYGRY
        for i in range (0, len(eval)):
            pass

    def make_a_guess(self, counter):
        if counter == 0:
            return words[random.randint(0, len(words)-1)]
        else:
            pass
