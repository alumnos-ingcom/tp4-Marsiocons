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
        #raise IngresoIncorrecto("No se puede transformar.")  
        ingreso_entero_reintento("Error. Reintente.", intento-1)
        

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    print(f"{mensaje} Intentos: {cantidad_reintentos}")
    if cantidad_reintentos > 0:
        print(ingreso_entero("Número:"))
    else:
        raise IngresoIncorrecto("Máximos intentos permitidos..")
        
        
 
def prueba():
    ingreso_entero("Ingrese un número:")
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