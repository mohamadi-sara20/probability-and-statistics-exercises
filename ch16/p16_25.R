library(randtests)
library(DescTools)

A <- c(5.5, 5.6, 6.3, 4.6, 5.3, 5.0, 6.2, 5.8, 5.1)
B <- c(3.8, 4.8, 4.3, 4.2, 4.0, 4.9, 4.5, 5.2, 4.5)
d_o <- mapply("-", A, B, SIMPLIFY = TRUE)

# [('B', 3.8), ('B', 4.0), ('B', 4.2), ('B', 4.3), ('B', 4.5), ('B', 4.5), ('A', 4.6), ('B', 4.8), ('B', 4.9), ('A', 5.0), ('A', 5.1), ('B', 5.2), ('A', 5.3), ('A', 5.5), ('A', 5.6), ('A', 5.8), ('A', 6.2), ('A', 6.3)]
# ['B', 'B', 'B', 'B', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'A', 'A', 'A', 'A', 'A', 'A']
# B B B B B B A B B A A B A A A A A A
# n1=n2=9, v=6 --> 0.044
# Obviously, this time it is not two-sided, since H1: MA>MB
# ==============================================================================

# Probably two-sided results
RunsTest(d_o)
# ==============================================================================
runs.test(d_o)
# This is odd. It says n1=n2=4. Where did that come from? No idea yet.
