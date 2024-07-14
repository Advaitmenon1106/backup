import random
from english_words import get_english_words_set

class HangmanAI:
    def __init__(self, len_of_words):
        self.word_list = list(get_english_words_set(['web2'], lower=False))
        self.word_list = [word for word in self.word_list if len(word) == len_of_words]
        self.guesses = []
        self.word_to_guess = random.choice(self.word_list)
        self.remaining_attempts = 8

        self.letter_probs = dict()
        for i in range(97, 97+26):
            self.letter_probs[chr(i)] = 0
        
        for word in self.word_list:
            for key in self.letter_probs:
                self.letter_probs[key]+=word.count(key)
        
        sum_letters = sum(self.letter_probs.values())
        for key in self.letter_probs:
            self.letter_probs[key] = self.letter_probs[key]/sum_letters

    def make_guess(self):
        guess = max(self.letter_probs, key=self.letter_probs.get)
        self.letter_probs.pop(guess)
        return guess
    
    def update_guesses(self, guess):
        self.guesses.append(guess)
    
    def display_word(self):
        revealed_word = ''
        for letter in self.word_to_guess:
            if letter in self.guesses:
                revealed_word += letter
            else:
                revealed_word += '_'
        return revealed_word
    
    def play_game(self):
        print("Welcome to Hangman!")
        while self.remaining_attempts > 0:
            print("Word to guess:", self.display_word())
            print("Remaining attempts:", self.remaining_attempts)
            guess = self.make_guess()
            print("AI's guess:", guess)
            self.update_guesses(guess)
            if all(letter in self.guesses for letter in self.word_to_guess):
                print("Congratulations, you guessed the word:", self.word_to_guess)
                break
            else:
                if guess in self.word_to_guess:
                    print("Correct guess!")
                else:
                    print("Incorrect guess.")
                    self.remaining_attempts -= 1
        else:
            print("You ran out of attempts. The word was:", self.word_to_guess)


games = 0
while(games!=10):
    print('Game', games+1, end='\n')
    hangman_ai = HangmanAI(5)
    hangman_ai.play_game()
    print('\n')
    games+=1