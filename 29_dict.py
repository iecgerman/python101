# [ ] = Listas
# ( ) = Tuplas
# { } = Diccionarios

my_dict = {}
print(type(my_dict))

my_dict = {
  'avion': "bla bla bla",
  'name': "Nicolas",
  'last_name': 'Molina Monroy',
  'age': 87
}

print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('unvalor'))# con get no meda error y me lanza un none para saber que no existe valor

print('avion' in my_dict)
print('carro' in my_dict)