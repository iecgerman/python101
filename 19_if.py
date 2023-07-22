import os
os.system('clear')

if True:
  print('Deberia de ejecutarse')

if False:
  print('Nunca se ejecuta')
  

pet = input('Cual es tu mascota favorita: ')

if pet == 'perro':
  print('genial eres todo un perro')
elif pet == 'gato':
  print('los gatos te protegen de espiritus malignos segun los egipcios')
elif pet == 'pez':
  print('quisiera ser un pez, para llenar de burbujas tu pecera')
else:
  print("no tienes ni perro, ni gato, ni pez")


"""
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')
"""
# RETO

numero = int(input('Digital un numero => '))
if numero %2 == 0:
  print('Tu numero es par')
else:
  print('tu numero es impar')
