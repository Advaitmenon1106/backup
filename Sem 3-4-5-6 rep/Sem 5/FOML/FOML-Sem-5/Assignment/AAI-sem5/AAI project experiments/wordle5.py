import itertools

# List of possible words to guess in Wordle
word_list = ["apple", "banana", "cherry", "date", "elder", "frank", "grape", "honey", "ivory", "jumps"]

# Create a class for Wordle knowledge
class WordleKnowledge:

    def __init__(self, words, word_length):
        self.words = words
        self.word_length = word_length

    def evaluate(self, guess):
        """
        Evaluate a guess and return whether it's consistent with the available words.
        """
        if len(guess) != self.word_length:
            raise ValueError("Invalid guess length")
        
        for word in self.words:
            if not self.is_consistent(guess, word):
                return False
        return True

    @staticmethod
    def is_consistent(guess, word):
        """
        Check if a guess is consistent with a target word.
        """
        for i in range(len(guess)):
            if guess[i] != word[i] and guess[i] in word:
                return False
        return True

def generate_possible_words(word_list, word_length):
    """
    Generate all possible words of a given length using the provided letters.
    """
    possible_words = ["".join(p) for p in itertools.permutations(word_list, word_length)]
    return possible_words

# Create a Wordle knowledge base
knowledge_base = WordleKnowledge(generate_possible_words("abcdefghijklmnopqrstuvwxyz", 5), 5)

# Example usage:
guess = "apple"  # Your guess
if knowledge_base.evaluate(guess):
    print(f"The guess '{guess}' is consistent with the Wordle knowledge.")
else:
    print(f"The guess '{guess}' is not consistent with the Wordle knowledge.")
