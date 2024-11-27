print("Hola soy un Registrador de Usuario")

nombre = input("ingrese su Nombre: ")
while nombre == "":
    nombre = input("ingrese su Nombre de nuevo: ")

apellido = input("ingrese su Apellido: ")
while apellido == "":
    apellido = input("ingrese su Apellido denuevo: ")

   
salir = True

Edad = int(input("ingrese su Edad: "))

while salir == True:

    if Edad > 0:
            if Edad < 100:
              
                salir = False
            else:
               
                Edad = int(input("ingrese su Edad denuevo: "))
    else:
            print("Edad incorrecta")
            Edad = int(input("ingrese su Edad denuevo: "))

correo = input("ingrese su Correo: ")
while correo == "":
    correo = input("ingrese su Correo de nuevo: ")


Fecha = input("ingrese su Fecha de nacimiento: ")
while Fecha == "":
    Fecha = input("ingrese su Fecha de nacimiento de nuevo: ")

