# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(año):
    if ((año % 4 == 0) and (año % 100 != 00)) or (año % 400 == 0):
        print(año, "es un año bisiesto")
    else:
        print(año, "no es un año bisiesto")

bisiesto(4)
bisiesto(100)
bisiesto(400)
bisiesto(1900)
bisiesto(2000)

# Output:
#   4 es un año bisiesto
#   100 no es un año bisiesto
#   400 es un año bisiesto
#   1900 no es un año bisiesto
#   2000 es un año bisiesto