library(partR2)
library(lme4)
library(lmerTest)
library(ggplot2)

cereal     <- rep(c("1", "1", "2", "2", "3", "3"), n=6)
power <-  rep(c("Low", "Current", "High"), each=12)

yield  <- c(
            395, 390, 392, 392, 402, 405,
            401, 400, 394, 401, 399, 399, 
            396, 399, 390, 392, 404, 403, 
            400, 402, 395, 502, 400, 399, 
            410, 408, 404, 406, 415, 412, 
            408, 407, 401, 400, 413, 415
)

data <- data.frame(power, cereal, yield)

m <- lmer(yield ~ power + (1|cereal) + (1|cereal:power), 
data=data)
summary(m)
anova(m)



# interaction.plot(x.factor = data$power, 
#                  trace.factor = data$cereal,
#                  response = data$yield)

ggplot(data=data) +
  aes(x = power, color = cereal, group = cereal, y = yield) +
  stat_summary(fun = mean, geom = "point") +
  stat_summary(fun = mean, geom = "line")
