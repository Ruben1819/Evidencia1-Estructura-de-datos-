import datetime #libreria datetime en python
import time
sepadador= ("*" * 20 ) + "\n"
#aqui creamos una hora especifica
hora = datetime.time(7,20,25)
print(f"El tipo de objeto de la hora es :{type(hora)}")
print(f"La hora es{hora}")
print(f"La hora de {hora} es {hora.hour}")
print(f"El minuto de {hora} es {hora.minute}")
print(f"El segundo de {hora} es {hora.second}")
print(f"El microsegundo de {hora} es {hora.microsecond}")
print(sepadador * 3)

 #Aqui se determina la fecha
fecha = datetime.date.today()
print(f"El tipo de objeto de la fecha es {type(fecha)}")
print(f"La fecha actual es {fecha}")
print(f"El año actual es: {fecha.year}")
print(f"El mes es {fecha.month}")
print(f"El dia es {fecha.day}")
print (sepadador * 3)

#convertimos un string a fecha
fecha_tomada =input("Dame una fecha (dd/mm/aaaa) : \n")
fecha_procesada = datetime.datetime.strptime(fecha_tomada, "%d/%m/%Y").date()
print(type(fecha_tomada))
print(type(fecha_procesada))
print(f"La fecha capturada se transforma a {fecha_procesada}")
 #aritmetica de fechas basicas
cant_dia= int(input("Dime la cantidad de dias a adelantar :\n"))
nueva_fecha=fecha_procesada + datetime.timedelta(days = +cant_dia)
print(f"La nueva fecha es {nueva_fecha}")
print(sepadador)