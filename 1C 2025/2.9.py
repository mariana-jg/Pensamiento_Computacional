# Crear una función que reciba un número y que devuelva True si es par, y False si es impar.

def resto_dos(numero):
    return numero % 2

def es_par(numero):
    return resto_dos(numero) == 0

print(es_par(78))