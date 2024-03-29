library(BSDA)

impurity <- c(2.4, 2.3, 3.1, 2.2, 2.3, 1.2, 1.0, 2.4,
            1.7, 1.1, 4.2, 1.9, 1.7, 3.6, 1.6, 2.3)

# H0: impurity = 2.5%
SIGN.test(impurity, md = 2.5)
