def pascal(filas):
  if filas < 1:
    return {"respuesta":"Error"}
  triangulo:list = [[1]]
  for f in range(1,filas):
    filaT = [0]+triangulo[f-1]+[0]
    triangulo.append([])
    for pos in range(len(filaT)-1):
      triangulo[f].append(filaT[pos]+filaT[pos+1])
  return triangulo

print(pascal(1))
print(pascal(2))
print(pascal(5))
