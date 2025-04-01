# Importing library
from scipy.stats import f_oneway
import numpy as np

# Definizione dei gruppi di dati
group1 = np.array([0.046, 0.025, 0.014, 0.017, 0.043])
group2 = np.array([0.038, 0.035, 0.031, 0.022, 0.012])
group3 = np.array([0.031, 0.042, 0.020, 0.018, 0.039])

# Creiamo una lista dei gruppi
groups = [group1, group2, group3]

# Numero totale di gruppi e numero di osservazioni per gruppo
m = len(groups)
n = len(groups[0])

# Calcolo della media di ogni gruppo (X_i*)
X_i_star = np.array([np.mean(group) for group in groups])
print(f"Media di ogni gruppo (X_i*): {X_i_star}")

# Calcolo della media complessiva (X_**)
X_star_star = np.mean(X_i_star)
print(f"Media complessiva (X_**): {X_star_star}")

# Calcolo di SSb
SSb = n * sum((X_i - X_star_star)**2 for X_i in X_i_star)
print(f"Somma dei quadrati tra i gruppi (SSb): {SSb}")

# Calcolo di ∑∑ X_ij^2
sum_X_ij_squared = sum(sum(X_ij**2 for X_ij in group) for group in groups)
print(f"Somma dei quadrati delle osservazioni (∑∑ X_ij^2): {sum_X_ij_squared}")

# Calcolo di SSw
SSw = sum_X_ij_squared - m * n * X_star_star**2 - SSb
print(f"Somma dei quadrati entro i gruppi (SSw): {SSw}")

# Calcolo dei gradi di libertà
df_b = m - 1
df_w = m * n - m
print(f"Gradi di libertà tra i gruppi (df_b): {df_b}")
print(f"Gradi di libertà entro i gruppi (df_w): {df_w}")

# Calcolo di MSb e MSw
MSb = SSb / df_b
MSw = SSw / df_w
print(f"Mean Square Between (MSb): {MSb}")
print(f"Mean Square Within (MSw): {MSw}")

# Calcolo del valore F
F = MSb / MSw
print(f"Valore F: {F:.4f}")

# Conduct the one-way ANOVA
print(f_oneway(group1, group2, group3))