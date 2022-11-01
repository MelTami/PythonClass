# (I)

def primo(n):
  cont = 0
  mult = 0

  for count in range(2,n):
    if (n % count == 0):
        mult += 1
  return True if mult == 0 and n != 1 else False
n = int(input('Digite um número: '))
print(primo(n))

# (II)

def lista(n):
  x = 0
  count = 0
  for _ in range(n):
    x = int(input("Digite um número: "))
    if primo(x) == True:
      count += 1
  return count

n = int(input("Digite o tamanho da sequência: "))

print(lista(n))