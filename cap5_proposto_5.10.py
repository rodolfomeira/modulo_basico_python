A = int(input('Digite um inteiro positivo: '))
i = 2
cont = 0
while i < A:
    if A % i == 0:
        cont += 1  # conta quantas vezes A é divisível por algum valor entre 2 e A-1
    i += 1
if cont == 0:      # se não for divisível nenhuma vez, então A é primo
    print(f'{A} é primo')
else:
    print(f'{A} não é primo')
print('Fim do Programa')

# Atenção: Esta solução funciona, mas é muito ineficiente.
# Desafio: Tente pensar em outra solução mais eficiente.