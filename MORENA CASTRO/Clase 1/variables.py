#variables (es un nombre que almacena en su memoria un dato)
#las variables se escriben en formato SNAKE_CASE(palabras en minusculas separadas por _)
a=3
print(a)
b=2
print(b)
#+= Conector/Concatenar
#int+int=int
#2+3=5
c=a+b
print(c)
#varible tipo string
nombre="more"
print(nombre)
apellido="castro"
print(apellido)
#Concatenar
#str+str=str
#Hola+Mundo= Hola mundo
nombre_completo= nombre+apellido
print(nombre_completo)
#agregamos espacios
#Opcion 1
nombre_completo=nombre+" "+apellido
print(nombre_completo)
#Opcion 2
nombre_completo=nombre+apellido
print(nombre_completo)
#verificar el tipo de variable
print("la variable es un: ")
print(type(a))
print("la variable nombre_completo es un : ")
print(type(nombre_completo))