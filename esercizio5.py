import math
import numpy as np
import scipy.stats as stats

x = [1, 3, 5, 7, 9]
y = [2, 4, 6, 8, 10]

n = len(x)
m = len(y)

x_mean = (1/n) * sum(x)
y_mean = (1/m) * sum(y)

s_x = sum((xi - x_mean) ** 2 for xi in x) / (n-1)
s_y = sum((yi - y_mean) ** 2 for yi in y) / (m-1)

s_p = (((n-1)*s_x)+((m-1)*s_y)/(n+m-2))

df = n+m-2

alpha = 0.05

T = (x_mean - y_mean)/(s_p*math.sqrt((1/n)+(1/m)))
print('T-Statistic:', T)

# T-Critico per un test a due code
t_critical = stats.t.ppf(1 - alpha/2, df)
print('Critical T-Score:', t_critical)

# Ipotesti per il T-Critico
if abs(T) > t_critical:
    print("Reject Null Hypothesis (H0)")
else:
    print("Fail to Reject Null Hypothesis (H0)")