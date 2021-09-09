import collections
separador= ("*" * 20 ) + "\n"

pila_lista=list()
for i in range(5):
    pila_lista.append(input("Dame el nombre a agregar: "))

#sacar elementos de la pila
while pila_lista:
    print(pila_lista.pop())
print(separador)

#una pila con deque permite agrefar y eleminar elementos
pila_deque=collections.deque()
for i in range(2):
    pila_deque.append(input("Dime el nombre a agregar: "))
#sacar elementos de la pila
while pila_deque:
    print(pila_deque.pop())
pass