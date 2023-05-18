library(DescTools)
blocks   <-  c(c("1", "2", "3", "4", "5"),
                    c("1", "2", "3", "4", "5"),
                    c("1", "2", "3", "4", "5"), 
                    c("1", "2", "3", "4", "5"))

conds <-  rep(c("1", "2", "3", "4"), each = 5)


yield  <- c(12.8, 10.6, 11.7, 10.7, 11, 
            11.7, 14.2, 11.8, 9.9, 13.8, 
            11.5, 14.7, 13.6, 10.7, 15.9, 
            12.6, 16.5, 15.4, 9.6, 17.1
            )
data <- data.frame(blocks, conds, yield)
data$conds = as.factor(data$conds)
data$blocks = as.factor(data$blocks)

model <- aov(yield ~ conds + blocks, data = data)
summary(model)

# Finding  (S1-S) / n also shows the variance differs from zero, 
# hence approving anvoa results. 