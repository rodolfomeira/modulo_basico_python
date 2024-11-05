X = int(input('Digite um inteiro: '))
Resto = X % 2         # Calcula o resto da divisão de X por 2
if Resto == 0:        # Verifica se o resto é 0
    print(f'O número {X} é par')
else:                 # Se a condição resultou False desvia para este else
    print(f'O número {X} é ímpar')
print('Fim do Programa')