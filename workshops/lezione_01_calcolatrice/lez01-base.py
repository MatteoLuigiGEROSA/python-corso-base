# Lezione 1 + 2 - Introduzione a Python, Condizioni, Cicli, Strutture Dati

# ================================
# 1. Stampa e input
# ================================
print("Benvenuto al Corso di Python!")
nome = input("Come ti chiami? ")
print("Ciao,", nome)

# ================================
# 2. Tipi di variabili e operatori
# ================================
intero = 10
virgola = 3.14
vero_falso = True
stringa = "Python"

somma = intero + virgola
print("Somma:", somma)

# ================================
# 3. Condizioni: if, elif, else
# ================================
eta = int(input("Quanti anni hai? "))
if eta >= 18:
    print("Sei maggiorenne")
elif eta > 0:
    print("Sei minorenne")
else:
    print("Età non valida")

# ================================
# 4. Calcolatrice base (con funzioni)
# ================================
def calcolatrice(a, b, operatore):
    if operatore == '+':
        return a + b
    elif operatore == '-':
        return a - b
    elif operatore == '*':
        return a * b
    elif operatore == '/':
        return a / b
    else:
        return "Operatore non valido"

print("Calcolatrice")
x = float(input("Numero 1: "))
y = float(input("Numero 2: "))
op = input("Operazione (+, -, *, /): ")
print("Risultato:", calcolatrice(x, y, op))

# ================================
# 5. Verifica pari o dispari
# ================================
numero = int(input("Inserisci un numero: "))
if numero % 2 == 0:
    print("Pari")
else:
    print("Dispari")

# ================================
# 6. Ciclo while
# ================================
contatore = 0
while contatore < 5:
    print("Contatore:", contatore)
    contatore += 1

# ================================
# 7. Simulazione do-until (loop con condizione alla fine)
# ================================
while True:
    risposta = input("Scrivi 'exit' per uscire: ")
    if risposta == 'exit':
        break

# ================================
# 8. Ciclo for con range
# ================================
for i in range(1, 6):
    print("Numero:", i)

# ================================
# 9. Liste e accesso agli elementi
# ================================
frutta = ["mela", "banana", "arancia"]
frutta.append("kiwi")
print("Lista frutta:", frutta)
print("Prima frutta:", frutta[0])

# ================================
# 10. Tuple e stringhe come sequenze
# ================================
tupla = (1, 2, 3)
print("Tupla:", tupla)
parola = "python"
for lettera in parola:
    print(lettera)

# ================================
# 11. Esercizi applicativi
# ================================
# Conteggio numeri da 1 a N
N = int(input("Fino a che numero vuoi contare? "))
for i in range(1, N + 1):
    print(i)

# Media voti
voti = []
while True:
    voto = input("Inserisci un voto (oppure 'stop'): ")
    if voto == 'stop':
        break
    voti.append(int(voto))

if voti:
    media = sum(voti) / len(voti)
    print("Media voti:", media)
else:
    print("Nessun voto inserito")

# Gestione lista spesa
spesa = []
print("Inserisci gli elementi della lista spesa (scrivi 'fine' per terminare):")
while True:
    item = input("Elemento: ")
    if item == 'fine':
        break
    spesa.append(item)

print("Lista spesa:", spesa)

