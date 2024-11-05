# esta versão cria duas listas diferentes
# LstNeg = []
# LstPos = []

# esta versão cria dois diferentes identificadores com o mesmo id, na prática
# significa que ambos são a mesma lista
# LstNeg = LstPos = []
# a alteração em uma delas causa alteração na outra.

# Execute o programa desta forma e veja o que ocorre
N = int(input('Digite a quantidade: '))
LstNeg = LstPos = []
for i in range(N):
    X = int(input(f'  elemento {i}: '))
    if X >= 0:
        LstPos.append(X)
    else:
        LstNeg.append(X)
print(f'\nLista de negativos: {LstNeg}, contém {len(LstNeg)} elementos')
print(f'Lista de positivos: {LstPos}, contém {len(LstPos)} elementos')
print('\nFim do Programa')