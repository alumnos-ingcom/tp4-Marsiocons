################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(entrada):
    ingreso = input(f"{entrada} #")
    try:
        salida = int(ingreso)
        return salida
    except ValueError:
        raise IngresoIncorrecto("No se puede transformar.")  


def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    if cantidad_reintentos > 0:
        print(f"{mensaje} Intentos: {cantidad_reintentos}")
        try:
            return (ingreso_entero("Número:"))
        except IngresoIncorrecto:
            cantidad_reintentos = cantidad_reintentos - 1
            ingreso_entero_reintento("Error.", cantidad_reintentos)
    else:
        raise IngresoIncorrecto("Máximos intentos permitidos.")
        
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    if (valor_minimo > valor_maximo or valor_minimo < 0 < valor_maximo):
        raise IngresoIncorrecto("Valor mínimo o máximo incorrectos.")
    print(f"{mensaje} {valor_minimo} y {valor_maximo}")
    numero = ingreso_entero("Ingrese un número:")
    if (numero >= valor_minimo and numero <= valor_maximo):
        return(numero)
    else:
        raise IngresoIncorrecto(f"El número no está entre los valores {valor_minimo} y {valor_maximo}")
    

def prueba():
    #ingreso_entero("Ingrese un número:")
    #ingreso_entero_reintento("Ingrese un número.", 5)
    ingreso_entero_restringido("Ingrese un número entre:", -12, 22)
    
    pass

if __name__ == "__main__":
    prueba()
# 
# 
# class IngresoIncorrecto(Exception):
#     """Esta es la Excepcion para el ingreso incorrecto"""
#     pass 
# 
# def conversion_int(dato, intentos):
#     while intentos > 0:
#         if intentos <= 0:
#             break
#         try:
#             dato_int = int(dato)
#             if ( ingreso_entero_restringido(dato_int) ):
#                 print(f"El número cumple con las características. ( {dato_int} )")
#                 break
#             else:
#                 ingreso_entero_reintento(dato, intentos)
#                 break
#         except ValueError as err:
#             raise IngresoIncorrecto("No se puede transformar")
#             ingreso_entero_reintento(dato, intentos)
#             #print("No se puede transformar")
#             
#             return
# 
# def ingreso_entero_reintento(dato, reintentos):
#     print(f"El dato es inválido: ( {dato} )")
#     print(f"Intentos restantes: {reintentos - 1}")
#     reintentos = reintentos - 1
#     if (reintentos > 0):
#         pedir_dato(reintentos)
# 
# def ingreso_entero_restringido(dato, dato_min=0, dato_max=10):
#     if (dato >= dato_min and dato <= dato_max):
#         return True
#     else:
#         return False
# 
# def pedir_dato(intentos=5):
#     dato_new= input("Ingrese un dato: ")
#     conversion_int(dato_new, intentos)
#     
# 
# def prueba():
#     pedir_dato()
#     pass
# 
# if __name__ == "__main__":
#     prueba()