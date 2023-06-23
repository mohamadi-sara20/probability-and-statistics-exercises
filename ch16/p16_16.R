library(stats)

t2 <- c(2.1, 5.3, 1.9, 0.5)
t1 <- c(1.4, 4.6, 0.9, 2.8, 3.1)
# kruskal.test(list(t1, t2))
wilcox.test(t2, t1, alternative='g')