data = input('Forneça uma data no formato aaaammdd >>> ')
if len(data) != 8:
    print('A entrada não corresponde ao formato especificado')
elif not data.isnumeric():
    print('A entrada deve conter apenas algarismos')
else:
    ano = data[0:4]
    mes = data[4:6]
    dia = data[6:8]
    print(f'A data fornecida é {dia}/{mes}/{ano}')
