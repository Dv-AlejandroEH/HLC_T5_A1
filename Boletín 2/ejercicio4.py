pass1 = input('Introduzca la contraseña')
pass2 = input('Repita la contraseña')
acumulador = 0
while pass1 != pass2 and acumulador == 3:
    pass1 = input('Introduzca la contraseña')
    pass2 = input('Repita la contraseña')
    acumulador++