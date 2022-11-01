def quant_list(n):
  xs = []
  x = 0
  count = 1
  y = 0
  i = 0
  for _ in range(n):
    xs.append(input("Digite um número para a lista: "))
    for _ in range(x):
      if xs[x] != xs[i]:
        y = 1
      else:
        y = 0
        break
      i += 1
    if y == 1:
      count += 1
    x += 1
    i = 0
  return count

n = int(input("Digite o tamanho da primeira lista: "))
print(quant_list(n))