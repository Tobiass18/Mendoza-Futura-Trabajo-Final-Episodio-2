"""
# Ejercico N 1
numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))
suma = numero1 + numero2
print("La suma de los dos numeros es: " + str(suma))
# 
# Al intertar sumarlos se juntan, no se suman
"""
"""

# Ejercicio N 2
nombre = input("ingresa tu nombre: ")
edad = input("ingresa tu edad: ")
print("tu nombre es " + nombre + " y tienes " + edad + " años." )

# Ejercicio N 3
#codigo con error
nota1 = int(input("ingresa la primera nota: "))
nota2 = int(input("ingresa la segunda nota: "))
nota3 = int(input("ingresa la tercera nota: "))

promedio = nota1 + nota2 + nota3 / 3
print("el promedio de las tres notas es: " + str(promedio))
"""

# codigo sin error
nota1 = int(input("ingresa la primera nota: "))
nota2 = int(input("ingresa la segunda nota: "))
nota3 = int(input("ingresa la tercera nota: "))

promedio = (nota1 + nota2 + nota3) / 3
print("el promedio de las tres notas es: " + str(promedio))
