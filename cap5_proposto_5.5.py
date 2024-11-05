LMin = int(input('Digite LMin: '))
LMax = int(input('Digite LMax: '))
D = int(input('Digite D: '))
cont = LMin
while cont <= LMax:
    if cont % D == 0:
        print(cont)
    cont += 1
print('Fim do Programa')
