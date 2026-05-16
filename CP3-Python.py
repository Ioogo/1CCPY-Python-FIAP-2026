temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

medias = []

critico = []

for sala in temperaturas:
    medias.append(sum(sala) / len(sala))

    contador = 0

    for temperatura in sala:
        if temperatura >= 33:
            contador += 1
    critico.append(contador)

for i in range(len(temperaturas)):
    print(f"Sala de Aula: {i+1}")
    print(f"Temperatura média: {medias[i]}")
    print(f"Quantidade de registros críticos: {critico[i]}")
    print()

sala_critica = 0
for crit_atual in critico:
    if crit_atual > sala_critica:
        sala_critica = crit_atual
print(f"A sala com mais temperaturas batendo no limite ou passando é a: {sala_critica}ª")