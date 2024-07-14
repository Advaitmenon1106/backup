# 1. While a vector is a (long) sequence of values, a matrix is a two dimensional 
# rectangular object with values



# 2. An array is a multi-dimensional extensions of a vector.
# In the special case that the array has only two dimensions, this array is also called a matrix.


#Ex1. Making a matrix
# matrix(elements, no of rows, no of columns, by row or by column)

m1 = matrix(1:10)
m2 = matrix (1:10, 2)
m2
m3 = matrix (1:10, 2, byrow = TRUE)
m3

data = c(1, 2, 100, 55, 7, 24, 23)

m4 = matrix (data, 2)
m4

m5 = matrix (data, 2, byrow = TRUE)
m5

m6 = matrix (data, 3)
m6 #circular input observed

dim(m6)
dim(m5)
nrow (m5)
ncol(m5)

v1 = c(1, 2, 3, 4, 5)
v2 = c(6, 7, 8)
cbind (v1, v2) # circular output observed in the vector with lesser elements
rbind (v1, v2)

m7 = c(2, 3, 4, 5, 6, 7)
dim(m7) = c(2, 3)
m7 # Product of rows and columns has to be perfectly equal to the total number of data

colnames (m7) = c("C1", "C2", "C3")
m7

rownames (m7) = c(paste0("R", 1:2))
m7

m7[1, 2]
m7[1, ]