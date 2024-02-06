# Leggi il nome dell'alunno
# Leggi il nome dell'alunno
 Chiedi in input il numero di giorni
num_giorni = int(input("Inserisci il numero di giorni: "))

# Chiedi in input i servizi richiesti
num_ombrelloni = int(input("Inserisci il numero di ombrelloni: "))
num_lettini = int(input("Inserisci il numero di lettini: "))
num_sdraio = int(input("Inserisci il numero di sedie a sdraio: "))

# Calcola il costo totale per servizio
costo_ombrelloni = num_ombrelloni * 12
costo_lettini = num_lettini * 5
costo_sdraio = num_sdraio * 6.5

# Calcola la spesa complessiva
spesa_complessiva = costo_ombrelloni + costo_lettini + costo_sdraio

# Moltiplica la spesa complessiva per il numero di giorni
spesa_totale = spesa_complessiva * num_giorni

# Visualizza la spesa totale
print("La spesa totale è:", spesa_totale, "euro")