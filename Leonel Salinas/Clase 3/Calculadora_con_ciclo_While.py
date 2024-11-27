print("Hola soy una calculadora Basica de python")
print("Elegí una de las operaciones a realizar: ")
# Opciones 
print("1_sumar")
print("2_Restar")
print("3_Multiplicar")
print("4_Dividir")
print("5_Potencia")
print("6_salir")

opcion = int(input("elige una opcion a realizar: ")) # Operaciones
if opcion == 1:   # Suma
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = a + b
    print(f"El resultado es: {c}")

elif opcion == 2:    # Resta
    a = int(input("Ingrese un numero  numero: "))
    b= int(input("ingrese el segundo numero: "))
    c = a - b
    print(f"El resultado es: {c}")


elif opcion == 3:    # Multiplicacion
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = a * b
    print(f"El resultado es: {c}")
     
elif opcion == 4: # Division
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    if b == 0:
        print("ERROR NO SE PUEDE DIVIDIR POR CERO")
    else :
        c = a / b
        print(f"El resultado es: {c}")
elif opcion == 5:    # Potencia
    a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    c = a ** b
    print(f"El resultado es: {c}")
else:
    print("OPCION INCORRECTA")
 

opcion = int(input("Ingrese una operacion: "))
opcion = int(input("Ingrese otro numero: "))
while opcion != opcion:
