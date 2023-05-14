library(DescTools)

data <- data.frame(
    angle = c(67, 67, 
    71, 71, 71, 71, 71, 71, 
    75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 
    79, 79, 79, 79, 
    83, 83
    ),
    y = c(83, 85,
            84, 85, 85, 86, 86, 87,
            86, 87, 88, 88, 88, 90, 87, 87, 88, 88, 89, 
            89, 90, 90, 91,
            90, 92))

data$angle <- as.factor(data$angle)
model <- aov(y ~ angle, data = data)
summary(model)
