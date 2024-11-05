risco = input('Digite BX ou AL para o grau de risco: ')
valor = float(input('Digite o valor: '))
if risco != 'BX' and risco != 'AL':
    print(f'{risco} é inválido para o grau de risco')
else:
    if risco == 'BX':
        if valor < 1000.0:
            tipo = 'Poupança'
        else:
            tipo = 'Renda fixa'
    else:  # risco == 'AL'
        if valor < 1000.0:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
    print(f'Você deve investir em {tipo}')