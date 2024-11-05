N = int(input('Digite a quantidade: '))
LstNeg = []
LstPos = []
for i in range(N):
    X = int(input(f'  elemento {i}: '))
    if X >= 0:
        LstPos.append(X)
    else:
        LstNeg.append(X)
print(f'\nLista de negativos: {LstNeg}, contém {len(LstNeg)} elementos')
print(f'Lista de positivos: {LstPos}, contém {len(LstPos)} elementos')
print('\nFim do Programa')