library(dplyr)
library(ggplot2)
library(agricolae)
library(DescTools)

yield <- c(
        38.62,
        38.45,
        39.82,
        39.82,
        37.20,
        38.64,
        39.15,
        40.26,
        38.02,
        38.75,
        39.78,
        39.72,
        37.67,
        37.81,
        39.53,
        39.56,
        37.57,
        37.75,
        39.76,
        39.25,
        37.85,
        37.91,
        39.90,
        39.04,
        37.51,
        37.21,
        39.34,
        39.74,
        37.74,
        37.42,
        39.60,
        39.49,
        37.58,
        37.79,
        39.62,
        39.45,
        37.52,
        37.60,
        40.09,
        39.36,
        37.15,
        37.55,
        39.63,
        39.38,
        37.51,
        37.91,
        39.67,
        39.00
       )
A <- c("A1", "A1", "A1", "A1", "A1", "A1",
        "A1", "A1", "A1", "A1", "A1", "A1",

        "A2", "A2", "A2", "A2", "A2", "A2",
        "A2", "A2", "A2", "A2", "A2", "A2",

        "A3", "A3", "A3", "A3", "A3", "A3",
        "A3", "A3", "A3", "A3", "A3", "A3",

        "A4", "A4", "A4", "A4", "A4", "A4",
        "A4", "A4", "A4", "A4", "A4", "A4"
        )

B <- rep(c("B1", "B2", "B1", "B2"), 12)
C <- rep(c("HOT", "HOT", "ROOM",  "ROOM"), 12)

data <- data.frame(A, B, C, yield)
model <- aov(yield ~ A * B * C, data=data)
summary(model)
# interaction.plot(x.factor = data$B, 
#                  trace.factor = data$C,
#                  response = data$yield, 
#                  fun = median, #metric to plot
#                  ylab = "C",
#                  xlab = "B",
#                  col = c("pink", "blue"),
#                  lty = 1, #line type
#                  lwd = 2, #line width
#                  trace.label = "weight percent of ammonium perchlorate")

interaction.plot(x.factor = data$A, 
                 trace.factor = data$B,
                 response = data$yield, 
                 fun = median, #metric to plot
                 ylab = "B",
                 xlab = "A",
                 col = c("pink", "blue"),
                 lty = 1, #line type
                 lwd = 2, #line width
                 trace.label = "weight percent of ammonium perchlorate")

PostHocTest(model, method = "duncan")
TukeyHSD(model) 