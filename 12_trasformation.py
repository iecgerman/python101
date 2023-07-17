name = "German"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("German" + " Garcia")
print(10 + 20)
print("German" + "12")

age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}") # de esta forma no tenemos que usar la funcion str, format te hace en automatico la trasformacion

age = input("Escribe tu edad =>")
print(type(age))
age = int(age)
age += 10
print(f'Tu edad en 10 años sera {age}')