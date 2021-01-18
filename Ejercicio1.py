palabras = {'Comida', 'Luz', 'Oscuridad', 'Eugenia', 'Blus'}
vocales = ['a', 'e', 'i', 'o', 'u']

score = 0
for palabra in palabras:
    n_vocales = 0
    pal_min=palabra.lower()
    for letra in pal_min:
        if letra in vocales:
            n_vocales = n_vocales + 1

    if n_vocales%2:
        score = score + 1
    else:
        score = score + 2

print('Mostrar palabras: ' + str(palabras))
print('El puntaje final es: ' + str(score))

