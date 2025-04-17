# ================================
# 4. Calcolatrice base (con funzioni)
# ================================
 
# Funzione per la calcolatrice
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
 
# Funzione per calcolare l'area di un triangolo
def area_del_triangolo(base, altezza):
    area = (base * altezza) / 2
    return area
 
# Menu di scelta per l'utente
print("Benvenuto nella calcolatrice!")
scelta = input("Vuoi usare la calcolatrice (1) o calcolare l'area di un triangolo (2)? ")
 
if scelta == '1':
    print("Calcolatrice")
    x = float(input("Numero 1: "))
    y = float(input("Numero 2: "))
    op = input("Operatore (+,-,*,/): ")
    print("Risultato:", calcolatrice(x, y, op))
 
elif scelta == '2':
    print("Calcolo Area Triangolo")
    base = float(input("Base del triangolo: "))
    altezza = float(input("Altezza del triangolo: "))
    print(f"L'area del triangolo è: {area_del_triangolo(base, altezza)}")
else:
    print("Scelta non valida.")