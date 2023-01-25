import math

def esPrimo(numero):
  if numero <= 1: return False
  raiz = math.sqrt(numero).__floor__()
  for mult in range(2,raiz+1):
    if numero % mult == 0: return False
  return True

print(esPrimo(1))
print(esPrimo(2))
print(esPrimo(21))
print(esPrimo(29))
