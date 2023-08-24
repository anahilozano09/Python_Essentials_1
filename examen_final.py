print("Pregunta 1")

my_list = [1, 2]

for v in range(2):
    my_list.insert(-1, my_list[v])

print(my_list)
"""
print("Pregunta 5")

def function_1(a):
    return None


def function_2(a):
    return function_1(a) * function_1(a)


print(function_2(2))
"""
print("Pregunta 6")
print(1 // 2)

"""
print("Pregunta 7")

def func(a, b):
    return b ** a


print(func(b=2, 2))

"""

print("Pregunta 8")

z = 0
y = 10
x = y < z and z > y or y < z and z < y

print(x)

print("Pregunta 10")

my_list =  [x * x for x in range(5)]


def fun(lst):
    del lst[lst[2]]
    return lst


print(fun(my_list))

print("Pregunta 11")

x = 1
y = 2
x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)

print("Pregunta 12")

a = 1
b = 0
a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)

print("Pregunta 13")

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2


print(fun(fun(2)))

print("Pregunta 14")

nums = [1, 2, 3]
vals = nums
del vals[:]

print(nums)
print(vals)
"""
print("Pregunta 15")

x = int(input())
y = int(input())
x = x % y
x = x % y
y = y % x
print(y)
"""
"""
print("Pregunta 16")
y = input()
x = input()
print(x + y)
"""

print("Pregunta 17")

print("a", "b", "c", sep="sep")

print("Pregunta 18")

x = 1 // 5 + 1 / 5
print(x)
"""
print("Pregunta 20")

x = float(input())
y = float(input())
print(y ** (1 / x))
"""

print("Pregunta 21")

dct = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dct['three']

for k in range(len(dct)):
    v = dct[v]

print(v)

print("Pregunta 22")

lst = [i for i in range(-1, -2)]
print(lst)
print(len(lst))

print("Pregunta 23")

def fun(a, b, c=0):
    # Cuerpo de la función.
    print(a,b,c, sep=" ")

fun(0, 1, 2)
fun(b=0, a=0)

print("Pregunta 24")

def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)


print(fun(0, 3))

"""

print("Pregunta 25")

i = 0
while i < i + 2 :
    i += 1
    print("*")
else:
    print("*")

"""

print("Pregunta 26")

tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
"""
print("Pregunta 27")

dd = {"1": "0", "0": "1"}
for x in dd.vals():
    print(x, end="")
"""
print("Pregunta 28")

dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)

for x in dct.keys():
    print(dct[x][1], end="")

print("\nPregunta 29")

def fun(inp=2, out=3):
    return inp * out


print(fun(out=2))

print("Pregunta 30")

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")

"""
print("Pregunta 31")

try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")

"""
"""
print("Pregunta 32")

try:
    print(5/0)
    break
except:
    print("Lo siento, algo salió mal...")
except (ValueError, ZeroDivisionError):
    print("Mala suerte...")
"""

print("Pregunta 33")

foo = (1, 2, 3)
foo.index(0)

print("Pregunta 35")

print(¡Hola, Mundo!)


