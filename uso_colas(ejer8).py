import collections
separadpr = ("*" * 20) + "\n"

cola=collections.deque()  #cola utilizando deque
for cantidad in range (5):
    nuevo=input("Nombre del recien llegado: ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}, elementos: ")
for elementos in cola:
    print(elementos)
print(separadpr)
pass

print("Procederemos a quitarlos")
while cola:
    print(cola.popleft())
pass