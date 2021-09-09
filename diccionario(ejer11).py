#creacion de diccionarios
dicciona_vacio ={}
dicciona_cit={"Targtalia" : "Clima perfecto para una batalla",
               "Iron Man":"Yo soy Iron Man"}
print(dicciona_cit)
pass

#accesar elementos
print(dicciona_cit["Iron Man"])
pass

#agregar elementos
print("*"*20)
dicciona_cit["Barbatos"] = "dios anemo"
print(dicciona_cit)
pass

#eliminar elements de un diccionario
print("*"*20)
del dicciona_cit["Iron Man"]
print(dicciona_cit)
pass

#opciones para obtener el volcaco de un diccionario
print("*"*20)
print(list(dicciona_cit.keys()))
pass

#opcion 2,solamente los valores
print("*"*10)
print(list(dicciona_cit.values()))
pass

#opcion3 elemento por elemento
print("*"*10)
print(list(dicciona_cit.items()))
pass
