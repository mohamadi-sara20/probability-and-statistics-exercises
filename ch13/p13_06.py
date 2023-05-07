import numpy as np
from p13_1 import is_significant
from p13_5 import anova_unequqal


if __name__ == "__main__":
    aromatics = np.array([1.06,0.95,0.79,0.65,0.82,1.15,0.89,1.12, 1.05])
    chloroalkanes = np.array([1.58,1.12,1.45,0.91,0.57,0.83,1.16,0.43])
    esters  = np.array([0.29,0.43,0.06,0.06,0.51,0.09,0.44,0.10,0.17,0.55,0.53,0.17,0.61,0.34,0.60])
    X = np.array([aromatics, chloroalkanes, esters], dtype=object)
    fval, dfd, dfn = anova_unequqal(X)
    is_significant(fval=fval, alpha=0.01, dfd=dfd, dfn=dfn)
    