nome = input('Digite o nome: ')
n1 = float(input('Nota da primeira avaliação: '))
n2 = float(input('Nota da segunda avaliação: '))
n3 = float(input('Nota da terceira avaliação: '))
MF = (n1 + n2 + n3) / 3
if MF >= 7:
    print(f'{nome} obteve média = {MF:.1f} e foi Aprovado') # média com 1 casa decimal
else:
    print(f'{nome} obteve média = {MF:.1f} e foi Reprovado')
