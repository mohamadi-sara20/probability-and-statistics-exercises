library(partR2)
library(lme4)
library(lmerTest)

operator   <-  rep(c("1", "2", "3", "4"), 9)
filter <- rep(c("1", "2", "3"), each=12)
yield  <- c(
            16.2,
            15.9,
            15.6,
            14.9,
            16.8,
            15.1,
            15.9,
            15.2,
            17.1,
            14.5,
            16.1,
            14.9,
            16.6,
            16.0,
            16.1,
            15.4,
            16.9,
            16.3,
            16.0,
            14.6,
            16.8,
            16.5,
            17.2,
            15.9,
            16.7,
            16.5,
            16.4,
            16.1,
            16.9,
            16.9,
            17.4,
            15.4,
            17.1,
            16.8,
            16.9,
            15.6
)

data <- data.frame(operator, filter, yield)
m <- aov(yield~ operator * filter, data=data)
summary(m)

# This is also a bit weird. These numbers are alike
# to the guide's, but some say - as far as I understood - 
# significance of random effects would better not be explored.
# Walpole says the mean squares in random effect models are the same 
# as mean squares in fixed effects models. 
# So to compute significance, he builds an F-test: s1**2/s**2
# If it is significant, then it means that H0 
# - that there is no random effect = that variance of the random effect equals zero
# is false. This I find still a bit confusing though so I will have
# to get back to this later. 
# More info on the issue: https://bbolker.github.io/mixedmodels-misc/glmmFAQ.html#testing-significance-of-random-effects