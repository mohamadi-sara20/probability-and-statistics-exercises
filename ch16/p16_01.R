library(BSDA)

time <- c(17, 15, 20, 20, 32, 28, 12, 26, 25, 25, 35, 24)
# H0 : median waiting time is not more than 20 minutes
t <- SIGN.test(time, md = 20, alternative = "greater")
