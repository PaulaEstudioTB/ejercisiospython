# comentario

# nombre de la variable = valor
# los nombres de las variables llevas snake_case (todos klos caracteres en miniuscula) si hay mas de una palabra en el nopmbre se unen con _ guión bajo
# ejemplo: 
#first_name = 'Paula "Helena"' # String (es decir objetos o colección de caracteres y se pueden escribir con comillas simples o dobles, conviene estandarizar)
#last_name= 'Moscatelli'
#print(first_name)
#print(last_name)

#otra variable
#full_name = first_name + ' ' + last_name
#print(full_name)

#Tipos de datos int, float, string, bool
#age = 38
#puntaje = 5.5 
#activo = True

#print(activo)
#print(age)
#print(puntaje)

#type

#result = type(first_name)
#print(result)

#tipado dinámico
#f-string
# los string son inmutables
#docstring
"""el codigo
"""
#constantes en MAYUSCULA

#solicitar ingreso de datos mediante teclado

#result = input() #sinstringdamalaexperienciadeusuario
#print('Se ingreso por teclado:' + result)

#result = input('Ingresa tu texto aquí:') #stringcomoargumento
#print('Se ingreso por teclado:' + result)
#print( type(result) )

#funcion input con valores de otro tipo

name   = input('ingresa tu nombre: ')
age    = int( input('ingresa tu edad: ') )
score  = float( input('ingresa tu puntaje: ') )
active = input('¿el usuario se encuentra activo?:(si/no)') == 'si'

#malapráctica
#print(name)
#print(age)
#print(score)
#print(active)

#mediomalapractica
#age = int(age)
#score = float(score)

print(type(name),type(age),type(score),type(active))

#funciones int - float, reciben como argumento un string  y a aprtir de alli generan un valor entero o flotante
#OPERADORES RELACIONALES (==, !=, >, >= <, <=)