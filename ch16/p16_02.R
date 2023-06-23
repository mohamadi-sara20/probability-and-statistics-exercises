library(BSDA)
library(stats)

time <- c(9, 12, 18, 14, 12, 14, 12, 10, 16, 11, 9, 11, 13, 11, 13, 15, 13, 14)
# H0 : median training is 12h
SIGN.test(time, md = 12)
binom.test(9, 15, p = 1/2)
