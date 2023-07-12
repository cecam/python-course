# Al usuario se le pide un texto de cualquier magnitud, después se le solicitará al usuario que ingrese tres letras

# al final se le dará al usuario:
#  - cuántas veces aparece cada letra sin importar si es mayúscula o minusculas     x
#  - cuántas palabras hay en total                                                  x
#  - cuál es la primer y última letra del texto                                     x
#  - devolver el texto al revés                                                     x
#  - saber si "python" aparece dentro del texto                                     x

user_text = input('Ingresa un texto cualquiera: ')
user_text_cpy = user_text.lower()


# CONTEO DE CARACTERES
first_letter = input('ingresa una letra: ')
second_letter = input('ingresa una segunda letra: ')
third_letter = input('ingresa una última letra: ')

first_letter_count = user_text_cpy.count(first_letter.lower())
second_letter_count = user_text_cpy.count(second_letter.lower())
third_letter_count = user_text_cpy.count(third_letter.lower())


print(f"La primer letra aparece {first_letter_count} veces")
print(f"La segunda letra aparece {second_letter_count} veces")
print(f"La tercer letra aparece {third_letter_count} veces")


# CONTEO DE PALABRAS
print(len(user_text.split()))

# PRIMER Y ULTIMO CARACTER
print(f"El primer caracter es {user_text[0]}")
print(f"El último caracter es {user_text[-1]}")

# TEXTO AL REVES
print(user_text[::-1])

# APARECE PYTHON?
if('python' in user_text.split()):
    print('si aparece python')
else:
    print('nel prro, no sta python')