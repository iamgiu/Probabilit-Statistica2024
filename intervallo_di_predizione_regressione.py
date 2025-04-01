import numpy as np
import scipy.stats as stats

# Funzione per calcolare la retta di regressione
def calcola_retta_regressione(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    Sxy = np.sum(x * y) - n * x_mean * y_mean
    Sxx = np.sum(x ** 2) - n * (x_mean ** 2)
    
    B = Sxy / Sxx
    A = y_mean - B * x_mean
    
    return A, B, Sxx, Sxy

# Funzione per prevedere il valore al giorno dato
def previsione(A, B, giorno):
    return A + B * giorno

# Funzione per calcolare l'intervallo di predizione al 95%
def intervallo_di_predizione(A, B, x, y, giorno, SSr):
    n = len(x)
    s_err = np.sqrt(SSr / (n - 2))
    
    x_mean = np.mean(x)
    Sxx = np.sum((x - x_mean)**2)
    
    t_value = stats.t.ppf(1-0.025, n-2)
    margin_of_error = t_value * s_err * np.sqrt(1 + 1/n + (giorno - x_mean)**2 / Sxx)
    
    y_estimated = previsione(A, B, giorno)
    lower_bound = y_estimated - margin_of_error
    upper_bound = y_estimated + margin_of_error
    
    return y_estimated, lower_bound, upper_bound

# Esempio di dati (numeri del giorno e ritardi)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.62, 1.73, 1.80, 1.80, 1.81, 1.87, 1.92, 1.94, 1.95, 1.97])

# Calcola la retta di regressione
A, B, Sxx, Sxy = calcola_retta_regressione(x, y)

# Stampa i risultati
print(f"La retta di regressione è: Y(x) = {A:.2f} + {B:.2f}x")

# Previsione per il giorno 11
giorno = 12
ritardo_previsto = previsione(A, B, giorno)
print(f"Il ritardo previsto per il giorno {giorno} è: {ritardo_previsto:.2f}")

# Per verificare il risultato, possiamo anche calcolare i vari step come nel testo
x_mean = np.mean(x)
y_mean = np.mean(y)
Syy = np.sum(y ** 2) - len(y) * y_mean **2
SSr = ((Sxx * Syy) - Sxy ** 2) / Sxx

# Calcola l'intervallo di predizione al 95% per il giorno 11
y_est, lower_bound, upper_bound = intervallo_di_predizione(A, B, x, y, giorno, SSr)
print(f"L'intervallo di predizione al 95% è: ({lower_bound:.2f}, {upper_bound:.2f})")

D_ts = np.sqrt(((10-2) * Sxx) / SSr) * (B - 0.02)
print(f"Il D_ts vale: {D_ts}")


# Stampa i vari step per verificare il risultato
print(f"x̄ = {x_mean}")
print(f"ȳ = {y_mean}")
print(f"Sxy = {Sxy}")
print(f"Sxx = {Sxx}")
print(f"Syy = {Syy}")
print(f"B = {B}")
print(f"A = {A}")
print(f"SSr = {SSr}")