diasNoMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # contém a quantidade de dias de cada mês

data = input('Forneça uma data no formato aaaammdd >>> ')
if len(data) != 8:
    print('A entrada não corresponde ao formato especificado')
elif not data.isnumeric():
    print('A entrada deve conter apenas algarismos')
else:
    ano = int(data[0:4])
    mes = int(data[4:6])
    dia = int(data[6:8])
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0): # ajusta o mês de fevereiro para anos bissextos
        diasNoMes[1] += 1
    if mes == 0 or mes > 12:
        print(f'O mês {mes} é inválido')
    elif dia == 0 or dia > diasNoMes[mes-1]:
        print(f'O dia {dia} é inválido para o mês {mes}')
    else:
        print(f'A data fornecida é {dia:02d}/{mes:02d}/{ano:04d}')
