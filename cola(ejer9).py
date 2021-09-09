separador =("*" * 15 ) + "\n"
 
cola=list()
for cantidad  in range(4):
    nuevo=input("Nombre del recien llegado : ")
    cola.append(nuevo)

print(f"Se agregaron {len(cola)}  elementos: ")
for elemento in cola:
    print(elemento)
print(separador)
pass

print("Procedemos a eliminar")
while cola:
    print(cola.pop())
pass