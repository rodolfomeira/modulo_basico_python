LstValores = []
LstRepetidos = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        LstRepetidos.append(valor)
        print(f'  erro! o valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('\nValores repetidos digitados')
print(LstRepetidos)
print('Fim do Programa')
