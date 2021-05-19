################
# Marcio Betanzo - @marsiocons
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    resultado = numero + otro_numero
    print(resultado)
    while numero != resultado:
        print(numero)
        numero = numero + 1

def prueba():
    suma_lenta(12,2)
    pass

if __name__ == "__main__":
    prueba() 