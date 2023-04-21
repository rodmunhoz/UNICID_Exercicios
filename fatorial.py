"""
Crie um programa que peça um número ao usuário e
retorne o fatorial desse número
"""

número = int(input("digite um número inteiro: "))
resultado = 1
for i in range(1,número+1):
  resultado = resultado * i
print("o fatorial de",número,"é =",resultado)
