#Escribir una función que reciba un número y devuelva True si es entero y False si no lo es. Pista: no se puede usar la función isinstance.

def es_entero(numero):
    return numero % 1 == 0

def es_entero2(numero):
    return int(numero) == float(numero)