#ls()
# Dealing with missing values
# A common task in data analysis is dealing with missing values. In R, missing values are often represented by NA
# NA (Not available), NaN(Not a Number), inf (infinity), -inf (negative infinity) -> types of NA
x <- c(1:4, NaN, 6:7, NA)
x
is.na(x)
length(x)
#Creating a dataframe with missing values


df1 = data.frame(col1 = c(1:3, NA), col2 = c("this", NA, "is", "Text"), col3 = c(T, F, T, T), col4 = c(2.5, 4.2, 3.2, NA))
df1
is.na(df1)
col1NA = is.na(df1["col1"])
which(is.na(df1))
sum(is.na(df1))
colSums(is.na(df1))
a = na.omit(df$col4)
a
#df1$col1[is.na(df1$col1)] <- mean(df1$col1, na.rm = T)
df1
df1$col4[is.na(df1$col4)]<- median(df1$col4, na.rm = T)
df1$col1[is.na(df1$col1)]<- median(df1$col1, na.rm = T)
df1
str(df1)
summary(df1)
data1 = c(1:4)
matrix(data1, 2, 2, F)
#a = array(data1, c(2, 4, 2))
#a[, , 2]
