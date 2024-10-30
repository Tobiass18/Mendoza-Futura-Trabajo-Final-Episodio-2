print("Hola soy una calculadora. Selecciona la operacion que desees realizar")
print("1_Suma")
print("2_Resta")
print("3_Multiplicar")
print("4_Dividir")
print("5_Potencia")

opcion=int(input("Selecciona una operacion: "))

if opcion==1:
    a=int(input("Introduce un valor: "))
    b=int(input("Introduca otro valor: "))
    c=a+b 
    print(f"El resultado de {a}+{b} es {c}")
elif opcion==2:
    a=int(input("Introdusca un valor: "))
    b=int(input("Introdusca otro valor: "))
    c=a-b
    print(f"El resultado de {a}-{b} es {c}")
elif opcion==3:
    a=int(input("Introdusca un valor: "))
    b=int(input("Introdusca otro valor: "))
    c=a*b
    print(f"El resultado de {a}x{b} es {c}")
elif opcion==4:
    a=int(input("Introdusca un valor: "))
    b=int(input("Introdusca otro valor: "))
    if b==0:
        print("Error, no se puede dividir por 0")
    else:
        c=a/b
        print(f"El resultado de {a}:{b} es {c}")
elif opcion==5:
    a=int(input("Introdusca el valor de la base: "))
    b=int(input("Introdusca el valor del exponente: "))
    c=a**b
    print(f"El resultado es {c}")