# Making DataFrame

A <- c(50, 60, 70, 80)
B <- c(45, 35, 70, 50)
C <- c(23, 29, 30, 45)
D <- c(30, 35, 40, 45)
studentData = data.frame(A, B, C, D)
row.names(studentData) = c("Physics", "Chemistry", "Maths", "Biology")
studentData

#apply()

apply(studentData, 1, sum)
apply(studentData, 2, mean)

#lapply()

lapply(studentData, mean)
lapply(studentData, function(studentData) data*2)

f = c('k', 'k', 'none', 'n', 'p', 'p', 'n', 'n', 'none', 'p', 'k', 'none')
factor1 = factor(f)
growth = c(10, 12, 8, 13, 18, 19, 11, 11, 9, 21, 10, 10)
factorGrowth = factor(growth)

factor1
factorGrowth

names(growth) = f
mean(growth['k'])
mean(growth['n'])
mean(growth['p'])
mean(growth['none'])