numero = int(input("ingrese un numero positivo: "))
while numero <= 0:
    print("El numero debe ser posiivo ")
    numero = int(input("Intente denuevo: "))
    print(f"ingresaste un numero correcto: {numero}")