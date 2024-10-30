

print("Hola soy una calculadora")
print("Elegí la Operación que deseas realizar: ")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Potencia")
operacion = int(input("Ingresa el numero de operación: "))
if operacion == 1:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = numero1 + numero2
    print(f"El resultado de la suma es: {resultado}")
elif operacion == 2:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("ingresa el segundo numero: "))
    resultado = numero1 - numero2
    print(f"El resultado de la resta es: {resultado}")
elif operacion == 3:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = numero1 * numero2
    print(f"El resultado de la Multiplicacion es: {resultado}")
elif operacion == 4:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de la division es: {resultado}")
    else:
        print("Errorazo amigo, no se puede dividir sobre Cero")
elif operacion == 5:
    numero1 = int(input("Ingresa el primer numero: "))
    numero2 = int(input("Ingresa el segundo numero: "))
    resultado = numero1 ** numero2
    print(f"El resultado de la potencia de {numero1} elevado a {numero2} es : {resultado}")
else: 
    print("Errorazo, elegí otra opción")
    
