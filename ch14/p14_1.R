library(dplyr)
temp   <-  rep(c("O1", "O2", "O3", "O4"), each = 6)
oven <-  c(
                c("500", "550", "600"),
                c("500", "550", "600"),
                c("500", "550", "600"),
                c("500", "550", "600")
            )
yield  <- c(
            #O2
            227, 187, 174, 
            221, 208, 202, 
            #O2
            214, 181, 198, 
            259, 179, 194, 
            #O3
            225, 232, 178,
            236, 198, 213,
            #O4
            260, 246, 206,
            229, 273, 219
            )

data <- data.frame(oven, temp, yield)

model <- aov(yield ~ oven * temp, data = data)
summary(model)