"""
Necesitamos escribir un programa de cobro en el supermercado. La función debe recibir un número entero que representa el monto a pagar 
y debe permitir al usuario que ingrese valores, hasta que el pago se haya realizado en su totalidad. Además, le debe ir indicando 
cuánto le queda por pagar. El programa no da vuelto.
Ejemplo:

Su total a pagar es: 500
Ingrese el monto a pagar: 100
Pendientes: 400. Ingrese el monto a pagar: 200
Pendientes: 200. Ingrese el monto a pagar: 200
Pendientes: 0. Gracias por su compra.
"""

def cobrar(monto_a_cobrar):
    print("Su total a pagar es:", monto_a_cobrar)
    while monto_a_cobrar > 0:
        pago = int(input(f"Pendientes: {monto_a_cobrar}. Ingrese el monto a pagar: "))
        monto_a_cobrar -= pago
    print("Gracias por su compra.")

cobrar(500)        

"""
Hacer que el programa anterior dé vuelto:
Ejemplo:

Su total a pagar es: 500
Ingrese el monto a pagar: 100
Pendientes: 400. Ingrese el monto a pagar: 200
Pendientes: 200. Ingrese el monto a pagar: 300
Pendientes: 0. Su vuelto es: 100. Gracias por su compra."""

def cobrar_con_vuelto(monto_a_cobrar):
    print("Su total a pagar es:", monto_a_cobrar)
    while monto_a_cobrar > 0:
        pago = int(input(f"Pendientes: {monto_a_cobrar}. Ingrese el monto a pagar: "))
        monto_a_cobrar -= pago
    print(f"Gracias por su compra. Su vuelto es: {abs(monto_a_cobrar)}")    