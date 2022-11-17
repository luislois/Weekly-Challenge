'''
 Escribe un programa que muestre por consola (con un print) los
 números de 1 a 100 (ambos incluidos y con un salto de línea entre
 cada impresión), sustituyendo los siguientes:
  - Múltiplos de 3 por la palabra "fizz".
  - Múltiplos de 5 por la palabra "buzz".
  - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 '''
for x in range(1,100):
    divide_3 = x%3
    divide_5 = x%5
    if (divide_3 == 0 & divide_5 == 0):
        print("fizzbuzz")
    elif (divide_3 == 0):
        print("fizz")
    elif (divide_5 == 0):
        print("buzz")
    else:
        print(x)
        
