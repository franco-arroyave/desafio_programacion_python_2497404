def aplanar(lista:list) -> list:
  salida:list = []
  for val in lista:
    if type(val) == list:
      salida = salida + val
    else:
      salida.append(val)
  return salida

print(aplanar([1,2,3,[2,3],4,[5,6]]))
