d = {1: 0, 2: 100, 3: 50, 4: 150}
print (d)
print (d[1])
d[1]+=1
print (d)
d[5] = 100
if 100 in d:
    print ("Yes")
elif 100 in d:
    print ("Yes2")
else:
    print ("no")
print (len(d))

print (d)
for x in d:
    print (x-1)

print (d)
key = [1, 2, 3, 4]
print (d[key[3]])