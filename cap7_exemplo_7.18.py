S = input('Digite um número inteiro: ')
if S.isnumeric():
    N = int(S)
    print(f'  o número digitado foi {N}')
else:
    print('  Erro: digite apenas números')
