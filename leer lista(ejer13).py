import csv
columnas =('clave','nombre','correo')
datos=[[1,'Rodimiro','rod@hotmail.com']
       [2,'Teofilo',None],
       [3,'Ruben','ruben@hotmail.com']]
with open("datos.csv","w",newline="") as archivo:
    registrador=csv.writer(archivo)
    registrador.writerow(columnas)
    registrador.writerow(datos)

columnas=None
datos=list()

with open("datos.csv","r") as archivo:
    lector=csv.reader(archivo,delimiter=",")
    registros=0

    for clave,nombre,correo in lector:
        if registros==0:
            columnas=(clave,nombre,correo)
            registros=registros + 1
        else:
            clave=int(clave)
            datos.append([clave,nombre,correo])

print(datos)