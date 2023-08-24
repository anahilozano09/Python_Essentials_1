print("Uso del ciclo for")
"""
print("Ejemplo 1")

for i in range(10):
    print("El valor de i es", i)

print("Ejemplo 2")
# usando range con 2 argumentos
for i in range(2, 8):
    print("El valor de i es", i)

print("Ejemplo 3")
#usando range con 3 argumetos
for i in range(2, 8, 3):
    print("El valor de i es", i)

print("Programa que imprime unas potencias del 2")

power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2

print("LAB: Fundamentos del bucle for contando lentamente (mississippily)")

import time

# Escribe un bucle for que cuente hasta cinco.
for i in range(1,6):
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    print(str(i) + " Mississippi")
    # Cuerpo del bucle, emplea : time.sleep(1)
    time.sleep(1)
# Escribe una función print con el mensaje final.
print("¡Listos o no, ahí voy!")

"""

print("Uso de la sentencia break y continue")
"""
print("Ejemplo 1")
# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

print("Ejemplo 2.1: variante con break")

largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")


print("Ejemplo 2.2: variante con continue")

largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")

"""

print("LAB: La sentencia break atrapado en un bucle")
"""
print("Con continue")

secret_word = "chupacabras"

counter = 0

palabra = input("Escriba una palabra: ")

while palabra != secret_word:
    if palabra == secret_word:
        continue
    counter += 1
    
    palabra = input("Ingrese otra palabra: ")

print("Has dejado el bucle con exito")


secret_word = "chupacabras"

while True:

    palabra = input("Ingrese una palabra: ")

    if palabra == secret_word:
        break

print("Has dejado el bucle con éxito")

"""

#print("LAB: La sentencia continue el Feo Devorador de Vocales")
"""
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

for letter in user_word:
    # Completa el cuerpo del bucle for.

"""
#print("LAB: La sentencia continue el Lindo Devorador de Vocales")
"""
word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.


for letter in user_word:
    # Completa el cuerpo del bucle.

# Imprimir la palabra asignada a word_without_vowels.

"""

#print("Sentencia while else")

"""
print("Ejemplo 1")

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)


print("Ejemplo 1.1")

i = 5
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)

"""

#print("Bucle for else")

"""

print("Ejemplo 1")

for i in range(5):
    print(i)
else:
    print("else:", i)


print("Ejemplo 1.2")

i = 111
for i in range(2, 1):
    print(i)
else:
    print("else:", i)

"""

#print("LAB: Fundamentos del bucle while")

"""
blocks = int(input("Ingresa el número de bloques: "))

#
# Escribe tu código aquí.
#	

print("La altura de la pirámide:", height)

"""

#print("LAB: La hipótesis de Collatz")

