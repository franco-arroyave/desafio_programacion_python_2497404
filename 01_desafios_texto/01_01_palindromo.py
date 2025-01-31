def es_palindromo(texto):

    texto_minuscula = texto.lower()
    texto_sin_espacios = texto_minuscula.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]


print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("palindromo"))  # False

def palindromo(palabra):
    palabra = palabra.lower().replace(" ", "")
    return palabra == palabra[::-1]

print(palindromo("Anita lava la tina"))
