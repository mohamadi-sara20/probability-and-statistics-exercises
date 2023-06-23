library(BSDA)

before <- c(60, 54.9, 58.1, 62.1, 58.5, 59.9, 54.4, 60.2, 62.3, 58.7)
after <- c(58.5, 60.3, 61.7, 69.0, 64.0, 62.6, 56.7, 63.6, 68.2, 59.4)
d_o <- mapply("-", after, before, SIMPLIFY = TRUE)
d_o

# H0: d0 = 4.5
# H1: d < 4.5

SIGN.test(d_o, md = 4.5, alternative = "less")
