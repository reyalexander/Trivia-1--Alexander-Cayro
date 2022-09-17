#Libraries
import time
import random

#Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

puntaje = 50 # Puntaje inicial
iniciar_trivia = True  # Iniciamos la variable en True

# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(BLUE + "Bienvenido a mi trivia sobre computación")
print("Pondremos a prueba tus conocimientos")
print("Tienes", puntaje, "de puntaje")
# Agregaremos personalización para nuestros jugadores, preguntando y almacenando sus nombres en una variable

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

#Rules
print("\nEstas son las reglas del juego: ")
print("1. Cada que aciertes una pregunta iras sumando 10 puntos.")
print("2. Cada que falles una pregunta iras restando 10 puntos.")
print(
    "3. Existe una pregunta con una respuesta secreta que te otorgara de 80 a 100 puntox que sera un bonus si es que logras acertarle."
)
print(
    "4. Existen preguntas con valoracion distinta segun tengas un respuesta aproximada a la correcta."
)
print("5. Finalmente solo diviertete y disfruta de este pequeño juego.\n")

for x in range(1, 6):
	print(YELLOW + "  ", x, RESET)
	time.sleep(1)

print(
    "\nSi entendiste las reglas dale a 'Enter' para poder empezar con el juego."
)
continuar = input("")

# Es importante dar instrucciones sobre cómo jugar:
# Ahora, lo personalizaremos con el nombre del jugador, diciéndole a print() que muestre el contenido de la variable "nombre". Cada cosa distinta que queremos que muestre en la pantalla, la separamos con comas

while iniciar_trivia == True:

  print(BLUE+"\nHola %s %s responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n" % (nombre, apellido),RESET)
  
  # OJO, el \n al final de la línea 6 es para dar un "salto de línea"
  
  #This is a "Trivia", where you find a different questions
  
  # Pregunta 1
  print(GREEN+'¿En que año fallecio la Reina Isabel II?\n'+RESET)
  
  print('a) 2008')
  print('b) 2015')
  print('c) 2022')
  print('d) 2021')
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta: ").lower()
  
  while respuesta_1 not in ("a", "b", "c", "d"):
  	respuesta_1 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  #Validando respuesta correcta o incorrecta
  if respuesta_1 == "a":
  	print("Incorrecto!", nombre,
  	      ". Ese no fue el año, estas muy lejos del año.")
  	puntaje = puntaje / 2
  elif respuesta_1 == "b":
  	print("Incorrecto!", nombre, ". Ese no fue el año, estas un poco lejos.")
  	puntaje = puntaje - 5
  elif respuesta_1 == "c":
  	print("Correcto!", nombre,
  	      "lamentablemente este fue el año en que fallecio la Reina.")
  	print("\nGood luck %s !!! Go ahead" % nombre)
  	puntaje = puntaje * 2
  else:
  	print("Incorrecto!", nombre, ". Ese no fue el año, pero estas muy cerca.")
  	puntaje = puntaje + 5
  
  print("\nTu puntaje actual es :", puntaje)
  time.sleep(2)
  
  # Pregunta 2
  print(GREEN+'\n¿Quien descubrio la electricidad?\n'+RESET)
  
  print('a) Thomas Edison')
  print('b) Nicola Porcella')
  print('c) Michael Faraday')
  print('d) Nikola Tesla')
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: ").lower()
  
  while respuesta_2 not in ("a", "b", "c", "d", "x"):
  	respuesta_2 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  #Validando respuesta correcta o incorrecta
  if respuesta_2 == "a":
  	print(
  	    "Incorrecto!", nombre,
  	    ". El fue un famoso inventor, cientifico y empresario estadounidense.")
  	puntaje -= 10
  elif respuesta_2 == "b":
  	print("Incorrecto!", nombre,
  	      ". El es una personalidad de television y exfutbolista peruano.")
  	puntaje -= 10
  elif respuesta_2 == "c":
  	print(
  	    "Incorrecto!", nombre,
  	    ". El fue un científico británico que estudió el electromagnetismo y la electroquímica."
  	)
  	puntaje -= 10
  elif respuesta_2 == "x":
  	print("Respuesta secreta te ganaste 100 puntos")
  	print(
  	    "\nYa que obtuviste la respuesta secreta la respuesta correcta era la D."
  	)
  	print(
  	    "El fue un inventor, ingeniero eléctrico y mecánico serbio nacionalizado estadounidense, célebre por sus contribuciones al diseño del moderno suministro de electricidad de corriente alterna."
  	)
  	bonus = random.randint(80, 100)
  	print("Tu bonus es de ", bonus)
  	puntaje += bonus
  else:
  	print(
  	    "Correcto!", nombre,
  	    ". El fue un inventor, ingeniero eléctrico y mecánico serbio nacionalizado estadounidense, célebre por sus contribuciones al diseño del moderno suministro de electricidad de corriente alterna."
  	)
  	print("\nGood luck %s !!! Go ahead" % nombre)
  	puntaje += 10
  
  print("\nTu puntaje actual es :", puntaje)
  time.sleep(2)
  # Pregunta 3
  print(GREEN+'\n¿Quien pinto la ultima cena?\n'+RESET)
  
  print('a) Miguel Angel')
  print('b) Leonardo DiCaprio')
  print('c) Leonardo Da Vinci')
  print('d) Vincent Van Gogh')
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: ").lower()
  
  while respuesta_3 not in ("a", "b", "c", "d"):
  	respuesta_3 = input(
  	    "Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ").lower()
  
  #Validando respuesta correcta o incorrecta
  if respuesta_3 == "a":
  	print(
  	    "Incorrecto!", nombre,
  	    "El fue un arquitecto, escultor, pintor y poeta italiano renacentista")
  	puntaje -= 10
  elif respuesta_3 == "b":
  	print("Incorrecto!", nombre,
  	      "El es un actor, productor de cine y ambientalista estadounidense.")
  	puntaje -= 10
  elif respuesta_3 == "c":
  	print(
  	    "Correcto!", nombre,
  	    "El fue un polímata florentino del Renacimiento italiano. Fue a la vez pintor, anatomista, arquitecto, paleontólogo, botánico, escritor, escultor, filósofo, ingeniero, inventor, músico, poeta y urbanista."
  	)
  	print("\nGood luck %s !!! Go ahead" % nombre)
  	puntaje += 10
  else:
  	print(
  	    "Correcto!", nombre,
  	    "El fue un pintor neerlandés, uno de los principales exponentes del postimpresionismo. Pintó unos 800 cuadros y realizó más de 1600 dibujos."
  	)
  	puntaje -= 10
  
  print("\nTu puntaje actual es :", puntaje)
  time.sleep(2)
  
  #Ruleta de puntos
  #Este Pequeño juego sera muy random como un regalo y va a depender de tu suerte cuanto puedas obtener de puntos
  suma = 0
  for i in range(1,5):
    bonus = random.randint(1, 10)
    suma += bonus
  
  print("Tu bonus de puntos aleatorio es:",suma)
  puntaje += suma
  
  print(nombre, apellido, "Tu puntaje final es :", puntaje,
        ".Gracias por jugar mi trivia")

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()  

  time.sleep(2)
  
  if repetir_trivia != "si":  # != significa "distinto"
     print("\nEspero", nombre,"que lo hayas pasado bien, hasta pronto!")
     iniciar_trivia = False  # Cambiamos el valor de iniciar_trivia a False para evitar que se repita.
