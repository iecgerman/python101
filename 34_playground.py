# Agrega solo los números positivos de una lista


numeros = [1, -1, 2, -2, 3, -3, 4, -4]
numeros2 = []

# Escribe tu solución 👇

for numero in numeros:
    if numero >= 0:
        numeros2.append(numero)

print(numeros2)

###########################

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for i in my_list:
  if i > 0:
    new_list += [i]

print(new_list)

#############################

my_list = [1, -1, 2, -2, 3, -3, 4, -4]

new_list = [e for e in my_list if e > 0]

print(new_list)