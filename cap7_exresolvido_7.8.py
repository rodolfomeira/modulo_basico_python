valores = input('Digite 3 inteiros separados por espaço: ')
valores = valores.split()  # usa o método .split() para serparar os valores
for i in range(len(valores)):      # itera sobre a lista valores
    valores[i] = int(valores[i])   # e converte cada objeto para int
print(f'n1 = {valores[0]}')
print(f'n2 = {valores[1]}')
print(f'n3 = {valores[2]}')
print(f'Soma = {sum(valores)}')
