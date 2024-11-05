LstValores = []
valor = int(input('Digite um inteiro: '))
while valor != 0:
    LstValores.append(valor)
    valor = int(input('Digite um inteiro: '))
print('\nResultado')
print(LstValores)
print(f'A lista contém {len(LstValores)} elementos')
print('Fim do Programa')
