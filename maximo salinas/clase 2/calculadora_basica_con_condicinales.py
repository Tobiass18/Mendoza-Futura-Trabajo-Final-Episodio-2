print("hola soy una calculadora")
print("las dos opciones qure tengo son: ")
print("1. sumar")
print("2. resta")
print("3. multiplicar")
print("4. dividir")
print("5., potencia")

a = int(input("seleccione una opcion: "))


if a == 1:
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    suma = num1 + num2  
    print(f"La suma es: {suma}")
elif a == 2:
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    resta = num1 - num2
    print(f"La resta es: {resta}")
elif a == 3:
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    multiplicacion = num1 * num2  
    print(f"La  multiplicacion es: {multiplicacion}")
elif a == 4:
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    if num2 == 0:
        print("no es posible dividir por cero")
    division = num1 / num2  
    print(f"La  division: {division}")
elif a == 5:
    num1 = int(input("ingrese el primer valor: "))
    num2 = int(input("ingrese el segundo valor: "))
    potencia = num1 ** num2  
    print(f"La  potencia es: {potencia}")

else:
        print("TOCASTE CUALQUIER OPCION")