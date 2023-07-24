linha = input();
itens = linha.split();
n, val = int(itens[0]), float(itens[1]);
print("n=%d, val=%f" % (n,val));
print(type(itens))
print(type(itens[0]))

print("---------------")
itens[0] = int(itens[0])
print(type(itens))
print(type(itens[0]))