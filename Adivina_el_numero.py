#importar un modulo de pythion
import random

#la x es el intervalo superior del numero aleatorio
def adivina_el_numero(x):
    #mensaje de bienvenida
    msn = '''=============================
    Bienvenido al Juego    
    ===================
    Tumeta es adivinar el numero generado por la PC'''
    print(msn)
    #rand = aleatorio int= numero entero randint(a=rango minimo, b=rango maximo)
    numero_aleatorio = random.randint(1, x)
    #para garantizar que la primera ronda nunca se de el mismo numero 
    prediccion = 0

    #no se tiene un numero de iteraciones especifico
    while prediccion != numero_aleatorio:
        #cadena de caracteres f-string para la captura del mensage
        #se parcea el valor ingresado para que sea un numero int(input())
        # x es un parametro de la funcion que cambia en cada iteraciòn 
        prediccion = int(input(f"Adivina un numero entre 1 y {x}: "))
        #manejo de prediccion superior o inferior
        if prediccion < numero_aleatorio:
            print("El numero es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("El numero es muy grande.")
    #cuando se adivina el numero    
    print(f"Felicitaciones adivinaste el numero {numero_aleatorio} correctamente")

#realizamos la llamada a la funcion
adivina_el_numero(10)
