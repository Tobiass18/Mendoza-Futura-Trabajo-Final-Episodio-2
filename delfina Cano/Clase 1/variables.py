#Variables (es un nombre que almacena en su memoria un dato)
#las variables se escriben en formato SNAKE_CASE(palabras en minuscula separadas por _)
a=3
print(a)
b=2
print(b)
# += Conector/Concatenar
#int+int=int
#2+3=5
c=a+b
print(c)
#variable tipo string
nombre="delfi"
print(nombre)
apellido="cano"
print(apellido)
#Concatenar
#str+str=str
#Hola+Mundo= Hola Mundo
nombre_completo=nombre+apellido
print(nombre_completo)
#agregamos espacios
#opcion 1 
nombre_completo=nombre+" "+apellido
print(nombre_completo)
#opcion 2
nombre_completo=nombre+ apellido
print(nombre_completo)
#verificar el tipo de variable
print("La variable a es un: ")
print(type(a))
print("La variable nombre_completo es un: ")
print(type(nombre_completo))