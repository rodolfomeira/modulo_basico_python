S = input('Digite dois inteiros e um real: ')
L = S.split()	# Faz a separação usando espaço em branco como separador
print("lista L: ", L)         # Exibe na tela a lista L
A = int(L[0])	# converte o elemento L[0] para inteiro
B = int(L[1])	# converte o elemento L[1] para inteiro
X = float(L[2])	# converte o elemento L[2] para real
print(f'A = {A}, B = {B}, X = {X}')
