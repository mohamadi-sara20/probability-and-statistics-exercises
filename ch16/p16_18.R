library(stats)

A <- c(10.4, 9.8, 11.5, 10.0, 9.9,9.6, 10.9, 11.8, 9.3, 10.7)
B <- c(8.7, 11.2, 9.8, 10.1, 10.8, 9.5, 11.0, 9.8, 10.5, 9.9)
wilcox.test(A, B, alternative='two.sided', exact=FALSE)
