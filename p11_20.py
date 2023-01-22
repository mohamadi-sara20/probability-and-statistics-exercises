from scipy import stats
from p11_1 import *
from p11_15 import * 

if __name__ == "__main__":
    x=[50,35,35,40,55,65,35,60,90,35,90,80,60,60,60,40,55,50,65,50]
    y=[53,41,61,56,68,36,11,70,79,59,54,91,48,71,71,47,53,68,57,79]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x,y=y,mean_x=mean_x, mean_y=mean_y)
    b0 = estimate_intercept(mean_y=mean_y, b1=b1, mean_x=mean_x)
    y_pred = []
    for i in range(len(x)):
        y_pred.append(b1 * x[i] + b0)
    Sxx = calculate_Sxx(x=x, mean_x=mean_x)
    s = calculate_s(y=y,y_pred=y_pred)
    x2 = np.sum(np.power(x, 2))
    den = s * math.sqrt(x2/ (len(x) * Sxx))
    tvalue = (b0 - 10) / den
    df = len(x) - 2
    tsig = stats.t.isf(0.05, df)
    if tvalue > tsig:
        print(f"Intercept is greater than 10. Tvalue: {tvalue} ")
    else:
        print(f"Tvalue {tvalue}. Not significant")
    