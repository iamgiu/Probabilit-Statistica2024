import numpy as np
from scipy.stats import f_oneway

# Definizione dei gruppi di dati con dimensioni diverse
group1 = np.array([35, 37, 29, 27, 30])
group2 = np.array([29, 38, 34, 30, 32])
group3 = np.array([44, 52, 56])

# Creiamo una lista dei gruppi
groups = [group1, group2, group3]

# Numero di gruppi
m = len(groups)

# Numero totale di osservazioni
n_total = sum(len(group) for group in groups)

# Calcolo della media di ogni gruppo (X_i*)
X_i_star = np.array([np.mean(group) for group in groups])
print(f"Media di ogni gruppo (X_i*): {X_i_star}")

# Calcolo della media complessiva (X_**)
all_data = np.concatenate(groups)
X_star_star = np.mean(all_data)
print(f"Media complessiva (X_**): {X_star_star}")

# Calcolo di SSb
SSb = sum(len(group) * (np.mean(group) - X_star_star)**2 for group in groups)
print(f"Somma dei quadrati tra i gruppi (SSb): {SSb}")

# Calcolo di ∑∑ X_ij^2
sum_X_ij_squared = sum(sum(X_ij**2 for X_ij in group) for group in groups)
print(f"Somma dei quadrati delle osservazioni (∑∑ X_ij^2): {sum_X_ij_squared}")

# Calcolo di SSw
SSw = sum(sum((X_ij - np.mean(group))**2 for X_ij in group) for group in groups)
print(f"Somma dei quadrati entro i gruppi (SSw): {SSw}")

# Calcolo dei gradi di libertà
df_b = m - 1
df_w = n_total - m
print(f"Gradi di libertà tra i gruppi (df_b): {df_b}")
print(f"Gradi di libertà entro i gruppi (df_w): {df_w}")

# Calcolo di MSb e MSw
MSb = SSb / df_b
MSw = SSw / df_w
print(f"Mean Square Between (MSb): {MSb}")
print(f"Mean Square Within (MSw): {MSw}")

# Calcolo del valore F
F = MSb / MSw
print(f"Valore F: {F}")

# Conduct the one-way ANOVA
print(f_oneway(group1, group2, group3))