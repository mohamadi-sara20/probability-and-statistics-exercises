library(dplyr)
library(DescTools)

yield <- c(
        82,
        124,
        88,
        129,
        114,
        157,
        121,
        164
       )

rate <- c("12","12","12","12", "24", "24", "24", "24")
temp <- c("220", "250", "220", "250", "220", "250", "220", "250")
p <- c("150", "150", "190", "190","150", "150", "190", "190")

data <- data.frame(rate, temp, p, yield)
model <- aov(yield ~ rate + temp + p + p:rate + p:temp, data=data)
summary(model)
interaction.plot(x.factor = data$p, 
                 trace.factor = data$rate,
                 response = data$yield, 
                 fun = median, #metric to plot
                 ylab = "Rate",
                 xlab = "Powder",
                 col = c("pink", "blue"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "radius of a propellant grain")

interaction.plot(x.factor = data$p, 
                 trace.factor = data$temp,
                 response = data$yield, 
                 fun = median, #metric to plot
                 ylab = "Temp",
                 xlab = "Powder",
                 col = c("pink", "blue"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "radius of a propellant grain")
