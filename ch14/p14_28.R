library(partR2)
library(lme4)
library(lmerTest)

inspector   <-  rep(c("A", "B", "C", "A", "B", "C", "A", "B", "C"), each=5)
inspection <- rep(c("Full", "Reduced", "Commercial"), each=15)
yield  <- c(
            7.50, 7.42, 5.85, 5.89,
            5.35, 7.58, 6.52,
            6.54, 5.64, 5.12, 7.70, 6.82,
            6.42, 5.39, 5.35,

            7.08, 6.17, 5.65, 5.30, 5.02,
            7.68, 5.86, 5.28, 5.38, 4.87,
            7.19, 6.19, 5.85, 5.35, 5.01,

            6.15,5.52,5.48,5.48,5.98,
            6.17,6.20,5.44,5.75,5.68,
            6.21,5.66,5.36,5.90,6.12
)

data <- data.frame(inspection, inspector, yield)
m <- lmer(yield ~ inspection + (1|inspector) + (1|inspector:inspection), 
data=data)
anova(m)
summary(m)

m2 <- aov(yield ~ inspection * inspector, data=data)
summary(m2)

# No effect found (inspection not significant; 
# inspector not significant, nor is interaction)
# Answer key says inspection should be significant though. 
# It is nearly significant at two levels though.
# Check in minitab or whatever to be sure. 