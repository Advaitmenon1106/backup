v1 = c(1:12)
m1 = matrix(v1, nrow= 3, ncol= 4, byrow= TRUE)
m1
v2 = c(13:24)
m2 = matrix(v2, nrow= 3, ncol= 4, byrow= TRUE)
m2
#Arrays can nbe of n dimensions. 
#Recall : Matrix = special case of arrays (2 dimensional arrays, to be specific)
#syntax : A = arr(<data (could be vector or a matrix)> , dimension )
Mfinal1 = array(c(m1, m2), dim= c(3, 4, 0)) #No matrix created
Mfinal1
#Two dimensional array but not all elements are accommodated (only first 12 taken into consideration) 
# {dim= (3,4) same as dim= c(3, 4, 1)}
Mfinal = array(c(m1, m2), dim= c(3, 4))
Mfinal
#Three dimensional array
TwoDim = array(c(m1, m2), dim= c(3, 4, 2))
TwoDim

-------------------------------------#Lab 5 ends here-------------------------------------------------------------
TwoDim2 = array(c(m1, m2), dim= c(3, 4, 2), dimnames = list(c("Year1", "Year2", "Year3"))) 
TwoDim2