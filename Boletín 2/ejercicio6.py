palabra = input('Introduzca una palabra: ')
caracteres = ['@', '#', '$', '%']
for caracter in caracteres:
    if caracter in palabra:
        print('La palabra contiene el caracter', caracter)
    else:
        print('La palabra no contiene el caracter', caracter)