import math
from scipy.stats import norm
from scipy.stats import t

x = [1.81, 1.73, 1.87, 1.80, 1.80, 1.92, 1.62, 1.95, 1.94, 1.97]

n = len(x)

# Calcolo della media
mu_hat = (1/n) * sum(x)

# Calcolo della deviazione standard
sigma_hat = math.sqrt(sum((xi - mu_hat) ** 2 for xi in x) / n)
s = math.sqrt(sum((xi - mu_hat) ** 2 for xi in x) / (n-1))

print(f"Media (mu_hat): {mu_hat}")
print(f"Deviazione standard (sigma_hat): {sigma_hat}")

print(f"Deviazione standard campionaria(s): {s}")


sigma = math.sqrt(5)

confidence_level = 0.95
z_score = norm.ppf(1 - (1 - confidence_level) / 2)

margin_of_error = z_score * (sigma / math.sqrt(n))

confidence_interval = (mu_hat - margin_of_error, mu_hat + margin_of_error)

print(f"Intervallo di confidenza al 95%: {confidence_interval}")

confidence_level_t = 0.95
alpha_t = 1 - confidence_level_t
t_score = t.ppf(1 - alpha_t/2, df=n-1)

margin_of_error_t = t_score * (s / math.sqrt(n))

confidence_interval_t = (mu_hat - margin_of_error_t, mu_hat + margin_of_error_t)

print(f"Intervallo di confidenza al 95% (varianza non nota): {confidence_interval_t}")