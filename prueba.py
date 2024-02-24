#varibles para máximos y minimos
min_car = 5
max_car = 50
max_phone_digits = 10


#defino una función por si necesito reutilizar este bloque de código
def registrar_usuario():
    name = input("Ingrese el nombre del usuario: ")
    while not(len(name) > min_car and len(name) < max_car):
          name = input('Error ! el NOMBRE debe tener entre 5 y 50 caracteres. Ingrese de nuevo el nombre : ')

    last_name = input("Ingrese los apellidos del usuario: ")
    while not(len(last_name) > min_car and len(last_name) < max_car):
          last_name = input('Error ! el APELLIDO debe tener entre 5 y 50 caracteres. Ingrese de nuevo el apellido : ')

    phone = input("Ingrese el número de teléfono del usuario: ")
    while len(phone) != max_phone_digits:
          phone = input('Error ! el teléfono debe tener 10 caracteres. Ingrese de nuevo el teléfono : ')
    

    mail = input("Ingrese el correo electrónico del usuario: ")
    while not(len(mail) > min_car and len(mail) < max_car):
          mail = input('Error ! el MAIL debe tener entre 5 y 50 caracteres. Ingrese de nuevo el mail : ')
    return mail

# uso try/catch(except) para capturar errores
try:
    cantidad_usuarios = int(input("¿Cuántos usuarios desea registrar? "))
    if cantidad_usuarios <= 0:
            print("Por favor, ingrese un número válido de usuarios.")
     # iteramos N veces según el números de usuarios a ingresar    
    for i in range(cantidad_usuarios):
            print(f"\nRegistrando usuario {i+1}:")
            correo = registrar_usuario()
            print(f"¡Usuario {i+1} registrado con éxito!")
            print(f"Se enviará un mail de confirmación a {correo}")
except ValueError:
        print("Por favor, ingrese un número entero válido para la cantidad de usuarios.")

print(f"Se han registrado {cantidad_usuarios} usuario/s")