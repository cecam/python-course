# index() es un método incluído en todos los strings
# Su función es la de encontrár un caracter o substring dentro de una cadena
# sólo encuentra hasta la primer coincidencia

my_text = 'Este es un ejemplo'
# Esto retornará 4, ya que es sensible a mayúsculas y minúsculas
result = my_text.index('e')
print(f"Extrayendo por indice {result}")

# Se le pueden pasar más parametros, como un rango de inicio y uno de término
# También existe el método rindex
# hace lo mismo que index() pero busca la primer coincidencia de final a principio

# ---------------------------------------------------------------------------
# Método slicing  usado para extraer cadenas indicando el rango de caracteres y frecuencia de extracción

# Esto extraerá la primer palabra de la cadena total
fragment = my_text[0:4]
print(f"Extrayendo por rango {fragment}")

# ---------------------------------------------------------------------------
# Diccionarios
# Un objeto en JS
# entidad clave-valor, se usan para acceder a información sin conocer su posición
dictionary = {
    'c1': 'primer valor',
    'c2': 'segundo valor'
}

print(dictionary)

# Para acceder, es necesario indicar la posición/atributo por medio del nombre 
# pero con sintaxis de un arreglo/lista
print(dictionary['c1'])

# Ejemplo de consulta
dic = {'c1': ['a','b','c'], 'c2': ['d', 'e', 'f']}
print(dic['c2'][1].upper())

# ---------------------------------------------------------------------------
# Tuplas
# Las tuplas son lo mismo que una lista... pero inmutables
# su sintaxis esigual que una lista, pero entre paréntesis

# Para convertir una tupla a una lista para modificarla...
my_tuple = 1,2,3,4,5
new_tuple = list(my_tuple)

# ---------------------------------------------------------------------------
# Sets
# Los sets son lo mismo que una tupla... pero sólo admiten elementos únicos

# Para declararlos es necesario usar llaves o enviar una lista a una función set()
my_set = {1,2,3,4,5}

# Dentro de un set, no se pueden almacenar ni diccionarios ni listas, unicamente valores únicos o tuplas
# Tiene operadores como "len" o consultas de existencia (something in set)

# para fusionar sets se usa la función union()
my_new_set = {6,7,8,9}
last_set = my_set.union(my_new_set)

# Cuenta con la función "add" y "remove" para agregar o eliminar elementos
# en caso que se mencione uno ya existente, simplemente se ignora