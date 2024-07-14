Team = c(rep("A", 2), rep("B", 2), rep("C", 3))
Points = c(77, 81, 89, 83, 99, 92, 97)
Assists = c(19, 22, 29, 15, 32, 39, 14)
#Q1. Create  a dataframe....
playerStats = data.frame(Team, Points, Assists)

#Q2. Extract all rows for columns- Teams and Assists
playerStats[c("Team", "Assists")]

#Q3. Select all rows for columns 1 and 3
playerStats[c(1, 3)]

#Q5. Extract rows 1, 5, 7
playerStats[c(1, 5, 7),]

#Q6. Select rows whose points are greater than 90
condition1 = subset(playerStats, Points>90)
greaterThanNinety

#Q7. Select rows with points greater than 90 OR less than 80
condition2 = subset(playerStats, Points>90 | Points<80)
greaterThanNinety2

#Q8. Condition: Points are greater than 90 AND assists less than 30

condition3 = subset(playerStats, Points>90 & Assists<30)
condition3

#Q9. Condition: Points greater than 90 and only show Team column

condition4 = subset (playerStats["Team"], Points >90)
condition4

#Qn. Create a new column called as Qualifying, in which, Team A is qualified
#Qn+1. Create a new row which will have team as C, points as 98, assists 14, qualifying No

View(playerStats)
edit(playerStats)
quantile(Points)