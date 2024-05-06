"""
Description
Escribe un programa que sea útil para determinar si los enteros X, Y y Z, dados por el usuario, son medidas correctas para los lados de un triángulo y si lo son, debe decir si es un Equilátero, Isósceles o Escaleno.

NOTA: X, Y y Z son los lados de un triángulo si cumplen con las siguientes condiciones:

*Todos los números son mayor que 0

*X + Y > Z

*X + Z > Y

*Y + Z > X

esto es, la suma de 2 de sus medidas debe ser estrictamente mayor que la tercera.

El triángulo equilátero tiene 3 lados iguales, el triángulo isósceles tiene 2 lados iguales y el triángulo escaleno tiene 3 lados diferentes.

Input
Tres enteros uno en cada línea.

Output
Cualquiera de las siguientes palabras: EQUILATERAL, ISOSCELES o SCALENE dependiendo del tipo de triángulo para los valores dados.

O la frase: IT IS NOT A TRIANGLE si los valores ingresados por el usuario no corresponden a los lados de un triángulo, esto es, no cumplen con las condiciones mencionadas anteriormente.

Escribe solo uno de los 4 mensajes permitidos usando mayúsculas exactamente como se indica.

Example
Entrada	Salida
2       IT IS NOT A TRIANGLE
3
9

3       EQUILATERAL
3
3

2       ISOSCELES
3
2
"""