import math
lista1=[]
lista2=[]
x = int(input("introduce un número ") )
y = int(input("Introduce posible raiz primitiva") )
z = 1

for i in range (0,x-1,1):
  j=z+i
  p=int(math.fmod(y**j, x))
  lista1.append(p)
lista1.sort()
for j in range (1,x,1):
  lista2.append(j)

def iguales(lista1, lista2):
    for i in range(len(lista1)):
        if lista1[i]!=lista2[i]:
            return False
    return True
if (iguales(lista1, lista2)):
    print("Es raiz Primitiva: ")
else:
    print("No es Raiz Primitiva: ")
