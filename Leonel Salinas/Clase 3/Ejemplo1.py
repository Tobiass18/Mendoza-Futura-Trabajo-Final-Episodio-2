"""
Permite que un bloque de codigo se ejecute repititivamente mientras una condicion sea verdadera

while condicion:

mi condicion es una expresion booleana es decir True o False.
El bucle continuara repetiendoce mientras la condicion sea
Verdadera(True)

Ejemplo:
"""
contador = 0
while contador < 5:
    print(f"contador: {contador}")
    contador = contador + 1

"""
Iniciamos la variable del contador en "0", mientras sea menor que 5,
el bucle imprime el valor del contador, y le incremente 1.

El bucle se detiene cuando el contador llega a 5, ya que la condicion del contador < 5 no es verdadera
"""