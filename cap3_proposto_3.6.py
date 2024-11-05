nomevend1 = input('Digite o nome do primeiro vendedor: ')
totvend1 = float(input('Total vendido do primeiro vendedor: '))
nomevend2 = input('Digite o nome do segundo vendedor: ')
totvend2 = float(input('Total vendido do segundo vendedor: '))
nomevend3 = input('Digite o nome do terceiro vendedor: ')
totvend3 = float(input('Total vendido do terceiro vendedor: '))

comis1 = 1200 + totvend1 * 0.06
print(f'vendedor {nomevend1} vendeu R$ {totvend1:.2f} e faz jus a uma comissão de R$ {comis1:.2f}')
comis2 = 1200 + totvend2 * 0.06
print(f'vendedor {nomevend2} vendeu R$ {totvend2:.2f} e faz jus a uma comissão de R$ {comis2:.2f}')
comis3 = 1200 + totvend3 * 0.06
print(f'vendedor {nomevend3} vendeu R$ {totvend3:.2f} e faz jus a uma comissão de R$ {comis3:.2f}')
