# (I)

def maximo(a, b):
    return a if a > b else b

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
print(maximo(a, b))

# (II)

def maxt(x,y,z):
  return maximo(maximo(x,y), z)

x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
print(maxt(x, y, z))