from random import randint

# Gera a lista A com tamanho nA, sem valores repetidos
nA = int(input('Digite a quantidade nA: '))
while nA > 100:
    print('o valor de nA não pode ser maior que 100')
    nA = int(input('Digite a quantidade nA: '))
A = []
while len(A) < nA:
    valor = randint(1, 100)
    if valor not in A:
        A.append(valor)
A.sort() # ordena a lista A
print(f'nA = {nA}  lista A = {A}')

# Gera a lista B com tamanho nB, sem valores repetidos
nB = int(input('\nDigite a quantidade nB: '))
while nB > 100:
    print('o valor de nB não pode ser maior que 100')
    nB = int(input('Digite a quantidade nB: '))
B = []
while len(B) < nB:
    valor = randint(1, 100)
    if valor not in B:
        B.append(valor)
B.sort() # ordena a lista B
print(f'nB = {nB}  lista B = {B}')

# Junta as listas A e B gerando a lista R (sem a inclusão de repetidos)
R = A.copy() # coloca todos os elementos de A em R
for b in B:
    if b not in A:  # acrescenta a R os elementos de B não repetidos em A
        R.append(b)
R.sort() # ordena a lista R
print('\nLista resultante')
print(f'nR = {len(R)}  Resultante = {R}')
