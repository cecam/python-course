name = input('Escribe tu nombre: ')
sales = int(input('Ventas totales del mes: '))

commission = round(sales * 13 / 100, 2)

print(f"Hola {name}, tus comisiones este mes son de ${commission}")


