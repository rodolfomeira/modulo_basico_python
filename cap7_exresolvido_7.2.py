P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a qtde de termos: "))
ultimo = P + R * (Q-1)
Termos = list(range(P, ultimo+1, R))  # a classe range gera a PA
print('Lista gerada com range')
print(Termos)
print('Fim do Programa')