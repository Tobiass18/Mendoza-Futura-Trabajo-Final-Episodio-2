def saludo():
    print("[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]")
    print("|                BIENVENIDO                  |")
    print("[~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~]")


saludo()

salir = True

precio = 0

while salir:
    print("Seleccionar la prenda: ")
    print("1. Pantalon")
    print("2. Remera")
    print("3. Campera")
    
    prenda = int(input("Ingresá el Numero: "))
    
    if prenda == 1:
        nombreprenda = "Pantalón"
        print("Seleccionaste Pantalón")
        print("El precio es de $20.000")
        precio = 20.000
        salir = False
        
    elif prenda == 2:
        nombreprenda = "Remera"
        print("Seleccionaste Remera")
        print("El precio es de $10.000")
        precio = 10.000
        salir = False
        
    elif prenda == 3:
        nombreprenda = "Campera"
        print("Seleccionaste Campera")
        print("El precio es de $30.000")
        precio = 30.000
        salir = False
        
    else:
        print("Volve a seleccionar una prenda valida")
        
cantidad = int(input("Ingresá la cantidad que vas a llevar: "))
while cantidad <= 0:
    cantidad = int(input("Volve a ingresar una cantidad valida: "))

cant = precio * cantidad 

print("¿Has venido aqui antes a comprar ropa?")
print("1. Sí")
print("2. No")

def descuento():
    precio_final = cant - (precio * 0.2)
    print(f"El total a pagar es ${precio_final * 1000}")
def no_descuento():
    precio_final = cant + (precio * 0.05)
    print(f"El total a pagar es ${precio_final * 1000}")

opcion = int(input("Selecione la respuesta: "))

salir_if = True

while salir_if:
    if opcion == 1:
        descuento()
        salir_if = False
    
    elif opcion == 2:
         no_descuento()
         salir_if = False
    
    else: 
        opcion = int(input("Responde correctamente: "))
    
    