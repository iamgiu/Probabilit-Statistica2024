from scipy.stats import binomtest

def test_dei_segni(pre, post):
    # Assicurati che le due liste abbiano la stessa lunghezza
    if len(pre) != len(post):
        raise ValueError("Le liste devono avere la stessa lunghezza.")
    
    # Calcola il numero di osservazioni positive e negative
    pos = 0
    neg = 0
    
    for p, q in zip(pre, post):
        if q > p:
            pos += 1
        elif q < p:
            neg += 1
    
    # Calcola il numero di "pareggi"
    ties = len(pre) - (pos + neg)
    
    # Calcola il valore di p usando il test binomiale
    n = pos + neg
    p_value = binomtest(min(pos, neg), n=n, p=0.5, alternative='two-sided')
    
    return pos, neg, ties, p_value

# Esempio di utilizzo
pre = [30.5, 18.5, 24.5, 32, 16, 15, 23.5, 25.5, 28, 18]
post = [23, 21, 22, 28.5, 14.5, 15.5, 24.5, 21, 23.5, 16.5]

pos, neg, ties, p_value = test_dei_segni(pre, post)

print(f"Positivi: {pos}")
print(f"Negativi: {neg}")
print(f"Pareggi: {ties}")
print(f"P-value: {p_value}")

#if p_value < 0.05:
    #print("Il risultato è statisticamente significativo (p < 0.05).")
#else:
    #print("Il risultato non è statisticamente significativo (p >= 0.05).")