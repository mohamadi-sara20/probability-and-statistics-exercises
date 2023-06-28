library(DescTools)

midterm <- c(84, 98, 91, 72,86, 93, 80, 0, 92, 87)
final <- c(73, 63, 87, 66, 78, 78, 91, 0, 88, 77)
cor.test(x = midterm, y = final, method = "spearman", exact = FALSE)
