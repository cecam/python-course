# Print es una función utilizada para imrimir valores de cualquier tipo
# incluso utilizando operaciones, ya sean aritméticas, operaciones u otras funciones (en caso que devuelva un valor)
# Se utiliza para debuggear o mostrar información en consola

print('hola mundo')

## CADENAS

# Hablando de lo que se puede mostrar en el print, hablemos de cómo mostrar strings
# Se pueden expresar simplemente colocando el texto dentro de comillas simples o dobles ('' o "")
# Igualmente para expresar caracteres o acciones especiales, se identificarán comenzando con un \
# A continuación, un par de ejemplos:

# Esta impresion tendra un salto de linea
print('hola \n mundo ')

# Si por alguna razón quieres mostrar la barra invertida, esta es la forma
print('Esto es la barra interida \\')


## LEER DEL TECLADO

# Para leer información del teclado o información que da el usuario, se utiliza la función "input"

input('Dime tu nombre')
print(input('Dame tu apellido para mostrarlo: '))

print(input("Escribe tu nombre:")+" "+input("Escribe tu apellido:"))
