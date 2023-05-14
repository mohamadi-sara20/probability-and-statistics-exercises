import numpy as np
from p13_01 import is_significant, anova
from p13_05 import anova_unequqal


if __name__ == "__main__":
    c50 = np.array([13.2,12.4,12.8,17.2,13.0,14.0,14.2,21.6,15.0,20.0])
    c100 = np.array([16.0,12.6,14.8,13.0,14.0,23.6,14.0,17.0,22.2,24.4])
    c200 = np.array([7.8,14.4,20.0,15.8,17.0,27.0,19.6,18.0,20.2,23.2])
    c400 = np.array([21.0,14.8,19.1,15.8,18.0,26.0,21.1,22.0,25.0,18.2])
    X = np.array([c50, c100, c200, c400], dtype=object)
    fval, dfd, dfn = anova_unequqal(X)
    is_significant(fval=fval, alpha=0.05, dfd=dfd, dfn=dfn)
    