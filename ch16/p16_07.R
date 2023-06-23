library(BSDA)

before <- c(158, 149, 160, 155, 164, 138, 163, 159, 165, 145, 150, 161, 132, 155, 146, 159)
after <- c(164, 158, 163, 160, 172, 147, 167, 169, 173, 147, 156, 164, 133, 161, 154, 170)
d_o <- mapply("-", after, before, SIMPLIFY = TRUE)


# H0: d0 = 8
# H1: d < 8

SIGN.test(d_o, md = 8, alternative = "less")
