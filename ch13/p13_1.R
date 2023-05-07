library(dplyr)

data <- data.frame(
    machine = c(1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6),
    tensile = c(17.5,  16.9,  15.8,  18.6, 16.4,  19.2,  17.7,  15.4, 20.3,  15.7, 17.8, 
                18.9, 14.6, 16.7, 20.8, 18.9, 17.5, 19.2, 16.5, 20.5, 18.3, 16.2, 17.5, 
                20.1
    ))

anv <- aov(tensile ~ as.factor(machine), data = data)
summary(anv)
