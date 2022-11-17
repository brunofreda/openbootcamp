# Dos print distintos en una misma línea

""" print(10, end=' ')
print(20) """

# Cambios de valores, print y type

""" x = 1
print(x)
print(type(x))

x = "hello"
print(x)
print(type(x)) """

# Límites de int

""" x = str("a")
y = int(12474836484444444444444)
print(x)
print(y + 1)
print(type(y)) """

# Límites de int y float

""" import sys

i = sys.maxsize
print(i)
print(i == i + 1)
i += 1
print(i)

f = sys.float_info.max
print(f)
print(f == f + 1)
f += 1
print(f) """

# Booleanos

""" x = 1 == 1
print(x)
print(x == True)
# print(x == true)
x == True """

# Arrays/lists y escapes

""" x = [1, 2, 3]
print(x)
print(type(x))

y = [1, "perro"]
print(y)
print(type(y))

z = [1, ["perro", 'a']]
print(z)

w = "This is my \"room\""
print(w)

q = [3, 2, 1]
print(x == q) """

# Tuplas

""" e = ("a", "b", "c")
print(e)
print(type(e))

r = ("b", "a", "c")
print (e == r)

f = "a", "b", 1
print(f)
print(type(f))

d = ()
print(type(d)) """

# Diccionarios

""" nombres_1 = {
    "Bruno": "Freda",
    "María": "Makokdjian"
}

nombres_2 = {
    "María": "Makokdjian",
    "Bruno": "Freda"
}

print(nombres_1 == nombres_2)

print(nombres_1["Bruno"])

print(nombres_1)

# print(nombres_1["Mariano"])

nombres_1["Mariano"] = "Santos"

print(nombres_1["Mariano"])

# print(nombres_1[0])

nombres_3 = {}
print(type(nombres_3)) """

# Clases y objetos

""" class RandomClass:
    x = 5

y = RandomClass()
# print(y)
print(y.x) """

# Clases, objetos y métodos

""" class User:
    def __init__(self, user, password):
        self.perro = user
        self.password = password
        self.species = "Human"

    def method_1(self, personality):
        print(self.perro + " es un " + personality)

    def method_2(self, newUser):
        self.perro = newUser

p1 = User("Usuario1", "1234")
p1.method_1("estúpido")
p1.method_2("Usuario2")
User("Usuario1", "1234").method_1("salvaje")

print(p1.perro, end="\n\n")
print(p1.password)
print(p1.species) """

# Len

""" x = "Bruno"

print(len(x)) """

# Funciones

""" def my_function(message):
    print("Hello from a " + message)

my_function("computer")

def my_new_function(fname):
    print(fname + " Refsnes")

my_new_function("Bruno")
my_new_function("Pedro")
my_new_function("Mariano") """

# Funciones y diferentes tipos de parámetros

""" # def suma(a, b):
#     print(a + b)

# def suma(a, b):
#     print(str(a) + b)

# suma(1, 2)
# suma(1, b)
# suma(1, "b")
# suma(str(1), "b")
# suma("a", "b")
# print(suma(1, 2))
# l = suma(1, 2)
# print(l) """

# Pass

""" def function_name():
    pass

function_name("dog") """

# Print y return

""" # def function_that_prints():
#    print("I printed")

# def function_that_returns():
#    return "I returned"

# f1 = function_that_prints()
# f2 = function_that_returns()
# print("Now let us see what the values of f1 and f2 are")
# print(f1)
# print(f2) """

# Funciones, print y return

""" def multiplicacion(a, b):
    a * b

def multiplicacion_return(a, b):
    return a * b

def multiplicacion_print(a, b):
    print(a * b)

def test_funciones(a, b, c):
    c(a, b)
    print(c(a, b))

    z = c(a, b)
    z
    print(z)

    y = c
    y
    y(a, b)

    print("")

test_funciones(2, 3, multiplicacion)
test_funciones(2, 3, multiplicacion_return)
test_funciones(2, 3, multiplicacion_print)

# x = multiplicacion_print
# x
# x(2, 3)
#
# y = multiplicacion_print(2, 3)
# y
# # y(2, 3) """

