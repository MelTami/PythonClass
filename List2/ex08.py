def lista_obj(n, y):
  lt = []
  eq = []
  gt = []
  for _ in range(n):
    x = input("Digite algo: ")
    if len(x) < len(y):
      lt.append(x)
    elif len(x) == len(y):
      eq.append(x)
    else:
      gt.append(x)
  return lt, eq, gt

n = int(input("Digite o tamanho da sequência: "))
y = input("Digite um objeto: ")

print(lista_obj(n, y))