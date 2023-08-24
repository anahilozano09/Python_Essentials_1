"""
print("Operador igual")

var = 0  # Asignando 0 a var
print(var == 0)

var = 1  # Asignando 1 a var
print(var == 0)

print("Operador no es igual a")

var = 0  # Asignando 0 a var
print(var != 0)
 
var = 1  # Asignando 1 a var
print(var != 0)

print("LAB: Preguntas y Respuestas")

n = int(input("Ingresa un número: "))
print(n>=100)

print("Sentencia if-else")

print("Ejemplo 1")

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)

print("Ejemplo 2")

# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))

# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2

# Imprime el resultado
print("El número más grande es:", larger_number)

print("Ejemplo 3")

# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Asumimos temporalmente que el primer número
# es el más grande.
# Lo verificaremos pronto.
largest_number = number1
 
# Comprobamos si el segundo número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number2 > largest_number:
    largest_number = number2
 
# Comprobamos si el tercer número es más grande que el mayor número actual
# y actualiza el número más grande si es necesario.
if number3 > largest_number:
    largest_number = number3
 
# Imprime el resultado.
print("El número más grande es:", largest_number)
 
print("Ejemplo 4")

# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))
 
# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.
 
largest_number = max(number1, number2, number3)
 
# Imprime el resultado.
print("El número más grande es:", largest_number)

print("LAB: Operadores de comparación y ejecución condicional")

planta = input("Escriba el nombre de una planta: ")
if planta == "ESPATIFILO":
    print('Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!')
elif planta == "espatifilo":
    print('No, ¡quiero un gran Espatifilo!')
elif planta == "Espatifilo":
    print('Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!')
else:
    print('¡Espatifilo!, !No ' + planta + '!')

    
print("LAB: Fundamentos de la sentencia if-else")

income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
else:
	tax = 14839.2 + (income-85528)*0.32

if tax < 0.0:
	tax = 0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

"""

print("LAB: Fundamentos de la sentencia if-elif-else")

year = int(input("Introduce un año: "))

if year < 1582:
	print("No esta dentro del período del calendario Gregoriano")
else:
    #  Escribe el bloque if-elif-elif-else aquí.
    if year%4 != 0.0:
          print("Año común")
    elif year%100 != 0.0:
          print("Año bisiesto")
    elif year%400 != 0.0:
          print("Año común")
    else:
          print("Año bisiesto")