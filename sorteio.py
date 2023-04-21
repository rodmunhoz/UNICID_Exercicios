"""
crie um programa que sorteie um número entre 1 e 10 e peça para o usuário adivinhar esse número. a cada tentativa, o programa deve informar se o chute foi muito alto ou muito baixo. ao acertar, o programa deve informar quantas tentativas foram necessárias.
"""
import random
numero_certo = random.randint(1,10)
acertou = False
tentativas = 0 

while acertou != True:
  tentativas += 1 #aumenta a variável em qualquer número
  palpite = int(input("digite um número inteiro entre 1  e 10: "))
  if palpite == numero_certo:
    print("Você acertou o número", numero_certo, "em"     ,tentativas, "tentativas")
    acertou = True
  else:
    if palpite < numero_certo:
      print("o número é maior!")
    else:
      print("o número é menor!")
