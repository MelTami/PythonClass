def int_sqrt(n):
  x = 0
  lista_quad = []
  for _ in range(n):
    x = int(input("Digite um número: "))
    k = x**2
    lista_quad.append(k)
  return lista_quad

n = int(input("Digite o tamanho da sequência: "))
print(int_sqrt(n))