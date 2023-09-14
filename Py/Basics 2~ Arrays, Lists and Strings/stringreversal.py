word = input("Enter a word: ")

string = []
length = len(word)

for x in range (0, length):
    element = word[x]
    string.append(element)

print (string) 
reversed = []

for i in range (length, 0, -1):
    popped = string.pop(i-1)
    reversed.append(popped)

print (reversed)

blank = ""

for j in reversed:
    blank += j

print (blank)