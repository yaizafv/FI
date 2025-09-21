## Encontrar cuál es el mayor de estos números: 2^15, 3^12 y 5^10
# a = 2**15
# b = 3**12
# c = 5**10
# print(max(a,b,c))

## Usando las funciones chr y ord, encuentra cuál es la letra que está 10 posiciones más adelante de la A
# posicionA = ord("A")
# letra = posicionA + 10
# print(chr(letra))


## Usando las funciones chr y hex encuentra cuál es el código binario de la letra 'a' y de la letra 'A' y
## verifica que se diferencian tan solo en un bit
# aM = ord("A")
# print(hex(aM))  # 0100 0001
# a = ord("a")
# print(hex(a))   # 0110 0001


## Escribe una expresión que calcule el resto de dividir 500 entre 7. Comprueba que sale 3
# resto = 500 % 7
# print(resto)


## Escribe un programa que haga salir en pantalla una línea formada por 80 asteriscos
# print("*"*80)


## Calcula la raiz cuadrada de 2 con cinco decimales
# raiz = pow(2, 1/2)
# print(f"{raiz:.5f}")


## ¿Qué crees que debería salir al poner type(1/2)? Comprueba qué sale. Comprueba también 
## el resultado de la operación. ¿Y con type(1//2)? ¿Cuál es la diferencia entre el operador / y el //?
# print(type(1/2))
# print(type(1//2))


## Prepara una variable n con el valor 5. Calcular la raíz n-sima de 2. Debe salir 1.1486983549970351.

n = 5
raiz = pow(2, 1/5)
print(raiz)