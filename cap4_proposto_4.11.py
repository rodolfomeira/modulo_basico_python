pcCusto = float(input('Preço de custo = '))
if pcCusto <= 100:
    pcVenda = pcCusto * 1.45
else:
    pcVenda = pcCusto * 1.35
print(f'O preço de venda do produto é {pcVenda:.2f}')
