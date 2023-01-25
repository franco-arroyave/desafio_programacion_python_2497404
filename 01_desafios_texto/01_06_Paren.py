import re

def val_par(cadena):
  par = re.sub("[^\(\)]","",cadena)
  while re.findall("\(\)",par):
    par = par.replace("()","")
  return par.__len__() == 0

print(val_par("(prue(=))al()"))