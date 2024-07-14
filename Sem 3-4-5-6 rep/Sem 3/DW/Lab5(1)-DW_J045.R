Sr.No <- c(seq(1, 5, 1))
Roll.NO <- c(paste0("J00", seq(1, 5, 1)))
Sap.ID <- c(paste0("700100", seq(1, 5, 1)))
Student.Name = c("A", "B", "C", "D", "E")
Attendance = c(T, T, T, F, F)
Branch <- rep("Data Science", 5)

student_data = data.frame(Sr.No, Roll.NO, Sap.ID, Student.Name, Attendance, Branch)
dataset
# Every data frame has different datatypes but each column must have the same data type
# Columns must have same amount of data to prevent circular input

str(student_data) #Shows the nature of data stored in each column
summary(student_data)
head(student_data) #top 5 obs
tail(student_data) #bottom 5 obs
head(student_data, 2)
student_data$Roll.NO
student_data[1,1]
student_data[1,]
student_data[1]
length(student_data)
student_data