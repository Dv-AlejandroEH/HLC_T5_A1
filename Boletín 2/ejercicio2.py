num1 = int(input('Introduzca el primer número: '))
num2 = int(input('Introduzca el segundo número: '))
num3 = int(input('Introduzca el tercer número: '))
if num1 > num2 and num1 > num3:
    cadena = 'El primer número', num1, 'es mayor que el segundo y tercer número'
    if num2 > num3:
        cadena += 'y el segundo número', num2, 'es mayor que el tercer número', num3
    else:
        cadena += 'y el tercer número', num3, 'es mayor que el segundo número', num2
elif num2 > num1 and num2 > num3:
    cadena = 'El segundo número', num2, 'es mayor que el primer y tercer número'
    if num1 > num3:
        cadena += 'y el primer número', num1, 'es mayor que el tercer número', num3
    else:
        cadena += 'y el tercer número', num3, 'es mayor que el primer número', num1
else:
    cadena = 'El tercer número', num3, 'es mayor que el primer y segundo número'
    if num1 > num2:
        cadena += 'y el primer número', num1, 'es mayor que el segundo número', num2
    else:
        cadena += 'y el segundo número', num2, 'es mayor que el primer número', num1
if num1 == num2 or num1 == num3 or num2 == num3:
    print('Dos o más números son iguales')
else:
    print(cadena)