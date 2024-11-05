from random import randint
Qtde = int(input('Digite a quantidade '))
Lista = []
for i in range(Qtde):
    Lista.append(randint(1, 100))
print('Lista gerada')
print(Lista)
print(f'Esta lista tem {len(Lista)} elementos')

X = int(input('Digite X: '))
while X > 0:
    while X in Lista:
        Lista.remove(X)
    print(Lista)
    print(f'Esta lista tem {len(Lista)} elementos')

    X = int(input('Digite X: '))