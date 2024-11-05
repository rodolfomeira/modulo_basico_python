X = 1
while X > 0:     # enquanto X for positivo faça as repetições
    X = int(input('Digite X: '))
    if X == 0:   # se X for zero interrompa o laço
        print('  você digitou zero...')
        break
    print(X)
else:            # este else é executado quando X for negativo se X for zero não
    print('você digitou negativo')
print('Fim do Programa')