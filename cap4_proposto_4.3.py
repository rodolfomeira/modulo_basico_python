salario = float(input('Digite o salário: '))
parcela = float(input('Digite a parcela: '))
if parcela < 0.08 * salario:
    print('Empréstimo concedido')
else:
    print('Empréstimo recusado')