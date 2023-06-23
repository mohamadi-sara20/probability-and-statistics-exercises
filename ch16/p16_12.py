from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 

    A = np.array([19, 21, 15, 17, 24, 12, 19, 14, 20, 18, 23, 21, 17, 12, 16, 15, 20, 18, 14, 22])
    B = np.array([17, 15, 12, 12, 16, 15, 11, 13, 14, 21, 19, 15, 11, 10, 20, 12, 13, 17, 16, 18])
    dif = B - A
    wval = wilxoc_test(dif, 0, "greater")
    print(wval)



