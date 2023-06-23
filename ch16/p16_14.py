from p16_08 import wilxoc_test
import numpy as np

if __name__ == "__main__":
    ## R's wilxoc test had problems with ties and gave strange results I couldn't figure out why.
    ## So I this one myself. 
    A = np.array([0.96,0.82,0.75,0.61,0.89,0.64,0.81,0.68,0.65,0.84,0.59,0.94,0.91,0.77])
    B = np.array([0.87,0.74,0.63,0.55,0.76,0.70,0.69,0.57,0.53,0.88,0.51,0.79,0.84,0.63])
    dif = B - A
    wval = wilxoc_test(dif, 0, "two.sided")
    print(wval)

