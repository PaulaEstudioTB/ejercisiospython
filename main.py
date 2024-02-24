#name         = input( 'Nombre(s): ')
#last_name    = input( 'Apellidos: ')
#full_name    = name +' '+ last_name
#phone_number = int( input( 'Número de teléfono: ') )
#email_addres = input( 'Correo electrónico: ')

#print('Hola '+ full_name + ', en breve recibirás un correo a: '+ email_addres)

#print('Hola!')
#users = input( '¿Cuantos usuarios desea registrar?' )
#for 

#print(users)

print('Hola, bienvenido!.')

#users = int(input( '¿Cuantos usuarios desea registrar?' ))
user_id = 1
data_user = {}
user_list = []

def new_user():

      users = int(input( '¿Cuantos usuarios desea registrar?' ))

      global user_id

      for usuario in range(users):

            name  = input('Nombre(s): ')
            while not(len(name) >= 5 and len(name) < 50): #5 < len(name) < 50
                  name = input ('vuelva a ingresar los datos:')
            
            last_name    = input( 'Apellidos: ')
            while not(len(last_name) >= 5 and len(last_name) < 50):
                  last_name = input ('vuelva a ingresar los datos:')

            phone_number = input( 'Número de teléfono: ')
            while len(phone_number) != 10: 
                  phone_number = input ('vuelva a ingresar los datos:')
            
            email_addres = input( 'Correo electrónico: ')
            while not(len(email_addres) >= 5 and len(email_addres) < 50): 
                  email_addres = input ('vuelva a ingresar los datos:') 
            
            #data_user.append ( [user_id, name, last_name, phone_number, email_addres] )
            # Ahora guardamos los datos en un Diccionario:
            data_user.update({
                  "ID" : user_id,
                  "Nombre" : name,
                  "Apellido" : last_name,
                  "Teléfono" : phone_number,
                  "Mail" : email_addres
            })

            # Sumamos el diccionario a una lista
            user_list.append(data_user.copy()) #Acá hacemos una copia del diccionario y lo agregamos a la lista

            user_id +=1  # usaer_is = user_id + 1

def show_user():
      id_user = int(input("Ingrese el ID del usuario que desea ver: "))

      usuario_encontrado = None

      for data_user in user_list:
            if data_user["ID"] == id_user:
                  usuario_encontrado = data_user
                  break
                  
      if usuario_encontrado is not None:
            print("Datos del usuario: ")
            for key, value in usuario_encontrado.items():
                        print(f"{key}: {value}")
      else:
            print(f"NO se encontró usuario con ID: {id_user}")

def edit_user():

# Modificar un usuario según el ID
      id_usuario = int(input("\nIngrese el ID del usuario que desea modificar: "))
      for user_data in user_list:
            if user_data["ID"] == id_usuario:
                  print("\nModificando usuario...")
                  # Solicitar al usuario que ingrese los nuevos datos
                  name = input("Ingrese el nuevo nombre del usuario: ")
                  last_name = input("Ingrese los nuevos apellidos del usuario: ")
                  phone = input("Ingrese el nuevo número de teléfono del usuario: ")
                  mail = input("Ingrese el nuevo correo electrónico del usuario: ")

                  # Actualizar los datos del usuario en el diccionario
                  user_data["Nombre"] = name
                  user_data["Apellido"] = last_name
                  user_data["Teléfono"] = phone
                  user_data["Mail"] = mail

                  print("\n¡Usuario modificado con éxito!")
                  print("\nNuevos datos del usuario:")

                  for key, value in user_data.items():
                        print(f"{key}: {value}")
                  
            else:
                  print(f"\nNo se encontró ningún usuario con el ID {id_usuario}")


def delet_user():
 # Eliminar un usuario según el ID
    id_usuario = int(input("\nIngrese el ID del usuario que desea eliminar: "))
    for data_user in user_list:
        if data_user["ID"] == id_usuario:
            print("\nEliminando usuario...")
            user_list.remove(data_user)
            print("\n¡Usuario eliminado con éxito!")
            break
        else:
            print(f"\nNo se encontró ningún usuario con el ID {id_usuario}")

def list_user():
      print("los usuarios registrado son:")
      for data_user in user_list:
            print("Datos de los usuarios:")
            for key, value in data_user.items():
                  print(f"{key}: {value}")
            print("---------------")

#--Inicia programa-----
new_user()


print (user_list)

# Itera sobre user_list y imprime los IDs de cada usuario registrado
print("Listado de IDs de usuarios registrados:")
for user_data in user_list:
      print(user_data["ID"])
      print("-----------------\n")
    
#print('Programa finalizado')
 

# -------------Menu de opciones-----------------
while True:
      option = input("\nQue desea hacer a continuación?:\nA - Agregar un nuevo Usuario\nB - Buscar un usuario por ID\nC - Modifificar un usuario\nD - Borrar usuario\nE - Listar usuarios\nF - Salir\n")

      #Procesamos la opcion seleccionada:
      if option == "A":
            new_user()
      elif option == "B":
            show_user()

      elif option == "C":
            edit_user()

      elif option == "D":
            delet_user()

      elif option == "E":
            list_user()
            
      elif option == "F":
            # Salir del programa
        print("\nSaliendo del programa...")
        break
      else:
        print("\nOpción no válida. Por favor, seleccione una opción válida.")


# ----------Fin de Menu de opciones-----------------


"""#listas = Estructurs de datos
#la buena practica es hacer listas cone l mismo tipo de dato,a  cad elemento le correponde un indice: simpre comienzan en 0
#            0   1      2         3              4
# my_lyst = [1, 3.14,'soy poly', True, [2, 14.3,'de nuevo yo', False] ]= #5
my_lyst = [int, float, 'strign', bool, [int, float, 'strign', bool ] ]"""
