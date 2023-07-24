# Grenais
# Repetição

# -*- coding: utf-8 -*-

inter = 0
gremio = 0
empate = 0

grenal = 1
countGrenal = 0

while (grenal == 1):
  golInter, golGremio = input().split()
  golInter = int(golInter)
  golGremio = int(golGremio)
  if (golInter > golGremio):
    inter += 1
  elif (golInter < golGremio):
    gremio += 1
  elif (golInter == golGremio):
    empate += 1
  countGrenal += 1
  print("Novo grenal (1-sim 2-nao)")
  grenal = int(input())

if (inter > gremio):
  resultado = "Inter venceu mais"
elif (inter < gremio):
  resultado = "Gremio venceu mais"
elif (inter == gremio):
  resultado = "Nao houve vencedor"

print("%d grenais" %(countGrenal))
print("Inter:%d" %(inter))
print("Gremio:%d" %(gremio))
print("Empates:%d" %(empate))
print(resultado)