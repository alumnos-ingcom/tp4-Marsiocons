################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

## 0C = 32,0F ## |
## 1C = 33,8F ## | Diferencia de
## 2C = 35,6F ## | 1,8F * C



def convertir_a_fahrenheit(centigrados):
    
    """La función hace uso de ing.ingreso_entero() para ingresar un número.
        Retorna la conversión de un número en grados
        centígrados a un número en grados Fahrenheit.
        El parámetro "centígrados" es el número en grados centígrados
        a convertir."""
    
    return (32 + (1.8 * centigrados))
    
    
def convertir_a_centigrados(fahrenheit):
    
    """La función hace uso de ing.ingreso_entero() para ingresar un número.
        Retorna la conversión de un número en grados
        fahrenheit a un número en grados centígrados.
        El parámetro "fahrenheit" es el número en grados fahrenheit
        a convertir."""
    
    return ((fahrenheit - 32)/1.8)


def prueba():
    fah = ing.ingreso_entero("Ingrese un número entero para convertir Fahrenheit a Centígrados")
    print(convertir_a_centigrados(fah))
    cen = ing.ingreso_entero("Ingrese un número entero para convertir Centígrados a Fahrenheit")
    print(convertir_a_fahrenheit(cen))
    pass

if __name__ == "__main__":
    prueba() 