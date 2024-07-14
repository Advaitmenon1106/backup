import numpy as np
import pandas as pd

df = pd.read_csv("Automobile_data.csv")
print (df)
print (df.isna().sum())

#Q11. Remove all NA values
meanWheelBase = df['wheel-base'].mean()
df['wheel-base'].fillna(meanWheelBase, inplace=True)
meanHorsepower = df['horsepower'].mean()
df['horsepower'].fillna(meanHorsepower, inplace=True)
meanPrice = df['price'].mean()
df['price'].fillna(meanPrice, inplace=True)
print (df.isna().sum()) #NA values are filled with mean

print ("")

#Q2 Done (cleared na values)
#Q3. Most expensive car company name

maxprice = df['price'].max()
print (maxprice)


#Q4

df.set_index('company', inplace= True)
print (df)

print(df.loc['toyota'])

print ('')

#Q5
print ("Count:-")
print ("")
df.value_counts()

#Q7


#Q8

print (df.sort_values('price'))

#Q9

GermanCars = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]})
print (GermanCars)

print ("")

japaneseCars = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]})
print (GermanCars)

allCars = GermanCars.append(japaneseCars, ignore_index=True)
print (allCars)
print ("")

#Q10

Car_Price = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]})
car_Horsepower = pd.DataFrame({'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]})

allCars2 = Car_Price.merge(car_Horsepower)
print (allCars2)