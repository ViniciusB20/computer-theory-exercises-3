# EXERCICIO 1 - LISTA 3
import random
 
matriz = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
diagonal = 0
tudo = 0
 
for l in range(0, 10):
  for c in range(0, 10):
    matriz[l][c] = random.randint(0, 1000)
 
print("")
print('*' *30, '10X10', '*' *30)
print("")
 
for l in range(0, 10):
  for c in range(0, 10):
    print(f'[{matriz[l][c]:^5}]', end='')
  print()
 
for l in range(0, 10):
  for c in range(0, 10):
    tudo += matriz[l][c]
print("")
print(f"A soma de todos numeros da matriz : {tudo}")  
 
for l in range (0, 10):
  diagonal += matriz[l][l]
print(f"A soma dos numeros da diagonal principal : {diagonal}")