from easy_logic import Symbol, model_check

class WordleGuess:
    def __init__(self, word, feedback):
        self.word = word
        self.feedback = feedback

class WordleSolver:
    def __init__(self, word_list):
        self.word_list = word_list
        self.guesses = []

    def make_guess(self):
        pass
        # Implement your logic for generating guesses
        # You can use the logic code to evaluate the guesses and determine validity
        # Return a WordleGuess object with the guessed word and feedback

    def play_game(self, max_guesses):
        for _ in range(max_guesses):
            guess = self.make_guess()
            self.guesses.append(guess)
            if guess.feedback == "Correct":
                print(f"Solver guessed the correct word in {len(self.guesses)} guesses: {guess.word}")
                break
        else:
            print("Solver ran out of guesses.")

if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry", "grape", "lemon", "orange", "kiwi"]
    solver = WordleSolver(word_list)
    solver.play_game(max_guesses=10)
