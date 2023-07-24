list = ['primeiro', 'segundo', 'terceiro']
saida1 = str(list)[1:-1]
saida2 = '-'.join(map(str, list))

print("Saida1: %s" %(saida1))
print()
print("Saida2: %s" %(saida2))