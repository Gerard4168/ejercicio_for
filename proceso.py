# caso 1
x = range(10)
for i in x:
    print(i)

# caso 2
x = range(10)
rta = "range = "
for i in x:
    rta = rta + ",  " + str(i)
rta = rta + ", "
print(rta)

# caso 3
x = range (3,10)
rta = "range = |"
for i in x:
 rta = rta + ",  " + str(i)

# ejemplo 1
rta = "Salida = |"
for i in [1,2,3,4,5,6,7,8,9,10]:
   rta = rta + str(i) + ", "
rta = rta + " | "
print(rta)

# ejemplo 2
for numero in range(1,2,3,4,5,6,7,8,9,10):
   print("Uis no es uno")

# ejemplo 3
rta = "Salida = |"
for numero in range(1,2,3,4,5,6,7,8,9,10):
   rta = rta + str(numero) + ", "
rta = rta + " | "
print(rta)

# ejemplo 4
rta = "Salida = |"
for numero in range(1,11):
   rta = rta + str(numero) + ", "
rta = rta + " | "
print(rta)

# ejemplo 5
rta = "Salida = |"
for numero in "Uis no es uno":
   rta = rta + str(numero) + ", "
rta = rta + " | "
print(rta)
# ejemplo 6
suma = 0
for i in range(1,11):
   suma = suma + i
print("La suma es: "(suma))

# ejemplo 7
frase = input("Digite una frase")
vocales = "aeiouAEIOU"
numero_vocales = 0
for i in frase:
   if i in vocales == numero_vocales + 1 :
      print("En la frase hay"(numero_vocales))

