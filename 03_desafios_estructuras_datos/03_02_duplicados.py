
def duplicados(lista:list):
  out:list = []
  for ind, val in enumerate(lista):
    if val in lista[ind+1:]:
      out.append(val)
  return out

print(duplicados([2,3,7,6,5,3,2]))