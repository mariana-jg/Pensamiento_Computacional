"""
a) Escribir un programa que contenga una contraseña inventada, 
que le pregunte al usuario la contraseña, y no le permita continuar hasta que la haya ingresado correctamente.
b) Modificar el programa anterior para que solamente permita una cantidad fija de intentos.
c) Modificar el programa anterior para que sea una función que devuelva si el usuario ingresó o no 
la contraseña correctamente, mediante un valor booleano (True o False).
"""

def login():
    contraseña = "hola1234"
    ingreso = input("Ingrese su contraseña: ")
    while ingreso != contraseña:
        print("Error!")
        ingreso = input("Ingrese su contraseña: ")
    print("Ingreso exitoso") 

def login_con_intentos(intentos):
    contrasenia = "1234"
    ingreso = input("Ingrese su contrasenia: ")
    intentos -= 1
    while ingreso != contrasenia and intentos > 0:
        print("Error!")
        ingreso = input("Ingrese su contraseña: ")
        intentos -= 1

    if ingreso == contrasenia:
        print("Ingreso exitoso!")
    else:
        print("Agotaste todos los intentos")

def login_exitoso(intentos):
    contrasenia = "1234"
    ingreso = input("Ingrese su contrasenia: ")
    intentos -= 1
    while ingreso != contrasenia and intentos > 0:
        print("Error!")
        ingreso = input("Ingrese su contraseña: ")
        intentos -= 1    
    return contrasenia == ingreso

print(login_exitoso(4))            

