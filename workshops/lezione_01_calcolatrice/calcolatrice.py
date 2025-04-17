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
