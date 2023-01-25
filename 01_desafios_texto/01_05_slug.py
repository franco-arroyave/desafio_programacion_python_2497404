import re

def slug(cadena):
  cadena = cadena.lower().replace(" ","-")
  return re.sub("[^\w\-]|", "", cadena)

print(slug("Cadena de pr=ueba 2 para extraer"))

