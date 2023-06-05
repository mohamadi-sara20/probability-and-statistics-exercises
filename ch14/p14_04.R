library(dplyr)
library(agricolae)
library(DescTools)
coating   <-  rep(c("Uncoated", "Anodized", "Conversion"), each = 18)
humidity <-  c(
                c("Low", "Medium", "High"),
                c("Low", "Medium", "High"),
                c("Low", "Medium", "High")
            )
yield  <- c(
            #Uncoated
            361, 314, 1344,
            469, 522, 1216,
            466, 244, 1027,
            937, 739, 1097,
            1069, 261, 1011,
            1357, 134, 1011,

            #Anodized
            114, 322, 78,
            1032, 471, 466,
            1236, 306, 387,
            92, 130, 107,
            533, 68, 130,
            211, 398, 327,
            #Conversion
            130, 252, 586,
            1482, 874, 524,
            841, 105, 402,
            529, 755, 751,
            1595, 847, 846,
            754, 573, 529
            )

data <- data.frame(coating, humidity, yield)

# print(data)


model <- aov(yield ~ coating * humidity, data = data)
summary(model)
mm <- aggregate(data$yield, by=list(Category=data$humidity), FUN=mean)
hmodel <- aov(yield  ~ humidity, data=data)
PostHocTest(hmodel, method = "duncan")