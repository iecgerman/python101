# indexing
text = "Ella sabe Python"
#       0123456789...  -1
print(text[0])
print(text[1])
# print(text[999]) #ArithmeticError
size = len(text)
print('size => ', size)
print(text[size - 1])
print(text[-1])

# slicing
print(text[0:5])
print(text[10:16])
print(text[0:10])
print(text[:10]) #forma abreviada
print(text[5:-1]) # sabe Pytho
print(text[5:]) 
print(text[:]) 
# saltos
print(text[10:16:1]) # Python
print(text[10:16:2]) # Pto
print(text[::2]) 
