# En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

# Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

import operaciones as o


def main():
    
    suma = o.sumar(4, 2)
    resta = o.restar(4, 2)
    multiplicacion = o.multiplicar(4, 2)
    division = o.dividir(4, 2)

    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)



if __name__ == "__main__":
    main()

