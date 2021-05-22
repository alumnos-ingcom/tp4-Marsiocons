################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
import tp4ej1 as ing

def maximo(lista):
    numero = lista[0]
    for i in range(len(lista)):
        if (numero < lista[i]):
            numero = lista[i]
    return numero

def minimo(lista):
    numero = lista[0]
    for i in range(len(lista)):
        if (numero > lista[i]):
            numero = lista[i]
    return numero

def crear_lista():
    cant = ing.ingreso_entero("Cuántos números desea guardar en la lista?")
    if (cant < 1):
        raise ing.IngresoIncorrecto("La cantidad de números no puede ser menor a 1!")
    lista = []
    for i in range(cant):
        numero_nuevo = ing.ingreso_entero("Ingrese un número para agregar a la lista:")
        lista.append(numero_nuevo)
    return lista

def prueba():
    lista = crear_lista()
    print(f"El número más grande de {lista} es:")
    print (maximo(lista))
    print(f"El número más chico de {lista} es:")
    print(minimo(lista))

if __name__ == "__main__":
    prueba() 