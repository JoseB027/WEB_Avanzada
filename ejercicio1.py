while True:
    dia = input("Ingrese el dia ('ext'para salir) : ")

    if dia == "ext":
        print("BYE, BYE")
        break

    tiempo = float(input("Ingrese el tiempo estacionado en horas: "))

    if tiempo <= 0:
        print("Error: Tiempo ingresado incorrecto")
    else:
        if dia in ["lunes", "martes", "miercoles"]:
            tarifa = 2.00
        elif dia in ["jueves", "viernes"]:
            tarifa = 2.50
        elif dia in ["sabado", "domingo"]:
            tarifa = 3.00
        else:
            print("El Dia de la semana ingresado es incorrecto")
            continue

        horas = int(tiempo)
        minutos = (tiempo - horas) 

        if minutos >= 0.5:
            horas += 1

        total_pagar = tarifa * horas
        print("El total a pagar es: $", total_pagar)