import random
separador=("*"*20) + "\n"
#creacion de una lista con elementos
list=[random.randrange(1,1001)for valor in range (10)]
print(type(list))
print(f"El primer elmento es {list[0]} y el ultimo es {list[1]}")
print(type(list))
print(separador)
#creacioon de lista]
lista_lista=[[random.randrange(1001)for valor in range (10)]for valor in range(5)]
print(lista_lista)
print(f"El primer elemento es {lista_lista[0][0]} y el ultimo es {lista_lista[4][9]}")
print (lista_lista[0])
for lista_interna in lista_lista:
    print(type(lista_lista))
print(type(lista_lista))

print("[")
for lista_primer_nivel in lista_lista:
    print("[", end="")
    for elemento in lista_primer_nivel:
        print(f"{elemento}", end ="\t")
        print("[", end="")
        print("")
print("[")
print(separador)

print(f"El primer elementos 0,2 es {lista_lista[0][2]}")
print(f"El elemento 2,7 es {lista_lista[2][7]}")
