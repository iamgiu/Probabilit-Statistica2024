import numpy as np
import scipy.stats as stats

def single_sample_t_test(sample_mean, population_mean, sample_std, sample_size, alpha):
    # Calcolare la statistica T
    t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(sample_size))
    print('T-Statistic:', t_statistic)
    
    # Calcolare i gradi di libertà
    df = sample_size - 1
    
    # Approach 1: Utilizzare il T-Critico
    # T-Critico per un test a due code
    t_critical = stats.t.ppf(1 - alpha/2, df)
    print('Critical T-Score:', t_critical)
    
    # Ipotesti per il T-Critico
    if abs(t_statistic) > t_critical:
        print("Reject Null Hypothesis (H0)")
    else:
        print("Fail to Reject Null Hypothesis (H0)")
    
    # Approach 2: Utilizzare il P-Value
    # Calcolare il P-Value per un test a due code
    p_value = (1 - stats.t.cdf(abs(t_statistic), df)) * 2 # -> bilaterale
    print('P-Value:', p_value)
    
    # Ipotesti per il P-Value
    if p_value < alpha:
        print("Reject Null Hypothesis (H0)")
    else:
        print("Fail to Reject Null Hypothesis (H0)")

# Esempio di utilizzo con i dati dell'immagine
population_mean = 26.4  # Media della popolazione venti anni fa
sample_mean = 30  # Media del campione attuale
sample_std = 3.53  # Deviazione standard del campione attuale
sample_size = 10  # Dimensione del campione attuale
alpha = 0.05  # Livello di significatività

single_sample_t_test(sample_mean, population_mean, sample_std, sample_size, alpha)