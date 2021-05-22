################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def suma_lenta(numero, otro_numero):
    """La función hace uso de ing.ingreso_entero() (función importada
    de tp4eje1) para ingresar dos números y hacer una suma/resta
    entre ellos.
    Retorna el resultado de dicha operación.
    El parámetro "numero" es el primer número (base de la operación).
    El parámetro "otro_numero" es el número que se le va a
    restar/sumar al primer número."""
    
    resultado = numero + otro_numero
    
    #### si ambos números son positivos ####
    if (numero >= 0 <= otro_numero):
        while numero <= resultado:
            numero = numero + 1
            
    #### si el primer número es positivo y el segundo negativo ####
    if (numero >= 0 > otro_numero):
        while numero >= resultado:
            numero = numero - 1
            
    #### si el primer número es negativo y el segundo positivo ####
    if (numero < 0 <= otro_numero):
        while numero <= resultado:
            numero = numero + 1
            
    #### si ambos números son negativos ####
    if (numero < 0 > otro_numero):
        while numero >= resultado:
            numero = numero - 1
            
    return resultado

def prueba():
    num1 = ing.ingreso_entero("Ingrese un número:")
    num2 = ing.ingreso_entero("Ingrese un número:")
    print(f"La suma lenta ({num1} +- 1) de {num1} y {num2} es: {suma_lenta(num1,num2)}")

if __name__ == "__main__":
    prueba() 