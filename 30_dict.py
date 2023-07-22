person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['last_name']
person.pop('age') #con pop también podemos eliminar una llave en los diccionarios y en las listas pop() sin un argumento elimina el ultimo elemento de la lista

print(person)

# esto va a ser muy util posteriormente pero de una vez lo vimos
print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())