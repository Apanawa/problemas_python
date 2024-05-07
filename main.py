"""
Description
Suma dos números

Escribe un programa que pida al usuario dos números enteros, y luego muestre en la 
pantalla su suma.

Input
Dos números enteros, uno en cada renglón

Output
La suma de los dos números tecleados por el usuario

Example
Entrada	Salida
3
4
          7

"""
def suma_numeros():
          num1 = int(input())
          num2 = int(input())
          print(num1 + num2)

def main():
          suma_numeros()

main()