name = "German"
last_name = "Garcia"
print(name)
print(last_name)

full_name = name + " " + last_name
print(full_name)

comillas1 = "I'm German"
print(comillas1)

comillas2 = 'She said "Hello" '
print(comillas2)

# format

age = 32
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name + " y tengo 32 años"
print('v1 =>', template)

template = 'Hola, mi nombre es {} y mi apellido es {} y tengo {} años'.format(name, last_name, age)
print('v2 =>', template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name} y tengo {age} años"
print('v3 =>', template)
