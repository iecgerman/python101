lives = 3
print(type(lives))
age = 12
budget = 100

temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = 12 + 15
print(lives)

lives = lives - 1
print(lives)

# forma pythonica para restar
lives -= 1
print(lives)

lives -= 5
print(lives)

lives += 5
print(lives)

number = 45000000000000000000000.1
print(type(number))
print(number) # 4.5e+22 <= Notación científica

number_b = 0.000000000000000001
print(number_b) # 1e-18 <= Notación científica

# reto de clase 10 - numbers

gastos_ene = input('Cuanto gastaste en Enero? $ ')
gastos_feb = input('Cianto gastaste en Febrero? $ ')
gastos_mar = input('Cuanto gastaste en Marzo? $ ')

# tenemos que convertirlos de str a int
gastos_ene = int(gastos_ene)
print(type(gastos_ene))
gastos_feb = int(gastos_feb)
print(type(gastos_feb))
gastos_mar = int(gastos_mar)
print(type(gastos_mar))

promedio = (gastos_ene + gastos_feb + gastos_mar) / 3

print(f'Tu promedio de gastos por mes es de:$ {round(promedio,4)}') # con el round podemos decirla a una variable cuantos decimales queremos despues del punto
print(type(promedio))