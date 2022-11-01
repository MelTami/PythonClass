# (I)

def sqrt(n):
    k = 0
    while k**2 < n:
        k += 1
    return True if k**2 == n and n >= 0 else False

n = int(input("Digite um número: "))
print(sqrt(n))

# (II)

def lista_sqrt(n):
  x = 0
  count = 0
  for _ in range(n):
    x = int(input("Digite um número: "))
    if sqrt(x) == True:
      count += 1
  return count

n = int(input("Digite o tamanho da sequência: "))

print(lista_sqrt(n))