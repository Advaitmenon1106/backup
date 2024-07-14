import random
from english_words import get_english_words_set
from easy_logic import *

words = list(get_english_words_set(['web2'], lower=False))
words = [word for word in words if len(word) == 5]

def word_to_logic(word):
    logic_expression = And([Symbol(letter) for letter in word])
    return logic_expression


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
    
    def interpret(self, evaluation):
        interpretations = []

        for i in range(5):
            if evaluation[i] == 'G':
                interpretations.append(symbol_letters[i])  # Letter is in the correct position.
            elif evaluation[i] == 'Y':
    
                wrong_position = Or([And([symbol_letters[j], Not(pos_symbols[i])]) for j in range(5) if j != i])
                interpretations.append(wrong_position)
            elif evaluation[i] == 'R':
                # You need to define the logic for a letter not being in the word.
                # For example, you can create a NOT condition for the specific position.
                not_in_word = Not(And([symbol_letters[i], pos_symbols[i]]))
                interpretations.append(not_in_word)

        # Combine all interpretations for each position using AND to get the final interpretation.
        final_interpretation = And(interpretations)
        self.knowledge.add(final_interpretation)

    def make_a_guess(self, counter):
        if counter == 0:
            # First guess: Choose a random word from the initial list
            return words[random.randint(0, len(words) - 1)]
        else:
            # Subsequent guesses:
            # Generate a list of candidate words based on existing knowledge
            candidate_words = [word for word in words if self.knowledge.evaluate(word_to_logic(word))]

            # Prioritize words based on some strategy (e.g., information gain)
            # You can implement a strategy to select the next word to guess here.

            # For simplicity, you can choose the first candidate word in this example.
            if candidate_words:
                return candidate_words[0]
            else:
                # If there are no candidate words, you can handle this case differently (e.g., raise an exception).
                # This could occur if the knowledge contradicts all remaining words.
                raise Exception("No valid candidate words found based on current knowledge.")


target_word = random.choice(words)
max_guesses = 10

wordle_ai = WordleAI()

num_guesses = 0
while num_guesses < max_guesses:
    # AI makes a guess
    guess = wordle_ai.make_a_guess(num_guesses)

    # Generate feedback based on the guess and the target word
    feedback = wordle_ai.eval_a_guess(target_word, guess)

    # Update AI's knowledge based on feedback
    wordle_ai.eval_a_guess(target_word, guess)
    wordle_ai.interpret(feedback)

    # Display the AI's guess, feedback, and game state
    print(f"Guess {num_guesses + 1}: {guess}, Feedback: {feedback}")

    # Check if the AI has guessed the word correctly
    if feedback == "GGGGG":
        print("AI wins! It correctly guessed the word:", target_word)
        break

    num_guesses += 1

# Check if the AI ran out of guesses without guessing the word
if num_guesses >= max_guesses:
    print("AI ran out of guesses. The target word was:", target_word)
