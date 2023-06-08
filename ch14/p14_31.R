library(partR2)
library(lme4)
library(lmerTest)


brand     <- c("A", "A", "B", "B","C", "C", "A", "A", "B", "B","C", "C", 
"A", "A", "B", "B","C", "C")
material <-  rep(c("A", "B", "C"), each=6)
yield  <- c(
           5.50, 5.15,
            4.75, 4.60,
            5.10, 5.20,
            5.60, 5.55,
            5.50, 5.60,
            5.40, 5.50,
            5.40, 5.48,
            5.05, 4.95,
            4.50, 4.55
)
data <- data.frame(brand, material, yield)

m <- lmer(yield ~ brand + (1|material) + (1|material:brand), 
data=data)
summary(m)
anova(m)



interaction.plot(x.factor = data$brand, 
                 trace.factor = data$material,
                 response = data$yield)


# aev <- aov(yield ~ brand * material, data=data)
# summary(aev)