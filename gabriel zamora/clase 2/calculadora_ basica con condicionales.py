print(" Hola soy una calculadora personal: ")
print("La opcion que tengo son: ")
print("1_ sumar")
print("2_ restar")
print("3_ multiplicar")
print("4_ dividir ")
print("5_ potencia")
opcion = int(input("seleccione una opcion: "))
if opcion == 1 : 
    num1 = int(input("Ingrese el primer valor a sumar: "))    
    num2 = int(input("Ingrese el segundo valor a sumar: "))   
    suma = num1 + num2
    print(f" la suma de {num1} + {num2} = {suma}")
elif opcion  == 2: 
     num1 = int(input("Ingrese el primer valor a restar: "))
     num2 = int(input("Ingrese el segundo valor a restar: ")) 

     restar = num1 + num2
     print(f" la resta de {num1} - {num2} = {restar} ")

elif opcion  == 3: 
    num1 = int(input("Ingrese el primer valor : "))
    num2 = int(input("Ingrese el segundo valor: ")) 
    multiplicación = num1 * num2
    print(f"La multiplicación de {num1} * {num2} = {multiplicación}")
elif opcion  == 4:
    num1 = int(input("Ingrese el primer valor : "))
    num2 = int(input("Ingrese el segundo valor : "))
    if num2 == 0:
       print("ERROR NO SE PUEDE DIVIDITR POR CERO ")
    else:
        div = num1 / num2
        print(f"La división de {num1} * {num2} = {div}")
elif opcion  == 5:    
     num1 = int(input("Ingrese el primer valor : "))    
     num2 = int(input("Ingrese el segundo valor : "))
     potencia = num1 ** num2
     print(f"La multiplicación de {num1} . {num2} = {potencia}")
else:
    print("OPCION INCORRECTA, ADIOS")
    











