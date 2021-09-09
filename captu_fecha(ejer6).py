import datetime
separador= "*" * 30
#capturaremos una lista de fechas de nacimiento
lista_fecha=[]
for elemento in range(3):
    fecha_cap=input("Dime una fecha (dd/mm/aaaa)  : ")
    fecha_proc= datetime.datetime.strptime(fecha_cap, "%d/%m/%Y").date()
    lista_fecha.append(fecha_proc)
print(separador)

lista_eda =[datetime.date.today().year - fecha.year for fecha in lista_fecha]
print(lista_eda)