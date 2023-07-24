# Sequência Lógica
# Repetição

# -*- coding: utf-8 -*-
iteration = int(input())
i = 1

while(i <= iteration):
    quad = i**2
    cubo = i**3
    print("%d %d %d" %(i, quad, cubo))
    quad = i**2 + 1
    cubo = i**3 + 1
    print("%d %d %d" %(i, quad, cubo))
    i += 1
