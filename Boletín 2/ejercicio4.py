pass1 = input('Introduzca la contraseña: ')
pass2 = input('Repita la contraseña: ')
acumulador = 1
while pass1 != pass2 and acumulador < 3:
    pass1 = input('Introduzca la contraseña '+ str(3-acumulador)+' intentos restantes: ')
    pass2 = input('Repita la contraseña: ')
    acumulador += 1
if pass1 != pass2:
    print('Lo siento alcanzo el número máximo de veces')
else:
    print('Las contraseñas coindicen')