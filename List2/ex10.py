def suf_list(xs, ys):
  x = 0
  k = len(ys) - len(xs)
  for _ in range(len(xs)):
    if len(xs) <= len(ys):
      if xs[x] == ys[k]:
        x += 1
        k += 1
    else:
      return False
  return True if x == len(xs) else False

n = int(input("Digite o tamanho da primeira lista: "))
m = int(input("Digite o tamanho da segunda lista: "))
xs = []
ys = []

for _ in range(n):
  xs.append(input("Digite um número para a primeira lista: "))
for _ in range(m):
  ys.append(input("Digite um número para a segunda lista: "))
print(suf_list(xs, ys))