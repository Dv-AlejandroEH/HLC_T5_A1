numeros = [0, 1]
for i in range(2, 10):
    siguiente_numero = numeros[i-1] + numeros[i-2]
    numeros.append(siguiente_numero)
print(numeros)