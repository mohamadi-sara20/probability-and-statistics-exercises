library(DescTools)
subject   <-  c(c("Math", "Enlglish", "French", "Biology"),
                c("Math", "Enlglish", "French", "Biology"),
                c("Math", "Enlglish", "French", "Biology"),
                c("Math", "Enlglish", "French", "Biology"),
                c("Math", "Enlglish", "French", "Biology"))

student <-  rep(c("1", "2", "3", "4", "5"), each = 4)
yield  <- c(68, 57, 73, 61,
            83, 94, 91, 86, 
            72, 81, 63, 59, 
            55, 73, 77, 66,
            92, 68, 75, 87
            )

data <- data.frame(subject, student, yield)
data$student <- as.factor(data$student)
data$subject <- as.factor(data$subject)

model <- aov(yield ~ subject + student, data = data)
summary(model)
