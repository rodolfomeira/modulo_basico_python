texto = input('Digite algum texto: ')
qtdecaracteres = len (texto)

print('\nSaída usando método format')
print('O texto {} contém {} caracteres'.format(texto, qtdecaracteres))

print('\nSaída usando método f-string')
print(f'O texto {texto} contém {qtdecaracteres} caracteres')
