from p11_1 import * 
from p11_15 import * 
from scipy import stats

if __name__ == "__main__":
    x = [40,20,25,20,30,50,40,20,50,40,25,50]   
    y = [385,400,395,365,475,440,490,420,560,525,480,510]
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    b1 = estimate_slope(x=x,y=y,mean_x=mean_x, mean_y=mean_y)
    b0 = estimate_intercept(mean_y=mean_y, b1=b1, mean_x=mean_x)
    y_pred = []
    for i in range(len(x)):
        y_pred.append(b1 * x[i] + b0)
    df = len(x) - 2
    s = calculate_s(y=y,y_pred=y_pred)
    tsig = stats.t.isf(0.025, df)
    Sxx = calculate_Sxx(x=x, mean_x=mean_x)
    tvalue = ((b1 - 6) * math.sqrt(Sxx)) / s
   
    if tvalue < tsig:
        print(f"Intercept is greater than 6. Tvalue: {tvalue} ")
    else:
        print(f"Tvalue {tvalue}. Not significant")
    