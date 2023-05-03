#TODO: My coefficients differ from the answer key's coefficient in terms of sign. Don't know if it is my mistake or the anwer key's. 

x <- c(5, 35, 70, 80, 90)
y <- c(0.0217, 0.190, 0.315, 0.318, 0.433)
log <- glm(y ~ x, family = binomial)
summary(log)


print("============= Odd Ratio ================")
# (p2 / (1-p2)) / (p1 / (1-p1))
# Failure odds are increased by almost 1.8 when 20lbs is added to the load.  
print(exp(20 * 0.02931))
