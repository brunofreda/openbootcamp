# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.


def main():

    f = open("file.txt", "a")
    f.write("Text 1\n")
    f.close()

    f = open("file.txt", "a")
    f.write("Text 2\n")
    f.close()


if __name__ == "__main__":
    main()