import random

numero_random = random.randint(0, 100)
numero_user = None
print("--- J U E G O  D E  A D I V I N A R --- \n ")
while (numero_user != numero_random):
    
    
    
    try:
        numero_user = int(input("Introduce un numero: "))
        assert numero_user == numero_random
        print("Felicidades, has acertado")
    except AssertionError:
       if numero_user < numero_random:
           print("ErrorEnterDemasiadoPequeño")
       if numero_user > numero_random:
           print("ErrorEnterDemasiadoGrande")
    except ValueError:
        print("ErrorNoEsEntero")
