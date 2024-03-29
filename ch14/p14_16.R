library(dplyr)
library(ggplot2)

yield <- c(
    
        # A1
        4, 3.4, 3.9, 4.4, 3.1, 3.1,
        4.9, 4.1, 4.3, 3.4, 3.5, 3.7,
        # A2
        3.6, 2.8, 3.1, 2.7, 2.9, 3.7,
        3.9, 3.2, 3.5, 3., 3.2, 4.2,
        # A3
        4.8, 3.3, 3.6, 3.6, 2.9, 2.9,
        3.7, 3.8, 4.2, 3.8, 3.3, 3.5,
        # A4
        3.6, 3.2, 3.2, 2.2, 2.9, 3.6,
        3.9, 2.8, 3.4, 3.5, 3.2, 4.3
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

B <- rep(c("B1", "B1", "B1", "B2", "B2", "B2"), 8)
C <- rep(c("C1", "C2", "C3",  "C1", "C2", "C3"), 8)

data <- data.frame(A, B, C, yield)
model <- aov(yield ~ A + B + C + B:C, data=data)
summary(model)