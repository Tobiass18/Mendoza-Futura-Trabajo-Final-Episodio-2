# VARIABLE: NOMBRE QUE ALMACENA EN SU MEMORIA UN DATO 
#las variables se escriben en formato sanke_case
# palabras en minusculas 
a = 3
print(a)
b = 2
print(b)
# + conector o conectar 
# int + int = int
# 2 + 3 = 5
c = a + b
print(c)
# Variable tipo String
nombre = "Valentina"
print(nombre)
apellido = "Vargas"
# Concatenar
#str + str = str
# Hola + Mundo = Hola Mundo 
nombre_completo = nombre + apellido
print(nombre_completo)
# Agregamos espacio 
# Opcion 1
nombre_completo = nombre+" "+ apellido
print(nombre_completo)
# Opcion 2
nombre = "Valentina"
nombre_completo = nombre + apellido
print(nombre_completo)

# verificar el tipo de variable 
print("la variable a es un:")
print(type(a))
print("la variable nombre_completo es un:")
print(type(nombre_completo))
