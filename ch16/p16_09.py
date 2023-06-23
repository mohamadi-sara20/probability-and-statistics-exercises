from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 
    time = np.array([9, 12, 18, 14, 12, 14, 12, 10, 16, 11, 9, 11, 13, 11, 13, 15, 13, 14])
    wval = wilxoc_test(time, 12)
    print(wval)
