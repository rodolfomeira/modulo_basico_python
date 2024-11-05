municipio = input('Digite o nome do município: ')
eleitores = int(input('  quantidade de eleitores: '))
votos = int(input('  quantidade de votos do 1º colocado: '))
if eleitores < 200000:
    print(f'No município {municipio} não haverá segundo turno')
else:
    if votos > eleitores / 2:
        print(f'No município {municipio} não haverá segundo turno')
    else:
        print(f'No município {municipio} haverá segundo turno')
