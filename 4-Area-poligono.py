'''
 * Reto #4
 * ÁREA DE UN POLÍGONO
 * Fecha publicación enunciado: 24/01/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
'''

def area_poligono(poligono,base,altura):
    match poligono:
        case "cuadrado":
            print(base ** 2)
        case "triangulo":
            print(base * altura / 2)
        case "rectangulo":
            print(base * altura)    


area_poligono("cuadrado", 2, 2)
area_poligono("triangulo", 2.5, 3.5)
area_poligono("rectangulo", 7, 4.5)

