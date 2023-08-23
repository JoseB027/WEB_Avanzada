while True:
    dia = input("Ingrese el día de la semana ('ext'para salir): ")

    if dia == "ext":
        print("¡Hasta luego!")
        break

    tiempo = float(input("Ingrese el tiempo estacionado en horas: "))

    if tiempo <= 0:
        print("Error: Tiempo ingresado incorrecto")
    else:
        if dia in ["lunes", "martes", "miércoles"]:
            tarifa = 2.00
        elif dia in ["jueves", "viernes"]:
            tarifa = 2.50
        elif dia in ["sábado", "domingo"]:
            tarifa = 3.00
        else:
            print("Error: Día de la semana incorrecto")
            continue

        horas = int(tiempo)
        minutos = (tiempo - horas) 

        if minutos >= 0.5:
            horas += 1

        total_pagar = tarifa * horas
        print("El monto a pagar es: $", total_pagar)