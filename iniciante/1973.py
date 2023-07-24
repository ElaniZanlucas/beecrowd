# Jornada nas estrelas
# Simulação

n = int(input())
v = input().split()
countStar = 0
carneirosRestantes = 0

for i in range(n):
    v[i] = int(v[i])

while i in range(0, n):
    if (v[i] > 0):
        v[i] -= 1
        countStar += 1
        if((v[i] % 2) == 0):
            i -= 1
        elif((v[i] % 2) == 1):
            i += 1
    else:
        i -= 1

for carneiros in v:
    carneirosRestantes = carneirosRestantes + carneiros
    
print("%d %d" %(countStar, carneirosRestantes))