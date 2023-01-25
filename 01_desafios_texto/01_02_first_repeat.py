def first_repeat(cadena):
    cadena = cadena.lower().replace(" ", "")
    for pos, letra in enumerate(cadena):
        if letra in cadena[pos+1:]:
            return letra
    return 'none'


print(first_repeat("Cadena de prueba"))
print(first_repeat("Caden"))
