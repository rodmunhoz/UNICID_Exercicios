"""
Contar o número de dígitos em número inteiro
"""
digitos = 0
n = int(input("digite um número inteiro: "))
while n != 0:
  digitos += 1
  n = n // 10
print(digitos)
