print("Pregunta 2")

x = 1
x = x == x

print(x)

print("Pregunta 3")

i = 0
while i <= 3 :
    i += 2
    print("*")

print("Pregunta 4")

i = 0
while i <= 5 :
    i += 1
    if i % 2 == 0:
        break
    print("*")

print("Pregunta 5")

for i in range(1):
    print("#")
else:
    print("#")

print("Pregunta 6")

var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

print("Pregunta 7")

var = 1
while var < 10:
    print("#")
    var = var << 1

print("Pregunta 8")

z = 10
y = 0
x = y < z and z > y or y > z and z < y

print(x)

print("Pregunta 9")

a = 1
b = 0
c = a & b
d = a | b
e = a ^ b

print(c + d + e)

print("Pregunta 10")

my_list = [3, 1, -2]
print(my_list[my_list[-1]])

print("Pregunta 11")

my_list = [1, 2, 3, 4]
print(my_list[-3:-2])

print("Pregunta 12")

vals = [0, 1, 2]
vals[0], vals[2] = vals[2], vals[0]

print(vals)

print("Pregunta 13")

vals = [0, 1, 2]
vals.insert(0, 1)
del vals[1]

total = 0

for i in vals:
    total += i
print(total)

print("Pregunta 14")

nums = [1, 2, 3]
vals = nums
del vals[1:2]

print(vals)

print("Pregunta 15")

nums = [1, 2, 3]
vals = nums[-1:-2]

print(vals)

print("Pregunta 16")

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)

print("Pregunta 17")

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

print("Pregunta 18")

my_list = [i for i in range(-1, 2)]

print(len(my_list))

print("Pregunta 19")

t = [[3-i for i in range (3)] for j in range (3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

print("Pregunta 20")

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

