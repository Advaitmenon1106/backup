word = input ("Enter a string: ")
cipher = ""

for x in word:
    a = ord(x)
    if a == 32:
        cipher+= chr(32)
    else:
        a+=2
        cipher+= chr(a)

print (cipher)