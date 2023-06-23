library(stats)

A <- c(5.5, 5.6, 6.3, 4.6, 5.3, 5.0, 6.2, 5.8, 5.1)
B <- c(3.8, 4.8, 4.3, 4.2, 4.0, 4.9, 4.5, 5.2, 4.5)
# kruskal.test(list(A, B))
wilcox.test(A, B, alternative='g', exact=FALSE)