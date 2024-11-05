from random import randint
# primeira parte - geração da lista
Lst = []
Qtde = int(input('Digite a quantidade: '))
for i in range(Qtde):
    a = randint(1, 20)
    Lst.append(a)
print('Lista gerada:')
print(f'  {Lst}\n')
# segunda parte - pesquisa na lista
X = 1
while X > 0:
    X = int(input('Digite X: '))
    if X in Lst:
        print(f'  há {Lst.count(X)} ocorrência(s) de {X} na lista')
    else:
        print(f'  {X} não está na lista')
print('Fim do Programa')