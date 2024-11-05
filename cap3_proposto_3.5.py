Tempo = (int(input('Digite um tempo em segundos: ')))
h = Tempo // 3600
Tempo = Tempo % 3600
m = Tempo // 60
s = Tempo % 60
print(f'{h} hora(s), {m} minuto(s), {s} segundo(s)')
