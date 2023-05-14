library(DescTools)

control <- c(2.1, 5.6, 3, 7.8, 5.2, 2.6)
low <- c(6.2, 4, 8.4, 2.8, 4.2, 5)
medium <- c(9.6, 8, 5.5, 12.6, 7, 7.8)
high <- c(10.3, 6.9, 7.8, 5.8, 7.2, 12)

x <- c(control, low, medium, high)
vec <- c("control", "low", "medium", "high")
g <- rep(vec, each = 6)

data <- data.frame(
    financial_leverage = g,
    x = x)

model <- aov(data$x ~ data$financial_leverage )
summary(model)

DunnettTest(x=x, g=g, control="control")
