# Agrega, modifica y elimina elementos de un diccionario

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

# Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".

person['twitter'] = '@nicobytes'
print(person)

# Actualizar el valor del elemento con la llave "name" con el valor "Felipe".

person['name'] = 'Felipe'
print(person)

# Eliminar el elemento del diccionario con la llave "age".

# person.pop('age')
del person['age']
print(person)

# Imprimir una lista con las llaves del diccionario.

print(person.keys())
print(list(person.keys()))

# Imprimir una lista con los valores del diccionario.

print(person.values())
print(list(person.values()))