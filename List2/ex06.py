def lista_str(n):
  tamanho = 0
  for _ in range(n):
    x = input("Digite uma palavra: ")
    tamanho += len(x)
  return tamanho

n = int(input("Digite o tamanho da sequência: "))

print(lista_str(n))