library(DescTools)

midterm <- c(6, 9, 2, 8, 5, 1, 7, 4, 3)
final <- c(480, 395, 575, 550, 510, 545, 400, 465, 420)
# Is there a significance correlation?
cor <- cor.test(x = midterm, y = final, method = "spearman", exact = FALSE)
print(cor$p.value)
