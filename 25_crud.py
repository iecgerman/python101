# CRUD "Create, Read, Update & Delete"

"""
Métodos de las listas

append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
"""

import os
os.system('clear')

numbers = [1,2,3,4,5] # Create
print(numbers[1]) # Read
numbers[-1] = 10 # Update
print(numbers)

numbers.append(700)
print(numbers)

numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

task = ['todo 1', 'todo 2', 'todo 3']
new_list = numbers + task
print(new_list)

#para preguntar en que posicion esta un item
# print(new_list.index('todo 2'))
index = (new_list.index('todo 2'))
new_list[index] = 'todo changed'
print(new_list)

# delete
new_list.remove('todo 1')
print(new_list)

new_list.pop() # delete el ultimo elemento de la lista
print(new_list)
new_list.pop(0)
print(new_list)

# reverse
new_list.reverse()
print(new_list)

# sort
numbers_a = [1,4,6,3]
numbers_a.sort()
print(numbers_a)

strings = ['re','ab', 'ed']
strings.sort()
print(strings)

# sort no puede ordenar cuando tiene tipos de datos mezclados
# new_list.sort()