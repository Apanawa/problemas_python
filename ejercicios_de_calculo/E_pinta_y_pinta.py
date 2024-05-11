"""
Description
Un Pintor

Un pintor cobra $5.00 pesos por mt2 y quiere un programa para ayudarle a calcular la 
cantidad total a cobrar por cada cuarto que pinta dadas sus dimensiones (alto, ancho y 
largo). El programa debe considerar que el techo del cuarto también se pinta. Observa
que tienes que calcular el área de cada una de las paredes y del techo.

Por ejemplo: Si el cliente tiene un cuarto de 2.5 mt de ancho, 4 mt de largo y 2.8 mt de
altura El pintor debe cobrar 232 pesos

Input
El ancho, largo y altura del cuarto. Son 3 números flotantes, uno en cada línea.

Output
La cantidad de dinero que el pintor va a cobrar por pintar el cuarto. Es un número 
flotante.

Example
Entrada	Salida
3.2     271.3
4.3
2.7
"""
def pintor(ancho,largo,altura):
          paredes_ancho = ancho * altura
          paredes_largo = largo * altura
          techo = ancho * largo
          suma = paredes_largo + paredes_largo + paredes_ancho + paredes_ancho + techo
          print(suma*5)

def main():
          ancho = float(input())
          largo = float(input())
          altura = float(input())
          pintor(ancho,largo,altura)

main()
