Mae = input('Digite o nome da mãe: ')
Pai = input('Digite o nome do pai: ')
Crianca = input('Digite o nome da criança: ')

print('\nSaída usando método format')
print('Os adultos {} e {} são os responsáveis por {}'.format(Mae, Pai, Crianca))

print('\nSaída usando método f-string')
print(f'Os adultos {Mae} e {Pai} são os responsáveis por {Crianca}')
