"""
while True:
  print("si es veradero se va a ejecutar")
  break # usar break o presionar ctrl + c


counter = 0

while counter < 10:
  counter += 1  
  print(counter)


counter = 0
while counter < 20:
  counter += 1
  if counter == 15:
    break
  print(counter)
"""

counter = 0

while counter < 20:
  counter += 1
  if counter < 15:
    continue # imprime lo que este despues del 15
  print(counter)
