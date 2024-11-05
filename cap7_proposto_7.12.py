ListaNomes = []
nome = input('Digite um nome: ')
while nome != '':
    ListaNomes.append(nome)
    nome = input('Digite um nome: ')

print('Primeiro modo de fazer') # usando lógica comum
cont = 1
for nome in ListaNomes:
    print(cont, nome)
    cont += 1

print('Segundo modo de fazer') # usando a função enumerate
for n, nome in enumerate(ListaNomes):
    print(n+1, nome)  # enumerate gera uma tupla com o número de ordem (iniciando em 0)
                      # e o elemento da lista
