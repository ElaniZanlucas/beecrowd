# Notas e Moedas
# Sequencial

# -*- coding: utf-8 -*-

valor = input()
destroy = valor.split(".")
# print(destroy)

real = int(destroy[0])
cent = int(destroy[1])
# print(real, cent)

nota100 = real // 100
if(nota100 > 0):
  real = real%100  

nota50 = real // 50
if(nota50 > 0):
  real = real%50  

nota20 = real // 20
if(nota20 > 0):
  real = real%20  

nota10 = real // 10
if(nota10 > 0):
  real = real%10

nota5 = real // 5
if(nota5 > 0):
  real = real%5 

nota2 = real // 2
moeda1 = real%2

moeda50 = cent // 50
if(moeda50 > 0):
  cent = cent%50

moeda25 = cent // 25
if(moeda25 > 0):
  cent = cent%25  

moeda10 = cent // 10
if(moeda10 > 0):
  cent = cent%10

moeda5 = cent // 5
moeda01 = cent%5

print("NOTAS:")
print("%d nota(s) de R$ 100.00" %(nota100))
print("%d nota(s) de R$ 50.00" %(nota50))
print("%d nota(s) de R$ 20.00" %(nota20))
print("%d nota(s) de R$ 10.00" %(nota10))
print("%d nota(s) de R$ 5.00" %(nota5))
print("%d nota(s) de R$ 2.00" %(nota2))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %(moeda1))
print("%d moeda(s) de R$ 0.50" %(moeda50))
print("%d moeda(s) de R$ 0.25" %(moeda25))
print("%d moeda(s) de R$ 0.10" %(moeda10))
print("%d moeda(s) de R$ 0.05" %(moeda5))
print("%d moeda(s) de R$ 0.01" %(moeda01))

