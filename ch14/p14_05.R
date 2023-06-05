library(dplyr)
library(agricolae)
library(DescTools)
muscle   <-  rep(c("1", "2", "3", "4", "5"), each = 3)
subject <-  c(
                c("1", "2", "3"),
                c("1", "2", "3"),
                c("1", "2", "3"),
                c("1", "2", "3"),
                c("1", "2", "3")
            )


yield  <- c(32, 63, 43,
            5, 10, 41,
            58, 64, 26,
            10, 45, 63,
            19, 43, 61,


            59, 60, 54,
            1.5, 9, 43,
            61, 78, 29,
            10, 61, 46,
            20, 61, 85,




            38, 50, 47,
            2, 7, 42,
            66, 78, 23,
            14, 71, 55,
            23, 42, 95
            )


data <- data.frame(subject, muscle, yield)

print(data)

model <- aov(yield ~ muscle * subject, data = data)
summary(model)
