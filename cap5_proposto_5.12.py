Qtde = int(input('Digite a quantidade: '))
Prim = int(input('Digite a Prim: '))
print(f'Os {Qtde} primeiros termos da sequência de Fibonacci maiores que {Prim} são:')
i = a = 0
b = 1
while i < Qtde:
    if a > Prim:
        print(a, end='  ')
        i += 1
    c = a + b
    a = b
    b = c
print('\nFim do Programa')
