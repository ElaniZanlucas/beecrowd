# Fibonacci em Vetor
# Vetores

# -*- coding: utf-8 -*-
  
count = int(input())

while(count > 0):
  val = int(input())
  fibAtual = 0

  if(val==0):
    fibAtual = 0
  elif (val==1) or (val==2):
    fibAtual = 1
  else:
    fib0 = 1
    fib1 = 1
    inter = 3
    while inter <= val:
      fibAtual = fib0 + fib1
      fib0 = fib1
      fib1 = fibAtual
      inter += 1
  
  count -=1

  print("Fib(%d) = %d" %(val, fibAtual))