# Más print y return

""" a = 2
def funcion(a, b):
    print(a + b)
    return a * b

print(funcion(3, 3))

print(a) """

# Otros

""" # nombres = 1
# nombres = "perro"
# nombres = "11"

print(type(nombres))
# print(nombres + "11")
# print(11 + nombres)
# print(11 + "11")
print(str(11) + "11")
print(11 + 11) """

# Input

""" a = input("Escriba su edad: ")
b = input("Descríbase: ")
print("Me voy a recibir a los", int(a) + 5, "años y soy", b)
print(type(a))
print(type(b)) """

# Parámetros de distinto tipo y linebreak

""" def funcion(a, b):
    print("Me voy a recibir a los", a + 5, "años y soy", b)
    print(type(a), "\n", type(b))
    print("a\nb")

funcion(30, "inteligente") """

# Paso de parámetros por valor y por referencia

""" var1, var2, var3 = 2, 3, 2

def funcion(a, b):
    a = 3
    return a + b

# print(funcion(2, 3))
print(funcion(var1, var2))
print(var1) """

""" def set_list(list):
    list = ["A", "B", "C"]
    return list

def add(list):
    list.append("D")
    return list

my_list = ["E"]

print(my_list)
print(set_list(my_list))
print(my_list)
print(add(my_list))
print(my_list) """

""" class Clase:
    def __init__(self, numero):
        self.num = numero

    # def metodo(self):
    #     self.num + 2

    # def metodo(self):
    #     return self.num + 2
    
    def metodo(self):
        self.num += 2

    # def metodo(self):
    #     return self.num
    #     self.num += 2

    # def metodo(self):
    #     self.num += 2
    #     return self.num
    #     # return 2 + 2

objeto = Clase(3)
print(objeto.num)
print(objeto.metodo())
print(objeto.num) """

# Múltiples líneas con un solo print

""" a = """
# 10
# 20
# 30
"""
print(a)

b = 10
for x in range(3):
    print(b)
    # b += 10

c, d = 10, 30
print("\n", c, "\n", d)

import os
print(f"c{os.linesep}d")
print(c, d, sep=os.linesep)

print("-"*30, "\nblablabla\n", "-"*30)
print('-'*30,'\nblablabla\n','-'*30)

print(f"{10}\n{20}")

print("perro\n", "gato", sep="")
print("perro", "\ngato", sep="")
print(10, "\n", 20, sep="")

print("perro", "gato", sep="")
print("perro", "gato", sep="", end="\n")
print("perro", "gato", end="") """

# Callback

""" def suma(a, b):
    return a + b

variable = suma
# variable = suma()

print(variable(1, 2)) """

# Ejercicios Tema 3

# # Primera parte:
# # Crear una función con tres parámetros que sean números que se suman entre sí.
# # Llamar a la función en el main y darle valores.

# # Segunda parte:
# # Crear una clase coche.
# # Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
# # Una función que incremente el número de puertas que tiene el coche.
# # Crear un objeto miCoche en el main y añadirle una puerta.
# # Mostrar el número de puertas que tiene el objeto.

""" def suma(num1, num2, num3):
    return num1 + num2 + num3

class Coche:
    def __init__(self, puerta):
        self.puertas = puerta
        
    def aumentar_puertas(self):
        self.puertas += 1

resultado = suma(1, 2, 3)
print(resultado)

mi_coche = Coche(2)
mi_coche.aumentar_puertas()
print(mi_coche.puertas) """

# Operadores lógicos y de comparación

""" print(2 > 1)
print(2 < 1)
print((2 > 1) and (1 < 2))
print((2 > 1) or (1 < 2)) """

# Condicionales

""" estacion = "Verano"
temperatura = 21

if estacion == "Verano" and temperatura > 20:
    print("Tomá agua y prendé el aire acondicionado")
elif estacion == "Verano":
    print("Tomá agua")
else:
    print("Llevá abrigo") """