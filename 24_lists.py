import os
os.system('clear')

numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])

# mutacion
text = 'hola'
#text[0] = 'W' # los str son inmutables
# TIP: Nota importante: las listas se pueden modificar. Los strings no.

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3]) # solo lee 0 1 2
print(True in types)
print('hola' in types)
