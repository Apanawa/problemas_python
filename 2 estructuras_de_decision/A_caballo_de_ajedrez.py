"""
Description
Escribe un programa que indique si un caballo de ajedrez se puede o no mover a una
posición dada.

Las posiciones en el tablero se representan con dos números enteros del 1 al 8, el
primero para el renglón y el segundo para la columna.

Input
La posición(renglón, columna) actual del caballo en el tablero.

La posición (renglón, columna) a la que se quiere mover.

Output
El mensaje “Valid” o “Not Valid”

Example
Entrada Salida
5       Valid
4
3
3

5       Not Valid
6
3
4
"""
def caballo(r_i, c_i, r_f, c_f):
          if r_f == r_i + 2 or r_f == r_i - 2 and c_f == c_i + 1 or c_f == c_i - 1:
                    print("Valid")
          else:
                    print("Not Valid")

def main():
          r_i = int(input())
          c_i = int(input())
          r_f = int(input())
          c_f = int(input())
          caballo(r_i, c_i, r_f, c_f)

main()