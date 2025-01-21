import random

numero_elegido = int(input('Introduzca u número entre 1 y 50: '))
numero_radom = random.randint(1, 50)
while numero_radom != numero_elegido:
    print('El número no es correcto')
    if numero_elegido < numero_radom:
        print('Pista: El número es mayor')
    else:
        print('Pista: El número es menor')
    numero_elegido = int(input('Introduzca u número entre 1 y 50: '))
print('¡Correcto!')
