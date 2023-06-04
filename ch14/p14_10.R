library(dplyr)
library(agricolae)
library(DescTools)
library(lme4)

dose   <-  c(   c("1", "1", "1"), 
                c("2", "2", "2")
                )

position <-  c( 
            c("1", "2", "3"),
            c("1", "2", "3")
            )


yield  <- c(c(15.5, 14.8, 21.3),
            c(27.2, 24.9, 26.1)
            )


data <- data.frame(dose, position, yield)
model <- aov(yield ~ dose + position, data = data)
summary(model)