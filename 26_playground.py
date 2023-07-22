# Agrega, modifica y elimina elementos de una lista

letters = ['A', 'B', 'C', 'D', 'E', 'F']

# Agregar la letra G al final de la lista.
letters.append('G')
print(letters)

# Reemplazar la letra en la posición 0 con la letra Z.

# preguntar primero la posicion auque ya sabemos que es la 0
# print(letters.index('A')) 

index = (letters.index('A'))
letters[index] = 'Z' # letters[0] = 'Z'
print(letters)

# Eliminar la letra C de la lista.
letters.remove('C')
print(letters)

# Imprimir la lista resultante al revés.
letters.reverse()
print(letters)
