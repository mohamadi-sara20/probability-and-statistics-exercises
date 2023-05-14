library(DescTools)

control <- c(6.8, 7.3, 6.3, 6.9, 7.1)
one <- c(8.2, 8.7, 9.4, 9.2, 8.6)
two <- c(7.7, 8.4, 8.6, 8.1, 8)
three <- c(6.9, 5.8, 7.2, 6.8, 7.4)
four <- c(5.9, 6.1, 6.9, 5.7, 6.1)

x <- c(control, one, two, three, four)
vec <- c("control","1","2", "3", "4")
g <- rep(vec, each = 5)
DunnettTest(x, g, control="control")

