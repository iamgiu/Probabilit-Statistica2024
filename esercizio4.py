import math
from scipy.stats import norm
from scipy.stats import t

x = [1.81, 1.73, 1.87, 1.80, 1.80, 1.92, 1.62, 1.95, 1.94, 1.97]

n = len(x)

# Calcolo della media
mu_hat = (1/n) * sum(x)
s = math.sqrt(sum((xi - mu_hat) ** 2 for xi in x) / (n-1))

confidence_level_t = 0.90
alpha_t = 1 - confidence_level_t
t_score = t.ppf(1 - alpha_t/2, df=n-1)

print(f"t_score {t_score}")

margin_of_error_t = t_score * (s / math.sqrt(1+(1/n)))

confidence_interval_t = (mu_hat - margin_of_error_t, mu_hat + margin_of_error_t)

print(f"Intervallo di confidenza al 95% (varianza non nota): {confidence_interval_t}")