library(DescTools)

data <- data.frame(
    sampling_method = c("D", "D", "D", "D", 
    "M", "M", "M", "M",
    "S", "S", "S", "S", 
    "SRK", "SRK", "SRK", "SRK", 
    "K", "K", "K", "K"),
    y = c(85, 55, 40, 77,
        75, 45, 35, 67,
        31, 20, 9, 37,
        43, 21, 15, 27,
        17, 10, 8, 15 ))

data$sampling_method <- as.factor(data$sampling_method)
model <- aov(y ~ sampling_method, data = data)
summary(model)
TukeyHSD(model, which = 'sampling_method') 