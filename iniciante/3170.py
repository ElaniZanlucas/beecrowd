# Bolinhas de Natal
# Desconhecido

# -*- coding: utf-8 -*-

bolinhas = int(input())
galhos = int(input())

qtd_b = galhos//2

if(bolinhas >= qtd_b):
    print("Amelia tem todas bolinhas!")
else:
    comprar_b = qtd_b - bolinhas
    print(f"Faltam {comprar_b} bolinha(s)")