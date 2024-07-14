import numpy as np
import english_words as eng
wordlist = eng.get_english_words_set(sources=['web2'], lower=True)
a = np.array(list(wordlist), dtype=str)
print (type(a))
guess_index = np.random.randint(0, len(wordlist)-1)
word = a[guess_index]
print (word)
arrayBlank = np.empty(len(word), dtype=str)
for i in range (0, len(word)):
    arrayBlank[i] = "_"
def fill(g):
    for j in range (0, len(word)):
        if g == list(word)[j]:
            arrayBlank[j] = g    
hangman = ["  |\n", "  O\n", " -", "  |",  "  -\n", " /", "    \\"]
chances = 1
while (chances<7):
    if "_" not in arrayBlank:
        print("Word is complete. Word: ", ''.join(arrayBlank))
        break
    guess = input ("Enter your guess: ")
    if list(guess) == list(word):
        print ("Correct")
        break
    elif guess in list(word):
        fill(guess)
        print (arrayBlank)
    else:
        print ("You have ", 6-chances, " chances left")
        chances+=1