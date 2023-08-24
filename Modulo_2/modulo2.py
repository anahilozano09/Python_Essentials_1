# Modulo 2
from math import pi
import math

print(-3 ** 2) 
print(-2 ** 3) 
print(-(3 ** 2))
print((-3)**2)


a = 8
b = 5

print(a / b)
print(a // b)
print(a % b)

A = True
c = 10.4
e = "Hola"

print(type(a))
print(type(A))
print(type(c))
print(type(e))

print("El valor de a es ", a, "el tipo es ", type(a))

print("El producto de a=", a, "por b=", b, "es igual a", a*b)
print("El producto de a=", a, "por b=", b, "es igual a", a*b, sep='--', end='**')
print("Otra linea", end='\n')
print("Una linea mas")

print("El valor de a es {a} y el valor de b es {b}")
print(f"El valor de a es {a} y el valor de b es {b}")

v = 16700
s = '100000100111100'
# sistemas numericos
print("El valor binario de ", v, "es", bin(v)[2:])
print(type(bin(v)))
print(int(s, 2))

print("Valor octal",oct(v))
print("Valor octal",oct(v)[2:])

def convetirGradosCentigrados(C):
    F = (1.8*C) + 32
    print(f"{C} oC es equivalente a {F} oF")

try:
    C = float(input('Ingresa los oC:'))
    convetirGradosCentigrados(C)
except ValueError as e:
    print(e)
    print("Se debe ingresar un valor numerico")

print(f"El valor de pi es {pi}")
print(math.ceil(math.pi))
print(math.floor(math.pi))

print(help("keywords"))

"""
comentario multilinea
"""