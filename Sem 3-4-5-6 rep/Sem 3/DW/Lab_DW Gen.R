Player = c(rep("Kohli", 4), rep("Rohit", 4))
Year = c(1, 1, 2, 2, 1, 1, 2, 2)
Action = rep(c("Batting", "Bowling"), 4)
Action
Outcome <- c(900, 20, 500, 10, 450, 15, 300, 10)
playerData = data.frame(Player, Year, Action, Outcome)
playerData

library(tidyr)
spread(playerData, Action, Outcome)
#Spread function : spread(data, key, value)
#key : column whose value will become variable name
#values: column where values will fill under new variable created from the key