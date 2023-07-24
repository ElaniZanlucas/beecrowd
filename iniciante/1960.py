# Numeração Romana para Números de Página
# Ad-Hoc, Digits, Switch-Case

decimal = int(input())
saida = ""

romans = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']

arabics = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]

for i in range(12, -1, -1):
    while (decimal >= arabics[i]):
        decimal = decimal - arabics[i]
        saida = saida + romans[i]

print(saida)
    

