# Lanche
# Seleção

# -*- coding: utf-8 -*-

lanche,quantidade = input().split()

lanche = int(lanche)
quantidade = int(quantidade)
total = 0

if (lanche == 1):
    total = quantidade * 4.00
elif (lanche == 2):
    total = quantidade * 4.50
elif (lanche == 3):
    total = quantidade * 5.00
elif (lanche == 4):
    total = quantidade * 2.00
elif (lanche == 5):
    total = quantidade * 1.50

print("Total: R$ %.2f" %(total))