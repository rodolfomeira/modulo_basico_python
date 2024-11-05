PH = float(input("Digite um valor do PH: "))
if PH < 6.0:
    r = "ácida"
elif PH < 7.0:
    r = "levemente ácida"
elif PH == 7.0:
    r = "neutra"
elif PH < 8.0:
    r = "levemente alcalina"
else:
    r = "alcalina"
print(f'Com pH = {PH} a solução é {r}')