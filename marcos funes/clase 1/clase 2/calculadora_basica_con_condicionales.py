print("Hola soy una calculadora")
print("las opciones que tengo son: ")
print("1_SUMAR")
print("2_RESTAR")
print("3_multiplicación")
print("4_divisón")
print("5_potencia")
opcion = int(input("seleccione una opcion: "))
if opcion==1:
    num1 = int(input("ingresae el primer valor sumar: "))
    num2 = int(input("ingresas otro dato: "))
    suma = num1 + num2
    print(f"la resta de {num1} + {num2} = {suma}")
elif opcion==2:
    num1 = int(input("ingrasa el primer valor de la resta: "))
    num2 = int(input("ingresa el segundo valor de la resta: "))
    resta = num1 + num2
    print(f"la resta de {num1} - {num2} = {resta}")
elif opcion==3:
    num1 = int(input("ingresa el primer valor: "))
    num2 = int(input("ingresa el segundo valor: "))
    multiplicación = num1 * num2
    print(f"la multiplicacion de {num1} * {num2} = {multiplicación}")
elif opcion==4:
    num1 = int(input("ingresa el primer valor: "))
    num2 = int(input("ingresa el segundo valor: "))
    if num2 == 0:
        print("ERROR NO SE PUEDE DIVIDIR POR CERO")
    else:
        division = num1 / num2
        print(f"la multiplicacion de {num1} / {num2} = {division}")
elif opcion==5:
    num1 = int(input("ingresa el primer valor: "))
    num2 = int(input("ingresa el segundo valor: "))
    potencia = num1 ** num2
    print(f"la multiplicacion de {num1} ** {num2} = {potencia}")
else:
    print("OPCION INCORRECTAM, ADIOS")    