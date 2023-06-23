from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 

    before = np.array([158, 149, 160, 155, 164, 138, 163, 159, 165, 145, 150, 161, 132, 155, 146, 159])
    after = np.array([164, 158, 163, 160, 172, 147, 167, 169, 173, 147, 156, 164, 133, 161, 154, 170])
    dif = after - before
    wval = wilxoc_test(dif, 8, "less")
    print(wval)
