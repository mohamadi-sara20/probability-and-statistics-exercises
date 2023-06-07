library(dplyr)
library(ggplot2)

time   <-  c(5, 5, 5, 12, 12, 12, 18, 18, 18,
             5, 5, 5, 12, 12, 12, 18, 18, 18,
             5, 5, 5, 12, 12, 12, 18, 18, 18)
copper <-  c(1, 1, 1, 1, 1, 1, 1, 1, 1,
             2, 2, 2,  2, 2, 2, 2, 2, 2,
             3, 3, 3, 3, 3, 3, 3, 3, 3)

yield  <- c(0.30, 0.34, 0.32, 0.37, 0.36, 0.35, 0.25, 0.23, 0.24,
            0.24, 0.30, 0.27, 0.23, 0.32, 0.25, 0.22, 0.31, 0.25,
            0.20, 0.30, 0.27, 0.28, 0.31, 0.29, 0.24, 0.30, 0.25)

data <- data.frame(time, copper, yield)
first_model <- lm(yield ~ time * copper, data = data)
summary(first_model)


second_model <- lm(yield ~ time + copper + time:copper + I(copper^2) 
+ I(time^2), data = data)
summary(second_model)
