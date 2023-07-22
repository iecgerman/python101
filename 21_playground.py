# Identifica si un número es par o impar

"""
En este desafío, tienes una variable llamada number como string, tu reto es determinar si ese string es un número par o impar. Para hacer esta validación, debes transformar el string a number y luego realizar una condicional que compruebe si el número es divisible por dos. Si lo es, significa que el número es par y debes imprimir el mensaje Es par. Si no lo es, significa que el número es impar y debes imprimir el mensaje Es impar.

A continuación se muestran ejemplos de cómo debería funcionar tu solución:

Ejemplo 1:

Input: '2'
Output: "Es par"

Ejemplo 2:

Input: '3'
Output: "Es impar"
"""

number = '11'
print(number)

number = int(number)
print(type(number))

if number %2 == 0:
  print('El numero es par')
else:
  print('El numero es impar')