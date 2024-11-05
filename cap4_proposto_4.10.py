A = int(input('Digite o lado A: '))
B = int(input('Digite o lado B: '))
C = int(input('Digite o lado C: '))
if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        print(f'{A}, {B}, {C} formam um triângulo ', end='') # não pula linha
        if A == B == C:
            print('equilátero')
        elif A == B or A == C or B == C:
            print('isóceles')
        else:
            print('escaleno')
    else:
        print(f'{A}, {B}, {C} não formam um triângulo')
else:
    print('Há pelo menos um valor inválido')