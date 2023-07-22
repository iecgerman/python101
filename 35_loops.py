matriz = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

# que elemento se encuentra en la posicion cero 
print(matriz[0]) # [1, 2, 3]

print(matriz[0][1]) # 2

for element in matriz: #  [1, 2, 3]
                       #  [4, 5, 6]
                       #  [7, 8, 9]
  print(element)

print('----------------CICLOS ANIDADOS-----------------')
# CICLOS ANIDADOS
for element in matriz:
  print(element)
  for item in element:
    print(item)
"""
[1, 2, 3]
1
2
3
[4, 5, 6]
4
5
6
[7, 8, 9]
7
8
9
"""
for fila in matriz:
  print(fila)
  for columna in fila:
    print(columna)

