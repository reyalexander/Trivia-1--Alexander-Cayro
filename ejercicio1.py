#Ejercicio 1
#Ingrese un numero cualquiera para saber si es positivo o negativo

x = int(input('Ingrese un numero: '))

if x < 0:
    print('El numero es negativo')
else:
    print('El numero es positivo')

#Ejercicio 2
#Ingrese un numero y lo multiplique por el mismo y te diga si es positivo o negativo

x = int(input('Ingrese un numero: '))

if x < 0:
    print(x * x)
    print('El numero es positivo')
else:
    print(x * x)
    print('El numero es positivo')

#Ejercicio 3
#Ingrese dos numeros e imprima el mayor

num1 = int(input('Ingrese numero 1: '))
num2 = int(input('Ingrese numero 2: '))

if num1 > num2:
    print('El numero mayor es ', num1)
else:
    print('El numero mayor es ', num2)

#Ejercicio 4
#Escriba una palabra y el numero de veces que quiera imprimirlas

word = input("Ingrese una palabra: ")
rep = int(input("Ingrese el numero de veces que se repetira: "))
x = 0
while x < rep:
    print(word)
    x = x + 1

#Ejercicio 5
#Imprima los 10 primeros numeros y cuando imprima el 3 imprima BOOM!
print("\n\n")
y = 0
while (y < 11):
    if y == 3:
        print("BOOM!")
    else:
        print(y)
    y = y + 1

#Ejercicio 6
#Escribir numero de filas y imprimir un triangulo

print("\n")
num_filas = int(input("Ingrese numero de filas: "))

for x in range(1, num_filas + 1):
  for y in range(x):
    print("+", end="")
  print("")


# Second way
num_fil =int(input("Ingrese numero de filas: "))
x = 0
while x <= num_fil:
  y = 0
  while y < x:
    print('+', end="")
    y = y + 1
  x = x + 1
  print("")