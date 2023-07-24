# Sequência de sequência
# Universo imaginário

while True:
  try:
      n = int(input())
      seq = []
      seq.append(0)

      for i in range(n):
          j = 0
          while (j < i+1):
             seq.append(i+1)
             j += 1
      tam = len(seq)

      if (n == 0):
        print("Caso %d: %d numero" %(nCaso, tam))
        print(' '.join(map(str, seq)))  
        print() 
      else:
        print("Caso %d: %d numeros" %(nCaso, tam))
        print(' '.join(map(str, seq)))
        print() 
  except EOFError:
    break
