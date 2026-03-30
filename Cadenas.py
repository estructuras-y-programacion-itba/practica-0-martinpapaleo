"""CONSTANTES DEFINICAS EN EL MODULO
string.digits - '0123456789'
string.ascii_letters  - concatena las lower and upper case
string.ascii_lowercase  - 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase  'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.puntation - C: !" #$%&'()*+,-./:;<=>?@[\]^_`{|} ~.
string.whitespace  Todos los caracteres de la cadena son espacios en blanco, incluye tabuladores, salto de linea,  retorno, salto de página y tabulador vertical"""

# import string

# print(string.digits)
# print(string.ascii_lowercase)
# print(string.ascii_letters)
# print('a'in string.digits)
# print('a'in string.ascii_letters)
# print(type(string.ascii_uppercase))

# Metodo find
# retorna el indice donde aparece una primera ocurrencia en una busqueda de una subcadena en una cadena

frase= 'anita lava la tina'
#print(frase.find('i'))
# print(frase.find('la'))
# print(frase.find('la',8,10))

# # Metodo index
# # retorna el indice donde aparece una primera ocurrencia en una busqueda de una subcadena en una cadena
# print(frase.index('la'))
# print(frase.index('la',8,10))

# Metodo count
# Cuantas veces una subcadena esta en una cadena o frase

# print(frase.count('a'))
# print(frase.count('tina'))
# print(frase.count('la'))
# print(frase.count('la',8))

# Metodo replace
# reemplaza una subcadena en el texto dado por una nueva subcaneda y me duvuelve el texto reemplazado
# print(frase.replace('i','o'))
# print(frase)
# frase=frase.replace('i','o')
# print(frase)
# print(frase.replace('a','o',2))

# Metodo strip
#elimina los espacios en blanco que hay en las cadenas al principio y al final de ellas
# print(frase.strip())
# print(frase)

# # Metodo lstrip y rstrip
# print(frase.lstrip())
# print(frase.rstrip())

# Metodo split
# es que divide los elemenos de la frase y los almacena en una lista
print(frase.split())
lista=frase.split()
print(lista)

fecha='11/3/2022'
listafecha=fecha.split('/')
print(listafecha)

# Metodo join 
# permite volve a unir los elementos de una lista en una cadena

# frase1='.'.join(listafecha)
# print(frase1)
# print(type(frase1))

# # Metodos que permiten determinar si una cadena caracteres numericos alfabeticos alfanumericos
# # isdigit, isalpha, isdecimal , isupper
# print(frase)
# print(frase.isdigit())
# print(frase.isalpha())
numero='1199511'
print(numero.isdigit())

