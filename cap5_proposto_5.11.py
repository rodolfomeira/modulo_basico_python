Qtde = int(input('Digite a quantidade: '))
print(f'Os {Qtde} primeiros termos da sequência de Fibonacci são:')
i = a = 0
b = 1
while i < Qtde:
    print(a, end='  ')
    i += 1
    c = a + b
    a = b
    b = c
print('\nFim do Programa')
