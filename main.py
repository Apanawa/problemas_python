"""
Description
Escribe un programa que lea un entero entre el 0 y 360 que representa los grados en el
plano Cartesiano y que muestre como resultado el número del cuadrante en el que se
encuentra.

En caso de que el grado se encuentre sobre un eje, su programa debe mostrar la palabra
"axis". En caso de que el grado sea menor que 0 o mayor que 360, su programa debe
desplegar la palabra "exceeds".

Por ejemplo:

Si la entrada es -10, la salida debe ser exceeds.

Input
Un entero que representa el número de grados.

Output
La palabra quadrant (en minúscula) seguida del número del cuadrante correspondiente
(por ejemplo: quadrant 2), o alguna de las palabras axis o exceeds.

Example
si el usuario teclea 215

el programa debe mostrar: quadrant 3

Entrada	Salida
-10     exceeds
90      axis
45      quadrant 1
"""
def cuadrante(angulo):
  if angulo < 0 or angulo > 360:
    print("exceeds")
  elif angulo == 90 or angulo == 180 or angulo == 270 or angulo == 0:
    print("axis")
  elif angulo > 0 and angulo < 90:
    print("quadrant 1")
  elif angulo > 90 and angulo < 180:
    print("quadrant 4")
  elif angulo > 180 and angulo < 270:
    print("quadrant 3")
  elif angulo > 270 and angulo < 360:
    print("quadrant 2")

def main():
  radio = float(input())
  cuadrante(radio)

main()