library(DescTools)

data <- data.frame(
    temp = c(0, 0, 0, 0, 0, 0,
    25,  25,  25,  25,  25,  25, 
    50, 50, 50, 50, 50, 50, 
    75, 75, 75, 75, 75, 75, 
    100, 100, 100, 100, 100, 100
    ),
    y = c(55, 55, 57, 54, 54, 56,
60, 61, 60, 60, 60, 60,
70, 72, 72, 68, 77, 77,
72, 72, 72, 70, 68, 69,
65, 66, 60, 64, 65, 65))

data$temp <- as.factor(data$temp)
model <- aov(y ~ temp, data = data)
summary(model)
TukeyHSD(model, which = 'temp') 