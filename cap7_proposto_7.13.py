Produtos = []
mensagem = 'Digite os dados (int float float): '
entrada = input(mensagem)
while entrada != '0 0 0':
    entrada = entrada.split()
    item = (int(entrada[0]), float(entrada[1]), float(entrada[2]))
    Produtos.append(item)
    entrada = input(mensagem)

print('\nExibição das Margens Brutas')
for cod, pcCompra, pcVenda in Produtos: # cada item em Produtos é uma tupla, por isso são três objetos no for
    MargemBruta = (pcVenda/pcCompra - 1) * 100
    print(f'Produto {cod} possui margem bruta = {MargemBruta:.1f} %')

print('\nFim do Programa')