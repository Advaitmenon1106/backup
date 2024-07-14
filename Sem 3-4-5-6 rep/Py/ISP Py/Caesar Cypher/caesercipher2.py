import random as ra

n = ra.randint(1,26)
word = input ("Enter a string: ")
cipher = ""

for x in word:
    a = ord(x)
    a+=2 
    cipher+= chr(a)

print (cipher)