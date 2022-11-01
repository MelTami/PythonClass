def grow_list(xs):
  i = 0
  count = 1
  for _ in range(len(xs)):
    if xs[i] < xs[i + 1]:
      count += 1
    else:
      break
    i += 1
  return count

n = int(input("Digite o tamanho da primeira lista: "))
xs = []

for _ in range(n):
  xs.append(input("Digite um número para a lista: "))
print(grow_list(xs))
