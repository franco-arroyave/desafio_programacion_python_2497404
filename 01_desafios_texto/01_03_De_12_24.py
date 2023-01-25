def doceto24(hora):
  hora = hora.lower().replace(" ","")
  hour = hora[:-2].split(":")[0]
  min = hora[:-2].split(":")[1]
  if (hora[-2:]=="pm"):
    return f'12:{min}' if hour == '12' else f'{int(hour)+12}:{min}'
  return f'00:{min}' if hour == '12' else f'{int(hour)}:{min}'

print(doceto24("12:30 am"))