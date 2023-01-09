# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.  Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = None
    nota = None

    def ingresar_nombre(self, nombre):
        self.nombre = nombre
    
    def ingresar_nota(self, nota):
        self.nota = nota

    def imprimir_aprobo(self):
        if self.nota >= 7:
            print(self.nombre, " se sacó un ", self.nota, ", por lo que aprobó", sep="")
        else:
            print(self.nombre, " se sacó un ", self.nota, ", por lo que no aprobó", sep="")

alumno_1 = Alumno()

alumno_1.ingresar_nombre(input("Ingrese el nombre del alumno: "))
alumno_1.ingresar_nota(int(input("Ingrese la nota del alumno: ")))
alumno_1.imprimir_aprobo()