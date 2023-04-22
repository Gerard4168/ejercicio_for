# Cuantos multiplos por 7 y por 9 hay en el rango de (1000,5000)

Mul_7=0
Mul_9=0

for i in range (1000,5000):
    if i % 7 ==0:
        Mul_7= Mul_7+1
    if i % 9 == 0:
        Mul_9= Mul_9+1
print("Hay: "+str(Mul_7), "Multiplos de 7")
print("Hay: "+str(Mul_9), "Multiplos de 9")