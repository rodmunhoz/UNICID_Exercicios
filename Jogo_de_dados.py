"""
JOGO DE DADOS
o jogador começa com um saldo (100)
O jogador faz um aposta - existe uma aposta mínima (10)
o python rola os dois dados e soma os resultados
o python testa o resultado
	2 ou 12 -> ganha o triplo da aposta
 	7 -> ganha o dobro da aposta
se o saldo for zero ou menor do que a aposta mínima -> fim de jogo
*** 
"""
import random

saldo = 100
aposta_atual = 0
aposta_minima = 10
resultado_atual = 0

def testar_dados():
	d1 = 0
	d2 = 0
	d3 = 0
	d4 = 0
	d5 = 0
	d6 = 0
	for i in range(10000):
		d = random.randint(1, 6)
		if d == 1:
			d1 += 1
		elif d == 2:
			d2 += 1
		elif d == 3:
			d3 += 1
		elif d == 4:
			d4 += 1
		elif d == 5:
			d5 += 1
		elif d == 6:
			d6 += 1
	print(d1)
	print(d2)
	print(d3)
	print(d4)
	print(d5)
	print(d6)

def apostar():
	global saldo
	global aposta_atual
	global aposta_minima
	aposta_atual = 0
	while aposta_atual < aposta_minima or aposta_atual > saldo and aposta_atual != -1:
		aposta_atual = int(input("Digite sua aposta "))
	saldo -= aposta_atual
	print("Voce apostou", aposta_atual)

def rolar_dados():
	global resultado_atual
	dado1 = random.randint(1, 6)
	dado2 = random.randint(1, 6)
	resultado_atual = dado1 + dado2
	print("os dados deram", dado1, "e", dado2)

def testar_rodada(r):
	global aposta_atual
	if r == 2 or r == 12:
		return aposta_atual * 3
	elif r == 7:
		return aposta_atual * 2
	else:
		return 0

def jogar():
	global saldo
	apostar()
	rolar_dados()
	saldo += testar_rodada(resultado_atual)
	print(saldo)

while saldo >= aposta_minima and aposta_atual != -1:
	jogar()
else:
	if saldo < aposta_minima:
		print("fim de jogo, você faliu. Seu saldo é", saldo)
	else:
		print("fim de jogo, seu saldo é", saldo)
