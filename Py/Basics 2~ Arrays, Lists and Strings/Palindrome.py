word = input ("Enter a string: ")
length = int(len(word))

for x in (0,length/2):
    tail = word[length-x-1]
    if word[x] == tail:
        print ("palindrome")
        break
   
    print("not a palindrome")
    break