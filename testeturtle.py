from turtle import *
raio = 5
cor1 = "lime"
cor2 = "white"
cor = cor1
bgcolor("darkgreen")

for i in range(1, 8):
  if cor == cor1:
      cor = cor2
  else:
    cor = cor1
  color(cor)
  circle(raio*i)
 
