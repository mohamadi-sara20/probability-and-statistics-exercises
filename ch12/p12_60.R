#TODO: My coefficients differ from the answer key's coefficient in terms of sign. Don't know if it is my mistake or the anwer key's. 

x <- c(0, 30, 60, 75, 90)
y <- c(0.025, 0.192, 0.312, 0.333, 0.4833)
log <- glm(y ~ x, family = binomial())
summary(log)



print("================== B0 ===================")
print(pchisq((-2.69893 / 2.88273)^2, 1))
print("================== B1 ===================")
print(pchisq((0.02931 / 0.04149)^2, 1))

# It does not seem like the coefficients are that significant. 


print("================== ED50 Estimation ==================")
# log(p / (1-p) = log(1) = 0 = B0 + B1X)
# So b0 + b1x = 0
# So x = -b0 / b1
# Effective Dose with a 0.5 prob needs to weigh:

print(2.69893 / 0.02931)




# Book Ex
# x <- c(0.10 ,0.15, 0.20, 0.30, 0.50, 0.70 ,0.95)
# counts <- c(47, 53, 55, 52, 46, 54, 52)
# # y <- c(8, 14, 24, 32, 38, 50, 50)
# p <- c(0.17, 0.264, 0.436, 0.615, 0.826, 0.926, 0.962)
# y <- glm(p  ~  x , family =  binomial())
# summary(y)
