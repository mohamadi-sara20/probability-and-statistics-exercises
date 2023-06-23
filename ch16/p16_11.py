from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 
    before = np.array([60, 54.9, 58.1, 62.1, 58.5, 59.9, 54.4, 60.2, 62.3, 58.7])
    after = np.array([58.5, 60.3, 61.7, 69.0, 64.0, 62.6, 56.7, 63.6, 68.2, 59.4])
    dif = after - before
    wval = wilxoc_test(dif, 4.5, "greater")
    print(wval)



