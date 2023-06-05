library(dplyr)
time   <-  rep(c("0", "3", "7"), each = 12)
brand <-  c(
                c("Richfood", "SealedSweet", "MinuteMaid"),
                c("Richfood", "SealedSweet", "MinuteMaid"),
                c("Richfood", "SealedSweet", "MinuteMaid"),
                c("Richfood", "SealedSweet", "MinuteMaid")
            )
yield  <- c(
            #0
            52.6, 54.2, 49.8, 46.5,
            56, 48, 49.6, 48.4,
            52.5, 52, 51.8, 53.6,
            #3
            49.4, 49.2, 42.8, 53.2,
            48.8, 44, 44, 42.4, 
            48, 47, 48.2, 49.6, 
            #7
            42.7, 48.8, 40.4, 47.6, 
            49.2, 44, 42, 43.2, 
            48.5, 43.3, 45.2, 47.6
            
            
            )

data <- data.frame(time, brand, yield)

model <- aov(yield ~ time * brand, data = data)
summary(model)