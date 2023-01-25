def anagrama(first, second=[]):
  if first.__len__() == second.__len__():
    first = first.lower()
    second = list(second.lower())
    for cha in first:
      try:
        second.remove(cha)
      except:
        break
  return second.__len__() == 0

print(anagrama("Rama","amar"))