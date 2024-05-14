"""
Descripción
Un grupo de amigos se reunieron para disfrutar 
 deliciosos muffins de chocolate y se los repartirán equitativamente, es decir, cada uno
 comerá la misma cantidad de muffins sin partirlos.

Repartir los pastelillos equitativamente permite que algunos de ellos sobren, por lo que
los amigos decidieron que le darán todos los muffins que sobren después de la 
repartición a Gil (uno de los integrantes del grupo) pues él adora los de chocolate.

Tu tarea es calcular cuántos muffins comerá Gil.

Entrada
Leerás un entero, 
, que representa la cantidad de muffins que tienen los amigos.

Luego leerás un entero, 
, que representa la cantidad de amigos que se reunieron a comer muffins
(incluyendo a Gil).

Salida
Un número entero, la cantidad de muffins que Gil comerá.

Ejemplo
Entrada 42 8
Salida 7
Si repartimos equitativamente, a cada quien le tocan 5 muffins. Así, de los 42 muffins
que habían sobran 2. Por lo tanto Gil se queda con 5 + 2 = 7 muffins.
"""

def calculo():
       muffins = int(input())
       amigos = int(input())
       equitativo = muffins // amigos
       resto = muffins % amigos
       print(resto + equitativo)

def main():
       calculo()

main()
