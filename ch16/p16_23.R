library(DescTools)
library(tseries)

A <- c("N","N","N","N","Y","Y","N","Y","Y","N","Y","N","N","N","N")
A <- factor(A)
runs.test(A)
RunsTest(A)

# Table A.18 p. 762:
# (5, 10) and v=7 gives us 0.455. So P = 0.455 * 2
# The results from the table, the RunsTest and runs.test are all different. 
# No idea why yet. 
