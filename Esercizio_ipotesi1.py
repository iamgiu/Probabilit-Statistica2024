import scipy.stats as stats

def verifica_ipotesi(mu_hat, s, n, mu_0, alpha):
    # Calcolo della statistica T
    T = (mu_hat - mu_0) / (s / (n ** 0.5))
    
    # Calcolo del valore critico t
    t_critical = stats.t.ppf(alpha, df=n-1)
    
    # Output dei risultati
    print(f"Statistica T: {T:.4f}")
    print(f"Valore critico t: {t_critical:.4f}")
    
    if T < t_critical:
        print("Rifiutare l'ipotesi nulla (H0).")
    else:
        print("Non rifiutare l'ipotesi nulla (H0).")

# Esempio di utilizzo del programma
mu_hat_primo_autobus = 4  # Media campionaria per il primo autobus
s_primo_autobus = 1.5  # Deviazione standard per il primo autobus
n_primo_autobus = 10  # Dimensione del campione per il primo autobus
mu_0_primo_autobus = 1 + 1  # Valore ipotizzato della media per il primo autobus
alpha = 0.1  # Livello di significatività

verifica_ipotesi(mu_hat_primo_autobus, s_primo_autobus, n_primo_autobus, mu_0_primo_autobus, alpha)

mu_hat_secondo_autobus = 4  # Media campionaria per il secondo autobus
s_secondo_autobus = 2  # Deviazione standard per il secondo autobus
n_secondo_autobus = 10  # Dimensione del campione per il secondo autobus
mu_0_secondo_autobus = 1 + 6  # Valore ipotizzato della media per il secondo autobus

verifica_ipotesi(mu_hat_secondo_autobus, s_secondo_autobus, n_secondo_autobus, mu_0_secondo_autobus, alpha)