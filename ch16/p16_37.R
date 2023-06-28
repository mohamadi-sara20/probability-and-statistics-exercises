library(DescTools)

judge1 <- c(5, 8, 4, 3, 6, 2, 7, 1)
judge2 <- c(7, 5, 4, 2, 8, 1, 6, 3)
cor <- cor.test(x = judge1, y = judge2, method = "spearman", exact = FALSE)
cor