N = int(input('Digite N: '))
while N < 100 or N > 200:      # o valor é inválido
    print(f'  erro!! o valor {N} é inválido')
    N = int(input('Digite N: '))
print(f'O valor {N} é válido')
print('Fim do Programa')
