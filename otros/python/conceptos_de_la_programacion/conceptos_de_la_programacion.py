# Hello world

""" msg = "Hello world"
print(msg) """

# Secuencia de fibonnacci del número n

""" def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
a = input("Escriba el número para el cual quiere calcular su secuencia de fibonacci: ")
fib(int(a)) """

# Standard plot

""" import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() """

# Pasar datos de una lista a otra vacía

""" lista_programadores = ["Gorka", "Martin", ["Alex", "Leire"]]

nombres = []
print(nombres)

# for x in lista_programadores:
#     nombres.append(x)

# nombres = lista_programadores.copy()

# nombres = lista_programadores[:]

# nombres = list(lista_programadores)

# import copy
# nombres = copy.copy(lista_programadores)
# nombres = copy.deepcopy(lista_programadores)

print(lista_programadores)
print(nombres) """

# Suma de los diez primeros enteros

""" # suma = 0
# for x in range(11):
#    suma += x

def diez_enteros():
    suma = 0
    for x in range(11):
        suma += x
    return suma

suma = diez_enteros()

print(suma)
# print(range(10)) """

# Funciones puras e impuras

""" # def suma(num1, num2):
#    return num1 + num2

total = 0
def suma(num1, num2):
    global total
    total += num1 + num2
    return total

print(suma(3, 8))
print(suma(3, 8))
print(suma(3, 8))
print(suma(3, 8)) """

# Funciones no recursivas y recursivas

""" # def factorial(num):
#     total = 1
#     for x in range(1, num + 1):
#         total = total * x
#     return total

# def factorial(num):
#      total = num
#      for x in range(num-1, 1, -1):
#          total = total * x
#      return total

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

# def factorial(num):
#     return num * factorial(num - 1)

print(factorial(5)) """

""" # def suma(a, b):
#     resultado = a + b
#     print(resultado)
#     return suma(a, b)

def suma(a, b):
    resultado = a + b
    print(resultado)
    return suma(a, resultado)
    
suma(1, 2) """

# Funciones que usan funciones

""" def suma(num1, num2):
    return num1 + num2

def multiplica(num1, num2):
    return num1 * num2

def suma_y_multiplica(num1, num2):
    return suma(num1, num2) * multiplica(num1, num2)

print(suma(1, 4))
print(multiplica(1, 4))
print(suma_y_multiplica(1, 4)) """