import time
separador =  ("*"*15)
segundos =int(input("Cantidad de segundos a esperar : \n"))
time.sleep(segundos)  #aqui esperamos la cantidad de segundo introduccidos en la linea anterior
print(f"Han transcurrido {segundos} segundos")
print(separador)

print("Ahora inicaremos un proceso simulado")
horainicio = time.time()
for terminar in range (5):
    time.sleep(segundos)
print("Proceso simulado terminado")
duracion =time.time() - horainicio #aqui depende si se cambia la hora del sistema
print(f"La duracion fue de {duracion} segundos")