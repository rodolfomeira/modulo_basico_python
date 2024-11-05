N = int(input('Digite a quantidade: '))
L = []
for i in range(N):
    try:
        X = float(input(f'  elemento {i}: '))
        L.append(X)
    except ValueError:
        print('  ...erro: digite apenas algarismos e um ponto decimal')
    except:
        print('  ...erro fatal!')
print('\nResultado:')
for valor in L:
    print(f'  {valor}')
print('Fim do Programa')