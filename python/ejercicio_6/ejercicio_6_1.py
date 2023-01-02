# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# -Color
# -Ruedas
# -Puertas
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# -Velocidad
# -Cilindrada
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = "Negro"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 200
    cilindrada = 4100

coche_1 = Coche()

print("coche_1 es de color ", coche_1.color.lower(), ", tiene ", coche_1.ruedas, " ruedas, ", coche_1.puertas, " puertas, una velocidad de ", coche_1.velocidad, " km por hora y una cilindrada de ", coche_1.cilindrada, " cc.", sep="")