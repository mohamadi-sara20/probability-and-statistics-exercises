library(MASS)
library(MuMIn)
library(olsrr)
library(handyplots)

y = c(4.75,4.07,4.04,4.18,4.35,4.16,4.43,3.20,3.02,3.64,3.68,3.60,3.85)
x1 = c(170, 140, 180, 160, 170, 150, 170, 110, 120, 130, 120, 140, 160)
x2 = c(170, 130, 170, 160, 150, 150, 180, 110, 110, 120, 140, 130, 150)
x3 = c(106, 92, 93, 103, 104, 101, 108, 86, 90, 85, 89, 92, 95)
x4 = c(106, 93, 78, 93, 93, 87, 106, 92, 86, 80, 83, 94, 95)
x5 = c(240.57,195.49, 152.99, 197.09, 266.56, 260.56, 219.25, 132.68, 130.24, 205.88, 153.92, 154.64, 240.57)

full.model <- lm(y ~ x1 + x2 + x3 + x4 + x5)

## Check this part's results. According to the stepwise regression, x1 and x5 should be kept. Answer key says otherwise (X3 and x5). 
print("========================== Stepwise Regression ==================================")
step <- stepAIC(full.model,  direction = "both", 
                      trace = 0, alpha=0.1)
summary(step)


print("======================== Combinations ====================================")
options(na.action = "na.fail")
dredge(full.model, evaluate = TRUE,
      rank = "AICc", fixed = NULL,trace = FALSE,subset=TRUE)

print("========================== Residual Plot ==================================")
options(device = "RStudioGD")
ols_plot_resid_stud(step)
resplot(step, residuals='studentized')
resplot(step, residuals='standard')

print("========================== Normal Probability Plot ==================================")
ols_plot_resid_qq(step)

