tipo = input('Digite o tipo de moeda: ')
valor = float(input('Valor a comprar: '))
if tipo == 'D':
    reais = valor * 4.89
    print(f'Para comprar {valor:.2f} dólares são necessários {reais:.2f} reais')
elif tipo == 'E':
    reais = valor * 5.26
    print(f'Para comprar {valor:.2f} euros são necessários {reais:.2f} reais')
elif tipo == 'L':
    reais = valor * 6.17
    print(f'Para comprar {valor:.2f} libras são necessários {reais:.2f} reais')
else:
    print(f'Tipo {tipo} inválido')
