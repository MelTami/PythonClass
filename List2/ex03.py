# (I)

def mdc(a, b):
  return a if not b else mdc(b, a % b)
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

print(mdc(a, b))

# (II)

def mmc(a, b):
  return (a * b) / mdc (a, b)

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))

print(mmc(a, b))