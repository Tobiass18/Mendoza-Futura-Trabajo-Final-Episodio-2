#Variables -> un nombre que almacena en su memoria, un dato
#Las variables se escriben en formato snake case(Reemplazamos el espacio por guiones bajos)

#Variable tipo INT
a = 3
print(a)
b = 2
print(b)
#Conector / Concatenar
# int + int = int
# 2 + 3 = 5
c = a + b
print(c)

#Variable tipo STR
nombre = "Lautaro"
apellido = "Flores"
#Concatenar
# str + str = str
#Hola + Mundo = Hola mundo
nombre_completo = (nombre + " " + apellido)
print(nombre_completo)

# verificar eñ tipo de variable
print("La variable a es un: ")
print(type(a))

print("La variable nombre_completo es un: ")
print(type(nombre_completo))