library(DescTools)
block   <-  c(c("1", "2", "3"),c("1", "2", "3"),c("1", "2", "3"),c("1", "2", "3") )
fertilizers <-  rep(c("f1", "f2", "f3", "f4"), each = 3)
yield   <- c(42.7, 50, 51.9, 
            39.3, 38, 46.3, 
            48.5, 50.9, 53.5, 
            32.8, 40.2, 51.1)

data <- data.frame(block, fertilizers, yield)
data$block = as.factor(data$block)

print(data)


model <- aov(yield ~ block + fertilizers, data = data)
summary(model)
