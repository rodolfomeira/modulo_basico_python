Invest = float(input('Valor do investimento: '))
Custos = float(input('Valor dos custos: '))
Receita = float(input('Valor da receita: '))
ROI = (Receita - (Custos + Invest)) / (Custos + Invest) * 100
print(f'ROI = {ROI:.1f} %')
