library(BSDA)
library(stats)

time <- c(9, 12, 18, 14, 12, 14, 12, 10, 16, 11, 9, 11, 13, 11, 13, 15, 13, 14)
# H0 : median waiting time is not more than 20 minutes
SIGN.test(time, md = 12)

binom.test(time, p = 1/2)
