# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

    
class Vehiculo:
    ruedas = 4

vehiculo_1 = Vehiculo()

f = open("vehiculo.bin", "wb")
pickle.dump(vehiculo_1, f)
f.close()

g = open("vehiculo.bin", "rb")
v_1 = pickle.load(g)
g.close()