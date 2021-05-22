################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def compara(numero, otro_numero):
    """La función retorna 0 si los números son iguales.
        Retorna 1 si el primer número es mayor al segundo.
        Y retorna -1 si el segundo número es mayor al primero."""
    
    if (numero == otro_numero):
        return 0
    if (numero > otro_numero):
        return 1
    if (numero < otro_numero):
        return -1

def prueba():
    num1 = ing.ingreso_entero("Ingrese el primer número a comparar:")
    num2 = ing.ingreso_entero("Ingrese el segundo número a comparar:")
    print(compara(num1,num2))

if __name__ == "__main__":
    prueba() 