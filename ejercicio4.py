n=int(input("Ingrese un valor entero positivo: "))

fac = 1

for i in range(1,N+1):
    fac = fac*i
print("El factorial de "+str(n),"es "+str(fac))