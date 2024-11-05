try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(f'Resultado = {R}')
except ZeroDivisionError:         # except nomeado
    print('B não pode ser zero')
except ValueError:                # except nomeado
    print('Digite números inteiros para A e B')
except:                           # except genérico (não-nomeado)
    print('Não é possível calcular a divisão. Erro desconhecido')
else:
    print('else')
finally:
    print('finally')

# Neste código as cláusulas else e finally foram incluídas (No EBook elas não estão presentes).