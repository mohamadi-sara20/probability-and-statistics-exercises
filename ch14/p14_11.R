library(dplyr)
library(agricolae)
library(DescTools)
library(lme4)

method   <-  c("1", "1", "1", "1", "1", "1", "1", "1","1", "1", "1", "1", "1", "1", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2")
lab <-  c(c("1", "2", "3", "4", "5", "6", "7", "1", "2", "3", "4", "5", "6", "7"),
            c("1", "2", "3", "4", "5", "6", "7", "1", "2", "3", "4", "5", "6", "7"))


yield  <- c(
c(0.109,
0.129,
0.115,
0.108,
0.097,
0.114,
0.155),
c(0.105,
0.122,
0.112,
0.108,
0.096,
0.119,
0.145),
c(0.105,
0.127,
0.109,
0.117,
0.110,
0.116,
0.164),
c(0.108,
0.124,
0.111,
0.118,
0.097,
0.122,
0.160)
)


data <- data.frame(method, lab, yield)
model <- aov(yield ~ method * lab, data = data)
summary(model)

interaction.plot(x.factor = data$lab, 
                 trace.factor = data$method,
                 response = data$yield, 
                 fun = median, #metric to plot
                 ylab = "Method",
                 xlab = "Lab",
                 col = c("pink", "blue"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "Sulfur Content")
