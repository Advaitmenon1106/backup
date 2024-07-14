# Making DataFrame

A <- c(50, 60, 70, 80)
B <- c(45, 35, 70, 50)
C <- c(23, 29, 30, 45)
D <- c(30, 35, 40, 45)
studentData = data.frame(A, B, C, D)
row.names(studentData) = c("Physics", "Chemistry", "Maths", "Biology")
studentData

#Q1. Total marks obtained by students in chem and bio

chemTotal <- sum(studentData[2,1:4])
bioTotal <- sum(studentData[4, 1:4])
chemTotal
bioTotal

#Q2. Total marks by student A in all subjects

totalOfA <- sum(studentData[, 1])
totalOfA

#Q3. Highest marks scored in bio

highestMarkBio = max(studentData[4, ])
highestMarkBio

#Q4. Total marks by B and C

sum(sum(studentData[, 2], sum(studentData[, 3])))

#Q5. Top Score in chem

topChem = max(studentData["Chemistry", ])
topChem

#Q6. Min of D

minOfD = min(studentData[, "D"])
minOfD

typeof(studentData)

sort(LETTERS, decreasing = TRUE)