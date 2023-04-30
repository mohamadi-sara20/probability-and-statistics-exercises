library(MASS)
library(tidyverse)

y = c(11.2, 14.5, 17.2, 17.8, 19.3, 24.5, 21.2, 16.9, 14.8, 20.0, 13.2, 22.5)
x1 = c(56.5, 59.5, 69.2, 74.5, 81.2, 88.0, 78.2, 69.0, 58.1, 80.5, 58.3, 84.0)
x2 = c(71.0, 72.5, 76.0, 79.5, 84.0, 86.2, 80.5, 72.0, 68.0, 85.0, 71.0, 87.2)
x3 = c(38.5, 38.2, 42.5, 43.4, 47.5, 47.4, 44.5, 41.8, 42.1, 48.1, 37.5, 51.0)
x4 = c(43.0, 44.8, 49.0, 56.3, 60.2, 62.0, 58.1, 48.1, 46.0, 60.3, 47.1, 65.2)

full.model <- lm(y ~ x1 + x2 + x3 + x4)
step.model <- stepAIC(full.model, direction = "both", 
                      trace = FALSE)
summary(step.model)
print("============================================================")
step.model <- stepAIC(full.model, direction = "forward", 
                      trace = FALSE)
summary(step.model)
print("============================================================")
step.model <- stepAIC(full.model, direction = "backward", 
                      trace = FALSE)
summary(step.model)
