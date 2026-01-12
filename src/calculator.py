#otro comentario
#funciones básicas aritméticas

#sumar dos numeros
def add(a, b):
    return a + b

#restar dos numeros
def subtract(a, b):
    return a - b

#dividir dos numeros
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
def sq(n):
   return n * n

def multiply(a, b):
    return a * b

def potencia(a,b):
    return a**b