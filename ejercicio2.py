opcion=0;
while(opcion != 3):
    print("******MENU CALCULO DE AREA********")
    print("1)Calcular area de un circulo")
    print("2)Calcular area de un triangulo")
    print("3)Salir.")
    opcion = int(input("'Ingrese la opcion :"))
    if opcion == 1:
        radio=float(input("Ingrese el radio del circulo que desea calcular su area: "))
        resultado= 3.1416 * (radio *radio)
        print("El Area del cierculo es :",resultado,"m2")
    elif opcion == 2:
        base=float(input("Ingrese la base del triangulo que desea calcular su area: "))
        altura = float(input("Ingrese la altura del triangulo que desea calcular su area: "))

        resultado= (base * altura) / 2
        print("El Area del triangulo es :",resultado,"m2")
    elif opcion == 3:
        print("Adios!!!")
    else:
        print("Opcion incorrecta")

