import numpy as np

# Funzione per calcolare la retta di regressione
def calcola_retta_regressione(x, y):
    n = len(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    
    Sxy = np.sum(x * y) - n * x_mean * y_mean
    Sxx = np.sum(x ** 2) - n * (x_mean ** 2)
    
    B = Sxy / Sxx
    A = y_mean - B * x_mean
    
    return A, B

# Funzione per prevedere il valore al giorno dato
def previsione(A, B, giorno):
    return A + B * giorno

# Esempio di dati (numeri del giorno e ritardi)
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([1.62, 1.73, 1.80, 1.80, 1.81, 1.87, 1.92, 1.94, 1.95, 1.97])

# Calcola la retta di regressione
A, B = calcola_retta_regressione(x, y)

# Stampa i risultati
print(f"La retta di regressione è: Y(x) = {A:.2f} + {B:.2f}x")

# Previsione per il giorno 15
giorno = 11
ritardo_previsto = previsione(A, B, giorno)
print(f"Il ritardo previsto per il giorno {giorno} è: {ritardo_previsto:.2f}")

# Per verificare il risultato, possiamo anche calcolare i vari step come nel testo
x_mean = np.mean(x)
y_mean = np.mean(y)
Sxy = np.sum(x * y) - len(x) * x_mean * y_mean
Sxx = np.sum(x ** 2) - len(x) * x_mean ** 2
Syy = np.sum(y ** 2) - len(y) * y_mean **2
SSr = ((Sxx * Syy) - Sxy ** 2) / Sxx

print(f"x̄ = {x_mean}")
print(f"ȳ = {y_mean}")
print(f"Sxy = {Sxy}")
print(f"Sxx = {Sxx}")
print(f"Syy = {Syy}")
print(f"B = {B}")
print(f"A = {A}")
print(f"SSr = {SSr}")

