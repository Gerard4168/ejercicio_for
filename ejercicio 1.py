# leer n numero enteros uno en cada lectura, mostrar e imprimir cuantos son pares y cuantos son impares.

n = int(input("Ingrese el rango: "))

par=0
impar=0

for i in range(n):
    p = int(input("Digite un número: "))
    if p%2==0:
        par = par + 1
    else:
        impar = impar + 1

print("Se leyeron", par, "Numeros pares y", impar, "Numeros impares")