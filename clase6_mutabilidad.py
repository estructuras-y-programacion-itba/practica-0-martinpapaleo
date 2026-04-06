nom = 'Ale'
print(type(nom))
print(nom.__class__)
print(isinstance(nom,str))

nom2 = nom # guardo a la direc de memoria de nom en nom2

print(id(nom), '', id(nom2))    # True
print(nom is nom2)              # True
print('-'*50)
a = [1,2,3]                     # dir a
b = [1,2,3]                     # dir b
print(a is b)                   # False porque tienen direcciones de memoria diferentes
print(a == b)                   # True porque compara los elementos del objeto
print('-'*50)
# MUTABILIDAD VS INMUTABILIDAD

# objeto mutable: se puede modificar despues de ser creado sin la necesidad de crear un nuevo objeto
# ej: listas, diccionarios, conjuntos.
# list, dict, set

# demostracion: 
print(id(a))
a.append(4)
print(id(a))

# objeto inmutable: no puede modificarse, si intentas cambiarlo, en realidad creas uno nuevo

print('-'*50)
x = 4
print(id(x))
x+=2 
print(id(x))