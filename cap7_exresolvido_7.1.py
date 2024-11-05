P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a qtde de termos: "))
Termos = [P]   # cria a lista já com o primeiro termo
i = 0
while i < Q-1:        # vai até Q-1 porque o primeiro termo já esta na lista
    P = P + R         # calcula o próximo termo
    Termos.append(P)  # acrescenta o termo à lista
    i += 1
print('Lista resultante')
print(Termos)
print('Fim do Programa')