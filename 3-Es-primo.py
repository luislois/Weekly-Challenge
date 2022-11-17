'''
 * Reto #3
 * ¿ES UN NÚMERO PRIMO?
 * Fecha publicación enunciado: 17/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 '''

def esPrimo (num):
    if (num < 2):
        return False
    else:
        for i in range(2 , num):
            if (num % i != 0):
                return False

        return True

