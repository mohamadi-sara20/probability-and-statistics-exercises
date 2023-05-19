library(dplyr)
strain   <-  rep(c("Bright", "Mixed", "Dull"), each = 16)
env <-  c(
                c("Free", "Restricted"),
                c("Free", "Restricted"),
                c("Free", "Restricted")
            )
yield  <- c(
            #Bright
            28, 72,
            22, 48,
            25, 25,
            36, 91,
            12, 32,
            23, 93,
            10, 31,
            86, 19,

            #Mixed
            33, 60,
            36, 35,
            41, 83,
            22, 99,
            83, 89,
            14, 126,
            76, 110,
            58, 118,

            #Dull
            101, 136,
            33, 38, 
            122, 64, 
            35, 87, 
            94, 120, 
            56, 153, 
            83, 128, 
            23, 140
            )

data <- data.frame(strain, env, yield)

model <- aov(yield ~ strain * env, data = data)
summary(model)