import math
#Ejercicio 1
salir = input("Desea empezar el primer reto S/N: ")

while salir != "N":
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))

    resultado = (num1 + num2) / 2
    print(resultado)

    salir = input("Desea volver a probarlo S/N: ")

print("Siguiente\n")

#Ejercicio 2

salir = input("\nDesea empezar el segundo reto S/N: ")

while salir != "N":
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))

    resultado = num1**num2
    print(resultado)

    salir = input("Desea volver a probarlo S/N: ")

print("Siguiente\n")

#Ejercicio 3

salir = input("\nDesea empezar el tercer reto S/N: ")

while salir != "N":
    num1 = int(input("Ingrese primer numero: "))

    resultado = math.sqrt(num1)
    print(resultado)

    salir = input("Desea volver a probarlo S/N: ")

print("Siguiente\n")

#Ejercicio 4

salir = input("\nDesea empezar el cuarto reto S/N: ")

while salir != "N":
    num1 = int(input("Ingrese primer numero: "))
    num2 = int(input("Ingrese segundo numero: "))

    resultado = math.sqrt((num1**2) + (num2**2))
    print(resultado)

    salir = input("Desea volver a probarlo S/N: ")

print("Siguiente\n")


# Ejercicio 5
def ejercicio5():
    rep = int(
        input("Ingrese el numero de veces q se repetira la palabra Hola: "))
    for x in range(0, rep):
        print("Hola")


#Ejercicio 6
def ejercicio6():
    for x in range(10,-1,-1):
        print(x)

#Ejercicio 7
def ejercicio7():
  filas = int(input("Ingrese numero de filas: "))
  for x in range(1,filas+1):
    for y in range(0,x):
      print("+",end="")
    print("")

ejercicio5()
print("\n")
ejercicio6()
print("\n")
ejercicio7()


#RETOS

def ejercicio8():
  edad = int(input("Ingrese la su edad: "))
  for x in range(1,edad + 1):
    print(x,end=" ")

def ejercicio9():
  num = int(input("\nIngrese numero: "))
  for x in range(1, num+1,2):
    print(x)

def ejercicio10():
  fact = 1
  num = int(input("\nIngrese numero: "))
  for x in range(1,num+1):
    fact = fact * x
  print(fact)

ejercicio8()
print("\n")
ejercicio9()
print("\n")
ejercicio10()