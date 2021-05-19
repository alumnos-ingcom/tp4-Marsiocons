################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def suma_lenta(numero, otro_numero):
    resultado = numero + otro_numero
    
    #### si ambos números son positivos ####
    if (numero >= 0 <= otro_numero):
        while numero <= resultado:
            print(numero)
            numero = numero + 1
            
    #### si el primer número es positivo y el segundo negativo ####
    if (numero >= 0 > otro_numero):
        while numero >= resultado:
            print(numero)
            numero = numero - 1
            
    #### si el primer número es negativo y el segundo positivo ####
    if (numero < 0 <= otro_numero):
        while numero <= resultado:
            print(numero)
            numero = numero + 1
            
    #### si ambos números son negativos ####
    if (numero < 0 > otro_numero):
        while numero >= resultado:
            print(numero)
            numero = numero - 1

def prueba():
    num1 = ing.ingreso_entero("Ingrese un número:")
    num2 = ing.ingreso_entero("Ingrese un número:")
    suma_lenta(num1, num2)
    pass

if __name__ == "__main__":
    prueba() 