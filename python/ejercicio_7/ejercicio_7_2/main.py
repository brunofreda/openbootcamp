# En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.  Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#
# En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.

import time as t


def main():
    
    if t.localtime().tm_hour > 7:
        print("Es hora de ir a casa.")
    else:
        t_actual_list = t.ctime().split()

        t_actual_list[3] = "07:00:00"
        if len(t_actual_list[2]) == 1:
            t_actual_list[2] = " " + t_actual_list[2]

        t_7_string = ' '.join(t_actual_list)

        t_7_struct = t.strptime(t_7_string)

        t_7_secs = t.mktime(t_7_struct)

        dif_tiempo_secs = t_7_secs - t.mktime(t.localtime())

        dif_tiempo_struct = t.gmtime(dif_tiempo_secs)

        if dif_tiempo_struct[3] == 1:
            if dif_tiempo_struct[4] == 1:
                print("Queda", dif_tiempo_struct[3], "hora y", dif_tiempo_struct[4], "minuto de trabajo.")
            else:
                print("Queda", dif_tiempo_struct[3], "hora y", dif_tiempo_struct[4], "minutos de trabajo.")
        else:
            if dif_tiempo_struct[4] == 1:
                print("Quedan", dif_tiempo_struct[3], "horas y", dif_tiempo_struct[4], "minuto de trabajo.")
            else:
                print("Quedan", dif_tiempo_struct[3], "horas y", dif_tiempo_struct[4], "minutos de trabajo.")

                

if __name__ == "__main__":
    main()