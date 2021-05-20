################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

## 0C = 32,0F ## |
## 1C = 33,8F ## | Diferencia de
## 2C = 35,6F ## | 1,8F * C



def convertir_a_fahrrenheit(centigrados):
    return (32 + (1.8 * centigrados))
    
    
def convertir_a_centigrados(fahrenheit):
    return ((fahrenheit - 32)/1.8)


def prueba():
    fah = ing.ingreso_entero("Ingrese un número entero para convertir Fahrenheit a Centígrados")
    print(convertir_a_centigrados(fah))
    cen = ing.ingreso_entero("Ingrese un número entero para convertir Centígrados a Fahrenheit")
    print(convertir_a_fahrrenheit(cen))
    pass

if __name__ == "__main__":
    prueba() 