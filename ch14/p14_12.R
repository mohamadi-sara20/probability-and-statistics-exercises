library(dplyr)
library(ggplot2) 


time   <-  c("5", "5", "5", "12", "12", "12", "18", "18", "18",
             "5", "5", "5", "12", "12", "12", "18", "18", "18",
             "5", "5", "5", "12", "12", "12", "18", "18", "18")
copper <-  c("1", "1", "1", "1", "1", "1", "1", "1", "1",
             "2", "2", "2",  "2", "2", "2", "2", "2", "2",
             "3", "3", "3", "3", "3", "3", "3", "3", "3")

yield  <- c(0.30, 0.34, 0.32, 0.37, 0.36, 0.35, 0.25, 0.23, 0.24,
            0.24, 0.30, 0.27, 0.23, 0.32, 0.25, 0.22, 0.31, 0.25,
            0.20, 0.30, 0.27, 0.28, 0.31, 0.29, 0.24, 0.30, 0.25)

data <- data.frame(time, copper, yield)
amodel <- aov(yield ~ time * copper, data = data)
summary(amodel)
interaction.plot(x.factor = data$copper,
                 trace.factor = data$time,
                 response = data$yield,
                 fun = median, #metric to plot
                 ylab = "Time",
                 xlab = "Copper",
                 col = c("pink", "blue", "red"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "Growth")

# This is weird. Interaction plot obviously signifies interaction,
# while anova results say otherwise. Why? I am guessing maybe it has
# sth to do with statistical power? Sample size should be increased?
# That answer key has totally different number though. Not sure.
# A linear model shows interaction on different levels of the factors.


lmodel <- lm(yield ~ time * copper, data = data)
summary(lmodel)
