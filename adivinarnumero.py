def menu():
    print("Adivina un numero")
    print("Nivel1\nNivel2\nNivel3\nNivel4")
    nivel = input("Ingresa el nivel: ")
    print(nivel)
    if nivel== "Nivel1":
        juego1(0,100)
    elif nivel == "Nivel2":
        juego1(0,1000)
    elif nivel == "Nivel3":
        juego1(0,10000)
    elif nivel == "Nivel4":
        juego1(0,100000)
    else:
        return menu()
def numeroaleatorio(minimo, maximo):
    import random
    numeroaleatorio = random.randint(minimo, maximo)
    return numeroaleatorio
def juego1(minimo, maximo):
    naleatorio = numeroaleatorio(minimo, maximo)
    print(naleatorio)
    numero = input()


menu()