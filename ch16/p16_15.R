library(stats)

A <- c(1, 12, 9, 13, 11, 14)
B <- c(8, 10, 7)
# kruskal.test(list(A, B))
wilcox.test(A, B, alternative='g')