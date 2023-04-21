"""
Crie um programa que peça um número ao usuário e
escreva a tabuada daquele número
"""

número = int(input("digite um número "))
for i in range(1, 11):
  print (número, "x",i, "=", número*i)
