library(DescTools)
library(EnvStats)

material <-  rep(c("1", "2", "3"), each = 10)
yield  <- c(6, 8, 4, 5, 7, 7, 9, 6, 7, 8, 
            3, 3, 5, 4, 2, 4, 4, 5, 4, 3, 
            12,8, 7, 14, 18, 6, 7, 18, 8, 5)

#a) Transform and F-test
trans_yield <- unlist(lapply(yield, sqrt))
data <- data.frame(material, trans_yield)
data$material <- as.factor(data$material)
model <- aov(trans_yield ~ material, data=data)
summary(model)

#b)
TukeyHSD(model, which = 'material')

#c) Residual Plot
resids <- residuals(model)
plot(fitted(model), resids)
abline(0, 0)


# d) Error is not homogenous in Poisson. So y had to be transformed
#    via a variance stabil. function

# e) Equal variances, we can clearly see variance is more
#    in (3)than in (1) and (2)

# f) QQplot
qqPlot(trans_yield)
