import random

numero_random = random.randint(0, 100)
numero_user = input("Introduzca un numero: ")

if not (numero_user.isdigit()):
    print("ErrorNoEsEntero")
else:
    numero_user = int(numero_user) 

    if numero_user > 100:
        print("ErrorEnteroDemasiadoGrande")
    elif numero_user < 0:
        print("ErrorEnteroDemasiadoPequeño")
    elif numero_user == numero_random:
        print("Felicidades, has acertado")
    else:
        print("No has acertado, el número era ", numero_random)
