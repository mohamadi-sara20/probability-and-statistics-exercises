library(lme4)

y = c(34.5,33.3,30.4,32.8,35.0,29.0,32.5,29.6,16.8,19.2,22.6,24.4,20.7,25.1,18.8,15.8,17.4,15.6,17.3,20.8,22.2,16.5,21.3,20.7,24.1)
x1 = c("sedan","sedan","sedan","sedan","sedan","sedan","sedan","sedan","van","van","van","van","van","van","van","van","van","SUV","SUV","SUV","SUV","SUV","SUV","SUV","SUV")
x2 = c(75000,60000,88000,15000,25000,35000,102000,98000,56000,72000,14500,22000,66500,35000,97500,42000,65500,65000,55500,26500,11500,38000,77500,19500,87000)
x3 = c(87.5,87.5,78.0,78.0,90.0,78.0,90.0,87.5,87.5,90.0,87.5,90.0,78.0,90.0,87.5,78.0,78.0,78.0,87.5,87.5,90.0,78.0,90.0,78.0,90.0)

fit <- lm(y ~ x1 + x2 + x3)
summary(fit)