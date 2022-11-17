def menu():
    print("Adivina un numero")
    print("Primer nivel\nSegundo nivel\nTercer nivel\nCuarto nivel")
    nivel = input("Ingresa el nivel que quieres: ")
    print(nivel)
    if nivel == "Primer nivel":
        juego1(0,100, na = numeroaleatorio (0,100))
    elif nivel == "Segundo nivel":
        juego1(0,1000, na = numeroaleatorio (0,1000))
    elif nivel == "Tercer nivel":
        juego1(0,10000, na = numeroaleatorio (0,10000))
    elif nivel == "Cuarto nivel":
        juego1(0,100000, na = numeroaleatorio (0,100000))
    else:
        return menu()
def numeroaleatorio(minimo, maximo):
    import random
    na = random.randint(minimo, maximo)
    return na
def juego1(minimo, maximo, na):
    numero = input("Ingresar un número entre", + str(minimo) + "y" + str(maximo) + ": ")
    numero = int(numero)
    print(numero)
    while True:
        if numero == na:
            print("Ganaste")
            ayuda+=1
        elif numero > na:
            print("El número es más pequeño")
            ayuda+=1
            if ayuda == 3:
                cuestion(minimo, maximo,na)
        elif numero < na:
            print("El número es más grande")
            ayuda+=1
            if ayuda == 3:
                cuestion(minimo, maximo, na)
        else:
            return juego1(minimo, maximo, na)
def cuestion(minimo, maximo, na):
    print("Necesitas ayuda?")
    respuesta = input("Necesitas ayuda?")
    if respuesta == "si":
        print("El número está aproximadamente entre", minimo, "y", maximo)
    elif respuesta == "no":
        print("Te quedas sin ella")
        return juego1(minimo, maximo, na)
    else:
        return cuestion(minimo, maximo, na)


menu()