separador = ("*" * 15) + "\n"
#creacion de listas
#lista vaica
lista_vacia=list()
otra_lista=[]
lista1 =[1 , 2 , 3 , 4]
print(lista1)
print(separador)
pass#sirve como marcador de posicion

lista1.append(5)
print(lista1)
lista1.append((6,7))#una lista puede ser elemento de otra lista
print(lista1)
print(separador)
pass

#remover elementos de una lista
lista1.remove((6,7))
print(lista1)
print(separador)

#ordenar elementos
#sort
lista_origi=[3,4,2]
print(lista_origi)
lista_origi.sort()
print(lista_origi)
pass

#sorted
lista_or2=[23,10,30,5]
lista_ordenada=sorted(lista_or2)
print(f"La lista original = {lista_or2} , y la version ordenada es {lista_ordenada}")
print(separador)
pass

#compresion de listas
print(f"Lista original = {lista_origi}")

#sin compresion
lista1_al_doble=[]
for valor in lista1:
    lista1_al_doble.append(valor * 2 )
print(f"Lista resultante de cada elemento al doble = {lista1_al_doble}")
pass

#con compresion
lista1_al_doble =[valor * 2 for valor in lista1]
print(f"Mimos resultado pero con la compresion de listas ={lista1_al_doble}")
pass

#compresion pero con condicion
lista_valores_pares=[valor for valor in lista1 if (valor % 2 == 0)]
print(f"Solamente se agregan los elementos par : {lista_valores_pares}")
