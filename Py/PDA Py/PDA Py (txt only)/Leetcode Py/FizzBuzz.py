List = []
n = int(input())
for x in range (1, n+1):
            if x%3 == 0 and x%5 == 0:
                List.append ("FizzBuzz")
            elif x%3 == 0:
                List.append ("Fizz")
            elif x%5 == 0:
                List.append ("Fizz")
            else:
                List.append (str(x))

print (List)