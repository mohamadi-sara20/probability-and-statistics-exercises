library(BSDA)

regular <- c(6.6,5.8,7.8,5.7,6.0,8.4,8.8,8.4,7.3,5.8,5.8,6.5)
new <- c(6.4, 5.8, 7.4, 5.5, 6.3, 7.8, 8.6, 8.2, 7.0, 4.9, 5.9, 6.5)
d_o <- mapply("-", new, regular, SIMPLIFY = TRUE)
sign

# H0: d0 = 0 (M1 = M2)
# H1:  d_0 < 0
SIGN.test(d_o, md = 0, alternative = "less")
