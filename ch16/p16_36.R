library(DescTools)

panel <- c(6, 9, 2, 8, 5, 1, 7, 4, 3)
price <- c(480, 395, 575, 550, 510, 545, 400, 465, 420)
# Is there a significance correlation?
cor <- cor.test(x = panel, y = price, method = "spearman", exact = FALSE)
print(cor$p.value)
