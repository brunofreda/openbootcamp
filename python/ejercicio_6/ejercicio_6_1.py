# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#
# -Color
# -Ruedas
# -Puertas
#
# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#
# -Velocidad
# -Cilindrada
#
# Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self):
        vehiculo = self.color + ", " + str(self.ruedas) + ", " + str(self.puertas)
        return vehiculo

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        vehiculo = self.color + ", " + str(self.ruedas) + ", " + str(self.puertas) + ", " + str(self.velocidad) + ", " + str(self.cilindrada) 
        return vehiculo

coche_1 = Coche("Negro", 4, 4, 200, 4100)

print(coche_1)