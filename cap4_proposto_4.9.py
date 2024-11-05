A = int(input('Digite A: '))
B = int(input('Digite B: '))
C = int(input('Digite C: '))
if A == B == C:  # é o mesmo que A == B and B == C
    print('Os três valores são iguais')
else:
    if A == B or A == C or B == C:
        print('Há dois valores iguais e um diferente')
    else:
        print('Os três valores são diferentes')
