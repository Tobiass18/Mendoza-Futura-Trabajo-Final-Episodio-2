print("Hola soy una calculadora")
print("¿Que tipo de operación querés realizar?")
print("1_Suma")
print("2_Resta")
print("3_Multiplicacion")
print("4_Division")
print("5_Potenciación")
opcion = int(input("Escribí el tipo de operación que quieras: "))
if opcion == 1: 
 print("dea")
 dato1 = int(input("Ingresa el primer dato "))
 dato2= int(input("Ingresa el segundo dato "))
 suma = dato1 + dato2
 print(f"La suma de {dato1} + {dato2} = {suma}")
elif opcion == 2:
 dato1 = int(input("Ingresa el primer dato "))
 dato2= int(input("Ingresa el segundo dato "))
 resta = dato1 - dato2
 print(f"La resta de {dato1} - {dato2} = {resta}")
elif opcion == 3:
 dato1 = int(input("Ingresa el primer dato "))
 dato2= int(input("Ingresa el segundo dato "))
 multiplicación = dato1 * dato2
 print(f"La multiplicacion de {dato1} * {dato2} = {multiplicación}")
elif opcion == 4:
 dato1 = int(input("Ingresa el primer dato "))
 dato2= int(input("Ingresa el segundo dato "))
 division = dato1 / dato2
 print(f"La division de {dato1} / {dato2} = {division}")
elif opcion == 5:
 dato1 = int(input("Ingresa el primer dato "))
 dato2= int(input("Ingresa el segundo dato "))
 potenciacion = dato1 ** dato2
 print(f"La potencia de {dato1} ** {dato2} = {potenciacion}")
else:
    print("Pusiste una opción incorrecta")
    

