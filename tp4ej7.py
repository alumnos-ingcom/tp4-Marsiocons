################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

import tp4ej1 as ing

def division_lenta(dividendo, divisor):
    if (divisor == 0):
        raise ing.IngresoIncorrecto("Error! El divisor no puede ser 0!")
    
    if (dividendo < 0):
        dividendo = dividendo * -1
        
    if (divisor < 0):
        divisor = divisor * -1
        
    cociente = 0
    
    while (dividendo > 0):
        dividendo = dividendo - divisor
        if (dividendo > 0):
            cociente = cociente + 1
            resto = dividendo
        elif(dividendo == 0):
            resto = 0
            cociente = cociente +1
        else:
            resto = dividendo + divisor
        resto_cociente = [resto, cociente]
    return resto_cociente
            

# def division_lenta(dividendo, divisor):
#     cociente = 0
#     decimal = False
#     while (dividendo > 0):
#         #print(dividendo)
#         resto = dividendo
#         dividendo = dividendo - divisor
#         if (dividendo > 0):
#             cociente = cociente + 1
#         elif (dividendo == 0):
#             cociente = cociente + 1
#             return print(f"el cociente es {cociente} y tiene resto 0")
#         else:
#             print("entré en el else")
#             decimal = True
#     if (decimal == True):
#         print("entré al decimal")
#         dividendo = resto * 10
#         print(f"el dividendo es {dividendo}")
#         while (dividendo > 0):
#             resto = dividendo
#             dividendo = dividendo - divisor
#             print(f"el dividendo es ahora {dividendo}")
#             if dividendo == 0:
#                 resto = 0
#             cociente = cociente + 0.1
#             
#                 
#             
#     print(f"El cociente de la operación es: {cociente}")
#     print(f"El resto de la operación es: {resto}")
        
        

def prueba():
    num1 = ing.ingreso_entero("Ingrese el dividendo de la operación: ")
    num2 = ing.ingreso_entero("Ingrese el divisor de la operación: ")
    rest_coc = division_lenta(num1, num2)
    print(f"El cociente de la divisón es: {rest_coc[1]}")
    print(f"El resto de la divisón es: {rest_coc[0]}")

if __name__ == "__main__":
    prueba() 