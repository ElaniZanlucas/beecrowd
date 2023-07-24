# Corvo contador
# Sistemas de numeração

# -*- coding: utf-8 -*-

countCaw = 0

while (countCaw < 3):
  entrada = input()

  if(entrada == "caw caw"):
    countCaw += 1
  else:
    entrada = entrada.replace("*", "1")
    entrada = entrada.replace("-", "0")
    entrada = int(entrada)

    binario = entrada
    decimal = 0
    i = 0  
    
    while (i <= 3):
      resto = binario % 10
      decimal = decimal + (resto * (2**i))
      i += 1
      binario = binario // 10
    
    print(decimal)
  
    