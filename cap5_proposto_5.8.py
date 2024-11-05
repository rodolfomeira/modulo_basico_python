TotRes = TotInd = 0
Cod = int(input('Digite o código: '))
while Cod != 0:
    Qtde = int(input('Digite a quantidade: '))
    T = Cod // 1000
    if T == 1:
        TotRes += Qtde
    elif T == 2:
        TotInd += Qtde
    else:
        print('  Tipo Inválido')
    Cod = int(input('Digite o código: '))

print(f'Total de produtos residenciais = {TotRes}')
print(f'Total de produtos industriais = {TotInd}')
print('Fim do Programa')
