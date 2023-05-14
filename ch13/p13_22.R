library(dplyr)
library(agricolae)
library(DescTools)

data <- data.frame(
    absolvent = c("aromatics","aromatics", "aromatics", "aromatics",
    "aromatics", "aromatics","aromatics","aromatics", "aromatics",
    "chloroalkanes", "chloroalkanes", "chloroalkanes", "chloroalkanes",
    "chloroalkanes", "chloroalkanes", "chloroalkanes", "chloroalkanes",
     "esters", "esters", "esters", "esters", "esters",
    "esters", "esters", "esters", "esters", "esters", "esters", "esters", 
    "esters", "esters", "esters"),
    y = c(1.06,0.95,0.79,0.65,0.82,1.15,0.89,1.12, 1.05,
    1.58,1.12,1.45,0.91,0.57,0.83,1.16,0.43,
    0.29,0.43,0.06,0.06,0.51,0.09,0.44,0.10,
    0.17,0.55,0.53,0.17,0.61,0.34,0.60))

anv <- aov(y ~ as.factor(absolvent), data = data)
PostHocTest(anv, method = "duncan")
