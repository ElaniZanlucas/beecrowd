# Reservatório de Mel
# Matemática

# -*- coding: utf-8 -*-

while True:
  try:
      v = float(input())
      d = float(input())

      area = 3.14*((d/2)**2)
      h = v/area

      print("ALTURA = %.2f" %(h))
      print("AREA = %.2f" %(area))
  except EOFError:
    break
