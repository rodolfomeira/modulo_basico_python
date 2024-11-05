nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
sexo = input('Digite o sexo (f ou m): ')
if sexo == 'f' or sexo == 'F':
    if idade >= 21 and idade <= 34:
        print(f'A mulher {nome} com {idade} será aceita para o serviço')
    else:
        print(f'A mulher {nome} com {idade} não será aceita para o serviço')
elif sexo == 'm' or sexo == 'M':
    if idade >= 18 and idade <= 39:
        print(f'O homem {nome} com {idade} será aceito para o serviço')
    else:
        print(f'O homem {nome} com {idade} não será aceito para o serviço')
else:
    print(f'{sexo} é inválido')
