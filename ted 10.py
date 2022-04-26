#Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, 
#o algoritmo deve escrever esses 20 números lidos na ordem inversa.

numeros = list(range(1,21))
numeros.reverse()
print(numeros)

#Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
#verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

import random

numeros_v = []
VET = []
for n in range(1, 51):
    VET.append(random.randint(1, 9))
print(VET)

for k in VET:
    if k not in numeros_v:
        indices = [indice for indice, valor in enumerate(VET) if valor == k]
        print("numero: ", k , " posições: ", indices)
        numeros_v.append(k)
