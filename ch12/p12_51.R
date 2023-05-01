library(MASS)
library(MuMIn)
library(handyplots)

y = c(812.52, 822.50, 1211.50, 1348.00, 1301.00, 2567.50, 2526.50, 2755.00, 4390.50 , 5581.50, 5548.00,6086.00, 5764.00, 8903.00)
x1 = c(1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17)

model <- lm(y ~ x1)
summary(model)


x2 <- c()
for (x in x1) {
    x2 <- c(x2, x^2)
}
model_q <- lm(y ~ x1 + x2)
summary(model_q)


## PRESS still left to compute. 