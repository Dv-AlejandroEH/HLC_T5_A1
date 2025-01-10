base = int(input("Introduzca la base del triangulo: "))
altura = int(input("Introduzca la altura del triangulo: "))
precio = int(input("Introduzca el precio por cada metro cuadrado de área del triangulo: "))
def calcular_area(b, h):
    return int(b*h/2)
area = calcular_area(base, altura)
def calcular_precio(area, precio):
    return area*precio
resultado = calcular_precio(area, precio)
print("Área =", area, "metros cuadrados. Costo total =", resultado, "unidades")