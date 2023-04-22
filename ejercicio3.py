import random

num_dados = 3
num_lanzamientos = 1000

resultados = {}
for i in range(1, num_dados + 1):
    resultados[i] = 0

for i in range(num_lanzamientos):
    suma = 0
    for j in range(num_dados):
        dado = random.randint(1, 6)
        suma += dado
        resultados[dado] += 1
    print(f"Lanzamiento {i+1}: {suma}")

for cara, veces in resultados.items():
    print(f"{cara}: {'*' * veces} {veces} veces")