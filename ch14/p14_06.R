library(dplyr)
library(agricolae)
library(DescTools)


additive   <-  c(c("Y", "Y", "Y", "Y"),
                    c("Y", "Y", "Y", "Y"),
                    c("Y", "Y", "Y", "Y"),
                    c("Y", "Y", "Y", "Y"),
                    c("M", "M", "M", "M"),
                    c("M", "M", "M", "M"),
                    c("M", "M", "M", "M"),
                    c("M", "M", "M", "M")
                    )

temp <-  c(
            c("50", "50", "50", "50"),
            c("60", "60", "60", "60"),
            c("70", "70", "70", "70"),
            c("80", "80", "80", "80"),

            c("50", "50", "50", "50"),
            c("60", "60", "60", "60"),
            c("70", "70", "70", "70"),
            c("80", "80", "80", "80")
            )


yield  <- c(2.3, 2.9, 3.1, 3.2,
            3.4, 3.7, 3.6, 3.2,
            3.8, 3.9, 4.1, 3.8,
            3.9, 3.2, 3, 2.7,

            4.3, 3.9, 3.9, 4.2,
            3.8, 3.8, 3.9, 3.5,
            3.9, 4, 3.7, 3.6,
            3.5, 3.6, 3.8, 3.9
            )


data <- data.frame(temp, additive, yield)
model <- aov(yield ~ additive * temp, data = data)
summary(model)
