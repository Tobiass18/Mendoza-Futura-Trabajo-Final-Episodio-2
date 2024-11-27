num_secreto = 10 # Numero secreto = 10 es el numero a adivinar
num_ingresado = int(input("ingrese otro valor: ")) 

while num_ingresado != num_secreto: # Es un tipo de bucle que esta que no adivines el numero Secreto
 if num_ingresado < num_secreto: # Lo que hace es que si el numero ingresado es menor a el numero secreto te dice que es menor
    print("El numero ingresado es menor")
 elif num_ingresado > num_secreto: # Lo que hace es que si eliges un numero mayor a el numero secreto
   print(("El numero ingresado es mayor"))
   num_ingresado = int(input("Ingrese otro valor: "))

   print("Lo adivinaste")
