library(DescTools)
analyst   <-  c(  c("1", "2", "3", "4", "5"),
                    c("1", "2", "3", "4", "5"),
                    c("1", "2", "3", "4", "5"))

conds <-  rep(c("A", "B", "C"), each = 5)
yield  <- c(3.8, 1.6, 2.7, 1.7, 2,
            2.7, 5.2, 2.8, 1.9, 4.8,
            3.6, 7.5, 6.4, 2.6, 8.1
            )

data <- data.frame(analyst, conds, yield)
data$analyst <- as.factor(data$analyst)

model <- aov(yield ~ analyst + conds, data = data)
summary(model)
