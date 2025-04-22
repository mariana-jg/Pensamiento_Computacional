# Escribir una función que, dado un número entero n, calcule si es impar o no.

def es_par(numero):
    return numero % 2 == 0

def es_par_con_ifs(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
