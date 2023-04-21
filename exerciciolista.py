"""
Crie um programa que retorne o maior número da lista
"""

lista = [3,5,8,2,4,6,12,5,10]
print(lista)

maior = lista[0]

for i in lista:
  if i>maior:
    maior=i

print("o maior número é o",maior)
