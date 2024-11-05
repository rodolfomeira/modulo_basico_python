LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    if valor not in LstValores:
        LstValores.append(valor)
    else:
        print(f'  erro! o valor {valor} já está na lista')
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')
