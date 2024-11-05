from random import randint
Qtde = int(input('Digite a quantidade '))
Lista = []
for i in range(Qtde):
    Lista.append(randint(1, 100))
Lista = [3, 6, 9, 9, 2, 8, 6, 9, 9, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 2, 3, 4, 5, 6]
print('\nLista gerada')
print(Lista)
print(f'Esta lista tem {len(Lista)} elementos')

for valor in Lista:
    pos = Lista.index(valor)
    for i in range(len(Lista)-1, pos, -1): # percorre a lista do fim até pos
        if Lista[i] == valor:              # se encontrar o valor
            Lista.pop(i)                   # usa pop para eliminação

print('\nLista após a eliminação dos repetidos')
print(Lista)
print(f'Esta lista tem {len(Lista)} elementos')