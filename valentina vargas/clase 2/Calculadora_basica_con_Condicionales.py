print("Hola soy una calculadora")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
print("5. potencia")

opcion = int(input("Seleccione una opcion: "))

if opcion == 1:
    a = int(input("Ingresa un dato: "))
    b = int(input("Ingresa un dato: "))
    suma = a + b
    print(f"la suma de {a} + {b} = {suma}")
elif opcion == 2:
    a = int(input("Ingresa un dato: "))
    b = int(input("Ingresa un dato: "))
    resta = a - b
    print(f"la resta de {a} - {b} = {resta}")
elif opcion == 3:
    a = int(input("Ingresa un dato: "))
    b = int(input("Ingresa un dato: "))
    c = a * b
    print(f"la multiplicacion da como resultado: {c}")
elif opcion == 4:
    a = int(input("Ingresa un dato: "))
    b = int(input("Ingresa un dato: "))
    if b == 0:
        print("no se puede divir por cero")
    c = a / b
    print(f"la division da como resultado: {c}")
elif opcion == 5:
    a = int(input("ingrese el dato: "))
    b = int(input("ingresa un dato: "))
    c = a ** b
    print(f"la potencia da como resultado: {c}")
    
else:
    print("INGRESASTE UNA OPCION INCORRECTA")
    
    







