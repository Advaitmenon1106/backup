import random as rand
import numpy as np
message = input("Enter a message: ")
preCiphertext = []
for x in message:
    preCiphertext.append(bin(ord(x)))

print (preCiphertext)

def xorFunction(x,y):
    xor = 5
    if x == 0 and y == 0:
        xor = 0
    elif x == 1 and y == 0:
        xor = 1
    elif x == 0 and y == 1:
        xor = 1
    elif x == 1 and y == 1:
        xor = 0
    return xor

keyInteger = rand.randint(10,99)
key = bin(keyInteger)
print (key)
length = len(preCiphertext)
ciphertext = []
for i in range (0, length):
    ciphert = preCiphertext[i]^key
    ciphertext.append (bin((ciphert)))

print (ciphertext)