s = read.csv("C:/Users/Kavita manoj/OneDrive/Desktop/data.csv")
s
class(s)
View(s)
price = s["Last.Traded.Price"]
symbols = s["Symbol"]
symbols1 = unlist(symbols)
price
max(price)
min(price)
max(s$Traded.Volume.lacs.) #on searching the max value obtained, in the csv file, we can find corresponding Symbol ~ NIFTY50
maxVol = which.max(s$Traded.Volume.lacs)
s[maxVol, ] # ---> gives all details about max of traded volume in lakhs
#turnover = volumes/average volume (for this question, dplyr is required/searching on excel is required)
minChange = which.min(s$X365.Days...Change)
s[minChange, ] #minimum change in 365 days

#Advantages of data warehousing:-

# Helps make better decisions after analysing the data in the repositories
# Historical Data can be viewed
# Data consistency and accuracy is maintained
# Saves time taken to analyse data
# Optimised speed of data analysis