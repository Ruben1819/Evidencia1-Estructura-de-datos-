import math
separador = ("*" * 20 ) + "\n"

valorFlotante = float (input("Introduce un valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")
print(separador)
print(f"El siguiente entero hacia abajo de {valorFlotante} es {math.floor(valorFlotante)}")
print(separador)
print(f"La parte entera truncada de {valorFlotante} es {math.trunc(valorFlotante)}")
print(separador *3 )
pass
valorNum =int (input("Dame un valor entero :\n"))
print(f"La raiz cuadrada de {valorNum} es igual a {math.sqrt(valorNum)}")
print(separador)
print(f"El factorial de {valorNum} es igual a {math.factorial(valorNum)}")
print(separador)
potencia=int(input("Dame un valor entero:\n"))
print(f"El resultado de elevar {valorNum} a la {potencia} potencia es igual a {math.pow(valorNum,potencia)}")
print(separador * 2)
pass
print (f"El valor de pi es {math.pi}")