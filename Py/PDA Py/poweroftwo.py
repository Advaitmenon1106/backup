num = int (input ("Enter a value: "))

def powerOfTwo(num):
    
    while(num>1):
        num = num/2
    if(num==1):
        return True
    else:
        return False

p = powerOfTwo(num)
print(p)