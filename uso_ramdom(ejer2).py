import random
Separador = ("*" * 15) + "\n"

print( f"Obteniendo un numero aleatorio que puede ir del 0 al 30 : {random.randrange(30)}")
print(Separador)
print(f"Obteniendo un numero entero aleatorio  del 2 al  30: {random.randrange (2,31,2)}")
print(Separador)
print(f"Obteniendo un valor numerico entre 0.0 y 1.0 : {random.random ()}")
print(Separador * 3)

listaPrueba =[ 10,30,15,45]
print(f"La lita de prueba es : {listaPrueba}")
print(f"El valor seleccionado aleatoriamente de la lista anterior es {random.choice(listaPrueba)}")
print(Separador)
random.shuffle(listaPrueba)
#"la funcion ramdon shuffle devuelve la secuencia pasada desordenada"
print(f"La lista desordenada es : {listaPrueba}")