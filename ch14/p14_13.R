library(dplyr)
library(agricolae)
library(DescTools)
library(lme4)

treatment   <-  c("1", "1", "1", "2", "2", "2", "1", "1", "1", "2", "2", "2")
time <-  c("1", "1", "1", "1", "1", "1",  "2", "2", "2",  "2", "2", "2")
yield  <- c(2.19, 2.15, 2.16, 2.03, 2.01, 2.04, 2.01, 2.03, 2.04, 1.88, 1.86, 1.91)

data <- data.frame(treatment, time, yield)
model <- aov(yield ~ treatment * time, data = data)
interaction.plot(x.factor = data$treatment, 
                 trace.factor = data$time,
                 response = data$yield, 
                 fun = median, #metric to plot
                 ylab = "Time",
                 xlab = "Treatment",
                 col = c("pink", "blue"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "mg Intake")


# summary(model)
data$treatment <- factor(data$treatment)
lmodel <- lm(yield ~ treatment * time, data=data)
summary(lmodel)