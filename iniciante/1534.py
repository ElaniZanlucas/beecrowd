# Matriz 123
# Matrizes

# -*- coding: utf-8 -*-

while True:
  try:
    n = int(input())
    M = []
    for i in range(n):
        linha = []
        for j in range(n):
            if(i == j):
                if(i+j == n-1):
                  linha.append(2)
                else:
                  linha.append(1)
            elif(i+j == n-1):
                linha.append(2)
            else:
                linha.append(3)
        M.append(linha)

    for i in range(n):
      for j in range(n):
        print(M[i][j], end= "")
      print("")
  except EOFError:
    break