################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(entrada):
    """La función intenta transformar lo que el usuario ingrese
        en un número entero. Si no lo logra se ejecuta la excepción
        IngresoIncorrecto.
        El parámetro "entrada" es el mensaje que acompaña al ingreso de un número"""
    
    ingreso = input(f"{entrada} #")
    try:
        salida = int(ingreso)
        return salida
    except ValueError as err:
        raise IngresoIncorrecto("No se puede transformar.") from err  

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """La función hace uso de ingreso_entero() para intentar
        retornar un número x cantidad de veces.
        Al superar los intentos, ejecuta la excepción IngresoIncorrecto.
        El parámetro "mensaje" es el mensaje que acompaña al ingreso
        de un número.
        El parámetro "cantidad_reintentos" es la cantidad de intentos
        que hay para retornar un número."""
    
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
    """La función hace uso de ingreso_entero() para retonar el número
        si y sólo si se encuentra dentro de los valores mínimos y máximos.
        Si el número no está dentro de dichos valores, ejecuta la excepción
        IngresoIncorrecto.
        Si el valor mínimo es mayor que el valor máximo, ejecuta la
        excepción IngresoIncorrecto.
        Si el valor mínimo es igual al máximo, ejecuta la excepción
        IngresoIncorrecto.
        El parámetro "mensaje" es el mensaje que acompaña al ingreso de un número.
        El parámetro "valor_minimo" es el valor mínimo que puede adoptar
        el número ingresado.
        El parámetro "valor_maximo" es el valor máximo que puede adoptar
        el número ingresado.
    """
    
    if (valor_minimo > valor_maximo or valor_minimo == valor_maximo):
        raise IngresoIncorrecto("Valor mínimo o máximo incorrectos.")
    print(f"{mensaje} {valor_minimo} y {valor_maximo}")
    numero = ingreso_entero("Ingrese un número:")
    if (numero >= valor_minimo and numero <= valor_maximo):
        return(numero)
    else:
        raise IngresoIncorrecto(f"El número no está entre los valores {valor_minimo} y {valor_maximo}")
    
def prueba():
    print(ingreso_entero("Ingrese un número:"))
    #print(ingreso_entero_reintento("Ingrese un número.", 5))
    #print(ingreso_entero_restringido("Ingrese un número entre:", -23, 22))

if __name__ == "__main__":
    prueba()
