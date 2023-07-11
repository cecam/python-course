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
