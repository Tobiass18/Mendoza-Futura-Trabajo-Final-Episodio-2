# Variables: es un nombre que almacena un dato en la memoria 
#Las variables se escriben en formato snake_case
#Palabras en minuscula separadas con _
# Variable tipo INT
a= 3
print(a)
b= 2
print(b)
# CONECTOR/CONCATENAR
# INT + INT= INT
# 2 + 3 = 5
c = a + b 
print(c)
#vARIABLE TIPO STRING
nombre= "Marcos"
print(nombre)
apellido= "Funes"
print(apellido)
#cocatetenar
# str + str = str
# Hola + Mundo = Hola Mundo 
nombre_completo = nombre + apellido 
print(nombre_completo)
#Agregamos espacio 
#opción 1
nombre_completo = nombre+" " + apellido 
print(nombre_completo)
# Opción 2
nombre = "Marcos "
nombre_completo = nombre + apellido 
print(nombre_completo)
# Verificar el tipo de variable 
print("La variable a es un")
print(type(a))
print("la variable nombre_completo es un:")
print(type(nombre_completo))
