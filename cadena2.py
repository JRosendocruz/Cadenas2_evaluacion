
#Crear listas cadenaLarga
#crear listas caractere
#listas de estadisticas
#listas de totales
#recorrer cadenaLarga
#ir acumulando los valores de totales segun caracteres
#imprimir totales tomando los valores de las listas (estadisticas y totales)

cadenaLarga = """
Tu cadena larga de 5 párrafos aquí...
"""

letras = 'abcdefghijklmnñopqrstuvwxyz'
caracteres =['a','e','i', 'o','u', ' ', ',','.' ]
estadisticas = ['Total de caracteres:', 'Total de letras : ', 'Total de vocales a :', 'Total de vocales e :', 'Total de vocales i :', 'Total de vocales o :', 'Total de vocales u :', 'Total de espacios :', 'Total de comas:', 'Total de puntos:']
totales = [0] * len(estadisticas)

for char in cadenaLarga:
    totales[0] += 1  # Total de caracteres
    if char in letras:
        totales[1] += 1  # Total de letras
    if char in caracteres[0]:
        totales[2] += 1  # Total de vocales a
    elif char in caracteres[1]:
        totales[3] += 1  # Total de vocales e
    elif char in caracteres[2]:
        totales[4] += 1  # Total de vocales i
    elif char in caracteres[3]:
        totales[5] += 1  # Total de vocales o
    elif char in caracteres[4]:
        totales[6] += 1  # Total de vocales u
    elif char == ' ':
        totales[7] += 1  # Total de espacios
    elif char == ',':
        totales[8] += 1  # Total de comas
    elif char == '.':
        totales[9] += 1  # Total de puntos

print("Resumen de estadísticas:")
for i in range(len(estadisticas)):
    print(estadisticas[i], totales[i])  # Espacio corregido aquí
