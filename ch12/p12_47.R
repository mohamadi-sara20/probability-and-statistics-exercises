library(MASS)

y = c(4.75,4.07,4.04,4.18,4.35,4.16,4.43,3.20,3.02,3.64,3.68,3.60,3.85)
x1 = c(170, 140, 180, 160, 170, 150, 170, 110, 120, 130, 120, 140, 160)
x2 = c(170, 130, 170, 160, 150, 150, 180, 110, 110, 120, 140, 130, 150)
x3 = c(106, 92, 93, 103, 104, 101, 108, 86, 90, 85, 89, 92, 95)
x4 = c(106, 93, 78, 93, 93, 87, 106, 92, 86, 80, 83, 94, 95)
x5 = c(240.57,195.49, 152.99, 197.09, 266.56, 260.56, 219.25, 132.68, 130.24, 205.88, 153.92, 154.64, 240.57)

full.model <- lm(y ~ x1 + x2 + x3 + x4 + x5)
step.model <- stepAIC(full.model, direction = "both", 
                      trace = FALSE)
forward <- stepAIC(full.model, direction = "forward", 
                      trace = FALSE)
backward <- stepAIC(full.model, direction = "backward", 
                      trace = FALSE)


print("============================= Stepwise Regression ============================= ")
summary(step.model)
print("Prediction is:")
print(predict(step.model, newdata=list("x1"=NULL, "x2"=180, "x3"=NULL, "x4"=NULL, "x5"=260)))
print("Prediction Interval:")
print(predict(step.model, newdata=list("x1"=NULL, "x2"=180, "x3"=NULL, "x4"=NULL, "x5"=260), interval="predict"))
print("============================= Forward ============================= ")
summary(forward)
print("============================= Backward ============================= ")
summary(backward)