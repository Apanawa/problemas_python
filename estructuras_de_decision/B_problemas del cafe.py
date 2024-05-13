"""
En una cafetería venden 3 tipos de café.

Regular $30.00
Descafeinado $35.00
Cappuccino $ 50.00
Opcionalmente puedes hacer un combo por $30 más agregando una dona o una rebanada de 
pastel.

Escribe un programa en Python que pregunte por el tipo de café, y si se quiere o no 
hacer el combo.

Pregunta también cuántas órdenes iguales se van a comprar

El programa debe mostrar como valor de retorno el precio que pagará el cliente.

Input
El tipo de café (r – para regular y d – para descafeinado y c - para cappuccino)

La letra s o n para indicar si se quiere hacer combo.

La cantidad de órdenes que se van a comprar (que es un número entero)

Output
El total a pagar por el cliente

Entrada Salida
r       150
n
5

d       195
s
3
"""
def caja_registradora(tipo_de_cafe, combo, cantidad):
  total = 0
  eleccion = 0
  if tipo_de_cafe == "r":
    eleccion = 30
  elif tipo_de_cafe == "d":
    eleccion = 35
  elif tipo_de_cafe == "c":
    eleccion = 50
  if combo == "s":
    eleccion += 30
  total = cantidad * eleccion
  print(total)

def main():
  tipo_de_cafe = input()
  combo = input()
  cantidad = input()
  caja_registradora(tipo_de_cafe, combo, cantidad)

main()