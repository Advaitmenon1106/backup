class House: #Blueprint
    walls = "White"
    flooring = "Wood"
    def openDoor(self): #Method
        print ("Door is opened")

house1 = House() #instance/object using blueprint
# house1.openDoor() - won't work without a self parameter in the method
# whenever an object calls its method, the object itself is passed as the first argument.
# therefore self is required

house1.openDoor() # roughly translates to = House.openDoor(house1)

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i
    def formComplex(self):
        print (self.real, end="")
        print (" +", self.imaginary, end="")
        print ("i")
    
n1 = Complex(2, 3)
finaln1 = n1.formComplex()

#Pynative 
#Q1.

class Vehicle:
    def __init__(self, max_speed, mileage):
        pass