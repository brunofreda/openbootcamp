class Vehiculo:
    color = "Negro"
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 200
    cilindrada = 4100

coche_1 = Coche()

print("coche_1 es de color ", coche_1.color.lower(), ", tiene ", coche_1.ruedas, " ruedas, ", coche_1.puertas, " puertas, una velocidad de ", coche_1.velocidad, " km por hora y una cilindrada de ", coche_1.cilindrada, " cc.", sep="")