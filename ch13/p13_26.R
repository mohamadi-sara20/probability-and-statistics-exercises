library(DescTools)
locations   <-  c(  c("1", "2", "3", "4"),
                    c("1", "2", "3", "4"),
                    c("1", "2", "3", "4"))

conds <-  rep(c("A", "B", "C"), each = 4)
yield   <- c(18, 20, 14, 11,
            13,23,12,17,
            12, 21, 9, 10
            )

data <- data.frame(locations, conds, yield)
data$locations = as.factor(data$locations)

model <- aov(yield ~ locations + conds, data = data)
summary(model)
