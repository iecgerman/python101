"""
La variable element suele llamarse en referencia a lo que se está recorriendo y es donde se almacena dinamicamente elemento por elemento.

Si trabajamos con una lista de gatitos podrían llegar a ver

for gato in gatos:
	print(gato)
 
Donde se está iterando en la lista gatos y en cada iteración se almacena nuestro valor en la variable gato que se denota como singular.

¿Cúando usar “while” o “for” ?

while: cuando no nonozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.

for: cuando conozas la cantidad de elementos a recorrer o el número de iteraciones a relaizar.

for element in range(1, 21):
  print(element)

"""

my_list = [23, 45, 67, 89, 43]

for element in my_list:
  print(element)

my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
  print(element)

product = {
  'name': 'Camisa',
  'price': '100',
  'stock': 89
}

for llave in product:
  print(llave, "=>",product[llave])

# otra forma igual es:

for llave, value in product.items():
  print(llave, '=>', value)

people = [
  {
    'name': 'nico',
    'age': '34'
  },
  {
    'name': 'zule',
    'age': 45
  },
  {
    'name': 'santi',
    'age': 4
  }
]

for person in people:
  print('Nombre =>', person['name'], "Edad =>", person['age'])

print('-----------------------------DICT-----------------------------')
for person in people:
  print(person)
  
print('-----------------------------KEY NAME-------------------------')
for person in people:
  print('name:', person['name'])
  
print('-----------------------------KEY AGE--------------------------')
for person in people:
  print('age:', person['age'])
  
print('-----------------------------KEY AND VALUE--------------------')
for person in people:
  name = person['name'].capitalize()
  age = person['age']

  print(f'{name} es un estudiante de Platzi y tiene {age} años de edad')
  
print('-----------------------------KEY------------------------------')
for person in people[0].keys():
  print(f'Las llaves del PRIMER diccionario son: {person}')
  
print('-----------------------------VALUES---------------------------')
for person in people[0].values():
  print(f'los valores del PRIMER diccionario son: {person}')

print('-----------------------------ITEMS----------------------------')
for key, value in people[0].items():
  print(f'La llave es "{key}" y el valor es "{value}"')

# El bucle for en python … El bucle for se utiliza para recorrer los elementos de un objeto iterable (lista, tupla, conjunto, diccionario)

zoo = {
    'Leon': 8,
    'Jirafa': 5,
    'Hipo': 4,
}

for animal, cantidad in zoo.items():
    print(f'En el zoo tenemos el/la {animal} con una poblacion de {cantidad}')

# Mezclando cositas: sacar las mayusculas de un texto

texto = 'hola Gabriel. hoy vi a jUAn Y a elvira'
mayusculas = []
for i in texto:
  if i.isupper():
    mayusculas.append(i)
print (mayusculas)

# acortando con list comprehensions

texto = 'hola Gabriel. hoy vi a jUAn Y a elvira'
mayusculas =[i for i in texto if i.isupper()]
print(mayusculas)