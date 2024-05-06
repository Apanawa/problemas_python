"""
Description
Write a program that reads the item key of the item you're going to buy (note that it's
a capital letter) or X if you don't want to buy any more items.

The program must show on the screen the price corresponding to each item ordered, the
program must be repeated while the user does not type the code X, when the user types
the code X the program must show on the screen the total of the customer's purchase.

Key	Price
A	120
B	250
C	360
Example of program execution:
B

250

A

120

X

370

Input
A sequence of letters that represent the key of the item to be purchased. It must end 
with X which means that the purchase is finished.

Output
For each letter entered, the price of the corresponding item must be displayed. After 
the letter X is typed, the total of the chosen items should be displayed.

Example
Entrada	Salida
x        0

B        
B
A
C
B
X

Salida
250
250
120
360
250
1230
"""