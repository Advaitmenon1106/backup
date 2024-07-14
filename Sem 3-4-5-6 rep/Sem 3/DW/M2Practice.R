library(tidyr)
Team = c(rep("A", 2), rep("B", 2), rep("C", 3))
Points = c(77, 81, 89, 83, 99, 92, 97)
Assists = c(19, 22, 29, 15, 32, 39, 14)
#Q1. Create  a dataframe....
playerStats = data.frame(Team, Points, Assists)
playerStats
spread(playerStats, Team, Assists)
player = c('Kohli', 'Kohli', 'Kohli', 'Kohli', 'Rohit', 'Rohit', 'Rohit', 'Rohit')
year = c(1, 1, 2, 2, 1, 1, 2, 2)
action = rep(c('Bat', 'Bowl'), 4)
outcome = c(900, 20, 500, 10, 450, 15, 300, 10)
df = data.frame(player, year, action, outcome)
df
spread(df, action, outcome)
list1 = list(1, 2, 3, 4, 5, "hello")
list1
m1 = matrix(player, year)
m1