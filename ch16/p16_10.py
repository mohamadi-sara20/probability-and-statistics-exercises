from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 
    before = np.array([66, 80, 69, 52, 75])
    after = np.array([71, 82, 68, 56, 73])
    dif = after - before
    wval = wilxoc_test(dif, 0, "less")
    print(wval)


